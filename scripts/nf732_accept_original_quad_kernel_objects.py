#!/usr/bin/env python3
"""NF732: source-bound, memory- and disk-bounded Lean object handoff.

Upstream NF729 has eight independently kernel-certified genuine original
numerical quad declarations (each contains HD and A range propositions).
Immutable successful job identity and artifact names are checked in GitHub
Actions BEFORE download. Because one accepted numerical bundle is ~321MB
compressed, ingest one download at a time, keep only compatible .olean modules
and its small receipt, and discard the extracted artifact before the next
download. This avoids simultaneous storage of eight large original banks.

Never promote source-only candidates to kernel truth: require original source
SHA, standard-axiom audit and actual compiled object for each numerical quad.
No incompatible reused compiled module is silently overwritten.
"""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

STARTS=(0,4,8,12,16,20,24,28)
ALLOWED={"propext","Classical.choice","Quot.sound"}
SOURCE=Path("WeilDefect/Generated/NF729")
BUILD=Path(".lake/build/lib/lean/WeilDefect")
RECEIPTS=Path("nf732-authenticated-original-quad-receipts")
EXPECTED_NAME=lambda b:f"nf729-real-original-HD-A-quad-{b:03d}-source-bound-kernel-audit"

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def unique(root,name):
    found=list(Path(root).rglob(name))
    assert len(found)==1,(root,name,found)
    return found[0]

def source_manifest():
    m=json.loads((SOURCE/"manifest.json").read_text())
    assert m["schema"]=="NF729-original-global-index-one-8-quads-source-custody-v1"
    assert m["accepted_index_one_global_product_declarations"]==252
    assert m["files"]=={name:sha(SOURCE/name) for name in m["files"]}
    assert [q["first_block"] for q in m["quads"]]==list(STARTS)
    assert [i for q in m["quads"]
       for i in range(q["first_coordinate"],q["end_coordinate"])]==list(range(242))
    return m

def ingest_one(b,root):
    assert b in STARTS
    m=source_manifest()
    root=Path(root)
    assert root.is_dir()
    assert not any(RECEIPTS.glob(f"quad-{b:03d}.json"))
    name=EXPECTED_NAME(b)
    receipt_file=unique(root,f"nf729-{b:03d}-original-audit.json")
    upstream=json.loads(receipt_file.read_text())
    assert upstream["schema"]=="NF729-independent-original-quad-lean-kernel-audit-v1"
    assert upstream["kind"]=="Original" and upstream["quad_first_block"]==b
    assert upstream["quad_first_coordinate"]==b*8
    assert upstream["quad_end_coordinate"]==min((b+4)*8,242)
    names=[f"nf729Original{t}Quad{b:03d}" for t in ("HD","A")]
    assert upstream["theorems"]==names
    assert set(upstream["axioms"])==set(names)
    assert all(set(v)<=ALLOWED for v in upstream["axioms"].values())
    assert upstream["status"]=="LEAN KERNEL PASS, source-specific global HD/A original gate claims"
    original=SOURCE/f"Quad{b:03d}Original.lean"
    assert upstream["source_sha256"]==sha(original)
    assert upstream["manifest_sha256"]==sha(SOURCE/"manifest.json")
    files=list(root.rglob("*.olean"))
    assert files,(b,root)
    expected_target=Path(f"Generated/NF729/Quad{b:03d}Original.olean")
    found=False
    copies=[]
    reused=[]
    for obj in files:
        assert "WeilDefect" in obj.parts,(name,obj)
        idx=obj.parts.index("WeilDefect")
        relative=Path(*obj.parts[idx+1:])
        assert str(relative),obj
        dest=BUILD/relative
        dest.parent.mkdir(parents=True,exist_ok=True)
        data_sha=sha(obj)
        if dest.exists():
            assert dest.is_file() and sha(dest)==data_sha,(
                "Incompatible original Lean object across accepted source-bound shards",
                str(relative),str(obj),str(dest))
            reused.append(str(relative))
        else:
            shutil.copy2(obj,dest)
            assert sha(dest)==data_sha
            copies.append(str(relative))
        if relative==expected_target:
            found=True
    assert found,(b,str(expected_target))
    accepted=BUILD/expected_target
    assert accepted.is_file() and accepted.stat().st_size>1024
    RECEIPTS.mkdir(parents=True,exist_ok=True)
    record={
       "schema":"NF732-one-original-numerical-quad-object-source-custody-v1",
       "quad":b,
       "accepted_upstream_artifact_name":name,
       "accepted_original_numerical_theorem_names":names,
       "original_source_sha256":sha(original),
       "source_manifest_sha256":sha(SOURCE/"manifest.json"),
       "accepted_original_numerical_audit_sha256":sha(receipt_file),
       "olean_sha256":sha(accepted),
       "new_compiled_objects":copies,
       "reused_identical_objects":reused,
       "numeric_original_HD_and_A_range_kernel_passed":True,
       "original_global_row_all_passed":False,
    }
    (RECEIPTS/f"quad-{b:03d}.json").write_text(
        json.dumps(record,indent=2,sort_keys=True)+"\n")
    print(f"NF732 original numerical quad {b:03d} actual HD/A Lean kernel object accepted; original source/standard axioms and {len(copies)} new + {len(reused)} identical reused compiled objects SHA-verified")

