#!/usr/bin/env python3
"""IV020 direct ORIGINAL source all-old-plus-new 1/10 kernel audit.

True unchanged historical NF543 two strict physical support collars,
new actual 1/500-radius complex Schwartz interval [99/500,101/500],
complete real signed original zeta Weil source, all genuine
von-Mangoldt prime powers, both ±log(n) translated correlations, n=9
surviving old prime and both actual original polar residues / Gamma.

Two new ORIGINAL Lean modules and all named upstream source anchors
must build, produce real .olean files and pass #print axioms with ONLY
the three standard kernel axioms. The independent exact Fraction
ledger is not a substitute for a real Lean compiler/audit receipt.
"""
import argparse
import hashlib
import json
import re
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path("WeilDefect/Arithmetic")
M1 = ROOT / "ActualZetaPhaseIVOriginalWiderThreeCellSourceMeasure.lean"
M2 = ROOT / "ActualZetaPhaseIVOriginalWiderThreeCellPrime9Coercivity.lean"
OLEAN = Path(".lake/build/lib/lean/WeilDefect/Arithmetic")
LOG1 = Path("iv020-original-wide-source-measure-axioms.log")
LOG2 = Path("iv020-original-wide-prime9-coercivity-axioms.log")
LEDGER = Path("iv020-original-doubled-radius-exact-rational-budget.json")
REPORT = Path("iv020-original-wide-three-cell-kernel-audit.json")
SCHEMA = "IV020-original-1over10-wider-three-cell-prime9-source-kernel-v1"
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

OLD1 = [
    "neutralNF600Collars_volume",
    "neutralIV019OriginalOneTenth_of_prime_and_L1",
    "neutralIV019WideFrozenConcrete_allIntegerGap",
]
NEW1 = [
    "neutralIV020WidePhysicalInterval_volume",
    "neutralIV020Wide_support_from_bump",
    "neutralIV020WideOldNew_disjoint",
    "neutralIV020WideThreeCell_volume",
    "neutralIV020WideThreeCell_supported_window",
    "neutralIV020WideThreeCell_L1_bound",
    "neutralIV020WideThreeCell_L1_sq",
    "neutralIV020WideThreeCell_oneTenth_of_primeBound",
]
OLD2 = [
    "neutralNF600Prime_single",
    "neutralNF600Prime_bound_actual",
    "neutralIV019WideFrozenConcrete_allIntegerGap",
    "neutralIV019WideSelfActiveGap",
]
NEW2 = [
    "neutralIV020WideOldPlusNew_supportedThreeCell",
    "neutralIV020WideOldPlusNew_mass_add",
    "neutralIV020WideOldMass_le_expandedMass",
    "neutralIV020WideExpandedCorrelation_eq_old_of_threeZeros",
    "neutralIV020WideExpandedActiveCorrelation_eq_old",
    "neutralIV020WideExpandedPrime_eq_old",
    "neutralIV020WideExpandedPrime_real_bound",
    "neutralIV020WideOriginalOldPlusNew_oneTenth_coercive",
    "neutralIV020WideOriginalFiniteOldPlusNew_oneTenth",
    "neutralIV020WideExistsGenuineNewThreeCellPositiveDirection",
]
DEPS = [
    ROOT / "ActualZetaPhaseIVOriginalVariableWidthSignedBudget.lean",
    ROOT / "ActualZetaPhaseIVOriginalWiderPrimeFreeBump.lean",
    ROOT / "ActualZetaPhaseIVOriginalThreeCellSignedEnvelope.lean",
    ROOT / "ActualZetaPhaseIVOriginalThreeCellPrime9Transfer.lean",
    ROOT / "ActualZetaPhaseIVOriginalNarrowSignedGamma.lean",
    ROOT / "ActualZetaPhaseIVOriginalNarrowDiagonalCoercivity.lean",
    ROOT / "ActualZetaPhaseIVOriginalConcreteGapPrimeFreeDiagonal.lean",
    ROOT / "ActualZetaPhaseIVOriginalNonzeroPrimeFreeSchwartzBump.lean",
    ROOT / "ActualZetaPhaseIVOriginalTwoCollarPrimeFreeBump.lean",
    ROOT / "ActualZetaPhaseIVOriginalActivePrimeSupportGeometry.lean",
    ROOT / "ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.lean",
    ROOT / "ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean",
    ROOT / "ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean",
    ROOT / "ActualZetaPhaseIVOriginalCrossSupportExtension.lean",
    ROOT / "ActualZetaPhaseIVOriginalSchwartzPolarization.lean",
    ROOT / "ActualZetaPhaseIVOriginalMixedHermitian.lean",
    ROOT / "ActualZetaOriginalCollarPrimeBound.lean",
    ROOT / "ActualZetaOriginalCollarPrimeGeometry.lean",
    ROOT / "ActualZetaOriginalCollarFourierMass.lean",
    ROOT / "ActualZetaOriginalCollarGammaLower.lean",
    ROOT / "ActualZetaOriginalCollarArchLower.lean",
    ROOT / "ActualZetaOriginalCollarPoleBound.lean",
    ROOT / "ActualZetaOriginalCollarLiteralArch.lean",
    ROOT / "ActualZetaOriginalCollar242Correction.lean",
    Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
    Path("scripts/iv019_original_width_capacity_kernel_audit.py"),
    Path("scripts/iv015_frozen_collar_exact_log_gap.py"),
    Path("lakefile.toml"),
    Path("lean-toolchain"),
    Path("lake-manifest.json"),
]

