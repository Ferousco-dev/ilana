# Metrics Report

| Field | Value |
| --- | --- |
| Period | |
| Prepared by | metrologist |
| Data sources | |

## 1. Product metrics

| Metric | Value | Unit | Source | Previous | Trend |
| --- | --- | --- | --- | --- | --- |
| Size | | KLOC | | | |
| Defect density | | defects / KLOC | | | |
| Cyclomatic complexity (mean, max) | | | | | |
| Test coverage | | % | | | |

Defect density worked example: a module of 5,000 lines with 10 confirmed bugs has a defect
density of 2 defects per KLOC.

## 2. Process metrics

| Metric | Value | Unit | Source | Previous | Trend |
| --- | --- | --- | --- | --- | --- |
| Defect rate | | defects / week | | | |
| Mean time to fix | | days | | | |
| Process cycle time | | days | | | |
| Rework effort | | % of total effort | | | |
| Review finding rate | | findings / review | | | |

## 3. Project metrics

| Metric | Value | Unit | Source | Previous | Trend |
| --- | --- | --- | --- | --- | --- |
| Cost variance | | currency | | | |
| Schedule adherence | | ratio | | | |

Cost variance: planned minus actual. Actual above planned gives a negative variance, meaning the
project is over budget. Actual below planned gives a positive variance, meaning under budget.

Schedule adherence: a task planned for 10 days and completed in 10 days demonstrates high
schedule adherence.

## 4. Defect root cause distribution

Where the process is leaking. This table is the single most useful thing in the report.

| Root cause phase | Count | % | Change since last period |
| --- | --- | --- | --- |
| 01 Requirements | | | |
| 02 Design | | | |
| 03 Interface | | | |
| 04 Construction | | | |
| 05 Verification gap | | | |
| 06 Configuration / environment | | | |
| 10 Third-party | | | |
| 11 Communication / handoff | | | |

## 5. Prevention ratio

```
defects found before G5 (prevention) : defects found after G5 (detection) : found in production
```

Rising prevention ratio means the process is working. Falling means it is decaying, and `DOCTOR`
mode is due.

## 6. Decisions this report supports

| Metric | Reading | Decision recommended |
| --- | --- | --- |

A metric with no decision attached does not belong in this report. Delete it and stop collecting
it.

## 7. Data quality caveats

State what is unmeasured, what is estimated, and what is unreliable. A metrics report that
presents estimates as measurements violates Article 2.
