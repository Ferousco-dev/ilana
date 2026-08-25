#!/usr/bin/env python3
"""Ilana ledger tool.

Creates, reads, appends to and validates the .ilana/ directory.
No third-party dependencies. Python 3.8+.

Usage:
    python3 ledger.py init    --project NAME [--rigour 3] [--mode FLEET]
    python3 ledger.py status
    python3 ledger.py append  --agent analyst --event "G1 PASS" --evidence "docs/srs.md"
    python3 ledger.py gate    --gate G1 --verdict PASS --owner analyst
    python3 ledger.py next-id --prefix REQ
    python3 ledger.py validate
"""

import argparse
import json
import os
import sys
from datetime import datetime

LEDGER = ".ilana"
STATE = "state.json"
LOG = "ledger.md"

FILES = {
    "ledger.md": "# Ilana Ledger\n\nAppend only. Newest at the bottom. Corrections supersede,\nthey never overwrite.\n",
    "requirements.md": "# Requirements Register\n\n| ID | Type | Priority | Statement | Source | Status |\n| --- | --- | --- | --- | --- | --- |\n",
    "decisions.md": "# Decision Records\n\n| ID | Date | Decision | Reason | Supersedes |\n| --- | --- | --- | --- | --- |\n",
    "defects.md": "# Defect Log\n\n| ID | Title | Severity | Priority | Status | Regression test |\n| --- | --- | --- | --- | --- | --- |\n",
    "changes.md": "# Change Requests\n\n| ID | Title | Type | Impact analysed | Disposition | Decided by |\n| --- | --- | --- | --- | --- | --- |\n",
    "risks.md": "# Risk Register\n\n| ID | Risk | Likelihood | Impact | Mitigation | Owner | Status |\n| --- | --- | --- | --- | --- | --- | --- |\n",
    "ethics.md": "# Ethics Register\n\n| ID | Finding | Severity | Principle | Disposition | Date |\n| --- | --- | --- | --- | --- | --- |\n",
    "traceability.csv": "req_id,requirement,type,priority,source,design_id,module,test_ids,result,status\n",
    "metrics.csv": "date,metric,category,value,unit,source\n",
}

PREFIXES = ["REQ", "NFR", "DOM", "DES", "UI", "TC", "DEF", "CR", "RSK", "DEC", "MET", "ETH"]


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def today():
    return datetime.now().strftime("%Y-%m-%d")


def path(root, *parts):
    return os.path.join(root, LEDGER, *parts)


def load_state(root):
    p = path(root, STATE)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as handle:
        return json.load(handle)


