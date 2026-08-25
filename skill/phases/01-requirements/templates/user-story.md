# User Story Template

For Agile-styled projects. A story is a placeholder for a conversation; the acceptance
criteria are the part that survives the conversation.

```
STORY-### / REQ-###
As a <role>
I want <capability>
So that <benefit>

Priority: must | should | could | wont
Estimate:
Source: <who asked, when, in what session>

Acceptance criteria
  AC-1  Given <precondition>, when <action>, then <observable outcome>
  AC-2  Given <precondition>, when <action>, then <observable outcome>
  AC-3  (failure path) Given <precondition>, when <failure>, then <observable recovery>

Non-functional constraints that apply
  NFR-###  <which, and the threshold that applies to this story>

Out of scope for this story

Definition of done
  [ ] code merged behind review
  [ ] unit tests written and passing, IDs recorded
  [ ] integration test covers any new module boundary
  [ ] acceptance criteria demonstrated to the requester
  [ ] documentation updated
  [ ] traceability row updated
```

## Rules

- A story with no failure-path acceptance criterion is incomplete. Systems fail; specify it.
- A story that cannot be demonstrated is not done, whatever the board says.
- Stories map to `REQ` IDs. The story is the conversation; the `REQ` is the record.
- "As a user I want the system to be fast" is not a story. Article 4.
