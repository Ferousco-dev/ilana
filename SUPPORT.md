# SUPPORT

## Before asking

```bash
ilana doctor          # verifies the installation and reports what is missing
make check            # validates the payload if you are working from a clone
```

Most installation problems are one of three things: `~/.local/bin` is not on your PATH, the agent
looks in a different directory than you installed to, or an old copy is shadowing the symlink.
`ilana doctor` reports all three.

## Where to go

| I want to | Go to |
| --- | --- |
| Report a bug | GitHub Issues, bug report template |
| Request a feature or a new gate criterion | GitHub Issues, feature template |
| Add support for a coding agent | GitHub Issues, adapter template, or a pull request |
| Ask how something works | GitHub Discussions |
| Report a security issue | **Not an issue.** See `SECURITY.md` |
| Report a code of conduct violation | Private contact below |

## Documentation

| Question | Document |
| --- | --- |
| How do I install and start? | `docs/quickstart.md` |
| Why is it built this way? | `docs/architecture.md` |
| Common questions | `docs/faq.md` |
| Where is topic X from my course? | `docs/syllabus-map.md` |
| What does a real run look like? | `docs/examples/` |
| How do I use it with my agent? | `adapters/` |
| How do I contribute? | `CONTRIBUTING.md` |

## Private contact

For security reports and code of conduct matters, use GitHub's private vulnerability reporting on
this repository, or contact a maintainer listed in `.github/CODEOWNERS` directly.

## Response expectations

This is a volunteer project. Realistic expectations:

| Kind | Typical response |
| --- | --- |
| Security report | 3 working days |
| Bug report | 1 week |
| Feature request | 2 weeks |
| Pull request | 1 week for a first look |
| Discussion | when someone has time |

## Not supported

- Writing your software for you. Ìlànà is a process, and the process still requires you.
- Debugging your project's code. Use Ìlànà's `DOCTOR` mode for process problems and your own tools
  for code problems.
- Guarantees about any agent's behaviour. Ìlànà is instructions. How well an agent follows them
  depends on the agent.
- Formal CMMI appraisal. Ìlànà produces indicative self-assessments. A formal appraisal requires
  certified appraisers.
