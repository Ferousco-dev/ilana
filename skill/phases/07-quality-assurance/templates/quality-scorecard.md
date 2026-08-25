# Quality Attribute Scorecard

Score with evidence or mark `UNVERIFIED`. Never mark an attribute "good" without a source.
Article 10 is enforced here.

| Attribute | Objective | Measured value | Source | Verdict |
| --- | --- | --- | --- | --- |
| Correctness | | | | met / not met / UNVERIFIED |
| Reliability | | | | |
| Efficiency | | | | |
| Usability | | | | |
| Maintainability | | | | |
| Portability | | | | |
| Security | | | | |

## What counts as evidence, per attribute

| Attribute | Acceptable evidence | Not evidence |
| --- | --- | --- |
| Correctness | traceability matrix showing every requirement covered by a passing test | "all tests pass" |
| Reliability | uptime measurement, crash rate, mean time between failures, soak test result | "it seems stable" |
| Efficiency | profiling output, resource ceilings observed under the stated load | "it feels fast" |
| Usability | task completion rate and time on task with real users, support ticket themes | "the design is clean" |
| Maintainability | complexity metrics, coupling, measured time to implement a representative change | "the code is readable" |
| Portability | CI matrix results across the target platforms | "it should work anywhere" |
| Security | scan output, the authentication and authorisation model reviewed, encryption verified | "we use HTTPS" |

## Reading the scorecard

- **All met**: report it plainly.
- **Some UNVERIFIED**: that is an honest and common outcome. Name what would be needed to verify
  each one, and how much it would cost.
- **Not met**: state the gap in numbers, and who accepted the shortfall.

A scorecard with seven greens and no sources is worse than an empty one, because it manufactures
confidence. Article 2.