def save_state(root, state):
    with open(path(root, STATE), "w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2)
        handle.write("\n")


def cmd_init(root, args):
    if os.path.exists(path(root, STATE)):
        print("ledger already exists at " + path(root))
        print("use `status` to see where the run is")
        return 1
    os.makedirs(path(root, "gates"), exist_ok=True)
    for name, content in FILES.items():
        target = path(root, name)
        if not os.path.exists(target):
            with open(target, "w", encoding="utf-8") as handle:
                handle.write(content)
    state = {
        "ilana_version": "1.0.0",
        "project": args.project,
        "mode": args.mode,
        "phase": None,
        "gate": "G0",
        "agent": "conductor",
        "process_style": args.style,
        "rigour": args.rigour,
        "open": [],
        "overrides": [],
        "counters": {p: 0 for p in PREFIXES},
        "attempts": {},
        "created": today(),
    }
    save_state(root, state)
    append(root, "conductor", "LEDGER INITIALISED",
           ["project: " + args.project,
            "mode: " + args.mode,
            "rigour: " + str(args.rigour),
            "process style: " + args.style])
    print("initialised " + path(root))
    print("commit this directory. process history is project history.")
    return 0


def append(root, agent, event, evidence=None):
    lines = ["", "## " + now() + " | " + agent + " | " + event]
    if evidence:
        lines.append("Evidence:")
        for item in evidence:
            lines.append("  - " + item)
    with open(path(root, LOG), "a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def cmd_append(root, args):
    state = load_state(root)
    if state is None:
        print("no ledger. run `init` first.")
        return 1
    append(root, args.agent, args.event, args.evidence)
    print("appended")
    return 0


def cmd_status(root, args):
    state = load_state(root)
    if state is None:
        print("no ledger at " + path(root))
        print("cold start: run `init`")
        return 1
    print("ILANA  " + state["project"])
    print("  mode:    " + str(state["mode"]))
    print("  phase:   " + str(state["phase"]))
    print("  gate:    " + str(state["gate"]))
    print("  agent:   " + str(state["agent"]))
    print("  rigour:  " + str(state["rigour"]) + " of 5")
    print("  style:   " + str(state["process_style"]))
    if state["open"]:
        print("  open:    " + ", ".join(state["open"]))
    else:
        print("  open:    none")
    if state["overrides"]:
        print("  overrides:")
        for o in state["overrides"]:
            print("    " + o.get("gate", "?") + ": " + o.get("reason", ""))
    counters = {k: v for k, v in state["counters"].items() if v}
    if counters:
        print("  ids:     " + ", ".join(k + "=" + str(v) for k, v in sorted(counters.items())))
    attempts = {k: v for k, v in state.get("attempts", {}).items() if v}
    if attempts:
        print("  attempts: " + ", ".join(k + "=" + str(v) for k, v in sorted(attempts.items())))
    return 0


def cmd_next_id(root, args):
    state = load_state(root)
    if state is None:
        print("no ledger. run `init` first.")
        return 1
    prefix = args.prefix.upper()
    if prefix not in PREFIXES:
        print("unknown prefix " + prefix + ". known: " + ", ".join(PREFIXES))
        return 1
    state["counters"][prefix] = state["counters"].get(prefix, 0) + 1
    save_state(root, state)
    print("%s-%03d" % (prefix, state["counters"][prefix]))
    return 0


def cmd_gate(root, args):
    state = load_state(root)
    if state is None:
        print("no ledger. run `init` first.")
        return 1
    gate = args.gate.upper()
    verdict = args.verdict.upper()
    attempts = state.setdefault("attempts", {})
    attempts[gate] = attempts.get(gate, 0) + 1

    record = path(root, "gates", gate + ".md")
    with open(record, "a", encoding="utf-8") as handle:
        handle.write("\n# %s attempt %d\n" % (gate, attempts[gate]))
        handle.write("Date: %s\nOwner: %s\nRigour: %s\nVerdict: %s\n" % (
            today(), args.owner, state["rigour"], verdict))
        if args.evidence:
            handle.write("\n## Evidence\n")
            for item in args.evidence:
                handle.write("  - " + item + "\n")
        if args.reason:
            handle.write("\n## Reason\n" + args.reason + "\n")

    if verdict == "PASS":
        state["gate"] = gate
        attempts[gate] = 0
    elif verdict == "OVERRIDE":
        state["gate"] = gate
        state["overrides"].append({
            "gate": gate, "reason": args.reason or "(none given)", "at": today()})
        attempts[gate] = 0
    save_state(root, state)
    append(root, args.owner, gate + " " + verdict, args.evidence)

    if verdict == "FAIL" and attempts[gate] >= 2:
        print("WARNING: %s has failed %d times. Escalate; do not remediate again." % (
            gate, attempts[gate]))
        print("see protocols/escalation.md")
    print("recorded " + gate + " " + verdict + " in " + record)
    return 0


def cmd_validate(root, args):
    problems = []
    state = load_state(root)
    if state is None:
        print("no ledger")
        return 2
    for name in FILES:
        if not os.path.exists(path(root, name)):
            problems.append("missing " + name)
    if not os.path.isdir(path(root, "gates")):
        problems.append("missing gates/ directory")
    if state.get("rigour") not in (1, 2, 3, 4, 5):
        problems.append("rigour must be 1..5, found " + repr(state.get("rigour")))
    if state.get("rigour") == 5 and state.get("overrides"):
        problems.append("rigour 5 permits no overrides, but overrides are recorded")
    log = path(root, LOG)
    if os.path.exists(log) and os.path.getsize(log) < 40:
        problems.append("ledger.md is effectively empty; nothing has been recorded")
    if problems:
        print("LEDGER PROBLEMS")
        for p in problems:
            print("  - " + p)
        return 1
    print("ledger valid")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Ilana ledger tool")
    parser.add_argument("--root", default=".", help="project root")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init")
    p_init.add_argument("--project", required=True)
    p_init.add_argument("--rigour", type=int, default=3, choices=[1, 2, 3, 4, 5])
    p_init.add_argument("--mode", default="FLEET")
    p_init.add_argument("--style", default="hybrid",
                        choices=["agile", "plan-driven", "hybrid", "devops"])

    sub.add_parser("status")
    sub.add_parser("validate")

    p_append = sub.add_parser("append")
    p_append.add_argument("--agent", required=True)
    p_append.add_argument("--event", required=True)
    p_append.add_argument("--evidence", nargs="*")

    p_gate = sub.add_parser("gate")
    p_gate.add_argument("--gate", required=True)
    p_gate.add_argument("--verdict", required=True,
                        choices=["PASS", "FAIL", "OVERRIDE", "pass", "fail", "override"])
    p_gate.add_argument("--owner", required=True)
    p_gate.add_argument("--evidence", nargs="*")
    p_gate.add_argument("--reason", default=None)

    p_next = sub.add_parser("next-id")
    p_next.add_argument("--prefix", required=True)

    args = parser.parse_args()
    handlers = {
        "init": cmd_init, "status": cmd_status, "append": cmd_append,
        "gate": cmd_gate, "next-id": cmd_next_id, "validate": cmd_validate,
    }
    return handlers[args.cmd](args.root, args)


if __name__ == "__main__":
    sys.exit(main())
