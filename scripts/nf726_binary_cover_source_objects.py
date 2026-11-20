#!/usr/bin/env python3
"""NF726: binary Fin 242 Lean kernel aggregation with original accepted NF725 chunks.

Each half depends on two independently accepted, exact .olean source witnesses.
A separate final job compiles the 31-binder master after authenticating both
new half-object checksums and their original 4 accepted chunk receipt hashes.
Only generic exact index coverage is asserted; no matrix gate validity.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path
from nf724_verify_bounded_fin_coverage import source as source_check

ROOT = Path("WeilDefect/Arithmetic")
BUILD = Path(".lake/build/lib/lean/WeilDefect/Arithmetic")
ALLOWED = {"propext","Classical.choice","Quot.sound"}
HALVES = (0,16)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def toolchain():
    return {
      "lean_version": subprocess.check_output(["lake","env","lean","--version"],text=True).strip(),
      "toolchain_sha256":sha("lean-toolchain"),
      "lake_manifest_sha256":sha("lake-manifest.json"),
    }


def one_axioms(path, name):
    log=Path(path).read_text()
    results=re.findall(
       rf"'WeilDefect\.{re.escape(name)}' depends on axioms: \[([^\]]*)\]",log)
    none=re.findall(
       rf"'WeilDefect\.{re.escape(name)}' does not depend on any axioms",log)
    assert len(results)+len(none)==1,(path,name,results,none)
    got=[x.strip() for x in results[0].split(",") if x.strip()] if results else []
    assert set(got)<=ALLOWED,(name,got)
    return got


def half_source(index):
    assert index in HALVES
    return ROOT/f"ActualZetaOriginalPhysicalPackedFinHalf{index:03d}.lean"


def half_object(index):
    assert index in HALVES
    return BUILD/f"ActualZetaOriginalPhysicalPackedFinHalf{index:03d}.olean"


def half(index):
    blocks=source_check()
    assert len(blocks)==31
    source=half_source(index)
    target=half_object(index)
    assert target.is_file() and target.stat().st_size>1024
    chunks=json.loads(Path("nf725-assembled-chunks.json").read_text())
    assert chunks["schema"]=="NF725-reconstructed-pinned-4-chunk-finite-coverage-v1"
    assert chunks["pinned_toolchain"]==toolchain()
    assert [z["block_start"] for z in chunks["accepted_lean_chunks"]]==[0,8,16,24]
    for z in chunks["accepted_lean_chunks"]:
        p=ROOT/f"ActualZetaOriginalPhysicalPackedFinChunk{z['block_start']:03d}.lean"
        assert sha(p)==z["source_sha256"]
    attestations=[z for z in chunks["accepted_lean_chunks"]
                  if index <= z["block_start"] < index+16]
    assert len(attestations)==2
    name=f"neutralNF726Half{index:03d}"
    axioms=one_axioms(f"nf726-half-{index:03d}-axioms.log",name)
    receipt={
      "schema":"NF726-source-bound-pinned-half-olean-v1",
      "half_block":index,
      "first_coordinate":index*8,
      "end_coordinate":min((index+16)*8,242),
      "theorem":name,
      "axioms":axioms,
      "source_sha256":sha(source),
      "olean_sha256":sha(target),
      "source_type":"Fin 242 pure arithmetic",
      "accepted_original_four_chunk_receipt_sha256":sha("nf725-assembled-chunks.json"),
      "accepted_original_four_chunk_fingerprints":chunks["accepted_lean_chunks"],
      "compiler":toolchain(),
      "numerical_products_asserted":False,
    }
    out=Path(f"nf726-half-{index:03d}")
    out.mkdir(exist_ok=True)
    shutil.copy2(target,out/target.name)
    (out/f"nf726-half-{index:03d}.json").write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print(f"NF726 independently compiled exact two-chunk half {index:03d} original coordinates [{receipt['first_coordinate']},{receipt['end_coordinate']}) LEAN PASS, standard axiom PASS, compiler and source SHA pinned")


def assemble(root):
    blocks=source_check()
    assert len(blocks)==31
    receipts=[]
    for index in HALVES:
        src=half_source(index)
        folder=root/f"nf726-source-bound-half-{index:03d}"
        manifest=folder/f"nf726-half-{index:03d}.json"
        data=json.loads(manifest.read_text())
        assert data["schema"]=="NF726-source-bound-pinned-half-olean-v1"
        assert data["half_block"]==index
        assert data["first_coordinate"]==index*8
        assert data["end_coordinate"]==min((index+16)*8,242)
        assert data["theorem"]==f"neutralNF726Half{index:03d}"
        assert set(data["axioms"])<=ALLOWED
        assert data["compiler"]==toolchain()
        assert data["source_sha256"]==sha(src)
        assert data["numerical_products_asserted"] is False
        original= data["accepted_original_four_chunk_fingerprints"]
        assert [z["block_start"] for z in original]==[0,8,16,24]
        for z in original:
            assert z["source_sha256"]==sha(
                ROOT/f"ActualZetaOriginalPhysicalPackedFinChunk{z['block_start']:03d}.lean")
        o=folder/f"ActualZetaOriginalPhysicalPackedFinHalf{index:03d}.olean"
        assert sha(o)==data["olean_sha256"]
        target=half_object(index)
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(o,target)
        assert sha(target)==data["olean_sha256"]
        receipts.append({"half":index,"manifest_sha256":sha(manifest),
                         "source_sha256":sha(src),"olean_sha256":sha(target),
                         "accepted_original_chunks":original})
    assert (receipts[0]["accepted_original_chunks"] ==
            receipts[1]["accepted_original_chunks"])
    result={
        "schema":"NF726-two-pinned-halves-exact-242-cover-source-binding-v1",
        "half_certificates":receipts,
        "whole_original_coordinate_domain":list(range(242)),
        "master_source_sha256":sha(ROOT/"ActualZetaOriginalPhysicalPackedFinCoverage.lean"),
        "compiler":toolchain(),
        "original_matrix_gates_proved_by_binary_cover":False,
    }
    Path("nf726-assembled-halves.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF726 two authenticated Lean half object receipts cover original Fin242; final original finite-cover Lean theorem PENDING")


def master():
    source_check()
    data=json.loads(Path("nf726-assembled-halves.json").read_text())
    assert data["compiler"]==toolchain()
    assert data["master_source_sha256"]==sha(
       ROOT/"ActualZetaOriginalPhysicalPackedFinCoverage.lean")
    name="neutralNF724Fin242OfPackedBlocks"
    got=one_axioms("nf726-master-axioms.log",name)
    o=BUILD/"ActualZetaOriginalPhysicalPackedFinCoverage.olean"
    assert o.is_file() and o.stat().st_size>1024
    result={
      **data,
      "schema":"NF726-full-Fin242-original-packed-finite-kernel-audit-v1",
      "master_theorem":name,
      "axioms":got,
      "master_olean_sha256":sha(o),
      "status":"LEAN PASS, exact source/object/compiler crosscheck PASS, standard axiom PASS",
      "original_242_HD_and_A_gate_custody": "separate NF715-NF723; NOT established by this generic finite-cover theorem",
    }
    Path("nf726-full-cover-audit.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF726 complete original 242-coordinate pure Lean Fin covering theorem PASS with two independently checked half kernels")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("action",choices=("half","assemble","master"))
    p.add_argument("--half",type=int)
    p.add_argument("--receipts",type=Path,default=Path("nf726-receipts"))
    a=p.parse_args()
    if a.action=="half":
        assert a.half in HALVES
        half(a.half)
    elif a.action=="assemble":
        assemble(a.receipts)
    else:
        master()
