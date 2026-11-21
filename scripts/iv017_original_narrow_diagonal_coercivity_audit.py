#!/usr/bin/env python3
"""IV017: source-bound true original 19/20 new-diagonal coercivity audit.

Two new genuine zeta / Mathlib physical Schwartz modules:
  (1) exact width-1/500 L1 Fourier density and low-band 1/50,
      unconditional SIGNED real digamma Gamma >= 483/500 mass;
  (2) unchanged original two-pole moment norm <= 2/125 mass,
      original full Gamma Fourier transport, true prime diagonal=0
      and proposed signed original diagonal >= 19/20 mass.

The full source must be KERNEL COMPILED with standard axiom receipts.
The arithmetic constant pilot/preflight cannot imply Lean acceptance;
the old/new mixed Schur inequality remains a separate unproved source
estimate. Failure at any upstream import also fails this audit.
"""
import argparse
import hashlib
import json
import re
from fractions import Fraction as Q
from pathlib import Path

MODULE_A=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowSignedGamma.lean")
MODULE_B=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowDiagonalCoercivity.lean")
OLEAN_ROOT=Path(".lake/build/lib/lean/WeilDefect/Arithmetic")
LOG_A=Path("iv017-original-narrow-signed-gamma-axioms.log")
LOG_B=Path("iv017-original-narrow-diagonal-coercivity-axioms.log")
PILOT=Path("iv017-original-narrow-coercivity-exact-rational-preflight.json")
RESULT=Path("iv017-original-narrow-coercivity-kernel-audit.json")

# Only `lake update` generates this dependency lock; bind it after setup.
MANIFEST=Path("lake-manifest.json")
SOURCE_DEPS=[
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalConcreteGapPrimeFreeDiagonal.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNonzeroPrimeFreeSchwartzBump.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalTwoCollarPrimeFreeBump.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalActivePrimeSupportGeometry.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteLocalSpan.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarFourierMass.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarGammaLower.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarArchLower.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarPoleBound.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarLiteralArch.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaCorrelationPoles.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollar242Correction.lean"),
    Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
    Path("lean-toolchain"),
]
UPSTREAM_A=[
    "neutralNF599GammaLower",
    "neutralNF599GammaHigh",
    "neutralNF600Density_mass",
    "neutralNF600Arch_integrable",
]
NEW_A=[
    "neutralIV017NarrowPhysicalInterval_volume",
    "neutralIV017Narrow_support_from_bump",
    "neutralIV017NarrowL1_bound",
    "neutralIV017NarrowL1_sq_le",
    "neutralIV017Density_le_L1_sq",
    "neutralIV017LowMass_le_tenL1_sq",
    "neutralIV017NarrowLowMass_le",
    "neutralIV017SignedGamma_lower",
    "neutralIV017NarrowGamma_coercive",
]
UPSTREAM_B=[
    "neutralIV016FrozenSmallBump_selfPrime_zero",
    "neutralIV012OriginalMixedPole_norm_le_momentBudget",
    "neutralNF573WindowEvaluation_eq_raw_of_ae",
    "neutralIV017NarrowGamma_coercive",
]
NEW_B=[
    "neutralIV017OriginalWindowMoment_bound",
    "neutralIV017OriginalPole_norm_le_eightL1_sq",
    "neutralIV017NarrowPole_real_lower",
    "neutralIV017OriginalWindowCorrelation_spectral",
    "neutralIV017OriginalWindowArch_real_eq_spectral",
    "neutralIV017NarrowOriginalDiagonal_coercive",
    "neutralIV017ExistsNonzeroNewSource_diagonalNonnegative",
    "neutralIV017OneNewSource_nonnegative_of_singleResidualBound",
]
ALL_NEW=NEW_A+NEW_B
ALLOWED={"propext","Classical.choice","Quot.sound"}
SCHEMA="IV017-original-zeta-narrow-Schwartz-19over20-signed-diagonal-kernel-v1"


