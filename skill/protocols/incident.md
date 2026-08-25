# PROTOCOL: INCIDENT

Something is broken in production. Ìlànà's job during an incident is to be useful and quiet, and
its job afterwards is to make sure the lesson survives.

## During

**Restore service first. Diagnose second.** These are different activities and doing them in the
wrong order extends the outage.

1. **Declare.** Say out loud that this is an incident, who is coordinating, and where updates will
   appear. Ambiguity about whether this is an incident is itself a delay.
2. **Stabilise.** Roll back, fail over, disable the feature, shed load. The fastest path back to
   working, even if it is inelegant.
3. **Communicate.** A short update at a fixed cadence, even when the update is "no change yet".
   Silence generates more interruption than updates do.
4. **Record the timeline as you go.** Timestamps, actions taken, what was observed after each.
   Reconstructing this afterwards from memory produces fiction.
5. **Do not make speculative changes in parallel.** One change at a time, observed, or you will
   not know which one helped.

## Roles during an incident

| Role | Does |
| --- | --- |
| Coordinator | decides, communicates, protects the responders from interruption |
| Responder | investigates and acts, one at a time on shared systems |
| Scribe | maintains the timeline |
| Communicator | handles stakeholders and users |

On a small team one person holds several. The coordinator role is the one that must not be merged
with responder, because someone has to be watching the whole picture.

## After

A post-incident review within a few days, while memory is fresh.

```markdown
# Post-Incident Review: <title>

## Summary
What happened, in two sentences, in plain language.

## Impact
Who was affected, how many, for how long, and what they could not do.

## Timeline
| Time | Event | Who | Observed |

## Detection
How did we find out? If the answer is "a customer told us", that is the first finding.
Time from onset to detection: ___

## Root cause
Not the last change; the reason the last change was able to cause this.

## Contributing factors
The conditions that made this possible or made it worse.

## What went well
Mandatory. Include it.

## Gate analysis
Which Ìlànà gate should have caught this, and why it did not.
| Gate | Should have caught | Why it did not | Change proposed |

## Actions
| # | Action | Owner | Due | Prevents recurrence or reduces impact |

## Detection improvement
What would have told us sooner, and is it now in place?
```

## Rules

1. **Blameless.** Article 14. Name the missing mechanism, never the person. The moment reviews
   become blame, the timelines become inaccurate and the instrument is destroyed.
2. **Root cause, not last change.** "Someone deployed a bad config" is not a root cause; the root
   cause is that a bad config could reach production without a check.
3. **Every action has an owner and a date**, or it is a wish.
4. **Detection is a first-class finding.** An incident found by a customer is two failures.
5. **Feed it back into the gates.** A post-incident review that does not change a gate, a test, or
   a control will be repeated verbatim next quarter.
