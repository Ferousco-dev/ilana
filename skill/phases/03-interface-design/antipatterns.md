# PHASE 03 ANTI-PATTERNS

## The Exempt CLI
"It's just a command line tool, it doesn't need interface design." The source material is
explicit that text-based interfaces rely on recall rather than recognition and that navigation
is harder. That means the principles apply *more*, not less.

## Feedback in the Log
The system knows what happened. The log knows what happened. The user does not.
**Fix:** every action produces an observable response at the interface the user is looking at.

## The Implementation Error Message
`NullPointerException`, `ERR_CONN_REFUSED`, `constraint violation on fk_order_customer`. These
tell the user nothing they can act on and tell an attacker more than they should know.
**Fix:** the error catalogue. Four columns, all filled.

## No Undo, No Confirm
A destructive action one click away with no confirmation and no recovery. This is a direct
violation of the tolerance principle.
**Fix:** enumerate destructive actions and give each one a recovery path.

## Intolerant Input
The date field accepts exactly one format and rejects the other four a reasonable person would
type. The machine is making the human do parsing work.
**Fix:** tolerate varied input where the interpretation is unambiguous. Reject clearly where it
is not.

## Consistency Drift
Screen one calls it "Cancel", screen two calls it "Discard", screen three calls it "Back".
Users cannot build a model of a system that will not hold still.
**Fix:** a vocabulary list in the interface specification, applied everywhere.

## Decoration Mistaken for Design
Graphics that carry no information, animation that delays the task, an icon set nobody can
read without hovering.
**Fix:** the visibility test. Anything neither needed nor removable is a finding.

## Designing for the Demo
The interface is optimised for the five-minute demonstration and hostile to the two-hour shift.
**Fix:** design for frequency. Ask question 2 in `questions.md` and mean it.

## Accessibility Deferred
"We'll add accessibility later." Keyboard reachability and semantic structure are structural,
like security. Retrofitting them means rebuilding.
**Fix:** G3 criterion 7 at RIGOUR 3 and above.
