# PROTOCOL: HANDOFF

The only legal way to move work between agents or phases. Most workflow failures are handoff
failures, so this is short and strict.

## Format

```
HANDOFF
  from:     <agent>
  to:       <agent>
  gate:     <G-n> PASSED | OVERRIDDEN | n/a
  produced: <paths of every artifact created or changed>
  ids:      <identifier ranges created>
  open:     <every unresolved item, with its id>
  assumed:  <every assumption made, with its DEC id>
  next:     <the specific first action for the receiving agent>
```

## Rules

1. **`open` is never "none" unless it is genuinely none.** An empty open list on a substantial
   piece of work usually means the sender did not look.
2. **The receiver must address or explicitly defer every open item.** Silently inheriting an open
   conflict is a process violation, and it is precisely how a requirements ambiguity becomes a
   production defect three phases later.
3. **`assumed` is where honesty lives.** Every assumption that would change the work if wrong goes
   here, with its `DEC` id.
4. **`next` is one specific action**, not a description of the receiver's job.
5. **Artifacts are paths, not descriptions.** "Wrote the SRS" is not a handoff; `docs/srs.md` is.

## Worked example

```
HANDOFF
  from:     analyst
  to:       architect
  gate:     G1 PASSED
  produced: docs/srs.md, .ilana/traceability.csv, docs/elicitation-plan.md
  ids:      REQ-001..REQ-024, NFR-001..NFR-009, DOM-001..DOM-003
  open:     REQ-017 conflicts with NFR-004 (latency vs report richness). Not resolved.
            Stakeholder decision needed before the reporting subsystem is designed.
  assumed:  DEC-005 peak concurrency 5000, unconfirmed by the operations team.
            DEC-006 fine schedule in DOM-002 will not change this academic year.
  next:     decompose REQ-001..REQ-012 into DES elements. Hold the reporting subsystem
            until REQ-017 is resolved.
```

The receiving agent's first response addresses the open item explicitly:

```
[architect] Received. REQ-017 blocks DES work on reporting; holding that subsystem and
proceeding on REQ-001..REQ-012. Escalating REQ-017 to conductor for a stakeholder session.
DEC-005 affects the caching design directly; I will design for 5000 and flag the
sensitivity in the ADR.
```

## Phase handoffs versus agent handoffs

A **phase** handoff always carries a gate verdict. An **agent** handoff inside a phase does not,
but is otherwise identical. Both are recorded in the ledger.

## When there is no receiving agent

At the end of a `TASK` run, the handoff is to the user:

```
HANDOFF
  from:     verifier
  to:       user
  produced: docs/test-plan.md
  open:     no requirements register exists, so coverage claims in section 9 are UNVERIFIED
  assumed:  DEC-001 the four testing levels all apply; correct this if acceptance is out of scope
  next:     the highest-value follow-up is a lightweight requirement register, so the
            coverage claims become checkable
```
