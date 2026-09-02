---
title: "Migração do projeto antigo para taxonomia por Estratégia"
kind: reference
status: active
summary: "Projeto antigo (por tema) migrado para taxonomia por Estratégia (0-8); mapeamento de temas antigos para pastas novas registrado aqui."
created: 2026-09-02
tags: [decision, migracao, taxonomia]
---

# Migração do projeto antigo → taxonomia por Estratégia

**Contexto:** o projeto antigo (`_Projeto-Antigo/res/`, repo `resumos-aulas` no GitHub)
organizava tudo **por tema** (copy, criativos, organico, ...). O novo projeto organiza
**por Estratégia** de marketing (VSL Google, Organico Insta, DTC, ...), com uma pasta
`0 - Copywriting` para compilar copy cross-tema. Esta nota registra o mapeamento aplicado
em 2026-09-02, para que ninguém precise adivinhar "onde foi parar X".

## Mapeamento tema → Estratégia

| Origem (tema antigo) | Destino (Estratégia nova) | Motivo |
|---|---|---|
| `resumo/copy.md` | `0 - Copywriting/_SINTESE-CONSOLIDADA.md` | Copy é cross-tema por definição — é exatamente a função da pasta 0 |
| `resumo/criativos-pago.md` | `3 - DTC/Resumos/_SINTESE-CONSOLIDADA.md` | Decisão do usuário: DTC agrega Google Ads + Meta Ads, e o conteúdo (Bifi — Facebook/Google Ads, escala, contas/BM) é operação de criativo pago cross-plataforma |
| `resumo/criativos-organico.md` | `2 - Organico Insta/Resumos/_SINTESE-CRIATIVO.md` | Princípios de criativo transversais ao orgânico (única Estratégia orgânica ativa hoje) |
| `resumo/organico.md` | `2 - Organico Insta/Resumos/_SINTESE-CONSOLIDADA.md` | Conteúdo é 100% sobre tráfego orgânico (Gustavo Roque, non-shop) |
| `transcricao/2026-08-22-organico-gustavoroque-{01..11}.txt` | `2 - Organico Insta/Transcrições/` | Mesma aula/professor do organico.md |
| `transcricao/sem-data-copy+criativos-bifi+amanda-01.txt` | `3 - DTC/Transcrições/` | Aula dual-tema (copy + criativos); transcrição única fica em DTC (criativos-pago), copy linka de volta a partir de `0 - Copywriting` |
| `transcricao/sem-data-trafego-lais-{01..09}.txt` (9 áudios novos, 2026-09-02) | `1 - VSL Google/Transcrições/` | Conteúdo confirmado (BridgePage, VSL, lances Google Ads, Performance Max) — mentoria de tráfego para funil VSL no Google |
| `docs/GUIA-CELULAR-ZERO.md`, `docs/GUIA_OPERACIONAL_VENDAS_ORGANICAS.pdf` | `Guias/` (raiz) | Guias operacionais, não ligados a uma aula específica |
| `processar.py`, `glossario.txt`, `.env`, `.venv`, `INSTRUCOES.md` | `_Pipeline/` | Motor de transcrição — decoupled de `_Inbox/` (drop zone) |
| `.claude/commands/resumir.md` | `_Pipeline/reference/resumir-legado.md` | Lógica de síntese (Ouro, Consenso/Evoluiu/Perecível/Estável/Divergência/Lacunas, "Minhas anotações") preservada como referência — reimplementada nos agentes `edu-sintetizador` e `edu-bibliotecario` |
| `resumo/_indice.md` | `_Pipeline/reference/indice-legado.md` | Substituído por `_INDEX - Aulas.md` (raiz) na nova taxonomia |

## Pendências abertas (não resolvidas nesta migração)

- **Datas reais das aulas.** Várias datas são "indefinida" ou aproximadas (data de
  importação do arquivo, não da gravação) — herdado do projeto antigo. Se o usuário
  souber a data real de alguma aula, atualizar o frontmatter do arquivo de transcrição
  correspondente.
