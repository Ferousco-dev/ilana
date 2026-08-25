# Software Configuration Management Plan: <PROJECT>

| Field | Value |
| --- | --- |
| Owner | |
| Version | |
| Last reviewed | |

## 1. Configuration items

Everything under control. If it can differ between environments and change behaviour, it belongs
here.

| Item | Location | Owner | Baseline point |
| --- | --- | --- | --- |
| Source code | | | every release tag |
| Requirements (SRS) | `docs/srs.md` | analyst | G1 |
| Design description | `docs/design.md` | architect | G2 |
| Interface specification | `docs/ui-spec.md` | interaction-designer | G3 |
| Test plan and cases | `docs/test-plan.md` | verifier | G5 |
| Infrastructure definitions | | | |
| CI pipeline definitions | `.github/workflows/` | | |
| Database migrations | | | |
| Dependency lock files | | | |
| Process ledger | `.ilana/` | conductor | every gate |

## 2. Version control

| Setting | Value |
| --- | --- |
| System | Git (distributed) |
| Remote | |
| Default branch | |
| Branch protection | required reviews, required checks, no force push |
| Branching strategy | trunk-based / GitHub flow / Git flow / release branches |
| Merge policy | merge commit / squash / rebase |
| Tag format | `v<major>.<minor>.<patch>` |

### 2.1 Branch naming

| Purpose | Pattern | Lifetime |
| --- | --- | --- |
| Feature | `feat/<CR-id>-<slug>` | days, not weeks |
| Fix | `fix/<DEF-id>-<slug>` | days |
| Release | `release/<version>` | until released |
| Hotfix | `hotfix/<version>-<slug>` | hours |

### 2.2 Commit message convention

```
<type>(<scope>): <what changed, imperative, one line>

<why it changed, and what would break without it>

Refs: REQ-### / CR-### / DEF-###
```

## 3. Change control

| Question | Answer |
| --- | --- |
| Who may raise a change request | |
| Who performs impact analysis | |
| Who approves | |
| Approval threshold requiring escalation | |
| Emergency change procedure | |
| Where change records live | `.ilana/changes.md` |

## 4. Build

| Aspect | Value |
| --- | --- |
| Build tool | |
| Build command | |
| Reproducible from a clean checkout | yes / no |
| Dependency locking | |
| Artifact storage | |
| CI system | |
| CI stages | build, lint, unit, integration, security scan, package |

## 5. Environments

| Environment | Purpose | Provisioned from | Data | Who can deploy |
| --- | --- | --- | --- | --- |
| Local | | | synthetic | anyone |
| CI | | | synthetic | pipeline |
| Staging | | | anonymised | pipeline |
| Production | | | real | named people only |

Every difference between staging and production is listed, because each one is a class of defect
that testing will not find.

## 6. Release

| Aspect | Value |
| --- | --- |
| Cadence | |
| Versioning scheme | semantic versioning |
| Who authorises | |
| Release evidence retained | where, for how long |

## 7. Access control

| Role | Repository | Deploy to staging | Deploy to production | Approve release |
| --- | --- | --- | --- | --- |

## 8. Audit

How to answer, from records alone: what is in production, who put it there, when, under which
change request, and which tests passed against it.
