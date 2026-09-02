#!/usr/bin/env python3
"""
processar.py — transcreve gravações de aula com Whisper (Groq).

Uso:
    _Pipeline/.venv/bin/python _Pipeline/processar.py

O que faz sozinho:
  - lê GROQ_API_KEY do .env (parser próprio, sem dependência extra);
  - varre ../_Inbox/ (drop zone do projeto) e processa só o que ainda NÃO tem
    .txt em transcricao-bruta/;
  - converte cada arquivo para OGG/Opus mono 16 kHz 16 kbps;
  - se o .ogg passar de 24 MB, divide em partes de 1800 s e soma o offset
    real de cada parte (medido com ffprobe) aos timestamps;
  - transcreve via SDK groq (whisper-large-v3-turbo, pt, verbose_json),
    usando o glossario.txt como prompt (montado dentro do limite de ~224 tokens);
  - salva transcricao-bruta/<nome>.txt, uma linha por segmento: [HH:MM:SS] texto
    (staging pré-classificação — o edu-transcritor lê daqui, classifica a
    Estratégia, renomeia e arquiva em {Estratégia}/Transcrições/);
  - imprime progresso e apaga os temporários no fim.
"""

import os
import re
import sys
import glob
import json
import shutil
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
DIR_AUDIO = RAIZ.parent / "_Inbox"          # drop zone do projeto — fora de _Pipeline/
DIR_TRANSCRICAO = RAIZ / "transcricao-bruta"  # staging pré-classificação (edu-transcritor lê daqui)
DIR_TRABALHO = RAIZ / ".trabalho"   # temporários (ignorado pelo git)
ARQ_ENV = RAIZ / ".env"
ARQ_GLOSSARIO = RAIZ / "glossario.txt"

LIMITE_BYTES = 24 * 1024 * 1024      # acima disso, divide em partes
SEGMENTO_S = 1800                    # 30 min por parte
MAX_TOKENS_PROMPT = 224              # teto do campo prompt do Whisper
EXTS_AUDIO = {".m4a", ".mp3", ".mp4", ".wav", ".ogg", ".opus",
              ".aac", ".flac", ".m4b", ".mkv", ".mov", ".webm"}


# --------------------------------------------------------------------------- #
# .env — parser próprio (sem python-dotenv)
# --------------------------------------------------------------------------- #
def ler_env(caminho: Path) -> dict:
    dados = {}
    if not caminho.exists():
        return dados
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        chave, _, valor = linha.partition("=")
        chave = chave.strip()
        valor = valor.strip().strip('"').strip("'")
        if chave:
            dados[chave] = valor
    return dados


# --------------------------------------------------------------------------- #
# ffmpeg / ffprobe
# --------------------------------------------------------------------------- #
def rodar(cmd: list) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def duracao_segundos(caminho: Path) -> float:
    """Duração real de um arquivo, via ffprobe."""
    cp = rodar([
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(caminho),
    ])
    try:
        return float(cp.stdout.strip())
    except (ValueError, AttributeError):
        return 0.0


def converter_para_ogg(entrada: Path, saida: Path) -> None:
    cp = rodar([
        "ffmpeg", "-y", "-i", str(entrada),
        "-vn", "-ar", "16000", "-ac", "1",
        "-c:a", "libopus", "-b:a", "16k",
        str(saida),
    ])
    if cp.returncode != 0 or not saida.exists():
        raise RuntimeError(f"ffmpeg falhou ao converter {entrada.name}:\n{cp.stderr[-800:]}")


def dividir_em_partes(ogg: Path, destino: Path) -> list:
    """Divide o .ogg em partes de SEGMENTO_S segundos (-c copy). Retorna as partes ordenadas."""
    padrao = destino / f"{ogg.stem}_parte%03d.ogg"
    cp = rodar([
        "ffmpeg", "-y", "-i", str(ogg),
        "-f", "segment", "-segment_time", str(SEGMENTO_S),
        "-c", "copy", str(padrao),
    ])
    if cp.returncode != 0:
        raise RuntimeError(f"ffmpeg falhou ao segmentar {ogg.name}:\n{cp.stderr[-800:]}")
    partes = sorted(destino.glob(f"{ogg.stem}_parte*.ogg"))
    if not partes:
        raise RuntimeError(f"segmentação não gerou partes para {ogg.name}")
    return partes


# --------------------------------------------------------------------------- #
# Glossário -> prompt (dentro do orçamento de tokens)
# --------------------------------------------------------------------------- #
def carregar_glossario(caminho: Path):
    """Retorna (professores, vocabulario) onde vocabulario é lista de (temas:set, termos:list)."""
    professores, vocabulario = [], []
    if not caminho.exists():
        return professores, vocabulario
    secao = None
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        crua = linha.strip()
        if not crua or crua.startswith("#"):
            continue
        m = re.match(r"^\[(.+?)\]$", crua)
        if m:
            secao = m.group(1).strip().upper()
            continue
        if secao == "PROFESSORES":
            professores.append(crua)
        elif secao == "VOCABULARIO":
            if "=>" in crua:
                temas_txt, _, termos_txt = crua.partition("=>")
                temas = {t for t in temas_txt.split() if t}
            else:
                temas, termos_txt = {"*"}, crua
            termos = [t.strip() for t in termos_txt.split(",") if t.strip()]
            if termos:
                vocabulario.append((temas, termos))
    return professores, vocabulario


