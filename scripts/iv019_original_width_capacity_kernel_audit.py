#!/usr/bin/env python3
"""IV019 REAL original-source signed width capacity and wider prime-gap audit.

Scope:
 * The complete ORIGINAL zeta mixed gamma+TWO-pole+von-Mangoldt
   signed Weil diagonal is retained.
 * The old NF543 strict two collars and true original 11/10 physical
   window never move.
 * The proposed new test around x=1/5 has radius 1/500, DOUBLE
   IV015's original 1/1000 radius. Its old/new and self log-frequency
   exclusion margins are certified independently by EXACT Fraction
   series enclosures, not approximate floating-point tests.
 * The signed analytic budget r<1/375 is a BUDGET threshold, NOT a
   no-go theorem about any other methods or the Riemann hypothesis.

All 16 new Lean declarations and seven genuine upstream anchors need
their ACTUAL compiled .olean and standard-only #print axioms receipts
before saying Lean PASS. Source and rational preflight alone are NOT
kernel acceptance.
"""
import argparse
import hashlib
import json
import re
from fractions import Fraction as Q
from pathlib import Path
from iv015_frozen_collar_exact_log_gap import log_bracket

ROOT=Path("WeilDefect/Arithmetic")
MOD_A=ROOT/"ActualZetaPhaseIVOriginalVariableWidthSignedBudget.lean"
MOD_B=ROOT/"ActualZetaPhaseIVOriginalWiderPrimeFreeBump.lean"
OLEAN_ROOT=Path(".lake/build/lib/lean/WeilDefect/Arithmetic")
LOG_A=Path("iv019-original-variable-width-signed-budget-axioms.log")
LOG_B=Path("iv019-original-wider-primefree-bump-axioms.log")
RATIONAL=Path("iv019-original-wider-physical-capacity-exact-rational.json")
RESULT=Path("iv019-original-width-capacity-kernel-audit.json")
SCHEMA="IV019-original-variable-width-signed-source-and-doubled-Schwartz-bump-v1"
ALLOWED={"propext","Classical.choice","Quot.sound"}

UP_A=[
    "neutralIV017SignedGamma_lower",
    "neutralIV017LowMass_le_tenL1_sq",
    "neutralIV017OriginalPole_norm_le_eightL1_sq",
    "neutralIV017OriginalWindowArch_real_eq_spectral",
]
NEW_A=[
    "neutralIV019OriginalSignedGamma_L1Budget",
    "neutralIV019OriginalSignedPole_L1Budget",
    "neutralIV019OriginalAnalytic_L1Budget",
    "neutralIV019OriginalSignedWeil_L1Budget_of_prime",
    "neutralIV019OriginalSignedWeil_massBudget_of_prime",
    "neutralIV019OriginalRadiusMargin_identity",
    "neutralIV019OriginalRadiusMargin_positive_iff",
    "neutralIV019OriginalDoubleRadius_margin",
    "neutralIV019OriginalOneTenth_of_prime_and_L1",
]
UP_B=[
    "neutralIV016FrozenLogBand_lt10",
    "neutralIV015ExistsComplexSchwartzBump",
    "neutralIV014ActiveMixedPrime_zero",
]
NEW_B=[
    "neutralIV019WideAbsClearance",
    "neutralIV019WideFourSignedGaps_of_band",
    "neutralIV019WideFrozenConcrete_allIntegerGap",
    "neutralIV019WideSelfLogClearance",
    "neutralIV019WideSelfActiveGap",
    "neutralIV019ExistsWiderOriginalPrimeSeparatedBump",
    "neutralIV019ExistsWiderOriginalMixedAndSelfPrimeFree",
]

# Lake generates this lockfile after the source-only preflight (via `lake update`).
# The real kernel verifier still requires and SHA256-binds the generated file.
MANIFEST = Path("lake-manifest.json")
DEPS=[
    ROOT/"ActualZetaPhaseIVOriginalThreeCellSignedEnvelope.lean",
    ROOT/"ActualZetaPhaseIVOriginalThreeCellPrime9Transfer.lean",
    ROOT/"ActualZetaPhaseIVOriginalNarrowSignedGamma.lean",
    ROOT/"ActualZetaPhaseIVOriginalNarrowDiagonalCoercivity.lean",
    ROOT/"ActualZetaPhaseIVOriginalConcreteGapPrimeFreeDiagonal.lean",
    ROOT/"ActualZetaPhaseIVOriginalNonzeroPrimeFreeSchwartzBump.lean",
    ROOT/"ActualZetaPhaseIVOriginalTwoCollarPrimeFreeBump.lean",
    ROOT/"ActualZetaPhaseIVOriginalActivePrimeSupportGeometry.lean",
    ROOT/"ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.lean",
    ROOT/"ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean",
    ROOT/"ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean",
    ROOT/"ActualZetaPhaseIVOriginalCrossSupportExtension.lean",
    ROOT/"ActualZetaPhaseIVOriginalSchwartzPolarization.lean",
    ROOT/"ActualZetaOriginalCollarPrimeBound.lean",
    ROOT/"ActualZetaOriginalCollarPrimeGeometry.lean",
    ROOT/"ActualZetaOriginalCollarFourierMass.lean",
    ROOT/"ActualZetaOriginalCollarArchLower.lean",
    ROOT/"ActualZetaOriginalCollarGammaLower.lean",
    ROOT/"ActualZetaOriginalCollarPoleBound.lean",
    ROOT/"ActualZetaOriginalCollarLiteralArch.lean",
    ROOT/"ActualZetaOriginalCollar242Correction.lean",
    Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
    Path("scripts/iv015_frozen_collar_exact_log_gap.py"),
    Path("scripts/iv018_original_three_cell_coercivity_audit.py"),
    Path("lean-toolchain"),
]

