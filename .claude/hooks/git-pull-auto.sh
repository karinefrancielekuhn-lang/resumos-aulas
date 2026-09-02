#!/usr/bin/env bash
# .claude/hooks/git-pull-auto.sh
# SessionStart hook — puxa atualizações do remoto automaticamente no início da sessão,
# sem nunca arriscar sobrescrever trabalho local.
#
# Como funciona:
# - Recebe via stdin o JSON do SessionStart: {"source":"startup|resume|clear|compact","cwd":"...",...}
# - Só age em source == startup | resume.
# - Working tree limpa + branch com upstream → `git pull --ff-only` (nunca merge/rebase;
#   se o histórico divergiu, aborta e avisa em vez de resolver sozinho).
# - Mudanças locais não commitadas → NÃO puxa, só avisa (evita conflito com trabalho em andamento).
# - Pull manual continua disponível a qualquer momento: `git pull` no terminal.

INPUT=$(cat)

json_field() {
  printf '%s' "$INPUT" | grep -o "\"$1\"[[:space:]]*:[[:space:]]*\"[^\"]*\"" | head -1 \
    | sed "s/\"$1\"[[:space:]]*:[[:space:]]*\"//;s/\"$//"
}

SOURCE=$(json_field "source")
CWD=$(json_field "cwd")

case "$SOURCE" in
  startup|resume) ;;
  *) exit 0 ;;
esac

[ -z "$CWD" ] && CWD="$PWD"
cd "$CWD" 2>/dev/null || exit 0

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

UPSTREAM=$(git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null)
[ -z "$UPSTREAM" ] && exit 0

emit() {
  ESC=$(printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g')
  printf '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"%s"}}\n' "$ESC"
}

if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
  emit "git-pull-auto: há mudanças locais não commitadas — pull automático pulado para não arriscar conflito. Rode 'git pull' manualmente depois de commitar ou guardar (stash) essas mudanças."
  exit 0
fi

BEFORE=$(git rev-parse HEAD 2>/dev/null)
if OUT=$(git pull --ff-only 2>&1); then
  AFTER=$(git rev-parse HEAD 2>/dev/null)
  if [ "$BEFORE" != "$AFTER" ]; then
    emit "git-pull-auto: repositório atualizado com o remoto (${BEFORE:0:7} -> ${AFTER:0:7})."
  fi
else
  emit "git-pull-auto: pull automático falhou (provável divergência de histórico com o remoto) — rode 'git pull' manualmente para resolver. Detalhe: $OUT"
fi
exit 0
