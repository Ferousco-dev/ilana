---
description: Where is this project in the Ìlànà process? Reads the ledger.
allowed-tools: Bash(python3:*), Bash(cat:*), Bash(ls:*), Read, Glob
---

Report where this project stands in the Ìlànà process.

Read `.ilana/` in the current working directory.

```bash
python3 ~/.claude/skills/ilana/instruments/scripts/ledger.py status 2>/dev/null \
  || python3 ~/.ilana-src/skill/instruments/scripts/ledger.py status 2>/dev/null \
  || echo "no ledger tool available"
```

If there is no `.ilana/` directory, say so plainly and offer to create one with
`ilana init --project <name> --rigour <n>`, explaining what rigour to choose. Do not create it
silently.

If there is one, report clearly:

- **Position**: mode, phase, gate, agent, rigour, process style.
- **Open items**: every defect, change request, conflict and unanswered question, with severity
  where it applies. Do not summarise this list; the user needs to see all of it.
- **Overrides**: every gate the user forced open, with the reason they gave and the date. This is
  the list people forget, and it is the one that matters at release time.
- **Gate history**: which gates passed, which failed and how many times. A gate at two attempts is
  one failure away from escalation.
- **Traceability health**: run `instruments/scripts/traceability.py` if `.ilana/traceability.csv`
  exists, and report requirements with no design, no test, or not yet verified.

End with the single most useful next action, and the command or phrase to trigger it.
