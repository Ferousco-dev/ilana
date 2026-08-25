# PHASE 10 ANTI-PATTERNS

## Tool Before Process
Jira is adopted, then the team tries to work out what its workflow should be by configuring the
tool. The tool's defaults become the process, and nobody chose them.
**Fix:** define the workflow in phase 09, then configure the tool to match it.

## The Stale Board
Cards have not moved in three weeks. Standups happen from memory. Managers report from the board
anyway. The source material names this exactly: incorrect updates lead to misleading reports and
decisions.
**Fix:** make staleness visible. A board nobody updates is deleted, not tolerated.

## The Twenty-Minute Pipeline
CI takes long enough that developers stop waiting for it, merge anyway and check later.
**Fix:** budget the pipeline. Fast checks first, parallelise, split slow suites into a
post-merge stage.

## Automating the Wrong Thing
Two days spent automating a task performed monthly, while the four-day code review queue is
untouched.
**Fix:** measure where the time goes before choosing what to automate.

## The Unowned Tool
A tool that everyone depends on and nobody maintains. It breaks during a release.
**Fix:** every tool in the chain has a named owner inside the team.

## Tool Sprawl
Four trackers, three chat tools, two wikis. Information is somewhere, and finding it costs more
than the tools save.
**Fix:** one place per kind of information. Retire the rest properly, do not just stop using them.

## Security Scanning Configured to Pass
The scanner runs, findings are suppressed wholesale, the badge is green.
**Fix:** suppressions are individually justified with an expiry date. A blanket suppression is a
finding.

## Over-Configured Jira
Fourteen workflow states, nine mandatory custom fields, and a transition that requires a form.
People start working outside the tool because it costs too much to use.
**Fix:** the workflow should match the real process. If the real process has three states, the
tool has three states.

## CI That Does Not Block
The pipeline runs and reports, but merging does not require it to pass. Every control in phases
04, 05 and 07 becomes optional.
**Fix:** required checks on the protected branch at RIGOUR 3 and above.
