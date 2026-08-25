# ASSESSMENT BANK: CONSTRUCTION

## Recall

1. State the three goals of coding.
2. Name six representative coding standards.
3. State the seven coding guidelines with their specific values where given.
4. Name eight characteristics of a programming language.

## Multiple choice

**Q1.** According to the stated goals of the coding phase, the primary purpose of efficient coding
is to:
A. minimise the effort spent during the coding phase itself
B. reduce the cost of later phases, particularly testing and maintenance
C. maximise lines of code produced per developer
D. eliminate the need for design documentation
*Answer: B*

**Q2.** Why do the coding guidelines recommend limiting function length?
A. longer functions compile more slowly
B. a lengthy function probably carries out many different functions and tends to have a
   disproportionately larger number of bugs
C. long functions cannot be indented correctly
D. compilers reject functions above a certain size
*Answer: B*

**Q3.** Why are `goto` statements prohibited by the coding standards?
A. they are slower at runtime
B. they make a program unstructured and very difficult to read and maintain
C. they prevent compilation
D. they require additional memory
*Answer: B*

**Q4.** Which activity best demonstrates adherence to professional standards?
A. omitting documentation to accelerate implementation
B. following organisational coding standards and peer review procedures
C. disabling software testing
D. ignoring version control practices
*Answer: B*

**Q5.** A development team refuses to perform code reviews because all members consider themselves
highly experienced. Which statement best describes this decision?
A. experience eliminates the need for peer review
B. it weakens quality assurance and violates responsible engineering practice
C. it improves software reliability
D. it accelerates maintenance activities
*Answer: B*

## Scenario

**S1.** Your project's language and framework make the 80-character line limit and the 10-line
function limit impractical. What do you do, and what would make your deviation a process failure
rather than a legitimate engineering decision?

**S2.** A reviewer finds a hard-coded database password in a pull request. Describe every step you
would take, in order.

**S3.** Your codebase has one comment per line, and every comment restates the code. Assess this
against the stated guideline, and say what you would change.

## Marking notes

- S1 must record the deviation with a reason in the project coding standard. Undocumented deviation
  is the failure, not deviation itself.
- S2 must include rotating the credential, not merely removing it, because the history retains it.
- S3 must distinguish the guideline's intent (documented code) from its proxy (density), and argue
  for commenting the why rather than the what.
