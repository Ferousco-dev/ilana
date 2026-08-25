## What this changes

<!-- One or two sentences. What is different after this merges. -->

## Why

<!-- What problem this solves. If it is a gate criterion or an anti-pattern, describe the real
     situation that motivated it. -->

## Change class

<!-- See GOVERNANCE.md -->

- [ ] Editorial (typo, clarity, formatting)
- [ ] Additive (new adapter, anti-pattern, questions, example)
- [ ] Substantive (new gate criterion, template, changed default)
- [ ] Structural (new phase, changed constitutional article, ledger format)
- [ ] Breaking (changes how existing projects behave)

## Traceability

<!-- Article 3 applies to Ilana itself. -->

What is this traceable to?

- [ ] The SEN102/212 source material (say which section)
- [ ] A named standard (ISO/IEC 12207, IEEE 830/1016/829, CMMI, ACM/IEEE)
- [ ] Defensible engineering practice (say what evidence)
- [ ] A real failure you have watched happen (describe it briefly)

Details:

## If this touches a gate

- **What does it catch?** (a specific defect class, with an example)
- **At what rigour does it apply, and why that threshold?**
- **What is the evidence a reviewer would check?**
- **Is it automatable?** If yes, is `gate_check.py` updated? If no, is it marked `MANUAL`?

## If this touches an adapter

- Agent and version tested on:
- Install path verified:
- Sub-agent support: yes / no / partial
- What degrades without sub-agents:

## Checklist

- [ ] `make check` passes
- [ ] No em dashes anywhere
- [ ] New files follow the structure rules in `CONTRIBUTING.md`
- [ ] `CHANGELOG.md` updated under `[Unreleased]`
- [ ] Added myself to `AUTHORS.md` if this is my first contribution
- [ ] I have the right to license this contribution under MIT
