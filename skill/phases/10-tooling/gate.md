# PHASE 10 GATE

This phase is continuous and has no dedicated gate. It is checked inside G4 (standard
enforcement), G5 (automation), G6 (build and deployment) and G7 (quality tooling).

At `RIGOUR` 1 to 2 the minimum toolchain is:

1. Version control.
2. A way to run the tests with one command.
3. Somewhere the defects are written down, even a file.

At `RIGOUR` 3 and above, add: CI that blocks merge, secret scanning, and a tracker whose workflow
matches the real one.
