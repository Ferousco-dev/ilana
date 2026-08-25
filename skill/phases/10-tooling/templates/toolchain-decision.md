# Toolchain Decision Record

| Field | Value |
| --- | --- |
| Project | |
| Owner | |
| Last reviewed | |

## 1. The chain

| Category | Tool chosen | Alternative considered | Why this one | Licence / cost | Owner in team | Exit path |
| --- | --- | --- | --- | --- | --- | --- |
| Version control | | | | | | |
| Repository hosting | | | | | | |
| CI/CD | | | | | | |
| Build | | | | | | |
| Test framework | | | | | | |
| Test automation (UI) | | | | | | |
| Static analysis | | | | | | |
| Security scanning | | | | | | |
| Secret scanning | | | | | | |
| Containerisation | | | | | | |
| Orchestration | | | | | | |
| Infrastructure as code | | | | | | |
| Defect tracking | | | | | | |
| Project board | | | | | | |
| Documentation | | | | | | |
| Monitoring | | | | | | |
| Alerting | | | | | | |

**Exit path** is the column people skip and later need. For each tool: if we had to leave it,
what would we lose and how would we get our data out?

## 2. Rejected tools

| Tool | Rejected because | Condition under which we would revisit |
| --- | --- | --- |

## 3. Automation inventory

What is automated, what is not, and the cost of the gap.

| Activity | Frequency | Manual effort each time | Automated | Annual cost of remaining manual |
| --- | --- | --- | --- | --- |

The last column is the argument for the next automation investment. Fill it with real numbers.

## 4. What deliberately stays human

| Activity | Why it is not automated |
| --- | --- |
| Requirements elicitation | requires judgement and relationship |
| Design trade-offs | requires context no tool holds |
| Exploratory testing | requires curiosity |
| Usability judgement | requires a human user |
| Ethical judgement | Article 1 |
| Acceptance decision | a business judgement, by definition |

Stating this explicitly prevents the recurring suggestion to automate them.

## 5. Total cost

| Tool | Licence | Infrastructure | Operating effort | Training | Annual total |
| --- | --- | --- | --- | --- | --- |

## 6. Review triggers

- A tool becomes unmaintained by its vendor or community.
- Cost changes materially.
- Team size crosses a threshold the tool does not handle.
- A tool becomes the bottleneck rather than the accelerator.
- Annually, regardless.