def hashbytes(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def frac_str(v):
    return f"{v.numerator}/{v.denominator}"

def abs_lower(lo,hi):
    if lo>0:return lo
    if hi<0:return -hi
    return Q(0)

def raw_gap_margin(center,radius,cutoff=10):
    old_centers=(-Q(1099,1000),Q(1099,1000))
    old_radius=Q(1,1000)
    m=None
    for n in range(cutoff):
        lo,hi=log_bracket(n)
        for oldc in old_centers:
            base=center-oldc
            for sign in (-1,+1):
                zl,zh=(base-hi,base-lo) if sign==-1 else (base+lo,base+hi)
                gap=abs_lower(zl,zh)-(old_radius+radius)
                if m is None or gap<m: m=gap
    return m

def exact_capacity_receipt():
    center=Q(1,5)
    r=Q(1,500)
    old_measure=Q(1,250)
    new_measure=2*r
    total=old_measure+new_measure
    low=10*total
    gamma=Q(11,10)-Q(67,10)*low
    two_poles=8*total
    active_prime_cost=Q(2,5)
    margin=gamma-two_poles-active_prime_cost
    assert total==Q(1,125)
    assert low==Q(2,25)
    assert gamma==Q(141,250)
    assert two_poles==Q(8,125)
    assert margin==Q(1,10)
    assert margin==Q(2,5)-150*r

    gap=raw_gap_margin(center,r)
    assert gap>0
    ln10lo,_=log_bracket(10)
    assert ln10lo>Q(11,5)

    self_lo,_=log_bracket(2)
    assert self_lo>2*r
    threshold=Q(1,375)
    assert raw_gap_margin(center,threshold)>0
    assert Q(2,5)-150*threshold==0
    assert raw_gap_margin(center,Q(1,100))>0
    assert Q(2,5)-150*Q(1,100)<0

    # Fail-closed counterfactual geometry.
    assert raw_gap_margin(Q(1099,1000),r)<0
    assert raw_gap_margin(center,Q(1,10))<0
    assert log_bracket(9)[1] < Q(11,5)

    data={
      "schema":"IV019-actual-original-signed-width-and-twofold-Schwartz-geometry-exact-rational-v1",
      "new_center":"1/5",
      "new_radius":"1/500",
      "historical_original_two_strict_NF543_collar_measure":"1/250",
      "new_interval_width":frac_str(new_measure),
      "union_measure":frac_str(total),
      "physical_low_frequency_mass_upper_fraction":frac_str(low),
      "true_signed_Gamma_symbol_lower_fraction":frac_str(gamma),
      "two_original_pole_upper_cost":frac_str(two_poles),
      "original_n9_prime_cost_requires_real_Lean_transfer":frac_str(active_prime_cost),
      "candidate_full_original_signed_Weil_lower":frac_str(margin),
      "analytic_positive_radius_iff_less_than":"1/375",
      "analytical_zero_margin_at_radius":"1/375",
      "self_active_prime_log2_strict_clearance":frac_str(self_lo-2*r),
      "minimum_original_frozen_two_collar_four_signed_translated_gap":frac_str(gap),
      "all_n_0_through_9_original_two_collars_both_signs_exact_Fraction_pass":True,
      "n10_true_original_log_cutoff_exact_Fraction_pass":True,
      "negative_control_old_collar_center_rejected":True,
      "negative_control_overwide_bump_overlap_rejected":True,
      "negative_control_cutoff_n9_rejected":True,
      "signed_budget_limitation_precedes_prime_overlap_at_center_1over5":True,
      "new_expanded_class_prime_transfer_LEAN_PROVED":False,
      "new_expanded_class_full_original_coercivity_LEAN_PROVED":False,
      "original_global_Weil_positivity_proved":False,
      "RH_proved":False,
    }
    RATIONAL.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
    print("IV019 EXACT FRACTION PASS: double-radius 1/500, union 1/125, Gamma 141/250, both poles 8/125, remaining 1/10 after n9 old-prime allowance. Active ±log gap STRICTLY positive. r=1/375 width-budget threshold, NOT no-go result. LEAN STILL PENDING.")
    return data

def source_preflight():
    for p,up,new in ((MOD_A,UP_A,NEW_A),(MOD_B,UP_B,NEW_B)):
        s=p.read_text()
        assert re.findall(r"^theorem (neutralIV019\w+)",s,re.M)==new,(p,"theorem mismatch")
        assert re.findall(r"^#print axioms (\w+)$",s,re.M)==up+new,(p,"axiom mismatch")
        assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b",s,re.M)
        assert not re.search(r"\bsorryAx\b",s)
    for symbol in (
        "neutralIV017SignedGamma_lower",
        "neutralIV017LowMass_le_tenL1_sq",
        "neutralIV017OriginalPole_norm_le_eightL1_sq",
        "neutralIV011OriginalMixed_arithmeticSplit",
        "neutralIV011OriginalMixedPrime",
        "neutralIV019OriginalOneTenth_of_prime_and_L1",
    ):
        assert symbol in MOD_A.read_text(),symbol
    for symbol in (
        "neutralIV016FrozenLogBand_lt10",
        "neutralIV015FrozenTwoCollarActiveGap",
        "neutralIV015ExistsComplexSchwartzBump",
        "neutralIV014ActiveSeparated_of_intervalGap",
        "neutralIV014ActiveMixedPrime_zero",
        "neutralIV019ExistsWiderOriginalMixedAndSelfPrimeFree",
    ):
        assert symbol in MOD_B.read_text(),symbol
    for p in DEPS:
        assert p.is_file(),("Missing actual source dependency",str(p))
    exact_capacity_receipt()
    print("IV019 SOURCE PREFLIGHT PASS: 16 new true original-source Lean candidates, 7 upstream standard axiom anchors; actual Lean verification PENDING.")

def check_log(path,names):
    s=path.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",s,re.I
    ),path
    out={}
    for name in names:
        full="'WeilDefect."+name+"'"
        yes=re.findall(re.escape(full)+r" depends on axioms: \[([^\]]*)\]",s,re.S)
        no=re.findall(re.escape(full)+r" does not depend on any axioms",s,re.S)
        assert len(yes)+len(no)==1,(path,name,len(yes),len(no))
        axioms=[] if no else [v.strip() for v in yes[0].split(",") if v.strip()]
        assert set(axioms)<=ALLOWED,(name,axioms)
        out[name]=axioms
    return out

