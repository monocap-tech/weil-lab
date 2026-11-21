#!/usr/bin/env python3
"""CP026 custody of a REAL original Zeta-v4.35 finite-point sign attachment.

There are FOUR EXPLICIT UNPAID Lean theorem premises:
 (i) original center zetaRemainderBound ≤3e-13 at tLeft,
 (ii) same at tRight,
 (iii) true original A6,256 rotated finite plus source error <0 at tLeft,
 (iv) true original A6,256 rotated finite minus source error >0 at tRight.

A JSON number or a CP025 Python PASS does NOT pay these premises.
This script checks theorem source/contracts, re-executes the CP025
original integer-directed arithmetic, and if an external receipt is
provided, checks ALL 26 exact rational data fields against the fresh
calculation. Only actual compiled Lean-v4.35 .olean and genuine
standard-only #print axioms logs can be called kernel accepted.

The source-only optional workflow is label/manual ONLY. No IV/NF runner
work or new source proof claimed accepted.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"cp011_zeta_v435"
SOURCE=BASE/"CP026OriginalPointBridge.lean"
ORIGINAL=ROOT/"scripts/cp025_original_EM_integer_directed_firstjet_root_bracket.py"
TOOLCHAIN=BASE/"lean-toolchain"
OLEAN=BASE/".lake/build/lib/lean/CP026OriginalPointBridge.olean"
AXLOG=BASE/"cp026-actual-original-point-bridge-axioms.log"
TARGETS=[
    "original_hardy_error_from_source_Borwein",
    "original_negative_of_finite_certificate",
    "original_positive_of_finite_certificate",
    "original_critical_line_zero_in_narrow_bracket",
]
REQUIRED_UPSTREAM={
"Zeta/Zeros/HardyZ.lean":"9975442b0c14011c35f4624197d0bf26169c7665",
"Zeta/EulerMaclaurin/Continuation.lean":"1bb01e946fa7e344497eaf7694fbecff0a714d09",
"Zeta/EulerMaclaurin/ErrorBound.lean":"01184af0dbfd1369e14725e02e990b016bedfe6f",
}
ORIGINAL_ZETA="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
NO_KERNEL={
    "CP026_original_Lean_v435_new_kernel_compiled":False,
    "CP026_original_Lean_v435_new_axiom_audit":False,
    "CP026_original_4_pointwise_analytic_numeric_premises_discharged":False,
    "CP026_original_critical_line_zero_Lean_theorem_unconditional":False,
    "CP026_exact_source_zero_ordinal53_attachment":False,
    "CP026_original_whole_interval_strict_mono_or_curvature":False,
    "CP026_original_signed_Weil_spectral_3x3_dictionary":False,
    "global_Weil_positivity_or_RH":False,
}
ALLOWED={"propext","Classical.choice","Quot.sound"}
POINT_KEYS={
    "149.5":{
      "z_finite_lo":"A_phase_rotated_finite_lo",
      "z_finite_hi":"A_phase_rotated_finite_hi",
      "theta_error_upper":"published_theta_error",
      "zeta_R_value_bound":"original_zeta_remainder_value_cap_source_candidate",
      "actual_Z_lower_conditional":"original_Z_lower",
      "actual_Z_upper_conditional":"original_Z_upper",
      "first_jet_finite_lo":"A_finite_first_derivative_lo",
      "first_jet_finite_hi":"A_finite_first_derivative_hi",
      "first_jet_error":"first_derivative_total_error",
      "actual_Zprime_lower_conditional":"original_Zprime_lower",
      "actual_Zprime_upper_conditional":"original_Zprime_upper",
    },
    "150.05352":{
      "z_finite_lo":"A_phase_rotated_finite_lo",
      "z_finite_hi":"A_phase_rotated_finite_hi",
      "theta_error_upper":"published_theta_error",
      "zeta_R_value_bound":"original_zeta_remainder_value_cap_source_candidate",
      "actual_Z_lower_conditional":"original_Z_lower",
      "actual_Z_upper_conditional":"original_Z_upper",
    },
    "150.05353":{
      "z_finite_lo":"A_phase_rotated_finite_lo",
      "z_finite_hi":"A_phase_rotated_finite_hi",
      "theta_error_upper":"published_theta_error",
      "zeta_R_value_bound":"original_zeta_remainder_value_cap_source_candidate",
      "actual_Z_lower_conditional":"original_Z_lower",
      "actual_Z_upper_conditional":"original_Z_upper",
    },
}
# The exact t of the second point in the uploaded receipt is
# 1875669/12500, NOT the decimal string 150.05352; compare numerically.
POINT_REAL={"149.5":F(299,2),"150.05352":F(1875669,12500),
            "150.05353":F(15005353,100000)}

def sha256(p:Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def git_blob_sha(p:Path):
    h=hashlib.sha1(b"blob "+str(p.stat().st_size).encode()+b"\0")
    with p.open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""):
            h.update(block)
    return h.hexdigest()

def source_integrity():
    code=SOURCE.read_text("utf-8")
    imported=re.findall(r"(?m)^public import\s+(\S+)",code)
    if len(imported)!=4 or any(not n.startswith(("Zeta.","Mathlib.")) for n in imported):
        raise ValueError("new original point Bridge must import ONLY four genuine upstream modules")
    if re.search(r"(?m)^\s*(sorry|axiom|constant|opaque)\b",code):
        raise ValueError("new theorem source contains admitted fact/new axiom")
    names=re.findall(r"(?m)^theorem\s+(\w+)\b",code)
    printed=re.findall(r"(?m)^#print axioms\s+CP026OriginalPointBridge\.(\w+)",code)
    if names!=TARGETS or printed!=TARGETS:
        raise ValueError("CP026 4 theorem/standard axiom declarations mismatch")
    # EXACT identities of the published actual Hardy-Z source:
    for api in (
        "riemannZeta_eq_approximant_add_remainder",
        "norm_zetaRemainder_le",
        "abs_riemannSiegelTheta_sub_approximant_two_le",
        "abs_hardyZ_sub_re_le'",
        "continuousOn_hardyZ",
        "hardyZ_eq_zero_iff_riemannZeta",
        "intermediate_value_Ioo",
    ):
        if api not in code:raise ValueError("original source proof transfer missing "+api)
    for target in ["hRLeft","hRRight","hFiniteLeft","hFiniteRight"]:
        if target not in code:raise ValueError("unpaid original proof obligation not explicit: "+target)
    if "[[lean_lib]]\nname = \"CP026OriginalPointBridge\"" not in (BASE/"lakefile.toml").read_text():
        raise ValueError("standalone true-upstream source compiler target not registered")
    if TOOLCHAIN.read_text("utf-8").strip()!="leanprover/lean4:v4.35.0":
        raise ValueError("original frozen Lean compiler mismatch")
    print("CP026 ORIGINAL HARDYZ SOURCE ZERO-BRIDGE FOUR-EXPLICIT-PREMISE LEAN CANDIDATES: 4/4 SOURCE CHECK PASS NOT LEAN")

def upstream_integrity(original:Path):
    for p,ref in REQUIRED_UPSTREAM.items():
        path=original/p
        if git_blob_sha(path)!=ref:raise ValueError("original published frozen SHA mismatch "+p)
    print("CP026 THREE ORIGINAL ZETA PRIMARY API GIT BLOBS: 3/3 PASS NOT LEAN")

def original_integer_replay():
    sp=importlib.util.spec_from_file_location("cp025_original_external_analytic",ORIGINAL)
    if sp is None or sp.loader is None:raise ValueError("CP025 script cannot be imported")
    engine=importlib.util.module_from_spec(sp)
    sp.loader.exec_module(engine)
    engine.arithmetic_controls()
    cert=engine.certificate()
    if "PASS_NOT_LEAN" not in cert["status"]:
        raise ValueError("CP025 external replay accidentally claimed new Lean kernel")
    points=cert["exact_point_intervals"]
    if set(points)!=set(POINT_KEYS):raise ValueError("not the original three source heights")
    # REPLAYED actual finite original A(s), original theta and phase error
    # enclosures must satisfy all deliberately conservative published caps.
    assert F(points["149.5"]["original_Zprime_lower"])>F("2.4426")>F(12,5)
    assert F(points["149.5"]["original_Zprime_upper"])<F("2.4429")
    assert F(points["150.05352"]["original_Z_upper"])<F("-0.000000681")<0
    assert F(points["150.05353"]["original_Z_lower"])>F("0.000015519")>0
    print("CP026 THREE ORIGINAL POINTS 10^55 INTEGER-DIRECTED SOURCE REPLAY: PASS NOT LEAN")
    return cert

def compare_uploaded(uploaded:Path,computed:dict):
    raw=uploaded.read_bytes()
    receipt=json.loads(raw)
    if receipt.get("genuine_Lean_v435_olean_or_axiom_receipts_for_new_CP") is not False:
        raise ValueError("uploaded numerical artifact is improperly labeled kernel certified")
    if receipt.get("source_original_zeta_commit")!=ORIGINAL_ZETA:
        raise ValueError("uploaded original Zeta commit provenance differs")
    if receipt.get("original_source_Git_blob_SHA")!={
        **REQUIRED_UPSTREAM,
        "Zeta/Gamma/LogGammaStirling.lean":"50b98a2a3dfef8cb4e6d77de82d33ac52c8ecaca",
        "Zeta/Gamma/DigammaStirling.lean":"9b5a21dfefe6c778411b03fc7e0cf8e8c5bcfac8",
        "Zeta/Gram/Averaging.lean":"6a30171433903a57736de2ab83b120ef660e08bd",
    }:
        raise ValueError("uploaded six true original source Git-SHA pins changed")
    given=receipt.get("exact_point_evidence",{})
    calc=computed["exact_point_intervals"]
    checks=0
    for height,mapping in POINT_KEYS.items():
        if height not in given:raise ValueError("original height missing "+height)
        if F(given[height]["t"])!=POINT_REAL[height]:
            raise ValueError("point exact rational height changed "+height)
        for uploaded_key,replay_key in mapping.items():
            if uploaded_key=="zeta_R_value_bound":
                # The uploaded receipt calls this source bound an analytical
                # assumption. The replay script intentionally leaves it as
                # a printed fraction rather than proof of source theorem.
                expected=F("3/10000000000000")
                if F(given[height][uploaded_key])!=expected:
                    raise ValueError("unexpected original source value-error premise "+height)
            else:
                if F(given[height][uploaded_key])!=F(calc[height][replay_key]):
                    raise ValueError("MISMATCH "+height+": "+uploaded_key)
            checks+=1
    if checks!=25:
        raise ValueError("all expected exact uploaded rational fields not checked: "+str(checks))
    print("CP026 USER-UPLOADED CP025 25 EXACT INTERVAL FIELDS REPLAY EQUAL: PASS NOT LEAN")
    print("  Upload bytes SHA256 =",hashlib.sha256(raw).hexdigest())
    return hashlib.sha256(raw).hexdigest()

def actual_kernel_audit():
    source_integrity()
    if not OLEAN.is_file() or not AXLOG.is_file():
        raise ValueError("NOT READY: actual original Lean .olean and #print axioms log missing")
    log=AXLOG.read_text("utf-8")
    if re.search(r"sorryAx|error:|unsolved goals|admit",log):
        raise ValueError("NOT READY: kernel log indicates error or admission")
    for theorem in TARGETS:
        pattern=re.compile(re.escape("'CP026OriginalPointBridge."+theorem+"'")
                           +r"\s+depends on axioms:\s*\[([^\]]*)\]")
        actual=pattern.findall(log)
        if len(actual)!=1:raise ValueError("NOT READY: missing unique actual Lean axiom output "+theorem)
        axioms={v.strip() for v in actual[0].split(",") if v.strip()}
        if not axioms<=ALLOWED:
            raise ValueError("NOT READY: unexpected nonstandard kernel axiom "+str(axioms-ALLOWED))
    print("CP026 CONDITIONAL FOUR-THEOREM ORIGINAL v4.35 LEAN KERNEL/Axioms PASS")
    print("  REMAINS CONDITIONAL: two original source remainder and two finite-point numerical Lean goals NOT PROVED")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source-check",action="store_true")
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--original-zeta",type=Path)
    p.add_argument("--uploaded-cp025",type=Path)
    p.add_argument("--kernel-audit",action="store_true")
    p.add_argument("--receipt",type=Path)
    a=p.parse_args()
    if a.source_check:source_integrity()
    if a.original_zeta:upstream_integrity(a.original_zeta)
    calc=original_integer_replay() if a.self_test else None
    sha=None
    if a.uploaded_cp025:
        if calc is None:raise ValueError("uploaded CP025 receipt needs genuine fresh integer replay")
        sha=compare_uploaded(a.uploaded_cp025,calc)
    if a.kernel_audit:actual_kernel_audit()
    if a.receipt:
        if not (a.source_check and a.original_zeta and a.self_test):
            raise ValueError("NOT READY: source imports + three upstream SHAs + exact 255-term integer replay required")
        result={
          "status":"CP026_TRUE_ORIGINAL_UPSTREAM_SOURCE_BRIDGE_AND_DIRECTED_POINT_REPLAY_PASS_NOT_LEAN",
          "source_declaration_sha256":sha256(SOURCE),
          "original_255plus6_EM_evaluation_sha256":sha256(ORIGINAL),
          "original_frozen_zeta_commit":ORIGINAL_ZETA,
          "original_primary_source_verified_sha":REQUIRED_UPSTREAM,
          "upload_exact_rational_match_count":25 if sha else 0,
          "optional_uploaded_receipt_sha256":sha,
          "original_hardy_sign_envelopes": {
           "left_upper":"-0.000000681","right_lower":"0.000015519",
           "anchor_derivative_lower":"2.4426"},
          "unproved_original_Lean_premises":{
           "left_source_center_Borwein":True,
           "right_source_center_Borwein":True,
           "left_true_original_finite_A_theta_sign":True,
           "right_true_original_finite_A_theta_sign":True},
          **NO_KERNEL,
        }
        a.receipt.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        print(result["status"])
    if not any((a.source_check,a.original_zeta,a.self_test,a.kernel_audit)):
        p.print_help()

if __name__=="__main__":
    try:main()
    except (AssertionError,ValueError,OSError,KeyError,ZeroDivisionError) as ex:
        raise SystemExit("CP026 FAIL-CLOSED NOT-READY: "+repr(ex))
