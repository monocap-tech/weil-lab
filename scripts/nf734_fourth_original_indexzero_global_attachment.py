#!/usr/bin/env python3
"""NF734: next genuine original global matrix index-zero HD/A product batch.

The first 24 original HD row-zero and A column-zero gates have already passed
Lean in NF708 (0..7), NF713 (8..15), and NF715 third global frontier (16..23).
This source-bound fourth batch proposes exactly positions 24..31 using the
same NF702 frozen original input, NF703 actual center cache, NF681 original
local products, and unchanged NF704 global emitter.

No new gate is considered accepted until the corresponding new Lean build
and strict 35-name standard-axiom audit pass.

The source step also creates an exhaustive remaining original matrix-index
inventory: 0:24 accepted source index pairs and 1:242 accepted universal index
pairs, with no certification claimed for any other index or remaining entry.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

from nf708_global_matrix_attachment_driver import (
    ALLOWED, manifest as validate_manifest, sha, theorem_names
)

N=242
START=24
STOP=32
PRIOR=24
PREVIOUS=(0,8,16,24)
SHARED=theorem_names(0)
FIRST=theorem_names(8)
SECOND=theorem_names(16)
THIRD=theorem_names(24)
COMPLETE=theorem_names(STOP)
NEW=SHARED+[
    f"nf704Col{i:03d}{suffix}"
    for i in range(START,STOP)
    for suffix in ("DGate","DProjection","HD","A")
]
assert len(SHARED)==3 and len(NEW)==35
assert len(THIRD)==99 and len(COMPLETE)==131
assert len(set(THIRD+NEW))==131


def file(root,name):
    paths=sorted(Path(root).rglob(name))
    assert len(paths)==1,(root,name,paths)
    return paths[0]


def read(p):
    return json.loads(Path(p).read_text())


def hash_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def axiom_map(axioms,names):
    assert isinstance(axioms,dict)
    assert set(axioms)==set(names),(sorted(set(names)-set(axioms)),sorted(set(axioms)-set(names)))
    assert all(isinstance(v,list) and set(v)<=ALLOWED for v in axioms.values())


def manifests():
    p1=file("nf734-first","manifest.json")
    p2=file("nf734-second","manifest.json")
    p3=file("nf734-third","manifest.json")
    current=Path("WeilDefect/Generated/NF704Frontier/manifest.json")
    assert current.is_file()
    m1,m2,m3,m4=[validate_manifest(p.parent) for p in (p1,p2,p3,current)]
    assert [x["schema"] for x in (m1,m2,m3,m4)]==[
        "NF704-global-matrix-projection-proposals-v1"
    ]*4
    assert [x["columns"] for x in (m1,m2,m3,m4)]==[8,16,24,STOP]
    assert [x["global_gate_targets"] for x in (m1,m2,m3,m4)]==[16,32,48,2*STOP]
    assert [len(x["files"]) for x in (m1,m2,m3,m4)]==[9,17,25,STOP+1]
    assert [x["audit_theorems"] for x in (m1,m2,m3,m4)]==[
        FIRST,SECOND,THIRD,COMPLETE
    ]
    binding=read("nf708-binding.json")
    assert binding["schema"]=="NF708-first-original-global-matrix-attachment-v1"
    assert binding["columns"]==STOP
    assert binding["theorems"]==COMPLETE
    assert binding["attachment_manifest_sha256"]==hash_file(current)
    assert set(binding["source_manifests"])==set(binding["accepted_audits"])=={
        "inputs","cache","frontier"
    }
    for m in (m1,m2,m3,m4):
        assert m["input_manifest_sha256"]==binding["source_manifests"]["inputs"]
        assert m["cache_manifest_sha256"]==binding["source_manifests"]["cache"]
        assert m["frontier_manifest_sha256"]==binding["source_manifests"]["frontier"]
    hashes=[
        {f["file"]:f["sha256"] for f in m["files"]}
        for m in (m1,m2,m3,m4)
    ]
    assert all(set(hashes[i])<set(hashes[i+1]) for i in range(3))
    for older,newer in zip(hashes,hashes[1:]):
        assert all(newer[k]==v for k,v in older.items()),(
            "Original matrix index-zero accepted prior Lean source drift",older,newer
        )
    c1=read(file("nf734-first","nf708-complete-audit.json"))
    c2=read(file("nf734-second","nf713-complete-audit.json"))
    c3=read(file("nf734-third","nf715-matrix-complete-audit.json"))
    assert c1["schema"]=="NF708-first-original-global-matrix-attachment-v1"
    assert c1["columns"]==8 and c1["theorems"]==FIRST
    assert c1["attachment_manifest_sha256"]==hash_file(p1)
    axiom_map(c1["axioms"],FIRST)
    assert c2["schema"]=="NF713-second-original-global-matrix-attachment-v1"
    assert (c2["first"],c2["end"],c2["new_global_gates"])==(8,16,16)
    assert c2["audit_theorems"]==SHARED+[
        f"nf704Col{i:03d}{t}"
        for i in range(8,16)
        for t in ("DGate","DProjection","HD","A")
    ]
    assert c2["old_attachment_manifest_sha256"]==hash_file(p1)
    assert c2["new_attachment_manifest_sha256"]==hash_file(p2)
    assert c2["old_audit_sha256"]==hash_file(file("nf734-first","nf708-complete-audit.json"))
    axiom_map(c2["axioms"],c2["audit_theorems"])
    assert c3["schema"]=="NF715-third-original-global-matrix-attachment-v1"
    assert (c3["first"],c3["end"],c3["new_global_gates"])==(16,24,16)
    assert c3["audit_theorems"]==SHARED+[
        f"nf704Col{i:03d}{t}"
        for i in range(16,24)
        for t in ("DGate","DProjection","HD","A")
    ]
    assert c3["first_accepted_audit_sha256"]==hash_file(
        file("nf734-first","nf708-complete-audit.json")
    )
    assert c3["second_accepted_audit_sha256"]==hash_file(
        file("nf734-second","nf713-complete-audit.json")
    )
    assert c3["first_source_manifest_sha256"]==hash_file(p1)
    assert c3["second_source_manifest_sha256"]==hash_file(p2)
    assert c3["new_attachment_manifest_sha256"]==hash_file(p3)
    assert c3["cumulative_original_global_matrix_gates"]==2*PRIOR
    assert c3["unique_cumulative_declarations"]==len(THIRD)
    assert c3["new_declarations"]==4*(PRIOR-16)
    assert c3["shared_declarations"]==SHARED
    axiom_map(c3["axioms"],c3["audit_theorems"])
    assert c1["source_manifests"]==c2["source_manifests"]==(
        c3["accepted_original_source_manifests"]
    )==binding["source_manifests"]
    assert c1["accepted_audits"]==c2["accepted_source_audits"]==(
        c3["accepted_source_audits"]
    )==binding["accepted_audits"]
    assert c3["prior_17_files_preserved"]==hashes[1]
    for name,h in c3["new_source_files"].items():
        assert hashes[2][name]==h==hashes[3][name]
    return binding,(p1,p2,p3,current),(c1,c2,c3),hashes


def prepare():
    bind,paths,certs,hashes=manifests()
    new_names=[
        f"nf704Col{i:03d}{t}"
        for i in range(START,STOP)
        for t in ("DGate","DProjection","HD","A")
    ]
    assert len(new_names)==32
    for i in range(START,STOP):
        src=Path(f"WeilDefect/Generated/NF704Frontier/Col{i:03d}.lean").read_text()
        for suffix in ("DGate","DProjection","HD","A"):
            assert re.search(rf"\btheorem nf704Col{i:03d}{suffix}\b",src)
        assert (
          f"nf703OriginalCache.HDGate nf702OriginalInputs 0 ({i}:Fin 242) = true"
          in src
        )
        assert (
          f"nf703OriginalCache.AGate nf702OriginalInputs ({i}:Fin 242) 0 = true"
          in src
        )
        assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",src,re.M)
    artifact={
        "schema":"NF734-original-indexzero-next-eight-actual-global-HD-A-v1",
        "accepted_existing_0_based_HD_row_indices":list(range(PRIOR)),
        "accepted_existing_0_based_A_column_indices":list(range(PRIOR)),
        "accepted_index_one_HD_indices":list(range(N)),
        "accepted_index_one_A_indices":list(range(N)),
        "proposed_indexzero_HD_indices":list(range(START,STOP)),
        "proposed_indexzero_A_indices":list(range(START,STOP)),
        "new_global_gate_proposals":2*(STOP-START),
        "new_Lean_declarations":len(new_names),
        "shared_Lean_declarations":SHARED,
        "new_axiom_audit_theorems":NEW,
        "full_emitted_manifest_sha256":hash_file(paths[3]),
        "source_data_manifests":bind["source_manifests"],
        "accepted_original_numerical_source_audits":bind["accepted_audits"],
        "accepted_first_indexzero_audit_sha256":hash_file(
             file("nf734-first","nf708-complete-audit.json")),
        "accepted_second_indexzero_audit_sha256":hash_file(
             file("nf734-second","nf713-complete-audit.json")),
        "accepted_third_indexzero_audit_sha256":hash_file(
             file("nf734-third","nf715-matrix-complete-audit.json")),
        "accepted_indexzero_source_hashes_before_batch":hashes[2],
        "new_indexzero_source_hashes":{
            k:v for k,v in hashes[3].items() if k not in hashes[2]
        },
        "next_original_HD_row_indexzero_open_indices":list(range(STOP,N)),
        "next_original_A_column_indexzero_open_indices":list(range(STOP,N)),
        "other_matrix_indices_universal_acceptance":[1],
        "existing_true_global_HD_A_gates":2*PRIOR+2*N,
        "source_certified_next_batch_only":True,
        "new_numerical_gate_kernel_pass":False,
        "full_matrix_numerical_custody_closed":False,
        "global_Weil_positivity_closed":False,
        "scope":"NF734 is only genuine ORIGINAL HD row0/A col0 coordinates 24..31; no further numerical gate may be claimed before new Lean acceptance"
    }
    Path("nf734-indexzero-next-eight-binding.json").write_text(
        json.dumps(artifact,indent=2,sort_keys=True)+"\n")
    assert len(artifact["new_indexzero_source_hashes"])==STOP-START
    print("NF734 authentic original NF708/NF713/NF715 source-verified 24 HD row0 +24 A col0 gates; original 242 index-one HD/A universal Lean accepted; next 8+8 ORIGINAL gates source-prepared only, new kernel pending")


def axioms():
    prepare()
    imports=["import WeilDefect.Generated.NF704Frontier.Common"]+[
        f"import WeilDefect.Generated.NF704Frontier.Col{i:03d}"
        for i in range(START,STOP)
    ]
    Path("nf734IndexZeroAudit.lean").write_text(
        "\n".join(imports+[f"#print axioms WeilDefect.{name}" for name in NEW])+"\n"
    )
    print("NF734 next eight original index-zero product gate names prepared for strict 35-declaration Lean axiom audit")


def verify():
    bind,paths,certs,hashes=manifests()
    receipt=read("nf734-indexzero-next-eight-binding.json")
    assert receipt["schema"]=="NF734-original-indexzero-next-eight-actual-global-HD-A-v1"
    assert receipt["full_emitted_manifest_sha256"]==hash_file(paths[3])
    assert receipt["source_data_manifests"]==bind["source_manifests"]
    assert receipt["new_axiom_audit_theorems"]==NEW
    assert receipt["new_indexzero_source_hashes"]=={
      k:v for k,v in hashes[3].items() if k not in hashes[2]
    }
    log=Path("nf734-indexzero-axioms.log").read_text()
    found={}
    for name,raw in re.findall(
      r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
        if name in NEW:
            assert name not in found,name
            found[name]=[x.strip() for x in raw.split(",") if x.strip()]
    for name in re.findall(
      r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
        if name in NEW:
            assert name not in found,name
            found[name]=[]
    axiom_map(found,NEW)
    assert "error:" not in log.lower()
    receipt["new_numerical_gate_kernel_pass"]=True
    receipt["new_gate_axioms"]=found
    receipt["accepted_indexzero_HD_indices_after_batch"]=list(range(STOP))
    receipt["accepted_indexzero_A_indices_after_batch"]=list(range(STOP))
    receipt["accepted_original_global_HD_A_gates_after_batch"]=2*STOP+2*N
    receipt["accepted_indexzero_universal_theorems"]=False
    receipt["full_matrix_numerical_custody_closed"]=False
    Path("nf734-indexzero-accepted-audit.json").write_text(
        json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("NF734 authentic ORIGINAL HD row zero 24..31 and A column zero 24..31 Lean PASS under standard axioms, first 32+32 indexzero gates certified; total 548 distinct original global matrix gates, all other matrix closure OPEN")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("prepare","axiom-file","verify"))
    args=p.parse_args()
    if args.stage=="prepare":prepare()
    elif args.stage=="axiom-file":axioms()
    else:verify()


if __name__=="__main__":
    main()