# Códigos curtos de tema no nome do arquivo -> arquivo de tema canônico em resumo/
ALIAS_TEMA = {
    "copy": "copy",
    "criativo": "criativos", "criativos": "criativos",
    "facebook": "facebook-ads", "facebookads": "facebook-ads", "fbads": "facebook-ads",
    "google": "google-ads", "googleads": "google-ads",
    "metrica": "metricas", "metricas": "metricas",
    "trafego": "gestao-de-trafego", "gestao": "gestao-de-trafego",
}

# Convenção: AAAA-MM-DD-tema[+tema]-prof[+prof]-NN  (data pode ser "sem-data").
_RE_NOME = re.compile(
    r"^(?P<data>\d{4}-\d{2}-\d{2}|sem-data)-(?P<temas>[^-]+)-(?P<profs>[^-]+)-(?P<nn>\d+)$"
)


def parse_nome_aula(stem: str) -> dict:
    """Extrai data, temas e professores do nome do arquivo, pela convenção."""
    m = _RE_NOME.match(stem)
    if not m:
        return {"reconhecido": False, "data": None, "data_indefinida": True,
                "temas": [], "professores": [], "ordem": None}
    indef = m.group("data") == "sem-data"
    temas = [ALIAS_TEMA.get(t.lower(), t.lower())
             for t in m.group("temas").split("+") if t]
    profs = [p.strip().capitalize() for p in m.group("profs").split("+") if p]
    return {
        "reconhecido": True,
        "data": None if indef else m.group("data"),
        "data_indefinida": indef,
        "temas": temas,
        "professores": profs,
        "ordem": m.group("nn"),
    }


def estimar_tokens(texto: str) -> int:
    """Estimativa conservadora (superestima) para não estourar o teto real do Whisper."""
    if not texto:
        return 0
    return int(len(texto) / 3.5) + texto.count(",")


def montar_prompt(nome_arquivo: str, professores, vocabulario) -> str:
    """Monta a dica priorizando nomes próprios e termos do tema do arquivo."""
    sinais = set(re.findall(r"[a-z0-9]+", nome_arquivo.lower()))

    def bate_tema(temas: set) -> bool:
        return bool(temas & sinais)

    # ordem de prioridade das linhas de vocabulário
    por_tema = [v for v in vocabulario if bate_tema(v[0]) and "*" not in v[0]]
    universais = [v for v in vocabulario if "*" in v[0]]
    resto = [v for v in vocabulario if v not in por_tema and v not in universais]

    termos_ordenados = []
    for _, termos in (por_tema + universais + resto):
        termos_ordenados.extend(termos)

    # cabeçalho fixo + nomes próprios (entram primeiro, sem serem cortados cedo)
    partes = ["Aula de marketing digital de resposta direta."]
    if professores:
        partes.append("Professores: " + ", ".join(professores) + ".")

    selecionados, vistos = [], set()
    for termo in termos_ordenados:
        chave = termo.lower()
        if chave in vistos:
            continue
        candidato = "; ".join(partes) + " Termos: " + ", ".join(selecionados + [termo]) + "."
        if estimar_tokens(candidato) > MAX_TOKENS_PROMPT:
            break
        vistos.add(chave)
        selecionados.append(termo)

    prompt = "; ".join(partes)
    if selecionados:
        prompt += " Termos: " + ", ".join(selecionados) + "."
    return prompt


# --------------------------------------------------------------------------- #
# Timestamps
# --------------------------------------------------------------------------- #
def hhmmss(segundos: float) -> str:
    s = max(0, int(round(segundos)))
    return f"{s // 3600:02d}:{(s % 3600) // 60:02d}:{s % 60:02d}"


# --------------------------------------------------------------------------- #
# Transcrição (Groq SDK)
# --------------------------------------------------------------------------- #
def transcrever(cliente, arquivo: Path, prompt: str):
    """Chama o Whisper e devolve a lista de segmentos (dicts com start/end/text)."""
    with open(arquivo, "rb") as fh:
        resposta = cliente.audio.transcriptions.create(
            file=(arquivo.name, fh.read()),
            model="whisper-large-v3-turbo",
            language="pt",
            temperature=0,
            response_format="verbose_json",
            prompt=prompt,
        )
    # a resposta pode vir como objeto ou dict, dependendo da versão do SDK
    if hasattr(resposta, "segments"):
        segs = resposta.segments
    elif isinstance(resposta, dict):
        segs = resposta.get("segments", [])
    else:
        segs = json.loads(resposta.model_dump_json()).get("segments", [])

    normalizados = []
    for s in segs:
        if isinstance(s, dict):
            normalizados.append((float(s.get("start", 0.0)), s.get("text", "")))
        else:
            normalizados.append((float(getattr(s, "start", 0.0)), getattr(s, "text", "")))
    return normalizados


