# ASSESSMENT BANK: CONFIGURATION MANAGEMENT

## Recall

1. Name five artifacts under configuration control.
2. Name the two types of version control system with an example of each.
3. State the change management process in six steps.
4. Name the four types of software change.
5. Name the four types of software release.
6. Name four build automation tools and the ecosystem each belongs to.

## Multiple choice

**Q1.** Which tool is primarily used for version control?
A. Selenium  B. Git  C. Kubernetes  D. JUnit
*Answer: B*

**Q2.** Which tool is most commonly used to orchestrate containerised applications across multiple
computing nodes?
A. Git  B. Kubernetes  C. Selenium  D. JUnit
*Answer: B*

**Q3.** Which correctly matches DevOps tools with their primary functions?
A. Git version control; Jenkins CI/CD automation; Docker containerisation; Kubernetes container
   orchestration; Selenium automated testing; Ansible configuration management and deployment
   automation
B. Git database management; Jenkins operating system; Docker compiler
C. Git image editing; Jenkins web browser; Docker antivirus
D. Git machine learning framework; Jenkins text editor; Docker IDE
*Answer: A*

**Q4.** Which DevOps principle most directly reduces deployment failures caused by environmental
inconsistencies?
A. manual configuration  B. infrastructure automation
C. sequential documentation  D. manual integration
*Answer: B*

**Q5.** During deployment, infrastructure configurations differ between testing and production
environments, resulting in application failure. Which practice most directly prevents this?
A. infrastructure as code and configuration automation  B. manual server configuration
C. sprint retrospectives  D. requirement workshops
*Answer: A*

**Q6.** During deployment, the operations team receives incomplete deployment documentation, causing
service interruptions. Which principle was most directly neglected?
A. software reusability  B. process adherence and effective team communication
C. functional independence  D. algorithm optimisation
*Answer: B*

## Scenario

**S1.** Your team deploys from whatever commit is on `main` at the time. Explain the specific risks
and describe what you would change.

**S2.** Production is down. A one-line fix goes straight to production without review or a change
request. Was this correct? What must happen next, and by when?

**S3.** A rollback plan exists in your documentation. It has never been executed. Assess the risk
and state what you would do about it.

## Marking notes

- S1 must identify that an untagged release cannot be precisely identified or rolled back to.
- S2: the emergency fix is often correct; the failure would be not writing the retrospective change
  request within one working day, with the justification and after-the-fact impact analysis.
- S3 must state that an unrehearsed rollback plan is a hypothesis, and schedule a rehearsal.
