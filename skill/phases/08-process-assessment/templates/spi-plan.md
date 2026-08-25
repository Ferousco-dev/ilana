# Software Process Improvement Plan

One improvement per cycle. This template only has room for one, deliberately.

| Field | Value |
| --- | --- |
| Cycle | |
| Owner | |
| Start date | |
| Recheck date | |

## 1. Measure

What the data says now.

| Metric | Current value | How measured | Period | Confidence |
| --- | --- | --- | --- | --- |

If there is no data, the first improvement is to start measuring, and that is a legitimate and
common answer.

## 2. Analyze

### The weakness
One paragraph. What specifically is not working, stated in terms of the measurement above.

### Root cause
Why it is happening. Distinguish:
- **process defect** (the procedure is wrong or missing)
- **tooling defect** (the procedure is right, the tooling makes it expensive)
- **capability gap** (people have not been trained)
- **structural** (the org chart makes the correct behaviour impossible)

These four need different fixes, and treating one as another is why improvements fail.

### Evidence ruled out
What else it could have been, and why that was excluded. An analysis with no rejected hypotheses
is an assumption.

## 3. Improve

### The single change
Exactly one. Describe it concretely enough that someone else could implement it.

### Technique category
- [ ] Automation of tasks
- [ ] Adoption of best practices
- [ ] Continuous monitoring and feedback
- [ ] Use of metrics for decision-making

### Implementation
| Step | Owner | Date |
| --- | --- | --- |

### Cost
Effort, tooling, disruption. An improvement whose cost exceeds its return is a net loss and
should be rejected here rather than discovered later.

## 4. Repeat

### Success metric
| Metric | Baseline | Target | Recheck date |
| --- | --- | --- | --- |

### What would make us revert
The observable condition under which this change is judged a failure and undone. Naming this in
advance is what stops a bad change becoming permanent.

### Recheck result
| Date | Value | Verdict | Next action |
| --- | --- | --- | --- |
| | | improved / no change / worse | keep / adjust / revert |

An SPI plan with an empty recheck row is an unfinished experiment, not a completed improvement.