# --------------------------------------------------------------------------- #
# Fluxo principal
# --------------------------------------------------------------------------- #
def pendentes() -> list:
    arquivos = []
    for caminho in sorted(DIR_AUDIO.iterdir()):
        if not caminho.is_file() or caminho.suffix.lower() not in EXTS_AUDIO:
            continue
        destino = DIR_TRANSCRICAO / f"{caminho.stem}.txt"
        if destino.exists():
            print(f"  - pulando (já transcrito): {caminho.name}")
            continue
        arquivos.append(caminho)
    return arquivos


def processar_um(cliente, entrada: Path, professores, vocabulario) -> None:
    print(f"\n=== {entrada.name} ===")
    trabalho = DIR_TRABALHO / entrada.stem
    if trabalho.exists():
        shutil.rmtree(trabalho)
    trabalho.mkdir(parents=True, exist_ok=True)

    meta = parse_nome_aula(entrada.stem)
    if meta["reconhecido"]:
        data_txt = "indefinida" if meta["data_indefinida"] else meta["data"]
        print(f"[meta] data={data_txt} · temas={', '.join(meta['temas'])} "
              f"· professores={', '.join(meta['professores'])} · ordem={meta['ordem']}")
    else:
        print("[meta] nome fora da convenção AAAA-MM-DD-tema-professores-NN "
              "(seguindo só com os sinais do nome)")

    prompt = montar_prompt(entrada.name, professores, vocabulario)
    print(f"[prompt ~{estimar_tokens(prompt)} tokens] {prompt}")

    ogg = trabalho / f"{entrada.stem}.ogg"
    print("[1/3] convertendo para OGG/Opus 16 kHz mono 16 kbps...")
    converter_para_ogg(entrada, ogg)
    tam_mb = ogg.stat().st_size / (1024 * 1024)
    print(f"      -> {ogg.name} ({tam_mb:.1f} MB)")

    # partes + offsets reais
    if ogg.stat().st_size > LIMITE_BYTES:
        print(f"[2/3] acima de 24 MB: dividindo em partes de {SEGMENTO_S}s...")
        partes = dividir_em_partes(ogg, trabalho)
        offsets, acumulado = [], 0.0
        for p in partes:
            offsets.append(acumulado)
            acumulado += duracao_segundos(p)
        print(f"      -> {len(partes)} partes (duração total {hhmmss(acumulado)})")
    else:
        print("[2/3] abaixo de 24 MB: parte única.")
        partes, offsets = [ogg], [0.0]

    print("[3/3] transcrevendo...")
    linhas = []
    for i, (parte, offset) in enumerate(zip(partes, offsets), start=1):
        print(f"      parte {i}/{len(partes)} (offset {hhmmss(offset)})...", flush=True)
        for start, texto in transcrever(cliente, parte, prompt):
            texto = texto.strip()
            if texto:
                linhas.append(f"[{hhmmss(start + offset)}] {texto}")

    destino = DIR_TRANSCRICAO / f"{entrada.stem}.txt"
    destino.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"      -> {destino.relative_to(RAIZ)} ({len(linhas)} segmentos)")

    shutil.rmtree(trabalho, ignore_errors=True)
    print("      temporários apagados.")


def main() -> int:
    env = ler_env(ARQ_ENV)
    api_key = env.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")
    if not api_key or api_key == "cole_aqui":
        print("ERRO: GROQ_API_KEY não encontrada no .env. Copie .env.exemplo para .env e preencha.")
        return 1

    for exe in ("ffmpeg", "ffprobe"):
        if shutil.which(exe) is None:
            print(f"ERRO: '{exe}' não encontrado no PATH.")
            return 1

    try:
        from groq import Groq
    except ImportError:
        print("ERRO: pacote 'groq' não instalado. Rode: .venv/bin/pip install groq")
        return 1

    DIR_TRANSCRICAO.mkdir(exist_ok=True)
    DIR_TRABALHO.mkdir(exist_ok=True)

    professores, vocabulario = carregar_glossario(ARQ_GLOSSARIO)
    print(f"Glossário: {len(professores)} professor(es), {len(vocabulario)} linha(s) de vocabulário.")

    fila = pendentes()
    if not fila:
        print("Nada a fazer: toda gravação em _Inbox/ já tem transcrição.")
        return 0
    print(f"A processar: {len(fila)} arquivo(s).")

    cliente = Groq(api_key=api_key)
    falhas = 0
    for entrada in fila:
        try:
            processar_um(cliente, entrada, professores, vocabulario)
        except Exception as e:  # noqa: BLE001
            falhas += 1
            print(f"!! ERRO em {entrada.name}: {e}")

    print(f"\nConcluído. {len(fila) - falhas} ok, {falhas} com erro.")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
