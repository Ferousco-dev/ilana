# Code Review Record

| Field | Value |
| --- | --- |
| Change ID | PR / branch / CR-### |
| Author | |
| Reviewer (never the author) | |
| Date | |
| Lines changed | |
| Review type | peer review / walkthrough / inspection |
| Requirements touched | REQ-... |
| Design elements touched | DES-... |

## Review type matters

Record what actually happened, not what sounds most rigorous.

| Type | Led by | Formality | Roles |
| --- | --- | --- | --- |
| Peer review | a peer | low | none fixed |
| Walkthrough | the author | informal | none fixed |
| Inspection | a Moderator | formal, strict procedure | Moderator, Reader, Recorder |

Calling a walkthrough an inspection is a G7 finding.

## Checklist

- [ ] Change traces to a requirement or a change request
- [ ] Coding standard followed, or the deviation is justified in the thread
- [ ] Every failure path handled or deliberately propagated
- [ ] No secrets, keys or credentials introduced
- [ ] Untrusted input validated at the boundary
- [ ] Tests added or updated; the test would fail without this change
- [ ] Error messages meaningful and consistent with the error catalogue
- [ ] No dead code, no leftover debugging output
- [ ] Documentation updated where behaviour changed
- [ ] Traceability row updated
- [ ] Dependency additions recorded with licence

## Findings

| # | Location | Finding | Class | Severity | Disposition |
| --- | --- | --- | --- | --- | --- |
| 1 | `path:line` | | defect / standard / design / clarity / security | major / minor | fixed / accepted / deferred DEF-### |

Classify findings. Counting them by class over time tells you where your process leaks, which
is the input `metrologist` needs at phase 08.

## Outcome

`approved` / `approved with minor findings` / `changes required` / `rejected`

A review of a large change with zero findings is itself a finding. Either the change was
trivial, or the review was not performed.
