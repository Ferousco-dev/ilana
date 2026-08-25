# LEDGER SPECIFICATION

Ìlànà writes its memory into `.ilana/` at the root of the user's project. This directory
belongs to the user. It is plain text. It survives Ìlànà. It should be committed to version
control, because process history is project history.

## Layout

```
.ilana/
  state.json          registers (cache, rebuildable from ledger.md)
  ledger.md           append-only narrative log, the source of truth
  traceability.csv    REQ -> DES -> code -> TC mapping
  requirements.md     the register (short form; full SRS lives in docs/)
  decisions.md        DEC-### architecture and process decision records
  defects.md          DEF-### log with lifecycle state
  changes.md          CR-### change requests and their disposition
  risks.md            RSK-### register with likelihood, impact, mitigation
  metrics.csv         MET-### time series of measurements
  ethics.md           ETH-### findings, vetoes, and their resolution
  gates/
    G0.md .. G8.md    one evidence record per gate attempt
  update-state.json   last update check
```

## `state.json`

```json
{
  "ilana_version": "1.0.0",
  "project": "library-management-system",
  "mode": "FLEET",
  "phase": "05",
  "gate": "G4",
  "agent": "verifier",
  "process_style": "hybrid",
  "rigour": 3,
  "open": ["DEF-004", "CR-002"],
  "overrides": [
    { "gate": "G3", "reason": "design review deferred; UI is a thin CLI", "at": "2026-08-22" }
  ],
  "counters": { "REQ": 24, "NFR": 9, "DOM": 3, "DES": 31, "TC": 61, "DEF": 4, "CR": 2 },
  "attempts": { "G4": 1 }
}
```

## `ledger.md`

Append-only. One block per event. Newest at the bottom. Never edited, only superseded.

```
## 2026-08-24 14:02 | G4 | verifier | GATE PASS
Evidence:
  - tests/ contains 61 cases, TC-001..TC-061
  - unit 44, integration 12, system 4, acceptance 1
  - run: 61 passed, 0 failed, coverage 78% (report: build/coverage.xml)
  - defect log: DEF-001 closed, DEF-002 closed, DEF-003 closed, DEF-004 open (low)
Traceability: 24/24 REQ have >= 1 TC. 9/9 NFR have >= 1 TC. Gap: none.
Decision: advance to phase 06.
```

Superseding an earlier entry:

```
## 2026-08-25 09:10 | CORRECTION | metrologist
Supersedes 2026-08-24 14:02 coverage figure.
Coverage was reported as 78%; recomputed against the correct source root it is 71%.
No gate reversal: G4 threshold at RIGOUR 3 is 70%.
```

## `traceability.csv`

```csv
req_id,requirement,type,design_id,module,test_ids,status
REQ-001,User can log in with email and password,functional,DES-004,auth/login.py,TC-001;TC-002;TC-003,verified
NFR-004,95th percentile response under 2s at 500 concurrent users,non-functional,DES-019,,TC-052,verified
DOM-001,Patient data handling complies with the applicable privacy regime,domain,DES-022,privacy/,TC-058;TC-059,partial
```

`status` is one of: `draft`, `specified`, `designed`, `implemented`, `verified`, `withdrawn`.

## `metrics.csv`

```csv
id,date,metric,category,value,unit,source
MET-001,2026-08-20,defect_density,product,2.4,defects_per_kloc,build/report.xml
MET-002,2026-08-20,process_cycle_time,process,4.5,days,jira_export.csv
MET-003,2026-08-20,cost_variance,project,-1200,currency,budget.xlsx
MET-004,2026-08-20,schedule_adherence,project,0.93,ratio,plan_vs_actual.csv
```

## Rules

1. **Append only.** Never rewrite a ledger entry. Corrections are new entries.
2. **Evidence is a path or a number.** Never a claim.
3. **Timestamps are dates the user can verify.** If you do not know the date, ask or omit it;
   do not invent one.
4. **The ledger is the user's.** Never delete `.ilana/` without explicit instruction.
5. **Commit it.** Recommend adding `.ilana/` to version control. It is documentation, and by
   Article 12 documentation is not optional.
