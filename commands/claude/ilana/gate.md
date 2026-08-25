---
description: Run a specific Ìlànà quality gate against this project.
argument-hint: <G0..G8> [rigour 1-5]
allowed-tools: Bash(python3:*), Bash(git:*), Read, Glob, Grep
---

Run an Ìlànà quality gate. Read `~/.claude/skills/ilana/SKILL.md` and `gates/GATES.md`.

Arguments: $ARGUMENTS

Parse the gate identifier (G0 through G8) and an optional rigour. If rigour is not given, read it
from `.ilana/state.json`; if that does not exist, default to 3 and say so.

**First run the automated checker**, which handles the mechanically verifiable criteria:

```bash
python3 ~/.claude/skills/ilana/instruments/scripts/gate_check.py --gate <GATE> --rigour <N> --repo .
```

If that path fails, try `~/.ilana-src/skill/instruments/scripts/gate_check.py`. If Python is
unavailable, say so and fall back to the manual procedure documented in the gate file.

**Then assess the criteria the checker marked `[MAN]`.** Those need human or model judgement and the
checker deliberately refuses to pass them silently. Read the full gate file
(`gates/G<n>-<name>.md`) and work through each manual criterion against the actual repository,
citing evidence.

Produce a verdict in the standard format:

```
[conductor] G<n> attempt <k>  verdict: PASS | FAIL

| # | Criterion | Rigour | Met | Evidence |
```

If it fails, state the specific consequence **for this project** in concrete terms, not in general
terms, then say what would remediate it.

Record the attempt in `.ilana/gates/G<n>.md`. If `.ilana/` does not exist, offer to create it with
`ilana init` rather than creating it silently.
