#!/bin/sh
# Structural validation of the Ilana skill payload.
# Exits non-zero on any structural problem. Used by CI and by `make validate`.

set -eu

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL="$ROOT/skill"
fail=0

ok()   { printf '  ok    %s\n' "$*"; }
bad()  { printf '  FAIL  %s\n' "$*"; fail=$((fail + 1)); }

need_file() { [ -f "$SKILL/$1" ] && ok "$1" || bad "missing file: $1"; }
need_dir()  { [ -d "$SKILL/$1" ] && ok "$1/" || bad "missing directory: $1"; }

printf '\nILANA STRUCTURAL VALIDATION\n\n'

printf 'core\n'
need_file SKILL.md
need_file manifest.json
need_file kernel/KERNEL.md
need_file kernel/constitution.md
need_file kernel/state-machine.md
need_file kernel/ledger-spec.md
need_file kernel/refusal-protocol.md
need_file kernel/glossary.md

printf '\nmodes\n'
need_file modes/MODES.md
for m in fleet task maintain audit tutor doctor drill; do need_file "modes/$m.md"; done

printf '\ngates\n'
need_file gates/GATES.md
for g in G0-intake G1-requirements G2-design G3-interface G4-construction \
         G5-verification G6-release G7-quality G8-closure; do
  need_file "gates/$g.md"
done

printf '\nphases\n'
phase_count=0
for d in "$SKILL"/phases/*/; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  phase_count=$((phase_count + 1))
  for f in PHASE.md checklist.md questions.md antipatterns.md gate.md reference.md; do
    if [ -f "$d$f" ]; then :; else bad "phases/$name/$f"; fi
  done
  [ -d "$d/templates" ] || bad "phases/$name/templates/"
done
if [ "$phase_count" -eq 11 ]; then
  ok "11 phases, each with 6 core files and templates/"
else
  bad "expected 11 phases, found $phase_count"
fi

printf '\nagents\n'
agent_count=0
for d in "$SKILL"/agents/*/; do
  [ -d "$d" ] || continue
  agent_count=$((agent_count + 1))
  [ -f "$d/AGENT.md" ] || bad "agents/$(basename "$d")/AGENT.md"
done
need_file agents/FLEET.md
if [ "$agent_count" -eq 13 ]; then
  ok "13 agents, each with AGENT.md"
else
  bad "expected 13 agents, found $agent_count"
fi

printf '\nprotocols\n'
for p in question-engine elicitation review-inspection defect-lifecycle change-control \
         conflict-resolution escalation release incident handoff \
         ceremony checkpoint scope-guard; do
  need_file "protocols/$p.md"
done

printf '\ninstruments\n'
need_file instruments/INSTRUMENTS.md
need_file instruments/metrics.md
need_file instruments/quality-attributes.md
need_file instruments/cmmi-probe.md
for s in metrics gate_check traceability ledger repo_map evidence privacy_scan; do
  need_file "instruments/scripts/$s.py"
done

printf '\nreferences\n'
for r in README quick-reference standards cmmi acm-ieee-ethics \
         agile-devops-plan-driven tools-map reading-list; do
  need_file "references/$r.md"
done

printf '\ninterrogation\n'
need_file interrogation/QUESTIONS.md
need_file interrogation/intake.md
need_dir  interrogation/banks
bank_count=$(find "$SKILL/interrogation/banks" -name '*.md' | wc -l | tr -d ' ')
[ "$bank_count" -ge 11 ] && ok "$bank_count question banks" || bad "expected at least 11 banks, found $bank_count"

printf '\ncommands\n'
CMDS="$ROOT/commands/claude"
[ -f "$CMDS/ilana.md" ] && ok "commands/claude/ilana.md" || bad "missing commands/claude/ilana.md"
for c in task fleet maintain audit ship review gate doctor drill tutor status rigour; do
  [ -f "$CMDS/ilana/$c.md" ] || bad "missing commands/claude/ilana/$c.md"
