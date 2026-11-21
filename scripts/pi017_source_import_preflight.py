#!/usr/bin/env python3
"""PI017 static (NON-COMPILER) provenance and import-path preflight.

Operates on a real git checkout of the immutable upstream project and the
actual resolved Mathlib v4.34.0 source tree of the Weil-Lab Lake graph.
Verifies all *direct* Mathlib import paths of the byte-exact original
Zeta23.Defs.lean exist. This is ONLY an import-path compatibility test:
no Lean elaboration, theorem lookup, common olean or Gamma identity follows.

Usage: python3 scripts/pi017_source_import_preflight.py \
  --upstream pi017-upstream --mathlib .lake/packages/mathlib
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import subprocess

UPSTREAM_COMMIT = "16a5ce41304fcdaea4e0be7c132e1c361dc26da5"
UPSTREAM_DEFS_BLOB = "8024700cbfefb54d763b487afa84c03fef58a550"
LOCAL_MATHLIB_COMMIT = "5ed2965256430c3649e86755f9576b54eca72435"
SOURCE_FORMULA = (
    "def paperFT (f : ℝ → ℂ) (z : ℂ) : ℂ := "
    "∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))"
)
EXPECTED_DIRECT_IMPORTS = {
    "Mathlib.Analysis.CStarAlgebra.Classes",
    "Mathlib.Analysis.SpecialFunctions.Gamma.Digamma",
    "Mathlib.Analysis.SpecialFunctions.Pow.Complex",
    "Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt",
    "Mathlib.MeasureTheory.Integral.Bochner.Basic",
    "Mathlib.MeasureTheory.Measure.Lebesgue.Basic",
    "Mathlib.Algebra.BigOperators.Finprod",
    "Mathlib.Data.Set.Card",
    "Mathlib.Data.Matrix.Basic",
}


def rev(path: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(path), "rev-parse", "HEAD"], text=True
    ).strip()


def blob(data: bytes) -> str:
    return hashlib.sha1(
        b"blob " + str(len(data)).encode() + b"\0" + data
    ).hexdigest()


def check(upstream: Path, mathlib: Path) -> list[str]:
    if rev(upstream) != UPSTREAM_COMMIT:
        raise RuntimeError("Upstream root repo did not match frozen commit")
    if rev(mathlib) != LOCAL_MATHLIB_COMMIT:
        raise RuntimeError("Resolved local Mathlib did not match v4.34.0 commit")
    defs_path = upstream / "zeta23/Zeta23/Defs.lean"
    raw = defs_path.read_bytes()
    if blob(raw) != UPSTREAM_DEFS_BLOB:
        raise RuntimeError("Original upstream Zeta23.Defs source Git blob differs")
    source = raw.decode("utf-8")
    if SOURCE_FORMULA not in source:
        raise RuntimeError("Upstream paperFT literal positive exponent changed")
    imports = set(re.findall(r"(?m)^import\s+(Mathlib\.[A-Za-z0-9_.]+)\s*$", source))
    if imports != EXPECTED_DIRECT_IMPORTS:
        raise RuntimeError(
            f"Upstream direct imports changed: "
            f"missing={sorted(EXPECTED_DIRECT_IMPORTS-imports)}, "
            f"new={sorted(imports-EXPECTED_DIRECT_IMPORTS)}"
        )
    missing = []
    for name in sorted(imports):
        source_path = mathlib / (name.replace(".", "/") + ".lean")
        if not source_path.is_file():
            missing.append(name)
    if missing:
        raise RuntimeError(
            f"Upstream direct Mathlib imports absent in v4.34.0: {missing}"
        )
    return sorted(imports)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--upstream", type=Path, required=True)
    p.add_argument("--mathlib", type=Path, required=True)
    a = p.parse_args()
    imports = check(a.upstream, a.mathlib)
    print("PI017 EXACT SOURCE DIRECT-IMPORT-PATH PREFLIGHT: PASS")
    print(f"Verified all {len(imports)} unchanged upstream Mathlib direct imports")
    for item in imports:
        print(f"  {item}")
    print("NOT checked: Lean theorem names, imports elaborating, actual .olean, axioms")
    print("NOT checked: PI008 Fourier atom, finite inverse pairing, Masullo or RH")


if __name__ == "__main__":
    main()
