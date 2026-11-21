#!/usr/bin/env python3
"""CP028: drastically looser, source-faithful finite Euler–Maclaurin sign boxes.

The ORIGINAL external CP025 255-term + six Bernoulli + pole/half
directed integer interval evaluator is re-executed, NOT trusted from
a JSON file. From its interval source, check at true rational tL/R:
    ||A_6,256(s_t)|| <= 1/1000
    Re(exp(i theta_stirling2(tL))*A_6,256(s_tL)) < -1/10^7
    Re(exp(i theta_stirling2(tR))*A_6,256(s_tR)) > 1/10^7.

Pure rational source-error transfer:
    12/150^4*(1/1000) + 3/10^13
        = 6481/270000000000000
        < 1/10^10,
with actual finite signed threshold ±1e-7. This proves the
FORMAL CONDITIONAL transition from two simple finite source
boxes to CP027's two yet-unpaid true original finite-sign goals.

The actual 255-term complex interval enclosures are still EXTERNAL:
the CP028 Lean file does NOT formally establish the four finite
component bounds, nor does it compile here. Actual original
Lean v4.35 .olean and standard-only #print axioms are REQUIRED
for the true proof. No zero ordinal 53, uniqueness, spectral
dictionary, RH, or original global Weil positivity.

No mpmath, sympy, float, numerical special-function oracle,
or uploaded JSON are needed to produce source-only PASS. All
source evidence is from CP025's 10^55 directed integer engine.
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
DIR=ROOT/"cp011_zeta_v435"
SRC=DIR/"CP028CoarseFiniteBoxes.lean"
CP025=ROOT/"scripts/cp025_original_EM_integer_directed_firstjet_root_bracket.py"
L=F(15005352,100000)
R=F(15005353,100000)
MAX_NORM=F(1,1000)
SIGN=F(1,10**7)
ERR_CAP=F(1,10**10)
BORWEIN=F(3,10**13)
ERR_RATIONAL=F(12,150**4)*MAX_NORM+BORWEIN
EXPECTED=F(6481,270000000000000)
TARGETS=[
    "sourcePointError_lt_ten_billionth",
    "original_left_finite_sign_of_coarse_box",
    "original_right_finite_sign_of_coarse_box",
    "original_narrow_zero_of_two_coarse_boxes",
]
ALLOWED={"propext","Classical.choice","Quot.sound"}

def pure_exact():
    assert L==F("150.05352") and R==F("150.05353") and 150<L<R
    assert ERR_RATIONAL==EXPECTED
    assert 0<ERR_RATIONAL<ERR_CAP<SIGN
    assert SIGN-ERR_CAP>0
    assert MAX_NORM==F(1,1000)
    # A smaller claimed phase/remainder error is invalid.
    assert ERR_RATIONAL>F(1,10**11)
    # A weak finite threshold of 1e-11 is NOT enough.
    assert F(1,10**11)<ERR_RATIONAL
    # The pointwise source Borwein remains an **uncompiled**
    # analytic proof input even though CP027 rational math is valid.
    print("CP028 EXACT COARSE-FINITE-PHASE ERROR RATIONAL BRIDGE: PASS NOT LEAN")
    print("  original source finite-point norm target <=",MAX_NORM)
    print("  original finite signed target ±",SIGN)
    print("  exact conditional original theta+B14 remainder error <=",ERR_RATIONAL)
    print("  hard upper target =",ERR_CAP)
    print("  strict finite-sign safety margin >",SIGN-ERR_CAP)
    print("  negative controls too-small error and too-small sign threshold: PASS")

def get_cp025():
    spec=importlib.util.spec_from_file_location("original_CP025_integer_directed",CP025)
    if spec is None or spec.loader is None:
        raise ValueError("cannot import original 255-term directed engine")
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def original_exact_replay():
    m=get_cp025()
    m.arithmetic_controls()
    rows={}
    for name,t in (("left",L),("right",R)):
        A,_deriv=m.original_A_and_Ds(t)
        n=A.normup()
        finite=m.enclosure(t,False)
        f_lo=F(finite["A_phase_rotated_finite_lo"])
        f_hi=F(finite["A_phase_rotated_finite_hi"])
        assert n>0
        assert n<=MAX_NORM, f"{name} genuine original A norm bound NOT paid"
        if name=="left":
            assert f_hi<-SIGN, "original finite left sign threshold not met"
        else:
            assert f_lo>SIGN, "original finite right sign threshold not met"
        rows[name]={
            "original_rational_t":str(t),
            "actual_255plus6_original_A_complex_interval_norm_upper":str(n),
            "original_finite_rotated_lower":str(f_lo),
            "original_finite_rotated_upper":str(f_hi),
            "passes_coarse_norm_target":n<=MAX_NORM,
            "passes_coarse_signed_finite_target":
                f_hi<-SIGN if name=="left" else f_lo>SIGN,
        }
        print("  original",name,
              "A norm upper",format(float(n),".12e"),
              "finite rotated",format(float(f_lo),".12e"),
              format(float(f_hi),".12e"),
              "COARSE DIRECTED INTERVAL PASS NOT LEAN")
    # Source calculations must be coarsely far from the targets;
    # two negative controls reject unsupported stronger claims.
    assert F(rows["right"]["actual_255plus6_original_A_complex_interval_norm_upper"])>F(1,10**5)
    assert F(rows["left"]["original_finite_rotated_upper"])>-F(1,10**6)
    print("CP028 ORIGINAL BOTH FINITE A6N256 10^55 INTEGER-DIRECTED COARSE BOXES: 2/2 PASS NOT LEAN")
    return rows

def source_audit():
    s=SRC.read_text("utf8")
    names=re.findall(r"(?m)^theorem\s+(\w+)\b",s)
    prints=re.findall(r"(?m)^#print axioms\s+CP028CoarseFiniteBoxes\.(\w+)\b",s)
    if names!=TARGETS or prints!=TARGETS:
        raise ValueError("four exact CP028 source Lean theorem/axiom signatures drift")
    imports=re.findall(r"(?m)^public import\s+([^\n]+)",s)
    if imports!=["CP027TwoFiniteSigns"]:
        raise ValueError("CP028 no longer imports actual two finite-sign original bridge")
    for word in (
        "sourcePointError t < (1 : ℝ) / (10 : ℝ) ^ 10",
        "sourceFiniteZ tLeft < -((1 : ℝ) / (10 : ℝ) ^ 7)",
        "((1 : ℝ) / (10 : ℝ) ^ 7) < sourceFiniteZ tRight",
        "‖sourceA tLeft‖ ≤ (1 : ℝ) / 1000",
        "‖sourceA tRight‖ ≤ (1 : ℝ) / 1000",
        "CP027TwoFiniteSigns.original_narrow_critical_line_zero_of_two_finite_signs",
    ):
        if word not in s:raise ValueError("original HardyZ source contract mismatch "+word)
    if re.search(r"(?m)^\s*(?:sorry|axiom|constant|opaque|unsafe)\b",s):
        raise ValueError("untrusted Lean proof admission")
    lake=(DIR/"lakefile.toml").read_text("utf8")
    if 'name = "CP028CoarseFiniteBoxes"' not in lake:
        raise ValueError("CP028 original true toolchain library not registered")
    if (DIR/"lean-toolchain").read_text().strip()!="leanprover/lean4:v4.35.0":
        raise ValueError("original source toolchain not v4.35")
    print("CP028 ORIGINAL TRUE SOURCE TWO COARSE FINITE BOXES / FOUR AXIOMS: 4/4 SOURCE PASS NOT LEAN")

def actual_kernel_audit():
    source_audit()
    olean=DIR/".lake/build/lib/lean/CP028CoarseFiniteBoxes.olean"
    log=DIR/"CP028CoarseFiniteBoxes-actual-source-axioms.log"
    if not (olean.is_file() and log.is_file()):
        raise ValueError("NOT READY: actual original v4.35 kernel .olean/axiom log ABSENT")
    text=log.read_text("utf8")
    if re.search(r"sorryAx|error:|unsolved goals|admit",text):
        raise ValueError("NOT READY: actual original compiler output contains admissions/errors")
    for t in TARGETS:
        m=re.findall(re.escape("'CP028CoarseFiniteBoxes."+t+"'")+
                 r"\s+depends on axioms:\s*\[([^\]]*)\]",text)
        if len(m)!=1:raise ValueError("NOT READY missing actual Lean axiom roster: "+t)
        ax={x.strip() for x in m[0].split(",") if x.strip()}
        if not ax<=ALLOWED:raise ValueError("nonstandard Lean axioms: "+str(ax-ALLOWED))
    print("CP028 CONDITIONAL ORIGINAL FOUR-SOURCE-THEOREM LEAN KERNEL PASS")
    print("  TWO ORIGINAL COMPLEX FINITE A BOX NUMERICAL CERTIFICATES ARE STILL UNPAID")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--source-check",action="store_true")
    p.add_argument("--kernel-audit",action="store_true")
    p.add_argument("--receipt",type=Path)
    a=p.parse_args()
    if a.self_test:
        pure_exact()
        res=original_exact_replay()
    else:res=None
    if a.source_check:source_audit()
    if a.kernel_audit:actual_kernel_audit()
    if a.receipt:
        if not (a.self_test and a.source_check):
            raise ValueError("fail closed: receipt REQUIRES original 255+6 integer replay and actual source contracts")
        o={
            "status":"CP028_ORIGINAL_TWO_COARSE_FINITE_DIRECTED_BOXES_PASS_NOT_LEAN",
            "source_original_Zeta_commit":"c06b4e13d9c847e50a32c3d738271cbad62ae9f3",
            "original_true_toolchain":"leanprover/lean4:v4.35.0",
            "original_lean_source_sha256":hashlib.sha256(SRC.read_bytes()).hexdigest(),
            "exact_255plus6_interval_engine_sha256":hashlib.sha256(CP025.read_bytes()).hexdigest(),
            "source_phase_and_Borwein_error_upper_conditional":str(ERR_RATIONAL),
            "coarse_finite_norm_upper":str(MAX_NORM),
            "coarse_finite_absolute_sign_lower":str(SIGN),
            "two_original_endpoints":res,
            "new_original_Lean_v435_kernel_accepted":False,
            "two_original_finite_numeric_Lean_enclosures_discharge":False,
            "original_Borwein_point_source_Lean_kernel_accepted":False,
            "original_unconditional_critical_line_zero_Lean_proved":False,
            "original_source_rank53":False,
            "whole_interval_curvature":False,
            "global_signed_Weil_positive":False,
            "Weil_spectral_full_3x3_equivalence":False,
            "RH":False,
        }
        a.receipt.write_text(json.dumps(o,indent=2)+"\n",encoding="utf8")
        print(o["status"])
    if not (a.self_test or a.source_check or a.kernel_audit):p.print_help()

if __name__=="__main__":
    try:main()
    except (AssertionError,ValueError,OSError,ZeroDivisionError) as e:
        raise SystemExit("CP028 FAIL-CLOSED: "+repr(e))
