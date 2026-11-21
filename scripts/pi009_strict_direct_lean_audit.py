#!/usr/bin/env python3
"""PI009 fail-closed audit of actual Lean module builds and #print axioms.

Run ONLY after both direct lake builds and independent "lake env lean" source
checks succeeded. This script does not compile Lean and does not certify
Fourier inversion or the original IV011 Gamma bridge.

Accepted proof axioms: propext, Classical.choice, Quot.sound only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "PI007FiniteGammaKernel": [
        "pi007FiniteGammaKernel_zero",
        "pi007FiniteGammaKernel_succ",
        "pi007FiniteGammaKernel_nonneg",
        "pi007FiniteGammaKernel_even",
        "pi007FiniteGammaKernel_le_succ",
    ],
    "PI008FiniteDigammaSymbol": [
        "pi008GammaRationalAtom_nonneg",
        "pi008GammaRationalAtom_even",
        "pi008FiniteDigammaSymbol_zero",
        "pi008FiniteDigammaSymbol_succ",
        "pi008FiniteDigammaSymbol_even",
    ],
}
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
LINE = re.compile(
    r"(?m)^(?P<decl>WeilDefect\.[A-Za-z_][A-Za-z_0-9']*) "
    r"(?:(?P<none>does not depend on any axioms)"
    r"|depends on axioms:\s*\[(?P<axioms>[^\]]*)\])\s*$"
)
UNFINISHED = re.compile(r"(?m)^\s*(?:axiom|sorry|admit|opaque)\b")


def git_rev() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], text=True
    ).strip()


def git_blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(
        b"blob " + str(len(data)).encode() + b"\x00" + data
    ).hexdigest()


def audit_one(modname: str, names: list[str], logdir: Path) -> dict:
    src = Path("WeilDefect/Arithmetic") / f"{modname}.lean"
    olean = Path(".lake/build/lib/lean/WeilDefect/Arithmetic") / f"{modname}.olean"
    logfile = logdir / f"{modname}-axioms.log"
    if not src.is_file() or not olean.is_file() or olean.stat().st_size == 0:
        raise RuntimeError(f"Missing source or compiled .olean for {modname}")
    if not logfile.is_file() or logfile.stat().st_size == 0:
        raise RuntimeError(f"Missing direct Lean axiom log for {modname}")
    source = src.read_text()
    if UNFINISHED.search(source):
        raise RuntimeError(f"Untrusted/unfinished declaration in {src}")
    log = logfile.read_text()
    if re.search(r"(?mi)^\s*(?:error:|.*:\d+:\d+: error:)", log):
        raise RuntimeError(f"Compiler error in {logfile}")

    entries: dict[str, list[str]] = {}
    for match in LINE.finditer(log):
        decl = match.group("decl")
        if decl in entries:
            raise RuntimeError(f"Duplicate axiom record: {decl}")
        raw = match.group("axioms")
        axioms = [] if raw is None or not raw.strip() else [
            s.strip() for s in raw.split(",")
        ]
        unexpected = set(axioms) - ALLOWED_AXIOMS
        if unexpected:
            raise RuntimeError(f"{decl}: nonstandard axioms {sorted(unexpected)}")
        entries[decl] = axioms

    required = {f"WeilDefect.{name}" for name in names}
    if set(entries) != required:
        raise RuntimeError(
            f"{modname}: missing/unexpected axiom records; "
            f"missing={sorted(required-set(entries))} "
            f"unexpected={sorted(set(entries)-required)}"
        )
    # Direct source compilation and generated object are the evidence;
    # a text log alone is never a kernel acceptance receipt.
    return {
        "source": str(src),
        "source_git_blob_sha": git_blob(src),
        "olean": str(olean),
        "olean_size_bytes": olean.stat().st_size,
        "olean_sha256": hashlib.sha256(olean.read_bytes()).hexdigest(),
        "direct_lean_log": str(logfile),
        "theorems": entries,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--logs", type=Path, default=Path("pi009-audit"))
    p.add_argument("--out", type=Path, default=Path("pi009-audit/receipt.json"))
    args = p.parse_args()

    # Fail closed on mismatched dependency pin.
    lakefile = Path("lakefile.toml").read_text()
    if 'rev = "v4.34.0"' not in lakefile:
        raise RuntimeError("Unexpected mathlib version; expected v4.34.0")
    if "mathlib4.git" not in lakefile:
        raise RuntimeError("Pinned mathlib source absent")

    report = {
        "status": "PASS_DIRECT_LEAN_MODULE_AND_AXIOM_AUDIT_ONLY",
        "commit_sha": git_rev(),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "mathlib_pin": "v4.34.0",
        "allowed_axioms": sorted(ALLOWED_AXIOMS),
        "modules": {},
        "not_certified": [
            "original IV011 source-bound archimedean inverse transform",
            "finite Fourier atom identity and analytic limit in Lean",
            "Masullo trace operator theorem and diagonal contact extension",
            "global Weil positivity, RH or GRH",
        ],
    }
    for modname, names in EXPECTED.items():
        report["modules"][modname] = audit_one(modname, names, args.logs)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("PI009 strict direct Lean module audit: PASS")
    print(f"Exact source commit: {report['commit_sha']}")
    print(f"Receipt: {args.out}")
    print("No source-bound Gamma/Weil transport theorem asserted.")


if __name__ == "__main__":
    main()
