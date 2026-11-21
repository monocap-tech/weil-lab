#!/usr/bin/env python3
"""UOI planning-only validator; not a GitHub Actions dispatcher or proof auditor.

Usage:
    python scripts/uoi_validate.py research/unified/obligations.json --plan
    python scripts/uoi_validate.py research/unified/obligations.json --plan --json

This program is deterministic and read-only: no network, shell commands, writes,
workflow dispatch, GitHub mutation, status promotion, or RH inference.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

VALID_STANDING = {"open", "conditional", "blocked", "accepted", "retired"}
VALID_RUN = {"read_only", "local", "heavy_manual"}
TRACKS = {"UOI", "CI", "NF", "IV", "CF", "GA", "CP", "PI", "RD"}
ID = re.compile(r"^[A-Z][A-Z0-9-]{2,63}$")
REQUIRED = {
    "id", "lead", "contributors", "kind", "standing", "depends_on",
    "priority", "run_class", "statement", "acceptance", "sources",
    "evidence", "closure_receipt",
}
SRC_PREFIX = "https://github.com/monocap-tech/weil-lab/"


class ManifestError(ValueError):
    """Fail closed on malformed or unsafe research governance."""


def validate(data: dict) -> dict[str, dict]:
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ManifestError("unsupported coordination schema_version")
    auth = data.get("authority")
    if not isinstance(auth, dict):
        raise ManifestError("missing authority")
    if auth.get("execution_policy") != "consolidation_hold":
        raise ManifestError("the consolidation hold may not be lifted by this validator")
    if (auth.get("automatic_dispatch") is not False
            or auth.get("automatic_mathematical_promotion") is not False):
        raise ManifestError("automatic dispatch and theorem promotion are forbidden")
    if (auth.get("historical_source_preservation") is not True
            or auth.get("maximum_concurrent_heavy_jobs") != 1):
        raise ManifestError("historical evidence preservation / heavy lease invalid")
    if auth.get("objective") != "Riemann hypothesis: open":
        raise ManifestError("RH cannot be declared closed in the coordination layer")
    if "W-ODD-NEG" not in str(auth.get("historical_manifest", "")):
        raise ManifestError("the original independent W-ODD-NEG manifest must be preserved")
    if set(data.get("tracks", [])) != TRACKS:
        raise ManifestError("missing or unknown function identifiers")

    obs = data.get("obligations")
    if not isinstance(obs, list) or not obs:
        raise ManifestError("nonempty obligations list required")
    nodes = {}
    priorities = set()
    for o in obs:
        if not isinstance(o, dict) or REQUIRED - set(o):
            raise ManifestError("malformed obligation / missing fields")
        key = o["id"]
        if not isinstance(key, str) or not ID.fullmatch(key) or key in nodes:
            raise ManifestError("bad/duplicate obligation id: " + repr(key))
        nodes[key] = o
        if (o["lead"] not in TRACKS
                or not isinstance(o["contributors"], list)
                or any(t not in TRACKS for t in o["contributors"])):
            raise ManifestError(key + ": unknown lead/contributors")
        if o["standing"] not in VALID_STANDING or o["run_class"] not in VALID_RUN:
            raise ManifestError(key + ": unknown standing / execution classification")
        priority = o["priority"]
        if type(priority) is not int or priority <= 0 or priority in priorities:
            raise ManifestError(key + ": duplicate/invalid priority")
        priorities.add(priority)
        if not isinstance(o["depends_on"], list) or not all(
                isinstance(dep, str) for dep in o["depends_on"]):
            raise ManifestError(key + ": invalid dependency list")
        if not isinstance(o["sources"], list) or not o["sources"] or not all(
                isinstance(s, str) and s.startswith(SRC_PREFIX) for s in o["sources"]):
            raise ManifestError(key + ": missing canonical source URLs")
        if not isinstance(o["evidence"], list):
            raise ManifestError(key + ": invalid evidence")
        if any(not isinstance(o[field], str) or not o[field].strip()
               for field in ("statement", "acceptance", "kind")):
            raise ManifestError(key + ": statement/scope/kind missing")
        for ev in o["evidence"]:
            if (not isinstance(ev, dict)
                    or not isinstance(ev.get("kind"), str)
                    or not isinstance(ev.get("reference"), str)
                    or ev.get("accepts_obligation") is not False):
                raise ManifestError(key + ": evidence cannot automatically promote theorem")
        receipt = o["closure_receipt"]
        if o["standing"] == "accepted":
            fields = ("source_sha", "artifact_sha256", "independent_audit", "scope_validation")
            if not isinstance(receipt, dict) or any(
                    not isinstance(receipt.get(f), str) or not receipt[f].strip()
                    for f in fields):
                raise ManifestError(key + ": accepted requires independent full scope receipt")
        elif receipt is not None:
            raise ManifestError(key + ": unaccepted obligation has a forged receipt")

    visiting, visited = set(), set()

    def visit(key):
        if key in visiting:
            raise ManifestError("dependency cycle at " + key)
        if key in visited:
            return
        visiting.add(key)
        deps = nodes[key]["depends_on"]
        if key in deps or len(set(deps)) != len(deps):
            raise ManifestError(key + ": self / duplicate dependencies")
        for d in deps:
            if d not in nodes:
                raise ManifestError(key + ": unknown dependency " + d)
            visit(d)
        visiting.remove(key)
        visited.add(key)

    for key in nodes:
        visit(key)

    cursor = auth.get("operational_cursor")
    if cursor not in nodes or nodes[cursor]["standing"] != "open":
        raise ManifestError("cursor must refer to an open declared obligation")
    routes = data.get("terminal_routes")
    if not isinstance(routes, list) or len(routes) < 2:
        raise ManifestError("independent terminal routes must be explicit")
    names = set()
    for route in routes:
        if not isinstance(route, dict):
            raise ManifestError("bad terminal route")
        name = route.get("name")
        if not isinstance(name, str) or name in names:
            raise ManifestError("missing or duplicate route name")
        names.add(name)
        all_of = route.get("all_of")
        if not isinstance(all_of, list) or not all_of or any(
                not isinstance(x, str) or x not in nodes for x in all_of):
            raise ManifestError("route has nonexistent or empty obligations")
    if not {"original-signed-Weil", "independent-arithmetic"} <= names:
        raise ManifestError("missing mathematical OR-route")
    return nodes


def plan(data: dict, nodes: dict[str, dict]) -> dict:
    ready, blocked = [], []
    for node in sorted(nodes.values(), key=lambda n: n["priority"]):
        if node["standing"] in {"accepted", "retired"}:
            continue
        unpaid = [dep for dep in node["depends_on"]
                  if nodes[dep]["standing"] != "accepted"]
        entry = {"id": node["id"], "lead": node["lead"],
                 "run_class": node["run_class"]}
        if unpaid or node["standing"] == "blocked":
            blocked.append({**entry, "unpaid": unpaid})
        else:
            ready.append(entry)
    return {
        "execution_policy": data["authority"]["execution_policy"],
        "current_cursor": data["authority"]["operational_cursor"],
        "dispatch_authorized": False,
        "mathematical_promotion_authorized": False,
        "ready_for_review_only": ready,
        "blocked_by_unpaid_prerequisites": blocked,
        "terminal_route_satisfied": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--plan", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
        nodes = validate(data)
        output = plan(data, nodes) if args.plan else {
            "manifest_valid": True, "node_count": len(nodes),
            "dispatch_authorized": False,
        }
        if args.json:
            print(json.dumps(output, indent=2))
        elif args.plan:
            print("UOI PLAN ONLY — NO DISPATCH; "
                  f"{len(output['ready_for_review_only'])} review-ready, "
                  f"{len(output['blocked_by_unpaid_prerequisites'])} blocked.")
            for row in output["ready_for_review_only"]:
                print("  REVIEW ONLY:", row["id"], "[" + row["lead"] + "]")
            for row in output["blocked_by_unpaid_prerequisites"]:
                print("  BLOCKED:", row["id"], "unpaid:", ", ".join(row["unpaid"]))
        else:
            print(f"UOI manifest PASS ({len(nodes)} nodes); no proof or CI authorization.")
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print("UOI validation FAIL: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
