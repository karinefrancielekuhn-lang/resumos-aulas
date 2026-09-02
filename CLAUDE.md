# Resumos-Aulas-Gold

Base de conhecimento pessoal de aulas — transcrição, síntese temática e compilação de copy. **Não é uma codebase de software.** A partir de áudio/vídeo de aula, o projeto transcreve, organiza por Estratégia de marketing e produz resumos inteligentes por tema, servindo como base de conhecimento para outros projetos, repositório versionado em git (acesso da equipe) e vault de estudo individual via Obsidian.

**Fonte de verdade do processo:** `docs/smart-memory/project/overview.md` · **Índice de aulas (usuário):** `_INDEX - Aulas.md`

---

## Taxonomia — por Estratégia (não por tema)

```
0 - Copywriting/        ← compilado cross-tema de copy (mantido por Sorae)
1 - VSL Google/         ← Transcrições/ · Resumos/ · Materiais/
2 - Organico Insta/     ← Transcrições/ · Resumos/ · Materiais/
3 - DTC/                ← Google Ads + Meta Ads · Transcrições/ · Resumos/ · Materiais/
4 - Fundo de Funil/     ← placeholder (sem conteúdo ainda)
5 - Info App/           ← placeholder
6 - Organico TikTok/    ← placeholder
7 - Tabula/             ← placeholder
8 - Ecom Branding Equity/ ← placeholder
_Inbox/                 ← drop zone única para áudio/vídeo novo (esvazia ao ser processada)
_Pipeline/              ← motor de transcrição (Whisper via Groq) — ver _Pipeline/INSTRUCOES.md
Guias/                  ← guias de referência, não ligados a uma aula específica
```

## Pipeline (4 agentes, squad `edu`)

1. **Coloque** o áudio/vídeo em `_Inbox/`.
2. **Transcreva:** `_Pipeline/.venv/bin/python _Pipeline/processar.py` (Whisper/Groq) → staging em `_Pipeline/transcricao-bruta/`.
3. **Classifique e arquive** (Kaelis): identifica a Estratégia, renomeia coerentemente, arquiva em `{Estratégia}/Transcrições/`.
4. **Sintetize** (Ithuel): gera/atualiza `{Estratégia}/Resumos/_SINTESE-CONSOLIDADA.md` (duas camadas: síntese consolidada + registro por aula append-only).
5. **Compile e organize** (Sorae): copy cross-tema → `0 - Copywriting/`; mantém `_INDEX - Aulas.md` e a taxonomia de pastas.
6. **Revise** (Threll): veredicto PASS/CONCERNS/FAIL antes de marcar a aula como concluída.

---

## Smart-Memory Protocol

Este projeto mantém base de conhecimento em `docs/smart-memory/` (formato Obsidian).

**Todo agente, teammate ou sessão deve (leitura em camadas):**

1. Ao iniciar: ler `docs/smart-memory/INDEX.md` + `project/overview.md` + o `DIGEST.md` da sua área + as stories ativas — **nunca pastas inteiras**. Notas profundas só quando o INDEX/DIGEST/wikilink apontar.
2. Ao concluir: atualizar a nota viva in-place (nunca criar `-v2`/`-r3`) ou criar episódio com frontmatter completo (`kind`, `status`, `summary`) e refletir a linha no `DIGEST.md` da área.
3. Atualizar `INDEX.md` ao criar arquivos novos na smart-memory. Atualizar `_INDEX - Aulas.md` (raiz) ao processar qualquer aula — é a view voltada ao usuário.
4. **Nunca ler `docs/smart-memory/_archive/`** — conteúdo frio compactado.
5. A memória guarda **estado e decisões, não histórico narrativo**.

**Nota específica deste projeto:** `project/tech-stack.md` não existe — não é aplicável (não há stack de software). Ver [[decisions/2026-09-02-migracao-taxonomia]] para o mapeamento completo da migração do projeto antigo.

---

## Squad `edu`

| Agente | Persona | Papel | Autoridade |
|---|---|---|---|
| **edu-transcritor** | Kaelis | Organiza transcrições brutas, classifica Estratégia, renomeia e arquiva | Exclusiva sobre `_Inbox/` |
| **edu-sintetizador** | Ithuel | Resumos inteligentes por tema (síntese consolidada + registro por aula) | Fonte de verdade sobre "o que a aula ensina" |
| **edu-bibliotecario** | Sorae | Compila copy cross-tema (`0 - Copywriting`), mantém `_INDEX - Aulas.md` e a taxonomia de pastas | Exclusiva sobre a estrutura de pastas |
| **edu-qa** | Threll | Veredicto PASS/CONCERNS/FAIL antes de "pronto" | Exclusiva sobre veredicto de qualidade |

Comunicação é peer-to-peer via `SendMessage`, pelo nome do agente. **Nenhum agente spawna outros agentes** — nested teams são proibidos por spec.

## Regras invariantes

1. **Nada em `_Inbox/` fica sem classificação.** Se Kaelis não conseguir inferir Estratégia/professor/tema com segurança, ele pergunta — nunca adivinha.
2. **Não invente metadado.** Data desconhecida = "indefinida"/aproximada, nunca inventada. Nome de curso não identificado fica vazio com TODO, nunca inventado.
3. **Síntese preserva "## Minhas anotações"** — seção do usuário no fim de qualquer `_SINTESE-CONSOLIDADA.md`, nunca editada/movida/apagada ao regravar.
4. **Reorganizar nunca é apagar.** Mover, nunca deletar, ao remapear conteúdo entre pastas.
5. **`git push` exige confirmação explícita do usuário** — nenhum agente empurra para o remote por conta própria (o repositório reaproveita o histórico e o remote do projeto anterior).
