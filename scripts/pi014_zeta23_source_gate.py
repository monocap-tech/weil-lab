#!/usr/bin/env python3
"""PI014 fail-closed source syntax and dependency gate for Zeta23.paperFT.

Source checking is OPTIONAL and is never silently advertised as run.
Use:
  python scripts/pi014_zeta23_source_gate.py --defs <Zeta23/Defs.lean> \
      --upstream-lake <zeta23/lakefile.toml>
  python scripts/pi014_zeta23_source_gate.py --defs ... --upstream-lake ... \
      --require-matched-mathlib

Only input bytes with the expected Git blob hashes are accepted. A matched
Zeta23 mathlib dependency is REQUIRED before claiming the source imported.
No claim of actual Lean compilation, operator trace or global RH.
"""
import argparse
import hashlib
import re
from pathlib import Path

EXPECTED_DEFS_BLOB = "8024700cbfefb54d763b487afa84c03fef58a550"
EXPECTED_UPSTREAM_LAKE_BLOB = "43d9da33fb523dce999b070df74e7cdd03381e2b"
EXPECTED_UPSTREAM_MATHLIB_REV = "51e6992efd06126df61a496bebf8f49482a4e129"
EXPECTED_LOCAL_MATHLIB_REV = "v4.34.0"
LITERAL_PAPER_FT = (
    "def paperFT (f : ℝ → ℂ) (z : ℂ) : ℂ := "
    "∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))"
)


def blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def check_file(path: Path, expected: str) -> str:
    raw=path.read_bytes()
    actual=blob_sha(raw)
    if actual != expected:
        raise RuntimeError(f"{path}: wrong upstream blob {actual}, expected {expected}")
    return raw.decode("utf-8")


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--defs",type=Path)
    p.add_argument("--upstream-lake",type=Path)
    p.add_argument("--require-matched-mathlib",action="store_true")
    args=p.parse_args()
    if (args.defs is None) != (args.upstream_lake is None):
        p.error("both --defs and --upstream-lake must be supplied together")
    if args.defs is None:
        if args.require_matched_mathlib:
            p.error("cannot require compatible import without actual upstream source files")
        print("PI014 UPSTREAM SOURCE CHECK: NOT RUN (files not supplied)")
        print("No Zeta23.paperFT import/custody receipt asserted")
        return

    defs=check_file(args.defs,EXPECTED_DEFS_BLOB)
    upstream=check_file(args.upstream_lake,EXPECTED_UPSTREAM_LAKE_BLOB)
    if LITERAL_PAPER_FT not in defs:
        raise RuntimeError("Source blob lacks exact inspected positive-exponent paperFT")
    local=Path("lakefile.toml").read_text(encoding="utf-8")
    if not re.search(r'rev\s*=\s*"v4\.34\.0"',local):
        raise RuntimeError("PI014 local Mathlib source pin changed")
    if EXPECTED_UPSTREAM_MATHLIB_REV not in upstream:
        raise RuntimeError("Upstream Mathlib dependency source pin changed")
    print("PI014 LITERAL UPSTREAM SOURCE HASH/SYNTAX GATE: PASS")
    print("Upstream Zeta23 paperFT exponent is +i*z*u; source bytes fixed")
    print(f"PI branch declared Mathlib: {EXPECTED_LOCAL_MATHLIB_REV}")
    print(f"External Zeta23 declared Mathlib: {EXPECTED_UPSTREAM_MATHLIB_REV}")
    print("EXTERNAL IMPORT COMPATIBILITY: OPEN — different declared revisions")
    if args.require_matched_mathlib:
        raise RuntimeError(
            "Cannot assert source-compiled Zeta23 import: "
            "Mathlib revisions are not matched or reconciled"
        )


if __name__=="__main__":
    main()
