# Retrospective

Not a feelings exercise. Four questions, each answered with evidence.

| Field | Value |
| --- | --- |
| Run / release / sprint | |
| Period | |
| Facilitator | |
| Participants | |

---

## 1. What did the process catch?

Defects caught before they reached production, and where they were caught.

| Gate | Defect or issue caught | Estimated cost had it reached production |
| --- | --- | --- |
| G1 | | |
| G2 | | |
| G4 | | |
| G5 | | |
| G7 | | |

This is the section that justifies the process to people who think it is overhead. Fill it in
properly.

## 2. What did the process miss?

Every defect found late is a gate that did not bite.

| Defect | Found at | Should have been caught at | Why the gate missed it | Gate change proposed |
| --- | --- | --- | --- | --- |

## 3. Where did the process cost more than it returned?

Ceremony that produced no finding is waste. Naming it is what keeps the process trusted.

| Activity | Effort spent | Findings produced | Verdict |
| --- | --- | --- | --- |
| | | | keep / trim / drop at this rigour |

## 4. What one change goes into the next run?

Exactly one.

| Change | Owner | Start date | Success metric | Baseline | Target | Recheck date |
| --- | --- | --- | --- | --- | --- | --- |

---

## Prevention ratio

```
Defects found before G5 (prevention):   ___
Defects found after G5 (detection):     ___
Defects found in production:            ___

Prevention ratio: ___ / ___ = ___%
Previous run:     ___%
Trend:            improving / flat / decaying
```

A decaying prevention ratio means the process is being eroded, usually by schedule pressure.
That is a `DOCTOR` mode trigger, not a note for next quarter.

## Facilitation rules

1. **Evidence, not impressions.** "Testing felt rushed" becomes "test execution had 3 days
   against a planned 7".
2. **Mechanisms, not people.** Article 14. Name the missing control, never the person who forgot.
3. **One change.** The urge to fix everything is why nothing gets fixed.
4. **Carry it forward.** The first item of the next retrospective is the recheck of this one.
