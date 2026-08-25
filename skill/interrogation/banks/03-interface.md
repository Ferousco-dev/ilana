# ASSESSMENT BANK: INTERFACE DESIGN

## Recall

1. Name the two main types of user interface and one advantage and one disadvantage of each.
2. Name the five GUI characteristics.
3. Name the five UI design principles and state each in one sentence.
4. Which principle concerns overall user interface architecture?

## Multiple choice

**Q1.** Which UI design principle is concerned with putting related things together, separating
unrelated things, and making similar things resemble one another?
A. structure  B. simplicity  C. visibility  D. tolerance
*Answer: A*

**Q2.** Which principle requires the design to decrease the cost of errors and misuse by allowing
undoing and redoing, and by interpreting all reasonable actions?
A. feedback  B. visibility  C. tolerance  D. simplicity
*Answer: C*

**Q3.** Which principle requires that all options and materials for a given function are shown
without distracting the user with extraneous or redundant data?
A. structure  B. visibility  C. feedback  D. simplicity
*Answer: B*

**Q4.** A stated disadvantage of a text-based user interface is that it:
A. requires less expert knowledge  B. relies heavily on recall rather than recognition
C. offers fewer customisation options  D. is difficult to switch between applications
*Answer: B*

**Q5.** Which GUI characteristic allows different information to be displayed simultaneously on the
user's screen?
A. icons  B. menus  C. windows  D. pointing
*Answer: C*

## Scenario

**S1.** A CLI tool deletes a project with a single command and no confirmation. Which principle is
violated, and what are two acceptable fixes?

**S2.** Your application returns `Error 500: constraint violation on fk_order_customer` to the user.
Rewrite it, and state the four jobs a good error message must do.

**S3.** A colleague argues that UI principles do not apply to command line tools. Respond, using the
stated properties of text-based interfaces.

## Marking notes

- S1: tolerance. Fixes: confirmation prompt, undo window, `--dry-run`, or a recoverable soft delete.
- S2 must remove the implementation detail (which is also a security concern), state the cause in
  the user's terms, give the next action, and confirm work is preserved.
- S3 must argue that because text interfaces rely on recall rather than recognition and navigation
  is harder, the principles apply more, not less.
