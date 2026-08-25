# PHASE 04 ANTI-PATTERNS

## Code Without a Requirement
A feature appears in the codebase that no requirement asked for and no test covers. It is now
maintained forever by people who do not know why it exists.
**Fix:** Article 3. Write the requirement or delete the code.

## The Hidden Credential
A static admin account, a hard-coded API key, a debug bypass left in "temporarily". The source
material calls the deliberate version of this a criminal offence, not a coding mistake.
**Fix:** secret scan at G4. Refusal protocol R1 if requested deliberately.

## The Swallowed Exception
`try { ... } catch { }`. The failure happened, nobody knows, the data is now wrong and the log
is silent.
**Fix:** handle it, or propagate it with context. Never absorb it.

## Comments That Restate the Code
`// increment i` above `i++`. This is comment density theatre. It satisfies a metric and
communicates nothing.
**Fix:** comment the decision, the constraint, the non-obvious reason. Delete the rest.

## The Standard Nobody Wrote Down
Everyone "knows" the conventions. New contributors guess. Reviews become arguments about taste.
**Fix:** `docs/coding-standard.md` plus a formatter config that ends the argument mechanically.

## Review as Rubber Stamp
Approved in 40 seconds, 900 lines changed. The record says the review happened. It did not.
**Fix:** small changes, and the review record template. A review with no comments on a large
change is itself a finding.

## Skipping Review Because the Team Is Senior
The specific case named in the source material. Experience does not eliminate the need for peer
review; it changes what the review finds.
**Fix:** G4 criterion 9. No exceptions above RIGOUR 3.

## The Long Function
Two hundred lines doing seven things, with a comment header for each thing. Those comment
headers are the function boundaries you did not create.
**Fix:** each comment header becomes a named function. The names replace the comments.

## Copy-Paste From the Internet
Code arrives with unknown licence, unknown provenance, unknown behaviour. This risks both
Article 8 and Article 9.
**Fix:** understand it before you keep it, and record where it came from and under what licence.

## Optimising the Coding Phase
Rushing construction to hit a date, producing code that costs three times as much in testing and
maintenance. This inverts the stated goal of the phase.
**Fix:** the goal is to cut the cost of *later* stages. Say so out loud when schedule pressure
arrives.
