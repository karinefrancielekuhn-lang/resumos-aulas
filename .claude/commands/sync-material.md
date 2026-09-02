---
description: Sobe pro GitHub o material extra adicionado manualmente (Materiais/ de qualquer Estratégia e Notas/) — add + commit + push num passo só.
---

# /sync-material — subir material extra pro GitHub

Este comando é pro lado "manual" do projeto: quando você (ou o colega) arrasta
PDFs, imagens ou outros arquivos extras das aulas para a pasta `Materiais/` de
qualquer Estratégia (ex.: `1 - VSL Google/Materiais/`, `0 - Copywriting/Materiais/`),
ou quando o agente `edu-mentor` cria algo novo em `Notas/`, esse comando manda isso
pro GitHub sem você precisar lembrar a sequência de comandos.

## Passo a passo

1. Rode `git status` e confira o que mudou. Se não houver nada dentro de alguma
   pasta `Materiais/` ou em `Notas/` para commitar, avise e pare — não invente
   commit vazio.
2. Rode `git add` **só** nos caminhos que mudaram dentro de `*/Materiais/` (em
   qualquer Estratégia) e `Notas/`. Nunca inclua `*/Transcrições/`, `*/Resumos/`
   ou `_Pipeline/` aqui: esse território é exclusivo do pipeline
   `_Pipeline/processar.py` + squad `edu` (Kaelis/Ithuel/Sorae/Threll).
3. Se houver mudança em outros arquivos fora de `Materiais/`/`Notas/` (ex.:
   `Resumos/`, `Transcrições/`, configs), avise o usuário e pergunte antes de
   mexer — não é escopo deste comando.
4. Faça **um** commit descrevendo o que entrou, por exemplo:
   `materiais: 3 PDFs novos em 1 - VSL Google + nota de checklist`.
5. Dê `git push` — **best effort**: se falhar (sem internet, autenticação
   pendente), avise o usuário mas não trave nem desfaça o commit. O commit
   local já está seguro; basta rodar `git push` depois.

## Regra de ouro

Antes de tudo isso, confirme que a working tree está sincronizada com o
remoto (`git pull` primeiro, se possível) — evita empurrar em cima de algo
que já mudou no GitHub enquanto você não olhava.
