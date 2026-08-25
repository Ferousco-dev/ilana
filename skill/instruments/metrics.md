# THE METRICS ENGINE

Three categories. A report with only one category is decoration.

---

## Product metrics

Characteristics of the software artifact itself.

### Defect density

```
defect density = confirmed defects / size in KLOC
```

Worked example from the source material: a module of 5,000 lines of code with 10 confirmed bugs
has a defect density of 10 / 5 = **2 defects per KLOC**. The same figure expressed per line is
0.002 defects per LOC. State the unit; the two forms are routinely confused.

Manual procedure: count non-blank, non-comment source lines; count defects with status `Closed`,
`Open`, `Fixed` or `Verified` against that module; divide.

Reading it: the absolute number matters less than the trend and the comparison between modules.
A module three times the codebase average is where your next inspection should go.

### Size

Lines of code. A crude measure, and the source material presents it as the product metric of
absolute size. Useful as a denominator, misleading as a goal.

### Complexity

Architectural or cyclomatic. Language-dependent tooling. Useful as an early warning: complexity
rises before maintainability collapses.

### Coverage

The proportion of code executed by tests. **A product metric, not a quality guarantee.** Report it
alongside which of the four testing levels actually run, or it will be misread.

---

## Process metrics

Efficiency of development activities.

### Defect rate

Defects discovered per unit time. Example from the source material: 15 bugs found in one week.

Reading it: a falling defect rate is ambiguous. It means either quality is improving or testing
has stopped. Always read it next to test execution volume.

### Time to fix

Mean elapsed time from `Open` to `Verified`. Long tails matter more than the mean; report the
median and the 90th percentile.

### Process cycle time

Elapsed time from the start of a task to its completion. Example: a backend microservice module
takes exactly 3 days from the moment a developer begins writing code until the task is completely
finished. A feature taking 5 days from start to finish is a direct calculation of process cycle
time.

Reading it: decompose it. Cycle time is usually dominated by waiting, not working. Time spent in
review queues is the most common hidden cost in software teams.

### Rework effort

Proportion of total effort spent repeating work because of errors or changes. A team where rework
consumes 55% of the timeline has a prevention problem, and the correct response is earlier defect
detection through inspections and reviews.

### Review finding rate

Findings per review, or per page inspected. Falling towards zero on substantial artifacts means
reviews have become ceremony.

---

## Project metrics

Overall project performance.

### Cost variance

```
cost variance = planned cost - actual cost
```

Actual above planned gives a **negative** variance, meaning **over budget**.
Actual below planned gives a **positive** variance, meaning **under budget**.

Worked example: planned 15,000, actual 12,000. Variance +3,000: under budget.
Worked example: planned 12,000, actual 15,000. Variance -3,000: over budget.

### Schedule adherence

```
schedule adherence = planned duration / actual duration
```

A task planned for 10 days and completed in 10 days demonstrates high schedule adherence. A
milestone planned for 15 days and completed in 15 days is the same.

Reading it: consistently perfect adherence usually means estimates are being padded, not that
execution is exceptional. Investigate 1.0 as carefully as 0.6.

---

## The derived measure Ìlànà cares about most

### Prevention ratio

```
prevention ratio = defects found before G5 / total defects found
```

Defects caught by reviews, inspections and requirements validation, divided by all defects found
anywhere including production.

This is the single number that says whether SQA is working, because SQA is prevention and testing
is detection. A rising prevention ratio means quality is being built in. A falling one means the
process is being eroded, usually by schedule pressure, and is a `DOCTOR` mode trigger.

---

## Metric selection by rigour

| Rigour | Minimum metric set |
| --- | --- |
| 1 | none required; record test counts |
| 2 | defect count, test pass rate |
| 3 | one product, one process, one project metric; defect root cause distribution |
| 4 | full set, tracked over time, with trends |
| 5 | full set plus statistical process control on the critical measures |
