# Elicitation Plan

## 1. Stakeholder map

| Stakeholder | Role | Interest | Influence | Consulted how | When |
| --- | --- | --- | --- | --- | --- |
| | primary user / secondary user / commissioner / regulator / operator / support | | high / medium / low | interview / questionnaire / workshop / observation | |

Include stakeholders who are **affected but not consulted**, and say why they are not being
consulted. That row is often where the missing requirement lives.

## 2. Technique selection

| Technique | Applied to | Why this technique | Session owner |
| --- | --- | --- | --- |

Minimum two techniques. One is not elicitation, it is an opinion.

## 3. Interview guide

Open, then narrow, then confirm.

**Open**
1. Walk me through your day where this system would be involved.
2. What is the most irritating part of that, right now?
3. When it goes wrong, what does going wrong look like?

**Narrow**
4. How often does that happen? What does it cost when it does?
5. Who else is involved when that happens?
6. What do you do to work around it today?
7. What information do you need at that moment that you do not have?

**Confirm**
8. If the system did exactly X, would that solve it? What would it miss?
9. What would make you stop using this system?
10. Who else should I be talking to?

Question 10 is the highest-yield question in the set.

## 4. Observation protocol

- Observe the real task in the real environment, not a demonstration.
- Record what people actually do, including the workarounds they will not mention in an
  interview because they are embarrassed by them.
- Note interruptions. Systems designed for uninterrupted use fail in interrupted environments.

## 5. Document analysis

| Document | What it tells us | What it cannot tell us |
| --- | --- | --- |
| existing system source | current behaviour | intended behaviour |
| user manuals | intended behaviour | actual behaviour |
| support tickets | failure modes and user vocabulary | frequency of silent failure |
| regulations | domain requirements | how strictly they are enforced |
| prior project post-mortems | why the last attempt failed | |

## 6. Prototype plan

| Prototype | Question it answers | Fidelity | Disposal plan |
| --- | --- | --- | --- |

State the disposal plan explicitly. Prototypes that survive into production are one of the
most reliable sources of long-term technical debt.

## 7. Output

Each session produces a dated note with attendees, raw notes, and a numbered list of candidate
requirements. Candidates are promoted to `REQ` / `NFR` / `DOM` during analysis, not during the
session.
