# G8 - CLOSURE

Owner: `conductor`. Closes: phase 08. Ends the run.

The gate almost everyone skips, which is exactly why processes never improve. Article 15
exists because of this gate.

## Criteria

| # | Criterion | Rigour | Evidence |
|---|---|---|---|
| 1 | Every gate has a record, including overrides and their reasons | R1+ | `.ilana/gates/` complete |
| 2 | Traceability matrix is complete: no requirement without a test result | R1+ | matrix export |
| 3 | Open items are closed, deferred with an owner and a date, or withdrawn | R1+ | `.ilana/` open lists empty or dispositioned |
| 4 | A retrospective was held and written down | R2+ | `docs/retrospective.md` |
| 5 | At least one concrete process change is carried into the next run | R2+ | named change, owner, start date |
| 6 | Metrics baseline recorded for comparison next time | R3+ | `.ilana/metrics.csv` snapshot |
| 7 | Indicative CMMI level assessed with the evidence behind it | R3+ | `docs/maturity-assessment.md` |
| 8 | Knowledge transfer complete: a new engineer could operate this from the docs alone | R3+ | onboarding doc, ideally tested on a real newcomer |
| 9 | Ethics register reviewed and every `ETH-###` dispositioned | R4+ | `.ilana/ethics.md` |
| 10 | Full lifecycle evidence package exportable for audit | R5 | archive |

## The retrospective

Not a feelings exercise. Four questions, each answered with evidence:

1. **What did the process catch?** Name the specific defects caught at G1, G2 or G7 that would
   otherwise have reached production, and estimate what they would have cost there.
2. **What did the process miss?** Every defect found late is a gate that did not bite. Which gate?
3. **Where did the process cost more than it returned?** Ceremony that produced no finding is
   waste and should be trimmed at this rigour.
4. **What one change goes into the next run?** One. With an owner and a date and a metric.

## The closing number

End every run with a single honest comparison:

```
Defects found before G5 (prevention):  17
Defects found after G5 (detection):     4
Defects found in production:            1 (DEF-022, severity medium)
Prevention ratio: 17/22 = 77%

Baseline for next run. Target: 85%.
```

If prevention ratio drops between runs, the process is decaying and `DOCTOR` mode is due.
