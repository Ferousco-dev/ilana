# PHASE 05 REFERENCE

## Definition

Software testing is the process of evaluating and verifying that a software application or
system works as expected. It involves executing software with the intent of identifying
defects, errors or missing requirements.

Testing ensures that software products are reliable, efficient, secure, maintainable and
user-friendly. It is a major activity in the SDLC and contributes significantly to software
quality assurance.

In software engineering, testing refers to evaluating a system or application to identify and
rectify discrepancies between expected and actual results. Its primary objective is to ensure
the software functions as intended, meets the specified requirements, and provides a seamless
user experience.

## Objectives of software testing

- Detecting defects before deployment
- Ensuring the software satisfies user requirements
- Verifying that components work correctly
- Improving software reliability and performance
- Preventing future failures
- Enhancing customer satisfaction

## Why testing is important

- **Bug detection.** Identifies and enables the fixing of defects, ranging from minor
  inconveniences to critical errors causing system failure.
- **Ensures reliability.** Gives confidence in reliability, stability and performance under
  various conditions.
- **Confirms compliance.** Verifies adherence to specified requirements.
- **Enhances user experience.** Produces a more polished, user-friendly product.
- **Saves time and money.** Identifying and fixing during testing is more cost-effective than
  after deployment.
- **Improves maintenance.** Well-tested software is easier to maintain and update.

## The software testing process

Requirement Analysis, Test Planning, Test Case Design, Test Environment Setup, Test Execution,
Defect Reporting, Test Closure.

## Levels of testing

### Unit testing
Testing individual components or modules independently. The smallest level of testing, usually
performed by developers, focusing on functions, methods or classes.

Examples of units: functions, methods, classes, modules.
Characteristics: performed by developers, focuses on internal logic, usually automated.
Objectives: verify logic correctness, detect coding errors, ensure each module works
independently.
Advantages: detects bugs early, simplifies debugging, improves code quality.
Tools: JUnit (Java), NUnit (.NET), PyTest (Python).

### Integration testing
Testing combined modules to ensure they work together correctly.
Focus: interfaces between modules, data flow between components, communication errors.
Objectives: detect interface defects, verify data communication between modules.
Types: top-down integration, bottom-up integration, big bang integration.
Advantages: identifies interaction errors, ensures subsystem compatibility.

### System testing
Testing the complete integrated system as a whole against specified requirements.
Conducted after integration testing, usually by independent testers.
Types: functional, performance, security, usability, stress testing.
Advantages: validates complete system behaviour, detects system-wide defects.

### Acceptance testing
Determines whether the software satisfies business requirements and is ready for deployment.
Performed by clients, end users and customers.
Types: User Acceptance Testing, Alpha testing (at the developer's site), Beta testing (by real
users in a real environment).
Objectives: validate user requirements, ensure business readiness.
Purpose: final approval before deployment.

## Test planning

Test planning is the process of defining the testing strategy, objectives, schedule, resources
and scope. It is one of the most important stages in software testing and results in a test plan
document.

Components: test objectives; scope of testing (features to test and features not to test); test
strategy (techniques, tools, approaches); resource planning (personnel, hardware, software
tools); test schedule (timelines and milestones); risk analysis (possible risks and mitigation);
exit criteria (conditions for stopping testing); test environment; roles and responsibilities;
deliverables.

Importance: provides direction, reduces risk, prevents confusion, ensures systematic testing.

## Test automation

Test automation involves using tools and scripts to automatically execute tests and compare
results.

Benefits: faster execution, reduced human effort, improved accuracy, reusable test scripts,
continuous testing support, repeatable tests, reduced human error, supports CI and CD,
cost-effective in the long term.

Areas suitable for automation: regression testing, repetitive testing, load testing, smoke
testing.

Tools: Selenium (web application testing), Cypress (frontend testing), JUnit (unit testing),
TestNG (Java testing framework), Appium (mobile testing), Jenkins (CI integration).

Automated testing flow: write test scripts, execute scripts automatically, compare actual and
expected results, generate test reports.

Challenges: high initial cost, maintenance complexity, requires skilled personnel, tool
compatibility issues.

## Defect tracking and reporting

A defect (bug) is an error or flaw in software that causes incorrect behaviour. Defect tracking
is the process of identifying, recording, monitoring and resolving defects.

**Life cycle:** New, Assigned, Open, Fixed, Retest, Verified, Closed.
**Alternative states:** Reopened, Deferred, Rejected.

**Report fields:** Defect ID (unique identifier), Title (brief summary), Description (detailed
explanation), Severity (impact level), Priority (urgency of fixing), Steps to Reproduce
(instructions to recreate the bug), Expected Result (correct behaviour), Actual Result (observed
behaviour), Status (current state).

**Tools:** Jira, Bugzilla, Azure DevOps, Redmine, MantisBT.

## Testing best practices

Start testing early. Automate repetitive tests. Maintain detailed test cases. Track defects
properly. Perform regression testing.
