#!/usr/bin/env python3
"""PI034: fail-closed exact-source PI032/PI033 replay custody.

Only scans/replays two unchanged inherited scripts at pinned Git blob SHAs.
Run from the repository or any working dir:
  python3 scripts/pi034_fixed_source_replay.py --part manifest
  python3 scripts/pi034_fixed_source_replay.py --part 32-core
  python3 scripts/pi034_fixed_source_replay.py --part 33-bridge
  python3 scripts/pi034_fixed_source_replay.py --part all

ALL replays PI032 core,1,2,3 and PI033 0,1,2,3,bridge.
This code does not install packages, submit PRs, call Actions, or run Lean.
Every actual interval acceptance is delegated to the SHA-pinned source
without monkeypatching. Exact SHA validation happens before AND after use.
"""
from __future__ import annotations
import argparse
import hashlib
import os
from pathlib import Path
import subprocess
import sys
from fractions import Fraction as F

SOURCE_BLOBS = {
    "pi032_exact_interval_transversality.py":
        "76f16e65e5553f36c5dbb3b74a2a01388083d680",
    "pi033_exact_nine_exhaustive.py":
        "0a5bf6d9cd928e7f1f68335258699f2cd468e78e",
}
# Source identity, NOT a claim that this file fetches or recompiles IV011.
ORIGINAL_IV011_BLOB = "14d8f01ce34f764900eccc68399d7323b4f4a25c"
# Lightweight analytic-geometry checks independent of either imported module.
SIGN_ATLAS = (
    (F(0), F(101, 1000)),
    (F(121, 1000), F(477, 1000)),
    (F(498, 1000), F(690, 1000)),
    (F(706, 1000), F(41, 50)),
)
MONOTONE = (
    (F(101, 1000), F(121, 1000)),
    (F(477, 1000), F(498, 1000)),
    (F(690, 1000), F(706, 1000)),
)
ROOT_BRACKETS = (
    (F(106,1000), F(115,1000)),
    (F(477,1000), F(490,1000)),
    (F(692,1000), F(704,1000)),
)
PARTS = {
    "32-core": ("pi032_exact_interval_transversality.py", "core"),
    "32-1": ("pi032_exact_interval_transversality.py", "1"),
    "32-2": ("pi032_exact_interval_transversality.py", "2"),
    "32-3": ("pi032_exact_interval_transversality.py", "3"),
    "33-0": ("pi033_exact_nine_exhaustive.py", "0"),
    "33-1": ("pi033_exact_nine_exhaustive.py", "1"),
    "33-2": ("pi033_exact_nine_exhaustive.py", "2"),
    "33-3": ("pi033_exact_nine_exhaustive.py", "3"),
    "33-bridge": ("pi033_exact_nine_exhaustive.py", "bridge"),
}


def git_blob_sha(contents: bytes) -> str:
    preamble = b"blob " + str(len(contents)).encode("ascii") + b"\x00"
    return hashlib.sha1(preamble + contents).hexdigest()


def verify_pinned(repo_scripts: Path) -> None:
    assert sys.flags.optimize == 0, "Python -O removes the asserts used as proof gates"
    for filename, expected in SOURCE_BLOBS.items():
        path = repo_scripts / filename
        assert path.is_file(), f"Missing dependency: {path}"
        actual = git_blob_sha(path.read_bytes())
        assert actual == expected, (
            f"Wrong source blob {filename}: expected {expected}, got {actual}"
        )


def verify_partition() -> None:
    intervals = sorted(
        [(a, b, "sign") for a, b in SIGN_ATLAS]
        + [(a, b, "monotone") for a, b in MONOTONE]
        + [(F(41,50), F(1), "analytic-tail")]
    )
    assert intervals[0][0] == 0 and intervals[-1][1] == 1
    assert all(a < b for a, b, _ in intervals)
    assert all(b == c for (_, b, _), (c, _, _) in zip(intervals, intervals[1:]))
    assert all(sum(a <= lo < hi <= b for a, b in MONOTONE) == 1
               for lo, hi in ROOT_BRACKETS)

    assert 435**2 > 21 * 9000
    assert F(13,4)*21/450 < F(1,5)
    assert F(3,2)*F(1,3)*F(2,5) == F(1,5)
    assert 90 >= 9000*F(10,1000)
    assert 65 > 9000*F(7,1000)
    assert 69 > 9000*F(7,1000)
    assert 75 > 9000*F(8,1000)
    v, delta_max = F(369,2500), F(1,3240000)
    p = 1-10*v+24*v*v-12*v**3-delta_max*v**4
    assert p > 0 and -10+48*v < 0
    print(f"PI034 partition/no-gap and source-phase rational gates PASS "
          f"(tail polynomial >0, IV011 blob {ORIGINAL_IV011_BLOB})")


def run_part(repo_scripts: Path, label: str) -> None:
    filename, part = PARTS[label]
    verify_pinned(repo_scripts)
    command = [sys.executable, "-B", str(repo_scripts / filename), "--part", part]
    clean_env = dict(os.environ)
    clean_env.pop("PYTHONOPTIMIZE", None)
    # A one-shot process; never dispatch CI or edit the input scripts.
    result = subprocess.run(command, cwd=str(repo_scripts), env=clean_env,
                            text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, check=False)
    verify_pinned(repo_scripts)
    if result.returncode != 0:
        raise RuntimeError(f"{label} failed ({result.returncode})\n"
                           f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}")
    expected = ("PI032 exact integral/derivative subcertificate PASS"
                if label.startswith("32-")
                else ("PI033 new Iprime(.491)>69 overlap" if label=="33-bridge"
                      else "PI033 exact interval coverage PASS"))
    assert expected in result.stdout, f"No acceptance receipt for {label}"
    print(f"PI034 independent exact-file replay PASS: {label}")
    for line in result.stdout.splitlines():
        if ("PI032 I(0):" in line or "PI032 derivative L2 norm:" in line
                or "PI032 bracket:" in line
                or "PI033 exact interval coverage PASS" in line
                or "PI033 new Iprime(.491)" in line):
            print("  " + line)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", required=True,
                        choices=["manifest", "all", *PARTS])
    args = parser.parse_args()
    scripts = Path(__file__).resolve().parent
    verify_pinned(scripts)
    verify_partition()
    if args.part == "manifest":
        for name, sha in SOURCE_BLOBS.items():
            print(f"PI034 exact pinned Git blob PASS: {name} {sha}")
        return
    for part in (list(PARTS) if args.part=="all" else [args.part]):
        run_part(scripts, part)
    print("PI034 only exact Python replay/custody; no Lean, GitHub Actions or "
          "full complex spectral equivalence.")


if __name__ == "__main__":
    main()
