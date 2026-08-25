# PROTOCOL: ESCALATION

Triggered when: a gate has failed twice, work is blocked, a conflict cannot be resolved, or an
ethics halt is raised.

**Do not guess your way past a blocker.** Guessing is how a small problem becomes an expensive one.

## Step 1: State the block precisely

```
BLOCKED
  phase:     05 Verification
  gate:      G5, attempt 2 of 2
  what:      integration tests cannot run
  because:   the test environment has no message broker, and the design assumes one
  tried:     in-memory substitute (behaviour differs), mocking (would not test the boundary)
  needs:     a broker in the test environment, or an explicit decision to accept the gap
  cost of waiting: verification of 6 requirements cannot proceed
```

Vague blockers do not get unblocked. Precision is the request.

## Step 2: Classify

| Class | Means | Goes to |
| --- | --- | --- |
| Information | a fact is missing | the person who has it |
| Decision | someone must choose | the accountable person in the RACI |
| Resource | something is unavailable | `conductor` |
| Capability | nobody here knows how | domain expert, or Article 9 disclosure |
| Conflict | two positions | `protocols/conflict-resolution.md` |
| Ethics | Article 1, 7 or 8 | `ethics-officer`, then the human user |
| Process | the gate itself is wrong for this project | `conductor`, and consider the rigour setting |

The last class is real and often overlooked. A gate that keeps failing on a criterion that does not
make sense for this project is a rigour problem, not a quality problem. Say so rather than
grinding.

## Step 3: Offer options, not just the problem

Never escalate a problem without at least two options and a recommendation.

```
Options:
  A. Add a broker to the test environment.  ~1 day.  Removes the gap entirely.
  B. Accept the gap, test the boundary in staging only.  0 days.  Boundary defects
     surface one environment later, where they cost more.
  C. Redesign to remove the broker dependency.  ~1 week.  Out of proportion here.

Recommendation: A. The boundary is where the payment reconciliation happens, and B moves
exactly that risk to production.
```

## Step 4: Time-box the wait

State when you will proceed on an assumption if no answer arrives, and what that assumption will
be. An escalation with no deadline becomes a silent stall.

```
If no answer by <date>, Ìlànà will proceed with option B, record the gap as an accepted
risk in the G5 record, and continue to phase 06.
```

## Step 5: Record

Every escalation is a ledger entry. Escalations that recur are a `DOCTOR` mode signal: the same
blocker three times means the process, not the blocker, is the problem.

## Ethics escalations are different

An ethics halt does not go to `conductor`. It goes directly to the human user, with the finding,
the article, and the legitimate alternatives. `conductor` cannot lift it, and Ìlànà does not argue
the point twice.
