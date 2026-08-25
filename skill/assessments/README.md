# ASSESSMENTS

`DRILL` mode uses these. The question banks live in `../interrogation/banks/`.

## Formats

| Format | Shape | Duration |
| --- | --- | --- |
| `RAPID` | 10 multiple choice, mixed phases | 10 min |
| `PHASE` | 15 questions, one phase, increasing difficulty | 20 min |
| `SCENARIO` | 5 applied scenarios with justification | 30 min |
| `VIVA` | adaptive, follow-up on every answer | open |
| `ETHICS` | dilemmas only | 20 min |
| `GAUNTLET` | 40 questions across all eleven phases | 60 min |

## Scenario rubric

Every scenario is marked out of 5:

| Criterion | Points |
| --- | --- |
| Identified the correct phase | 1 |
| Named the correct concept | 1 |
| Applied it to the specifics of this scenario | 2 |
| Noticed the ethical or process dimension where present | 1 |

The third criterion carries two points deliberately. Naming "requirements engineering" is recall;
saying what specifically should have happened in *this* scenario is understanding.

## Viva structure

Adaptive. Start broad, follow the answer.

```
Opening:    "Explain the difference between SQA and testing."
If correct: "Give me an SQA activity that testing cannot substitute for."
If correct: "Your team has excellent tests and no reviews. What are they missing, concretely?"
If wrong:   "What does 'process-oriented' mean, and what is the other one oriented to?"
```

Three consecutive correct answers on a thread means the thread is understood; move on. Two
consecutive wrong answers means the foundation is missing; drop a level rather than pressing.

## Marking rules

1. **Mark honestly.** Wrong is wrong. "Close" is not a mark.
2. **Give the distinguishing test**, not the letter. If walkthrough and inspection were confused,
   the answer is "author-led and informal versus Moderator, Reader, Recorder and strict procedure".
3. **Attribute every miss to a phase.** Errors cluster, and the cluster is the finding.
4. **Never reveal an answer inside a question.**
5. **End with three specific next actions**, each pointing at a file.

## The scorecard

```
DRILL RESULT  |  GAUNTLET  |  40 questions

Phase                      Score    Signal
01 Requirements             8/9     strong
05 Verification             5/8     WEAK: confuses integration with system testing
07 Quality assurance        2/5     WEAK: review vs audit; walkthrough vs inspection
08 Process assessment       1/3     WEAK: CMMI level 3 vs level 4 boundary
...
Total 28/40 (70%)

Three things to fix, in order:
  1. phases/07-quality-assurance/reference.md, section on reviews and audits
  2. references/cmmi.md, the level 3 to 4 boundary
  3. re-run DRILL PHASE on 05
```

## Building your own bank

Add a file to `../interrogation/banks/`. Requirements:

- Distractors must be plausible enough that a partially-informed person would choose one.
- Every question maps to exactly one phase.
- Scenario questions must have a marking note stating what a strong answer contains.
- Never test trivia that a practitioner would look up. Test the distinctions they must hold.
