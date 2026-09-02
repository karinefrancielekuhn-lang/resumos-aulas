# Como usar — transcrição e organização de aulas (Resumos-Aulas-Gold)

> **Migrado do projeto antigo (2026-09-02).** Este documento é a referência técnica
> do pipeline de transcrição. A camada de síntese por tema (`/resumir`) foi
> substituída pelo squad de agentes `edu` (Kaelis, Ithuel, Sorae, Threll) — ver
> `CLAUDE.md` na raiz do projeto. Este arquivo cobre só a parte que **não mudou**:
> transcrever áudio com Whisper/Groq.

Fluxo recorrente, toda vez que chegar uma aula nova:

## 1. Jogue a gravação em `_Inbox/` (raiz do projeto)

Copie o arquivo da aula para a pasta `_Inbox/` na raiz do projeto (não aqui em
`_Pipeline/`). Aceita `.m4a`, `.mp3`, `.mp4`, `.wav` e outros formatos comuns.

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
_Pipeline/.venv/bin/python _Pipeline/processar.py
```

(Rode da raiz do projeto, ou ajuste o caminho conforme onde você estiver.)

O script:
- processa só o que ainda **não** tem `.txt` em `_Pipeline/transcricao-bruta/`
  (pode rodar de novo à vontade);
- converte o áudio, divide se for grande e transcreve com o Whisper (Groq);
- salva `_Pipeline/transcricao-bruta/<nome>.txt`, uma linha por trecho no
  formato `[HH:MM:SS] texto` — é **staging**, ainda não classificado por
  Estratégia.

## 3. Classifique e arquive (squad `edu`, dentro do Claude Code)

Peça ao **edu-transcritor (Kaelis)** para processar `_Pipeline/transcricao-bruta/`:
ele identifica a Estratégia (`0` a `8`), renomeia com título coerente
(`AAAA-MM-DD - Professor - Tema.md`) e arquiva em `{Estratégia}/Transcrições/`.
Em seguida o **edu-sintetizador (Ithuel)** gera/atualiza a síntese consolidada
em `{Estratégia}/Resumos/_SINTESE-CONSOLIDADA.md` (mesmo formato de duas camadas
que o `/resumir` antigo usava — síntese no topo, registro por aula embaixo,
append-only). O **edu-bibliotecario (Sorae)** compila o que for copy cross-tema
em `0 - Copywriting/`, e o **edu-qa (Threll)** valida antes de marcar como
concluído. Ver `CLAUDE.md` na raiz do projeto e `docs/smart-memory/`.

---

## Manutenção do glossário

Quando aparecer um **professor novo**, acrescente o nome na seção
`[PROFESSORES]` de `glossario.txt`. Termos técnicos novos que o Whisper erre
podem ser somados nas linhas de `[VOCABULARIO]`.

## Configuração inicial (já feita na migração — só para referência)

- Ambiente: `python3 -m venv _Pipeline/.venv && _Pipeline/.venv/bin/pip install groq`
- Chave: `_Pipeline/.env` (copiada de `.env.exemplo`, sua chave da Groq —
  console.groq.com > API Keys). Fica fora do git.

## 4. Pergunte sobre o conteúdo (agente `edu-mentor`)

Este projeto tem um agente do Claude Code Agent Teams — `edu-mentor` — que lê todo
o acervo (`*/Resumos/`, `*/Transcrições/`, `*/Materiais/`, `_Pipeline/glossario.txt`,
`Guias/`) para responder perguntas cruzando Estratégias e professores, e criar
material derivado quando fizer sentido (guias de estudo, checklists, comparativos).

- Perguntas de conteúdo → ele lê e responde citando Estratégia/aula de origem.
- Pedidos de material novo (ex.: "monte um checklist de lançamento cruzando VSL e
  DTC") → ele escreve em **`Notas/`** (raiz do projeto) — pasta separada de
  `Resumos/` e `Transcrições/`, que continuam território exclusivo do pipeline
  `_Pipeline/processar.py` + squad `edu`. Isso evita conflito entre o que o agente
  cria e o que o Ithuel reescreve na próxima aula processada.
- Ative com Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` já fica ligado via
  `.claude/settings.json`) ou peça um subagente com esse papel numa sessão normal.

## Materiais fornecidos pelo professor

Diferente de `Transcrições/` (o que foi dito na aula) e `Resumos/` (a síntese) —
`{Estratégia}/Materiais/` é onde entra o material que o professor forneceu junto:
slides, PDF, planilha, swipe file. Não é gerado por transcrição; é colado manualmente.
Nomeie com a mesma referência de data/professor da aula, para rastrear a origem:

```
{Estratégia}/Materiais/<data-ou-sem-data>-<professor>-<descrição>.<ext>
```

## Sincronização com o GitHub (automática + manual)

- **Automática:** um hook `SessionStart` (`.claude/hooks/git-pull-auto.sh`) roda
  `git pull --ff-only` sozinho ao abrir/retomar uma sessão do Claude Code neste
  projeto — só quando a working tree está limpa. Se houver mudanças locais não
  commitadas, ele **pula o pull** e avisa, para nunca sobrescrever nada.
- **Manual:** continua funcionando normalmente, a qualquer momento: `git pull`.
- Nenhum agente do squad `edu` (nem o `edu-mentor`) dá `git push` (bloqueado por
  hook `block-git-push.sh`) — quem sobe pro GitHub é você, manualmente, ou via
  `/sync-material` (para Materiais/Notas) / commit do squad (para Resumos/Transcrições).

### Divisão entre computadores (Mac x Dell)

- **Mac:** fonte da estrutura de aulas — roda `processar.py` + squad `edu`, edita
  `*/Transcrições/` e `*/Resumos/`, e dá push.
- **Dell:** adiciona material extra das aulas manualmente em `{Estratégia}/Materiais/`
  e material derivado em `Notas/`. Depois de adicionar, rode `/sync-material` — sobe
  isso pro GitHub num passo só (add + commit + push), sem precisar lembrar a sequência
  de comandos.
- Regra para nunca dar conflito: **`git pull` antes de mexer em qualquer arquivo**, e
  commit + push logo depois de terminar — não deixar mudança pendurada por dias dos
  dois lados. O hook `git-pull-auto.sh` avisa disso a cada sessão.
- Arquivos/pastas diferentes nunca conflitam entre si. Só editar o *mesmo* arquivo nos
  dois computadores sem sincronizar entre uma edição e outra dá problema — evite isso.
