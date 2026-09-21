---
description: Ìlànà MAINTAIN mode. Change an existing repository safely with the least paperwork and the most verified evidence.
argument-hint: [what to change or which milestone to continue]
---

Run Ìlànà in `MAINTAIN` mode. Read `~/.claude/skills/ilana/SKILL.md`, `modes/maintain.md`,
`protocols/checkpoint.md` and `protocols/scope-guard.md`.

Task: $ARGUMENTS

Follow the procedure in `modes/maintain.md` exactly:

1. Orient with `.ilana/handoff.json` (if present) and `repo_map.py map`. Do not read the whole ledger.
2. Reality check: verify claims in the prompt, roadmap and earlier reports against git, code,
   migrations and tests. The repository wins; record each disagreement.
3. Snapshot the working tree with `repo_map.py snapshot`. Files that were already dirty are not
   yours and stay byte-identical.
4. Generate the privacy checklist with `privacy_scan.py scan` and carry relevant rows forward.
5. Specify at the ceremony level (`light`, `standard`, `regulated`; default `standard`).
6. Implement the smallest change. Report unrelated bugs; do not fix them unless required.
7. Run every check through `evidence.py run` and cite `EV-###` ids, never pasted output.
8. `repo_map.py guard` must exit 0. Update Ilana with `evidence.py handoff`.
9. Validate the commit message with `evidence.py commit-check`. Never add AI or co-author
   attribution. Stage only intended files. Do not push unless asked.
10. Report with `evidence.py report`, then STOP. Do not start anything in the stop boundary.

Ask at most three intake questions, and only if `.ilana/policy.json` does not exist.
