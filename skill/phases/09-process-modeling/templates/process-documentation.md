# Process Documentation Template

The six standard sections. Every documented process has all six.

```markdown
# Process: <name>

| Field | Value |
| --- | --- |
| Process ID | |
| Owner | |
| Version | |
| Last reviewed | |
| Standard followed | |

## 1. Purpose
The reason this process exists. One paragraph. If you cannot state why it exists, that is a
finding, not a formatting problem.

## 2. Scope
Boundaries. What this process covers, and explicitly what it does not.

## 3. Inputs
| Input | Source | Format | Required |
|---|---|---|---|

## 4. Activities
| # | Activity | Role | Duration | Output |
|---|---|---|---|---|

## 5. Outputs
| Output | Consumer | Format | Where stored |
|---|---|---|---|

## 6. Roles
| Role | Responsibility | Authority |
|---|---|---|

## 7. Decision points
| Decision | Condition | If yes | If no | Decided by |
|---|---|---|---|---|

## 8. Exceptions
| Exception | Trigger | Handling | Escalation |
|---|---|---|---|

## 9. Diagram
(activity diagram or BPMN model)

## 10. Metrics
| Metric | Target | Measured how |
|---|---|---|
```

## Worked example: course registration

```markdown
# Process: Course Registration

## 1. Purpose
Register students for courses in a given academic session.

## 2. Scope
Covers self-service registration by enrolled students. Does not cover admissions, late
registration by exception, or inter-institution transfers.

## 3. Inputs
| Input | Source | Format | Required |
| Student details | student record system | record | yes |
| Course catalog | academic office | catalog | yes |
| Prerequisite record | student record system | record | yes |

## 4. Activities
| # | Activity | Role | Duration | Output |
| 1 | Login | student | 1 min | authenticated session |
| 2 | Course selection | student | 10 min | draft selection |
| 3 | Validation | system | seconds | validation result |
| 4 | Approval | adviser | 1 day | approved selection |

## 5. Outputs
| Output | Consumer | Format | Where stored |
| Registration slip | student | PDF | student portal |
| Enrolment record | academic office | database row | student record system |

## 6. Roles
| Role | Responsibility | Authority |
| Student | select courses | may withdraw before the deadline |
| Adviser | approve or reject | may override a prerequisite |
| System | validate | may reject an invalid selection |

## 7. Decision points
| Decision | Condition | If yes | If no | Decided by |
| Prerequisites met? | all prerequisites passed | proceed to approval | show which prerequisite is missing | system |
| Adviser approves? | selection is coherent for the programme | issue registration slip | return with reasons | adviser |
```
