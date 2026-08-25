# G2 - DESIGN BASELINE

Owner: `architect`. Closes: phase 02. Opens: phase 03 Interface design.

## Criteria

| # | Criterion | Rigour | Evidence |
|---|---|---|---|
| 1 | All three design levels addressed: architecture, high-level, detailed | R1+ | `docs/design.md` sections |
| 2 | Every `REQ` maps to at least one `DES` element | R1+ | traceability matrix, no orphan requirements |
| 3 | Every `DES` element maps back to at least one `REQ` | R1+ | no orphan design (Article 3) |
| 4 | Module boundaries and interfaces are explicit | R2+ | interface table with inputs, outputs, errors |
| 5 | Six design objectives assessed: correctness, completeness, efficiency, flexibility, consistency, maintainability | R2+ | one paragraph each |
| 6 | Non-functional requirements have an architectural mechanism | R3+ | e.g. NFR-004 latency -> caching layer DES-019 |
| 7 | At least one alternative architecture was considered and rejected with reasons | R3+ | `DEC-###` architecture decision record |
| 8 | Failure modes and degradation behaviour specified | R4+ | what happens when each dependency is down |
| 9 | Data model documented with ownership and retention | R4+ | `docs/data-model.md` |
| 10 | Independent design review by a non-author | R4+ | dated review record |
| 11 | Formal inspection, and hazard analysis where safety applies | R5 | `docs/reviews/inspection-G2.md` |

## The orphan check

Two directions, both mandatory:

```
requirements with no design element  -> the system will not do what was asked
design elements with no requirement  -> you are building something nobody asked for
```

Both are gate failures. The second one is the one teams forget.

## Common failures

- Jumping to detailed design without stating the architecture, so conceptual integrity is
  never established.
- Designing without the database or operations people in the room, which the source material
  identifies as a classic collaboration failure producing data type mismatches across
  structural components.
- Recording the chosen option but not the rejected ones, which destroys the reasoning for
  whoever inherits the system.
