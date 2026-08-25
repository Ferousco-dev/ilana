# Formal Inspection Record

An inspection is highly structured, follows strict procedures, and has three defined roles. If
those roles were not assigned, what happened was a walkthrough, and this is the wrong template.

| Field | Value |
| --- | --- |
| Inspection ID | INS-### |
| Artifact | (document, module, or change) |
| Version inspected | |
| Date | |
| Duration | |

## Roles

| Role | Person | Responsibility |
| --- | --- | --- |
| **Moderator** | | leads the session, keeps it to procedure, is not the author |
| **Reader** | | paraphrases the artifact aloud, section by section |
| **Recorder** | | logs every finding verbatim, classifies nothing during the session |
| Author | | answers questions; does not defend |
| Inspector(s) | | find defects |

The author does not lead. That is what distinguishes an inspection from a walkthrough.

## Procedure followed

- [ ] **Planning.** Moderator confirms the artifact meets entry criteria and is stable.
- [ ] **Overview.** Author gives context, briefly.
- [ ] **Preparation.** Inspectors examine the artifact individually before the meeting. Record
      preparation time; an inspection without preparation finds little.
- [ ] **Inspection meeting.** Reader paraphrases; inspectors raise findings; Recorder logs.
- [ ] **Rework.** Author addresses findings.
- [ ] **Follow-up.** Moderator verifies each finding is resolved.

## Rules of the session

1. **Find defects, do not fix them.** Discussing solutions destroys the session's throughput.
2. **Inspect the artifact, not the author.** Findings are about the work.
3. **The author does not defend.** They answer factual questions only.
4. **Time-box it.** Inspection effectiveness drops sharply after about two hours.
5. **No management present.** Inspection data must never be used for performance evaluation, or
   people stop reporting defects.

## Preparation

| Inspector | Time spent | Pages / lines covered |
| --- | --- | --- |

## Findings

| # | Location | Finding | Class | Severity | Disposition |
| --- | --- | --- | --- | --- | --- |
| 1 | | | defect / standard violation / ambiguity / omission / question | major / minor | accepted / rejected / deferred |

Classes:
- **defect**: it is wrong and will cause incorrect behaviour
- **standard violation**: it contravenes the coding or documentation standard
- **ambiguity**: it admits more than one reading (Article 4)
- **omission**: something required is missing
- **question**: unclear, needs an answer before it can be classified

## Statistics

| Measure | Value |
| --- | --- |
| Artifact size (pages or lines) | |
| Total preparation time | |
| Meeting duration | |
| Major findings | |
| Minor findings | |
| Findings per hour | |
| Findings per page or KLOC | |

These numbers feed the process metrics at phase 08. An inspection that finds nothing on a
substantial artifact usually means preparation did not happen.

## Verdict

`accept` / `accept with rework` / `re-inspect after rework`

Moderator: ______________________  Date: __________
Follow-up verified on: __________
