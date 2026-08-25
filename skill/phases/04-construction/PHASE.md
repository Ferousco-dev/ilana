# PHASE 04 - CONSTRUCTION

Owner: `constructor`. Entry gate: G3. Exit gate: G4.

> Coding is the process of transforming the design of a system into a computer language format.
> The goal is not to reduce the effort and cost of the coding phase, but to cut the cost of
> later stages.

That sentence is the whole phase. Code written to be fast to write is code that is expensive to
test and ruinous to maintain. Construction optimises for the phases that come after it.

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| Source code | the repository | n/a |
| Coding standard | `docs/coding-standard.md` | `templates/coding-standard.md` |
| Code review records | PR threads or `docs/reviews/` | `templates/code-review.md` |
| Dependency register | `docs/dependencies.md` | `templates/dependency-register.md` |

---

## The three goals of coding

1. **Translate the design into a computer language format** that a machine can execute and that
   performs the tasks specified during design.
2. **Reduce the cost of later phases.** Testing and maintenance cost can be significantly
   reduced by efficient coding.
3. **Make the program readable.** Readability and understandability as explicit objectives of
   the coding activity themselves help produce more maintainable software.

Note that coding is done by programmers who are, in the classical model, distinct people from
the designers. That separation is why the design document has to be good enough to code from.

---

## Coding standards

A coding standard lists rules to be followed during coding: how variables are named, how code
is laid out, error return conventions, and so on. It is organisational, not personal.

The representative standards from the source material:

| Standard | Rule |
| --- | --- |
| **Indentation** | Proper, consistent indentation to emphasise the body of a control structure, the body of a conditional, and each new scope block. |
| **Inline comments** | Used frequently to analyse the functioning of a subroutine or key aspects of an algorithm. |
| **Limits on globals** | Explicit rules stating what types of data may be declared global and what may not. |
| **Structured programming** | Structured or modular methods only. No `goto`, because it produces code that is hard to read and maintain. |
| **Naming conventions** | A consistent convention across globals, locals and constants. One documented example: globals begin with a capital letter, locals are lower case, constants are all capitals. |
| **Error return conventions** | Uniform across the organisation. Functions encountering an error condition return consistently. Exception handling is uniform. |

## Coding guidelines

Guidelines are best practice rather than rule. The source material gives seven:

1. **Line length** at or below 80 characters. Longer lines may not display correctly on some
   terminals and tools, and some printers truncate at 80 columns.
2. **Spacing.** Appropriate spaces within a line improve readability.
   `cost = price + (price * sales_tax)` beats `cost=price+(price*sales_tax)`.
3. **Documentation.** As a rule of thumb, at least one comment line on average for every three
   source lines.
4. **Function length** should ordinarily not exceed about 10 source lines. A very long function
   is hard to understand because it probably does many different things, and long functions
   tend to carry a disproportionately large number of bugs.
5. **No `goto`.** It makes a program unstructured and very hard to understand.
6. **Inline comments** promote readability.
7. **Meaningful error messages.** Error handling is not only the logic to detect and handle
   errors, but also making the messages meaningful.

### How Ìlànà applies these in a modern codebase

Guidelines 1 and 4 are the two that provoke argument, and they should be adapted rather than
obeyed literally or ignored silently.

- **Line length.** 80 is a defensible default. 100 or 120 are equally defensible in a modern
  toolchain. Pick one, put it in a formatter config, and stop discussing it.
- **Function length.** The *principle* is that a function should do one thing. Ten lines is a
  proxy for that, and it is a good proxy in C. In a language with expressive constructs, a
  25-line function that does exactly one thing is better than three 8-line functions that only
  make sense together. Measure the principle (cyclomatic complexity, number of responsibilities)
  and use length as a warning signal, not a rule.
- **Comment density.** One in three is high for self-documenting code and low for a numerical
  algorithm. The real rule is: comment the *why*, never the *what*. If a comment restates the
  code, delete the comment; if it explains a decision, keep it forever.

Ìlànà requires only that the project's actual choices are **written down** in
`docs/coding-standard.md` with reasons. Undocumented deviation is the failure. Deviation with a
reason is engineering.

---

## Characteristics of a programming language

The course lists the properties by which a language is judged. They are worth having in mind
when a project is choosing one, and they belong in the toolchain decision record.

| Characteristic | Meaning |
| --- | --- |
| Cost | The ultimate cost of a language is a function of many of its characteristics. |
| Quick translation | It should permit quick translation. |
| Efficiency | It should allow creation of efficient object code. |
| Modularity | Programs can be developed as several separately compiled modules. |
| Readability | Programs can be written in a way that resembles a plain-English description of the underlying functions, so coding is essentially self-documenting. |
| Portability | High-level languages, being virtually machine-independent, make portable software easier. |
| Generality | Most high-level languages allow a vast range of programs, so the programmer need not become an expert in many diverse languages. |
| Brevity | The language can implement the algorithm with less code. |
| Error checking | Structure that ensures self-consistency and catches the many errors a programmer will make. |
| Wide availability | Translators exist for all major machines and primary operating systems. |

---

## Construction discipline in Ìlànà

1. **Every module traces to a `DES` element.** No orphan code. Article 3.
2. **Write the test with the code, not after it.** Handing untested code to phase 05 makes the
   verifier reconstruct your intent, badly.
3. **No secret ever enters the repository.** Configuration and secret stores exist for this.
4. **Errors are handled where they can be handled, and propagated with context where they
   cannot.** Swallowing an exception is a defect, not a style choice.
5. **Peer review before merge** at `RIGOUR` 3 and above. The source material is explicit that
   refusing code review because the team is experienced weakens quality assurance and violates
   responsible engineering practice.
6. **Commit messages are documentation.** They are read far more often than they are written.

---

## Exit

Run `checklist.md`, attempt G4. Handoff goes to `verifier` with the module list, the test hooks,
and every known limitation stated plainly.
