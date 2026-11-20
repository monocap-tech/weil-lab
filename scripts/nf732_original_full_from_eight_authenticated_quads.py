#!/usr/bin/env python3
"""NF732: exact original physical index-one HD/A full-row proof handoff.

Source stage regenerates literal genuine NF702/NF703 complete HD row-one and
A column-one source candidates from NF729's accepted original-source bank.
This only establishes provenance of proof terms, not new kernel acceptance.

The single Mathlib-only Fin242 eight-range logical master is independently
kernel audited. New original universal theorems are kernel accepted only if
eight source-bound NF729 numerical quad proof object receipts are accepted,
the final generated Lean module compiles and its two axioms audits pass.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from emit_nf630_original_literal_payments import filetext

SRC = Path("WeilDefect/Generated/NF729")
DEST = Path("WeilDefect/Generated/NF732")
LOGICAL = Path("WeilDefect/Arithmetic/ActualZetaOriginalPhysicalEightQuadFullCover.lean")
STARTS = (0,4,8,12,16,20,24,28)
ALLOWED = {"propext","Classical.choice","Quot.sound"}
NUMERICAL = ("nf732OriginalHDRowOneAll","nf732OriginalAColumnOneAll")
LOGICAL_NAME = "neutralNF732AllFin242OfEightQuads"

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(path):
    return json.loads(Path(path).read_text())

def predicate(typ,index="i"):
    if typ=="HD":
        return (f"nf703OriginalCache.HDGate nf702OriginalInputs "
                f"(1 : Fin 242) {index} = true")
    assert typ=="A"
    return (f"nf703OriginalCache.AGate nf702OriginalInputs "
            f"{index} (1 : Fin 242) = true")

def original_source():
    p = SRC/"manifest.json"
    assert p.is_file()
    m=read(p)
    assert m["schema"]=="NF729-original-global-index-one-8-quads-source-custody-v1"
    assert m["accepted_index_one_global_product_declarations"]==252
    assert m["accepted_original_index_one_HD_gates"]==242
    assert m["accepted_original_index_one_A_gates"]==242
    assert m["new_generic_lean_theorems"]==8
    assert m["new_genuine_original_source_specific_theorems"]==16
    assert m["quad_count"]==8
    assert m["files"]=={k:sha(SRC/k) for k in m["files"]}
    assert set(m["files"])=={f"Quad{b:03d}{suffix}.lean" for b in STARTS
      for suffix in ("Finite","Original")}
    assert [(q["first_block"],q["first_coordinate"],q["end_coordinate"])
      for q in m["quads"]]==[
      (b,b*8,min((b+4)*8,242)) for b in STARTS]
    assert [j for q in m["quads"]
      for j in range(q["first_coordinate"],q["end_coordinate"])]==list(range(242))
    assert isinstance(m["accepted_earlier_original_source_manifest_sha256"],str)
    assert len(m["accepted_earlier_original_source_manifest_sha256"])==64
    for b,q in zip(STARTS,m["quads"]):
        assert q["generic_theorem"]==f"nf729Quad{b:03d}Fin242"
        assert q["actual_theorems"]==[
          f"nf729OriginalHDQuad{b:03d}",
          f"nf729OriginalAQuad{b:03d}"]
        s=(SRC/f"Quad{b:03d}Original.lean").read_text()
        assert re.findall(r"^theorem (nf729Original\w+)",s,re.M)==q["actual_theorems"]
        assert re.findall(r"^    (nf\d+Block\d{3}GlobalHD)$",s,re.M)==q["accepted_actual_global_HD"]
        assert re.findall(r"^    (nf\d+Block\d{3}GlobalA)$",s,re.M)==q["accepted_actual_global_A"]
        assert predicate("HD","index") in s
        assert predicate("A","index") in s
        assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",s,re.M)
    return m

def pure_source():
    s=LOGICAL.read_text()
    assert s.startswith("import Mathlib.Tactic\n")
    assert re.findall(r"^theorem (neutralNF732\w+)",s,re.M)==[LOGICAL_NAME]
    for b in STARTS:
        start=b*8
        end=min((b+4)*8,242)
        assert f"(q{b:03d} : ∀ i : Fin 242, {start} ≤ i.val → i.val < {end} → P i)" in s
        assert f"exact q{b:03d} i (by omega)" in s
    assert "#print axioms "+LOGICAL_NAME in s
    assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",s,re.M)
    return sha(LOGICAL)

def emit():
    m=original_source()
    digest=pure_source()
    assert not DEST.exists(),DEST
    DEST.mkdir(parents=True)
    imports=[
       "WeilDefect.Arithmetic.ActualZetaOriginalPhysicalEightQuadFullCover"
    ]+[
       f"WeilDefect.Generated.NF729.Quad{b:03d}Original" for b in STARTS
    ]
    body=(
      "set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
      "/-! NF732 actual ORIGINAL NF702/NF703 global index-one HD row and "
      "A column. These proof statements use 8 genuine NF729 source-specific "
      "original gate-range theorems, never mere source-only assumptions. "
      "Both new declarations require independent Lean kernel acceptance. -/\n\n"
    )
    for name,typ in zip(NUMERICAL,("HD","A")):
        body+=(
           f"theorem {name} :\n"
           f"    ∀ i : Fin 242, {predicate(typ)} := by\n"
           "  exact neutralNF732AllFin242OfEightQuads\n"
           f"    (fun i : Fin 242 => {predicate(typ)})\n"
        )
        body+="".join(f"    nf729Original{typ}Quad{b:03d}\n" for b in STARTS)
        body+="\n"
    body+="".join(f"#print axioms {name}\n" for name in NUMERICAL)
    path=DEST/"ActualOriginalFull.lean"
    path.write_text(filetext(imports,body))
    manifest={
       "schema":"NF732-exact-original-physical-global-HD-A-index-one-8-quad-full-source-v1",
       "source":str(path),
       "source_sha256":sha(path),
       "accepted_source_provenance_manifest_sha256":sha(SRC/"manifest.json"),
       "accepted_prior_NF728_original_bank_manifest_sha256":
           m["accepted_earlier_original_source_manifest_sha256"],
       "nf729_original_source_preflight_run_id":44767040253,
       "nf729_original_source_preflight_artifact_id":14645281954,
       "accepted_original_global_gate_coordinate_counts":{"HD":242,"A":242},
       "accepted_prior_original_theorem_declarations":252,
       "required_NF729_numerical_quad_modules":[
           f"WeilDefect.Generated.NF729.Quad{b:03d}Original" for b in STARTS],
       "required_NF729_numerical_quad_theorems":[
           name for b in STARTS for name in
            (f"nf729OriginalHDQuad{b:03d}",f"nf729OriginalAQuad{b:03d}")],
       "required_pure_gluing_source_sha256":digest,
       "new_original_universal_theorems":list(NUMERICAL),
       "proof_status":"Original source-authenticated two full index-one theorem CANDIDATES; actual original 8 numerical quad kernels and this final Lean module require independent acceptance",
       "scope":"Actual original HD row index 1 and A column index 1 only. Other matrix indices, original vector and payment rows, full numerical enclosure, global Weil positivity and RH remain OPEN."
    }
    (DEST/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
    source()
    print("NF732 actual original complete HD/A index-one 242 + 242 source candidates emitted from 8 source-authenticated exact quad families; NEW complete Lean theorems UNPROVED")

def source():
    m=original_source()
    dig=pure_source()
    cert=read(DEST/"manifest.json")
    p=DEST/"ActualOriginalFull.lean"
    s=p.read_text()
    assert cert["schema"]=="NF732-exact-original-physical-global-HD-A-index-one-8-quad-full-source-v1"
    assert cert["source_sha256"]==sha(p)
    assert cert["accepted_source_provenance_manifest_sha256"]==sha(SRC/"manifest.json")
    assert cert["accepted_prior_NF728_original_bank_manifest_sha256"]==m["accepted_earlier_original_source_manifest_sha256"]
    assert cert["required_pure_gluing_source_sha256"]==dig
    assert cert["new_original_universal_theorems"]==list(NUMERICAL)
    imports=re.findall(r"^import (WeilDefect\.Generated\.NF729\.Quad\d{3}Original)$",s,re.M)
    assert imports==cert["required_NF729_numerical_quad_modules"]
    assert re.findall(r"^theorem (nf732Original\w+)",s,re.M)==list(NUMERICAL)
    for typ in ("HD","A"):
        required=[f"nf729Original{typ}Quad{b:03d}" for b in STARTS]
        found=re.findall(rf"^    (nf729Original{typ}Quad\d{{3}})$",s,re.M)
        assert found==required,(typ,found)
        assert predicate(typ) in s
    assert s.count("exact neutralNF732AllFin242OfEightQuads")==2
    assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",s,re.M)
    print("NF732 source custody: immutable authentic 31 original blocks, 8 original HD and 8 original A accepted-source quad candidates, exactly 2 complete original Lean theorem candidates; new kernel acceptance pending")

def axioms(path,names):
    log=Path(path).read_text()
    found={}
    for name,raw in re.findall(
       r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
        if name in names:
            assert name not in found,name
            found[name]=[x.strip() for x in raw.split(",") if x.strip()]
    for name in re.findall(
       r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
        if name in names:
            assert name not in found,name
            found[name]=[]
    assert set(found)==set(names),(found,names)
    assert all(set(a)<=ALLOWED for a in found.values())
    return found

def verify_pure():
    src=pure_source()
    found=axioms("nf732-pure-axioms.log",[LOGICAL_NAME])
    result={
       "schema":"NF732-pure-8-range-original-Fin242-full-cover-lean-kernel-v1",
       "source_sha256":src,"theorem":LOGICAL_NAME,
       "axioms":found,
       "kernel_status":"LEAN PASS; standard axioms only",
       "actual_original_numerical_gate_claimed":False
    }
    Path("nf732-pure-accepted-audit.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF732 pure original-coordinate 8-range to Fin242 full gluing LEAN PASS, numerical product truth remains a separate kernel obligation")

def verify_original():
    source()
    found=axioms("nf732-original-axioms.log",list(NUMERICAL))
    master=read("nf732-accepted-original-numerical-inputs.json")
    assert master["schema"]=="NF732-original-eight-accepted-NF729-numerical-quad-olean-inputs-v1"
    assert [x["quad"] for x in master["sources"]]==list(STARTS)
    assert master["all_eight_accepted_original_quad_kernel_runs"] is True
    assert master["eight_original_gate_ranges_complete_Fin242"] is True
    for x in master["sources"]:
        assert x["source_manifest_sha256"]==sha(SRC/"manifest.json")
        assert x["original_source_sha256"]==sha(SRC/f"Quad{x['quad']:03d}Original.lean")
        assert x["olean_sha256"]==sha(
          Path(".lake/build/lib/lean/WeilDefect/Generated/NF729")/
          f"Quad{x['quad']:03d}Original.olean"
        )
    cert={
       "schema":"NF732-actual-original-HD-and-A-complete-index-one-lean-kernel-v1",
       "source_sha256":sha(DEST/"ActualOriginalFull.lean"),
       "source_manifest_sha256":sha(DEST/"manifest.json"),
       "upstream_8_accepted_quad_lean_objects_sha256":sha("nf732-accepted-original-numerical-inputs.json"),
       "theorems":list(NUMERICAL),"axioms":found,
       "HD_row_index":1,"A_column_index":1,
       "HD_actual_original_gate_coordinates":242,
       "A_actual_original_gate_coordinates":242,
       "status":"Lean KERNEL PASS; two genuine original complete source-bound HD/A index-one universal theorems and standard axiom audit PASSED",
       "scope":"Index one only. Full original all-indices numerical enclosure custody, payment, global Weil positivity and RH remain open."
    }
    Path("nf732-original-complete-audit.json").write_text(
       json.dumps(cert,indent=2,sort_keys=True)+"\n")
    print("NF732 actual original index-one HD row and A column each 242/242 complete universal Lean theorem PASSED; no other full-matrix claim")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("prepare","source","pure","original"))
    a=p.parse_args()
    if a.stage=="prepare":emit()
    elif a.stage=="source":source()
    elif a.stage=="pure":verify_pure()
    else:verify_original()
