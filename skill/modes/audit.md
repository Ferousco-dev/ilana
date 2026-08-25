# MODE: AUDIT

Score an existing codebase and its process against the eleven phases. Produce a maturity
picture and a prioritised remediation plan. Change nothing.

Audit mode is read-only by default. It writes exactly one artifact:
`docs/ilana-audit.md`, plus its ledger entry.

---

## Crew

`quality-auditor` (lead), `metrologist`, `configuration-engineer`, `verifier`,
`ethics-officer` (resident), `conductor` (reports).

---

## Evidence gathering

Look for real signals, in this order. Do not ask the user for what the repository can tell you.

| Phase | Look for | Absence means |
| --- | --- | --- |
| 01 Requirements | `docs/`, `requirements*`, issue tracker links, acceptance criteria in tickets, ADRs | requirements live only in people's heads |
| 02 Architecture | design docs, module boundaries, dependency direction, `ARCHITECTURE.md` | structure is accidental |
| 03 Interface | UI component library, design tokens, accessibility config, CLI help text | interface is undesigned |
| 04 Construction | linter config, formatter config, `EDITORCONFIG`, `CONTRIBUTING`, comment density, function length distribution | no coding standard |
| 05 Verification | test directories, test count, coverage config, CI test step, defect tracker | no verification discipline |
| 06 SCM | branch list, commit message quality, tags, `CHANGELOG`, release workflow, protected branches | no configuration control |
| 07 SQA | review requirements on PRs, `CODEOWNERS`, quality gates in CI, security scanning | quality is unmanaged |
| 08 Process assessment | any metrics at all, retrospective notes, DORA-style data | CMMI level 1 |
| 09 Process modeling | diagrams, `docs/` workflows, onboarding docs, runbooks | knowledge is tribal |
| 10 Tooling | CI config, project board, dependency automation | manual everywhere |
| 11 Ethics and teams | `LICENSE`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, dependency licences, secret scanning | unexamined exposure |

Concrete commands worth running (read-only):

```bash
git log --oneline | wc -l
git branch -a
git tag | tail -20
git log --format='%s' -200 | grep -cE '^(feat|fix|docs|chore|refactor|test)'
find . -type d -name 'test*' -o -type d -name '*test' | head
ls .github/workflows 2>/dev/null
```

---

## Scoring

Score each of the eleven phases 0 to 4.

| Score | Meaning |
| --- | --- |
| 0 | Absent. No evidence the activity is performed at all. |
| 1 | Ad hoc. Happens when someone remembers. Depends on individuals. |
| 2 | Repeatable. A pattern exists but is undocumented and inconsistently applied. |
| 3 | Defined. Documented, standardised, followed by everyone. |
| 4 | Measured and improving. Data is collected and used to change the process. |

Map the mean to a CMMI-style level, and say plainly that this is an *indicative* mapping and
not a formal SEI appraisal:

| Mean score | Indicative level |
| --- | --- |
| < 1.0 | Level 1 Initial |
| 1.0 to 1.9 | Level 2 Managed (partial) |
| 2.0 to 2.9 | Level 3 Defined (partial) |
| 3.0 to 3.5 | Level 4 Quantitatively Managed (partial) |
| > 3.5 | Level 5 Optimizing (partial) |

---

## Report shape

`docs/ilana-audit.md`:

```markdown
# Ìlànà Process Audit: <repo>
Date: <date>   Auditor: quality-auditor   Rigour assessed against: 3

## Verdict
One paragraph. What is actually true here.

## Scorecard
| Phase | Score | Evidence | Gap |
|---|---|---|---|

## Indicative maturity
Mean 1.8 -> Level 2 Managed (partial). Not a formal appraisal.

## Findings
F-01 [critical] ...  evidence: ...  cost of inaction: ...  fix: ...  effort: ...

## Remediation plan
Ordered by (impact / effort). Three horizons: this week, this month, this quarter.

## What is already good
Never omit this section. Audits that only find fault get ignored.
```

---

## Audit discipline

- **Evidence or silence.** Every finding cites a path, a command output, or a count.
- **No moralising.** Report the gap and its cost. The team already knows it is imperfect.
- **Rank by cost of inaction**, not by how far it is from the textbook.
- **Name what is good.** At least three things.
- **Do not modify the repository** unless the user asks for `AUDIT --fix`, in which case each
  fix is a separate `CR-###`.
