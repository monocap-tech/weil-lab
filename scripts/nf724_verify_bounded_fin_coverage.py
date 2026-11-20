#!/usr/bin/env python3
"""NF724: strict Lean axiom/source audit of four bounded Fin 242 chunks.

Does not claim original numerical matrix validity: generic partitioning of
Fin 242 and its stable NF722 source-independent interface are separate from
the original NF723 attachment of 242 HD and 242 A gates.
"""
import hashlib
import json
import re
from pathlib import Path
SRC=Path("WeilDefect/Arithmetic/ActualZetaOriginalPhysicalPackedFinCoverage.lean")
SPLIT=Path("WeilDefect/Arithmetic/ActualZetaOriginalPhysicalPackedRowOneFiniteClosure.lean")
NAMES=[f"neutralNF724Chunk{i:03d}" for i in (0,8,16,24)]+[
    "neutralNF724Fin242OfPackedBlocks"]
ALLOWED={"propext","Classical.choice","Quot.sound"}


def source():
    s = SRC.read_text()
    assert re.findall(r"^theorem (neutralNF724\\w+)", s, re.M) == [
        "neutralNF724Fin242OfPackedBlocks"
    ]
    assert not re.search(r"\\b(sorry|admit|axiom|unsafe)\\b", s)
    assert "exact neutralNF726Half000 P" in s
    assert "exact neutralNF726Half016 P" in s
    blocks = []
    halves = {}
    for half in (0,16):
        name=f"neutralNF726Half{half:03d}"
        hpath=SRC.with_name(
            f"ActualZetaOriginalPhysicalPackedFinHalf{half:03d}.lean")
        h=hpath.read_text()
        assert (f"import WeilDefect.Arithmetic."
                f"ActualZetaOriginalPhysicalPackedFinHalf{half:03d}") in s
        assert re.findall(r"^theorem (neutralNF726\\w+)",h,re.M)==[name]
        assert f"#print axioms {name}" in h
        assert not re.search(r"\\b(sorry|admit|axiom|unsafe)\\b", h)
        halves[half]=h
    for chunk in (0, 8, 16, 24):
        cname = f"neutralNF724Chunk{chunk:03d}"
        path = SRC.with_name(
            f"ActualZetaOriginalPhysicalPackedFinChunk{chunk:03d}.lean")
        local = path.read_text()
        half=0 if chunk<16 else 16
        h=halves[half]
        assert local.startswith("import Mathlib.Tactic\\n")
        assert re.findall(r"^theorem (neutralNF724\\w+)",local,re.M)==[cname]
        assert f"#print axioms {cname}" in local
        assert not re.search(r"\\b(sorry|admit|axiom|unsafe)\\b", local)
        assert (f"import WeilDefect.Arithmetic."
                f"ActualZetaOriginalPhysicalPackedFinChunk{chunk:03d}") in h
        assert f"exact {cname} P" in h
        for b in range(chunk,min(chunk+8,31)):
            first=b*8
            width=min(8,242-first)
            assert width in (2,8)
            term=(f"(⟨{first} + k.val, by omega⟩ : Fin 242)"
                  if first else "(⟨k.val, by omega⟩ : Fin 242)")
            label=f"h{b:03d}"
            expected=f"({label} : ∀ k : Fin {width}, P {term})"
            assert local.count(expected)==1,(b,local.count(expected))
            assert h.count(expected)==1,(b,h.count(expected))
            assert s.count(expected)==1,(b,s.count(expected))
            blocks.append({"index":b,"first":first,"end":first+width,
                           "width":width,"source":str(path),
                           "half":half})
    assert blocks[-1]["end"]==242 and blocks[-1]["width"]==2
    assert sum(x["width"] for x in blocks)==242
    bridge=SPLIT.read_text()
    assert "import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedFinCoverage" in bridge
    assert "exact neutralNF724Fin242OfPackedBlocks P" in bridge
    for b in range(31):
        assert f"    h{b:03d}\\n" in bridge
    return blocks

def audit(logname):
    blocks=source()
    t=Path(logname).read_text()
    matched={}
    for name,raw in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",t):
        if name in NAMES:
            assert name not in matched,name
            matched[name]=[x.strip() for x in raw.split(",") if x.strip()]
    for name in re.findall(
        r"'WeilDefect\.(\w+)' does not depend on any axioms",t):
        if name in NAMES:
            assert name not in matched,name
            matched[name]=[]
    assert set(matched)==set(NAMES),sorted(set(NAMES)-set(matched))
    assert all(set(x)<=ALLOWED for x in matched.values())
    result={
        "schema":"NF724-4-bounded-fin242-packing-lean-audit-v1",
        "source_sha256":hashlib.sha256(SRC.read_bytes()).hexdigest(),
        "original_glue_source_sha256":hashlib.sha256(SPLIT.read_bytes()).hexdigest(),
        "axioms":matched,
        "theorems":NAMES,
        "blocks":blocks,
        "coordinates":list(range(242)),
        "original_numerical_gates_asserted":False,
        "scope":"Four generic bounded partition lemmas and Fin242 full cover only. Complete original row-one source attachment NF723 separately requires kernel and source provenance audits."
    }
    Path("nf724-axiom-audit.json").write_text(
        json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF724 four bounded and one global Fin242 source-independent coverage theorem LEAN PASS; authentic original numerical row theorem remains separate")


if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("source","audit"))
    p.add_argument("--log",default="nf724-axioms.log")
    a=p.parse_args()
    if a.stage=="source":
        blocks=source()
        print(f"NF724 exact {len(blocks)} original Fin242 coordinate blocks and 4 independent chunks: SOURCE PREFLIGHT PASS; kernel pending")
    else:
        audit(a.log)
