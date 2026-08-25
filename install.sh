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
case ":$PATH:" in
  *":$BIN:"*) ;;
  *)
    say "  NOTE  $BIN is not on your PATH. Add this to your shell profile:"
    say "          export PATH=\"$BIN:\$PATH\""
    say ""
    ;;
esac

say "  next steps"
say "    ilana doctor                 verify the installation"
say "    ilana init --rigour 3        create .ilana/ in a project"
say "    ilana autoupdate --enable    keep it current automatically"
say ""
say "  in your coding agent, say:  use ilana"
say ""
