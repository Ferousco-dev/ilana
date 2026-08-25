# PROTOCOL: REVIEWS, WALKTHROUGHS AND INSPECTIONS

Reviews focus on early defect detection: systematic examination of artifacts before the software
is executed. Defects found early are far cheaper than defects found late.

## Choose the right activity

| Activity | Led by | Formality | Roles | Use for |
| --- | --- | --- | --- | --- |
| **Peer review** | a peer | low | none fixed | routine changes |
| **Walkthrough** | **the author** | informal | none fixed | explaining logic, gathering early feedback, low-risk artifacts |
| **Inspection** | **a Moderator** | formal, strict procedure | **Moderator, Reader, Recorder** | high-risk artifacts: requirements, architecture, safety-related code |
| **Audit** | independent personnel | formal | auditor | verifying process and standards compliance, not technical content |

The distinction matters and G7 fails when the record misnames the activity.

## Running a walkthrough

1. The author distributes the artifact in advance.
2. The author presents it to peers, section by section, explaining the logic.
3. Peers ask questions and raise concerns.
4. Someone records the findings.
5. The author addresses them.

Informal, author-led, cheap, and genuinely useful. It is not an inspection and should not be
recorded as one.

## Running an inspection

### Roles

| Role | Responsibility | Constraint |
| --- | --- | --- |
| **Moderator** | leads the session, enforces procedure, verifies follow-up | must not be the author |
| **Reader** | paraphrases the artifact aloud, section by section | must not be the author |
| **Recorder** | logs every finding verbatim | classifies nothing during the session |
| Author | answers factual questions | does not defend, does not lead |
| Inspectors | find defects | prepared in advance |

The Reader paraphrasing rather than the author explaining is the mechanism. It forces the artifact
to stand on its own, which is exactly the test that matters.

### Six stages

1. **Planning.** Moderator confirms entry criteria: the artifact is stable, complete enough to
   inspect, and distributed with enough lead time.
2. **Overview.** Author gives context. Brief.
3. **Preparation.** Inspectors examine individually, before the meeting. **Record preparation
   time.** An inspection without preparation finds almost nothing and wastes everyone's afternoon.
4. **Inspection meeting.** Reader paraphrases; inspectors raise findings; Recorder logs.
5. **Rework.** Author addresses findings.
6. **Follow-up.** Moderator verifies each finding is resolved. Without this stage the whole
   exercise is optional.

### Rules of the meeting

1. **Find defects, do not fix them.** Solution discussion destroys throughput. Log it and move on.
2. **Inspect the artifact, not the author.**
3. **The author does not defend.** Factual answers only.
4. **Time-box.** Effectiveness drops sharply after about two hours.
5. **No management present.** Inspection data must never feed performance evaluation, or people
   stop reporting defects and the instrument is destroyed.

### Statistics to record

Preparation time, meeting duration, artifact size, major findings, minor findings, findings per
hour, findings per page or KLOC. These feed the process metrics at phase 08.

**A substantial artifact that yields no findings almost always means preparation did not happen.**

## Classifying findings

| Class | Meaning |
| --- | --- |
| Defect | it is wrong and will cause incorrect behaviour |
| Standard violation | it contravenes the coding or documentation standard |
| Ambiguity | it admits more than one reading (Article 4) |
| Omission | something required is missing |
| Question | unclear, needs an answer before it can be classified |

Counting by class over time shows which phase is leaking, which is the input phase 08 needs.

## Code review specifically

The source material is direct: a team that refuses code review because its members consider
themselves experienced is weakening quality assurance and violating responsible engineering
practice. Experience changes what a review finds; it does not remove the need for one.

- Small changes. A 900-line review approved in 40 seconds is not a review.
- A large change with zero findings is itself a finding.
- Review comments are resolved, not merely marked resolved.
- The reviewer is never the author.