def sha(p:Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def exact_rational_preflight():
    width=Q(201,1000)-Q(199,1000)
    low_band_length=Q(10)
    low_mass_factor=width*low_band_length
    global_gamma_floor=-Q(28,5)
    high_gamma_floor=Q(11,10)
    gamma_penalty=high_gamma_floor-global_gamma_floor
    signed_gamma_lower=high_gamma_floor-gamma_penalty*low_mass_factor
    two_pole_loss=Q(8)*width
    final_lower=signed_gamma_lower-two_pole_loss
    assert width==Q(1,500)
    assert low_mass_factor==Q(1,50)
    assert gamma_penalty==Q(67,10)
    assert signed_gamma_lower==Q(483,500)
    assert two_pole_loss==Q(2,125)
    assert final_lower==Q(19,20)
    assert final_lower>0
    obj={
        "schema":"IV017-source-mass-width-and-signed-gamma-exact-rational-check-v1",
        "real_physical_interval":["199/1000","201/1000"],
        "original_support_width":str(width),
        "fourier_low_band_length":str(low_band_length),
        "fourier_low_band_mass_ratio":str(low_mass_factor),
        "true_symbol_gamma_lower_low":str(global_gamma_floor),
        "true_symbol_gamma_lower_high":str(high_gamma_floor),
        "exact_symbol_loss":str(gamma_penalty),
        "signed_gamma_mass_lower":str(signed_gamma_lower),
        "two_original_pole_mass_loss":str(two_pole_loss),
        "true_original_prime_diagonal_assumed_zero_by_IV016_source":True,
        "candidate_original_signed_diagonal_mass_lower":str(final_lower),
        "not_a_Lean_kernel_audit":True,
        "original_mixed_schur_bound_proved":False,
        "original_full_support_Weil_positivity_proved":False,
        "RH_proved":False,
    }
    PILOT.write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n")
    print("IV017 exact Fraction arithmetic 1/500,1/50,483/500,2/125,19/20 PASS — source math only, LEAN PENDING")
    return obj


def source_preflight():
    raw_a=MODULE_A.read_text()
    raw_b=MODULE_B.read_text()
    assert re.findall(r"^theorem (neutralIV017\w+)",raw_a,re.M)==NEW_A
    assert re.findall(r"^theorem (neutralIV017\w+)",raw_b,re.M)==NEW_B
    assert re.findall(r"^#print axioms (\w+)$",raw_a,re.M)==UPSTREAM_A+NEW_A
    assert re.findall(r"^#print axioms (\w+)$",raw_b,re.M)==UPSTREAM_B+NEW_B
    for raw in (raw_a,raw_b):
        assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b",raw,re.M)
        assert not re.search(r"\b(?:sorry|sorryAx)\b",raw)
    for marker in (
       "Real.volume_Icc","neutralNF600Mass_eq_integral",
       "integral_mul_norm_le_Lp_mul_Lq",
       "SchwartzMap.norm_fourier_apply_le_toLp_one",
       "neutralNF599GammaHigh","neutralNF599GammaLower",
       "neutralNF600HighFrequency",
       "neutralIV017NarrowLowMass_le",
       "neutralIV017NarrowGamma_coercive",
    ):
        assert marker in raw_a,("missing real narrow Fourier/Gamma source",marker)
    for marker in (
       "neutralIV017OriginalWindowMoment_bound",
       "neutralIV012OriginalMixedPole_norm_le_momentBudget",
       "neutralIV006Schwartz_window_ae",
       "neutralRawTransform_fourier",
       "neutralIV017OriginalWindowArch_real_eq_spectral",
       "neutralIV016FrozenSmallBump_selfPrime_zero",
       "neutralIV017NarrowOriginalDiagonal_coercive",
       "neutralIV017OneNewSource_nonnegative_of_singleResidualBound",
       "neutralIV010OriginalOneNewSource_nonnegative_of_crossBound",
    ):
        assert marker in raw_b,("missing real original pole/Gamma/Schur source",marker)
    for p in SOURCE_DEPS:
        assert p.is_file(),("missing original dependency",p)
    exact_rational_preflight()
    print("IV017 original source preflight PASS: 17 new original pole/Gamma signed physical source candidates and 8 upstream axioms, NOT kernel certification")


def verify_log(p:Path, names):
    log=p.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        log,re.I)
    receipts={}
    for name in names:
        q="'WeilDefect."+name+"'"
        yes=re.findall(re.escape(q)+r" depends on axioms: \[([^\]]*)\]",log,re.S)
        no=re.findall(re.escape(q)+r" does not depend on any axioms",log,re.S)
        assert len(yes)+len(no)==1,(name,len(yes),len(no))
        axioms=[] if no else [v.strip() for v in yes[0].split(",") if v.strip()]
        assert set(axioms)<=ALLOWED,(name,axioms)
        receipts[name]=axioms
    return receipts


def kernel_verify():
    source_preflight()
    assert MANIFEST.is_file(), ("Missing generated Lake manifest after update", str(MANIFEST))
    oleans=[OLEAN_ROOT/(p.stem+".olean") for p in (MODULE_A,MODULE_B)]
    for o in oleans:
        assert o.is_file() and o.stat().st_size>0,("real Lean compiled object absent",o)
    a=verify_log(LOG_A,UPSTREAM_A+NEW_A)
    b=verify_log(LOG_B,UPSTREAM_B+NEW_B)
    out={
        "schema":SCHEMA,
        "scope":"Genuine narrow complex Schwartz original source L1/Plancherel, signed gamma lower and true two-pole coercivity; original vonMangoldt self-prime 0 via IV016.",
        "source_sha256":{str(p):sha(p) for p in [MODULE_A,MODULE_B]+SOURCE_DEPS+[MANIFEST]},
        "source_exact_Fraction_preflight_sha256":sha(PILOT),
        "real_compiled_original_Lean_object_sha256":{str(p):sha(p) for p in oleans},
        "new_IV017_Lean_theorems":ALL_NEW,
        "original_Lean_source_anchors":UPSTREAM_A+UPSTREAM_B,
        "standard_axioms_only":{**a,**b},
        "new_narrow_original_source_diagonal_mass_lower_19over20_Lean_PASS":True,
        "original_primal_Weil_zero_side_RH_proved":False,
        "mixed_old_new_pole_Gamma_Schur_residual_proved":False,
        "global_Weil_positivity_proved":False,
    }
    RESULT.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print("IV017 REAL ORIGINAL LEAN KERNEL PASS: signed 19/20 narrow physical diagonal coercivity, 17 new + 8 upstream standard axioms; mixed Schur still OPEN.")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","verify"))
    if p.parse_args().stage=="preflight":
        source_preflight()
    else:
        kernel_verify()
