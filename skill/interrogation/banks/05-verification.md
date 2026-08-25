# ASSESSMENT BANK: VERIFICATION

## Recall

1. Name the four levels of testing and who performs each.
2. Name the three integration testing strategies.
3. Name the nine fields of a defect report.
4. Give the defect life cycle, including the alternative states.
5. What distinguishes alpha from beta testing?
6. Name four areas suitable for test automation and two that are not.
7. Name the nine components of a test plan.

## Multiple choice

**Q1.** An engineering team is evaluating the interactions, data exchanges and structural
interfaces between separate software components. Which level are they performing?
A. unit  B. integration  C. system  D. acceptance
*Answer: B*

**Q2.** Which level verifies that individual source code components operate correctly before they
are combined with other modules?
A. unit  B. integration  C. system  D. acceptance
*Answer: A*

**Q3.** Which level validates the complete, fully integrated product against the functional and
non-functional requirements outlined in the SRS?
A. unit  B. integration  C. system  D. component
*Answer: C*

**Q4.** During a formal technical review a team identifies structural interface errors where
separate modules fail to exchange parameters cleanly. Which level of testing is explicitly
designed to detect these boundary communication failures?
A. unit  B. integration  C. system  D. acceptance
*Answer: B*

**Q5.** A developer commits source code directly to the production branch without automated
testing. Which DevOps practice has most clearly been bypassed?
A. continuous integration  B. sprint planning  C. requirement validation  D. business analysis
*Answer: A*

**Q6.** Which practice most effectively prevents defects from propagating throughout the SDLC?
A. performing verification and validation activities throughout every development phase
B. delaying testing until after deployment
C. eliminating design reviews
D. depending solely on user acceptance testing
*Answer: A*

## Calculation

**C1.** A module has 5,000 lines of code and 10 confirmed bugs found during system testing. What is
its defect density, in which category of metric does it fall, and what does it directly measure?

*Answer: 2 defects per KLOC (equivalently 0.002 per LOC). It is a product metric. It measures the
quality of the software product relative to its absolute size.*

**C2.** A backend module takes exactly 3 days from the moment a developer begins writing code until
the task is completely finished. Name the metric and its category.

*Answer: process cycle time; a process metric.*

## Scenario

**S1.** Your project has 92% line coverage, all tests green, and no integration test level. The
release is tomorrow. What do you tell the release manager, and what do you write in the G5 record?

**S2.** A defect is fixed and the ticket is closed. Three months later it reappears. What was
missing from the closure procedure, and what rule would have prevented it?

**S3.** Management asks you to skip the scheduled integration testing phase to deliver a medical
portal on its original deadline. State your position and your reasoning, and describe the specific
alternatives you would offer.

**S4.** Three tests in your suite fail intermittently. The team re-runs the build when it happens.
Explain what this is costing and what you would do about it.

## Marking notes

- S1 must state that coverage does not substitute for the integration level, and that interface
  defects are what integration testing exists to find. It must record the gap honestly rather than
  claim readiness.
- S2 must identify the missing regression test case.
- S3 must identify this as an ethical matter, not only a technical trade-off. Neglecting quality
  for speed or cost is unethical. A strong answer offers alternatives: reduce scope, test the
  highest-risk boundaries only, ship behind a flag, delay.
- S4 must recognise that intermittent failure teaches the team to ignore red, which is worse than
  the individual test failures.
