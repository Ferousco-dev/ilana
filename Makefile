# Ilana - repository tasks.

SHELL := /bin/sh
SKILL := skill
SCRIPTS := $(SKILL)/instruments/scripts
VERSION := $(shell cat VERSION)

.DEFAULT_GOAL := help

.PHONY: help
help: ## show this help
	@printf '\nilana %s\n\n' "$(VERSION)"
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[1m%-18s\033[0m %s\n", $$1, $$2}'
	@printf '\n'

.PHONY: install
install: ## install the skill into every detected agent (symlink)
	@./bin/ilana install --link --all

.PHONY: install-copy
install-copy: ## install by copying instead of linking
	@./bin/ilana install --copy --all

.PHONY: doctor
doctor: ## verify the installation
	@./bin/ilana doctor

.PHONY: uninstall
uninstall: ## remove installed skills (never touches project ledgers)
	@./bin/ilana uninstall

.PHONY: check
check: validate lint-shell lint-python no-emdash ## run every check

.PHONY: validate
validate: ## verify the skill payload is structurally complete
	@sh tests/validate.sh

.PHONY: lint-shell
lint-shell: ## syntax-check the shell scripts
	@for f in bin/ilana install.sh $(SKILL)/update/check-update.sh tests/validate.sh; do \
	  sh -n "$$f" && printf '  ok   %s\n' "$$f" || exit 1; \
	done
	@command -v shellcheck >/dev/null 2>&1 && shellcheck -S warning bin/ilana install.sh || \
	  printf '  skip shellcheck not installed\n'

.PHONY: lint-python
lint-python: ## compile-check the instruments
	@python3 -m py_compile $(SCRIPTS)/*.py && printf '  ok   instruments compile\n'
	@rm -rf $(SCRIPTS)/__pycache__

.PHONY: no-emdash
no-emdash: ## enforce the house style: no em dashes anywhere
	@if find . -name '*.md' -not -path './.git/*' -print0 | xargs -0 grep -l "$$(printf '\342\200\224')" 2>/dev/null | head -1 | grep -q .; then \
	  printf 'em dash found in:\n'; \
	  find . -name '*.md' -not -path './.git/*' -print0 | xargs -0 grep -l "$$(printf '\342\200\224')" 2>/dev/null | sed 's|^|  |'; \
	  exit 1; \
	else printf '  ok   no em dashes\n'; fi

.PHONY: metrics
metrics: ## run the metrics engine against this repository
	@python3 $(SCRIPTS)/metrics.py --repo .

.PHONY: gate
gate: ## run a gate check, e.g. make gate G=G4 R=3
	@python3 $(SCRIPTS)/gate_check.py --gate $(or $(G),G4) --rigour $(or $(R),3) --repo .

.PHONY: trace
trace: ## run the traceability checker
	@python3 $(SCRIPTS)/traceability.py --file .ilana/traceability.csv

.PHONY: tree
tree: ## print the skill structure
	@find $(SKILL) -type f -name '*.md' | sort | sed 's|^|  |'

.PHONY: count
count: ## count the skill payload
	@printf '  files:   %s\n' "$$(find $(SKILL) -type f | wc -l | tr -d ' ')"
	@printf '  phases:  %s\n' "$$(find $(SKILL)/phases -maxdepth 1 -mindepth 1 -type d | wc -l | tr -d ' ')"
	@printf '  agents:  %s\n' "$$(find $(SKILL)/agents -name AGENT.md | wc -l | tr -d ' ')"
	@printf '  gates:   %s\n' "$$(find $(SKILL)/gates -name 'G*.md' | wc -l | tr -d ' ')"
	@printf '  words:   %s\n' "$$(cat $$(find $(SKILL) -name '*.md') | wc -w | tr -d ' ')"

.PHONY: release
release: check ## tag a release, e.g. make release V=1.1.0
	@test -n "$(V)" || { printf 'usage: make release V=1.1.0\n'; exit 1; }
	@printf '%s\n' "$(V)" > VERSION
	@sed -i.bak 's/version: [0-9.]*/version: $(V)/' $(SKILL)/SKILL.md && rm -f $(SKILL)/SKILL.md.bak
	@git add VERSION $(SKILL)/SKILL.md CHANGELOG.md
	@git commit -m "release $(V)"
	@git tag -a "v$(V)" -m "ilana $(V)"
	@printf '\ntagged v%s. push with: git push && git push --tags\n' "$(V)"

.PHONY: setup-repo
setup-repo: ## point the repo at your GitHub account, e.g. make setup-repo OWNER=yourhandle
	@test -n "$(OWNER)" || { printf 'usage: make setup-repo OWNER=yourhandle\n'; exit 1; }
	@files=$$(grep -rl 'OWNER' --include='*.md' --include='*.yml' --include='*.yaml' \
	   --include='*.json' --include='*.cff' --include='*.sh' --include='CODEOWNERS' \
	   . 2>/dev/null | grep -v '^./source/' | grep -v '^./.git/'); \
	 for f in $$files bin/ilana Makefile; do \
	   sed -i.bak "s|Ferousco-dev/ilana|$(OWNER)/ilana|g; s|@Ferousco-dev|@$(OWNER)|g" "$$f" && rm -f "$$f.bak"; \
	 done; \
	 printf 'repository now points at github.com/%s/ilana\n' "$(OWNER)"
	@printf 'remaining OWNER references: %s\n' "$$(grep -rl 'OWNER' --include='*.md' --include='*.yml' . 2>/dev/null | grep -v source | wc -l | tr -d ' ')"

.PHONY: topics
topics: ## set the GitHub repository topics (requires gh)
	@gh repo edit --add-topic ai-skill,claude-skill,claude-code,codex,agent-skills,software-engineering,sdlc,requirements-engineering,software-testing,software-quality-assurance,cmmi,iso-12207,devops,scm,process-improvement,software-architecture,code-review,technical-documentation,oau,open-source
