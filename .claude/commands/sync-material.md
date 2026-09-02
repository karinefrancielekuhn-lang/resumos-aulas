---
description: Sobe pro GitHub o material extra adicionado manualmente (material-fornecido/ e notas/) — add + commit + push num passo só.
---

# /sync-material — subir material extra pro GitHub

Este comando é pro lado "manual" do projeto: quando você (ou o colega) arrasta
PDFs, imagens ou outros arquivos extras das aulas pra `material-fornecido/`, ou
quando o agente `mentoria-guia` cria algo novo em `notas/`, esse comando manda
isso pro GitHub sem você precisar lembrar a sequência de comandos.

## Passo a passo

1. Rode `git status` e confira o que mudou. Se não houver nada em
   `material-fornecido/` ou `notas/` pra commitar, avise e pare — não invente
   commit vazio.
2. Rode `git add material-fornecido/ notas/` — **só essas duas pastas**. Nunca
   inclua `resumo/` ou `transcricao/` aqui: esse território é exclusivo do
   pipeline `processar.py` + `/resumir`.
3. Se houver mudança em outros arquivos fora dessas duas pastas (ex.:
   `resumo/`, código, configs), avise o usuário e pergunte antes de mexer —
   não é escopo deste comando.
4. Faça **um** commit descrevendo o que entrou, por exemplo:
   `materiais: 3 PDFs novos de copy + nota de checklist`.
5. Dê `git push` — **best effort**: se falhar (sem internet, autenticação
   pendente), avise o usuário mas não trave nem desfaça o commit. O commit
   local já está seguro; basta rodar `git push` depois.

## Regra de ouro

Antes de tudo isso, confirme que a working tree está sincronizada com o
remoto (`git pull` primeiro, se possível) — evita empurrar em cima de algo
que já mudou no GitHub enquanto você não olhava.
