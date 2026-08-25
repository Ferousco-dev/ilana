# MODE: DOCTOR

The user has symptoms, not a request. Doctor mode diagnoses the *process*, not the code.

Crew: `metrologist` (lead), `quality-auditor`, `conductor`.

---

## Symptom to root-cause map

Start from what the user actually said. These mappings come straight from the failure modes
described in the source material.

| Symptom | Likely root cause | Phase | First probe |
| --- | --- | --- | --- |
| "We keep building the wrong thing" | elicitation failure, no stakeholder validation | 01 | Is there an SRS? Who signed it? |
| "Requirements keep changing" | no change control, not a requirements problem | 06 | Is there a CR log with impact analysis? |
| "The same bugs keep coming back" | no regression suite, no defect root-cause analysis | 05 | Does each closed defect have a test case? |
| "Two developers built the same module" | role ambiguity, no RACI | 11 | Who owns which component, in writing? |
| "Integration always breaks" | interfaces never specified, no integration testing level | 02, 05 | Are module interfaces documented? |
| "Deployments fail" | dev and production environments diverge, no IaC | 06, 10 | Is the environment reproducible from source? |
| "We are always late" | no measurement, estimating from optimism | 08 | Is process cycle time recorded anywhere? |
| "Testing takes forever" | no automation, manual regression | 05 | What fraction of tests are automated? |
| "Nobody understands the old code" | documentation debt, knowledge loss | 09 | Can a new hire onboard from docs alone? |
| "Reviews are rubber stamps" | walkthrough posing as inspection, no defined roles | 07 | Are Moderator, Reader, Recorder assigned? |
| "Quality is fine until release, then it explodes" | no system or acceptance testing level | 05 | Which of the four levels actually run? |
| "Management overrides engineering on safety" | ethics and governance failure | 11 | Is there a documented escalation path? |
| "We are Agile but nothing improves" | retrospectives with no follow-through | 08 | Name one process change from the last retro. |

---

## Diagnostic procedure

1. **Take the history.** Ask for three things: the symptom, when it started, and one specific
   recent instance with dates and names of artifacts.
2. **Measure, do not guess.** Constitution Article 10. Pull whatever real numbers exist:
   commit frequency, PR review latency, reopened defect count, time from branch to merge,
   failed deploy count. If nothing exists, that absence *is* the finding.
3. **Localise.** Which phase and which gate is leaking? A symptom in phase 05 often has its
   root in phase 01.
4. **Distinguish** a process defect from a people defect from a tooling defect. All three exist
   and they need different fixes.
5. **Prescribe one change.** Exactly one, with a metric that will show whether it worked and a
   date to check. Prescribing five changes at once guarantees that none of them are evaluated.
6. **Schedule the recheck.** Measure -> Analyze -> Improve -> Repeat is a loop, not a slogan.

---

## Output

`docs/ilana-diagnosis.md`:

```markdown
# Process Diagnosis
Symptom (user's words): "..."
Onset: ...
Instance examined: ...

## Measurements taken
| Metric | Value | Source | Interpretation |

## Root cause
One paragraph. Phase and gate identified.

## Differential
What else it could have been, and why that was ruled out.

## Prescription
ONE change. Owner. Start date.

## Success metric
Metric, current baseline, target, recheck date.
```

---

## Doctor's rules

- **One prescription.** Discipline yourself. The temptation to fix everything is why nothing
  gets fixed.
- **Absence of data is data.** "You have no metrics" is a legitimate and often the correct
  primary diagnosis.
- **Do not blame individuals.** Article 14: team dynamics failures are system failures. Name
  the missing mechanism, not the person who forgot.
- **Recheck or it did not count.** A prescription with no recheck date is a suggestion.
