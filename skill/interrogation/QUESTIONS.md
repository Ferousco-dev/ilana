# THE INTERROGATION SYSTEM

Ìlànà asks questions. This directory governs which ones.

Two distinct purposes, often confused:

| Purpose | Direction | Files |
| --- | --- | --- |
| **Elicit** | Ìlànà asks the user, to build the artifact correctly | `intake.md`, each phase's `questions.md` |
| **Assess** | Ìlànà asks the user, to test their understanding | `banks/*.md`, used by `DRILL` mode |

The protocol governing *how* to ask is `protocols/question-engine.md`. This file governs *what*.

## Elicitation questions

| When | File | Budget |
| --- | --- | --- |
| Boot, every invocation | `intake.md` | 5 to 9, one batch |
| Entering a phase | `phases/<n>/questions.md` | up to 5, one batch |
| Mid-phase | only for a genuine fork | 1 |

## Assessment banks

| Bank | Covers |
| --- | --- |
| `banks/01-requirements.md` | elicitation, types, process, challenges |
| `banks/02-design.md` | levels, objectives, architecture |
| `banks/03-interface.md` | types, GUI characteristics, five principles |
| `banks/04-construction.md` | goals, standards, guidelines, language characteristics |
| `banks/05-verification.md` | levels, planning, automation, defects |
| `banks/06-scm.md` | version control, change, build, release |
| `banks/07-quality.md` | SQA, reviews, metrics, attributes |
| `banks/08-process.md` | assessment, CMMI, ISO/IEC 12207, optimization |
| `banks/09-modeling.md` | notations, documentation, workflows |
| `banks/10-tooling.md` | CASE, project management, CI |
| `banks/11-ethics-teams.md` | ethics, team dynamics, industry practice |
| `banks/scenarios.md` | applied judgement questions across all phases |

## Writing a good assessment question

1. **Distractors must be plausible.** A question whose wrong answers are obviously wrong tests
   nothing except reading speed.
2. **Test the distinction, not the definition.** "What is an inspection?" is weak. "You attended a
   session led by the document's author with no assigned roles. What was it?" is strong.
3. **Never reveal the answer inside the stem.**
4. **Scenario questions beat recall questions** for anything a practitioner will actually do.
5. **Every question maps to a phase**, so the scorecard can find clusters.
