# PHASE 07 ANTI-PATTERNS

## SQA Equals Testing
The team has tests, therefore it has quality assurance. But testing is detection and SQA is
prevention. A project with excellent tests and no reviews, no standards and no metrics has one
half of quality.
**Fix:** the five core activities. Testing is one of five.

## The Quality Plan Written for the Audit
Produced after construction, describing what was done. It is a report wearing a plan's clothes,
and it controlled nothing.
**Fix:** G7 checks the date. A quality plan is an input to construction.

## The Walkthrough Called an Inspection
The record says "inspection". What happened was the author talking through their own code with
no Moderator, no Reader, no Recorder and no procedure.
**Fix:** record what actually happened. Both are legitimate activities; misnaming them corrupts
the evidence.

## The Audit by the Team Being Audited
Independence is the entire mechanism that makes an audit objective. Auditing yourself produces a
document, not an assessment.
**Fix:** at RIGOUR 3+, a named auditor from outside the delivery team.

## One Metric Category
Only product metrics (lines of code, coverage), or only project metrics (are we on schedule).
The three categories answer different questions and one alone gives a distorted picture.
**Fix:** one of each, minimum, at G7.

## Metrics Nobody Acts On
Measured, dashboarded, never used to change anything. This is measurement theatre and it costs
real effort.
**Fix:** every metric names the decision it informs. A metric that informs no decision is
deleted.

## Quality as an Adjective
"The code quality is good." Based on what? Article 10 exists for exactly this sentence.
**Fix:** the scorecard. Evidence per attribute, or `UNVERIFIED`.

## Correctness Mistaken for Quality
It passes its tests, therefore it is high quality. But it takes 45 seconds to load a menu,
consumes almost all available memory, and nobody can maintain it.
**Fix:** all seven attributes, every time.

## Reviews as Compliance Ritual
Every PR gets an approval within a minute so the process metric looks healthy. The control has
been converted into its own measurement.
**Fix:** classify and count review findings. A large change with zero findings is itself a
finding.
