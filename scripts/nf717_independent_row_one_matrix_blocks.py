#!/usr/bin/env python3
"""NF717: independently attach NF700 signed-digit blocks 004..007 to index one.

Unlike NF716, this job does *not* depend on NF716's pending completion:
it checks the already accepted NF715 12-theorem source-specific audit,
reconstructs that exact first block and its common projected row/column
from immutable NF702/NF703/NF700 source, and compiles four disjoint further
blocks, 32..63, independently against the same accepted NF700 local products.
"""
import argparse
import json
import re
from pathlib import Path

from emit_nf630_original_literal_payments import filetext
from nf716_second_global_matrix_row_continuation import (
    ALLOWED, WIDTH, OPTIONS, generated_block, reproduce_nf715,
    source_manifest, sha
)

BLOCKS = tuple(range(4, 8))
START, END = 32, 64
SUFFIXES = ("DGate", "DProjection", "HDTargetGate",
            "HDTargetProjection", "ATargetGate", "ATargetProjection",
            "GlobalHD", "GlobalA")
MODULE = "WeilDefect.Generated.NF717"


def theorem_names(block):
    assert block in BLOCKS
    return [f"nf717Block{block:03d}{suffix}" for suffix in SUFFIXES]


def preflight():
    checked = []
    for block in BLOCKS:
        text = generated_block(block, stage="nf717", lower=BLOCKS[0], upper=BLOCKS[-1]+1)
        names = theorem_names(block)
        assert all(f"theorem {name}" in text for name in names)
        assert len(text.split("theorem ")) == 1 + len(names)
        assert f"nf700Block{block:03d}HDAllCoordinates j" in text
        assert f"nf700Block{block:03d}AAllCoordinates j" in text
        assert f"⟨{WIDTH*block} + j.val, by omega⟩" in text
        checked.extend(range(WIDTH*block, WIDTH*(block+1)))
    assert checked == list(range(START, END))
    print("NF717 proof-template design PASS: 4 disjoint accepted local signed-digit blocks, 64 global gates pending Lean")


def prepare(a):
    original, old, accepted_audit_file = reproduce_nf715(a)
    packed = source_manifest(Path("WeilDefect/Generated/NF700"))
    assert packed["schema"] == "NF700-original-packed-second-matrix-frontier-v1"
    assert packed["H_source_row"] == packed["HD_source_column"] == 1
    assert packed["HD_exact_external"] == packed["A_exact_external"] == 242
    assert len(packed["blocks"]) == 31
    assert old["actual_global_HD_gates"] == old["actual_global_A_gates"] == 8
    assert old["first"] == 0 and old["end"] == 8
    a.output.mkdir(parents=True,exist_ok=True)
    names, files, coords = [], [], []
    for block in BLOCKS:
        b = packed["blocks"][block]
        assert b["module"] == f"Block{block:03d}"
        assert (b["start"],b["stop"],b["width"]) == (
            WIDTH*block, WIDTH*(block+1), WIDTH)
        assert {f"nf700Block{block:03d}HDAllCoordinates",
                f"nf700Block{block:03d}AAllCoordinates"} <= set(b["theorems"])
        text = generated_block(block,stage="nf717",lower=BLOCKS[0],upper=BLOCKS[-1]+1)
        ns = theorem_names(block)
        assert all("theorem "+n in text for n in ns)
        text += "\n".join(f"#print axioms {n}" for n in ns)+"\n"
        path = a.output/f"Block{block:03d}.lean"
        path.write_text(filetext([
            "WeilDefect.Generated.NF715.Common",
            f"WeilDefect.Generated.NF700.Block{block:03d}",
        ],OPTIONS+text))
        files.append({"file":path.name,"sha256":sha(path)})
        names.extend(ns)
        coords.extend(range(WIDTH*block,WIDTH*(block+1)))
    assert coords == list(range(START,END))
    assert len(names)==len(set(names))==32
    metadata = {
        "schema":"NF717-independent-original-global-row-one-matrix-attachment-v1",
        "original_index":1, "first":START, "end":END,
        "blocks":list(BLOCKS), "new_HD_gates":32, "new_A_gates":32,
        "coordinates":coords,"audit_theorems":names,"files":files,
        "accepted_nf715_manifest_sha256":sha(original/"manifest.json"),
        "accepted_nf715_audit_sha256":sha(accepted_audit_file),
        "nf700_packed_manifest_sha256":sha(Path("WeilDefect/Generated/NF700/manifest.json")),
        "source_manifests":old["source_manifests"],
        "accepted_source_audits":old["accepted_audits"],
        "scope":"Index-one original global HD/A coordinates 32..63. Independently sourced from accepted NF715 and NF700; no NF716 result presumed; remaining global matrix, vector and payment gates remain open.",
    }
    (a.output/"manifest.json").write_text(json.dumps(metadata,indent=2)+"\n")
    print("NF717 immutable NF715 accepted source and 12-theorem audit PASS; 64 new global product candidates emitted for 32..63, Lean pending")


def axiom_file(a):
    manifest=source_manifest(a.output)
    assert manifest["schema"]=="NF717-independent-original-global-row-one-matrix-attachment-v1"
    assert manifest["audit_theorems"]==[n for b in BLOCKS for n in theorem_names(b)]
    lines=[f"import {MODULE}.Block{b:03d}" for b in BLOCKS]
    lines.extend(f"#print axioms WeilDefect.{n}" for n in manifest["audit_theorems"])
    Path("nf717Audit.lean").write_text("\n".join(lines)+"\n")


def verify(a):
    manifest=source_manifest(a.output)
    assert manifest["blocks"]==list(BLOCKS)
    assert manifest["first"]==START and manifest["end"]==END
    assert manifest["coordinates"]==list(range(START,END))
    assert manifest["new_HD_gates"]==manifest["new_A_gates"]==32
    expected={n for block in BLOCKS for n in theorem_names(block)}
    assert set(manifest["audit_theorems"])==expected
    log=Path("nf717-axioms.log").read_text()
    found={}
    for name,raw in re.findall(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
        if name in expected:
            assert name not in found,name
            found[name]=[x.strip() for x in raw.split(",") if x.strip()]
    for name in re.findall(r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
        if name in expected:
            assert name not in found,name
            found[name]=[]
    assert set(found)==expected,(sorted(expected-set(found)),sorted(set(found)-expected))
    assert len(found)==32
    assert all(set(axioms)<=ALLOWED for axioms in found.values())
    result={
        "schema":"NF717-independent-original-global-row-one-matrix-audit-v1",
        "manifest_sha256":sha(a.output/"manifest.json"),
        "source_audit_sha256":manifest["accepted_nf715_audit_sha256"],
        "axioms":found,
        "row":1,"column":1,"coordinates":list(range(START,END)),
        "HD_gates":32,"A_gates":32,
        "scope":"64 new original global product gates and only these. NF716 status remains independent.",
    }
    Path("nf717-complete-audit.json").write_text(json.dumps(result,indent=2)+"\n")
    print("NF717 64 original global HD/A source-bound gates in blocks 004..007: 32 declarations LEAN PASS")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","prepare","axiom-file","verify"))
    p.add_argument("--receipts",type=Path,default=Path("nf717-receipts"))
    p.add_argument("--prior",type=Path,default=Path("nf717-prior"))
    p.add_argument("--output",type=Path,default=Path("WeilDefect/Generated/NF717"))
    a=p.parse_args()
    {"preflight":lambda _:preflight(),
     "prepare":prepare,
     "axiom-file":axiom_file,
     "verify":verify}[a.stage](a)


if __name__=="__main__":
    main()
