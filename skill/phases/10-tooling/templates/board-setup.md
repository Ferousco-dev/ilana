# Project Board Configuration

Configure the tool to the process, never the reverse. Define the workflow in phase 09 first,
then build the board to match it.

## 1. Workflow states

State the **real** workflow. If work genuinely waits in a review queue, "In Review" is a state,
because otherwise the queue is invisible and nobody can fix it.

| State | Means | Entry condition | Exit condition | WIP limit |
| --- | --- | --- | --- | --- |
| Backlog | specified, not started | has a requirement ID | prioritised | none |
| Ready | ready to be picked up | acceptance criteria written | picked up | |
| In Progress | actively being worked | assigned | code complete | per person |
| In Review | waiting for or in review | PR opened | approved | |
| In Test | verification in progress | merged to the test branch | tests pass | |
| Done | shippable | acceptance criteria demonstrated | released | none |

**WIP limits are the point of a Kanban board.** Without them it is a to-do list with columns.
Limiting work in progress reduces bottlenecks and improves flow efficiency.

## 2. Item types

| Type | Used for | Must carry |
| --- | --- | --- |
| Epic | a body of work spanning releases | business objective |
| Story / task | a unit of deliverable work | requirement ID, acceptance criteria |
| Defect | something that is wrong | all nine defect fields |
| Change request | a change to agreed scope | impact analysis before approval |
| Spike | time-boxed investigation | the question it answers, and a time box |

## 3. Required fields

Keep this list short. Every mandatory field is friction, and friction is why boards go stale.

| Field | Required on | Why |
| --- | --- | --- |
| Requirement ID | story, task | traceability, Article 3 |
| Acceptance criteria | story | definition of done |
| Severity | defect | triage |
| Priority | defect | triage |
| Owner | everything in progress | accountability |

## 4. Definition of done

One list, applied to everything, visible on the board.

- [ ] Acceptance criteria demonstrated
- [ ] Code reviewed and approved
- [ ] Tests written and passing; test IDs recorded
- [ ] Documentation updated
- [ ] Traceability row updated
- [ ] Merged and deployed to staging

## 5. Reports and the decision each supports

| Report | Decision it informs |
| --- | --- |
| Cumulative flow | where work is queueing, so the bottleneck can be relieved |
| Cycle time distribution | whether commitments are realistic |
| Burndown or burnup | whether the current iteration will land |
| Defect ageing | whether triage is keeping up |

A report nobody acts on is switched off.

## 6. Staleness policy

An item untouched for longer than an agreed window is flagged. The board's value is entirely
dependent on its truthfulness; the source material is explicit that incorrect updates lead to
misleading reports and decisions.

| Window | Action |
| --- | --- |
| 3 days in progress with no update | flag at standup |
| 2 weeks in any active state | escalate or return to backlog |
| Item nobody can explain | delete it |
