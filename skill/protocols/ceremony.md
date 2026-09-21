# PROTOCOL: CEREMONY

How much process artifact to produce for a given piece of work. Ceremony is the documentation and
gate-formality axis. `RIGOUR` (kernel) is the correctness axis. They move together by default and
can be set independently.

Article 13 says one process does not fit all projects. Ceremony makes that operational for
maintenance work: a small change to a mature repository should not pay the same paperwork as a
new safety-critical system.

## The three levels

| | `light` | `standard` | `regulated` |
| --- | --- | --- | --- |
| Default `RIGOUR` | 2 | 3 | 4 or 5 |
| Typical work | small fix, config, internal refactor | a feature or milestone in a production system | health, finance, safety, or contractual audit |
| Requirements | one sentence in the handoff | requirements-to-tests table | full SRS (`FLEET` phase 01) |
| Design | none unless a decision is made | `decisions.md` entries for real decisions | design description, ADRs |
| Gates | one done-check (below) | three checkpoints: Plan, Build, Verify and Close | all of G0 to G8, one record each |
| Evidence | `evidence.jsonl` | `evidence.jsonl` plus rendered report | plus independent verification |
| Handoff | `handoff.json` | `handoff.json` plus `milestone-state.md` | plus per-gate handoffs |
| Review | self-check | self-check plus scope guard | independent review, ethics signature |

Ceremony never removes a constitutional article. It removes duplicate paperwork, not
obligations. Articles 1, 2, 7 and 8 apply at every level.

## Gate mapping

- `light` done-check: tests pass with an evidence id, scope guard clean, commit message passes.
- `standard` checkpoints: **Plan** covers G0 to G3, **Build** covers G4, **Verify and Close**
  covers G5 to G8. Each checkpoint is one ledger line citing evidence ids, not one file.
- `regulated`: unchanged from `gates/GATES.md`.

## Choosing and changing the level

1. If the user names a level, use it.
2. If `.ilana/policy.json` exists, use its `ceremony`.
3. Otherwise `standard`. Say so and offer to change.

Escalate one level, and record a `DEC`, when the change touches authentication, money, personal
data, cryptography, migrations of live data, or an external contract. De-escalate only at the
user's request.

Set it with `evidence.py policy --ceremony light|standard|regulated`. `ledger.py init --ceremony`
sets it at project creation. The value lives in `.ilana/policy.json` and is mirrored into
`state.json`.

## Anti-duplication rule

Each fact has one owner artifact. Everything else references it by id.

| Fact | Owner |
| --- | --- |
| requirement statements | `traceability.csv` (or the SRS at `regulated`) |
| decisions | `decisions.md` |
| test and command results | `evidence.jsonl` |
| current milestone status | `handoff.json` |
| architecture facts | the project's architecture document |
| narrative | one line per event in `ledger.md`, citing ids |

A document that restates another document's facts is a defect (`DEF`) in the process.
