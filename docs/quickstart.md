# QUICKSTART

Five minutes from nothing to a gated process.

---

## 1. Install

```bash
curl -fsSL https://raw.githubusercontent.com/OWNER/ilana/main/install.sh | sh
```

Or, if you prefer to see what you are running first:

```bash
git clone https://github.com/OWNER/ilana.git ~/.ilana-src
~/.ilana-src/bin/ilana install --link --all
```

Verify:

```bash
ilana doctor
```

## 2. Say the word

In your coding agent:

```
use ilana
```

Ìlànà announces itself, then asks the only question that matters at the start:

> **How should Ìlànà run this?**
> **[1] FLEET** - a bundle of specialist agents, full gated lifecycle.
> **[2] TASK** - one specialist, one focused operation.

## 3. Answer the intake

Five to nine questions, in one batch. Answer what you can; say "assume" for the rest and Ìlànà will
print its assumptions rather than hiding them.

Two of the questions are asked every time, regardless: who is harmed if this is wrong, and what
happens to a person if this data leaks. They set the rigour, which sets how hard the gates bite.

## 4. Work

Ìlànà announces the phase, the gate and the agent as it goes:

```
[analyst] Phase 01. Attempting G1.
REQ-001..REQ-024 written to docs/srs.md.
G1 criterion 3 FAILED: "the system should be responsive" is not measurable.
Proposed rewrite: NFR-004, 95th percentile response under 2 seconds at 500 concurrent users.
Confirm the numbers or give me yours.
```

## 5. Ship

```
[release-manager] G6.
Unmet: criterion 5, rollback plan exists but has never been rehearsed.
Consequence here: your migration drops a column, so rollback is not reversible
without the pre-deploy backup, which has also never been restore-tested.
Rehearse it, or override with a reason and Ìlànà will record who accepted the risk.
```

---

## Try it without installing anything

Paste `adapters/templates/ILANA.md` into any chat interface and say "run the boot sequence". It is
self-contained. You lose the templates and the question banks; you keep the process.

---

## Five things to try first

```
use ilana                                    the full boot, with the fork
audit this repo with ilana                   score an existing codebase, change nothing
ilana: write me a test plan for this         TASK mode, one artifact
ilana doctor mode: we keep missing deadlines diagnose the process, not the code
ilana drill: gauntlet                        40 questions, full scorecard
```

---

## The ledger

```bash
ilana init --project my-service --rigour 3
```

Creates `.ilana/`. Commit it. It is your process history, it is plain text, and it outlives any
particular tool.

```
.ilana/
  state.json        where the run is
  ledger.md         append-only narrative
  traceability.csv  requirement -> design -> code -> test
  defects.md        the defect log
  decisions.md      decisions and assumptions
  gates/            one evidence record per gate attempt
```

---

## Staying current

```bash
ilana check                     compare local and upstream
ilana update                    pull and refresh every install
ilana autoupdate --enable       weekly, in the background
```

If you installed with `--link`, `git pull` in the source directory updates every agent on the
machine at once.

---

## Local rules that survive updates

Never edit the installed skill. Put your house rules in overrides:

```bash
mkdir -p ~/.config/ilana/overrides/gates
cat > ~/.config/ilana/overrides/gates/G4.append.md <<'RULES'
## House rules

- All SQL goes through the query builder. No string concatenation, ever.
- Every public function has a docstring stating its error conditions.
RULES
```

Ìlànà reads these after the core file and treats them as additive. `ilana doctor` lists which
overrides are active.
