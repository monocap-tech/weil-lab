#!/usr/bin/env python3
"""NF727: strictly audit the exact pure Lean binary finite-index glue.

Source-independent certification is distinct from source-specific original
physical HD/A numerical attachment. Accepted NF726 halves are referenced
through their own immutable kernel receipts, not assumed here.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

SRC = Path("WeilDefect/Arithmetic/ActualZetaOriginalPhysicalFiniteBinaryGluing.lean")
NAME1 = "neutralNF727Fin242OfTwoHalves"
NAME2 = "neutralNF727PairFin242OfTwoHalves"
NAMES = [NAME1, NAME2]
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source():
    s = SRC.read_text()
    assert s.startswith("import Mathlib.Tactic\n")
    assert re.findall(r"^theorem (neutralNF727\w+)",s,re.M) == NAMES
    assert not re.search(r"\b(sorry|admit|axiom|unsafe)\b",s)
    assert "(left : ∀ i : Fin 242, i.val < 128 → P i)" in s
    assert "(right : ∀ i : Fin 242, 128 ≤ i.val → P i)" in s
    assert "right i (Nat.le_of_not_gt h)" in s
    for k in ("hdLeft", "hdRight", "aLeft", "aRight"):
        assert f"({k} : ∀ i : Fin 242," in s
    assert "(∀ i : Fin 242, HD i) ∧ (∀ i : Fin 242, A i)" in s
    assert "#print axioms "+NAME1 in s
    assert "#print axioms "+NAME2 in s
    print("NF727 pure binary Fin242 bridge source: two named theorems and four separate HD/A half premises PASS")
    return {"source_sha256":digest(SRC),"source_length":len(s)}


def verify():
    metadata=source()
    log=Path("nf727-bridge-axioms.log").read_text()
    found={}
    for name,axioms in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
        if name in NAMES:
            assert name not in found
            found[name]=[x.strip() for x in axioms.split(",") if x.strip()]
    for name in re.findall(r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
        if name in NAMES:
            assert name not in found
            found[name]=[]
    assert set(found)==set(NAMES),(set(NAMES)-set(found),set(found)-set(NAMES))
    assert all(set(v)<=ALLOWED for v in found.values())
    result={
        "schema":"NF727-source-independent-2-premise-fin242-HD-A-gluing-v1",
        **metadata,
        "theorems":NAMES,
        "axioms":found,
        "domain":list(range(242)),
        "halves":[{"first":0,"end":128},{"first":128,"end":242}],
        "numerical_original_gate_truth_proved":False,
        "status":"LEAN KERNEL PASS with 2 strict standard-axiom declarations",
        "scope":"Logical two-half composition only. NF726's accepted source-specific finite cover proofs and NF715–NF720's 484 accepted physical index-one gates remain separate. Full actual HD/A universal source attachment requires its own Lean proof."
    }
    Path("nf727-bridge-audit.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF727 Lean binary logical Fin242 HD/A gluing: 2 theorems standard-axiom PASS; original matrix universal attachment still OPEN")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("source","verify"))
    a=p.parse_args()
    source() if a.stage=="source" else verify()
