# GATES

A gate is a named checkpoint between phases. It has entry criteria, exit criteria, required
evidence, and a named owner. Gates are the enforcement surface of Ìlànà. Everything else is
advice; gates are the part that says no.

---

## The nine gates

| Gate | Name | Closes | Opens | Owner | Evidence lives in |
| --- | --- | --- | --- | --- | --- |
| G0 | Intake | (boot) | 01 Requirements | `conductor` | `.ilana/gates/G0.md` |
| G1 | Requirements baseline | 01 | 02 Architecture | `analyst` | `.ilana/gates/G1.md` |
| G2 | Design baseline | 02 | 03 Interface | `architect` | `.ilana/gates/G2.md` |
| G3 | Interface baseline | 03 | 04 Construction | `interaction-designer` | `.ilana/gates/G3.md` |
| G4 | Construction complete | 04 | 05 Verification | `constructor` | `.ilana/gates/G4.md` |
| G5 | Verification complete | 05 | 06 Config management | `verifier` | `.ilana/gates/G5.md` |
| G6 | Release readiness | 06 | 07 Quality assurance | `release-manager` | `.ilana/gates/G6.md` |
| G7 | Quality sign-off | 07 | 08 Process assessment | `quality-auditor` | `.ilana/gates/G7.md` |
| G8 | Closure | 08 | (done) | `conductor` | `.ilana/gates/G8.md` |

---

## How rigour changes a gate

Every gate criterion carries a rigour threshold. The criterion applies at that rigour and above.

```
[R1+] applies always
[R3+] applies at production rigour and above
[R4+] applies at regulated rigour and above
[R5]  applies only at safety-critical rigour
```

At `RIGOUR` 1 a gate is a two-line sanity check. At `RIGOUR` 5 it is a formal review with
independent verification and an ethics signature. Same gate, different teeth. This is
Article 13 made operational.

---

## Gate record format

Every attempt, pass or fail, is written to `.ilana/gates/G<n>.md`.

```markdown
# G1 - Requirements baseline
Attempt: 2 of 2 allowed before escalation
Date: 2026-08-21
Owner: analyst
Rigour: 3
Verdict: PASS

## Criteria
| # | Criterion | Rigour | Met | Evidence |
|---|---|---|---|---|
| 1 | Every requirement has a unique stable ID | R1+ | yes | .ilana/traceability.csv, 36 rows |
| 2 | No requirement contains an unmeasurable adjective | R1+ | yes | grep audit, 0 hits for fast/easy/user-friendly |
| 3 | Functional, non-functional and domain requirements all present | R1+ | yes | 24 REQ, 9 NFR, 3 DOM |
| 4 | Every NFR is quantified with a number and a unit | R3+ | yes | see NFR-001..NFR-009 |
| 5 | Requirements validated with a stakeholder | R3+ | yes | review note docs/reviews/2026-08-21.md |
| 6 | Conflicts identified and resolved or logged | R3+ | yes | 1 conflict, resolved, DEC-004 |
| 7 | Independent review by someone other than the author | R4+ | n/a | rigour 3 |
| 8 | Formal inspection with Moderator, Reader, Recorder | R5 | n/a | rigour 3 |

## Open items carried forward
REQ-017 assumption: peak concurrency 5000, unconfirmed. Logged DEC-005.

## Handoff
-> architect. Decompose REQ-001..REQ-024.
```

---

## Overrides

A user may override a gate at `RIGOUR` 1 to 4. Ìlànà:

1. states exactly which criteria are unmet,
2. states the specific consequence in this project's terms, not in general terms,
3. records the override with the user's reason in `state.json` and the gate record,
4. proceeds without arguing a second time.

```
[conductor] G4 OVERRIDE ACCEPTED
Unmet: criterion 3 (integration tests exist for every module boundary).
Consequence here: the payment/ledger boundary is the one where money is reconciled,
and it will ship unverified.
Your reason (recorded): "demo on Friday, integration suite lands next sprint".
Recorded as OVERRIDE-002. Advancing to phase 05.
```

At `RIGOUR` 5 there are no overrides. Ìlànà says so and stops. It does not pretend the gate
was met, and it does not lecture.

---

## The two-attempt rule

A gate may fail twice. On the second failure Ìlànà stops remediating and runs
`protocols/escalation.md`, because a gate that fails twice is signalling that the problem is
upstream, not in the artifact under review.

Attempt counters persist across sessions. They are reset only by a passing verdict.
