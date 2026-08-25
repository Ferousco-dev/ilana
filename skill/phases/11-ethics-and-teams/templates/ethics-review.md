# Ethics Review

| Field | Value |
| --- | --- |
| Review ID | ETH-### |
| Phase | |
| Reviewer | ethics-officer |
| Date | |
| Trigger | intake / gate / specific request / incident |

## 1. The two questions

**Who is harmed if this software is wrong?**
Name them. Not "users": which users, and what happens to them.

**What data does this hold, and what happens to a person if it leaks?**

If both answers are genuinely empty, record that and proceed lightly. If either names a real
person or a real harm, `RIGOUR` is at least 3.

## 2. Exposure scan

| Dimension | Present | Detail | Rigour implication |
| --- | --- | --- | --- |
| Personal data | | | 4 |
| Medical or health data | | | 4 to 5 |
| Financial data or transactions | | | 4 |
| Children's data | | | 4 to 5 |
| Physical safety | | | 5 |
| Legal or regulatory obligation | | | 4 |
| Automated decisions affecting people | | | 4 |
| Public infrastructure | | | 5 |

## 3. The five ethical issues

| Issue | Assessment | Evidence | Finding |
| --- | --- | --- | --- |
| Honesty and integrity | are capabilities and defects reported accurately? | | |
| Confidentiality | is sensitive data protected, and is any of it where it should not be? | | |
| Quality and safety | were any verification activities skipped for speed or cost? | | |
| Intellectual property | are all licences recorded and complied with? | | |
| Professional responsibility | does the team have the competence, and are processes followed? | | |

## 4. ACM/IEEE code assessment

| Principle | Compliant | Evidence or concern |
| --- | --- | --- |
| Public interest | | |
| Client and employer responsibilities | | |
| Product quality | | |
| Professional competence | | |

## 5. Findings

| ID | Finding | Severity | Principle | Required action | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| ETH-001 | | halt / major / minor / observation | | | | |

**halt**: work stops until a human decides. Only the user lifts it.
**major**: must be resolved before the next gate.
**minor**: resolve before closure.
**observation**: recorded, no action required.

## 6. Halt record (if applicable)

```
HALT ETH-###
Raised at:        phase, gate, date
Reason:           one paragraph, specific
Principle:        which article, which code principle
Options offered:  the legitimate alternatives presented to the user
User decision:    lifted / accepted / work re-scoped
User's stated justification (verbatim):
Lifted on:        date
```

## 7. Disposition at closure

Every `ETH-###` is dispositioned at G8: resolved, accepted with a named accepter, or carried
forward with an owner and a date. None may remain open and unowned.
