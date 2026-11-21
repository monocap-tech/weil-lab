#!/usr/bin/env python3
"""PI011 direct compiler, source and standard-axiom audit. Fail closed.

Must run after successful exact-source lake build and direct lake env lean.
Accepts only actual compiled PI011 and the five named #print axioms records.
Does not certify Masullo, IV011, RH, or an unproved rational simplification.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

NAME = "PI011WholeLineFourierAtom"
DECLS = {
    "WeilDefect.pi011Piecewise_integrableOn_Iic",
    "WeilDefect.pi011Piecewise_integrableOn_Ioi",
    "WeilDefect.pi011Piecewise_whole_integral",
    "WeilDefect.pi011Physical_eq_piecewise",
    "WeilDefect.pi011Physical_whole_integral",
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
AXIOM_LINE = re.compile(
    r"(?m)^(?P<decl>WeilDefect\.[A-Za-z_][A-Za-z_0-9']*) "
    r"(?:(?P<none>does not depend on any axioms)"
    r"|depends on axioms:\s*\[(?P<axioms>[^\]]*)\])\s*$"
)
UNSAFE = re.compile(r"(?m)^\s*(?:sorry|admit|axiom|opaque)\b")


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(
        b"blob " + str(len(raw)).encode() + b"\0" + raw
    ).hexdigest()


def verify(log_file: Path, out: Path) -> None:
    source = Path(f"WeilDefect/Arithmetic/{NAME}.lean")
    module_pi10 = Path("WeilDefect/Arithmetic/PI010FourierHalflineAtom.lean")
    obj = Path(f".lake/build/lib/lean/WeilDefect/Arithmetic/{NAME}.olean")
    pi10_obj = Path(".lake/build/lib/lean/WeilDefect/Arithmetic/PI010FourierHalflineAtom.olean")
    if any(not p.is_file() or p.stat().st_size == 0
           for p in (source, module_pi10, obj, pi10_obj, log_file)):
        raise RuntimeError("Required PI010/PI011 source, compiler object or axiom log absent")
    if "leanprover/lean4:v4.34.0" not in Path("lean-toolchain").read_text():
        raise RuntimeError("Unexpected Lean compiler pin")
    if 'rev = "v4.34.0"' not in Path("lakefile.toml").read_text():
        raise RuntimeError("Unexpected Mathlib source pin")
    src = source.read_text()
    if UNSAFE.search(src):
        raise RuntimeError("Unproved/untrusted declaration in PI011 source")
    if "import WeilDefect.Arithmetic.PI010FourierHalflineAtom" not in src:
        raise RuntimeError("The genuine PI010 source dependency was not imported")
    if "integral_Iic_add_Ioi" not in src:
        raise RuntimeError("No genuine whole-line integration split located")

    log = log_file.read_text()
    if re.search(r"(?mi)(?:^error:|:\d+:\d+: error:)", log):
        raise RuntimeError("PI011 direct Lean error in axiom log")
    found = {}
    for match in AXIOM_LINE.finditer(log):
        decl = match.group("decl")
        if decl in found:
            raise RuntimeError("Duplicate theorem receipt: " + decl)
        raw = match.group("axioms")
        axioms = [] if not raw or not raw.strip() else [a.strip() for a in raw.split(",")]
        if set(axioms) - ALLOWED:
            raise RuntimeError(f"Nonstandard axiom(s) in {decl}: {axioms}")
        found[decl] = axioms
    if set(found) != DECLS:
        raise RuntimeError(
            f"Theorem receipt mismatch; missing {sorted(DECLS - set(found))}, "
            f"extra {sorted(set(found) - DECLS)}"
        )

    commit_sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], text=True
    ).strip()
    receipt = {
        "status": "PASS_PI011_FIVE_WHOLE_LINE_CANDIDATES_ONLY",
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "checked_out_commit": commit_sha,
        "source_git_blob_sha": git_blob(source.read_bytes()),
        "pi010_dependency_git_blob_sha": git_blob(module_pi10.read_bytes()),
        "pi011_olean_sha256": hashlib.sha256(obj.read_bytes()).hexdigest(),
        "pi010_olean_sha256": hashlib.sha256(pi10_obj.read_bytes()).hexdigest(),
        "pi011_olean_size": obj.stat().st_size,
        "pi010_olean_size": pi10_obj.stat().st_size,
        "axiom_records": found,
        "accepted_axioms": sorted(ALLOWED),
        "NOT_certified": [
            "closed rational Fourier transform 2alpha/(alpha^2+r^2) in Lean",
            "finite source Fourier inversion against Gamma rational atoms",
            "literal IV011 signed Gamma transport and diagonal terms",
            "Masullo operator trace, positivity, RH or GRH",
        ],
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
    print("PI011 strict direct whole-line Lean audit: PASS (five lemmas only)")


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--log", type=Path, default=Path("pi011-audit/PI011WholeLineFourierAtom-axioms.log"))
    p.add_argument("--out", type=Path, default=Path("pi011-audit/receipt.json"))
    args = p.parse_args()
    verify(args.log, args.out)
