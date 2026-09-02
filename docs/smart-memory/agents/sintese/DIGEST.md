---
title: "DIGEST — sintese (Ithuel)"
kind: digest
type: overview
status: active
updated: 2026-09-02
tags: [digest, sintese]
---

# DIGEST — síntese (Ithuel / edu-sintetizador)

> Resumo vivo da área. Leitura obrigatória para o edu-sintetizador além do INDEX e stories ativas.

## Estado atual

- **Formato: um arquivo de síntese POR SUB-TÓPICO dentro de cada Estratégia**, não um
  único `_SINTESE-CONSOLIDADA.md` — decisão do usuário em 2026-09-02, para facilitar
  consulta como base de conhecimento. Cada arquivo mantém as duas camadas herdadas do
  `/resumir` do projeto antigo (síntese consolidada reescrita no topo + registro por
  aula append-only embaixo — ver `_Pipeline/reference/resumir-legado.md` para o
  framework completo: Ouro, marcação fato/opinião/testado, Consenso, Evoluiu,
  Perecível, Estável, Divergência entre professores, Lacunas).
- **`0 - Copywriting`**: `_SINTESE-CONSOLIDADA.md` (1 fonte, Bifi+Amanda) — tópico
  único, não precisou dividir.
- **`1 - VSL Google`**: dividido em `_SINTESE-COPY-E-PAGINAS.md` (aulas 01-03) e
  `_SINTESE-TRAFEGO-E-ESCALA.md` (aulas 04-09).
- **`2 - Organico Insta`**: dividido em `_SINTESE-FUNDAMENTOS-E-FUNIL.md` (aulas 01,
  11), `_SINTESE-INFRAESTRUTURA-E-CONTAS.md` (aulas 02-07, inclui a integração do
  guia externo do colega) e `_SINTESE-PRODUCAO-DE-CONTEUDO-IA.md` (aulas 08-10) —
  mais a nota companheira `_SINTESE-CRIATIVO.md` (princípios de criativo transversal,
  já existia separada).
- **`3 - DTC`**: `_SINTESE-CONSOLIDADA.md` (1 fonte, criativo pago) — tópico único.
- Todas as 4 Estratégias ativas (0, 1, 2, 3) têm síntese completa. Nenhuma passou por
  QA (Threll) ainda — próximo estágio do pipeline, não do Ithuel.
- **Critério para dividir por sub-tópico:** quando as aulas de uma Estratégia cobrem
  assuntos claramente distintos que alguém consultaria separadamente (ex.: "como
  configurar proxy" vs "como fazer copy de página") — divida. Quando é uma fonte só
  ou o conteúdo já é topicamente coeso, mantenha um arquivo. Cada arquivo linka os
  irmãos no topo (`> Escopo: ... ver também [[...]]`).
- Regra inviolável herdada: preservar qualquer seção `## Minhas anotações` no fim do
  arquivo, sem alterar, ao reescrever a síntese consolidada.

## Referências vivas (kind: reference)

| Nota | O que é |
|---|---|
| [[../../decisions/2026-09-02-migracao-taxonomia|Migração de taxonomia]] | Mapeamento tema→Estratégia + decisão de dividir sínteses por sub-tópico |
| `_Pipeline/reference/resumir-legado.md` | Framework completo de síntese do projeto antigo |

## Episódios

| Episódio | Status | Conclusão (summary) |
|---|---|---|
| Migração inicial (2026-09-02) | resolved | 4 arquivos de síntese migrados (copy, criativos-pago, criativos-organico, organico) sem alteração de conteúdo |
| Síntese VSL Google (2026-09-02) | resolved | 9 aulas da Laís sintetizadas do zero — Ouro, Consenso/Perecível/Estável/Divergência/Lacunas, registro por aula |
| Divisão por sub-tópico (2026-09-02) | resolved | VSL Google e Organico Insta divididos em 2 e 3 arquivos de síntese respectivamente, por pedido do usuário |