def finalize():
    source_manifest()
    files=sorted(RECEIPTS.glob("quad-*.json"))
    assert len(files)==8
    records=[json.loads(p.read_text()) for p in files]
    assert [p["quad"] for p in records]==list(STARTS)
    installed={}
    for r in records:
        b=r["quad"]
        assert r["schema"]=="NF732-one-original-numerical-quad-object-source-custody-v1"
        assert r["numeric_original_HD_and_A_range_kernel_passed"] is True
        assert r["original_global_row_all_passed"] is False
        assert r["accepted_original_numerical_theorem_names"]==[
           f"nf729OriginalHDQuad{b:03d}",f"nf729OriginalAQuad{b:03d}"]
        assert r["accepted_upstream_artifact_name"]==EXPECTED_NAME(b)
        assert r["source_manifest_sha256"]==sha(SOURCE/"manifest.json")
        assert r["original_source_sha256"]==sha(SOURCE/f"Quad{b:03d}Original.lean")
        target=BUILD/"Generated"/"NF729"/f"Quad{b:03d}Original.olean"
        assert target.stat().st_size>1024
        assert sha(target)==r["olean_sha256"]
        for rel in r["new_compiled_objects"]+r["reused_identical_objects"]:
            path=BUILD/rel
            assert path.is_file(),(b,rel)
            digest=sha(path)
            if rel in installed:
                assert installed[rel]==digest,(b,rel)
            else:
                installed[rel]=digest
    output={
        "schema":"NF732-original-eight-accepted-NF729-numerical-quad-olean-inputs-v1",
        "upstream_run_id":44767040253,
        "upstream_exact_numerical_quad_jobs_success_requirement":8,
        "all_eight_accepted_original_quad_kernel_runs":True,
        "eight_original_gate_ranges_complete_Fin242":True,
        "sources":[{
            "quad":r["quad"],
            "proof_theorems":r["accepted_original_numerical_theorem_names"],
            "original_source_sha256":r["original_source_sha256"],
            "source_manifest_sha256":r["source_manifest_sha256"],
            "accepted_original_numerical_audit_sha256":r["accepted_original_numerical_audit_sha256"],
            "olean_sha256":r["olean_sha256"],
            "new_compiled_objects":len(r["new_compiled_objects"]),
            "reused_identical_compiled_objects":len(r["reused_identical_objects"])
        } for r in records],
        "installed_compiled_modules":installed,
        "original_HD_gate_range_claims":8,
        "original_A_gate_range_claims":8,
        "theorem_status":"16 accepted source-specific original range theorems from 8 independently kernel-verified upstream jobs. New NF732 full universal theorem still requires its own Lean compilation and axiom audit.",
    }
    Path("nf732-accepted-original-numerical-inputs.json").write_text(
       json.dumps(output,indent=2,sort_keys=True)+"\n")
    print("NF732 eight genuine numerical original HD/A quad Lean kernel receipts compiled and authenticated with bounded intermediate disk; final original universal theorem kernel remains pending")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("ingest","finalize"))
    p.add_argument("--quad",type=int)
    p.add_argument("--root",type=Path)
    a=p.parse_args()
    if a.stage=="ingest":
        assert a.quad in STARTS and a.root is not None
        ingest_one(a.quad,a.root)
    else:
        finalize()
