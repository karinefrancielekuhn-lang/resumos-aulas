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

Use `sem-data` quando a data real da aula é desconhecida. Temas e professores em
minúsculas, múltiplos separados por `+`. `NN` é a ordem sequencial.

## Nomenclatura de transcrição arquivada

```
AAAA-MM-DD (aula NN) - Professor - Tema.md
```

(ou `sem-data (aula NN) - ...` quando a data é desconhecida). Frontmatter obrigatório:
`kind`, `status`, `professor`, `curso`, `tema`, `data`, `estrategia`.

## Síntese por Estratégia

Um arquivo `_SINTESE-CONSOLIDADA.md` por Estratégia em `{Estratégia}/Resumos/`, com duas
camadas: síntese consolidada (reescrita por inteiro a cada aula nova, com Ouro/Consenso/
Evoluiu/Perecível/Estável/Divergência/Lacunas) + registro por aula (append-only, nunca
reescrito). Preservar sempre uma eventual seção `## Minhas anotações` no fim do arquivo.

## Frontmatter Obsidian

YAML no topo de toda nota nova; wikilinks `[[...]]` para navegação, nunca paths relativos
markdown (`[texto](../pasta/arquivo.md)`) — quebram quando a pasta é reorganizada.
