# ARCHITECTURE

Why Ìlànà is shaped the way it is.

---

## The problem

A coding agent given a task will do the task. That is the failure mode.

Ask for a login form and you get a login form: no requirement written down, no acceptance
criterion, no thought about what happens when the password reset email bounces, no test for the
locked-account path, no record of why the session timeout is thirty minutes. It works, it ships,
and six months later nobody can safely change it.

The gap is not capability. It is **process**. Ìlànà supplies the process.

---

## The shape: an operating system, not a checklist

Most engineering skills are a list of things to remember. Lists degrade: the model reads them,
retains the first three, and the rest evaporate under context pressure.

Ìlànà is structured as a small operating system instead:

```
  SKILL.md         boot loader     always read, deliberately short
      |
  kernel/          mechanism       invariant across projects, languages, teams
      |
  modes/           scheduler       which programme runs
      |
  gates/           enforcement     the part that says no
      |
  phases/          programmes      loaded one at a time, on demand
  agents/          processes       roles adopted, with charters and refusals
  protocols/       system calls    repeatable cross-phase procedures
  instruments/     drivers         measurement
  references/      manuals         lookup, not read-through
  interrogation/   input           how it asks
      |
  .ilana/          filesystem      the user's project, the source of truth
```

Three properties follow from this shape:

**Shardable.** No invocation reads the whole tree. Boot reads `SKILL.md`, the kernel and one mode.
A phase adds one `PHASE.md` and one template. Total context per operation stays small even though
the payload is large.

**Resumable.** State lives in `.ilana/`, not in the conversation. A session can end anywhere and
another agent, another model, another human can pick it up from the ledger.

**Degradable.** Every layer states what it does without the layer below. No sub-agents: rotate
agent cards. No filesystem: emit fenced blocks. No Python: manual procedures. Nothing is a hard
dependency except reading, writing and talking.

---

## Why a constitution rather than instructions

Instructions get weighed against each other under pressure. "Write tests" competes with "the user
is in a hurry" and often loses.

The constitution is **ordered by precedence**. Article 1 beats Article 16. When public interest
conflicts with the schedule, there is no weighing to do; the ordering already decided it. This
converts a judgement call into a lookup, which is exactly what you want under pressure.

Sixteen articles is more than a slogan and fewer than a policy manual. Nine of them are carried in
`SKILL.md` as the short form, because those are the ones needed in working memory at all times.

---

## Why gates rather than advice

Advice is free to ignore, and advice that is always ignored trains people to ignore advice.

A gate has four properties advice lacks:

1. **A name.** You can say "we did not pass G4" and everyone knows what that means.
2. **Explicit criteria.** Not "is the code good" but "does a coding standard exist, is it enforced,
   are there secrets, was there a peer review".
3. **Evidence.** A gate passes on artifacts and numbers, never on an agent's confidence.
4. **A record.** Including overrides, with their reasons.

The last one is the one that changes behaviour. An override is easy; an override that appears in a
permanent record with your reason next to it is a decision you make deliberately.

---

## Why rigour is a dial

The source material is explicit that no single process fits all projects, and a process tool that
ignores this gets uninstalled by the second project.

`RIGOUR` 1 to 5 scales every gate criterion. The *phases* never disappear, which is the important
part: even at rigour 1 you are asked what problem you are solving and whether anyone gets hurt if
it is wrong. What changes is the ceremony, not the thinking.

This is Article 13 made operational, and it is the single design decision that determines whether
the tool survives contact with real work.

---

## Why thirteen agents

Not for parallelism. For **separation of duties**.

The value of `verifier` is not that it tests faster; it is that it does not fix what it raised, so
the confirmation is independent. The value of `quality-auditor` is not that it reviews better; it
is that it does not audit its own work. The value of `ethics-officer` is that it can stop the run
and `conductor` cannot overrule it.

These are the same controls that exist in real engineering organisations, and they exist for the
same reason: a single actor evaluating its own work is not a control.

On a small team, or on a host with no sub-agents, one context holds all thirteen roles in turn.
The separation is then maintained by discipline rather than by process boundaries, which is
weaker, and Ìlànà says so rather than pretending otherwise.

---

## Why the ledger is plain text in the user's repository

Three reasons.

1. **It is theirs.** Process history is project history. It should outlive Ìlànà, this model, and
   this vendor.
2. **It is diffable.** A process record you cannot review in a pull request is not a record.
3. **It is portable.** Another agent, or a human, can pick up the run from the ledger alone.

`.ilana/` is deliberately boring: markdown and CSV. No database, no lock file, no proprietary
format. If Ìlànà disappeared tomorrow, `.ilana/` would still be readable and still be useful.

---

## Why the boot fork is mandatory

Two failure modes, and the fork prevents both.

**Under-serving.** The user asks to "build a system", the agent writes some code, and none of the
process happens. This is the common case and it is what Ìlànà exists to prevent.

**Over-serving.** The user asks for a test plan and gets a thirteen-agent lifecycle with nine
gates. This is the failure that makes people uninstall process tools, and it is more damaging than
the first because it destroys trust in the whole idea.

Asking costs one turn. Guessing wrong costs the relationship.

---

## Why it interrogates

The most expensive defects in software originate in requirements, and requirements defects
originate in questions nobody asked.

The question engine is deliberately constrained: batched, budgeted, and required to change an
artifact. An agent that asks twenty questions before starting is as unusable as one that asks none.
Five, in one batch, with an explicit assumption fallback, is the balance.

Two questions are never skipped, at any rigour, in any mode: who is harmed if this is wrong, and
what happens to a person if this data leaks. Everything else is negotiable.

---

## Where the content comes from

Every phase reference is derived from SEN102/212 Software Engineering Process at Obafemi Awolowo
University, Ile-Ife. The complete deck is in `source/`.

What Ìlànà adds on top:

| Course material | Ìlànà addition |
| --- | --- |
| the five requirements stages | gate criteria, the adjective grep, the read-back loop |
| the three design levels | the NFR mechanism table, the both-way orphan check |
| the five UI principles | each restated as a test you can fail |
| coding standards and guidelines | how to adapt 80-character lines and 10-line functions honestly |
| the four testing levels | the coverage trap, the regression-test closure rule |
| SCM four pillars | the rollback rehearsal requirement, the environment-drift question |
| SQA five activities | the review-type honesty rule, `UNVERIFIED` as a legitimate score |
| CMMI five levels | the three boundary tests, indicative-not-appraisal discipline |
| process modeling notations | Mermaid encodings that render and diff |
| CASE and PM tools | the stale-board rule, the pipeline-as-enforcement-surface position |
| ACM/IEEE ethics | the refusal protocol, and an explicit list of what is *not* refused |

The course supplies the vocabulary and the standards. Ìlànà supplies the enforcement.
