# PHASE 05 - VERIFICATION

Owner: `verifier`. Entry gate: G4. Exit gate: G5.

> Testing is the process of evaluating and verifying that a software application works as
> expected. It involves executing software with the intent of identifying defects, errors, or
> missing requirements.

Testing is **detection**. Quality assurance, in phase 07, is **prevention**. They are different
disciplines and this phase is only one half of quality. Do not confuse having tests with having
quality.

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| Test plan | `docs/test-plan.md` | `templates/test-plan.md` |
| Test cases | `docs/test-cases.md` or the test suite itself | `templates/test-case.md` |
| Defect reports | `.ilana/defects.md` | `templates/defect-report.md` |
| Automation strategy | `docs/automation-strategy.md` | `templates/automation-strategy.md` |
| Test report | `docs/test-report.md` | `templates/test-report.md` |

---

## Why testing matters

Six reasons, and they are worth stating because "we don't have time to test" is always an
argument about these six.

| Reason | What it buys |
| --- | --- |
| Bug detection | finds defects ranging from minor inconvenience to system failure |
| Ensures reliability | confidence in stability and performance under varying conditions |
| Confirms compliance | verifies the software adheres to specified requirements |
| Enhances user experience | a more polished, usable product |
| Saves time and money | fixing during testing is far cheaper than fixing after deployment |
| Improves maintenance | well-tested software is easier to maintain and update safely |

---

## The testing process

Seven stages. Test execution is one of them, which is the point.

```
Requirement Analysis -> Test Planning -> Test Case Design -> Test Environment Setup
   -> Test Execution -> Defect Reporting -> Test Closure
```

---

## The four levels and the pyramid

```
        Acceptance      few tests     satisfies the business?     users, clients
       ------------
        System          some          meets the SRS as a whole?   independent testers
      --------------
       Integration      more          do modules talk correctly?  developers, testers
    ------------------
      Unit              many          is each part correct alone? developers
```

### Unit testing
Testing individual components or modules independently. The smallest level. Usually performed
by developers. Focuses on functions, methods and classes.

Objectives: verify logic correctness, detect coding errors, ensure each module works
independently.
Characteristics: performed by developers, focuses on internal logic, usually automated.
Advantages: detects bugs early, simplifies debugging, improves code quality.
Tools: JUnit (Java), NUnit (.NET), PyTest (Python).

### Integration testing
Testing combined modules to ensure they work together correctly. Focus: interfaces between
modules, data flow between components, communication errors.

Strategies:
- **Top-down** - testing starts from top-level modules, using stubs for those below.
- **Bottom-up** - testing begins with lower-level modules, using drivers for those above.
- **Big bang** - all modules integrated simultaneously. Cheap to set up, expensive to diagnose.

Example: testing the interaction between the login module, the database and the authentication
service.

### System testing
Testing the complete integrated system as a whole, against specified requirements. Conducted by
an independent testing team, after integration testing.

Includes functional, performance, security, usability and stress testing.

Example: testing a full e-commerce site including registration, product search, payment
processing and order confirmation.

### Acceptance testing
Determines whether the system satisfies business requirements and is ready for deployment.
Conducted by end users, clients and business stakeholders. Final approval before deployment.

Types:
- **User Acceptance Testing (UAT)**
- **Alpha testing** - performed at the developer's site.
- **Beta testing** - performed by real users in a real environment.

---

## The coverage trap

A project with 90% unit coverage and no integration level is not well tested.

Unit tests cannot find interface defects. Interface defects between separately developed
components are exactly what integration testing exists for, and they are among the most common
and most expensive defects in real systems. Coverage is a product metric. It measures how much
code the tests execute, not how much risk the tests retire.

Ìlànà rule at G5: report coverage **and** report which of the four levels actually run. A
project missing a level says so explicitly, with the risk it accepts.

---

## Test planning

Test planning defines the scope, objectives, approach and resources for testing activities. It
results in a test plan document.

Components of a test plan:

| Component | What it answers |
| --- | --- |
| Test objectives | what the testing intends to achieve |
| Scope of testing | features to test, and features explicitly not to test |
| Test strategy | techniques, tools, approaches |
| Test environment | hardware, software, data |
| Roles and responsibilities | who does what |
| Risk analysis | what could go wrong and the mitigation |
| Schedule | timelines and milestones |
| Deliverables | what testing hands over |
| Exit criteria | the conditions for stopping testing |

Importance: provides direction, reduces risk, prevents confusion, ensures systematic testing.

**Exit criteria deserve special attention.** "We stopped testing when we ran out of time" is not
an exit criterion. "All high-severity defects closed, 100% of REQ covered by at least one
passing test, no open critical defects" is.

---

## Test automation

Automation uses tools and scripts to execute test cases automatically and compare results.

Benefits: faster execution, repeatable tests, reduced human error, reduced human effort,
improved accuracy, reusable scripts, continuous testing support, supports CI and CD,
cost-effective in the long term.

Suitable areas: regression testing, repetitive testing, load testing, smoke testing.

| Tool | Purpose |
| --- | --- |
| Selenium | web application testing |
| Cypress | frontend testing |
| JUnit | unit testing |
| TestNG | Java testing framework |
| Appium | mobile testing |
| Jenkins | CI integration |

Flow: write test scripts -> execute automatically -> compare actual and expected -> generate
reports.

Challenges, which are real and should be planned for: high initial cost, maintenance complexity,
requires skilled personnel, tool compatibility issues.

**Ìlànà position:** automate regression first. It is the highest return, because regression is
the thing humans are worst at doing repeatedly and reliably. Do not attempt to automate
exploratory testing; that is what humans are for.

---

## Defect tracking

A defect is an error or flaw in software that causes incorrect behaviour. Defect tracking is the
process of identifying, recording, monitoring and resolving defects.

### Life cycle

```
New -> Assigned -> Open -> Fixed -> Retest -> Verified -> Closed
```

Alternative states: **Reopened** (failed retest), **Deferred**, **Rejected**.

### Report fields

| Field | Description |
| --- | --- |
| Defect ID | unique identifier |
| Title | brief summary |
| Description | detailed explanation |
| Severity | impact level |
| Priority | urgency of fixing |
| Steps to Reproduce | instructions to recreate |
| Expected Result | correct behaviour |
| Actual Result | observed behaviour |
| Status | current state |

Tools: Jira, Bugzilla, Azure DevOps, Redmine, MantisBT.

### Severity is not priority

The single most common confusion in defect management.

- **Severity** is technical impact. How badly does the system misbehave?
- **Priority** is business urgency. How soon must it be fixed?

A cosmetic typo on the landing page is low severity and can be top priority. A data corruption
bug in an unused legacy import is critical severity and may be low priority. Both fields exist
because they are independent.

### The closure rule

**A defect closed without a regression test case will come back.** Ìlànà requires every closed
defect to name the test case that now prevents its return. This single rule does more for
long-term quality than any amount of coverage.

---

## Testing and team dynamics

Testing requires close coordination between developers and testers. Testers need accurate
information to identify defects; developers need to fix what is discovered. Without proper
coordination, defects remain unresolved and low-quality software ships. A tester who discovers a
critical defect and fails to communicate it before deployment causes defective software to reach
production, and that is a communication failure, not a testing failure.

---

## Exit

Run `checklist.md`, attempt G5. Handoff goes to `configuration-engineer` with the test report,
the open defect list, and the exit criteria table showing actuals against targets.
