# WORKED EXAMPLE: AUDIT MODE

Scoring an existing repository. Read-only. One artifact produced.

---

> User: audit this repo with ilana

```
Ìlànà v1.0.0 online.

AUDIT selected. Read-only: nothing in your repository will be modified.
Crew: quality-auditor (lead), metrologist, configuration-engineer, verifier,
ethics-officer (resident).

Gathering evidence from the repository rather than asking you. Back shortly.
```

```
[quality-auditor] Evidence gathered.

  git log --oneline | wc -l                     847
  git branch -a                                 main, 14 others, 9 stale over 60 days
  git tag                                       none
  find . -type d -name 'test*'                  ./tests (4 files)
  ls .github/workflows                          ci.yml
  ls docs                                       (no such directory)
  grep -c conventional commit prefixes          31 of 200 sampled
  grep -c commits referencing a ticket           6 of 200 sampled
```

---

## The scorecard

```
| Phase | Score | Evidence | Gap |
| 01 Requirements       | 0 | no docs/, no acceptance criteria in issues | requirements exist only in people's heads |
| 02 Architecture       | 1 | module boundaries visible, nothing written | structure is accidental, not designed |
| 03 Interface          | 2 | component library, consistent styling | no error catalogue, no accessibility config |
| 04 Construction       | 2 | eslint config, prettier, CI runs both | no written standard, no CODEOWNERS |
| 05 Verification       | 1 | 4 test files, unit only, CI runs them | no integration level, no test plan, no defect log |
| 06 Configuration mgmt | 1 | git in use, CI exists | no tags, no changelog, no rollback, 9 stale branches |
| 07 Quality assurance  | 0 | no reviews required, no metrics | quality is unmanaged |
| 08 Process assessment | 0 | no data of any kind | CMMI level 1 |
| 09 Process modeling   | 1 | README explains how to run it | no diagrams, no runbook, knowledge is tribal |
| 10 Tooling            | 2 | CI exists and runs | no security scanning, no dependency automation |
| 11 Ethics and teams   | 1 | LICENSE present | no SECURITY.md, no dependency licence record |

Mean 1.0.  Indicative CMMI level 2 Managed (partial). Not a formal appraisal.
```

---

## Findings, ranked by cost of inaction

```
F-01 [critical]  No release tags.
     Evidence: `git tag` returns nothing across 847 commits.
     Cost of inaction: you cannot say what is in production, and you cannot roll back
     to a known good state. This is the finding that will hurt you first.
     Fix: tag the current production commit today. Tag every release from now on.
     Effort: 5 minutes, then 5 seconds per release.

F-02 [critical]  No integration test level.
     Evidence: 4 test files, all unit, in a codebase with 6 service boundaries.
     Cost of inaction: interface defects between services are found by users.
     Fix: one integration test per boundary. Start with the two that handle money.
     Effort: 2 days.

F-03 [high]      Nothing traces to anything.
     Evidence: 6 of 200 sampled commits reference a ticket or requirement.
     Cost of inaction: nobody can answer "why does this code exist" for most of the
     codebase, which makes deletion impossible and changes risky.
     Fix: commit message convention with a Refs line. Enforce in CI.
     Effort: 1 hour to set up.

F-04 [high]      No rollback procedure.
     Evidence: no docs/, no deploy scripts with a reverse path.
     Cost of inaction: an outage lasts as long as it takes to improvise.
     Fix: write it, then rehearse it once. The rehearsal is the part that matters.
     Effort: half a day.

F-05 [medium]    Nine branches stale over 60 days.
     Cost of inaction: merge conflicts compound, and nobody knows which are alive.
     Fix: merge, close, or document each one. Then set a staleness policy.

F-06 [medium]    No security scanning in CI.
F-07 [medium]    No dependency licence record.
F-08 [low]       No CODEOWNERS, so review assignment is ad hoc.
```

---

## What is already good

Mandatory section. An audit that only finds fault gets routed around.

```
1. CI exists, runs on every pull request, and runs both the linter and the tests. Many
   repositories at this maturity have neither.
2. The linter and formatter are configured and enforced mechanically, which is better than
   a written standard nobody applies.
3. Module boundaries are visible and coherent even though nobody documented them, which
   suggests whoever built this had a design in mind. Writing it down is cheap from here.
4. The README genuinely explains how to run the project. That is rarer than it should be.
```

---

## Remediation plan

```
THIS WEEK       (2 hours total, disproportionate return)
  1. Tag the production commit.                                   F-01
  2. Add a commit message convention and enforce it in CI.        F-03
  3. Add secret scanning to the pipeline.                         F-06

THIS MONTH      (3 days)
  4. Integration tests for the two money-handling boundaries.     F-02
  5. Write and rehearse a rollback procedure.                     F-04
  6. Triage the nine stale branches.                              F-05

THIS QUARTER    (1 week, spread)
  7. Reconstruct a lightweight requirement register from behaviour.  F-03
  8. Add CODEOWNERS and require review on protected paths.          F-08
  9. Record dependency licences.                                    F-07
```

---

```
[conductor] Audit complete. Written to docs/ilana-audit.md.
Nothing else in your repository was modified.

Next: `ilana` in TASK mode can do items 1, 2, 3 and 5 now if you want them.
Say which, or say all four.
```

---

## What audit mode deliberately does not do

- It does not modify anything without `--fix` and a change request per fix.
- It does not moralise. Every finding is a gap and a cost, not a judgement.
- It does not rank by distance from the textbook. It ranks by what will hurt first.
- It does not omit what is working, because an audit that only finds fault gets ignored.
