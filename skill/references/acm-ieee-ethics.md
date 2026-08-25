# ACM/IEEE SOFTWARE ENGINEERING CODE OF ETHICS

**ACM**: Association for Computing Machinery.
**IEEE**: Institute of Electrical and Electronics Engineers.

Both are internationally recognised professional bodies that establish standards and publish
guidelines, including codes of ethics, to help software engineers practise responsibly.

Full text: https://www.acm.org/code-of-ethics

---

## The four principles Ìlànà applies

### 1. Public interest

Software engineers should act in ways that benefit and protect the public. They should not
knowingly release unsafe software and should always consider how their work affects users and
society.

**Where it binds in practice:**
- A defect that can cause harm is discovered late and management wants to ship. The correct action
  is to delay deployment, disclose the risk to stakeholders, resolve the defect, and repeat
  verification before release.
- Employer instruction conflicts with public safety. Public interest takes precedence.
- A team knowingly releases a faulty, unsafe system into a public healthcare environment. This is
  a direct violation of this clause.

### 2. Client and employer responsibilities

Software engineers should be honest, trustworthy and loyal to their clients or employers. They
should not hide important problems in a software system or misuse company resources for personal
gain.

**Where it binds:**
- Hiding project risks from management to obtain approval.
- Using company computing resources for personal commercial activity.
- Being asked to conceal financial calculation errors from customers. The correct response is to
  refuse, because the request violates professional ethics.

### 3. Product quality

Engineers have a responsibility to ensure the software they develop meets acceptable quality
standards. This includes proper testing and avoiding the release of software containing known
defects or serious faults.

**Where it binds:**
- Skipping integration testing to hit a date.
- Bypassing automated security testing in the pipeline to reduce build time.
- Refusing code review because the team considers itself experienced. This weakens quality
  assurance and violates responsible engineering practice.

### 4. Professional competence

Software engineers should possess the necessary knowledge and skills to perform their duties
effectively. They should continue learning and should avoid accepting tasks beyond their level of
competence.

**Where it binds:**
- Accepting a cryptographic architecture project without the necessary skills, training or
  technical capability.
- Proceeding on safety-critical or medical work without domain review.

The competent response is not to refuse all unfamiliar work. It is to consult domain experts,
acquire the necessary knowledge, and validate the design before implementation.

---

## The five ethical issues these map onto

| Issue | Core obligation |
| --- | --- |
| Honesty and integrity | accurate information about capabilities; no misleading stakeholders; truthful reporting of bugs, risks and challenges |
| Confidentiality | protect user information; no unauthorised disclosure; follow data protection policies |
| Quality and safety | meet required standards; systems safe for users; risks identified and mitigated. Neglecting quality for speed or cost is unethical |
| Intellectual property rights | respect copyright; honour licence terms; acknowledge ownership of code and ideas |
| Professional responsibility | follow established processes; adhere to standards; take responsibility for the work |

---

## Ethics in process adherence

The point the course makes most forcefully: **following a defined software process is not just a
technical requirement, it is an ethical responsibility.**

- Skipping testing to meet a deadline is unethical, because the team knowingly released software
  that had not been properly tested.
- Ignoring documentation standards is unethical, because it creates unnecessary problems for
  others who must maintain the system.
- Bypassing code or design reviews to save time is unethical, because reviews exist to identify
  errors and reduce risk before release.

A responsible engineer follows established processes not because the organisation requires them,
but because it is the right thing to do for users, the organisation and society.

---

## What this does not mean

The code is not a reason to refuse ordinary engineering work that merely sounds risky. Security
tooling for authorised testing, handling sensitive data correctly, aggressive refactoring, shipping
quickly on a low-stakes project: none of these engage the code. Overapplying it is its own failure,
because it trains people to ignore it when it matters.
