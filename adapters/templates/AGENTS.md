# AGENTS.md

Drop this into a repository root for Codex, OpenCode, or any agent that reads `AGENTS.md`.
Edit the marked lines to match your project.

---

## Process: Ìlànà

This project follows Ìlànà, a gated software engineering process.

**Definition:** `.ilana-src/skill/SKILL.md`
(vendored with `git submodule add https://github.com/Ferousco-dev/ilana.git .ilana-src`)

**Project posture** (edit these):

| Setting | Value |
| --- | --- |
| Rigour | 3 of 5 |
| Process style | hybrid |
| Ledger | `.ilana/` |
| Gates in force | G1, G4, G5, G6 |

### Before non-trivial work

Read the definition and run its boot sequence. The first thing it does is ask whether to run a
**fleet of specialist agents** or a **single focused task**. Ask; do not assume.

### Standing rules for this repository

1. **Every change traces to a requirement or a change request.** Commit messages carry
   `Refs: REQ-### / CR-### / DEF-###`.
2. **No merge to `main` without G4.** Coding standard enforced, no secrets, peer review complete.
3. **No release without G6.** Built from a tag, rollback rehearsed, changelog written.
4. **No defect closes without a named regression test.**
5. **Test results are reported as counts.** Failures are pasted, not summarised.
6. **Documentation changes in the same commit as the behaviour it documents.**

### Where things live

| Artifact | Path |
| --- | --- |
| Requirements | `docs/srs.md` |
| Design | `docs/design.md` |
| Interface spec | `docs/ui-spec.md` |
| Coding standard | `docs/coding-standard.md` |
| Test plan | `docs/test-plan.md` |
| SCM plan | `docs/scm-plan.md` |
| Quality plan | `docs/quality-plan.md` |
| Rollback plan | `docs/rollback.md` |
| Process ledger | `.ilana/` |

### Escalation

Blocked, or a gate has failed twice: stop, state the block precisely, offer at least two options
with a recommendation, and time-box the wait. Do not guess past a blocker.
