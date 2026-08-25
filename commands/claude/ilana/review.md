---
description: Ìlànà code review against the project's coding standard and gate G4.
argument-hint: [branch, commit range, or path; defaults to the working diff]
---

Run an Ìlànà code review. Read `~/.claude/skills/ilana/SKILL.md`, `gates/G4-construction.md` and
`protocols/review-inspection.md`.

Target: $ARGUMENTS (default: the uncommitted working diff, or the diff against the default branch)

Adopt the `constructor` agent card for standards, and `quality-auditor` for review discipline.

First, get the diff:

```bash
git diff --stat
git diff
```

**Record what kind of review this actually is.** A peer review, a walkthrough and an inspection are
different activities with different formality and different roles. Calling a walkthrough an
inspection corrupts the quality evidence. This is a peer review unless the user says otherwise.

Review against the checklist in `phases/04-construction/templates/code-review.md`:

- Does every change trace to a requirement or a change request?
- Is the project's coding standard followed, or is the deviation justified?
- Is every failure path handled or deliberately propagated, with no swallowed exceptions?
- Any secrets, keys or credentials introduced? Run the secret scan from `gates/G4-construction.md`.
- Is untrusted input validated at the boundary named in the design?
- Are tests added or updated, and would the test fail without this change?
- Any dead code, commented-out blocks, or leftover debugging output?
- Are error messages meaningful and consistent with the error catalogue?
- Is documentation updated where behaviour changed?

**Classify every finding** by class (defect, standard violation, ambiguity, omission, question) and
severity (major, minor). Counting findings by class over time is what tells the team where the
process leaks, and it is the input phase 08 needs.

Note honestly if the change is large and you found nothing. A substantial change with zero findings
is itself a finding: either the change was trivial or the review was not performed properly.

End with a verdict: approved, approved with minor findings, changes required, or rejected.
