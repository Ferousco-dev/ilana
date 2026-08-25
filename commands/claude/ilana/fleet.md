---
description: Ìlànà FLEET mode. Up to 13 specialist agents running the full gated lifecycle.
argument-hint: <what you are building>
---

Run Ìlànà in `FLEET` mode. Read `~/.claude/skills/ilana/SKILL.md`, `modes/fleet.md` and
`agents/FLEET.md`.

Skip the fork question; the user has already chosen FLEET.

What they are building: $ARGUMENTS

**Before spawning anything**, print the plan and get a yes. Fleet mode is expensive and surprising
the user with it is rude. The plan states: project, process style, rigour, phases, agent roster with
a count, gates, the artifacts that will be produced, and a rough estimate of turns.

Offer the trimmed variant in the same message if rigour lands at 1 or 2: phases 01, 02, 04, 05, 06
only; agents `analyst`, `architect`, `constructor`, `verifier`, `configuration-engineer`; gates G1,
G4, G5.

Then run the intake interrogation before the first phase.

**Runtime.** If you have a sub-agent capability, use the wave structure in `modes/fleet.md`. If you
do not, or if the user says `rotate, do not spawn`, run the fleet as a sequential role rotation in
one context. The artifacts and gates are identical; only the wall-clock differs. Say which runtime
you are using.

**Throughout:**
- Announce every phase entry, every gate attempt and every agent switch, using the `[agent]` prefix.
- Emit a full handoff block at every transition. The receiving agent must address or explicitly
  defer every open item.
- A gate passes on evidence, never on assertion.
- A gate that fails twice stops the run and escalates rather than remediating a third time.
- `ethics-officer` is resident and may halt any wave.