def verify():
    source_preflight()
    assert MANIFEST.is_file(), ("Missing generated Lake manifest after update", str(MANIFEST))
    objects=[OLEAN_ROOT/(p.stem+".olean") for p in (MOD_A,MOD_B)]
    for p in objects:
        assert p.is_file() and p.stat().st_size>0,("actual compiled Lean object missing",p)
    a=check_log(LOG_A,UP_A+NEW_A)
    b=check_log(LOG_B,UP_B+NEW_B)
    data={
      "schema":SCHEMA,
      "true_original_source_and_toolchain_sha256":{str(p):hashbytes(p) for p in [MOD_A,MOD_B]+DEPS+[MANIFEST]},
      "compiled_Lean_source_objects_sha256":{str(p):hashbytes(p) for p in objects},
      "independent_exact_rational_capacity_sha256":hashbytes(RATIONAL),
      "new_IV019_proved_Lean_declarations":NEW_A+NEW_B,
      "genuine_upstream_original_axiom_anchors":UP_A+UP_B,
      "verified_standard_only_Lean_axioms":{**a,**b},
      "original_1over10_signed_Weil_L1_and_prime_gate_LEAN_PASS":True,
      "wider_nonzero_complex_Schwartz_prime_free_self_and_mixed_LEAN_PASS":True,
      "wider_old_plus_new_complete_prime_transfer_LEAN_PASS":False,
      "wider_old_plus_new_unconditional_original_coercivity_LEAN_PASS":False,
      "global_Weil_positivity":False,
      "RH":False,
    }
    RESULT.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n")
    print("IV019 ACTUAL LEAN KERNEL PASS: 16 new source + 7 upstream standard axiom anchors, true original bounded-prime signed L1 budget and double-radius real Schwartz prime-free witness. Broader support class transfer UNPROVED.")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","verify"))
    if p.parse_args().stage=="preflight": source_preflight()
    else: verify()
