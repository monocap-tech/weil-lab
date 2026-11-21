#!/usr/bin/env python3
"""IV015 strict true ORIGINAL two-collar nonzero Schwartz witness kernel audit.

TWO real Lean modules, genuine .olean objects, every #print axioms, full
source/SHA custody. A prior independent Python exact-rational certificate
for c=1/5, r=1/1000, N=10 is NOT a Lean proof of the finite log gap.

The true frozen NF543 collars, original von-Mangoldt mixed prime side,
full original pole+Gamma remainder, and physical finite superposition
are preserved. No kernel acceptance from source preflight or Python.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

ONE=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNonzeroPrimeFreeSchwartzBump.lean")
TWO=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalTwoCollarPrimeFreeBump.lean")
ROOT=Path(".lake/build/lib/lean/WeilDefect/Arithmetic")
LOG_ONE=Path("iv015-nonzero-schwartz-bump-axioms.log")
LOG_TWO=Path("iv015-original-two-collar-bump-axioms.log")
GAP=Path("iv015-frozen-collar-exact-rational-log-gap.json")
OUT=Path("iv015-original-two-collar-nonzero-schwartz-kernel-audit.json")
ALLOWED={"propext","Classical.choice","Quot.sound"}

UP_ONE=[
    "neutralIV014ActiveSeparated_of_intervalGap",
    "neutralIV014ActiveMixedPrime_zero",
    "neutralIV014ActiveMixed_eq_analytic",
    "neutralIV009PhysicalSchwartzSum_supported",
]
NEW_ONE=[
    "neutralIV015ExistsComplexSchwartzBump",
    "neutralIV015Bump_supported_largeWindow",
    "neutralIV015Bump_not_oldPhysicalSpan",
    "neutralIV015ExistsUniformActivePrimeSeparatedBump",
    "neutralIV015ExistsOriginalPrimeFreeNewPhysicalDirection",
]
UP_TWO=[
    "neutralIV015ExistsComplexSchwartzBump",
    "neutralNF738OriginalCollars_finset_linear",
    "neutralIV014ActiveMixedPrime_zero",
    "neutralIV014ActiveMixed_eq_analytic",
]
NEW_TWO=[
    "neutralIV015FrozenCollars_in_centerIntervals",
    "neutralIV015PhysicalIntervalTranslate_excluded",
    "neutralIV015FrozenCollar_activeSeparated_of_gap",
    "neutralIV015ExistsNonzeroNewTwoCollarPrimeSeparatedBump",
    "neutralIV015ExistsOriginalTwoCollarPrimeFreeDirection",
    "neutralIV015FrozenConcrete_logCutoff",
    "neutralIV015FrozenConcrete_centerOutside",
    "neutralIV015FrozenConcrete_originalPrimeFreeBump_of_gap",
]
ALL_NEW=NEW_ONE+NEW_TWO
SRC_DEPS=[
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalActivePrimeSupportGeometry.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteLocalSpan.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVLocalSpan.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollar242Correction.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeGeometry.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaCorrelationPoles.lean"),
    Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
    Path("scripts/iv015_frozen_collar_exact_log_gap.py"),
    Path("lean-toolchain"),
    Path("lake-manifest.json"),
]

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def check_source(src, up, new):
    raw=src.read_text()
    assert "import Mathlib" in raw,("Mathlib original physical Schwartz not imported",str(src))
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b",raw,re.M),src
    assert not re.search(r"\b(?:sorry|sorryAx)\b",raw),src
    decl=re.findall(r"^theorem (neutralIV015\w+)",raw,re.M)
    assert decl==new,(str(src),decl,new)
    expected=up+new
    actual=re.findall(r"^#print axioms (\w+)$",raw,re.M)
    assert actual==expected,(str(src),actual,expected)

def preflight():
    check_source(ONE,UP_ONE,NEW_ONE)
    check_source(TWO,UP_TWO,NEW_TWO)
    s=ONE.read_text()+TWO.read_text()
    for marker in (
        "exists_contDiff_tsupport_subset",
        "Complex.ofRealCLM",
        "HasCompactSupport",
        "toSchwartzMap",
        "neutralIV015FrozenCollars_in_centerIntervals",
        "neutralIV015FrozenTwoCollarActiveGap",
        "neutralNF543OriginalCollars",
        "neutralNF735InOriginalCollars",
        "neutralNF738OriginalCollars_finset_linear",
        "neutralIV014ActiveMixedPrime_zero",
        "neutralIV014ActiveMixed_eq_analytic",
        "Real.log_ten_eq",
        "Real.log_two_gt_d9",
        "Real.log_five_gt_d9",
        "neutralIV015FrozenConcrete_originalPrimeFreeBump_of_gap",
    ):
        assert marker in s,("Missing true original physical / arithmetic marker",marker)
    for path in SRC_DEPS:
        assert path.is_file(),path
    print("IV015 source preflight PASS: 13 nonzero true complex Schwartz / original frozen two-collar Lean proof candidates, 2 separate direct kernel modules, explicit original exact numeric gap leaf. KERNEL PENDING.")

def audit_log(log,names):
    raw=log.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",raw,re.I
    ),log
    result={}
    for name in names:
        q="'WeilDefect."+name+"'"
        yes=re.findall(re.escape(q)+r" depends on axioms: \[([^\]]*)\]",raw,re.S)
        no=re.findall(re.escape(q)+r" does not depend on any axioms",raw,re.S)
        assert len(yes)+len(no)==1,(log,name,len(yes),len(no))
        axs=[] if no else [a.strip() for a in yes[0].split(",") if a.strip()]
        assert set(axs)<=ALLOWED,(name,axs)
        result[name]=axs
    return result

def verify():
    preflight()
    for src in (ONE,TWO):
        o=ROOT/(src.stem+".olean")
        assert o.is_file() and o.stat().st_size>0,(
            "Actual original compiled .olean object missing",str(o))
    assert GAP.is_file(),"Independent exact Fraction literal NF543 collar geometry receipt missing"
    gap=json.loads(GAP.read_text())
    assert gap["schema"]=="IV015-actual-original-NF543-collar-exact-rational-analytic-gap-v1"
    assert gap["all_original_integer_support_shift_geometric_inequalities_exact_rational_pass"] is True
    assert gap["original_log_cutoff_exact_rational_pass"] is True
    assert gap["source_only_numeric_rational_proof_not_Lean_kernel"] is True
    assert gap["exact_fraction_input"]["candidate_center"]=="1/5"
    assert gap["exact_fraction_input"]["candidate_outer_radius"]=="1/1000"
    assert gap["exact_fraction_input"]["cutoff_N"]==10
    assert gap["certified_lower_strict_log_gap"]!="0/1"

    a=audit_log(LOG_ONE,UP_ONE+NEW_ONE)
    b=audit_log(LOG_TWO,UP_TWO+NEW_TWO)
    report={
        "schema":"IV015-genuine-nonzero-original-two-collar-Schwartz-bump-kernel-v1",
        "scope":"Two true original Mathlib complex Schwartz compact bump and unchanged NF543/NF600 two-collar source, arithmetic-active prime separation, exact mixed prime-free EF, and explicit concrete N10 original gap outstanding as Lean numeric leaf.",
        "source_sha256":{str(p):digest(p) for p in (ONE,TWO,*SRC_DEPS)},
        "compiled_oleans_sha256":{
            str(ROOT/(p.stem+".olean")):digest(ROOT/(p.stem+".olean"))
            for p in (ONE,TWO)
        },
        "exact_rational_geometry_receipt_sha256":digest(GAP),
        "module_one_source_standard_axioms":a,
        "module_two_source_standard_axioms":b,
        "thirteen_new_Lean_proof_candidates":ALL_NEW,
        "new_Schwartz_bump_exists_for_positive_interval_radius":True,
        "new_original_two_collar_bump_exists_conditional_on_finite_gap":True,
        "finite_explicit_N10_gap_discharged_inside_Lean":False,
        "exact_logarithmic_N10_cutoff_inside_Lean":True,
        "original_new_support_diagonal_nonnegative_established":False,
        "original_pole_Gamma_residual_bound_sufficient_for_Schur_established":False,
        "global_Weil_positivity_proved":False,
        "RH_proved":False,
    }
    OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print("IV015 ORIGINAL COMPLEX SCHWARTZ/TWO-COLLAR SOURCE KERNEL PASS: 13 new proof declarations + standard upstream axiom receipts; concrete finite log gap still an EXPLICIT Lean hypothesis, independently exact-rational certified.")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","verify"))
    if p.parse_args().stage=="preflight":preflight()
    else:verify()
