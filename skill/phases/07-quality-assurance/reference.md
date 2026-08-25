# PHASE 07 REFERENCE

## Introduction

Software is used almost everywhere: mobile phones, banking systems, hospitals, airports,
schools, businesses and government. Because society depends heavily on software, a failure can
cause financial loss, security breaches, incorrect medical decisions, service disruption and
loss of trust. Producing high-quality software is therefore not optional.

## Definition of SQA

Software Quality Assurance is a systematic and organized set of activities designed to ensure
that both the software development process and the software product meet specified requirements,
standards and user expectations.

Unlike approaches that focus only on identifying errors after development, SQA emphasises
**preventing defects** by ensuring proper processes are followed from the beginning.

SQA is **process-oriented**: it focuses on how software is developed, not just on the final
product. The assumption is that a team following well-defined and effective processes is more
likely to produce reliable, secure, high-quality software.

## Concept of software quality

Software quality is the degree to which a software product meets its specified requirements and
satisfies the needs and expectations of its users.

Characteristics of a high-quality system:
1. It performs its intended functions correctly.
2. It is reliable and efficient: operating consistently without frequent failures and using
   system resources effectively.
3. It is easy to use and maintain.
4. It is secure and adaptable.

**Quality is not only correctness.** A system may produce correct results and still be difficult
to use, slow, insecure or hard to maintain. Quality is better understood as **fitness for use**,
including usability, performance, security, reliability, maintainability and user satisfaction.

## Objectives of SQA

1. **Defect prevention** rather than waiting to find errors after completion.
2. **Process standardisation**: developers, testers and other team members follow established
   standards, guidelines and procedures.
3. **Process improvement**: processes are continuously monitored and evaluated to identify
   weaknesses and make improvements.
4. **Risk reduction**: reduces the chance of delays, budget overruns and software failures.
5. **Customer satisfaction**: the software meets requirements and satisfies user needs.

## SQA as a continuous process

SQA begins at the start of a project and continues through the entire SDLC: requirements
gathering, system design, coding, testing, deployment, maintenance.

Quality cannot be added at the end; it must be built into the software from the beginning.
Preventing problems early is more effective and less costly than fixing them at the end.

Quality planning, reviews, audits, software metrics and testing are not separate topics; they are
components of the broader SQA process.

## Core activities

### Quality planning
The starting point. Before development begins, the team determines what quality means for the
project and how it will be achieved. Quality standards are identified, objectives defined, tools
and techniques selected, and procedures established. The result is a **Quality Management Plan**,
which serves as a roadmap for all quality-related activities. Its importance is that it ensures
quality is intentionally built into the development process rather than treated as an
afterthought.

### Reviews
Focus on early defect detection. Systematic examination of software artifacts such as
requirements documents, design specifications and source code, before the software is executed.
Defects are easier and less expensive to fix early. Forms: peer reviews, walkthroughs,
inspections. Detecting issues early prevents defects spreading into later stages where
correction is more costly.

### Audits
Focus on process compliance. While reviews examine technical content, audits examine whether the
team is following required standards, procedures and policies. Audits check whether
documentation is complete, standards are followed, and processes are properly implemented. They
are usually conducted by independent personnel, giving an objective assessment and maintaining
consistency and discipline.

### Software metrics
Numerical measurements used to evaluate software quality and development performance. Instead of
relying on assumptions, metrics provide objective data supporting decision-making.

**Product metrics** measure characteristics of the software product itself: lines of code, code
complexity, defect density.
**Process metrics** measure the efficiency of development activities: defect rates, time taken
to fix defects, process cycle time.
**Project metrics** measure overall project performance: cost variance, schedule adherence.

### Testing
A key SQA activity involving executing the software to identify defects and verify that it meets
specified requirements. Unlike other SQA activities which focus on prevention, testing is
primarily concerned with **detection**.

Levels: unit, integration, system, acceptance.
Testing ensures the software behaves as expected, errors are identified before deployment, and
system reliability is improved.

## Software quality attributes

**Correctness.** The software must do exactly what it is supposed to do according to the
requirements. If it does not meet the requirements it is not correct, no matter how nice it looks.

**Reliability.** How consistently the software performs without failing. A reliable system should
not crash randomly or behave unpredictably; it should work properly every time under normal
conditions.

**Efficiency.** How well the software uses system resources such as memory, processor and
storage. Efficient software performs its tasks quickly without wasting resources.

**Usability.** How easy the software is for users to learn and operate. A good system should not
confuse users; it should be simple, clear and user-friendly.

**Maintainability.** How easy it is to modify, update or fix the software when changes are
needed. Well-structured software is easier to maintain over time.

**Portability.** The ability to run on different platforms or environments, such as different
operating systems or devices, without major changes.

**Security.** Protecting the software and its data from unauthorised access, attacks or damage.
A secure system ensures user data remains safe and confidential.

## Distinguishing SQA from testing

Testing is primarily concerned with defect detection via code execution. SQA is a broader,
continuous discipline focused on process prevention and standards compliance.
