#!/usr/bin/env python3
"""NF738: strict source and kernel audit of finite local original EF coercivity.

The four original NF736/legacy-NF735 two-generator source-bound theorems passed
Lean in successful original job 136461473716 of run 44786163030, despite that
run's separate pure-moving-support job failing. The immutable original source
audit artifact is 14656510729, and is authenticated by the GitHub workflow.

This audit never substitutes a previous source theorem for the NEW finite
family theorem: both the new actual source module and strict Lean standard
axiom printing must compile separately. Neither asserts global Weil positivity.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

PRIOR=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVLocalSpan.lean")
NEW=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVFiniteLocalSpan.lean")
ACCEPTED=Path("nf738-accepted-original-local-span/nf735-literal-audit.json")
LOG=Path("nf738-finite-local-EF-axioms.log")
OUT=Path("nf738-original-finite-complex-collar-span-kernel-audit.json")
ALLOWED={"propext","Classical.choice","Quot.sound"}
PRIOR_NAMES=[
  "neutralNF735OriginalCollars_add",
  "neutralNF735OriginalCollars_smul",
  "neutralNF735OriginalLocalSpanTwo_coercive",
  "neutralNF735OriginalLocalSpanTwo_nonnegative",
]
NEW_NAMES=[
  "neutralNF738OriginalCollars_finset_linear",
  "neutralNF738OriginalFiniteCollarSpan_coercive",
  "neutralNF738OriginalFiniteCollarSpan_nonnegative",
  "neutralNF738OriginalFiniteCollarSpan_positive",
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source():
    assert PRIOR.is_file() and NEW.is_file() and ACCEPTED.is_file()
    proof=json.loads(ACCEPTED.read_text())
    assert proof["schema"]=="NF735-original-literal-EF-local-span-audit-v1"
    assert proof["source_sha256"]==sha(PRIOR)
    assert set(proof["axioms"])==set(PRIOR_NAMES)
    assert all(set(xs)<=ALLOWED for xs in proof["axioms"].values())
    prior=PRIOR.read_text()
    new=NEW.read_text()
    assert re.findall(r"^theorem (neutralNF735\w+)",prior,re.M)==PRIOR_NAMES
    assert re.findall(r"^theorem (neutralNF738\w+)",new,re.M)==NEW_NAMES
    assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",new,re.M)
    assert new.startswith("import WeilDefect.Arithmetic.ActualZetaPhaseIVLocalSpan\n")
    assert "neutralNF600SmoothCollarLower" in new
    assert "neutralNF735InOriginalCollars" in new
    assert "neutralNF735OriginalCollars_add" in new
    assert "neutralNF735OriginalCollars_smul" in new
    assert new.count("(∑ i ∈ F, c i • s i)")>=4
    assert "neutralNF543OriginalCollars" in prior
    assert "neutralNF598SmoothWeil" in new
    assert "2/5:ℝ" in new
    assert all(f"#print axioms {n}" in new for n in NEW_NAMES)
    print("NF738 SOURCE PASS: immutable accepted NF736 actual original literal signed EF local two-generator Lean result, correct 4 source theorem names, and proposed 4 new arbitrary FINITE complex-collar span theorems. The latter remain KERNEL PENDING.")


def verify():
    source()
    text=LOG.read_text()
    found={}
    for name,raw in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",text):
        if name in NEW_NAMES:
            assert name not in found,name
            found[name]=[x.strip() for x in raw.split(",") if x.strip()]
    for name in re.findall(
       r"'WeilDefect\.(\w+)' does not depend on any axioms",text):
        if name in NEW_NAMES:
            assert name not in found,name
            found[name]=[]
    assert set(found)==set(NEW_NAMES),(
      "Missing actually compiled Lean theorem axioms",set(NEW_NAMES)-set(found))
    assert all(set(xs)<=ALLOWED for xs in found.values()),found
    assert not re.search(r"(?m)^(?:.*(?:error:|##\[error\]))",text,re.I)
    receipt={
      "schema":"NF738-original-literal-EF-arbitrary-finite-complex-collar-span-lean-kernel-v1",
      "accepted_original_NF600_theorem":"neutralNF600SmoothCollarLower",
      "accepted_upstream_original_NF736_legacy_NF735_job":136461473716,
      "accepted_upstream_run":44786163030,
      "accepted_upstream_original_local_span_artifact_id":14656510729,
      "accepted_upstream_original_local_span_source_sha256":sha(PRIOR),
      "accepted_upstream_local_span_receipt_sha256":sha(ACCEPTED),
      "new_source_sha256":sha(NEW),
      "new_theorems":NEW_NAMES,
      "strict_standard_axioms":found,
      "original_literal_EF_window":"11/10",
      "original_fixed_two_collar_support":True,
      "arbitrary_finite_complex_families_inside_original_support":True,
      "nonzero_sum_required_for_strict_positivity":True,
      "support_extension_beyond_original_collars_proved":False,
      "global_mixed_Weil_cross_term_proved":False,
      "arbitrary_support_Weil_positivity_proved":False,
      "RH_proved":False,
      "kernel_status":"NEW four actual original literal signed EF finite-complex-local-span theorems Lean PASS standard axioms only",
      "scope":"Only finite complex superposition in unchanged original fixed collars E. No moving support, new prime window, original full global matrix, global Weil positivity or RH."
    }
    OUT.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("NF738 ACTUAL original literal signed Weil 2/5 coercivity on arbitrary finite complex spans INSIDE fixed E: four Lean theorems KERNEL PASS strict standard axioms. Nonlocal mixed Weil form and RH remain OPEN.")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("source","verify"))
    args=p.parse_args()
    if args.stage=="source":source()
    else:verify()
