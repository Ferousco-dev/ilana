# G6 - RELEASE READINESS

Owner: `release-manager`. Closes: phase 06. Opens: phase 07 Quality assurance.

The go/no-go gate. This is where configuration management, verification and operations meet.

## Criteria

| # | Criterion | Rigour | Evidence |
|---|---|---|---|
| 1 | All source under version control, nothing local-only | R1+ | `git status` clean, no untracked source |
| 2 | Release is built from a tagged commit, reproducibly | R1+ | tag name, build log |
| 3 | Release type classified: major, minor, patch, emergency | R1+ | `CHANGELOG` entry |
| 4 | Build is automated, not hand-assembled | R2+ | build tool config |
| 5 | A written rollback plan exists and has been rehearsed at least once | R2+ | `docs/rollback.md` plus a dated rehearsal note |
| 6 | Every change in the release traces to a `CR` or a `REQ` | R2+ | changelog to ticket mapping |
| 7 | Branching strategy documented and followed | R2+ | `docs/scm-plan.md` |
| 8 | CI pipeline green: build, tests, static analysis, security scan | R3+ | pipeline run URL or log |
| 9 | Deployment environments reproducible from source, no manual drift | R3+ | infrastructure as code |
| 10 | Post-release monitoring defined: what is watched, by whom, and the alert threshold | R3+ | `docs/runbook.md` |
| 11 | Change advisory approval recorded | R4+ | approver, date |
| 12 | Deployment rehearsed in a staging environment matching production | R4+ | staging run record |
| 13 | Automated rollback triggered by monitoring, not by a human noticing | R5 | pipeline config |
| 14 | Independent release authorisation, separate from the implementing team | R5 | named authoriser |

## The environment-drift question

Ask it every time, because the source material identifies environment mismatch as the classic
deployment failure:

> Can you rebuild the production environment from source, from scratch, with no human
> remembering a step? If not, what is the step that only lives in someone's head?

## Change classification

Every item in the release is one of the four types of software change:

| Type | Meaning | Risk posture |
| --- | --- | --- |
| Corrective | fixes a fault | needs a regression test proving the fault is gone |
| Adaptive | fits a new environment | needs environment-matrix testing |
| Perfective | improves what already works | needs a before and after metric (Article 10) |
| Preventive | forestalls a future fault | needs a stated hypothesis about the fault prevented |
