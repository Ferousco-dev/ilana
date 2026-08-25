# INSTRUMENT: QUALITY ATTRIBUTE SCORECARD

Seven attributes. Each scored with evidence or marked `UNVERIFIED`. Never "good".

| Attribute | The question | Measure with | Threshold source |
| --- | --- | --- | --- |
| Correctness | does it do exactly what the requirements say? | requirement-to-test traceability, all passing | the SRS |
| Reliability | does it work every time under normal conditions? | uptime, mean time between failures, crash rate, soak test | the availability NFR |
| Efficiency | does it use CPU, memory and storage well? | profiling under the stated load, resource ceilings | the performance NFR |
| Usability | can users learn and operate it? | task completion rate, time on task, error rate, support themes | the usability NFR |
| Maintainability | can it be modified safely? | complexity, coupling, measured time to make a representative change | the coding standard |
| Portability | does it run elsewhere with minimal change? | CI matrix across the target platforms | the portability NFR |
| Security | is data protected from unauthorised access? | scan results, auth model review, encryption at rest and in transit | the security NFR and domain requirements |

## Manual procedures

Where automation is unavailable, these are cheap and legitimate.

**Correctness.** Count requirements. Count requirements with at least one passing test. Divide.
Anything below 100% is stated as a number, not softened.

**Reliability.** If no monitoring exists, run the system under representative load for a fixed
period and count failures. Absence of monitoring is itself the finding.

**Efficiency.** Time the primary operation ten times under the stated load. Report median and
worst. Compare against the NFR threshold. A system taking 45 seconds to load a simple menu and
consuming 95% of available memory is failing efficiency regardless of its functional correctness.

**Usability.** Three people who have not seen the system attempt the primary task, unaided, while
you watch and time them. This costs an hour and finds more than any heuristic checklist.

**Maintainability.** Pick a representative small change. Time how long it takes from ticket to
merged. That number is maintainability, expressed the way it actually matters.

**Portability.** Run the test suite on each target platform. If the answer is "we only ever ran it
on one", the attribute is `UNVERIFIED`, not "probably fine".

**Security.** At minimum: is authentication enforced on every non-public path; is authorisation
checked at the resource, not only in the interface; is data encrypted in transit and at rest;
are there secrets in the repository; is input validated at the trust boundary named in the design.

## The trap

A system may satisfy every functional requirement and still be bad software. It may take 45
seconds to load a menu, be unusable without training, run on one platform only, and be so tangled
that nobody dares change it. Correctness is one of seven attributes, not a synonym for quality.

This is why the scorecard has seven rows and why `UNVERIFIED` is an honest and common answer.
