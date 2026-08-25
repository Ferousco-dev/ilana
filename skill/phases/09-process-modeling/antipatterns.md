# PHASE 09 ANTI-PATTERNS

## The Aspirational Model
The diagram shows the process the team wishes it followed. Everyone recognises it as fiction and
stops consulting it.
**Fix:** accuracy is a stated characteristic of a good process model. Model reality first, label
the target state separately.

## The Diagram That Needs a Diagram
Sixty nodes, crossing lines, no swimlanes, printed on A3 and never read.
**Fix:** simplicity is a stated characteristic. Decompose into sub-processes, each fitting on one
screen.

## Documentation Written Once
Accurate on the day it was written, stale within a month, actively misleading within a year.
**Fix:** documentation is a configuration item. It changes with the code, in the same commit.

## The Missing Decision Condition
A diamond with two arrows out and no labels. The reader cannot tell which condition sends flow
which way.
**Fix:** condition text next to every decision marker. This is the notation's own rule.

## Implied Parallelism
Two activities drawn side by side with no fork, so nobody knows whether they run concurrently or
in either order.
**Fix:** fork and join nodes. If they are sequential in either order, say that explicitly.

## Documentation Nobody Can Find
Excellent documentation on someone's personal drive, in a chat thread, in a wiki nobody has
access to.
**Fix:** accessibility is a stated characteristic. It lives in the repository.

## BPMN for a Function
Full BPMN with pools, lanes, message flows and gateways, to describe a 30-line function.
**Fix:** match notation to audience. Activity diagram for software flow.

## Standards Cited but Not Followed
"Our SRS follows IEEE 830." It does not; someone read the name once.
**Fix:** if you cite the standard, follow its structure. If you deviate, say where and why.

## Documentation as an End-of-Project Task
Written after delivery, from memory, by whoever is left. It captures what people remember, which
is not what happened.
**Fix:** documentation starts before the process and runs through all phases. That is the
definition in the source material.
