---
description: Ìlànà AUDIT mode. Score this repository against all 11 phases. Read-only.
argument-hint: [path, defaults to the current repository]
---

Run Ìlànà in `AUDIT` mode. Read `~/.claude/skills/ilana/SKILL.md` and `modes/audit.md`.

Target: $ARGUMENTS (default: the current repository)

**This mode is read-only.** Change nothing except writing the single report file. Do not fix
anything, do not reformat anything, do not open pull requests.

Gather evidence from the repository rather than asking the user. Run the read-only commands listed
in `modes/audit.md`, and check for the signals in its evidence table: requirements documents,
design documents, module boundaries, linter configuration, test directories and levels, branch and
tag state, commit message quality, CI configuration, review requirements, metrics of any kind,
diagrams and runbooks, licence and security files.

Then:

1. **Score each of the eleven phases 0 to 4** using the scale in `modes/audit.md`, with the evidence
   that supports each score and the specific gap.
2. **Derive an indicative CMMI level** from the mean, and say plainly that it is indicative and not
   a formal appraisal.
3. **Write findings ranked by cost of inaction**, not by distance from the textbook. Each finding
   carries: evidence, cost of inaction stated concretely, the fix, and the effort.
4. **Name at least three things that are already good.** This section is mandatory. Audits that only
   find fault get routed around.
5. **Produce a remediation plan** across three horizons: this week, this month, this quarter,
   ordered by impact divided by effort.

Write it to `docs/ilana-audit.md`. Then offer to do the cheapest one or two findings in TASK mode.
