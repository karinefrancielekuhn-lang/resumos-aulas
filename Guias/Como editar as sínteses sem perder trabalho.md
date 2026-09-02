---
title: "Como editar as sínteses sem perder trabalho"
type: guia
tags: [guia, obsidian, sintese]
---

# Como editar `_SINTESE-CONSOLIDADA.md` sem perder trabalho

Cada `_SINTESE-CONSOLIDADA.md` (em `{Estratégia}/Resumos/`) tem duas camadas:

1. **Síntese consolidada (topo)** — regravada por inteiro pelo Ithuel a cada aula nova.
   **Não edite à mão** — o que você digitar aí é perdido na próxima síntese.
2. **Registro por aula (embaixo)** — blocos `## Aula ... — ...`, append-only. Não edite
   blocos já existentes (perde fidelidade à transcrição).

## Onde colocar as SUAS anotações (preservado sempre)

- **Notas separadas:** crie outro arquivo `.md` na mesma pasta e use wikilinks
  (`[[_SINTESE-CONSOLIDADA]]`) para referenciar.
- **Seção própria no fim do arquivo:** adicione, ao final, uma seção que comece
  exatamente com `## Minhas anotações`. O Ithuel preserva essa seção sem alterar uma
  vírgula ao regravar a síntese.

> Herdado do pipeline original do projeto — a regra continua valendo na nova estrutura.