- **Nome oficial do curso/mentoria.** Nenhuma transcrição lida até aqui menciona o nome
  oficial do curso da Laís nem do Gustavo Roque — campo `curso` ficou vazio com TODO em
  cada transcrição. Não inventado, por regra do `edu-transcritor`.
- **Ordem das 9 aulas da Laís.** Inferida por timestamp de modificação do arquivo (mtime),
  não por conteúdo — os arquivos chegaram num intervalo de ~40 min, mtime pode não refletir
  a ordem real de gravação/aula. Confirmar com o usuário se a ordem 01-09 faz sentido.
- **`_Projeto-Antigo/` não foi apagado.** Todo o conteúdo relevante foi movido (não
  copiado) para a nova estrutura; o que resta em `_Projeto-Antigo/res/` (audio/ vazio,
  transcricao/ e resumo/ com os arquivos originais, .git próprio) é redundante com a nova
  estrutura e o histórico já importado para o `.git` da raiz. Fica como rede de segurança
  até o usuário confirmar e decidir remover.
- **Git:** o repositório da raiz agora carrega o histórico e o remote
  (`github.com/karinefrancielekuhn-lang/resumos-aulas`) do projeto antigo, por decisão
  explícita do usuário ("reaproveitar o repo antigo").

## Reconciliação com o push do Dell (mesmo dia, 2026-09-02)

Entre o commit de migração e o push, a esposa do usuário deu `git push` no Dell dela,
que ainda estava no projeto antigo — trouxe 3 commits com trabalho independente e
valioso: `material-fornecido/copy/*` (11 PDFs/imagens de research/swipe de copy),
`notas/` (pasta para conteúdo derivado sob pedido) e um agente ad-hoc `mentoria-guia`
+ comando `/sync-material` + hook `git-pull-auto.sh` (auto-pull no `SessionStart`) —
aparentemente construídos numa sessão anterior do team-os-creator sobre o mesmo
projeto, já seguindo o Native Teams Protocol.

Reconciliação feita via `git merge --no-commit --no-ff origin/main` + resolução manual:

| Origem (push do Dell) | Destino (taxonomia nova) | Motivo |
|---|---|---|
| `material-fornecido/copy/*.pdf`, `*.png` (11 arquivos) | `0 - Copywriting/Materiais/` | Material de copy, mesma lógica do mapeamento tema→Estratégia acima |
| `notas/_indice.md` | `Notas/_indice.md` | Pasta renomeada, mesmo conceito (conteúdo derivado, não gerado pelo pipeline) |
| `.claude/agents/mentoria-guia.md` | Promovido a agente oficial do squad `edu` no CT: `edu-mentor` (persona **Nyra**, Oráculo do Acervo) | Já seguia o Native Teams Protocol quase integralmente — só precisava apontar para a nova taxonomia (`*/Resumos/`, `*/Transcrições/`, `*/Materiais/` em vez de `resumo/`, `transcricao/`, `material-fornecido/`) |
| `.claude/commands/sync-material.md` | Mantido em `.claude/commands/sync-material.md`, paths adaptados para `*/Materiais/` + `Notas/` | Comando local do projeto, fora do escopo de propagação do CT |
| `.claude/hooks/git-pull-auto.sh` + registro em `.claude/settings.json` | Mantidos como estão — taxonomia-agnóstico | Útil para qualquer estrutura de pastas |
| `INSTRUCOES.md` (raiz, editado pelo Dell) | Conteúdo novo (seções sobre `mentoria-guia`/`git-pull-auto`/divisão Mac×Dell) incorporado em `_Pipeline/INSTRUCOES.md`, adaptado à nova taxonomia; arquivo da raiz permanece deletado (conflito modify/delete resolvido a favor da migração) | Evitar duas fontes de instrução divergentes |

**Fluxo Mac↔Dell daqui em diante:** Mac roda o pipeline de transcrição/síntese e dá
push; Dell adiciona `Materiais/` e pede notas à Nyra, sobe com `/sync-material`. Ver
`CLAUDE.md` (raiz) seção "Mac ↔ Dell".
