#!/usr/bin/env python3
"""IV018 true original three-cell physical source 1/4 coercivity auditor.

Strictly distinguish source-level proven exact Fraction constants from
real pinned Lean kernel acceptance; both 20 new ORIGINAL source
theorems and eight upstream old source anchors must compile and pass
standard axioms (no sorryAx/Oracle) before any 1/4 positivity claim.

The original two NF543 strict collars are UNCHANGED and the new
interval [199/1000,201/1000] is added. Genuine von Mangoldt source
prime term is transferred to the real NF600 n=9 old bound using
actual complex translated Schwartz product integrals, not deleted.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from fractions import Fraction as Q

ROOT=Path("WeilDefect/Arithmetic")
MOD_A=ROOT/"ActualZetaPhaseIVOriginalThreeCellSignedEnvelope.lean"
MOD_B=ROOT/"ActualZetaPhaseIVOriginalThreeCellPrime9Transfer.lean"
OLEAN=Path(".lake/build/lib/lean/WeilDefect/Arithmetic")
LOG_A=Path("iv018-original-three-cell-signed-envelope-axioms.log")
LOG_B=Path("iv018-original-three-cell-prime9-transfer-axioms.log")
PILOT=Path("iv018-original-three-cell-rational-ledger.json")
AUDIT=Path("iv018-original-three-cell-source-kernel-audit.json")
SCHEMA="IV018-original-three-cell-direct-onequarter-kernel-v1"
ALLOWED={"propext","Classical.choice","Quot.sound"}

UPSTREAM_A=[
    "neutralNF600Collars_volume",
    "neutralIV017LowMass_le_tenL1_sq",
    "neutralIV017SignedGamma_lower",
    "neutralIV017OriginalWindowArch_real_eq_spectral",
]
NEW_A=[
    "neutralIV018OldNew_disjoint",
    "neutralIV018ThreeCell_volume",
    "neutralIV018ThreeCell_supported_window",
    "neutralIV018ThreeCell_L1_bound",
    "neutralIV018ThreeCell_L1_sq",
    "neutralIV018ThreeCell_lowMass",
    "neutralIV018ThreeCell_signedGamma_lower",
    "neutralIV018ThreeCell_poleReal_lower",
    "neutralIV018ThreeCell_analyticReal_lower",
    "neutralIV018ThreeCell_oneQuarter_of_primeBound",
]
UPSTREAM_B=[
    "neutralNF600Prime_single",
    "neutralNF600Prime_bound_actual",
    "neutralIV016FrozenConcrete_allIntegerGap",
    "neutralIV016FrozenSelfActiveGap",
]
NEW_B=[
    "neutralIV018OldPlusNew_supportedThreeCell",
    "neutralIV018OldPlusNew_mass_add",
    "neutralIV018OldMass_le_expandedMass",
    "neutralIV018ExpandedCorrelation_eq_old_of_threeZeros",
    "neutralIV018ExpandedActiveCorrelation_eq_old",
    "neutralIV018ExpandedPrime_eq_old",
    "neutralIV018ExpandedPrime_real_bound",
    "neutralIV018OriginalOldPlusNew_oneQuarter_coercive",
    "neutralIV018OriginalFiniteOldPlusNew_oneQuarter",
    "neutralIV018ExistsGenuineNewThreeCellPositiveDirection",
]
DEPS=[
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
    ROOT/"ActualZetaPhaseIVOriginalMixedHermitian.lean",
    ROOT/"ActualZetaOriginalCollarPrimeBound.lean",
    ROOT/"ActualZetaOriginalCollarPrimeGeometry.lean",
    ROOT/"ActualZetaOriginalCollarFourierMass.lean",
    ROOT/"ActualZetaOriginalCollarGammaLower.lean",
    ROOT/"ActualZetaOriginalCollarArchLower.lean",
    ROOT/"ActualZetaOriginalCollarPoleBound.lean",
    ROOT/"ActualZetaOriginalCollarLiteralArch.lean",
    ROOT/"ActualZetaOriginalCollar242Correction.lean",
    Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
    Path("lean-toolchain"),
    Path("lakefile.toml"),
    Path("lake-manifest.json"),
]

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def exact_rationals():
    old=Q(1,250)
    new=Q(1,500)
    total=old+new
    low=10*total
    gamma=Q(11,10)-(Q(11,10)+Q(28,5))*low
    poles=8*total
    signed_residual=gamma-poles
    old_prime=Q(2,5)
    all_source_margin=signed_residual-old_prime
    assert old==Q(1,250)
    assert new==Q(1,500)
    assert total==Q(3,500)
    assert low==Q(3,50)
    assert gamma==Q(349,500)
    assert poles==Q(6,125)
    assert signed_residual==Q(13,20)
    assert all_source_margin==Q(1,4)
    assert total>0 and all_source_margin>0
    def rat(x): return f"{x.numerator}/{x.denominator}"
    result={
        "schema":"IV018-original-three-cell-exact-Fraction-signed-budget-v1",
        "true_old_two_collar_measure":rat(old),
        "true_new_closed_interval_measure":rat(new),
        "true_union_physical_measure":rat(total),
        "low_band_width":10,
        "low_Fourier_mass_fraction":rat(low),
        "original_signed_gamma_mass_floor":rat(gamma),
        "two_original_pole_mass_loss":rat(poles),
        "original_analytic_remaining_mass_floor":rat(signed_residual),
        "historical_NF600_single_n9_prime_mass_upper":rat(old_prime),
        "proposed_FULL_original_signed_Weil_mass_lower":rat(all_source_margin),
        "source_prime_bound_must_pass_Lean_transfer":True,
        "independent_rational_calculation_is_not_Lean_kernel":True,
        "global_Weil_positivity_proved":False,
        "RH_proved":False,
    }
    PILOT.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("IV018 EXACT rational THREE-cell ledger PASS: measure=3/500, low=3/50, Gamma=349/500, two-poles=6/125, analytic=13/20, genuine n9 prime cost=2/5, residual full=1/4. NOT LEAN.")
    return result

def source_preflight():
    for mod,up,new in ((MOD_A,UPSTREAM_A,NEW_A),(MOD_B,UPSTREAM_B,NEW_B)):
        source=mod.read_text()
        assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b",source,re.M),mod
        assert not re.search(r"\b(?:sorryAx)\b",source),mod
        actual=re.findall(r"^theorem (neutralIV018\w+)",source,re.M)
        assert actual==new,(mod,actual,new)
        prints=re.findall(r"^#print axioms (\w+)$",source,re.M)
        assert prints==up+new,(mod,prints,up+new)
    a=MOD_A.read_text()
    b=MOD_B.read_text()
    for marker in (
        "neutralNF543OriginalCollars",
        "neutralIV017NarrowPhysicalInterval",
        "measure_union",
        "neutralNF600Collars_volume",
        "neutralIV017NarrowPhysicalInterval_volume",
        "integral_mul_norm_le_Lp_mul_Lq",
        "neutralIV017SignedGamma_lower",
        "neutralIV017OriginalPole_norm_le_eightL1_sq",
        "neutralIV017OriginalWindowArch_real_eq_spectral",
        "neutralIV018ThreeCell_oneQuarter_of_primeBound",
    ):
        assert marker in a,("Missing authenticated physical/analytic marker",marker)
    for marker in (
        "neutralIV015FrozenCollar_activeSeparated_of_gap",
        "neutralIV016FrozenConcrete_allIntegerGap",
        "neutralIV016FrozenSelfActiveGap",
        "neutralIV014ActiveSeparated_of_intervalGap",
        "neutralIV011MixedCorrelation_eq_schwartzIntegral",
        "neutralIV011OriginalMixedPrime_eq_finite",
        "neutralNF600Prime_bound_actual",
        "neutralIV018ExpandedPrime_eq_old",
        "neutralIV018ExpandedPrime_real_bound",
        "neutralIV018OriginalOldPlusNew_oneQuarter_coercive",
        "neutralIV018ExistsGenuineNewThreeCellPositiveDirection",
    ):
        assert marker in b,("Missing real original n9 prime support transfer",marker)
    for path in DEPS:
        assert path.is_file(),("Missing original source dependency",path)
    exact_rationals()
    print("IV018 ORIGINAL source-only preflight PASS: 20 new three-cell signed/prime source Lean candidates + 8 genuine upstream anchors, not a kernel result.")

def parse_log(path,names):
    log=path.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        log,re.I),(path,"Lean source error")
    out={}
    for name in names:
        target="'WeilDefect."+name+"'"
        yes=re.findall(re.escape(target)+r" depends on axioms: \[([^\]]*)\]",log,re.S)
        no=re.findall(re.escape(target)+r" does not depend on any axioms",log,re.S)
        assert len(yes)+len(no)==1,(path,name,len(yes),len(no))
        a=[] if no else [s.strip() for s in yes[0].split(",") if s.strip()]
        assert set(a)<=ALLOWED,(name,a)
        out[name]=a
    return out

def kernel_verify():
    source_preflight()
    oleans=[OLEAN/(p.stem+".olean") for p in (MOD_A,MOD_B)]
    for p in oleans:
        assert p.is_file() and p.stat().st_size>0,("Actual compiled Lean object required",p)
    one=parse_log(LOG_A,UPSTREAM_A+NEW_A)
    two=parse_log(LOG_B,UPSTREAM_B+NEW_B)
    report={
        "schema":SCHEMA,
        "scope":"Unchanged original literal zeta signed Weil form on historical two strict NF543 collars PLUS true narrow Schwartz interval: physical 3/500 Gamma+2-pole and EXACT n9 prime transfer from old original source.",
        "original_source_sha256":{str(p):digest(p) for p in [MOD_A,MOD_B]+DEPS},
        "actual_compiled_Lean_object_sha256":{str(p):digest(p) for p in oleans},
        "independent_exact_rational_budget_sha256":digest(PILOT),
        "original_upstream_axiom_anchors":UPSTREAM_A+UPSTREAM_B,
        "new_Lean_source_theorems":NEW_A+NEW_B,
        "genuine_standard_axiom_receipts":{**one,**two},
        "genuine_original_1over4_three_cell_Weil_coercivity_Lean_PASS":True,
        "true_n9_original_prime_bounds_transferred":True,
        "original_new_bump_nonzero_and_outside_old_collars":True,
        "global_Weil_positivity_proved":False,
        "RH_proved":False,
    }
    AUDIT.write_text(json.dumps(report,sort_keys=True,indent=2)+"\n")
    print("IV018 REAL ORIGINAL SOURCE 1/4 COERCIVITY KERNEL PASS: 20 new + 8 accepted source anchor standard axioms; genuine expanded THREE-cell class, NOT RH.")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","verify"))
    if p.parse_args().stage=="preflight": source_preflight()
    else: kernel_verify()
