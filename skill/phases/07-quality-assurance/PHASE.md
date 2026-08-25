# PHASE 07 - SOFTWARE QUALITY ASSURANCE

Owner: `quality-auditor`. Support: `metrologist`. Entry gate: G6. Exit gate: G7.

> Software Quality Assurance is a systematic and organized set of activities designed to ensure
> that both the software development process and the software product meet specified
> requirements, standards and user expectations.

The two sentences that define this phase:

- **SQA is process-oriented.** It is concerned with *how* software is developed, not only with
  the final product.
- **SQA prevents defects; testing detects them.** They are different disciplines and a project
  needs both.

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| Quality management plan | `docs/quality-plan.md` | `templates/quality-plan.md` |
| Review and inspection records | `docs/reviews/` | `templates/inspection-record.md` |
| Audit report | `docs/audit-report.md` | `templates/audit-report.md` |
| Metrics report | `docs/metrics-report.md` | `templates/metrics-report.md` |
| Quality attribute scorecard | inside the quality plan | `templates/quality-scorecard.md` |

---

## What software quality actually means

Software quality is the degree to which a software product meets its specified requirements and
satisfies the needs and expectations of its users.

The critical point, and the one most often missed: **quality is not only correctness.** A system
may produce the correct output and still be slow, insecure, unusable or unmaintainable. Quality
is better understood as **fitness for use**, which includes usability, performance, security,
reliability, maintainability and user satisfaction.

A high-quality software system:
- performs its intended functions correctly,
- is reliable and efficient,
- is easy to use and maintain,
- is secure and adaptable.

---

## Objectives of SQA

| Objective | Meaning |
| --- | --- |
| Defect prevention | prevent defects occurring, rather than waiting to find them |
| Process standardisation | everyone follows established standards, guidelines and procedures |
| Process improvement | processes are monitored, weaknesses identified, improvements made |
| Risk reduction | reduce the chance of delays, overruns, failures |
| Customer satisfaction | the software meets requirements and satisfies users |

---

## SQA as a continuous process

SQA begins at the very start of a project and continues through requirements gathering, design,
coding, testing, deployment and maintenance.

Quality cannot be added to a product at the end. It must be built in from the beginning. This is
why phase 07 is not "the phase where we check quality"; it is the phase where we verify that
quality was assured throughout, and where the plan that governed it was written before
construction began.

**G7 checks the date on the quality plan.** A quality plan written after construction is a
document produced for an audit, not a control.

---

## The five core activities

### 1. Quality planning
The starting point. Before development begins, the team determines what quality means for this
project and how it will be achieved: quality standards identified, quality objectives defined,
tools and techniques selected, procedures established.

Output: the **Quality Management Plan**, a roadmap for all quality-related activities.

### 2. Reviews
Early defect detection. Systematic examination of artifacts (requirements documents, design
specifications, source code) **before execution**. Defects are cheaper to fix early. Forms: peer
review, walkthrough, inspection.

### 3. Audits
Process compliance. While reviews examine technical content, audits examine whether the team is
following required standards, procedures and policies: is documentation complete, are standards
followed, are processes properly implemented. Usually conducted by independent personnel, which
is what makes the assessment objective.

### 4. Software metrics
Numerical measurements evaluating quality and development performance, so decisions rest on data
rather than assumption. Three categories, detailed below.

### 5. Testing
Execution-based defect detection. The one SQA activity concerned with detection rather than
prevention. Covered in phase 05.

---

## Review, walkthrough, inspection, audit

The four are routinely conflated, and G7 fails when the record calls a walkthrough an inspection.

| Activity | Led by | Formality | Defined roles | Purpose |
| --- | --- | --- | --- | --- |
| Peer review | a peer | low | none fixed | catch obvious problems |
| **Walkthrough** | **the author** | **informal** | none fixed | author presents the artifact to peers to explain its logic and gather early feedback |
| **Inspection** | **a Moderator** | **formal, strict procedure** | **Moderator, Reader, Recorder** | structured, disciplined, objective evaluation to detect defects early |
| Audit | independent personnel | formal | auditor | verify compliance with process and standards |

Choose by risk: walkthrough for low-risk artifacts, inspection for high-risk ones. Record which
one you actually performed.

Protocol for running an inspection: `protocols/review-inspection.md`.

---

## Software metrics

Three categories. A project that reports only one category is not measuring; it is decorating.

### Product metrics
Characteristics of the software artifact itself.

| Metric | Definition | Formula |
| --- | --- | --- |
| Lines of code | absolute size of the codebase | count |
| Code complexity | architectural or cyclomatic complexity | tool-dependent |
| **Defect density** | defects relative to size | confirmed defects / KLOC |

Worked example from the course: a module with 5,000 lines of code and 10 confirmed bugs has a
defect density of 10 / 5 KLOC = **2 defects per KLOC**. Note that the same figure is sometimes
expressed as 0.002 defects per line of code; state your unit.

### Process metrics
Efficiency of development activities.

| Metric | Definition |
| --- | --- |
| Defect rate | how frequently defects are discovered over time, e.g. 15 bugs in one week |
| Time to fix defects | mean elapsed time from Open to Verified |
| **Process cycle time** | elapsed time from the start of a task to its completion, e.g. 3 days from first line of code to task finished |
| Rework effort | proportion of work repeated because of errors or changes |

### Project metrics
Overall project performance.

| Metric | Definition | Interpretation |
| --- | --- | --- |
| **Cost variance** | planned budget minus actual expenditure | actual above planned is a negative variance, meaning over budget |
| **Schedule adherence** | actual completion against planned completion | planned 10 days, completed in 10 days, is high schedule adherence |

Compute them with `instruments/scripts/metrics.py`.

---

## The seven quality attributes

The measurable characteristics used to judge any software system.

| Attribute | Question | Fails when |
| --- | --- | --- |
| **Correctness** | does it do exactly what the requirements say? | output is wrong, however pretty the interface |
| **Reliability** | does it perform consistently without failing? | it crashes randomly or behaves unpredictably |
| **Efficiency** | does it use memory, processor and storage well? | 45 seconds to load a text menu, 95% of available memory |
| **Usability** | is it easy to learn and operate? | users are confused, training is required for simple tasks |
| **Maintainability** | can it be modified, updated or corrected easily after deployment? | every change is dangerous and slow |
| **Portability** | can it run on different platforms with minimal change? | works on Windows desktop, crashes on the Linux server |
| **Security** | is it protected from unauthorised access, attack or damage? | data is exposed or transactions are not verified |

Ìlànà rule: score each attribute with **evidence** or mark it `UNVERIFIED`. Never mark it "good".
Scorecard: `templates/quality-scorecard.md`.

---

## Exit

Run `checklist.md`, attempt G7. Handoff goes to `metrologist` with the metrics set, the review
records, and the audit findings.
