#!/usr/bin/env python3
"""NF728: specialize accepted real original HD/A packed gate sources to two halves.

Requires the immutable NF727 *successful source-preflight* artifact, whose
NF723 OriginalRowOne.lean and manifest were independently generated from the
authentic NF702 input, NF703 original center cache, 31 NF700 local blocks,
NF715–NF720 accepted global block proofs and NF721 ledger.

This constructs actual original propositions, unlike the generic NF727 glue:
  nf703OriginalCache.HDGate nf702OriginalInputs 1 i = true
  nf703OriginalCache.AGate  nf702OriginalInputs i 1 = true

The four source-specific half theorems and two complete universal theorems
require NEW Lean kernel passes; Python source checks do not certify them.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from emit_nf630_original_literal_payments import filetext

PREVIOUS = Path("nf728-prior-original/WeilDefect/Generated/NF723")
PRIOR_META = Path("nf728-prior-original/nf723-binding.json")
DEST = Path("WeilDefect/Generated/NF728")
STAGES = (715, 716, 717, 718, 719, 720)
COVER = tuple(range(242))
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
HALF_NAMES = [
    "nf728OriginalHDLeft",
    "nf728OriginalALeft",
    "nf728OriginalHDRight",
    "nf728OriginalARight",
]
FULL_NAMES = ["nf728OriginalHDRowOneAll", "nf728OriginalAColumnOneAll"]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def stage(i):
    assert 0 <= i < 31
    return 715 if i == 0 else 716 if i < 4 else 717 if i < 8 else (
        718 if i < 16 else 719 if i < 24 else 720)


def source_context():
    original = PREVIOUS/"OriginalRowOne.lean"
    original_manifest = PREVIOUS/"manifest.json"
    assert original.is_file() and original_manifest.is_file() and PRIOR_META.is_file()
    m, meta=read(original_manifest),read(PRIOR_META)
    assert m==meta, "NF727 accepted original full-row manifest / source receipt disagree"
    assert m["schema"]=="NF723-actual-original-complete-row-one-source-attachment-v1"
    assert sha(original)==m["new_source_sha256"]
    assert m["new_module"]=="WeilDefect.Generated.NF723.OriginalRowOne"
    assert m["accepted_prior_theorem_declarations"]==252
    assert m["accepted_original_coordinate_pairs"]==242
    assert m["expected_original_hd_gates"]==m["expected_original_a_gates"]==242
    assert m["nf717_newly_closed_coordinate_interval"]==[32,64]
    assert m["new_universal_theorems"]==[
      "nf723OriginalHDRowOneAll","nf723OriginalAColumnOneAll"]
    assert len(m["accepted_stages"])==9
    assert set(m["source_files"])=={
        "NF715","NF716","NF717","NF718","NF719","NF720"}
    for group in m["accepted_stages"]:
        assert group["stage"] in {f"nf{x}" for x in STAGES}
        assert all(len(x)==64 for x in group["source_files"].values())
        assert len(group["manifest_sha256"])==len(group["audit_sha256"])==64
    actual = original.read_text()
    assert not re.search(r"\b(sorry|admit|axiom|unsafe)\b",actual)
    imports = re.findall(r"^import WeilDefect\.Generated\.(NF\d+)\.(Block\d{3})$",actual,re.M)
    assert len(imports)==31
    assert imports == [(f"NF{stage(i)}", f"Block{i:03d}") for i in range(31)]
    all_modules={}
    for typ in ("HD","A"):
        items = re.findall(rf"^    (nf\d+Block\d{{3}}Global{typ})$",actual,re.M)
        expected=[f"nf{stage(i)}Block{i:03d}Global{typ}" for i in range(31)]
        assert items==expected,(typ,items,expected)
        all_modules[typ]=items
    return m,all_modules,imports


def formula(typ, i="j"):
    assert typ in ("HD","A")
    if typ=="HD":
        return (f"nf703OriginalCache.HDGate nf702OriginalInputs "
                f"(1 : Fin 242) {i} = true")
    return (f"nf703OriginalCache.AGate nf702OriginalInputs "
            f"{i} (1 : Fin 242) = true")


def actual_half(which,names,imports):
    assert which in ("Left","Right")
    start,end=(0,16) if which=="Left" else (16,31)
    index=0 if which=="Left" else 16
    bound="i.val < 128" if which=="Left" else "128 ≤ i.val"
    hbound="hi"
    needed = [
      f"WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedFinHalf{index:03d}"
    ]+[
      f"WeilDefect.Generated.NF{stage(i)}.Block{i:03d}"
      for i in range(start,end)
    ]
    assert len(needed)==end-start+1
    body=(
        "set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
        f"/-! NF728: genuine original HD/A source-bound {which.lower()}-half "
        f"global product gates on {start*8}..{min(end*8,242)-1}. "
        "No new numerical oracle; all local gate witnesses were previously Lean-accepted. "
        "The two NEW universally quantified half claims must still pass the kernel. -/\n\n"
    )
    for typ in ("HD","A"):
        tname=f"nf728Original{typ}{which}"
        predicate=formula(typ,"i")
        body+=(
            f"theorem {tname} (i : Fin 242) ({hbound} : {bound}) :\n"
            f"    {predicate} := by\n"
            f"  exact neutralNF726Half{index:03d}\n"
            f"    (fun j : Fin 242 => {formula(typ,'j')})\n"
        )
        body+="".join(f"    {names[typ][i]}\n" for i in range(start,end))
        body+=f"    i {hbound}\n\n"
    body+=f"#print axioms nf728OriginalHD{which}\n"
    body+=f"#print axioms nf728OriginalA{which}\n"
    return filetext(needed,body)


def actual_complete():
    imports=[
      "WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFiniteBinaryGluing",
      "WeilDefect.Generated.NF728.ActualLeft",
      "WeilDefect.Generated.NF728.ActualRight",
    ]
    body=(
      "set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
      "/-! NF728: actual original full index-one HD row and A column, "
      "from four separately kernel-accepted real numerical half theorems. "
      "This file alone must pass Lean to claim both full universal gates. -/\n\n"
    )
    for typ in ("HD","A"):
        name=FULL_NAMES[0] if typ=="HD" else FULL_NAMES[1]
        body+=(
           f"theorem {name} :\n"
           f"    ∀ j : Fin 242, {formula(typ,'j')} := by\n"
           "  exact neutralNF727Fin242OfTwoHalves\n"
           f"    (fun j : Fin 242 => {formula(typ,'j')})\n"
           f"    nf728Original{typ}Left\n"
           f"    nf728Original{typ}Right\n\n"
        )
    body+="".join(f"#print axioms {name}\n" for name in FULL_NAMES)
    return filetext(imports,body)


def prepare():
    m,names,imports=source_context()
    assert not DEST.exists(),DEST
    DEST.mkdir(parents=True)
    files={
      "ActualLeft.lean":actual_half("Left",names,imports),
      "ActualRight.lean":actual_half("Right",names,imports),
      "ActualComplete.lean":actual_complete(),
    }
    for name,content in files.items():
        (DEST/name).write_text(content)
    manifest={
      "schema":"NF728-original-global-HD-A-binary-half-source-candidates-v1",
      "original_inputs":m["actual_source_manifests"],
      "accepted_original_numerical_source_audits":m["accepted_original_source_audits"],
      "nf727_original_source_receipt_sha256":sha(PRIOR_META),
      "nf727_original_compiler_preflight_run":44760318280,
      "nf727_original_preflight_artifact_id":14641426213,
      "accepted_prior_global_product_theorem_declarations":252,
      "accepted_original_index_one_HD_coordinate_gates":242,
      "accepted_original_index_one_A_coordinate_gates":242,
      "blocks": [
         {"number":i,"first":i*8,"end":min((i+1)*8,242),
          "globalHD":names["HD"][i],"globalA":names["A"][i],
          "accepted_original_stage":f"NF{stage(i)}"}
         for i in range(31)
      ],
      "half_ranges":[{"part":"Left","first":0,"end":128},
                     {"part":"Right","first":128,"end":242}],
      "half_theorems":HALF_NAMES,
      "full_theorems":FULL_NAMES,
      "files":{name:sha(DEST/name) for name in files},
      "status":"Source-authenticated actual original numerical half/global Lean proof candidates; ALL SIX NEW theorems await distinct Lean kernel acceptance",
      "scope":"Only original HD row one and A column one. Full original cache, vectors, payment rows, global Weil positivity, and RH are not proved."
    }
    assert [(v["first"],v["end"]) for v in manifest["blocks"]]==[
      (8*i,min(8*(i+1),242)) for i in range(31)]
    assert [j for b in manifest["blocks"] for j in range(b["first"],b["end"])]==list(COVER)
    (DEST/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
    print("NF728 exact authentic 31 original global proof blocks source-bound to four actual index-one HD/A half claims and two original universal claims; Lean pending")


def source_verify():
    m,names,_=source_context()
    manifest=read(DEST/"manifest.json")
    assert manifest["schema"]=="NF728-original-global-HD-A-binary-half-source-candidates-v1"
    assert manifest["original_inputs"]==m["actual_source_manifests"]
    assert manifest["accepted_original_numerical_source_audits"]==m["accepted_original_source_audits"]
    assert manifest["nf727_original_source_receipt_sha256"]==sha(PRIOR_META)
    assert manifest["half_theorems"]==HALF_NAMES
    assert manifest["full_theorems"]==FULL_NAMES
    assert len(manifest["blocks"])==31
    assert len(set(b["globalHD"] for b in manifest["blocks"]))==31
    assert len(set(b["globalA"] for b in manifest["blocks"]))==31
    assert manifest["files"]=={
      name:sha(DEST/name) for name in manifest["files"]
    }
    for which in ("Left","Right"):
        s=(DEST/f"Actual{which}.lean").read_text()
        start,end=(0,16) if which=="Left" else (16,31)
        expected_modules=[
            f"WeilDefect.Generated.NF{stage(i)}.Block{i:03d}"
            for i in range(start,end)
        ]
        assert re.findall(r"^import (WeilDefect\.Generated\.NF\d+\.Block\d{3})$",s,re.M)==expected_modules
        assert re.findall(r"^theorem (nf728Original\w+)",s,re.M)==[
            f"nf728OriginalHD{which}",f"nf728OriginalA{which}"]
        for typ in ("HD","A"):
            found=re.findall(rf"^    (nf\d+Block\d{{3}}Global{typ})$",s,re.M)
            assert found==names[typ][start:end],(which,typ)
        assert not re.search(r"\b(sorry|admit|axiom|unsafe)\b",s)
    s=(DEST/"ActualComplete.lean").read_text()
    assert re.findall(r"^theorem (nf728Original\w+)",s,re.M)==FULL_NAMES
    assert all(f"nf728Original{typ}{side}" in s
       for typ in ("HD","A") for side in ("Left","Right"))
    assert "neutralNF727Fin242OfTwoHalves" in s
    assert not re.search(r"\b(sorry|admit|axiom|unsafe)\b",s)
    print("NF728 real original HD/A 242-coordinate source and 3 generated theorem-module candidate preflight PASS — requires kernel")


def strict_axioms(log_path,expected):
    log=Path(log_path).read_text()
    found={}
    for name,raw in re.findall(
      r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
        if name in expected:
          assert name not in found,name
          found[name]=[s.strip() for s in raw.split(",") if s.strip()]
    for name in re.findall(
      r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
        if name in expected:
          assert name not in found
          found[name]=[]
    assert set(found)==set(expected),(expected,found)
    assert all(set(v)<=ALLOWED for v in found.values())
    return found


def verify_half(which):
    source_verify()
    assert which in ("Left","Right")
    names=[f"nf728Original{t}{which}" for t in ("HD","A")]
    proven=strict_axioms(f"nf728-{which.lower()}-axioms.log",names)
    target=DEST/f"Actual{which}.lean"
    receipt={
      "schema":"NF728-real-original-HD-A-half-lean-proof-audit-v1",
      "half":which,
      "theorems":names,
      "axioms":proven,
      "source_sha256":sha(target),
      "manifest_sha256":sha(DEST/"manifest.json"),
      "status":"LEAN KERNEL PASS, 2 actual original HD/A half-gate theorems strict standard-axiom PASS",
      "full_original_row_one_accepted":False,
    }
    Path(f"nf728-{which.lower()}-audit.json").write_text(
       json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print(f"NF728 actual original {which} HD and A half theorems LEAN PASS — 2 real numerical source-bound claims, full row pending")


def verify_complete():
    source_verify()
    proofs=strict_axioms("nf728-complete-axioms.log",FULL_NAMES)
    result={
      "schema":"NF728-original-global-HD-A-index-one-all-lean-audit-v1",
      "new_full_theorems":FULL_NAMES,
      "axioms":proofs,
      "source_sha256":sha(DEST/"ActualComplete.lean"),
      "manifest_sha256":sha(DEST/"manifest.json"),
      "original_global_HD_row_one_all":242,
      "original_global_A_column_one_all":242,
      "status":"LEAN KERNEL PASS with standard axioms; complete original source-bound matrix index-one HD/A universal rows",
      "scope":"Only index 1 HD/A, not full cache, original vector/payment or Weil positivity."
    }
    Path("nf728-complete-audit.json").write_text(
      json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF728 actual original complete HD index-one and A index-one 242/242 universal Lean PASS")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("prepare","source","verify-half","verify-complete"))
    p.add_argument("--half",choices=("Left","Right"))
    a=p.parse_args()
    if a.stage=="prepare":prepare()
    elif a.stage=="source":source_verify()
    elif a.stage=="verify-half":
        assert a.half
        verify_half(a.half)
    else:verify_complete()
