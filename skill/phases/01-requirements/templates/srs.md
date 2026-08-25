# Software Requirements Specification: <SYSTEM NAME>

Structure follows IEEE 830. Sections may be collapsed at RIGOUR 1 to 2 but not deleted.

| Field | Value |
| --- | --- |
| Document ID | SRS-<project>-v<n> |
| Status | draft / under review / baselined |
| Author | |
| Reviewers | |
| Baselined on | |
| Supersedes | |

---

## 1. Introduction

### 1.1 Purpose
What this document is for and who should read it.

### 1.2 Scope
What the system is, what it does, and the benefit it delivers.

### 1.3 Definitions, acronyms and abbreviations
Domain vocabulary. If a stakeholder uses a word the development team does not share, it
belongs here.

### 1.4 References
Standards, regulations, prior systems, interface contracts.

### 1.5 Overview
How the rest of this document is organised.

---

## 2. Overall description

### 2.1 Product perspective
Where this sits: standalone, a component, a replacement, an integration.

### 2.2 Product functions
A summary list. Detail belongs in section 3.

### 2.3 User characteristics
Who uses it, their expertise, their frequency of use, their environment.

### 2.4 Constraints
Regulatory, hardware, legacy interfaces, language, platform, budget, deadline.

### 2.5 Assumptions and dependencies
Every assumption gets a `DEC-###`. Unlogged assumptions are the failure mode this section
exists to prevent.

### 2.6 Out of scope
Explicit. This section prevents more disputes than any other.

---

## 3. Specific requirements

### 3.1 Functional requirements

```
REQ-001  [priority: must|should|could|wont]  [source: <who, how, when>]
<The system shall ...>

Rationale:
Acceptance criteria:
  Given <precondition>
  When <action>
  Then <observable outcome>
Failure behaviour:
Verified by: TC-
Depends on:
```

### 3.2 Non-functional requirements

Every one carries a number and a unit.

```
NFR-001  [category: performance|usability|reliability|security|scalability|maintainability|portability]
<measurable statement>

Measurement method:
Threshold:
Verified by: TC-
```

Categories to sweep, so none is forgotten:

| Category | Prompt |
| --- | --- |
| Performance | response time at what percentile, under what load |
| Usability | time to complete the primary task by a new user |
| Reliability | availability target, mean time between failures |
| Security | authentication, authorisation, encryption at rest and in transit, audit |
| Scalability | concurrent users, data volume, growth horizon |
| Maintainability | who maintains it, how fast a change must be deliverable |
| Portability | which platforms, browsers, devices, operating systems |

### 3.3 Domain requirements

```
DOM-001  [source rule: <regulation, standard, industry norm, with citation>]
<statement>

Applies because:
Consequence of non-compliance:
Verified by: TC-
```

If no domain requirement applies, state which rules were checked and found inapplicable.

### 3.4 External interface requirements
User interfaces, hardware interfaces, software interfaces, communication interfaces.

---

## 4. Verification

Traceability summary. Full matrix in `.ilana/traceability.csv`.

| Requirement | Type | Priority | Design | Test cases | Status |
| --- | --- | --- | --- | --- | --- |

---

## 5. Approval

| Role | Name | Date | Signature |
| --- | --- | --- | --- |
| Author | | | |
| Stakeholder representative | | | |
| Technical reviewer | | | |
