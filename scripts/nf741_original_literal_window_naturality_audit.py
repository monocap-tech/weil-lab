#!/usr/bin/env python3
"""NF741 strict ORIGINAL source-specific literal Weil mixed-window audit.

Run only AFTER real Lean kernel build AND direct #print axioms source replay.
No global positivity assumption. The upstream actual NF533/NF534/NF573
definitions are reimported and explicitly independently axiom-audited.

The accepted physical source and theorem name hashes are recorded, but
no immutable CI artifact acceptance is claimed before audit() succeeds.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

LEAN=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.lean")
OLEAN=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVWindowNaturality.olean")
LOG=Path("nf741-original-mixed-window-axioms.log")
OUT=Path("nf741-original-mixed-window-naturality-kernel-audit.json")
ALLOWED={"propext","Classical.choice","Quot.sound"}
UPSTREAM=[
 "neutralNF573WindowEvaluation_eq_raw_of_ae",
 "neutralWindowCorrelation_eq_realBilinearConvolution",
 "neutralActualZetaWindowCorrelation_literature_of_contDiff",
]
NEW=[
 "neutralNF741Schwartz_window_ae",
 "neutralNF741Schwartz_support_expand",
 "neutralNF741WindowEvaluation_eq_of_support",
 "neutralNF741WindowReflection_ae",
 "neutralNF741WindowCorrelation_eq_of_support",
 "neutralNF741LiteralMixedEF_eq_of_support",
 "neutralNF741MixedDivisorSum_eq_of_support",
 "neutralNF741LiteralMixedEF_natural",
 "neutralNF741LiteralDiagonalWeil_natural",
]
NAMES=UPSTREAM+NEW
SOURCE_DEPS=[
 Path("WeilDefect/Arithmetic/ActualZetaOriginalRealOddSchwartzFullSource.lean"),
 Path("WeilDefect/Arithmetic/ActualZetaSmoothCorrelationRegularity.lean"),
 Path("WeilDefect/Arithmetic/ActualZetaSmoothLiteralFormulaAutomatic.lean"),
 Path("WeilDefect/Arithmetic/ActualZetaOriginalSignedGraphForm.lean")
]

def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def preflight():
    raw=LEAN.read_text()
    assert "neutralWindowCorrelation a" in raw and "neutralWindowCorrelation b" in raw
    assert "Zeta23.EF.literatureRHS" in raw
    assert "neutralWindowEvaluation" in raw and "NeutralActualZetaDivisorCoordinate" in raw
    assert "convolution_congr" in raw and "Measure.map_neg_eq_self" in raw
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b",raw,re.M)
    asserted=re.findall(r"^#print axioms (\w+)$",raw,re.M)
    assert asserted==NAMES,(asserted,NAMES)
    theorem_names=re.findall(r"^theorem (neutralNF741\w+)",raw,re.M)
    assert theorem_names==NEW,(theorem_names,NEW)
    for p in SOURCE_DEPS:
        assert p.is_file(),p
    print("NF741 exact original signed Weil window/EF source identities present; nine new theorem candidates and three authentic upstream axiom receipts prepared. LEAN KERNEL STILL PENDING.")

def verify():
    preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size>0, "Missing real compiled Lean output"
    raw=LOG.read_text()
    assert not re.search(r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",raw,re.I), "Lean error/sorry is forbidden"
    found={}
    for name in NAMES:
        key="'WeilDefect."+name+"'"
        parts=re.findall(re.escape(key)+r" depends on axioms: \[([^\]]*)\]",raw,re.S)
        none=re.findall(re.escape(key)+r" does not depend on any axioms",raw,re.S)
        assert len(parts)+len(none)==1,(name,len(parts),len(none))
        axs=[] if none else [v.strip() for v in parts[0].split(",") if v.strip()]
        assert set(axs)<=ALLOWED,(name,axs)
        found[name]=axs
    source_hashes={str(p):digest(p) for p in [LEAN]+SOURCE_DEPS}
    out={
      "schema":"NF741-original-genuine-two-argument-window-naturality-kernel-v1",
      "scope":"Exact literal Weil EF and full-divisor series naturality for arbitrary two compact-window complex Schwartz tests. No cross-support PSD or RH.",
      "source_sha256":source_hashes,
      "compiled_olean_sha256":digest(OLEAN),
      "original_source_anchors":UPSTREAM,
      "new_source_theorems":NEW,
      "axioms":found,
      "new_original_Weil_support_domain_extended":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("NF741 ORIGINAL genuine mixed EF window naturality: 9 NEW LEAN KERNEL PASS, three existing source anchors standard-axiom audited, full artifact hashes bound. NO positivity claim.")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","verify"))
    a=p.parse_args()
    if a.stage=="preflight":preflight()
    else:verify()
