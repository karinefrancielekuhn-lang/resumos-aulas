---
title: "Visão Geral — Resumos-Aulas-Gold"
type: overview
agent: team-os-creator (bootstrap)
created: 2026-09-02
updated: 2026-09-02
tags: [project]
---

# Visão Geral — Resumos-Aulas-Gold

**Domínio / propósito:** Base de conhecimento pessoal de aulas. A partir de áudio/vídeo de aulas, o projeto organiza a transcrição, produz resumos inteligentes por tema e compila o conteúdo de copywriting de todas as estratégias num único lugar. Serve três públicos: (1) base de conhecimento para outros projetos, (2) repositório versionado em git compartilhado entre Mac e Dell (uso do usuário e da esposa), (3) estudo individual via Obsidian.

**Tipo:** Vault de conhecimento (não é um software tradicional) — squad customizado `edu` (ver [[../../../CLAUDE.md|CLAUDE.md]]).

## Taxonomia — por Estratégia

O projeto é organizado por **Estratégia de marketing**, não por tipo de conteúdo:

| Pasta | Estratégia | Status |
|---|---|---|
| `0 - Copywriting` | Compilado cross-tema de copy (mantido por Sorae/edu-bibliotecario) | ativa |
| `1 - VSL Google` | VSL para Google Ads | ativa |
| `2 - Organico Insta` | Orgânico Instagram | ativa |
| `3 - DTC` | DTC — inclui conteúdo de Google Ads **e** Meta Ads | ativa |
| `4 - Fundo de Funil` | reservada para conteúdo futuro | placeholder |
| `5 - Info App` | reservada | placeholder |
| `6 - Organico TikTok` | reservada | placeholder |
| `7 - Tabula` | reservada | placeholder |
| `8 - Ecom Branding Equity` | reservada | placeholder |

Cada pasta de Estratégia (1-8, quando ativa) contém `Transcrições/`, `Resumos/` e `Materiais/` — ver [[architecture]].

## Estado atual

- Estrutura de pastas criada (2026-09-02), squad `edu` (5 agentes) instalado.
- **Reconciliado com o push do Dell** (mesmo dia): materiais de copy (11 arquivos) e a
  pasta `Notas/` incorporados; agente ad-hoc `mentoria-guia` promovido a `edu-mentor`
  (Nyra) no CT. Ver [[decisions/2026-09-02-migracao-taxonomia]].
- `_Inbox/` — pasta única de drop de áudio/vídeo novo, aguardando processamento.
- `_Projeto-Antigo/` — staging do projeto anterior do usuário (estrutura antiga: copy / criativo-orgânico / criativo-tráfego-pago / orgânico), que serve de **referência e matéria-prima** para o `edu-bibliotecario` remapear na nova taxonomia por Estratégia. Conteúdo é movido, nunca apagado, com o mapeamento registrado em `decisions/`.
- Mecanismo de transcrição: `_Pipeline/processar.py` (Whisper via Groq) — migrado do projeto antigo, paths ajustados (`_Inbox/` → `_Pipeline/transcricao-bruta/`). Ver `_Pipeline/INSTRUCOES.md`.
- **Migração inicial concluída em 2026-09-02** — 21 aulas processadas: 11 (Gustavo Roque, orgânico) + 1 (Bifi/Amanda, copy+criativos) migradas do projeto antigo com síntese já existente; 9 (Laís, tráfego VSL Google) transcritas nesta sessão, síntese ainda pendente. Ver [[decisions/2026-09-02-migracao-taxonomia]] e [[../../../_INDEX - Aulas|_INDEX - Aulas]].
