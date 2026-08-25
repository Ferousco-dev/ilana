# PHASE 05 QUESTIONS

Maximum five.

1. What must never break? Name the two or three behaviours whose failure would be unacceptable.
   Those get the deepest testing.
2. Who performs acceptance testing, and when are they available? (If the answer is "the
   developers", the acceptance level does not exist and G5 must record that.)
3. What is the test environment, and how does it differ from production? Every difference is a
   class of defect you will not find.
4. What test data exists? Is any of it real personal or financial data? (If yes, that is an
   Article 7 problem and needs synthetic data before anything else.)
5. What are the exit criteria: what condition means testing is finished?

## Ask when there is an existing suite

6. Which tests currently fail or are skipped, and why?
7. Are there known flaky tests? (Flaky tests destroy the value of the whole suite by teaching
   people to ignore red.)

## Ask for non-functional testing

8. What load must the system sustain, and has that number come from the NFR or from a guess?