def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def frac(x):
    return f"{x.numerator}/{x.denominator}"

def exact_ledger():
    old=Q(1,250)
    radius=Q(1,500)
    new=2*radius
    measure=old+new
    low=10*measure
    gamma_floor=Q(11,10)-Q(67,10)*low
    pole_loss=8*measure
    analytic=gamma_floor-pole_loss
    original_prime_allowance=Q(2,5)
    final=analytic-original_prime_allowance
    assert old==Q(1,250)
    assert new==Q(1,250)
    assert measure==Q(1,125)
    assert low==Q(2,25)
    assert gamma_floor==Q(141,250)
    assert pole_loss==Q(8,125)
    assert analytic==Q(1,2)
    assert final==Q(1,10)
    assert final==Q(7,10)-75*measure
    assert Q(0)<radius<Q(1,375)
    data={
        "schema":"IV020-original-wider-three-cell-real-exact-budget-v1",
        "old_two_true_NF543_strict_collar_measure":frac(old),
        "new_real_interval":"[99/500,101/500]",
        "new_radius":frac(radius),
        "new_measure":frac(new),
        "full_actual_three_cell_measure":frac(measure),
        "low_Fourier_mass_proportion":frac(low),
        "true_signed_Gamma_lower":frac(gamma_floor),
        "two_original_pole_loss":frac(pole_loss),
        "pole_plus_Gamma_remaining":frac(analytic),
        "original_n9_surviving_prime_allowance":frac(original_prime_allowance),
        "target_original_signed_Weil_lower":frac(final),
        "all_components_exact_Fraction":True,
        "original_prime_transfer_must_pass_direct_Lean_kernel":True,
        "Python_preflight_not_Lean_proof":True,
        "unconditional_global_Weil_positivity":False,
        "RH_proved":False,
    }
    LEDGER.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n")
    print("IV020 exact rational source budget PASS: 1/125 union, 2/25 low band, 141/250 original signed Gamma, 8/125 two poles, 1/2 analytic, 2/5 historical n9, proposed 1/10 full original Weil. LEAN PENDING.")
    return data

