# PHASE 08 - PROCESS ASSESSMENT AND IMPROVEMENT

Owner: `metrologist`. Support: `conductor`. Entry gate: G7. Exit gate: G8.

> Process assessment tells us what is wrong. Process improvement tells us how to fix it.
> Without measurement, any attempt to improve a software process is guesswork.

This is the phase that turns a project into an organisation that gets better. Most teams skip
it, which is why most teams have the same retrospective every quarter.

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| Maturity assessment | `docs/maturity-assessment.md` | `templates/maturity-assessment.md` |
| Process improvement plan | `docs/spi-plan.md` | `templates/spi-plan.md` |
| ISO/IEC 12207 process map | `docs/process-map.md` | `templates/process-map-12207.md` |
| Retrospective | `docs/retrospective.md` | `templates/retrospective.md` |

---

## Software process assessment

Assessment answers: *is our current way of working actually working?*

It evaluates existing practices and whether those practices are producing good results. A team
can follow a process faithfully and still produce software users are unhappy with; assessment is
what surfaces that.

Purpose, threefold:
1. **Evaluate whether current practices are producing good results.**
2. **Determine process maturity**: how stable, predictable and well-controlled the process is.
3. **Identify where improvement is needed.**

---

## Software process improvement

SPI is the continuous, systematic effort to make development stronger and more effective.

Three key activities:
1. **Identify process weaknesses.** Study the current process to find what is not working:
   delays, frequent errors, poor communication, inefficient procedures.
2. **Introduce improvements.** Change procedures, adopt better tools, improve team practices,
   restructure workflows.
3. **Monitor the impact.** Check whether the change actually improved things. If not, adjust
   again.

Processes are never considered perfect or finished. They are always being reviewed, refined and
improved.

---

## Process measurement

Process measurement means collecting and analysing data about how the development process is
performing. Instead of saying "the process is slow" or "testing is difficult", use real data:
"testing now takes 5 days instead of the expected 2", "we are recording about 50 bugs per week".

**Purpose:** evaluate process performance, identify inefficiencies, track improvements over
time, support decision-making with real data.

**Common process metrics:** defect rate, time taken to complete tasks, cost of development,
rework effort.

**Importance:** objectivity (decisions based on facts, not opinion), evidence-based decisions,
tracking progress over time.

This is Article 10 in its natural home.

---

## CMMI: Capability Maturity Model Integration

A structured framework used to evaluate how good an organisation's development process is, and
how it can be improved. It answers two questions: *how mature is our current process*, and *how
do we make it better*.

**Process maturity** is how developed and well-organised a development process is. A mature
organisation follows clearly defined processes, produces consistent results, and continuously
improves.

### The five levels

| Level | Name | Characteristics | The tell |
| --- | --- | --- | --- |
| **1** | Initial | Chaotic and unstructured. No standard procedures. Everything depends on individual effort. Results unpredictable, quality usually poor. | success depends on heroics |
| **2** | Managed | Some order. Work is planned and tracked. Basic project management practices used. Requirements managed, progress monitored. | projects are controlled, but each does it its own way |
| **3** | Defined | Processes clearly documented and standardised across the whole organisation. Everyone follows the same procedures. Training provided. Outcomes more predictable. | one organisational process, followed by all |
| **4** | Quantitatively Managed | Data and metrics used to control processes. Decisions based on actual numbers rather than assumptions. Performance predictable. | statistical control of process performance |
| **5** | Optimizing | Continuous improvement. Processes constantly refined based on feedback and performance data. Innovation encouraged. Problems prevented before they occur. | the process changes itself, deliberately |

### The two boundaries people get wrong

**Level 2 to 3.** Level 2 means each project is managed. Level 3 means the *organisation* has one
standard process that projects tailor from. Documented per-project practice is still level 2.

**Level 3 to 4.** The transition requires beginning to **manage, measure and control process
performance using quantitative data and statistical techniques**. An organisation with excellent
documented processes and no quantitative control is level 3, not level 4, however good it feels.

**Importance of CMMI:** provides a roadmap for improvement, enhances product quality, increases
customer confidence, improves the predictability of software projects.

Ìlànà always reports a CMMI figure as **indicative**, never as an appraisal. A formal appraisal
is conducted by certified appraisers against the full model; what Ìlànà produces is a
self-assessment using CMMI's vocabulary.

---

## ISO/IEC 12207: software life cycle processes

A globally accepted standard defining what processes should exist when developing software from
start to finish.

**Purpose, threefold:** establish a common structure for software processes; clearly define the
activities involved in development and maintenance; ensure consistency across organisations and
projects.

**Three categories:**

| Category | Contains | Nature |
| --- | --- | --- |
| **Primary processes** | requirements analysis, design, implementation, testing, maintenance | the core activities directly involved in building software |
| **Supporting processes** | documentation, configuration management, quality assurance, verification and validation | not development itself, but they support it |
| **Organizational processes** | process improvement, training, infrastructure management | management and long-term improvement, corporate-wide governance |

The classification questions that come up repeatedly:

- Software maintenance -> **primary**.
- Software configuration management, including version control, baseline tracking and change
  authorisation -> **supporting**.
- Software quality assurance, verification and validation -> **supporting**.
- Corporate training programmes, infrastructure management, institutional process improvement ->
  **organizational**.
- Software requirements analysis -> **primary**.

**Importance:** standardises software processes, improves communication among teams because
everyone shares one framework, and ensures quality and consistency across projects.

---

## Process optimization

Improving and refining the development process so it becomes faster, more efficient and more
effective.

**Goals:** reduce development time without sacrificing quality; minimise costs; improve product
quality; increase productivity.

**Four techniques:**

1. **Automation of tasks.** Tools perform repetitive work automatically: automated testing, CI
   and CD pipelines that build and deploy. Reduces human error, saves time, speeds development.
2. **Adoption of best practices.** Proven methods: clean structured code, coding standards,
   methodologies such as Agile.
3. **Continuous monitoring and feedback.** Constantly observe process performance and gather
   feedback from users and team members, so problems are detected early.
4. **Use of metrics for decision-making.** Real data guides decisions: bug frequency, development
   time, system performance.

---

## The relationship between assessment and improvement

Assessment feeds improvement; improvement depends on assessment. The relationship is a
continuous cycle:

```
        Measure -> Analyze -> Improve -> Repeat
           ^                                |
           +--------------------------------+
```

Measure the process with data and metrics. Analyse the data to understand what is working.
Improve by making the necessary changes. Repeat. It is not a one-time activity.

---

## Exit

Run `checklist.md`, attempt G8. Handoff goes to `conductor` for closure with the maturity
assessment, the improvement plan, and the metrics baseline for the next run.
