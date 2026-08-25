# PHASE 05 CHECKLIST

## Planning
- [ ] Test plan exists with all nine components
- [ ] Exit criteria are objective and measurable
- [ ] Features explicitly NOT being tested are listed
- [ ] Risks identified with mitigations
- [ ] Test environment specified: hardware, software, data
- [ ] Roles assigned

## Levels
- [ ] Unit tests exist and pass
- [ ] Integration tests cover every module boundary
- [ ] System testing performed against the SRS as a whole
- [ ] Acceptance testing performed by users or clients, not by the developers
- [ ] Any missing level is stated explicitly with the accepted risk

## Coverage of requirements
- [ ] Every REQ maps to at least one test case
- [ ] Every NFR maps to at least one test case
- [ ] Every DOM requirement maps to at least one test case
- [ ] Failure paths are tested, not only happy paths
- [ ] Boundary values tested for every numeric or bounded input

## Non-functional testing
- [ ] Performance tested against the NFR threshold, under the NFR load
- [ ] Security tested: authentication, authorisation, input validation
- [ ] Usability tested with a representative user
- [ ] Stress or load tested to the stated capacity

## Defects
- [ ] Every defect has all nine report fields
- [ ] Severity and priority set independently
- [ ] Every defect has a lifecycle state
- [ ] Every closed defect names the regression test that prevents its return
- [ ] Open defects are listed with severity in the handoff

## Automation
- [ ] Regression suite is automated
- [ ] Automated suite runs on every change (RIGOUR 3+)
- [ ] Automation maintenance owner named
- [ ] Flaky tests are tracked, not ignored or deleted

## Reporting
- [ ] Test report states counts: run, passed, failed, skipped, blocked
- [ ] Exit criteria table shows target and actual
- [ ] Failures are pasted, not summarised
