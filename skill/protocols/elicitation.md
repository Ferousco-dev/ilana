# PROTOCOL: ELICITATION

Requirement elicitation is the process of identifying requirements from the people or users
involved. It is the first stage of requirements engineering.

## Technique selection

Never one technique. One technique produces an opinion.

| Technique | Best for | Weakness | Minimum to be useful |
| --- | --- | --- | --- |
| Interviews | depth, and the *why* behind a request | small sample, interviewer bias | 3 people across 2 roles |
| Questionnaires | breadth across many users | shallow, no follow-up | 20 responses |
| Workshops | stakeholders who disagree and need to hear each other | the loudest voice dominates | a facilitator who is not a stakeholder |
| Brainstorming | a genuinely open solution space | volume without priority | a convergence step afterwards |
| Observation | users who cannot articulate what they actually do | expensive, observer effect | the real task in the real environment |
| Document analysis | replacement or integration | documents describe the past | the source system plus its support tickets |
| Use cases and scenarios | conditional, multi-step behaviour | can miss non-functional needs | the failure paths, not only the happy path |
| Prototyping | users who cannot judge a description but can judge a thing | mistaken for the product | a stated disposal plan |

**Ìlànà default:** interviews plus document analysis plus one scenario or prototype pass. Add
observation whenever a user says "it's hard to explain, you'd have to see it". That sentence is
the single most reliable signal that interviews alone will fail.

## Interview structure

Open, narrow, confirm.

**Open**
1. Walk me through your day where this system would be involved.
2. What is the most irritating part of that right now?
3. When it goes wrong, what does going wrong look like?

**Narrow**
4. How often does that happen, and what does it cost when it does?
5. Who else is involved when that happens?
6. What do you do to work around it today?
7. What information do you need at that moment that you do not have?

**Confirm**
8. If the system did exactly X, would that solve it? What would it miss?
9. What would make you stop using this system?
10. **Who else should I be talking to?**

Question 10 is the highest-yield question in requirements engineering. Ask it every time.

## Recording

Every session produces a dated note with attendees, raw notes, and a numbered list of candidate
requirements. **Candidates are promoted to `REQ`, `NFR` or `DOM` during analysis, never during the
session.** Promoting in the room means promoting whatever was said most confidently.

## The read-back loop

This is the mechanism that prevents the most expensive class of defect.

1. Stakeholder states the need.
2. Analyst writes it as a requirement with an acceptance criterion.
3. **Analyst reads it back to the stakeholder in the stakeholder's own vocabulary.**
4. Stakeholder confirms in writing, with a date.
5. It enters the SRS.

Step 3 is what teams skip and it is what catches the misunderstanding. The source material is
explicit that a business analyst misunderstanding a requirement due to poor communication, with
developers then faithfully implementing the incorrect specification, is an ineffective team
dynamics failure during requirements engineering.

## The domain sweep

Before leaving elicitation, ask explicitly:

- Which regulator, standard or industry rule applies?
- What does the industry take for granted that an outsider would not know?
- What is the consequence of non-compliance?

If nothing applies, record which rules were checked and found inapplicable. Empty because
unexamined is a G1 failure.

## Elicitation is not a phase you leave

The process is cyclical. Analysis exposes gaps that send you back. Plan for a second pass; a team
that treats elicitation as a one-week event at the start will discover its gaps during
construction instead.
