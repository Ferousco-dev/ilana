#!/bin/sh
# Ilana one-command installer.
#
#   curl -fsSL https://raw.githubusercontent.com/Ferousco-dev/ilana/main/install.sh | sh
#
# Clones the repository to ~/.ilana-src, symlinks the skill into every coding
# agent it can find, and puts `ilana` on your PATH.
#
# Environment:
#   ILANA_SRC     where to clone           (default ~/.ilana-src)
#   ILANA_BIN     where to put the CLI     (default ~/.local/bin)
#   ILANA_METHOD  link | copy              (default link)
#   ILANA_REPO    git URL                  (default the public repository)

set -eu

REPO="${ILANA_REPO:-https://github.com/Ferousco-dev/ilana.git}"
SRC="${ILANA_SRC:-$HOME/.ilana-src}"
BIN="${ILANA_BIN:-$HOME/.local/bin}"
METHOD="${ILANA_METHOD:-link}"

say()  { printf '%s\n' "$*"; }
die()  { printf 'install: %s\n' "$*" >&2; exit 1; }

command -v git >/dev/null 2>&1 || die "git is required"

say ""
say "  ilana - software engineering process for coding agents"
say "  ----------------------------------------------------"
say ""

if [ -d "$SRC/.git" ]; then
  say "  updating existing clone at $SRC"
  git -C "$SRC" fetch --quiet origin main
  git -C "$SRC" merge --ff-only origin/main >/dev/null 2>&1 \
    || say "  (local commits present; leaving as is)"
else
  say "  cloning into $SRC"
  git clone --quiet --depth 1 "$REPO" "$SRC" || die "clone failed"
fi

VERSION="$(tr -d ' \n' < "$SRC/VERSION" 2>/dev/null || echo unknown)"
say "  version $VERSION"
say ""

mkdir -p "$BIN"
ln -sf "$SRC/bin/ilana" "$BIN/ilana"
say "  cli      $BIN/ilana"

"$SRC/bin/ilana" install "--$METHOD" --all

say ""

# The CLI is optional (only `ilana update` and `ilana doctor` need it), but a
# missing PATH entry is the single most common install complaint, so be explicit
# about which file to edit rather than saying "your shell profile".
case ":$PATH:" in
  *":$BIN:"*)
    say "  path     $BIN is already on your PATH"
    ;;
  *)
    profile=""
    case "$(basename "${SHELL:-sh}")" in
      zsh)  profile="$HOME/.zshrc" ;;
      bash) [ -f "$HOME/.bash_profile" ] && profile="$HOME/.bash_profile" || profile="$HOME/.bashrc" ;;
      fish) profile="$HOME/.config/fish/config.fish" ;;
    esac

    say "  NOTE  $BIN is not on your PATH."
    say "        The skill itself works without it. Only \`ilana update\` and"
    say "        \`ilana doctor\` need the command."
    say ""
    if [ "$(basename "${SHELL:-sh}")" = "fish" ]; then
      say "        Run:  fish_add_path $BIN"
    elif [ -n "$profile" ]; then
      say "        Run:  echo 'export PATH=\"$BIN:\$PATH\"' >> $profile && exec \$SHELL"
    else
      say "        Add to your shell profile:  export PATH=\"$BIN:\$PATH\""
    fi
    say ""
    say "        Or use the full path:  $SRC/bin/ilana"
    ;;
esac

say ""
say "  next steps"
say "    1.  start a NEW session in your coding agent"
say "    2.  say:  use ilana"
say "    3.  answer the fork question: fleet of agents, or a single task"
say ""
say "  guide     $SRC/docs/USING.md"
say "  verify    $SRC/bin/ilana doctor"
say "  autoupdate $SRC/bin/ilana autoupdate --enable"
say ""
