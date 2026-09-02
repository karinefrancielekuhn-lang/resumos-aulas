---
title: "Convenções — Resumos-Aulas-Gold"
type: overview
agent: team-os-creator (bootstrap)
created: 2026-09-02
updated: 2026-09-02
tags: [project, conventions]
---

# Convenções

## Nomenclatura de áudio (entrada em `_Inbox/`)

Herdada do projeto antigo — carrega os metadados no nome do arquivo:

```
AAAA-MM-DD-<tema[+tema...]>-<professor[+professor...]>-NN.ext
```

Use `sem-data` no nome do arquivo **de entrada** (`_Inbox/`) quando a data real da aula
é desconhecida — é só um placeholder até o Kaelis processar. Temas e professores em
minúsculas, múltiplos separados por `+`. `NN` é a ordem sequencial.

## Nomenclatura de transcrição arquivada

```
AAAA-MM-DD (aula NN) - Professor - Tema.md
```

**Data real desconhecida → usar a data de transcrição** (dia em que rodou o
`processar.py`) no lugar de `AAAA-MM-DD`, e marcar isso explicitamente no campo `data`
do frontmatter (ex.: `"2026-09-02 (data de transcrição — gravação original sem data
real conhecida)"`). **Nunca deixe `sem-data` ou `indefinida` soltos no resultado
arquivado** — é convenção documentada, não invenção de dado. Frontmatter obrigatório:
`kind`, `status`, `professor`, `curso`, `tema`, `data`, `estrategia`.

## Síntese por Estratégia

Um ou mais arquivos `_SINTESE-{SUB-TÓPICO}.md` por Estratégia em `{Estratégia}/Resumos/`
— divida por sub-tópico quando as aulas cobrem assuntos distintos o bastante para
consulta separada (ver `docs/smart-memory/agents/sintese/DIGEST.md` para o critério).
Cada arquivo tem duas camadas: síntese consolidada (reescrita por inteiro a cada aula
nova, com Ouro/Consenso/Evoluiu/Perecível/Estável/Divergência/Lacunas) + registro por
aula (append-only, nunca reescrito). Preservar sempre uma eventual seção
`## Minhas anotações` no fim do arquivo.

## Frontmatter Obsidian

YAML no topo de toda nota nova; wikilinks `[[...]]` para navegação, nunca paths relativos
markdown (`[texto](../pasta/arquivo.md)`) — quebram quando a pasta é reorganizada.
