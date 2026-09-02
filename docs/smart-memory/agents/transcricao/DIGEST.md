---
title: "DIGEST — transcricao (Kaelis)"
kind: digest
type: overview
status: active
updated: 2026-09-02
tags: [digest, transcricao]
---

# DIGEST — transcrição (Kaelis / edu-transcritor)

> Resumo vivo da área. Leitura obrigatória para o edu-transcritor além do INDEX e stories ativas.

## Estado atual

- 21 aulas já transcritas e arquivadas na migração de 2026-09-02 (11 Gustavo Roque →
  `2 - Organico Insta`, 1 Bifi+Amanda → `3 - DTC`, 9 Laís → `1 - VSL Google`).
- Mecanismo de transcrição: `_Pipeline/processar.py` (Whisper via Groq), lê `_Inbox/`,
  escreve staging bruto em `_Pipeline/transcricao-bruta/`. Kaelis lê daqui, classifica,
  renomeia e arquiva em `{Estratégia}/Transcrições/`.
- Convenção de nome de áudio herdada do projeto antigo:
  `AAAA-MM-DD-<tema[+tema]>-<professor[+professor]>-NN.ext` (ou `sem-data-...` quando a
  data real é desconhecida).
- Glossário (`_Pipeline/glossario.txt`) tem 4 professores cadastrados: Bifi, Amanda,
  Gustavo Roque, Laís. Acrescentar novo professor aqui sempre que aparecer.
- `_Inbox/` deve ficar vazia ao final do trabalho do Kaelis — é a autoridade exclusiva
  sobre essa pasta.

## Referências vivas (kind: reference)

| Nota | O que é |
|---|---|
| [[../../decisions/2026-09-02-migracao-taxonomia|Migração de taxonomia]] | Mapeamento tema→Estratégia da migração inicial |
| [[../../../../../_INDEX - Aulas|_INDEX - Aulas]] | Índice geral de aulas e status |

## Episódios

| Episódio | Status | Conclusão (summary) |
|---|---|---|
| Migração inicial (2026-09-02) | resolved | 21 aulas migradas do projeto antigo; taxonomia por tema → por Estratégia |
