# PROTOCOL: CONFLICT RESOLUTION

Two kinds of conflict, needing two different procedures. Confusing them is why so many technical
arguments become personal.

---

## A. Requirement conflict (two stakeholders want incompatible things)

One stakeholder wants richer reporting; another wants throughput. Both compete for the same
resources.

**Never resolve this unilaterally.** It is a business decision, not an engineering one.

1. **Document both positions** precisely, in each stakeholder's own words, with the requirement IDs.
2. **Make the incompatibility concrete.** Not "these conflict" but "satisfying REQ-014 at the
   stated volume makes NFR-004 unachievable at the stated latency; here are the numbers."
3. **Present the options**, with what each costs and what each gives up. Always include a hybrid
   and always include "do neither".
4. **Facilitate a joint session** if the stakeholders can be in a room. A facilitated workshop with
   both present resolves in an hour what asynchronous negotiation takes a month to fail at.
5. **Escalate to the person with authority** if consensus fails. That person is named in the RACI.
6. **Record the decision** as `DEC-###`, with the requirement that lost and why, so nobody
   relitigates it in three months.

---

## B. Technical disagreement (two engineers disagree about how)

Two architects disagree about microservices versus a monolith. Two developers disagree about an
approach.

**The mechanism, in order:**

1. **Agree the evaluation criteria first, before looking at the options.** This is the whole
   protocol. Criteria chosen after seeing the options are criteria chosen to favour a preferred
   option, and everyone in the room knows it.

   Typical criteria: does it satisfy the NFRs, can this team operate it, what does it cost to
   change later, what does it cost to run, how long to deliver, what is the failure mode.

2. **Score both options against the criteria**, objectively, with the person who proposed each
   option scoring the *other* one first.

3. **Run a time-boxed spike** where the disagreement is empirical rather than a matter of judgement.
   Half a day of measurement settles what a week of argument will not.

4. **The named decision-maker decides** where scoring does not converge. That is `architect` for
   design, `configuration-engineer` for process and tooling, `conductor` for anything cross-cutting.

5. **Record it as an ADR** with the alternatives, the criteria, the scores and the revisit trigger.

6. **Disagree and commit.** Once recorded, the losing party implements the decision fully. Silent
   non-compliance is worse than continued argument.

### What is prohibited

- **Seniority as an argument.** Seniority may make the final call after scoring; it is not itself
  a score.
- **Deadline pressure as an argument.** "We don't have time to discuss it" is a schedule decision
  masquerading as a technical one. Say which it is.
- **Choosing the first proposal by default.**
- **Ignoring the non-functional requirements** because they are inconvenient for a preferred option.

---

## C. When the conflict is really about something else

Sometimes a technical argument is a proxy for an unresolved ownership question, an unstated
constraint, or a resourcing dispute. Signals:

- the same argument recurs, unresolved, in different technical clothing,
- one party keeps changing the criteria,
- the argument continues after the data has settled the technical question.

Response: stop the technical discussion and name the underlying question. Almost always it is
"who owns this decision", and the answer belongs in the RACI, not in a design review.

---

## Recording

Every resolved conflict produces a `DEC-###` containing: the positions, the criteria, the
decision, the reason, and what would make us revisit. Conflicts resolved in conversation and never
written down are conflicts that will recur.
