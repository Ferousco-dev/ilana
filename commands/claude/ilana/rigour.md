---
description: Set or explain the Ìlànà rigour level, the dial that controls how hard the gates bite.
argument-hint: [1-5, or leave blank to see the current level and what it means]
---

Read `~/.claude/skills/ilana/SKILL.md` and `kernel/KERNEL.md` section 2.

Requested: $ARGUMENTS

**If a number was given (1 to 5):** update `rigour` in `.ilana/state.json`, confirm the change, and
state in one or two sentences what specifically changes at that level for this project. Record the
change as a decision in `.ilana/decisions.md` with the user's reason if they gave one.

**If nothing was given:** report the current rigour from `.ilana/state.json`, explain what it means
here, and show the table so they can choose.

| Rigour | Typical project | Gate behaviour |
| --- | --- | --- |
| 1 | throwaway script, spike, experiment | advisory; ledger still written |
| 2 | internal tool, portfolio project | warn; one override allowed per gate |
| 3 | production software with real users | enforce; overrides logged and counted |
| 4 | regulated: finance, health records, government, personal data at scale | enforce; overrides need written justification and a compensating control |
| 5 | safety-critical: medical devices, avionics, traffic control | no overrides; independent verification mandatory; ethics officer signs every gate |

**Anchor the choice rather than letting it be chosen by feel.** Ask: does this system touch money,
health, safety, personal data, or a legal obligation? If yes, the minimum is 4.

If they are dropping the rigour because Ìlànà feels heavy, say that this is the correct response
and not a compromise. The phases never disappear; only the ceremony does. Article 13 exists
precisely because no single process fits all projects.

If they ask for rigour 5, warn them once that gates become non-overridable at that level, and that
Ìlànà will stop rather than pretend a gate was met.
