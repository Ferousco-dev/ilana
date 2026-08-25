# PHASE 04 REFERENCE

## Definition

Coding is the process of transforming the design of a system into a computer language format.
This phase of software development is concerned with translating the design specification into
source code. It is necessary to write source code and internal documentation so that
conformance of the code to its specification can be easily verified.

Coding is done by coders or programmers, who are people independent of the designer. The goal
is not to reduce the effort and cost of the coding phase, but to cut the cost of later stages.
The cost of testing and maintenance can be significantly reduced with efficient coding.

## Goals of coding

1. **To translate the design of the system into a computer language format.** The resulting
   program can be executed by a computer and performs the tasks specified by the design.
2. **To reduce the cost of later phases.** The cost of testing and maintenance can be
   significantly reduced with efficient coding.
3. **To make the program more readable.** A program should be easy to read and understand.
   Having readability and understandability as a clear objective of the coding activity can
   itself help produce more maintainable software.

## Characteristics of a programming language

- **Cost.** The ultimate cost of a programming language is a function of many of its
  characteristics.
- **Quick translation.** It should permit quick translation.
- **Efficiency.** It should allow the creation of efficient object code.
- **Modularity.** Programs can be developed as several separately compiled modules.
- **Readability.** A good high-level language allows programs to be written in ways that
  resemble a quite-English description of the underlying functions, so coding can be done in an
  essentially self-documenting way.
- **Portability.** High-level languages, being virtually machine-independent, make portable
  software easier to develop.
- **Generality.** Most high-level languages allow the writing of a vast collection of programs,
  relieving the programmer of the need to become an expert in many diverse languages.
- **Brevity.** The language should be able to implement the algorithm with less code. Programs
  in high-level languages are often significantly shorter than their low-level equivalents.
- **Error checking.** A programmer is likely to make many errors. High-level languages provide
  structure for ensuring self-consistency among modules.
- **Wide availability.** Translators should exist for all major machines and primary operating
  systems.

## Coding standards

General coding standards refer to how a developer writes code. A coding standard lists rules to
be followed during coding: how variables are named, how code is laid out, error return
conventions, and so on.

**Representative standards:**

- **Indentation.** Proper and consistent indentation is essential in producing easy-to-read and
  maintainable programs. Use indentation to emphasise the body of a control structure such as a
  loop or a select statement, the body of a conditional statement, and a new scope block.
- **Inline comments.** Inline comments analysing the functioning of a subroutine, or key aspects
  of an algorithm, should be used frequently.
- **Rules for limiting the use of globals.** These rules state what types of data can be
  declared global and what cannot.
- **Structured programming.** Structured or modular programming methods shall be used. `goto`
  statements shall not be used, as they lead to unstructured code that is hard to read and
  maintain.
- **Naming conventions** for global variables, local variables and constant identifiers. One
  possible convention: global variable names always begin with a capital letter, local variable
  names are lower case, and constant names are always capitals.
- **Error return conventions and exception handling.** How different functions report error
  conditions should be standard within an organisation. For example, on encountering an error
  condition, different functions should consistently return either 0 or 1.

## Coding guidelines

General coding guidelines give the programmer a set of best methods to make programs more
comfortable to read and maintain.

1. **Line length.** Keep source lines at or below 80 characters. Longer lines may not be visible
   properly on some terminals and tools, and some printers truncate lines longer than 80 columns.
2. **Spacing.** Appropriate use of spaces within a line improves readability.
   Bad: `cost=price+(price*sales_tax)`.
   Better: `cost = price + ( price * sales_tax )`.
3. **The code should be well documented.** As a rule of thumb, there should be at least one
   comment line on average for every three source lines.
4. **Function length.** The length of any function should not exceed 10 source lines. A very
   lengthy function is generally difficult to understand because it possibly carries out many
   different functions. For the same reason, lengthy functions are likely to have a
   disproportionately larger number of bugs.
5. **Do not use `goto` statements.** Their use makes a program unstructured and very difficult
   to understand.
6. **Inline comments** promote readability.
7. **Error messages.** Error handling is an essential aspect of programming. It includes both
   adding the necessary logic to test for and handle errors, and making error messages
   meaningful.
