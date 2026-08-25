# ADR-###: <short decision title>

| Field | Value |
| --- | --- |
| Status | proposed / accepted / superseded by ADR-### / deprecated |
| Date | |
| Deciders | |
| Ledger ID | DEC-### |

## Context
The forces at play. What makes this a decision rather than an obvious choice. Include the
specific `REQ` and `NFR` identifiers that constrain it.

## Options considered

### Option A: <name>
- How it works, in three sentences.
- Satisfies: NFR-002 (yes, by X), NFR-005 (partially, because Y)
- Costs: build effort, operational burden, licence, team learning curve
- Risks:

### Option B: <name>
(same shape)

### Option C: do nothing / keep the current approach
Always include this option. Its cost is the baseline everything else is compared against.

## Decision
We chose <option>.

## Reasons
The specific reasons, ranked. Not a list of the option's virtues: the reasons *this* option
beat *those* options for *this* system.

## Consequences

**Accepted:**
- what becomes harder as a result

**Rejected options remain rejected because:**
- the specific condition under which we would revisit each one

## Revisit trigger
The observable condition that should make someone reopen this decision.
Example: "if median write latency exceeds 200ms or write volume exceeds 5000/s, revisit
Option B."

An ADR with no revisit trigger becomes a permanent constraint by accident.
