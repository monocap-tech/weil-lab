#!/usr/bin/env python3
"""NF725 source-bound kernel object handoff across 4 isolated Lean chunk jobs.

Each chunk must have been compiled to a real .olean by the same pinned Lean
toolchain and same Mathlib package lock as this checkout. SHA-256 checks are
recomputed after artifact download, before importing the compiled object.
The only valid axioms are the usual standard Lean axioms. No numerical gate
identity is asserted by these pure Fin 242 partition lemmas.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

STARTS = (0, 8, 16, 24)
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
ROOT = Path("WeilDefect/Arithmetic")
OBJECT_DIR = Path(".lake/build/lib/lean/WeilDefect/Arithmetic")
FINAL = ROOT / "ActualZetaOriginalPhysicalPackedFinCoverage.lean"
OUT = Path("nf725-kernel-object")
NAMESPACE = "WeilDefect."


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def toolchain():
    return {
        "lean_version": subprocess.check_output(
            ["lake", "env", "lean", "--version"], text=True).strip(),
        "toolchain_sha256": digest("lean-toolchain"),
        "lake_manifest_sha256": digest("lake-manifest.json"),
    }


def source(block):
    assert block in STARTS
    return ROOT / f"ActualZetaOriginalPhysicalPackedFinChunk{block:03d}.lean"


def object_name(block):
    assert block in STARTS
    return f"ActualZetaOriginalPhysicalPackedFinChunk{block:03d}.olean"


def one_axiom(log, name):
    matches = re.findall(
        rf"'{re.escape(NAMESPACE+name)}' depends on axioms: \[([^\]]*)\]", log)
    noaxiom = re.findall(
        rf"'{re.escape(NAMESPACE+name)}' does not depend on any axioms", log)
    assert len(matches) + len(noaxiom) == 1, (name, matches, noaxiom)
    got = [x.strip() for x in matches[0].split(",") if x.strip()] if matches else []
    assert set(got) <= ALLOWED, (name, got)
    return got


def stage_chunk(block):
    from nf724_verify_bounded_fin_coverage import source as verify_source
    verify_source()
    log = Path(f"nf725-axioms-{block:03d}.log").read_text()
    name = f"neutralNF724Chunk{block:03d}"
    axioms = one_axiom(log, name)
    o = OBJECT_DIR / object_name(block)
    assert o.is_file() and o.stat().st_size > 1024, o
    assert source(block).is_file()
    OUT.mkdir(parents=True, exist_ok=True)
    local = OUT / o.name
    shutil.copy2(o, local)
    receipt = {
        "schema": "NF725-standalone-8-block-lean-kernel-object-v1",
        "block_start": block,
        "first_coordinate": block * 8,
        "end_coordinate": min((block+8)*8, 242),
        "theorem": name,
        "source_sha256": digest(source(block)),
        "olean_sha256": digest(local),
        "axioms": axioms,
        "compiler": toolchain(),
        "scope": "One Lean-accepted bounded pure-Fin242 partition proof; no global numerical product truth asserted.",
    }
    (OUT / f"nf725-chunk-{block:03d}.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"NF725 pure-Lean chunk {block:03d}, coordinates "
          f"{receipt['first_coordinate']}..{receipt['end_coordinate']-1}: "
          "kernel PASS; standard axioms PASS; versioned .olean SHA pinned")


def stage_assemble(receipts):
    from nf724_verify_bounded_fin_coverage import source as verify_source
    chunks = verify_source()
    assert len(chunks) == 31
    tc = toolchain()
    combined = []
    for block in STARTS:
        artifact = receipts / f"nf725-kernel-chunk-{block:03d}"
        path = artifact / f"nf725-chunk-{block:03d}.json"
        m = json.loads(path.read_text())
        assert m["schema"] == "NF725-standalone-8-block-lean-kernel-object-v1"
        assert m["block_start"] == block
        assert m["first_coordinate"] == block*8
        assert m["end_coordinate"] == min((block+8)*8,242)
        assert m["theorem"] == f"neutralNF724Chunk{block:03d}"
        assert m["compiler"] == tc, (m["compiler"],tc)
        assert m["source_sha256"] == digest(source(block))
        assert set(m["axioms"]) <= ALLOWED
        artifact_obj = artifact / object_name(block)
        assert digest(artifact_obj) == m["olean_sha256"]
        target = OBJECT_DIR / object_name(block)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(artifact_obj, target)
        assert digest(target) == m["olean_sha256"]
        combined.append({"block_start":block,
                         "audit_sha256":digest(path),
                         "object_sha256":m["olean_sha256"],
                         "source_sha256":m["source_sha256"],
                         "theorem":m["theorem"]})
    assert [x["block_start"] for x in combined] == list(STARTS)
    assert sum(min(64, 242 - b*8) for b in STARTS) == 242
    result = {
        "schema": "NF725-reconstructed-pinned-4-chunk-finite-coverage-v1",
        "accepted_lean_chunks": combined,
        "source_sha256": digest(FINAL),
        "pinned_toolchain": tc,
        "coordinates": list(range(242)),
        "numerical_product_certified_by_this_job": False,
        "scope": "Exact source+compiler+olean hashes of four accepted Lean chunks; final Fin242 cover and NF722 attachment require independent Lean acceptance."
    }
    Path("nf725-assembled-chunks.json").write_text(
        json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF725 all four separately kernel-accepted pure arithmetic chunks recovered with exact Lean-version, original source and object fingerprints")


def stage_final():
    from nf724_verify_bounded_fin_coverage import source as verify_source
    verify_source()
    log=Path("nf725-master-axioms.log").read_text()
    name="neutralNF724Fin242OfPackedBlocks"
    axioms=one_axiom(log,name)
    pre=json.loads(Path("nf725-assembled-chunks.json").read_text())
    assert pre["pinned_toolchain"]==toolchain()
    o=OBJECT_DIR/"ActualZetaOriginalPhysicalPackedFinCoverage.olean"
    assert o.is_file() and o.stat().st_size>1024
    result = {
        **pre,
        "schema":"NF725-source-bound-full-Fin242-lean-cover-v1",
        "master_theorem":name,
        "master_axioms":axioms,
        "master_olean_sha256":digest(o),
        "master_source_sha256":digest(FINAL),
        "proof_status":"LEAN KERNEL PASS with exact four independent chunk theorem inputs and accepted standard axiom audit",
        "genuine_original_HD_or_A_row1_gate_claimed":False,
    }
    Path("nf725-complete-audit.json").write_text(
        json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF725 source-bound full 242-coordinate pure Fin cover and 4 component lemmas: 5 actual Lean kernel PASS; 0 new numerical identities")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("stage", choices=("chunk","assemble","final"))
    p.add_argument("--block",type=int,default=None)
    p.add_argument("--receipts",type=Path,default=Path("nf725-receipts"))
    a=p.parse_args()
    if a.stage=="chunk":
        assert a.block in STARTS
        stage_chunk(a.block)
    elif a.stage=="assemble":
        stage_assemble(a.receipts)
    else:
        stage_final()


if __name__=="__main__":
    main()