done
cmd_count=$(find "$CMDS/ilana" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
[ "$cmd_count" -ge 11 ] && ok "$cmd_count subcommands present" || bad "expected 11+ subcommands, found $cmd_count"
fm_ok=1
for f in "$CMDS/ilana.md" "$CMDS"/ilana/*.md; do
  [ -f "$f" ] || continue
  head -1 "$f" | grep -q '^---$' || { bad "$(basename "$f") missing frontmatter"; fm_ok=0; }
  grep -q '^description:' "$f" || { bad "$(basename "$f") missing description"; fm_ok=0; }
done
[ "$fm_ok" -eq 1 ] && ok "every command carries frontmatter and a description"

printf '\nversion drift\n'
if grep -rn 'Ìlànà v[0-9]' "$SKILL" --include='*.md' >/dev/null 2>&1; then
  bad "a hardcoded version string is in the skill payload; it will go stale on release"
  grep -rn 'Ìlànà v[0-9]' "$SKILL" --include='*.md' | sed 's|^|          |'
else
  ok "no hardcoded version strings in the skill prose"
fi

printf '\nmanifest counts\n'
mc() { sed -n "s/.*\"$1\"[[:space:]]*:[[:space:]]*\([0-9][0-9]*\).*/\1/p" "$SKILL/manifest.json" | head -1; }
[ "$(mc modes)" = "7" ] && ok "manifest modes = 7" || bad "manifest modes count is not 7"
[ "$(mc protocols)" = "13" ] && ok "manifest protocols = 13" || bad "manifest protocols count is not 13"
[ "$(mc constitution_articles)" = "17" ] && ok "manifest articles = 17" || bad "manifest articles count is not 17"
[ "$(cat "$ROOT/VERSION")" = "$(sed -n 's/.*"version"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$SKILL/manifest.json" | head -1)" ] \
  && ok "VERSION matches manifest.json" || bad "VERSION and manifest.json disagree"
grep -q "version: $(cat "$ROOT/VERSION")" "$SKILL/SKILL.md" && ok "SKILL.md metadata version matches" \
  || bad "SKILL.md metadata version does not match VERSION"

printf '\nupdate\n'
need_file update/UPDATE.md
need_file update/check-update.sh

printf '\nfrontmatter\n'
head -1 "$SKILL/SKILL.md" | grep -q '^---$' && ok "SKILL.md opens with frontmatter" \
  || bad "SKILL.md must open with YAML frontmatter"
grep -q '^name: ilana$' "$SKILL/SKILL.md" && ok "name: ilana" || bad "SKILL.md name field"
grep -q '^description:' "$SKILL/SKILL.md" && ok "description present" || bad "SKILL.md description field"

printf '\nthe fork question\n'
grep -q 'FLEET' "$SKILL/SKILL.md" && grep -q 'TASK' "$SKILL/SKILL.md" \
  && ok "boot fork present in SKILL.md" || bad "SKILL.md must present the FLEET/TASK fork"

printf '\nscripts are executable\n'
for s in "$ROOT/bin/ilana" "$ROOT/install.sh"; do
  [ -x "$s" ] && ok "$(basename "$s")" || bad "$(basename "$s") is not executable"
done

printf '\nhouse style\n'
if find "$ROOT" -name '*.md' -not -path '*/.git/*' -print0 2>/dev/null \
   | xargs -0 grep -l "$(printf '\342\200\224')" 2>/dev/null | head -1 | grep -q .; then
  printf '  FAIL  em dash found in:\n'
  find "$ROOT" -name '*.md' -not -path '*/.git/*' -print0 \
    | xargs -0 grep -l "$(printf '\342\200\224')" 2>/dev/null | sed 's|^|          |'
  fail=$((fail + 1))
else
  ok "no em dashes"
fi

printf '\n'
if [ "$fail" -eq 0 ]; then
  printf 'VALID. %s files.\n\n' "$(find "$SKILL" -type f | wc -l | tr -d ' ')"
  exit 0
fi
printf 'INVALID. %s problems.\n\n' "$fail"
exit 1
