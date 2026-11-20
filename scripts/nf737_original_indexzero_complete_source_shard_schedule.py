#!/usr/bin/env python3
"""NF737: exhaustive ORIGINAL matrix index-zero source-bound global HD/A schedule.

This is distinct from NF729 original index ONE. NF708+NF713+NF715 third
matrix-frontier successfully certified positions 0..23 of the genuine
NF702/NF703 original HD row 0 / A column 0. The NF734 next 24..31 job
is a proposed source-specific numerical batch, not an accepted input.

This driver regenerates precisely the remaining 218 coordinate sources,
from original accepted NF681 242 local HD/A proof objects and the original
NF702 / NF703 source bank. It authenticates all 25 already-accepted source
modules and source/Lean axiom receipts before treating new modules as
source candidates. It also generates a pure Mathlib Fin242 logical covering
theorem for 28 disjoint pending coordinate shards.

No new original numerical gate becomes true merely by source generation
or acceptance of the generic logical coverage theorem. All 436 new
individual original global gate instances await their own Lean kernel
compilation and strict original-source axiom audits.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

from nf708_global_matrix_attachment_driver import (
    ALLOWED, manifest as check_manifest, theorem_names
)

N=242
ACCEPTED=24
BLOCK_WIDTH=8
STARTS=tuple(range(ACCEPTED,N,BLOCK_WIDTH))
assert len(STARTS)==28
SHARDS=tuple((start,min(start+BLOCK_WIDTH,N)) for start in STARTS)
assert [i for a,b in SHARDS for i in range(a,b)]==list(range(ACCEPTED,N))
SOURCE=Path("WeilDefect/Generated/NF704Frontier")
LOGIC=Path("WeilDefect/Arithmetic/ActualZetaOriginalIndexZeroRemainingCover.lean")
BIND=Path("nf737-original-indexzero-complete-source-schedule.json")
AUDIT=Path("nf737-original-indexzero-coverage-audit.json")
THEOREM="neutralNF737RemainingIndexZeroOf28Shards"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def one(folder,name):
    x=sorted(Path(folder).rglob(name))
    assert len(x)==1,(folder,name,x)
    return x[0]


def expected_gate_names(first,end):
    return [
        f"nf704Col{i:03d}{suffix}"
        for i in range(first,end)
        for suffix in ("DGate","DProjection","HD","A")
    ]


def axiom_map(m,names):
    assert set(m)==set(names),(len(m),len(names),set(names)-set(m))
    assert all(isinstance(v,list) and set(v)<=ALLOWED for v in m.values())


def source_custody():
    prior_paths=[one(p,"manifest.json") for p in (
      "nf737-accepted-000-007", "nf737-accepted-008-015",
      "nf737-accepted-016-023"
    )]
    prior=[check_manifest(p.parent) for p in prior_paths]
    full=check_manifest(SOURCE)
    assert [m["columns"] for m in prior]==[8,16,24]
    assert full["columns"]==N
    assert [len(m["files"]) for m in prior]==[9,17,25]
    assert len(full["files"])==N+1
    assert [m["global_gate_targets"] for m in prior]==[16,32,48]
    assert full["global_gate_targets"]==2*N
    assert [m["audit_theorems"] for m in prior]==[
        theorem_names(x) for x in (8,16,24)]
    assert full["audit_theorems"]==theorem_names(N)
    assert len(set(full["audit_theorems"]))==3+4*N==971
    assert all(m["schema"]=="NF704-global-matrix-projection-proposals-v1"
               for m in prior+[full])
    b=read("nf708-binding.json")
    assert b["schema"]=="NF708-first-original-global-matrix-attachment-v1"
    assert b["columns"]==N
    assert b["theorems"]==theorem_names(N)
    assert b["attachment_manifest_sha256"]==sha(SOURCE/"manifest.json")
    assert set(b["source_manifests"])==set(b["accepted_audits"])=={
       "inputs","cache","frontier"
    }
    for m in prior+[full]:
        assert m["input_manifest_sha256"]==b["source_manifests"]["inputs"]
        assert m["cache_manifest_sha256"]==b["source_manifests"]["cache"]
        assert m["frontier_manifest_sha256"]==b["source_manifests"]["frontier"]
    hashes=[{f["file"]:f["sha256"] for f in m["files"]}
        for m in prior+[full]]
    assert all(set(old)<set(new) for old,new in zip(hashes,hashes[1:]))
    for old,new in zip(hashes,hashes[1:]):
        assert all(new[name]==hashval for name,hashval in old.items())
    assert set(hashes[2])=={"Common.lean"} | {
        f"Col{i:03d}.lean" for i in range(ACCEPTED)
    }
    assert set(hashes[3])=={"Common.lean"} | {
        f"Col{i:03d}.lean" for i in range(N)
    }
    c1=read(one("nf737-accepted-000-007","nf708-complete-audit.json"))
    c2=read(one("nf737-accepted-008-015","nf713-complete-audit.json"))
    c3=read(one("nf737-accepted-016-023","nf715-matrix-complete-audit.json"))
    assert c1["schema"]=="NF708-first-original-global-matrix-attachment-v1"
    assert c1["columns"]==8 and c1["theorems"]==theorem_names(8)
    assert c1["attachment_manifest_sha256"]==sha(prior_paths[0])
    axiom_map(c1["axioms"],c1["theorems"])
    assert c2["schema"]=="NF713-second-original-global-matrix-attachment-v1"
    assert (c2["first"],c2["end"],c2["new_global_gates"])==(8,16,16)
    assert c2["audit_theorems"]==theorem_names(0)+expected_gate_names(8,16)
    assert c2["old_attachment_manifest_sha256"]==sha(prior_paths[0])
    assert c2["new_attachment_manifest_sha256"]==sha(prior_paths[1])
    assert c2["old_audit_sha256"]==sha(
       one("nf737-accepted-000-007","nf708-complete-audit.json"))
    axiom_map(c2["axioms"],c2["audit_theorems"])
    assert c3["schema"]=="NF715-third-original-global-matrix-attachment-v1"
    assert (c3["first"],c3["end"],c3["new_global_gates"])==(16,24,16)
    assert c3["audit_theorems"]==theorem_names(0)+expected_gate_names(16,24)
    assert c3["first_accepted_audit_sha256"]==sha(
       one("nf737-accepted-000-007","nf708-complete-audit.json"))
    assert c3["second_accepted_audit_sha256"]==sha(
       one("nf737-accepted-008-015","nf713-complete-audit.json"))
    assert c3["first_source_manifest_sha256"]==sha(prior_paths[0])
    assert c3["second_source_manifest_sha256"]==sha(prior_paths[1])
    assert c3["new_attachment_manifest_sha256"]==sha(prior_paths[2])
    assert c3["new_declarations"]==32
    assert c3["cumulative_original_global_matrix_gates"]==2*ACCEPTED
    assert c3["unique_cumulative_declarations"]==len(theorem_names(ACCEPTED))
    assert c3["shared_declarations"]==theorem_names(0)
    assert c3["prior_17_files_preserved"]==hashes[1]
    for filename,hashval in c3["new_source_files"].items():
        assert hashes[2][filename]==hashval==hashes[3][filename]
    axiom_map(c3["axioms"],c3["audit_theorems"])
    assert c1["source_manifests"]==c2["source_manifests"]==(
        c3["accepted_original_source_manifests"])==b["source_manifests"]
    assert c1["accepted_audits"]==c2["accepted_source_audits"]==(
        c3["accepted_source_audits"])==b["accepted_audits"]
    for start,end in SHARDS:
        for i in range(start,end):
            f=SOURCE/f"Col{i:03d}.lean"
            s=f.read_text()
            for suffix in ("DGate","DProjection","HD","A"):
                assert re.search(rf"^theorem nf704Col{i:03d}{suffix}\s*:",s,re.M),(i,suffix)
            assert (
                f"nf703OriginalCache.HDGate nf702OriginalInputs 0 ({i}:Fin 242) = true" in s
            ),i
            assert (
                f"nf703OriginalCache.AGate nf702OriginalInputs ({i}:Fin 242) 0 = true" in s
            ),i
            assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",s,re.M),i
            assert s.count("#print axioms nf704Col")==4,i
    return b,prior_paths,c1,c2,c3,hashes


def finite_logic():
    lines=[
      "import Mathlib.Tactic",
      "",
      "namespace WeilDefect",
      "",
      "set_option maxRecDepth 100000",
      "set_option maxHeartbeats 0",
      "",
      "/-! NF737 genuine original Fin242 coordinate range decomposition only.",
      "There are 28 shards, the last has two coordinates [240,242).",
      "This theorem does not assert any original numerical matrix gate truth. -/",
      "",
      "/-- 28-source-range logical implication for the remaining original",
      "HD row zero or A column zero positions. Source-independent. -/",
      f"theorem {THEOREM}",
      "    (P : Fin 242 → Prop)"
    ]
    for i,j in SHARDS:
        lines.append(
          f"    (s{i:03d} : ∀ k : Fin 242, {i} ≤ k.val → k.val < {j} → P k)"
        )
    lines.extend([
      "    (k : Fin 242) (hlo : 24 ≤ k.val) : P k := by",
    ])
    pad="  "
    for i,j in SHARDS[:-1]:
        lines.extend([
          pad+f"by_cases h{j} : k.val < {j}",
          pad+f"· exact s{i:03d} k (by omega) h{j}",
          pad+"·"
        ])
        pad+="  "
    lines.append(pad+"exact s240 k (by omega) k.isLt")
    lines.extend(["",f"#print axioms {THEOREM}","","end WeilDefect",""])
    return "\n".join(lines)


def prepare():
    b,paths,c1,c2,c3,hashes=source_custody()
    assert not LOGIC.exists(),LOGIC
    LOGIC.parent.mkdir(parents=True,exist_ok=True)
    LOGIC.write_text(finite_logic())
    j={
      "schema":"NF737-original-indexzero-242-complete-global-HD-A-source-schedule-v1",
      "full_original_matrix_N":N,
      "first_previously_accepted_indexzero_coordinates":list(range(ACCEPTED)),
      "original_indexone_HD_row_universal_certified":True,
      "original_indexone_A_column_universal_certified":True,
      "original_indexone_universal_accepted_custody_run_id":44782027897,
      "original_indexone_universal_accepted_custody_artifact_id":14652498322,
      "original_indexzero_HD_accepted":ACCEPTED,
      "original_indexzero_A_accepted":ACCEPTED,
      "original_indexzero_HD_new_gate_candidates":N-ACCEPTED,
      "original_indexzero_A_new_gate_candidates":N-ACCEPTED,
      "new_original_global_gate_candidates":2*(N-ACCEPTED),
      "new_original_Lean_declaration_candidates":4*(N-ACCEPTED),
      "full_original_indexzero_HD_A_proposed_gates":2*N,
      "full_original_indexzero_Lean_declarations":3+4*N,
      "distinct_original_indexzero_and_indexone_currently_accepted_gates":2*ACCEPTED+2*N,
      "accepted_prior_original_indexzero_source_sha256":{
        "NF708":sha(paths[0]),"NF713":sha(paths[1]),"NF715":sha(paths[2])
      },
      "accepted_original_base_input_cache_frontier_source_manifests":b["source_manifests"],
      "original_global_source_manifest_sha256":sha(SOURCE/"manifest.json"),
      "original_global_source_module_hashes":hashes[3],
      "accepted_prior_source_module_hashes":hashes[2],
      "shard_width":BLOCK_WIDTH,
      "shard_count":len(SHARDS),
      "shards":[{
        "start":i,"end":j,
        "local_modules":[f"Col{k:03d}.lean" for k in range(i,j)],
        "original_HD_gate_theorems":[f"nf704Col{k:03d}HD" for k in range(i,j)],
        "original_A_gate_theorems":[f"nf704Col{k:03d}A" for k in range(i,j)],
        "new_decl_names":expected_gate_names(i,j),
        "kernel_status":"SOURCE CANDIDATE; original global numerical Lean verification pending",
      } for i,j in SHARDS],
      "terminal_shard_exact_coordinates":[240,241],
      "pure_cover_file":str(LOGIC),
      "pure_cover_source_sha256":sha(LOGIC),
      "pure_cover_theorem_name":THEOREM,
      "new_original_numeric_kernel_pass":False,
      "complete_original_indexzero_universal_Lean_PASS":False,
      "complete_original_242x242_global_matrix_enclosure_Lean_PASS":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
      "scope":"Genuine original NF702/NF703 HD row index zero/A column index zero: 0–23 accepted from NF708+NF713+NF715; 24–241 28 new 8/terminal2 source candidates only. NF734 24–31 may compile independently. Index-one already closed, all other matrix indices and vector/payment/Weil goals remain open."
    }
    BIND.write_text(json.dumps(j,sort_keys=True,indent=2)+"\n")
    verify()
    print("NF737 exactly 218 remaining authentic ORIGINAL HD row0 and 218 A col0 source candidates across 28 disjoint finite shards; accepted old 24 source files byte-identical; original index-one 242+242 separately Lean accepted; NEW original numerical kernel proofs not yet attempted")


def verify():
    b,paths,c1,c2,c3,hashes=source_custody()
    j=read(BIND)
    assert j["schema"]=="NF737-original-indexzero-242-complete-global-HD-A-source-schedule-v1"
    assert j["shard_count"]==28
    assert len(j["shards"])==28
    assert [(s["start"],s["end"]) for s in j["shards"]]==list(SHARDS)
    assert [k for shard in j["shards"] for k in range(shard["start"],shard["end"])]==list(range(24,N))
    assert j["terminal_shard_exact_coordinates"]==[240,241]
    assert j["first_previously_accepted_indexzero_coordinates"]==list(range(24))
    assert j["new_original_global_gate_candidates"]==436
    assert j["new_original_Lean_declaration_candidates"]==872
    assert j["full_original_indexzero_Lean_declarations"]==971
    assert j["distinct_original_indexzero_and_indexone_currently_accepted_gates"]==532
    assert j["original_global_source_manifest_sha256"]==sha(SOURCE/"manifest.json")
    assert j["original_global_source_module_hashes"]==hashes[3]
    assert j["accepted_prior_source_module_hashes"]==hashes[2]
    assert j["accepted_prior_original_indexzero_source_sha256"]=={
        "NF708":sha(paths[0]),"NF713":sha(paths[1]),"NF715":sha(paths[2])
    }
    assert j["accepted_original_base_input_cache_frontier_source_manifests"]==b["source_manifests"]
    assert j["pure_cover_file"]==str(LOGIC)
    assert j["pure_cover_source_sha256"]==sha(LOGIC)
    assert j["pure_cover_theorem_name"]==THEOREM
    text=LOGIC.read_text()
    assert text.startswith("import Mathlib.Tactic\n")
    assert re.findall(r"^theorem (neutralNF737\w+)",text,re.M)==[THEOREM]
    assert text.count("by_cases h")==len(SHARDS)-1
    assert text.count("· exact s")==len(SHARDS)-1
    assert "exact s240 k (by omega) k.isLt" in text
    assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",text,re.M)
    assert j["new_original_numeric_kernel_pass"] is False
    assert j["complete_original_indexzero_universal_Lean_PASS"] is False
    assert j["global_Weil_positivity_proved"] is False
    print("NF737 real original 242 gate-source enumeration, accepted 24 prefix preservation, 28 cover ranges, terminal Fin2, 532 existing gates and 436 new gate candidates SOURCE/PREFLIGHT PASS; numerical Lean acceptance pending")


def verify_pure():
    verify()
    log=Path("nf737-remaining-indexzero-pure-axioms.log").read_text()
    lines=re.findall(
       rf"'WeilDefect\.{THEOREM}' depends on axioms: \[([^\]]*)\]",
       log
    )
    no=re.findall(rf"'WeilDefect\.{THEOREM}' does not depend on any axioms",log)
    assert len(lines)+len(no)==1,(lines,no)
    values=[p.strip() for p in lines[0].split(",") if p.strip()] if lines else []
    assert set(values)<=ALLOWED,values
    assert not re.search(r"\berror:",log,re.I)
    r={
      "schema":"NF737-generic-original-indexzero-remaining-28-shard-Fin242-cover-Lean-v1",
      "theorem":THEOREM,
      "source_sha256":sha(LOGIC),
      "schedule_sha256":sha(BIND),
      "axioms":values,
      "first_coordinate":24,
      "end_coordinate":242,
      "remaining_coordinates_covered":218,
      "shards":len(SHARDS),
      "last_shard":[240,242],
      "status":"LEAN PASS exact generic finite-index 28-shard implication only; ZERO new original numerical gate assertions"
    }
    AUDIT.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n")
    print("NF737 genuine original indexzero source-neutral 28-range logical cover LEAN PASS (if direct Lean and this strict audit succeeded); 436 new global HD/A numerical gates remain kernel OPEN")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("stage",choices=("prepare","verify","verify-pure"))
    args=parser.parse_args()
    if args.stage=="prepare":prepare()
    elif args.stage=="verify":verify()
    else:verify_pure()
