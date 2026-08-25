# ASSESSMENT BANK: INTEGRATED SCENARIOS

Applied judgement across phases. These are the questions that distinguish someone who has memorised
the vocabulary from someone who can use it.

Each scenario is marked out of 5:
- identified the correct phase (1)
- named the correct concept (1)
- applied it to the specifics of the scenario (2)
- noticed the ethical or process dimension where present (1)

---

**SC-01.** A multinational organisation develops a cloud-based air traffic management system. During
final acceptance testing, independent auditors discover the system occasionally produces
inconsistent aircraft separation calculations under rare network latency conditions. The project
sponsor argues the probability is extremely low and that delaying deployment will incur significant
financial penalties.

*What is the correct action, and what governs it?*

Expected: delay deployment, disclose the safety risk to stakeholders, correct the defect, and
complete independent verification before release. Public interest overrides schedule and financial
pressure. Rigour 5; no gate override is available.

---

**SC-02.** A software organisation develops for air traffic control, financial systems, healthcare
and government. It enforces professional ethics, rigorous requirements engineering, structured team
collaboration, comprehensive documentation, automated CI/CD pipelines, formal verification and
validation, continuous process improvement and strict regulatory compliance.

*Characterise this organisation's maturity, and identify which single further step would move it up
a CMMI level.*

Expected: a mature, integrated engineering culture. Whether it is level 4 or 5 depends on whether
quantitative and statistical control of process performance is present, and whether processes are
refined because data said so.

---

**SC-03.** A team's dashboard shows: rework consumes 55% of the development timeline; the same three
defect classes recur every release; and there are no reviews before merge.

*Diagnose, and prescribe exactly one change.*

Expected: a prevention failure, not a detection failure. Early defect detection through formal
inspections and walkthroughs. One change, with a baseline (current rework percentage), a target, and
a recheck date.

---

**SC-04.** During peer review, a developer discovers an intentionally inserted backdoor allowing
unauthorised administrative access after deployment.

*State the governing principle and the sequence of actions.*

Expected: public interest and professional responsibility take precedence over client
confidentiality. This is not merely unethical; deliberately leaving a hidden backdoor in a system
handling customer accounts is a criminal matter. Halt, escalate outside the immediate team, preserve
evidence, do not merge.

---

**SC-05.** A Scrum team consistently completes only 60% of its committed sprint backlog because of
poor effort estimation.

*Which Scrum activity primarily addresses this, and what specifically should change?*

Expected: the Sprint Retrospective. Supported by better backlog refinement, collaborative estimation
and historical velocity analysis. The underlying violation is sustainable sprint commitment.

---

**SC-06.** A financial institution adopts Git for version control, Jenkins for CI, Docker for
containerisation and Kubernetes for orchestration, while maintaining formal documentation and
regulatory approval procedures.

*Characterise this approach and say whether it is coherent.*

Expected: integrating modern DevOps practices within a controlled software engineering process. It
is coherent and mature, not a contradiction. Regulatory obligation and delivery automation are
orthogonal concerns.

---

**SC-07.** A team has 92% unit test coverage, zero integration tests, and ships weekly. Integration
failures appear in production roughly monthly.

*Explain the causal link and state what the coverage number is and is not telling them.*

Expected: unit tests cannot find interface defects. Coverage is a product metric measuring code
executed, not risk retired. The missing integration level is precisely the level that exists to find
these defects.

---

**SC-08.** A business analyst misunderstands a stakeholder requirement due to poor communication.
Developers faithfully implement the incorrect specification. The defect is found in acceptance
testing.

*Identify the root cause and the gate that should have caught it.*

Expected: ineffective team dynamics during requirements engineering. The read-back and written
stakeholder confirmation loop at G1 is the missing control. Root cause category: requirement missing
or wrong, phase 01, not a coding error.

---

**SC-09.** An organisation periodically analyses project performance metrics and modifies its
development process to reduce defect density.

*Name the principle, and state what would have to be true for this to indicate CMMI level 5 rather
than level 4.*

Expected: continuous improvement. Level 5 requires that processes are continuously refined based on
performance data and innovation, with problems prevented before they occur, not merely that data is
collected and used for control.

---

**SC-10.** You join a project with no requirements document, no tests, a single 4,000-line file, one
developer who wrote all of it and is leaving in two weeks, and a live customer base.

*State your first three actions, in order, and justify the ordering.*

Expected: no single right answer, but strong answers prioritise knowledge capture before the
developer leaves, then a characterisation test suite to make change safe, then a lightweight
requirement register reconstructed from behaviour. Rewriting first is the wrong answer.
