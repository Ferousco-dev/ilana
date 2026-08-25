# STATE MACHINE

## States

```
BOOT -> INTERROGATE -> PLAN -> PHASE_ENTRY -> WORK -> ARTIFACT -> GATE
                                   ^                                |
                                   |                          pass  |  fail
                                   |                                |
                                   +--- ADVANCE <-------------------+
                                                                    |
                                                            REMEDIATE (x2 max)
                                                                    |
                                                                ESCALATE
```

Terminal states: `CLOSED` (G8 passed), `HALTED` (ethics veto or hard stop),
`SUSPENDED` (user left; ledger holds position).

## Transition table

| From | Event | To | Side effect |
| --- | --- | --- | --- |
| `BOOT` | ledger found | `INTERROGATE` | load registers, report position |
| `BOOT` | no ledger | `INTERROGATE` | cold start |
| `INTERROGATE` | intake answered | `PLAN` | write `.ilana/state.json` |
| `INTERROGATE` | user says "assume defaults" | `PLAN` | print assumptions as `DEC-###` |
| `PLAN` | mode = TASK | `PHASE_ENTRY` | single phase, single agent |
| `PLAN` | mode = FLEET | `PHASE_ENTRY` | phase 01, full roster announced |
| `PHASE_ENTRY` | phase questions answered | `WORK` | adopt agent card |
| `WORK` | artifact drafted | `ARTIFACT` | write file to repo |
| `ARTIFACT` | checklist complete | `GATE` | assemble evidence block |
| `GATE` | all criteria met | `ADVANCE` | append `GATE-##`, emit handoff |
| `GATE` | criteria missing | `REMEDIATE` | list exactly what is missing |
| `GATE` | user override, RIGOUR <= 4 | `ADVANCE` | append override with reason |
| `GATE` | user override, RIGOUR = 5 | `HALTED` | refuse, explain, stop |
| `REMEDIATE` | fixed | `GATE` | retry, attempt counter +1 |
| `REMEDIATE` | attempt counter = 2 | `ESCALATE` | run `protocols/escalation.md` |
| any | ethics veto | `HALTED` | append `ETH-###`, notify user |
| `ADVANCE` | phase 11 done and G8 passed | `CLOSED` | retrospective |

## Attempt counters

Reset per gate, not per session. A gate that failed twice yesterday is still at two attempts
today. This is deliberate: repeated failure at the same gate is a process signal, and
`doctor` mode reads it.

## Resume semantics

On re-entry, Ìlànà reconstructs from `.ilana/state.json` and reports:

```
Resuming. MODE=FLEET PHASE=05 GATE=G4 AGENT=verifier RIGOUR=3
Open: DEF-004 (severity high, unassigned), CR-002 (awaiting approval)
Last ledger entry: 2026-08-24 G4 passed, evidence tests/report.xml
```

If `state.json` and `ledger.md` disagree, the ledger wins and Ìlànà rebuilds `state.json`
from it. The ledger is the source of truth; state is a cache.
