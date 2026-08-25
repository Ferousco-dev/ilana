#!/bin/sh
# Minimal standalone update check for Ilana.
# Use when the full `ilana` CLI is not installed.
#
#   sh check-update.sh [remote-raw-url-of-VERSION]

set -eu

REPO_RAW="${1:-https://raw.githubusercontent.com/Ferousco-dev/ilana/main/VERSION}"
STATE_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/ilana"
LOCAL_VERSION_FILE="$(dirname "$0")/../../VERSION"

if [ ! -f "$LOCAL_VERSION_FILE" ]; then
  echo "ilana: cannot find local VERSION file" >&2
  exit 1
fi

local_version="$(tr -d ' \n' < "$LOCAL_VERSION_FILE")"

fetch() {
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL --max-time 10 "$1"
  elif command -v wget >/dev/null 2>&1; then
    wget -qO- --timeout=10 "$1"
  else
    return 1
  fi
}

remote_version="$(fetch "$REPO_RAW" 2>/dev/null | tr -d ' \n' || true)"

mkdir -p "$STATE_DIR"
date +%Y-%m-%d > "$STATE_DIR/last_checked"

if [ -z "$remote_version" ]; then
  echo "ilana: update check failed (offline or unreachable). local $local_version"
  exit 0
fi

if [ "$local_version" = "$remote_version" ]; then
  echo "ilana $local_version is current"
else
  echo "ilana $local_version installed, $remote_version available"
  echo "run: ilana update"
fi
