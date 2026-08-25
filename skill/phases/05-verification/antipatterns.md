# PHASE 05 ANTI-PATTERNS

## Coverage as Quality
90% line coverage, no integration level, no acceptance level. The number looks excellent and the
system is untested where it actually fails.
**Fix:** report coverage and level presence separately at G5.

## Testing Only the Happy Path
Every test supplies valid input and asserts success. Production supplies invalid input,
duplicate requests, expired tokens and half-written files.
**Fix:** a mandatory failure-path pass. Every requirement gets at least one negative test.

## The Developer as Acceptance Tester
The person who built it decides it meets the business need. The source material is explicit that
acceptance testing is conducted by end users, clients and business stakeholders.
**Fix:** name a real acceptance tester or record at G5 that the level is absent.

## Skipping Testing to Meet a Deadline
The specific scenario the course calls unethical: knowingly releasing software that has not been
properly tested. It is not a trade-off, it is a transfer of risk onto people who did not agree
to carry it.
**Fix:** Article 6. `ethics-officer` may veto. The decision, if taken, is recorded with a named
person accountable.

## Flaky Tests Tolerated
Three tests fail intermittently. The team learns to re-run the build. Now nobody believes a red
build, and a real failure goes out.
**Fix:** a flaky test is a defect (`DEF-###`) with a severity. Quarantine it, fix it, or delete
it. Never leave it failing intermittently in the main suite.

## Defect Closed Without a Test
The bug is fixed, the ticket is closed, no test exists that would catch it again. Six months
later a refactor brings it back.
**Fix:** the closure rule. Every `Closed` defect names its regression test.

## Severity Equals Priority
One field doing two jobs, so cosmetic-but-urgent and catastrophic-but-dormant cannot be
distinguished, and triage becomes argument.
**Fix:** two independent fields, both mandatory.

## Real Data in Test Fixtures
A production dump used as test data. Now personal or financial records live in a repository, a
CI log, and every developer's laptop.
**Fix:** Article 7. Synthetic or anonymised data. Treat any occurrence as an incident.

## Testing Against a Different Environment
Tests pass in an environment that differs from production in ways nobody has enumerated. The
source material names environment inconsistency as the classic deployment failure.
**Fix:** enumerate the differences in the test plan, and treat each one as a known blind spot.

## The Test Plan Written After Testing
Produced for the audit, describing what was done rather than directing what will be done.
**Fix:** the test plan is dated before test execution begins. G7 checks the date.