def source_preflight():
    for mod,up,new in ((M1,OLD1,NEW1),(M2,OLD2,NEW2)):
        s=mod.read_text()
        actual=re.findall(r"^theorem (neutralIV020Wide\w+)",s,re.M)
        assert actual==new,(str(mod),"theorem mismatch",actual,new)
        prints=re.findall(r"^#print axioms (\w+)$",s,re.M)
        assert prints==up+new,(str(mod),"axiom declaration mismatch",prints,up+new)
        assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b",s,re.M)
        assert not re.search(r"\bsorryAx\b",s)
    a=M1.read_text()
    b=M2.read_text()
    for token in (
        "neutralNF543OriginalCollars",
        "neutralIV020WidePhysicalInterval",
        "Real.volume_Icc",
        "neutralNF600Collars_volume",
        "neutralIV020WideThreeCell_volume",
        "integral_mul_norm_le_Lp_mul_Lq",
        "neutralIV020WideThreeCell_L1_sq",
        "neutralIV019OriginalOneTenth_of_prime_and_L1",
        "neutralIV020WideThreeCell_oneTenth_of_primeBound",
    ):
        assert token in a,("missing original physical/source measure",token)
    for token in (
        "neutralIV019WideFrozenConcrete_allIntegerGap",
        "neutralIV019WideSelfActiveGap",
        "neutralIV015FrozenCollar_activeSeparated_of_gap",
        "neutralIV011MixedCorrelation_eq_schwartzIntegral",
        "neutralIV011OriginalMixedPrime_eq_finite",
        "neutralNF600Prime_bound_actual",
        "neutralIV020WideExpandedCorrelation_eq_old_of_threeZeros",
        "neutralIV020WideExpandedPrime_eq_old",
        "neutralIV020WideExpandedPrime_real_bound",
        "neutralIV020WideOriginalOldPlusNew_oneTenth_coercive",
        "neutralIV020WideExistsGenuineNewThreeCellPositiveDirection",
    ):
        assert token in b,("missing real unchanged original n9 prime transfer",token)
    assert "neutralIV017NarrowPhysicalInterval" not in b, "Wider source mistakenly restricted to narrower IV017 interval"
    assert "neutralIV016FrozenConcrete_allIntegerGap" not in b, "Wider source mistakenly reusing old radius numerical gap"
    for p in DEPS:
        if p.name == "lake-manifest.json":
            continue  # Lake generates this AFTER source preflight.
        assert p.is_file(),("Missing physical source dependency",str(p))
    exact_ledger()
    print("IV020 ORIGINAL SOURCE preflight PASS: 18 new original direct Lean candidates + 7 genuine prior strict source anchors. NOT kernel acceptance.")

def parse_axioms(log_path,names):
    data=log_path.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        data,re.I
    ),log_path
    out={}
    for name in names:
        target="'WeilDefect."+name+"'"
        positive=re.findall(re.escape(target)+r" depends on axioms: \[([^\]]*)\]",data,re.S)
        none=re.findall(re.escape(target)+r" does not depend on any axioms",data,re.S)
        assert len(positive)+len(none)==1,(log_path,name,len(positive),len(none))
        axioms=[] if none else [x.strip() for x in positive[0].split(",") if x.strip()]
        assert set(axioms)<=ALLOWED,(name,axioms)
        out[name]=axioms
    return out

def verify():
    source_preflight()
    assert Path("lake-manifest.json").is_file(), "Missing Lake-generated manifest: lake update must run before KERNEL verification"
    object_files=[OLEAN/(m.stem+".olean") for m in (M1,M2)]
    for o in object_files:
        assert o.is_file() and o.stat().st_size>0,("actual direct Lean compiled source object required",str(o))
    ax1=parse_axioms(LOG1,OLD1+NEW1)
    ax2=parse_axioms(LOG2,OLD2+NEW2)
    report={
        "schema":SCHEMA,
        "scope":"Authentic original Zeta23 signed Weil quadratic coercivity 1/10 for all genuine two-collar Schwartz S plus doubled-radius new Schwartz t and v complex; literal NF600 n9 prime source remains, and actual two pole/Gamma terms retained.",
        "original_source_SHA256":{str(p):digest(p) for p in [M1,M2]+DEPS},
        "actual_compiled_original_Lean_oleans_SHA256":{str(o):digest(o) for o in object_files},
        "independent_exact_Fraction_source_budget_SHA256":digest(LEDGER),
        "genuine_source_upstream_anchors":OLD1+OLD2,
        "new_original_Lean_theorems":NEW1+NEW2,
        "strict_standard_Lean_axioms":{**ax1,**ax2},
        "true_original_wider_three_cell_one_tenth_Weil_coercivity_Lean_PASS":True,
        "full_original_n9_prime_transfer_into_wider_cell_Lean_PASS":True,
        "new_nonzero_wider_source_outside_original_collars_Lean_PASS":True,
        "global_Weil_positivity":False,
        "RH":False,
    }
    REPORT.write_text(json.dumps(report,sort_keys=True,indent=2)+"\n")
    print("IV020 REAL ORIGINAL SOURCE KERNEL PASS: wider 1/10 Weil coercivity, 18 new+7 strict upstream standard axioms, authentic n9 kept. Restricted class ONLY, not RH.")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("stage",choices=("preflight","verify"))
    stage=ap.parse_args().stage
    if stage=="preflight":
        source_preflight()
    else:
        verify()
