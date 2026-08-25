# Workflow Definition Template

```markdown
# Workflow: <name>

| Field | Value |
| --- | --- |
| Purpose | |
| Owner | |
| Trigger | what starts this workflow |
| Service level | expected end-to-end duration |

## Activities
| # | Activity | Role | Input | Output | Duration | Exit condition |
|---|---|---|---|---|---|---|

## Roles
| Role | Responsible for | Must not |
|---|---|---|

## Decision points
| Decision | Condition | Path if yes | Path if no | Decided by |
|---|---|---|---|---|

## Handoffs
| From | To | What is handed over | How it is confirmed |
|---|---|---|---|

The handoff table is the one that matters most. Most workflow failures are handoff failures.

## Exceptions
| Exception | Detection | Handling | Escalation |
|---|---|---|---|

## Metrics
| Metric | Target | Current |
|---|---|---|
| Cycle time | | |
| Rework rate | | |
| Queue time at the slowest step | | |
```

## The canonical software development workflow

```
Requirements -> Analysis -> Design -> Implementation -> Testing -> Deployment -> Maintenance
```

| Step | What happens |
| --- | --- |
| Requirements | gather user needs and business objectives |
| Analysis | study requirements and assess feasibility |
| Design | create system architecture and detailed designs |
| Implementation | develop source code |
| Testing | verify software correctness |
| Deployment | release software to users |
| Maintenance | fix defects and implement improvements |

## Other workflows worth defining explicitly

Teams usually define the development workflow and leave these implicit, which is where the
delays actually accumulate.

| Workflow | Why it needs a definition |
| --- | --- |
| Defect triage | who sets severity and priority, and how fast |
| Change request | Article 11; impact analysis before approval |
| Code review | who reviews, what blocks, how fast |
| Release | go/no-go, authorisation, rollback trigger |
| Incident response | detection, escalation, communication, post-incident review |
| Onboarding | how a new engineer becomes productive, and by when |
