# Como usar — transcrição e resumo de aulas

Fluxo recorrente, toda vez que chegar uma aula nova:

## 1. Jogue a gravação em `audio/`

Copie o arquivo da aula para a pasta `audio/`. Aceita `.m4a`, `.mp3`, `.mp4`,
`.wav` e outros formatos comuns.

### Convenção de nome do arquivo (importante)

O nome carrega os metadados da aula. Formato:

```
AAAA-MM-DD-<tema[+tema...]>-<professor[+professor...]>-NN.ext
```

Exemplos:
- `2026-08-17-copy+criativos-bifi+amanda-01.m4a`
- `2026-08-24-facebookads+metricas-bifi-02.m4a`
- `sem-data-trafego-amanda-03.m4a`  ← quando não se sabe a data

Regras:
- **Data:** `AAAA-MM-DD`. Se não souber a data real da aula (ex.: arquivo copiado,
  cuja data do sistema é a de hoje), escreva `sem-data` — aí o `/resumir` registra
  a data como "indefinida" e usa só a ordem `NN`.
- **Temas:** use os **códigos curtos** abaixo, juntando vários com `+` (sem espaço).
  Uma aula pode alimentar vários temas.

  | código no nome | arquivo de tema em resumo/ |
  |---|---|
  | `copy` | copy.md |
  | `criativos` (ou `criativo`) | criativos.md |
  | `facebookads` (ou `facebook`, `fbads`) | facebook-ads.md |
  | `googleads` (ou `google`) | google-ads.md |
  | `metricas` | metricas.md |
  | `trafego` (ou `gestao`) | gestao-de-trafego.md |

  (Códigos sem hífen de propósito — o hífen é o separador de campos do nome.)
- **Professores:** nomes em minúsculas, juntando vários com `+` (ex.: `bifi+amanda`).
- **NN:** ordem sequencial da aula (`01`, `02`, ...).

O `processar.py` extrai data, temas e professores do nome automaticamente e os
imprime ao processar; o `/resumir` usa os mesmos campos para arquivar por tema.

## 2. Transcreva

```bash
.venv/bin/python processar.py
```

O script:
- processa só o que ainda **não** tem `.txt` em `transcricao/` (pode rodar de novo à vontade);
- converte o áudio, divide se for grande e transcreve com o Whisper (Groq);
- salva `transcricao/<nome>.txt`, uma linha por trecho no formato `[HH:MM:SS] texto`.

## 3. Resuma (dentro do Claude Code)

```
/resumir
```

Atualiza os resumos **por tema** (`resumo/copy.md`, `resumo/criativos.md`, ...).
Cada arquivo tem uma **síntese consolidada** no topo (reescrita a cada aula) e um
**registro por aula** empilhado embaixo (append only). O controle de o que já
entrou em cada tema fica em `resumo/_indice.md`.

---

## Manutenção do glossário

Quando aparecer um **professor novo**, acrescente o nome na seção
`[PROFESSORES]` de `glossario.txt`. Termos técnicos novos que o Whisper erre
podem ser somados nas linhas de `[VOCABULARIO]`.

## Configuração inicial (só uma vez)

- Ambiente: `python3 -m venv .venv && .venv/bin/pip install groq`
- Chave: copie `.env.exemplo` para `.env` e cole sua chave da Groq
  (console.groq.com > API Keys). O `.env` fica fora do git.
