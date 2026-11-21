#!/usr/bin/env python3
"""CP029: STRICT one-leaf original-Zeta-v4.35 compiler custody.

Target: the UPSTREAM-ONLY CP027PointwiseBorwein lean_lib with 11 actual
source proof candidates (including BOTH unconditional original
zetaRemainderBound endpoint lemmas). Do NOT infer kernel acceptance
from source syntax, Python Fraction tests, a PR check mark, or the
26-field CP025 external integer-directed enclosure.

Source-only mode validates the immutable CP027 candidate identity,
the 11 matching axiom queries, exactly four original Zeta/Mathlib
imports and preserved v4.35 toolchain. The existing independent CP027
source gate verifies original Zeta/Mathlib Git blobs separately.

Kernel mode MUST consume a fresh compiled .olean, the real successful
'lake build CP027PointwiseBorwein' log, and the actual v4.35
'lake env lean CP027PointwiseBorwein.lean' #print axioms transcript.
Every theorem must have ONE real axiom line and only standard Lean
propext / Classical.choice / Quot.sound assumptions (or NONE).
Reject errors, sorry, unlisted axioms and absent results.

No CP021, CP026, CP027TwoFiniteSigns or CP028 local build required.
No RH, global signed Weil positivity, source #53, HardyZ derivative
or unconditional narrow-zero claim follows from this leaf alone.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"cp011_zeta_v435"
SOURCE=BASE/"CP027PointwiseBorwein.lean"
EXPECTED_SOURCE_BLOB="7a4dd8f0994e13c2653cdc3e499409b6072ed8a7"
TOOLCHAIN="leanprover/lean4:v4.35.0"
UPSTREAM_COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
AXIOM_LOG=BASE/"CP027PointwiseBorwein-cp029-isolated-actual-axioms.log"
BUILD_LOG=BASE/"CP027PointwiseBorwein-cp029-isolated-actual-build.log"
OLEAN=BASE/".lake/build/lib/lean/CP027PointwiseBorwein.olean"
ALLOWED={"propext","Classical.choice","Quot.sound"}
TARGETS=[
    "original_ascending_pochhammer_norm",
    "original_B14",
    "original_B14_norm",
    "center_geometry",
    "center_prefactor",
    "original_cpow_norm",
    "original_omitted_term",
    "exact_center_majorant",
    "original_center_Borwein",
    "original_center_Borwein_left",
    "original_center_Borwein_right",
]
EXPECTED_IMPORTS=[
    "Zeta.EulerMaclaurin.ErrorBound",
    "Mathlib.RingTheory.Polynomial.Pochhammer",
    "Mathlib.NumberTheory.Bernoulli",
    "Mathlib.Analysis.SpecialFunctions.Pow.Real",
]

def sha256(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git_blob(path:Path)->str:
    h=hashlib.sha1(b"blob "+str(path.stat().st_size).encode()+b"\\0")
    with path.open("rb") as fh:
        for part in iter(lambda:fh.read(1<<20),b""):
            h.update(part)
    return h.hexdigest()

def source_audit():
    source=SOURCE.read_text(encoding="utf8")
    if git_blob(SOURCE)!=EXPECTED_SOURCE_BLOB:
        raise ValueError("CP027 ORIGINAL source was modified: freeze changes and recheck compiler target before running")
    imports=re.findall(r"(?m)^public import\\s+([^\\n]+)",source)
    if imports!=EXPECTED_IMPORTS:
        raise ValueError("point-only leaf imports not exactly four published upstream modules")
    names=re.findall(r"(?m)^theorem\\s+([A-Za-z0-9_']+)",source)
    printed=re.findall(r"(?m)^#print axioms\\s+CP027PointwiseBorwein\\.([A-Za-z0-9_']+)",source)
    if names!=TARGETS or printed!=TARGETS:
        raise ValueError("eleven original theorem declarations / axiom queries do not match")
    if re.search(r"(?m)^\\s*(?:sorry|axiom|opaque|constant|unsafe)\\b",source):
        raise ValueError("source admissions or new unsafe declarations forbidden")
    if 'name = "CP027PointwiseBorwein"' not in (BASE/"lakefile.toml").read_text("utf8"):
        raise ValueError("original standalone Lake target no longer registered")
    if (BASE/"lean-toolchain").read_text("utf8").strip()!=TOOLCHAIN:
        raise ValueError("original Lean toolchain is NOT pinned v4.35.0")
    for tok in ("zetaRemainderBound (center left) 6 256",
                "zetaRemainderBound (center right) 6 256",
                "original_center_Borwein left", "original_center_Borwein right"):
        if tok not in source:
            raise ValueError("actual original pointwise Borwein theorem contents altered: "+tok)
    print("CP029 ORIGINAL STANDALONE POINTWISE SOURCE/11 AXIOMS/4 UPSTREAM IMPORTS: PASS NOT LEAN")

def kernel_audit():
    source_audit()
    if not (OLEAN.is_file() and OLEAN.stat().st_size>0):
        raise ValueError("genuine original Lean .olean artifact missing")
    if not (BUILD_LOG.is_file() and AXIOM_LOG.is_file()):
        raise ValueError("genuine BUILD and AXIOM transcripts missing")
    build=BUILD_LOG.read_text("utf8",errors="replace")
    axioms=AXIOM_LOG.read_text("utf8",errors="replace")
    if not build.strip() or not axioms.strip():
        raise ValueError("empty Lean compiler transcript")
    for kind,log in (("build",build),("axioms",axioms)):
        if re.search(r"(?i)(?:^|\\n)[^\\n]*(?:error:|unsolved goals|sorryAx|declaration uses 'sorry'|admit)",log):
            raise ValueError(kind+" original v4.35 compiler output contains errors/admissions")
    acceptance={}
    for theorem in TARGETS:
        tag=re.escape("'CP027PointwiseBorwein."+theorem+"'")
        regex=(
            rf"(?m)^{tag}\\s+"
            r"(?:depends on axioms:\\s*\\[([^\\]]*)\\]"
            r"|does not depend on any axioms)\\s*$"
        )
        matches=re.findall(regex,axioms)
        if len(matches)!=1:
            raise ValueError("no UNIQUE genuine #print axioms line for "+theorem)
        terms={s.strip() for s in matches[0].split(",") if s.strip()}
        if not terms <= ALLOWED:
            raise ValueError("forbidden original Lean axiom: "+theorem+" "+str(terms-ALLOWED))
        acceptance[theorem]=sorted(terms)
    print("CP029 ORIGINAL STANDALONE ZETA4.35 CP027 POINTWISE LEAF 11/11 KERNEL+STANDARD-AXIOM PASS")
    print("  Certified: unconditional original source pointwise Borwein error cap at both rational endpoints")
    print("  NOT certified: CP026/27 root bridge or CP028 two true finite boxes")
    return acceptance

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source-check",action="store_true")
    p.add_argument("--kernel-audit",action="store_true")
    p.add_argument("--receipt",type=Path)
    a=p.parse_args()
    if a.source_check:source_audit()
    axioms=kernel_audit() if a.kernel_audit else None
    if a.receipt:
        if axioms is None:
            raise ValueError("FAIL CLOSED: KERNEL receipt requires actual .olean, build transcript and 11 genuine standard-only axiom lines")
        data={
            "status":"CP029_ORIGINAL_435_POINTWISE_BORWEIN_TWO_ENDPOINTS_ACTUAL_KERNEL_ACCEPTED",
            "original_zeta_commit":UPSTREAM_COMMIT,
            "toolchain":TOOLCHAIN,
            "source_git_blob":git_blob(SOURCE),
            "source_sha256":sha256(SOURCE),
            "actual_olean_sha256":sha256(OLEAN),
            "actual_build_log_sha256":sha256(BUILD_LOG),
            "actual_axioms_log_sha256":sha256(AXIOM_LOG),
            "eleven_true_standard_axiom_theorems":axioms,
            "new_source_center_remainder_left_kernel_accepted":True,
            "new_source_center_remainder_right_kernel_accepted":True,
            "original_finite_A6N256_left_box_Lean_paid":False,
            "original_finite_A6N256_right_box_Lean_paid":False,
            "original_critical_line_zero_unconditional_Lean_accepted":False,
            "original_ordinal53_Lean_accepted":False,
            "whole_height_HardyZ_curvature":False,
            "signed_Weil_spectral_matrix_equivalence":False,
            "global_signed_Weil_positivity_or_RH":False,
        }
        a.receipt.write_text(json.dumps(data,indent=2)+"\\n",encoding="utf8")
        print(data["status"])
    if not a.source_check and not a.kernel_audit:p.print_help()

if __name__=="__main__":
    try:main()
    except (AssertionError,ValueError,OSError,UnicodeError) as ex:
        raise SystemExit("CP029 NOT KERNEL-ACCEPTED: "+str(ex))
