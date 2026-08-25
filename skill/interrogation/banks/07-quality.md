# ASSESSMENT BANK: QUALITY ASSURANCE

## Recall

1. What is the fundamental difference between software testing and Software Quality Assurance?
2. Name the five core SQA activities.
3. Name the three categories of software metrics with two examples of each.
4. Name the seven software quality attributes.
5. What are the three defined roles in a formal inspection?
6. What is the primary output of quality planning?

## Multiple choice

**Q1.** What is the fundamental difference between software testing and SQA?
A. testing is process-oriented and prevention-focused, SQA is product-oriented and debugging-focused
B. testing is primarily concerned with defect detection via code execution, whereas SQA is a
   broader continuous discipline focused on process prevention and standards compliance
C. testing runs only during requirements gathering, SQA only during deployment
D. testing tracks budgets, SQA tracks hardware failure rates
*Answer: B*

**Q2.** Which type of software review is characterised as an informal walkthrough led directly by
the author of the document or source code?
A. a structured panel inspection with Moderator and Recorder
B. a formal evaluation where the author presents the artifact to peers to explain its logic and
   gather early feedback
C. an independent audit verifying process compliance against international standards
D. a dynamic system test executed against user acceptance criteria
*Answer: B*

**Q3.** A project lead states that an upcoming code review will be an "Inspection". To fulfil the
requirements of this specific, highly structured SQA activity, what must the team do?
A. allow the author of the code to lead the session informally without predefined procedures
B. assign separate, formal operational roles such as Moderator, Reader and Recorder to
   structurally detect bugs early
C. evaluate only the final financial cost variances
D. conduct the evaluation exclusively after deployment
*Answer: B*

**Q4.** An SQA manager records a metric called "Defect Rate" (15 bugs found in one week). How
should this be categorised and what does it directly measure?
A. product metric measuring the absolute size of the codebase
B. project metric measuring the difference between planned and actual costs
C. process metric measuring how frequently defects are discovered in the software process over time
D. quality attribute evaluating cross-platform operational compatibility
*Answer: C*

**Q5.** A medical application must run seamlessly across Android, iOS and a standard web browser
without changes to its core operational source code. Which quality attribute must be prioritised?
A. efficiency  B. portability  C. usability  D. correctness
*Answer: B*

**Q6.** A system operates perfectly according to its functional requirements but takes 45 seconds
to load a simple text menu and consumes 95% of available memory. This demonstrates a critical
failure in which quality attribute?
A. correctness  B. portability  C. efficiency  D. usability
*Answer: C*

**Q7.** Why must Quality Planning be the first step in SQA, and what is its primary output?
A. a fully compiled executable binary
B. a comprehensive Quality Management Plan serving as an operational guide for all quality-related
   tasks
C. a completed SRS database schema
D. a CMMI Level 5 optimization framework document
*Answer: B*

**Q8.** An SQA auditor wants to evaluate maintainability. Which parameter provides the most direct
evidence?
A. the ease with which the software can be modified, updated or corrected after deployment
B. how consistently the application runs without crashes
C. the visual layout and colour scheme
D. total lines of code written in a week
*Answer: A*

## Calculation

**C1.** Planned cost 15,000. Actual cost 12,000. State the metric, its category, and what it
indicates about the project.
*Answer: cost variance; a project metric; positive variance, the project is under budget.*

**C2.** Planned cost 12,000. Actual cost 15,000. Same three answers.
*Answer: cost variance; project metric; negative variance, the project is over budget.*

**C3.** A milestone planned to take 15 days was completed in 15 days. Which metric does this
demonstrate, and at what level?
*Answer: schedule adherence, high.*

## Scenario

**S1.** Your team has 95% test coverage, a CI pipeline, and no quality plan, no reviews before
merge, and no metrics. Someone says "our quality is excellent". Respond, using the distinction
between prevention and detection.

**S2.** You are asked to audit a project you personally delivered three months ago. What do you do
and why?

**S3.** A review record in the repository says "Inspection, 2026-08-14, attendees: the author and
two developers." What is wrong with this record, and what would you change?

## Marking notes

- S1 must identify that they have detection without prevention, and name at least two of the five
  core SQA activities that are absent.
- S2 must refuse on independence grounds and propose an independent auditor.
- S3 must identify that with no Moderator, Reader or Recorder this was a walkthrough, not an
  inspection, and that misnaming it corrupts the quality evidence.
