---
description: Boot Ìlànà, the software engineering process. Asks whether to run a fleet of specialist agents or a single focused task.
argument-hint: [what you are working on, optional]
---

Load the Ìlànà software engineering process and run its boot sequence now.

Read the skill definition at `~/.claude/skills/ilana/SKILL.md`. If that path does not exist, try
`~/.ilana-src/skill/SKILL.md`. If neither exists, tell the user Ìlànà is not installed and point
them at https://github.com/Ferousco-dev/ilana

Then execute the boot sequence in full, in order:

1. Announce that Ìlànà is online.
2. Look for `.ilana/` in the working directory. If present, read it and report the current phase,
   the last gate passed, and any open items. You are resuming, not starting.
3. **Ask the fork question.** Do not skip it, do not answer it yourself, and do not begin work
   until the user has chosen:
   - `[1] FLEET` a bundle of specialist agents running a full, gated lifecycle
   - `[2] TASK` one specialist, one focused operation, one artifact
   If the working directory is an existing repository and the request is to change, fix, continue
     or resume work, say "Reading this as MAINTAIN" and follow `modes/maintain.md` instead.
   Then mention the other modes in one line: MAINTAIN, AUDIT, TUTOR, DOCTOR, DRILL.
4. Run the intake interrogation from `interrogation/intake.md`. Five to nine questions, asked in
   **one batch**, never one at a time.
5. Set `RIGOUR` from the answers and say it out loud with your reason.

Context the user gave, which may already answer part of the intake: $ARGUMENTS

If that context clearly indicates a mode, say how you read it and let them correct you rather than
asking the fork question twice.
