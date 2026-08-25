# Cursor

Cursor reads rules from `.cursor/rules/*.mdc`.

## Install

```bash
git clone https://github.com/OWNER/ilana.git ~/.ilana-src
mkdir -p .cursor/rules
cp ~/.ilana-src/adapters/templates/ilana.mdc .cursor/rules/ilana.mdc
ln -s ~/.ilana-src/skill .cursor/ilana
```

The `.mdc` file is the trigger; the symlinked directory is the payload it points at.

## Rule file

`.cursor/rules/ilana.mdc`:

```markdown
---
description: Ìlànà software engineering process. Load for requirements, design, testing, SCM, quality, process, ethics and team work.
globs:
alwaysApply: false
---

Read `.cursor/ilana/SKILL.md` and run its boot sequence before starting.

Non-negotiables:
1. No requirement, no code. Every change traces to a requirement ID.
2. No gate skip. Gates may be overridden, with a recorded reason. They may not be bypassed.
3. Ambiguity is a defect. Raise it; never resolve it silently.
4. Prevention beats detection. Review before you test.
5. Measure or stay silent. No superlative without a number.
6. Write it down. Ledger entry or it did not happen.

The first thing to do is ask: fleet of agents, or a single task?
```

## Notes

Cursor has no sub-agent mechanism, so fleet mode runs as a sequential rotation through the agent
cards. Same gates, same artifacts, one context.

Because Cursor rules are per-project, this is a good place to record the project's `RIGOUR` and
process style directly in the rule file, so every session starts from the same posture.
