# Process Compliance Audit Report

An audit examines whether the team is following required standards, procedures and policies. It
is not a review of technical content, and it is performed by someone independent of the team
being audited.

| Field | Value |
| --- | --- |
| Audit ID | AUD-### |
| Scope | |
| Auditor | (must be independent of the delivery team) |
| Independence basis | reports to, not a member of the delivery team |
| Date | |
| Standards audited against | |

## 1. Method

What was examined: documents, repository, pipeline configuration, records, interviews. State the
sample, not just the conclusion.

## 2. Compliance findings

| # | Requirement of the standard | Expected | Observed | Compliant | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | Quality plan exists before construction | dated before first commit | | | |
| 2 | Requirements reviewed before design | review record exists | | | |
| 3 | Code review required before merge | branch protection configured | | | |
| 4 | Test plan predates test execution | dates compared | | | |
| 5 | Defects have all nine fields | sampled 10 defects | | | |
| 6 | Every closed defect names a regression test | sampled | | | |
| 7 | Changes traceable to a CR or REQ | sampled 10 commits | | | |
| 8 | Releases tagged and reproducible | tag list, build log | | | |
| 9 | Documentation under version control | | | | |
| 10 | Metrics collected in all three categories | `.ilana/metrics.csv` | | | |

## 3. Non-conformances

| ID | Non-conformance | Severity | Standard clause | Owner | Due | Status |
| --- | --- | --- | --- | --- | --- | --- |
| NC-01 | | major / minor / observation | | | | |

**Major**: the control does not exist or is not operating.
**Minor**: the control exists and operates, with lapses.
**Observation**: not a non-conformance; an improvement opportunity.

## 4. Positive findings

Mandatory section. At least three. An audit that only finds fault is an audit the team learns to
route around.

## 5. Conclusion

Overall compliance statement, in one paragraph, with the sample size that supports it.

## 6. Follow-up

| Non-conformance | Corrective action agreed | Verification date | Verified |
| --- | --- | --- | --- |

Auditor signature: ______________________
Audited party acknowledgement: ______________________
