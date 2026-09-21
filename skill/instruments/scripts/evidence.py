#!/usr/bin/env python3
"""Ilana evidence capture, commit hygiene, handoff and final report.

One place for the facts an agent would otherwise retype into three documents.
Stdlib only. Python 3.8+.

Usage:
    python3 evidence.py policy   [--repo .] [--ceremony standard] [--stop TEXT ...] [--show]
    python3 evidence.py run      [--repo .] [--label L] -- CMD ARGS...
    python3 evidence.py commit-check [--repo .] [FILE|-]
    python3 evidence.py hook     [--repo .]
    python3 evidence.py handoff  [--repo .] [--set KEY=VALUE ...] [--add KEY=VALUE ...] [--show]
    python3 evidence.py report   [--repo .]

Files (all under .ilana/):
    policy.json        ceremony level, commit rules, stop boundary
    evidence.jsonl     one record per command run, referenced by EV-### id, never copied
    handoff.json       the single machine-readable state of the current milestone
    milestone-state.md rendered view of handoff.json (regenerated, never hand-edited)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime

ILANA = ".ilana"
POLICY = "policy.json"
EVIDENCE = "evidence.jsonl"
HANDOFF = "handoff.json"
STATE_MD = "milestone-state.md"

CONVENTIONAL = re.compile(r"^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([^)\s]+\))?!?: \S.*$")
AI_PATTERNS = [
    r"co-authored-by\s*:", r"signed-off-by\s*:.*(claude|anthropic|codex|openai|copilot|gemini|chatgpt|bot)",
    r"generated (with|by) (claude|an? ai|ai|chatgpt|codex|copilot|gemini)", r"\bclaude\b", r"\banthropic\b", r"\bcodex\b", r"\bchatgpt\b", r"\bopenai\b",
    r"\bcopilot\b", r"\bgemini\b", r"\bai[- ]assisted\b", r"\U0001F916",
]
SECRET_TAIL = re.compile(r"(?i)((?:password|passwd|secret|token|api[_-]?key|authorization)\s*[=:]\s*)\S+")
LIST_KEYS = ("completed", "verified", "remaining", "limitation", "disagreement", "decision")
SCALAR_KEYS = ("milestone", "step", "next", "ceremony", "base_commit", "stop_before")

CEREMONY_RIGOUR = {"light": 2, "standard": 3, "regulated": 4}


def now():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def path(repo, name):
    return os.path.join(repo, ILANA, name)


def load(repo, name, default):
    try:
        with open(path(repo, name), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def save(repo, name, data):
    os.makedirs(os.path.join(repo, ILANA), exist_ok=True)
    with open(path(repo, name), "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, sort_keys=True)
        fh.write("\n")


def git(repo, *args):
    try:
        out = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


def default_policy(ceremony="standard"):
    return {
        "ceremony": ceremony,
        "commit": {"conventional": True, "forbid_ai_attribution": True, "header_max": 72},
        "stop_boundary": [],
    }


# ---------------------------------------------------------------- policy ----

def cmd_policy(args):
    pol = load(args.repo, POLICY, None) or default_policy()
    if args.ceremony:
        if args.ceremony not in CEREMONY_RIGOUR:
            print("ceremony must be light, standard or regulated", file=sys.stderr)
            return 2
        pol["ceremony"] = args.ceremony
    if args.stop:
        pol["stop_boundary"] = list(args.stop)
    if not args.show:
        save(args.repo, POLICY, pol)
    print(json.dumps(pol, indent=2, sort_keys=True))
    return 0


# ------------------------------------------------------------------- run ----

def next_id(records):
    return "EV-%03d" % (len(records) + 1)


def read_records(repo):
    records = []
    try:
        with open(path(repo, EVIDENCE), encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
    except OSError:
        pass
    return records


def cmd_run(args):
    cmd = list(args.cmd)
    if cmd and cmd[0] == "--":
        cmd = cmd[1:]
    if not cmd:
        print("usage: evidence.py run [--label L] -- CMD ARGS...", file=sys.stderr)
        return 2
    started = time.time()
    try:
        proc = subprocess.run(cmd, cwd=args.repo, capture_output=True, text=True)
        code, output = proc.returncode, (proc.stdout or "") + (proc.stderr or "")
    except OSError as exc:
        code, output = 127, str(exc)
    tail = [SECRET_TAIL.sub(r"\1[redacted]", ln.strip())[:200] for ln in output.splitlines() if ln.strip()][-3:]
    records = read_records(args.repo)
    record = {
        "id": next_id(records), "ts": now(), "label": args.label or cmd[0], "cmd": " ".join(cmd),
        "exit": code, "seconds": round(time.time() - started, 1),
        "head": git(args.repo, "rev-parse", "--short", "HEAD"),
        "dirty": bool(git(args.repo, "status", "--porcelain")), "tail": tail,
    }
    os.makedirs(os.path.join(args.repo, ILANA), exist_ok=True)
    with open(path(args.repo, EVIDENCE), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")
    print("%s %s exit=%d %.1fs  %s" % (record["id"], "PASS" if code == 0 else "FAIL", code, record["seconds"], record["cmd"]))
    return code


# ---------------------------------------------------------- commit-check ----

def check_message(message, policy):
    problems = []
    lines = message.splitlines()
    header = next((ln for ln in lines if ln.strip() and not ln.startswith("#")), "")
    rules = policy.get("commit", {})
    if rules.get("conventional", True) and not CONVENTIONAL.match(header):
        problems.append("header is not a Conventional Commit (type(scope): subject): %r" % header[:80])
    if len(header) > int(rules.get("header_max", 72)):
        problems.append("header is %d characters (max %s)" % (len(header), rules.get("header_max", 72)))
    if rules.get("forbid_ai_attribution", True):
        body = "\n".join(ln for ln in lines if not ln.startswith("#"))
        for pattern in AI_PATTERNS:
            found = re.search(pattern, body, re.I)
            if found:
                problems.append("AI or automated-tool attribution is forbidden: matched %r" % found.group(0).strip())
    return problems


def cmd_commit_check(args):
    policy = load(args.repo, POLICY, None) or default_policy()
    if args.file in (None, "-"):
        message = sys.stdin.read()
    else:
        with open(args.file, encoding="utf-8") as fh:
            message = fh.read()
    problems = check_message(message, policy)
    for problem in problems:
        print("commit-check: " + problem, file=sys.stderr)
    if not problems:
        print("commit-check: ok")
    return 1 if problems else 0


def cmd_hook(args):
    hook = os.path.join(args.repo, ".git", "hooks", "commit-msg")
    marker = "# ilana-commit-check"
    if os.path.exists(hook):
        with open(hook, encoding="utf-8") as fh:
            if marker not in fh.read():
                print("a different commit-msg hook exists; not overwriting it", file=sys.stderr)
                return 1
    script = os.path.abspath(__file__)
    with open(hook, "w", encoding="utf-8") as fh:
        fh.write('#!/bin/sh\n%s\nexec python3 "%s" commit-check "$1"\n' % (marker, script))
    os.chmod(hook, 0o755)
    print("installed commit-msg hook (Conventional Commits, no AI attribution)")
    return 0


# --------------------------------------------------------------- handoff ----

def latest_by_label(records):
    latest = {}
    for record in records:
        latest[record["label"]] = record
    return latest


def cmd_handoff(args):
    repo = args.repo
    state = load(repo, HANDOFF, {})
    policy = load(repo, POLICY, None) or default_policy()
    for item in args.set or []:
        key, _, value = item.partition("=")
        if key not in SCALAR_KEYS:
            print("unknown key %r (use one of: %s)" % (key, ", ".join(SCALAR_KEYS)), file=sys.stderr)
            return 2
        state[key] = value
    for item in args.add or []:
        key, _, value = item.partition("=")
        if key not in LIST_KEYS:
            print("unknown list %r (use one of: %s)" % (key, ", ".join(LIST_KEYS)), file=sys.stderr)
            return 2
        state.setdefault(key, [])
        if value and value not in state[key]:
            state[key].append(value)
    state.setdefault("base_commit", git(repo, "rev-parse", "--short", "HEAD"))
    state["head"] = git(repo, "rev-parse", "--short", "HEAD")
    state["branch"] = git(repo, "branch", "--show-current")
    state["dirty_paths"] = len([ln for ln in git(repo, "status", "--porcelain", "-uall").splitlines() if ln])
    state["ceremony"] = state.get("ceremony") or policy.get("ceremony", "standard")
    state["stop_boundary"] = policy.get("stop_boundary", [])
    state["updated"] = now()
    state["evidence"] = {label: {"id": r["id"], "exit": r["exit"], "head": r["head"]}
                         for label, r in sorted(latest_by_label(read_records(repo)).items())}
    if not args.show or args.set or args.add:
        save(repo, HANDOFF, state)
        with open(path(repo, STATE_MD), "w", encoding="utf-8") as fh:
            fh.write(render_state(state, read_records(repo)))
    print(json.dumps(state, indent=2, sort_keys=True) if args.show else "handoff updated: %s, %s" % (HANDOFF, STATE_MD))
    return 0


def bullet(items):
    return "\n".join("- " + i for i in items) if items else "- none"


def render_state(state, records):
    latest = latest_by_label(records)
    rows = ["| %s | %s | %s | %s |" % (r["id"], label, "PASS" if r["exit"] == 0 else "FAIL", r["cmd"][:70])
            for label, r in sorted(latest.items())]
    text = [
        "# Milestone state: %s" % state.get("milestone", "(unset)"), "",
        "Ceremony %s. Step: %s. Base `%s`, head `%s` on `%s`; %d dirty path(s)." % (
            state.get("ceremony"), state.get("step", "(unset)"), state.get("base_commit"), state.get("head"),
            state.get("branch"), state.get("dirty_paths", 0)),
        "", "## Completed", bullet(state.get("completed", [])),
        "", "## Verified behavior", bullet(state.get("verified", [])),
        "", "## Remaining", bullet(state.get("remaining", [])),
        "", "## Known limitations", bullet(state.get("limitation", [])),
        "", "## Repository contradicted an earlier claim", bullet(state.get("disagreement", [])),
        "", "## Stop boundary (do not start)", bullet(state.get("stop_boundary", [])),
        "", "## Next action", state.get("next", "(unset)"),
        "", "## Latest evidence", "| id | label | result | command |", "| --- | --- | --- | --- |"] + (rows or ["| - | - | - | - |"]) + [
        "", "Rendered from `.ilana/handoff.json`. Edit with `evidence.py handoff`, not by hand."]
    return "\n".join(text) + "\n"


def cmd_report(args):
    state = load(args.repo, HANDOFF, {})
    records = read_records(args.repo)
    latest = latest_by_label(records)
    failing = [r for r in latest.values() if r["exit"] != 0]
    print("# Validation report: %s" % state.get("milestone", "(unset)"))
    print("head %s on %s, %d dirty path(s)" % (git(args.repo, "rev-parse", "--short", "HEAD"),
                                               git(args.repo, "branch", "--show-current"),
                                               len([ln for ln in git(args.repo, "status", "--porcelain", "-uall").splitlines() if ln])))
    print("")
    for label, r in sorted(latest.items()):
        print("%-6s %-24s exit=%d at %s (%s)" % (r["id"], label, r["exit"], r["head"], r["cmd"][:60]))
    print("")
    print("Ilana updated: %s" % ("YES" if os.path.exists(path(args.repo, HANDOFF)) else "NO"))
    print("Failing checks: %s" % (", ".join(r["label"] for r in failing) or "none"))
    return 1 if failing or not latest else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("policy")
    p.add_argument("--repo", default=".")
    p.add_argument("--ceremony")
    p.add_argument("--stop", nargs="*")
    p.add_argument("--show", action="store_true")
    r = sub.add_parser("run")
    r.add_argument("--repo", default=".")
    r.add_argument("--label")
    r.add_argument("cmd", nargs=argparse.REMAINDER)
    c = sub.add_parser("commit-check")
    c.add_argument("--repo", default=".")
    c.add_argument("file", nargs="?")
    h = sub.add_parser("hook")
    h.add_argument("--repo", default=".")
    o = sub.add_parser("handoff")
    o.add_argument("--repo", default=".")
    o.add_argument("--set", action="append")
    o.add_argument("--add", action="append")
    o.add_argument("--show", action="store_true")
    t = sub.add_parser("report")
    t.add_argument("--repo", default=".")
    args = parser.parse_args(argv)
    return {"policy": cmd_policy, "run": cmd_run, "commit-check": cmd_commit_check, "hook": cmd_hook,
            "handoff": cmd_handoff, "report": cmd_report}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
