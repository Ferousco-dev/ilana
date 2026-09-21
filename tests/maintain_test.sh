#!/bin/sh
# Behavioural regression tests for the MAINTAIN mode instruments.
# Builds a throwaway git repository and exercises repo_map, evidence and privacy_scan.

set -eu

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
S="$ROOT/skill/instruments/scripts"
fail=0
ok()  { printf '  ok    %s\n' "$*"; }
bad() { printf '  FAIL  %s\n' "$*"; fail=$((fail + 1)); }
expect_rc() { # expected_rc description command...
  want="$1"; desc="$2"; shift 2
  set +e; "$@" >/dev/null 2>&1; rc=$?; set -e
  [ "$rc" -eq "$want" ] && ok "$desc" || bad "$desc (exit $rc, wanted $want)"
}

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cd "$TMP"
git init -q .
git config user.email t@example.com
git config user.name tester
mkdir -p cmd/app internal/store internal/api migrations
printf 'module example.com/app\n\ngo 1.22\n' > go.mod
printf 'package main\nimport _ "example.com/app/internal/api"\nfunc main() { _ = os.Getenv("APP_ADDR") }\n' > cmd/app/main.go
printf 'package api\nimport _ "example.com/app/internal/store"\nfunc h() { log.Printf("token=%%s", token) }\n' > internal/api/api.go
printf 'package store\n' > internal/store/store.go
printf 'CREATE TABLE users (id TEXT);\n' > migrations/0001_init.up.sql
printf 'mine\n' > preexisting.txt
git add -A
git commit -qm "chore: initial"
printf 'someone elses edit\n' >> preexisting.txt

printf '\nrepo map\n'
python3 "$S/repo_map.py" map --stdout > map.txt
grep -q 'internal/api.*-> internal/store' map.txt && ok "package import edges" || bad "package import edges"
grep -q 'tables: users' map.txt && ok "data ownership tables" || bad "data ownership tables"
grep -q 'APP_ADDR' map.txt && ok "environment variables" || bad "environment variables"
grep -q 'preexisting.txt\|(1 paths)' map.txt && ok "uncommitted work reported" || bad "uncommitted work reported"

printf '\nscope guard\n'
expect_rc 2 "guard without baseline exits 2" python3 "$S/repo_map.py" guard
python3 "$S/repo_map.py" snapshot --allow "internal/**" >/dev/null
printf 'package store\nvar x = 1\n' > internal/store/store.go
expect_rc 0 "in-scope change passes the guard" python3 "$S/repo_map.py" guard
printf 'stray\n' > stray.txt
expect_rc 1 "out-of-scope new file fails the guard" python3 "$S/repo_map.py" guard
rm stray.txt
printf 'clobbered\n' > preexisting.txt
expect_rc 1 "modifying pre-existing dirty file fails the guard" python3 "$S/repo_map.py" guard
git checkout -q preexisting.txt
expect_rc 1 "reverting pre-existing dirty file fails the guard" python3 "$S/repo_map.py" guard

printf '\ncommit hygiene\n'
printf 'feat(api): add thing\n' > m1.txt
printf 'add thing\n' > m2.txt
printf 'feat: add thing\n\nCo-Authored-By: Some Tool <x@y.z>\n' > m3.txt
printf 'fix: use database cursor pagination\n' > m4.txt
expect_rc 0 "conventional message passes" python3 "$S/evidence.py" commit-check m1.txt
expect_rc 1 "non-conventional message fails" python3 "$S/evidence.py" commit-check m2.txt
expect_rc 1 "co-author trailer fails" python3 "$S/evidence.py" commit-check m3.txt
expect_rc 0 "the word cursor is not attribution" python3 "$S/evidence.py" commit-check m4.txt
printf 'feat: made with Claude\n' > m5.txt
expect_rc 1 "tool name in message fails" python3 "$S/evidence.py" commit-check m5.txt

printf '\nevidence and handoff\n'
python3 "$S/evidence.py" policy --ceremony standard --stop "v9.9" >/dev/null
expect_rc 0 "passing command is recorded" python3 "$S/evidence.py" run --label unit -- true
expect_rc 1 "failing command exit code is preserved" python3 "$S/evidence.py" run --label bad -- false
[ "$(wc -l < .ilana/evidence.jsonl | tr -d ' ')" = "2" ] && ok "two evidence records" || bad "two evidence records"
expect_rc 1 "report fails while a label is failing" python3 "$S/evidence.py" report
python3 "$S/evidence.py" run --label bad -- true >/dev/null
expect_rc 0 "report passes once latest run passes" python3 "$S/evidence.py" report
python3 "$S/evidence.py" handoff --set milestone=m1 --set next="do x" --add completed=a --add disagreement="claimed clean; tree was dirty" >/dev/null
grep -q '"milestone": "m1"' .ilana/handoff.json && ok "handoff json written" || bad "handoff json written"
grep -q 'v9.9' .ilana/milestone-state.md && ok "stop boundary rendered" || bad "stop boundary rendered"
grep -q 'claimed clean' .ilana/milestone-state.md && ok "reality disagreement rendered" || bad "reality disagreement rendered"
expect_rc 2 "unknown handoff key rejected" python3 "$S/evidence.py" handoff --set bogus=1

printf '\nprivacy\n'
python3 "$S/privacy_scan.py" scan --stdout > priv.txt
grep -q 'credentials' priv.txt && ok "credential class detected" || bad "credential class detected"
grep -q 'internal/api/api.go:3' priv.txt && ok "sensitive log line flagged" || bad "sensitive log line flagged"
printf 'all fine\n' > clean.log
printf 'oops hunter2 leaked\n' > dirty.log
expect_rc 0 "clean output passes marker check" python3 "$S/privacy_scan.py" check --markers hunter2 clean.log
expect_rc 1 "leaked marker fails marker check" python3 "$S/privacy_scan.py" check --markers hunter2 dirty.log

printf '\nledger ceremony\n'
mkdir ledgerproj && cd ledgerproj
python3 "$S/ledger.py" init --project p --rigour 4 >/dev/null
grep -q '"ceremony": "regulated"' .ilana/state.json && ok "rigour 4 defaults to regulated" || bad "rigour 4 defaults to regulated"
python3 - <<'PY'
import json
p = ".ilana/state.json"
s = json.load(open(p)); s["ceremony"] = "light"; json.dump(s, open(p, "w"))
PY
expect_rc 1 "light ceremony rejected at rigour 4" python3 "$S/ledger.py" validate

printf '\n'
if [ "$fail" -eq 0 ]; then printf 'MAINTAIN TESTS PASSED\n\n'; exit 0; fi
printf 'MAINTAIN TESTS FAILED: %s\n\n' "$fail"
exit 1
