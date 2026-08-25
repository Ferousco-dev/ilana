---
description: Ìlànà DOCTOR mode. Diagnose a broken process from its symptoms, not the code.
argument-hint: <the symptom, e.g. "the same bugs keep coming back">
---

Run Ìlànà in `DOCTOR` mode. Read `~/.claude/skills/ilana/SKILL.md` and `modes/doctor.md`.

The symptom, in the user's words: $ARGUMENTS

This mode diagnoses the **process**, not the code. Adopt `metrologist` as lead, with
`quality-auditor` and `conductor`.

Follow the diagnostic procedure:

1. **Take the history.** Ask three things and wait: the symptom, when it started, and one specific
   recent instance with dates and the artifacts involved.
2. **Measure, do not guess.** Constitution Article 10. Pull whatever real data exists: commit
   frequency, pull request review latency, reopened defect count, time from branch to merge, failed
   deployment count, test suite runtime. Use `instruments/scripts/metrics.py` where it helps.
   **If nothing exists, that absence is the finding**, and it is often the primary one.
3. **Localise** using the symptom-to-root-cause table in `modes/doctor.md`. Remember that a symptom
   appearing in phase 05 very often has its root in phase 01.
4. **Distinguish** a process defect from a people defect from a tooling defect. All three exist,
   they look similar, and they need completely different fixes.
5. **Prescribe exactly one change.** One. With an owner, a metric, a baseline and a date to check.
   Prescribing five changes at once guarantees none of them are evaluated.
6. **Set the recheck date.** Measure, Analyze, Improve, Repeat is a loop, not a slogan.

Write it to `docs/ilana-diagnosis.md`.

**Never blame individuals.** Article 14: team dynamics failures are system failures. Name the
missing mechanism, never the person who forgot.
