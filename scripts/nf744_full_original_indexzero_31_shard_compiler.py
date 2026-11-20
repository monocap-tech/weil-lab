#!/usr/bin/env python3
"""NF744: source-bound full ORIGINAL index-zero HD/A row/column assembly.

The authentic NF704 original source bank carries 242 physical global
HDGate row-zero and 242 AGate column-zero candidate proofs. NF708, NF713
and NF715 third physical global stage have already kernel certified 0..23.
The other 218 pairs remain NEW numerical Lean obligations. NF744 does not
pretend those are accepted by building a source binder.

The emitter creates:
  * 31 original source-specific 8-coordinate (terminal 2) shard modules,
    two theorem candidates per shard (62 total), importing the REAL
    NF704Frontier.ColNNN gates, not a Boolean substitute.
  * 1 exact original FULL index-zero HD/A two-universal-theorem module
    using a separate 31-way Mathlib logical cover.
All 64 source-specific new declarations remain KERNEL OPEN until EVERY
relevant exact source-bound numerical module and new theorem compiles in
Lean with a strict standard-axiom audit.

The 31-range pure Mathlib implication has its own independent Lean job,
but cannot be used to certify numerical propositions without actual
original numerical premises.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import nf737_original_indexzero_complete_source_shard_schedule as source737
from nf708_global_matrix_attachment_driver import theorem_names

ROOT=Path("WeilDefect/Generated/NF704Frontier")
DEST=Path("WeilDefect/Generated/NF744")
LOGICAL=Path("WeilDefect/Arithmetic/ActualZetaOriginalIndexZero31ShardFullCover.lean")
LOGICAL_LOG=Path("nf744-original-indexzero-31-shard-pure-axioms.log")
PURE_RECEIPT=Path("nf744-original-indexzero-31-shard-lean-logical-audit.json")
NAME="neutralNF744AllFin242Of31OriginalIndexZeroShards"
FULL_THEOREMS=["nf744OriginalHDRowZeroAll","nf744OriginalAColumnZeroAll"]
STARTS=tuple(range(0,242,8))
RANGES=tuple((i,min(i+8,242)) for i in STARTS)
ALLOWED={"propext","Classical.choice","Quot.sound"}
assert len(RANGES)==31
assert [i for a,b in RANGES for i in range(a,b)]==list(range(242))
assert [a for a,b in RANGES[3:]]==[a for a,b in source737.SHARDS]
assert RANGES[-1]==(240,242)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(path):
    return json.loads(Path(path).read_text())

def predicate(typ,index="i"):
    if typ=="HD":
        return f"nf703OriginalCache.HDGate nf702OriginalInputs (0 : Fin 242) {index} = true"
    if typ=="A":
        return f"nf703OriginalCache.AGate nf702OriginalInputs {index} (0 : Fin 242) = true"
    raise ValueError(typ)

def source_bank():
    source737.verify()
    m=read(source737.BIND)
    assert m["schema"]=="NF737-original-indexzero-242-complete-global-HD-A-source-schedule-v1"
    assert m["full_original_matrix_N"]==242
    assert m["original_indexzero_HD_accepted"]==24
    assert m["original_indexzero_A_accepted"]==24
    assert m["new_original_global_gate_candidates"]==436
    assert m["new_original_numeric_kernel_pass"] is False
    assert m["original_indexone_HD_row_universal_certified"] is True
    assert m["original_indexone_A_column_universal_certified"] is True
    assert m["original_global_source_manifest_sha256"]==sha(ROOT/"manifest.json")
    assert m["first_previously_accepted_indexzero_coordinates"]==list(range(24))
    assert m["shard_count"]==28 and m["terminal_shard_exact_coordinates"]==[240,241]
    original=read(ROOT/"manifest.json")
    assert original["schema"]=="NF704-global-matrix-projection-proposals-v1"
    assert original["columns"]==242
    assert original["audit_theorems"]==theorem_names(242)
    assert original["global_gate_targets"]==484
    assert len(original["files"])==243
    for i in range(242):
        p=ROOT/f"Col{i:03d}.lean"
        s=p.read_text()
        assert f"nf703OriginalCache.HDGate nf702OriginalInputs 0 ({i}:Fin 242) = true" in s,(i,"HD")
        assert f"nf703OriginalCache.AGate nf702OriginalInputs ({i}:Fin 242) 0 = true" in s,(i,"A")
        assert re.findall(rf"^theorem (nf704Col{i:03d}\w+)",s,re.M)==[
           f"nf704Col{i:03d}{suf}" for suf in ("DGate","DProjection","HD","A")
        ]
        assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",s,re.M)
    return m,original

def shard_name(first,typ):
    assert typ in ("HD","A")
    return f"nf744Original{typ}Shard{first:03d}"

def range_module(first,end):
    assert (first,end) in RANGES
    imports=["import Mathlib.Tactic"]+[
       f"import WeilDefect.Generated.NF704Frontier.Col{i:03d}"
       for i in range(first,end)
    ]
    lines=imports+[
      "",
      "namespace WeilDefect",
      "",
      "set_option maxRecDepth 100000",
      "set_option maxHeartbeats 0",
      "",
      "/-! Original NF702/NF703 physical global gate RANGE transfer.",
      "This module imports REAL original NF704 gate proofs for each index;",
      "source generation alone does not certify any new theorem. -/",
      ""
    ]
    for typ in ("HD","A"):
        lines.extend([
          f"theorem {shard_name(first,typ)}",
          f"    (i : Fin 242) (hlo : {first} ≤ i.val)",
          f"    (hhi : i.val < {end}) :",
          f"    {predicate(typ)} := by",
          "  have h : "+ " ∨ ".join(
             f"i.val = {j}" for j in range(first,end)
          )+" := by omega",
          "  rcases h with " + " | ".join(
             "h" for _ in range(first,end)
          )
        ])
        for i in range(first,end):
            lines.extend([
              f"  · have hi : i = ({i} : Fin 242) := by",
              "      apply Fin.ext",
              "      simpa using h",
              "    subst i",
              f"    exact nf704Col{i:03d}{typ}"
            ])
        lines.extend(["",f"#print axioms {shard_name(first,typ)}",""])
    lines.extend(["end WeilDefect",""])
    return "\n".join(lines)

def full_module():
    lines=[
     "import WeilDefect.Arithmetic.ActualZetaOriginalIndexZero31ShardFullCover"
    ]+[
     f"import WeilDefect.Generated.NF744.Shard{first:03d}"
     for first,end in RANGES
    ]
    lines+=["","namespace WeilDefect","","set_option maxRecDepth 100000",
     "set_option maxHeartbeats 0","","/-! Exact ORIGINAL row0 HD and column0 A universal gate handoff.",
     "This source is NOT kernel certified until all 242 genuine NF704 gate",
     "source modules and 31 numerical shards have independently compiled. -/",""]
    for typ,theorem in zip(("HD","A"),FULL_THEOREMS):
        lines.extend([
          f"theorem {theorem} :",
          f"    ∀ i : Fin 242, {predicate(typ)} := by",
          "  exact neutralNF744AllFin242Of31OriginalIndexZeroShards",
          f"    (fun i => {predicate(typ)})",
        ])
        lines.extend(f"    {shard_name(first,typ)}" for first,end in RANGES)
        lines.extend(["",f"#print axioms {theorem}",""])
    lines.extend(["end WeilDefect",""])
    return "\n".join(lines)

def pure():
    s=LOGICAL.read_text()
    assert s.startswith("import Mathlib.Tactic\n")
    assert re.findall(r"^theorem (neutralNF744\w+)",s,re.M)==[NAME]
    assert "#print axioms "+NAME in s
    for a,b in RANGES:
        assert f"(s{a:03d} : ∀ k : Fin 242, {a} ≤ k.val → k.val < {b} → P k)" in s
        assert f"exact s{a:03d} k (by omega)" in s
    assert s.count("by_cases h")==30
    assert s.count("· exact s")==30
    assert "exact s240 k (by omega) k.isLt" in s
    assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",s,re.M)
    return sha(LOGICAL)

def emit():
    m,original=source_bank()
    logical_sha=pure()
    assert not DEST.exists(),("NF744 cannot overwrite already emitted numerical source",DEST)
    DEST.mkdir(parents=True)
    files={}
    for first,end in RANGES:
        name=f"Shard{first:03d}.lean"
        (DEST/name).write_text(range_module(first,end))
        files[name]=sha(DEST/name)
    (DEST/"ActualOriginalFull.lean").write_text(full_module())
    files["ActualOriginalFull.lean"]=sha(DEST/"ActualOriginalFull.lean")
    assert len(files)==32
    cert={
      "schema":"NF744-full-original-global-indexzero-HD-row-A-column-source-31-shards-v1",
      "accepted_original_numeric_source":"NF737 full source preflight run 44791346863 artifact 14660147684",
      "accepted_original_source_bank_sha256":sha(ROOT/"manifest.json"),
      "accepted_original_nf737_source_schedule_sha256":sha(source737.BIND),
      "previously_accepted_original_indexzero_HD_indices":list(range(24)),
      "previously_accepted_original_indexzero_A_indices":list(range(24)),
      "source_only_unaccepted_global_indexzero_indices":list(range(24,242)),
      "original_full_indexzero_HD_global_gate_indices":list(range(242)),
      "original_full_indexzero_A_global_gate_indices":list(range(242)),
      "original_full_indexone_HD_A_universal_lean_custody_pass":True,
      "shard_count":len(RANGES),
      "shards":[{
          "first":a,"end":b,
          "source_imports":[f"nf704Col{i:03d}{typ}"
             for i in range(a,b) for typ in ("HD","A")],
          "source_specific_theorems":[shard_name(a,"HD"),shard_name(a,"A")],
          "new_Lean_kernel_status":(
             "Original 0..23 coordinate proofs previously accepted; NEW shard gluing Lean pending"
             if b<=24 else
             "Original indexzero numerical gates and shard gluing both NEW LEAN PENDING")
      } for a,b in RANGES],
      "source_specific_shard_theorem_candidates":62,
      "source_specific_universal_theorem_candidates":2,
      "new_source_specific_theorem_candidates":64,
      "source_bound_new_original_numerical_gate_candidates":436,
      "accepted_original_0_to_23_global_gate_instances":48,
      "accepted_original_indexone_universal_gate_instances":484,
      "current_source_evidenced_accepted_gate_instance_total":532,
      "terminal_two_coordinate_shard":[240,242],
      "generic_full_Fin242_logical_lemma":NAME,
      "generic_logical_source_sha256":logical_sha,
      "files":files,
      "new_original_indexzero_range_numerical_lean_pass":False,
      "new_original_complete_indexzero_universal_lean_pass":False,
      "full_original_242x242_matrix_numeric_custody_closed":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
      "scope":"Only original frozen NF702/NF703 indexzero HD row/A column source. Full genuine global numerical gate terms require actual accepted 242 original modules; 31 shard and two universal Lean theorem sources are NOT accepted until source-bound kernel jobs succeed."
    }
    (DEST/"manifest.json").write_text(json.dumps(cert,sort_keys=True,indent=2)+"\n")
    verify()
    print("NF744: complete ORIGINAL indexzero 242-coordinate global HD and A source-specific 31-shard compiler assembly PREPARED; 62 interval + 2 universal proposed Lean theorems, 31 disjoint ranges and final Fin2; NO new original numerical indexzero theorem kernel accepted")

def verify():
    m,original=source_bank()
    logical_sha=pure()
    c=read(DEST/"manifest.json")
    assert c["schema"]=="NF744-full-original-global-indexzero-HD-row-A-column-source-31-shards-v1"
    assert c["accepted_original_numeric_source"]=="NF737 full source preflight run 44791346863 artifact 14660147684"
    assert c["accepted_original_source_bank_sha256"]==sha(ROOT/"manifest.json")
    assert c["accepted_original_nf737_source_schedule_sha256"]==sha(source737.BIND)
    assert c["generic_logical_source_sha256"]==logical_sha
    assert c["shard_count"]==31
    assert [(x["first"],x["end"]) for x in c["shards"]]==list(RANGES)
    assert c["terminal_two_coordinate_shard"]==[240,242]
    assert [i for s in c["shards"] for i in range(s["first"],s["end"])]==list(range(242))
    assert c["accepted_original_0_to_23_global_gate_instances"]==48
    assert c["accepted_original_indexone_universal_gate_instances"]==484
    assert c["current_source_evidenced_accepted_gate_instance_total"]==532
    assert c["new_source_specific_theorem_candidates"]==64
    assert c["source_bound_new_original_numerical_gate_candidates"]==436
    assert c["source_only_unaccepted_global_indexzero_indices"]==list(range(24,242))
    assert set(c["files"])=={"ActualOriginalFull.lean"} | {
        f"Shard{a:03d}.lean" for a,b in RANGES
    }
    for file,digest in c["files"].items():
        assert sha(DEST/file)==digest,(file,digest)
        s=(DEST/file).read_text()
        assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",s,re.M)
    for a,b in RANGES:
        s=(DEST/f"Shard{a:03d}.lean").read_text()
        assert re.findall(r"^theorem (nf744Original\w+)",s,re.M)==[
            shard_name(a,"HD"),shard_name(a,"A")
        ]
        assert s.count("theorem nf744Original")==2
        assert s.count("  · have hi : i = (")==2*(b-a)
        assert s.count("#print axioms nf744Original")==2
        for i in range(a,b):
            assert f"import WeilDefect.Generated.NF704Frontier.Col{i:03d}" in s
            for typ in ("HD","A"):
                assert f"exact nf704Col{i:03d}{typ}" in s
                assert f"have hi : i = ({i} : Fin 242)" in s
        assert predicate("HD") in s and predicate("A") in s
    full=(DEST/"ActualOriginalFull.lean").read_text()
    assert re.findall(r"^theorem (nf744Original\w+)",full,re.M)==FULL_THEOREMS
    assert full.count("neutralNF744AllFin242Of31OriginalIndexZeroShards")==2
    assert full.count("#print axioms nf744Original")==2
    for a,b in RANGES:
        assert f"import WeilDefect.Generated.NF744.Shard{a:03d}" in full
        assert full.count(f"    {shard_name(a,'HD')}")==1
        assert full.count(f"    {shard_name(a,'A')}")==1
    assert c["new_original_indexzero_range_numerical_lean_pass"] is False
    assert c["new_original_complete_indexzero_universal_lean_pass"] is False
    assert c["global_Weil_positivity_proved"] is False
    print("NF744 original complete 31-range genuine NF702/NF703 HD/A indexzero source bank, 64 theorem candidates, 242 positions/family and terminal Fin2 exact hash custody SOURCE PASS; NUMERICAL KERNEL OPEN")

def pure_verify():
    assert pure()
    s=LOGICAL_LOG.read_text()
    names={}
    for k,raw in re.findall(
      r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",s):
        if k==NAME:
            assert k not in names
            names[k]=[x.strip() for x in raw.split(",") if x.strip()]
    for k in re.findall(
      r"'WeilDefect\.(\w+)' does not depend on any axioms",s):
        if k==NAME:
            assert k not in names
            names[k]=[]
    assert set(names)=={NAME},names
    assert set(names[NAME])<=ALLOWED,names[NAME]
    assert not re.search(r"\berror:|sorryAx",s,re.I)
    p=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaOriginalIndexZero31ShardFullCover.olean")
    assert p.stat().st_size>1024
    r={
      "schema":"NF744-independent-original-indexzero-31-shard-Fin242-logical-Lean-v1",
      "theorem":NAME,
      "source_sha256":sha(LOGICAL),
      "compiled_olean_sha256":sha(p),
      "standard_axioms":names[NAME],
      "range_count":31,
      "full_original_coordinate_indices":list(range(242)),
      "terminal_shard":[240,242],
      "new_original_numerical_gate_proved":False,
      "full_original_indexzero_gate_universal_proved":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
      "scope":"Source-neutral 31-way Fin242 covering implication only; original NF702/NF703 gates are NOT proven by this logical lemma."
    }
    PURE_RECEIPT.write_text(json.dumps(r,sort_keys=True,indent=2)+"\n")
    print("NF744 31-shard full Fin242 logical cover Lean kernel + strict standard axioms PASS; all 436 previously unaccepted actual original indexzero numerical gate instances remain OPEN")


# Deferred source-specific full assembly: NO numerical truth follows from an
# emitted source, a finite-range cover, or the presence of cached object names.
# A FUTURE genuine full-kernel job must compile all 242 original numeric gate
# modules and 31 source-bound shards, then check all 64 theorem axioms.
FULL_AXFILE=Path("nf744ActualOriginalAll31AxiomAudit.lean")
FULL_AXLOG=Path("nf744-actual-full-original-indexzero-axioms.log")
FULL_AUDIT=Path("nf744-actual-full-original-indexzero-universal-kernel-audit.json")
COMPILED_ROOT=Path(".lake/build/lib/lean/WeilDefect/Generated")

def emit_complete_axiom_file():
    verify()
    names=[
        shard_name(a,typ)
        for a,b in RANGES for typ in ("HD","A")
    ]+FULL_THEOREMS
    assert len(names)==len(set(names))==64
    lines=[
      "import WeilDefect.Generated.NF744.ActualOriginalFull",
      ""
    ]+[f"#print axioms WeilDefect.{name}" for name in names]
    FULL_AXFILE.write_text("\n".join(lines)+"\n")
    assert FULL_AXFILE.read_text().count("#print axioms WeilDefect.")==64
    print("NF744 FULL original NF702/NF703 matrix row0 HD/col0 A 64-name strict proof-object axiom audit file PREPARED; no claim of numerical or full-universal kernel PASS")

def verify_complete_kernel():
    """Only after independently compiling every original numeric dependency.

    This is intentionally NOT run in NF744 source-only CI: individual original
    indexzero gates 24..241 remain pending. A future full-kernel workflow must
    build 242 actual original modules and 31 shards plus full master, then
    call this checker after compiling the all-64-axioms import file.
    """
    verify()
    emit_complete_axiom_file()
    assert FULL_AXLOG.is_file(),("Missing genuine final Lean axiom log",FULL_AXLOG)
    source=read(DEST/"manifest.json")
    assert not source["new_original_indexzero_range_numerical_lean_pass"]
    assert not source["new_original_complete_indexzero_universal_lean_pass"]
    objects={}
    for i in range(242):
        path=COMPILED_ROOT/f"NF704Frontier/Col{i:03d}.olean"
        assert path.is_file() and path.stat().st_size>1024,(
          "Not every genuine original source-specific numeric gate was compiled",
          path)
        objects[f"NF704Frontier/Col{i:03d}.olean"]=sha(path)
    for a,b in RANGES:
        path=COMPILED_ROOT/f"NF744/Shard{a:03d}.olean"
        assert path.is_file() and path.stat().st_size>1024,(
          "Not every source-bound original range shard compiled",path)
        objects[f"NF744/Shard{a:03d}.olean"]=sha(path)
    master=COMPILED_ROOT/"NF744/ActualOriginalFull.olean"
    assert master.is_file() and master.stat().st_size>1024,master
    allnames=[
        shard_name(a,typ)
        for a,b in RANGES for typ in ("HD","A")
    ]+FULL_THEOREMS
    log=FULL_AXLOG.read_text()
    found={}
    for name,raw in re.findall(
      r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
        if name in allnames:
            assert name not in found,name
            found[name]=[x.strip() for x in raw.split(",") if x.strip()]
    for name in re.findall(
      r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
        if name in allnames:
            assert name not in found,name
            found[name]=[]
    assert set(found)==set(allnames),(
      "Not all 62 actual original shard and 2 full universal declaration axioms were printed",
      set(allnames)-set(found))
    assert all(set(v)<=ALLOWED for v in found.values()),found
    assert not re.search(r"\berror:|sorryAx|declaration uses .sorry.",log,re.I)
    result={
      "schema":"NF744-authentic-original-global-indexzero-HD-A-31-shard-full-Lean-kernel-v1",
      "original_source_bank_sha256":source["accepted_original_source_bank_sha256"],
      "original_full_31_shard_source_manifest_sha256":sha(DEST/"manifest.json"),
      "original_full_master_source_sha256":sha(DEST/"ActualOriginalFull.lean"),
      "original_full_master_olean_sha256":sha(master),
      "actual_original_NF704_numerical_gate_compiled_module_count":242,
      "actual_original_NF744_31_shard_compiled_module_count":31,
      "actual_original_compiled_module_sha256":objects,
      "source_bound_original_theorems":allnames,
      "original_full_HD_row0_Lean_theorem":"nf744OriginalHDRowZeroAll",
      "original_full_A_column0_Lean_theorem":"nf744OriginalAColumnZeroAll",
      "printed_full_kernel_axioms_sha256":sha(FULL_AXLOG),
      "standard_axioms":found,
      "new_original_global_HD_row0_gate_instances":218,
      "new_original_global_A_column0_gate_instances":218,
      "original_indexzero_universal_gate_instance_count":484,
      "original_indexone_universal_gate_instance_count":484,
      "original_HDA_indexzero_plus_indexone_gate_instances":968,
      "original_complete_242x242_matrix_enclosure_closed":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
      "scope":"Only complete genuine frozen original NF702/NF703 HD row0 and A column0. All 242 original numeric modules/31 source-bound shards/2 full universal Lean declarations kernel compiled, exact 64 standard axiom lists and source/olean hashes required. Other matrix rows, vectors, payments, global Weil positivity remain OPEN.",
      "status":"GENUINE ORIGINAL HD ROW0 AND A COL0 FULL NUMERICAL LEAN PASS, only if all required original source and compiled kernel objects and the printed 64 theorem axioms were actually accepted"
    }
    FULL_AUDIT.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF744 genuine ORIGINAL HD row0 242/242 plus A col0 242/242 UNIVERSAL Lean KERNEL PASS and 64 theorem strict axioms PASS; full matrix, payments, global Weil positivity and RH OPEN")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("emit","verify","pure-verify","full-axiom-file","verify-complete-kernel"))
    args=p.parse_args()
    if args.stage=="emit":emit()
    elif args.stage=="verify":verify()
    elif args.stage=="pure-verify":pure_verify()
    elif args.stage=="full-axiom-file":emit_complete_axiom_file()
    else:verify_complete_kernel()
