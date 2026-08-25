# STANDARDS

## ISO/IEC 12207: Software Life Cycle Processes

A globally accepted standard defining what processes should exist when developing software from
start to finish.

**Purpose, threefold:** establish a common structure for software processes; clearly define the
activities involved in development and maintenance; ensure consistency across organisations and
projects.

### The three categories

| Category | Nature | Contains |
| --- | --- | --- |
| **Primary** | the core activities directly involved in building software | requirements analysis, design, implementation, testing, maintenance |
| **Supporting** | not development itself, but they support it | documentation, configuration management, quality assurance, verification and validation |
| **Organizational** | management and long-term improvement, corporate-wide governance | process improvement, training, infrastructure management |

### Classification quick answers

These are the ones that recur in assessment and in practice.

| Activity | Category |
| --- | --- |
| Software requirements analysis | primary |
| Software design | primary |
| Implementation | primary |
| System integration and testing | primary |
| **Software maintenance** | **primary** |
| Documentation | supporting |
| **Software configuration management** (version control, baseline tracking, change authorisation) | **supporting** |
| **Software quality assurance** | **supporting** |
| Verification and validation | supporting |
| **Corporate training programmes** | **organizational** |
| **Infrastructure management** | **organizational** |
| Institutional process improvement | organizational |

The two most commonly mistaken: software maintenance is **primary**, not supporting. Corporate
training and infrastructure management are **organizational**, not supporting.

**Importance:** standardises processes; improves communication because everyone shares one
framework; ensures quality and consistency across projects.

---

## ISO/IEC 25010: Software Quality Model

Supplies the quality characteristics that the seven attributes in phase 07 draw on. Where a
project needs a formal quality model to cite, this is it.

---

## IEEE documentation standards

| Standard | Covers | Used in Ìlànà at |
| --- | --- | --- |
| **IEEE 830** | Software Requirements Specification | `phases/01-requirements/templates/srs.md` |
| **IEEE 1016** | Software Design Description | `phases/02-architecture-design/templates/design-description.md` |
| **IEEE 829** | Software Test Documentation | `phases/05-verification/templates/test-plan.md` |

**Benefits:** standardised structure, improved quality, better communication.

### IEEE 830 structure (as used by Ìlànà)

```
1. Introduction
   1.1 Purpose  1.2 Scope  1.3 Definitions  1.4 References  1.5 Overview
2. Overall description
   2.1 Product perspective  2.2 Product functions  2.3 User characteristics
   2.4 Constraints  2.5 Assumptions and dependencies  2.6 Out of scope
3. Specific requirements
   3.1 Functional  3.2 Non-functional  3.3 Domain  3.4 External interfaces
4. Verification
5. Approval
```

### IEEE 829 test plan sections

Objectives, scope, strategy, environment, roles and responsibilities, risk analysis, schedule,
deliverables, exit criteria, suspension and resumption.

---

## Citing a standard honestly

If you say a document follows IEEE 830, it must follow the structure. If you deviate, say where
and why. Citing a standard you have not followed is worse than citing none, because it manufactures
confidence in a reader who will not check.
