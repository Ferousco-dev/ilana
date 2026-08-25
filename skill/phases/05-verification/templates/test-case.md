# Test Case Template

```
TC-###
Title:
Level:        unit | integration | system | acceptance
Type:         functional | performance | security | usability | stress | regression
Verifies:     REQ-### / NFR-### / DOM-### / DEF-### (regression)
Priority:     high | medium | low
Automated:    yes | no    Script:

Preconditions:
  -

Test data:
  -

Steps:
  1.
  2.
  3.

Expected result:

Actual result:                     (filled at execution)
Status:       pass | fail | blocked | skipped
Executed by:                       Date:
Defect raised: DEF-###
```

## Design techniques worth using

| Technique | Use for | Example |
| --- | --- | --- |
| Equivalence partitioning | inputs with classes of behaviour | age: negative, 0-17, 18-64, 65+, non-numeric |
| Boundary value analysis | any bounded numeric or length input | loan period 14 days: test 13, 14, 15 |
| Decision table | combinations of conditions | member status x item type x overdue |
| State transition | anything with a lifecycle | the defect life cycle itself |
| Error guessing | experience-driven | empty string, very long string, unicode, SQL metacharacters |
| Negative testing | every requirement | what happens when the precondition is false |

## The rule for every requirement

At minimum, two test cases per functional requirement:

1. the behaviour when the precondition holds,
2. the behaviour when it does not.

A requirement with only a positive test is half tested.
