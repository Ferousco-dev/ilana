# G0 - INTAKE

Owner: `conductor`. Closes: boot. Opens: phase 01 Requirements.

The cheapest gate and the one most often skipped. Its whole purpose is to stop Ìlànà from
building a beautifully engineered answer to the wrong question.

## Criteria

| # | Criterion | Rigour | Evidence |
|---|---|---|---|
| 1 | The problem is stated in one sentence, in the user's words | R1+ | quoted in `.ilana/ledger.md` |
| 2 | Primary users and stakeholders are named | R1+ | intake answers |
| 3 | Mode selected and recorded | R1+ | `state.json.mode` |
| 4 | Rigour selected and justified | R1+ | `state.json.rigour` plus one line of reasoning |
| 5 | Process style selected: agile, plan-driven, hybrid, devops | R2+ | `state.json.process_style` |
| 6 | Domain and regulatory exposure identified | R3+ | `.ilana/ethics.md` initial scan |
| 7 | Existing artifacts inventoried (code, docs, tickets) | R3+ | list in the ledger |
| 8 | Safety, privacy or financial impact classified | R4+ | `ETH-001` |
| 9 | Independent confirmation of scope by a second stakeholder | R5 | named person, dated |

## Failure modes

- The user gives a solution ("build me a React dashboard") instead of a problem. Convert it:
  "who looks at this dashboard, and what decision do they make after looking at it?"
- Rigour set by vibes. Anchor it: does this system touch money, health, safety, personal data,
  or a legal obligation? If yes, minimum 4.
- Skipping the existing-artifact inventory and then rewriting something that already worked.
