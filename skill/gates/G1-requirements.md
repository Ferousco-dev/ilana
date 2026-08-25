# G1 - REQUIREMENTS BASELINE

Owner: `analyst`. Closes: phase 01. Opens: phase 02 Architecture design.

This is the highest-leverage gate in the whole process. A defect that passes G1 is the most
expensive kind of defect there is.

## Criteria

| # | Criterion | Rigour | Evidence |
|---|---|---|---|
| 1 | Every requirement has a unique, stable ID | R1+ | `.ilana/traceability.csv` |
| 2 | All three types represented or their absence justified: functional, non-functional, domain | R1+ | counts by type |
| 3 | No requirement contains an unmeasurable adjective | R1+ | grep for fast, easy, user-friendly, secure, scalable, robust, intuitive |
| 4 | Each requirement is independently testable | R1+ | a sentence describing how you would test it |
| 5 | Scope boundary written: what the system will NOT do | R2+ | SRS section "Out of scope" |
| 6 | Every NFR carries a number and a unit | R3+ | e.g. "95th percentile < 2s at 500 concurrent users" |
| 7 | Requirements validated with an actual stakeholder | R3+ | dated review note |
| 8 | Conflicts between requirements identified and dispositioned | R3+ | `.ilana/decisions.md` |
| 9 | Assumptions explicitly logged, not embedded | R3+ | `DEC-###` entries |
| 10 | Domain and regulatory requirements traced to their source rule | R4+ | citation per `DOM-###` |
| 11 | Formal inspection with Moderator, Reader, Recorder | R5 | `docs/reviews/inspection-G1.md` |
| 12 | Independent verification that the SRS reflects stakeholder intent | R5 | second reviewer, named |

## The adjective test

Run this. It catches more real defects than any other single check at this gate.

```bash
grep -inE '\b(fast|quick|easy|simple|user[- ]friendly|intuitive|secure|scalable|robust|efficient|reliable|flexible|modern|seamless)\b' docs/srs.md
```

Every hit is either rewritten with a number, or explicitly accepted as a design goal rather
than a requirement, and moved out of the requirements section.

## Common failures

- Non-functional requirements written as aspirations. "The system should be secure" is not a
  requirement; "all data at rest is encrypted with AES-256 and keys rotate every 90 days" is.
- Domain requirements missing entirely because nobody asked what regulator or industry rule
  applies.
- Requirements written by the developer rather than elicited from the user, then validated by
  the same developer.
