# Test Automation Strategy

| Field | Value |
| --- | --- |
| Owner | |
| Maintenance owner (often forgotten, always needed) | |
| Runs on | every commit / every PR / nightly / pre-release |

## 1. What is automated, and why

| Area | Automate | Reason | Tool |
| --- | --- | --- | --- |
| Regression | yes | humans are unreliable at repetition; this is the highest-return automation | |
| Repetitive functional | yes | | |
| Smoke | yes | fastest signal that a build is worth testing at all | |
| Load and stress | yes | not humanly performable | |
| Exploratory | no | this is precisely what humans are better at | |
| Usability | no | requires human judgement | |
| One-off acceptance demo | no | cost exceeds return | |

## 2. Pyramid targets

| Level | Target count or proportion | Runtime budget | Current |
| --- | --- | --- | --- |
| Unit | many, fastest | under 60s total | |
| Integration | fewer | under 5 min | |
| System / end-to-end | fewest | under 20 min | |

A suite that takes longer than the team's patience will be skipped, and a skipped suite has
negative value because it creates false confidence.

## 3. Tooling

| Tool | Purpose | Version | Owner |
| --- | --- | --- | --- |
| | | | |

Reference set from the course material: Selenium (web), Cypress (frontend), JUnit (unit),
TestNG (Java framework), Appium (mobile), Jenkins (CI integration), GitHub Actions, GitLab CI.

## 4. Known challenges and mitigations

| Challenge | Mitigation here |
| --- | --- |
| High initial cost | automate regression first; measure hours saved per month |
| Maintenance complexity | named maintenance owner; delete tests that no longer protect anything |
| Requires skilled personnel | pair on the first suite; document the patterns |
| Tool compatibility | pin versions; run the toolchain in CI, not only locally |

## 5. Flaky test policy

A flaky test is a defect. It is raised as `DEF-###` with a severity, quarantined out of the
blocking suite within one day, and fixed or deleted within an agreed window.

Never leave an intermittently failing test in the blocking suite. It teaches the whole team to
ignore red, and that habit is what lets a real failure through.

## 6. What automation cannot do

State this explicitly so nobody assumes otherwise:

- It cannot tell you the requirement was wrong.
- It cannot tell you the interface is confusing.
- It cannot find the defect nobody thought to write a test for.
- It cannot replace the acceptance level, which is a business judgement.
