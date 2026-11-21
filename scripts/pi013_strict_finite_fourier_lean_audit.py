#!/usr/bin/env python3
"""Fail-closed PI013 exact-module Lean binary and standard-axiom receipt.

The script is *not a compiler*. Call it only after the dedicated exact
lake build and direct lake env lean passes. It accepts just five PI013
Gamma-cast theorems and three PI013 finite-sum theorems.

No result here certifies Masullo's operator trace, IV011 Gamma transport,
diagonal contact compensation, global Weil positivity or RH.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path

EXPECTED = {
    "PI013GammaAtomCast": (
        "pi013GammaDamping_pos",
        "pi013GammaDamping_eq",
        "pi013RealGammaAtom",
        "pi013ComplexGammaAtom",
        "pi013FourierIntegralGammaAtom",
    ),
    "PI013FiniteFourierSum": (
        "pi013PhysicalGammaAtom_integrable",
        "pi013FiniteDampedFourier_zero",
        "pi013FiniteFourierIntegral",
    ),
}
IMPORTS = (
    "PI007FiniteGammaKernel",
    "PI008FiniteDigammaSymbol",
    "PI010FourierHalflineAtom",
    "PI011WholeLineFourierAtom",
    "PI012ComplexRationalIdentity",
    "PI012SourceFourierAtom",
)
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
RECORD = re.compile(
    r"(?m)^(?P<name>WeilDefect\.[A-Za-z_][A-Za-z_0-9']*) "
    r"(?:(?P<none>does not depend on any axioms)"
    r"|depends on axioms:\s*\[(?P<axioms>[^\]]*)\])\s*$"
)
FORBIDDEN = re.compile(r"(?m)^\s*(?:axiom|sorry|admit|opaque)\b")


def blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def source_path(name: str) -> Path:
    return Path("WeilDefect/Arithmetic") / (name + ".lean")


def olean_path(name: str) -> Path:
    return Path(".lake/build/lib/lean/WeilDefect/Arithmetic") / (name + ".olean")


def check_object(name: str) -> dict:
    src, obj = source_path(name), olean_path(name)
    if not src.is_file() or not obj.is_file() or obj.stat().st_size == 0:
        raise RuntimeError(f"Missing actual Lean source or compiled object: {name}")
    raw = src.read_bytes()
    if FORBIDDEN.search(raw.decode("utf-8")):
        raise RuntimeError(f"Unfinished project axiom/proof in {src}")
    return {
        "source": str(src),
        "source_git_blob": blob(raw),
        "olean": str(obj),
        "olean_sha256": hashlib.sha256(obj.read_bytes()).hexdigest(),
        "olean_size_bytes": obj.stat().st_size,
    }


def check_axioms(module: str, expected: tuple[str, ...], log_path: Path) -> dict:
    if not log_path.is_file() or log_path.stat().st_size == 0:
        raise RuntimeError(f"Missing direct Lean #print axioms log: {log_path}")
    output = log_path.read_text(encoding="utf-8")
    if re.search(r"(?mi)(?:^error:|:\d+:\d+: error:)", output):
        raise RuntimeError(f"Actual Lean compiler error: {log_path}")
    found = {}
    for m in RECORD.finditer(output):
        name = m.group("name")
        if name in found:
            raise RuntimeError(f"Repeated axiom record {name}")
        raw = m.group("axioms")
        axioms = [] if raw is None or not raw.strip() else [
            x.strip() for x in raw.split(",")
        ]
        if set(axioms) - ALLOWED:
            raise RuntimeError(f"{name} has nonstandard axioms: {axioms}")
        found[name] = axioms
    required = {f"WeilDefect.{v}" for v in expected}
    if set(found) != required:
        raise RuntimeError(
            f"{module}: missing {sorted(required-set(found))}; "
            f"extra {sorted(set(found)-required)}"
        )
    return {"log": str(log_path), "theorems": found}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--logs", type=Path, default=Path("pi013-audit"))
    parser.add_argument("--receipt", type=Path, default=Path("pi013-audit/receipt.json"))
    args = parser.parse_args()

    if "leanprover/lean4:v4.34.0" not in Path("lean-toolchain").read_text():
        raise RuntimeError("Lean toolchain drift; required v4.34.0")
    lake = Path("lakefile.toml").read_text()
    if 'rev = "v4.34.0"' not in lake or "mathlib4.git" not in lake:
        raise RuntimeError("Mathlib v4.34.0 source pin drift")

    modules = {}
    for name in (*IMPORTS, *EXPECTED):
        modules[name] = check_object(name)

    for name, decls in EXPECTED.items():
        modules[name]["axioms"] = check_axioms(
            name, decls, args.logs / (name + "-axioms.log")
        )

    report = {
        "status": "PASS_PI013_EIGHT_DIRECT_LEAN_DECLARATIONS_ONLY",
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "checked_out_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "allowed_axioms": sorted(ALLOWED),
        "mathlib": "v4.34.0",
        "modules": modules,
        "NOT_certified": [
            "pi013 finite integrand equals literal Zeta23.paperFT of PI007 kernel in Lean",
            "inverse Fourier transform with factor 1/(2*pi)",
            "PI007/PI008 infinite gamma limit in Lean",
            "literal IV011 signed original Gamma distribution transport",
            "Masullo operator trace and h(0)!=0 diagonal contact law",
            "global Weil positivity, RH or GRH",
        ],
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("PI013 actual source and eight-theorem Lean axiom audit: PASS")


if __name__ == "__main__":
    main()
