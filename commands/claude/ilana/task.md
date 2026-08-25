---
description: Ìlànà TASK mode. One specialist, one operation, one artifact. The mode you want most days.
argument-hint: <what you want, e.g. "write a test plan for the payments service">
---

Run Ìlànà in `TASK` mode. Read `~/.claude/skills/ilana/SKILL.md` and `modes/task.md`.

Skip the fork question; the user has already chosen TASK by invoking this command.

The request: $ARGUMENTS

Follow the task procedure exactly:

1. **Classify.** Map the request to a phase and an agent using the routing table in
   `modes/task.md`. State the mapping in one line, for example:
   `[TASK] phase 05 Verification, agent verifier, artifact test plan.`
2. **Interrogate.** Up to five questions, one batch, from that phase's `questions.md`. Read the
   repository first; never ask what the files can tell you.
3. **Load.** Read only that phase's `PHASE.md`, the relevant template, and the agent card. Do not
   read the whole tree.
4. **Produce.** Write the artifact to a file in the repository, not into chat.
5. **Self-gate.** Run that phase's `checklist.md` against your own output and report the score
   honestly.
6. **Record.** One line appended to `.ilana/ledger.md`.
7. **Offer.** Name the single most valuable next task.

If the artifact depends on something that does not exist (a test plan with no requirements to trace
to), say so plainly, state what will be `UNVERIFIED` as a result, and offer to build the missing
piece first. Offer the fleet once, as a fact plus an option, without pushing.
