#!/usr/bin/env python3
"""Fail-closed consistency check and explicitly selected active-obligation replays.

This is research governance/custody, NOT a proof of the missing Weil inequality.
No checkpoint number is used for frontier selection.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "research" / "obligations.json"
ID_RE = re.compile(r"^[A-Z][A-Z0-9-]{2,64}$")
# One existing historical NF356–370 custody key predates the strict identifier
# grammar. Admit precisely this immutable custody key; do not silently rename
# its evidence references or weaken the general id rule.
LEGACY_EVIDENCE_IDS = {"NF356_370_HISTORICAL_CUSTODY"}
VALID_METHODS = {"SI", "SM", "RC", "LF", "INTEGRATION"}
VALID_STATUSES = {"open", "closed"}
VALID_ROLES = {"retained-prerequisite", "frontier-candidate", "verification"}
VALID_CADENCES = {"per-update", "on-demand"}
# Exact historical file names must remain executable. Preserve a
# restricted scripts/validation-path grammar, permitting case-sensitive
# SM52C/SM54 names, plus ONLY the two existing pre-prefix legacy pilots.
CHECK_PATH_PATTERN = re.compile(
    # EF15 activates a distinct original even validation family, never arbitrary scripts.
    r"scripts/validate_rpb108_(?:sm|si|rc|ef)[A-Za-z0-9_]*\.py"
)
LEGACY_CHECK_PATHS = {
    "scripts/sm36_original_odd_numerical_pilot.py",
    "scripts/sm38_leafwise_original_odd_fourier_audit.py",
    # Exact SHA-manifest verifier introduced by the immutable NF356–364
    # historical custody reconciliation: no generic local_replay commands.
    "scripts/local_replay/verify_provisional_manifest.py",
}


class GovernanceError(ValueError):
    pass


def fail(message: str) -> None:
    raise GovernanceError(message)


def verify(data: dict, root: Path = ROOT) -> tuple[dict, list[dict]]:
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        fail("unsupported or absent manifest schema_version")
    objective = data.get("objective")
    if not isinstance(objective, dict) or objective.get("id") != "RH":
        fail("expected an explicit RH objective")
    if objective.get("status") != "open":
        fail("do not mark RH complete by changing a metadata field")
    gov = data.get("governance")
    if not isinstance(gov, dict) or gov.get("no_automatic_promotion") is not True:
        fail("no_automatic_promotion must remain true")
    obligations = data.get("obligations")
    if not isinstance(obligations, list) or not obligations:
        fail("nonempty obligations list is required")
    ids: dict[str, dict] = {}
    priorities: set[int] = set()
    for obj in obligations:
        if not isinstance(obj, dict):
            fail("obligation must be an object")
        key = obj.get("id")
        if not isinstance(key, str) or not ID_RE.fullmatch(key) or key in ids:
            fail(f"invalid or duplicate obligation id: {key!r}")
        ids[key] = obj
        if obj.get("status") not in VALID_STATUSES:
            fail(f"{key}: invalid status")
        if not isinstance(obj.get("acceptance"), str) or not obj["acceptance"].strip():
            fail(f"{key}: missing mathematical acceptance")
        if not isinstance(obj.get("statement"), str) or not obj["statement"].strip():
            fail(f"{key}: missing theorem statement")
        if not isinstance(obj.get("next_action"), str) or not obj["next_action"].strip():
            fail(f"{key}: missing next action")
        if not isinstance(obj.get("depends_on"), list) or not isinstance(obj.get("evidence"), list):
            fail(f"{key}: missing dependency or evidence arrays")
        methods = obj.get("methods")
        if not isinstance(methods, list) or not methods or any(m not in VALID_METHODS for m in methods):
            fail(f"{key}: unrecognized methods")
        priority = obj.get("priority")
        if obj["status"] == "open":
            if type(priority) is not int or priority < 1 or priority in priorities:
                fail(f"{key}: open priorities must be distinct positive integers")
            priorities.add(priority)
        elif priority is not None or not obj["evidence"]:
            fail(f"{key}: closed obligation needs evidence and null priority")

    evidence = data.get("evidence")
    if not isinstance(evidence, dict):
        fail("missing evidence registry")
    for name, item in evidence.items():
        if not isinstance(name, str) or not (ID_RE.fullmatch(name) or name in LEGACY_EVIDENCE_IDS) or not isinstance(item, dict):
            fail(f"invalid evidence record: {name!r}")
        for prop in ("kind", "scope", "pr", "verification"):
            if not isinstance(item.get(prop), str) or not item[prop].strip():
                fail(f"{name}: missing {prop}")
        if not item["pr"].startswith("https://github.com/monocap-tech/weil-lab/pull/"):
            fail(f"{name}: untrusted PR location")
        path = item.get("repo_path")
        if path is not None:
            p = Path(path)
            if p.is_absolute() or ".." in p.parts or not (root / p).is_file():
                fail(f"{name}: missing/unsafe evidence path {path!r}")

    visiting: set[str] = set()
    done: set[str] = set()

    def walk(key: str) -> None:
        if key in visiting:
            fail(f"cycle in obligations at {key}")
        if key in done:
            return
        visiting.add(key)
        for dep in ids[key]["depends_on"]:
            if not isinstance(dep, str) or dep not in ids or dep == key:
                fail(f"{key}: unknown/self dependency {dep!r}")
            walk(dep)
        for ev in ids[key]["evidence"]:
            if ev not in evidence:
                fail(f"{key}: unknown evidence {ev!r}")
        visiting.remove(key)
        done.add(key)

    for key in ids:
        walk(key)

    active = data.get("active_obligation")
    if active not in ids or ids[active]["status"] != "open":
        fail("active_obligation must be an open declared obligation")
    if any(ids[d]["status"] != "closed" for d in ids[active]["depends_on"]):
        fail("active_obligation has unresolved mandatory dependencies")

    checks = data.get("active_checks")
    if not isinstance(checks, list) or not checks:
        fail("declare at least one active check")
    seen_checks = set()
    for check in checks:
        if not isinstance(check, dict):
            fail("check must be an object")
        cid = check.get("id")
        if not isinstance(cid, str) or not cid or cid in seen_checks:
            fail(f"duplicate/invalid check id {cid!r}")
        seen_checks.add(cid)
        if check.get("obligation_id") != active:
            fail(f"{cid}: cannot silently validate a different active obligation")
        if check.get("role") not in VALID_ROLES:
            fail(f"{cid}: role must disclose whether check is a prerequisite or a candidate")
        if not isinstance(check.get("interpretation"), str) or not check["interpretation"].strip():
            fail(f"{cid}: missing limited-scope interpretation")
        if check.get("cadence") not in VALID_CADENCES:
            fail(f"{cid}: missing/invalid replay cadence")
        argv = check.get("argv")
        if (not isinstance(argv, list) or len(argv) != 2 or argv[0] != "python3"
                or not isinstance(argv[1], str)
                or not (CHECK_PATH_PATTERN.fullmatch(argv[1]) or argv[1] in LEGACY_CHECK_PATHS)
                or not (root / argv[1]).is_file()):
            fail(f"{cid}: unsafe or missing validation command")
    if not any(c["cadence"] == "per-update" for c in checks):
        fail("at least one active replay must run per update")
    return ids[active], checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-active", action="store_true",
                        help="replay only the explicit checks declared for the active obligation")
    parser.add_argument("--deep", action="store_true",
                        help="also replay retained historical checks marked on-demand")
    args = parser.parse_args()
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        active, checks = verify(data)
        print(f"Obligation manifest PASS: {active['id']} ({active['status']}); "
              f"{len(checks)} declared active checks", flush=True)
        print("Mathematical acceptance remains OPEN: " + active["acceptance"], flush=True)
        if args.run_active:
            for check in checks:
                if check["cadence"] == "on-demand" and not args.deep:
                    print(f"Retained historical check {check['id']} not rerun by default; use --deep.", flush=True)
                    continue
                print(f"Replay {check['id']} [{check['role']}]: {check['interpretation']}",
                      flush=True)
                subprocess.run([sys.executable, check["argv"][1]],
                               cwd=ROOT, check=True)
        print("Governance check PASS; no whole-form / RH closure implied.", flush=True)
        return 0
    except (GovernanceError, OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Obligation governance FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
