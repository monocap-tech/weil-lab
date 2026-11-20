#!/usr/bin/env python3
"""NF730: produce actual original index-one HD/A half and universal certificates.

Consumes the successful NF729 original 31-block SOURCE-CUSTODY artifact.
That artifact establishes exact provenance and source consistency, NOT that
the 16 newly generated original quad theorems passed Lean. The NF730 four
numerical half proofs and two full numerical universal proofs are also only
CANDIDATES until compiled and axiom-audited against actual accepted original
NF729 numerical quad objects.

The two independent source-free Fin242 four-quad routing theorems are audited
separately and cannot be substituted for numerical gate truth.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from emit_nf630_original_literal_payments import filetext

N=242
SOURCE=Path("WeilDefect/Generated/NF729")
OUTPUT=Path("WeilDefect/Generated/NF730")
STARTS=(0,4,8,12,16,20,24,28)
SIDES={"Left":(0,4,8,12),"Right":(16,20,24,28)}
NAMES=[
    "nf730OriginalHDLeft", "nf730OriginalALeft",
    "nf730OriginalHDRight","nf730OriginalARight",
    "nf730OriginalHDRowOneAll","nf730OriginalAColumnOneAll"
]
ALLOWED={"propext","Classical.choice","Quot.sound"}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def gate(typ,idx):
    if typ=="HD":
        return f"nf703OriginalCache.HDGate nf702OriginalInputs (1 : Fin 242) {idx} = true"
    assert typ=="A"
    return f"nf703OriginalCache.AGate nf702OriginalInputs {idx} (1 : Fin 242) = true"


def input_audit():
    mf=SOURCE/"manifest.json"
    assert mf.is_file()
    m=read(mf)
    assert m["schema"]=="NF729-original-global-index-one-8-quads-source-custody-v1"
    assert m["accepted_index_one_global_product_declarations"]==252
    assert m["accepted_original_index_one_HD_gates"]==N
    assert m["accepted_original_index_one_A_gates"]==N
    assert m["quad_count"]==8
    assert m["new_generic_lean_theorems"]==8
    assert m["new_genuine_original_source_specific_theorems"]==16
    assert len(m["files"])==16
    assert m["files"]=={
        f:sha(SOURCE/f) for f in m["files"]
    }
    assert [q["first_block"] for q in m["quads"]]==list(STARTS)
    assert [q["first_coordinate"] for q in m["quads"]]==[8*b for b in STARTS]
    assert [q["end_coordinate"] for q in m["quads"]]==[
        min(8*(b+4),N) for b in STARTS
    ]
    assert [i for q in m["quads"] for i in range(q["first_coordinate"],q["end_coordinate"])]==list(range(N))
    for q in m["quads"]:
        b=q["first_block"]
        assert q["generic_theorem"]==f"nf729Quad{b:03d}Fin242"
        assert q["actual_theorems"]==[
            f"nf729OriginalHDQuad{b:03d}",f"nf729OriginalAQuad{b:03d}"]
        body=(SOURCE/f"Quad{b:03d}Original.lean").read_text()
        assert re.findall(r"^theorem (nf729Original\w+)",body,re.M)==q["actual_theorems"]
        assert f"nf729Quad{b:03d}Fin242" in body
        assert "nf703OriginalCache.HDGate nf702OriginalInputs" in body
        assert "nf703OriginalCache.AGate nf702OriginalInputs" in body
    return m


def generate_half(side):
    qs=SIDES[side]
    imports=[
      f"WeilDefect.Arithmetic.ActualZetaOriginalPhysicalEightQuad{side}Cover"
    ]+[f"WeilDefect.Generated.NF729.Quad{b:03d}Original" for b in qs]
    body=(
        "set_option maxRecDepth 100000\n"
        "set_option maxHeartbeats 0\n\n"
        f"/-! NF730 genuine original HD/A {side.lower()} index-one half, "
        "requires four REAL original NF729 numerical quad proofs. "
        "This emitted text is a source candidate, not a Lean-accepted certificate. -/\n\n"
    )
    for typ in ("HD","A"):
        name=f"nf730Original{typ}{side}"
        cond="i.val < 128" if side=="Left" else "128 ≤ i.val"
        body+=(
          f"theorem {name} (i : Fin 242) (h : {cond}) :\n"
          f"    {gate(typ,'i')} := by\n"
          f"  exact neutralNF730{side}OfFourQuads\n"
          f"    (fun j : Fin 242 => {gate(typ,'j')})\n"
        )
        body+="".join(
           f"    nf729Original{typ}Quad{b:03d}\n" for b in qs)
        body+="    i h\n\n"
    body+="".join(f"#print axioms nf730Original{typ}{side}\n" for typ in ("HD","A"))
    return filetext(imports,body)


def generate_universal():
    imports=[
        "WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFiniteBinaryGluing",
        "WeilDefect.Generated.NF730.ActualLeft",
        "WeilDefect.Generated.NF730.ActualRight"
    ]
    body=(
       "set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
       "/-! NF730 original HD row one and A column one complete, source-bound to "
       "four actual original numerical half theorems, themselves derived from "
       "16 accepted original NF729 numerical quad theorems. "
       "Lean kernel and strict axiom acceptance still REQUIRED. -/\n\n"
    )
    for typ in ("HD","A"):
        name=f"nf730Original{typ}{'RowOneAll' if typ=='HD' else 'ColumnOneAll'}"
        body+=(
           f"theorem {name} :\n"
           f"    ∀ i : Fin 242, {gate(typ,'i')} := by\n"
           "  exact neutralNF727Fin242OfTwoHalves\n"
           f"    (fun i : Fin 242 => {gate(typ,'i')})\n"
           f"    nf730Original{typ}Left\n"
           f"    nf730Original{typ}Right\n\n"
        )
    body+=(
       "#print axioms nf730OriginalHDRowOneAll\n"
       "#print axioms nf730OriginalAColumnOneAll\n"
    )
    return filetext(imports,body)


def prepare():
    prior=input_audit()
    assert not OUTPUT.exists(),OUTPUT
    OUTPUT.mkdir(parents=True)
    files={
      "ActualLeft.lean":generate_half("Left"),
      "ActualRight.lean":generate_half("Right"),
      "ActualComplete.lean":generate_universal(),
    }
    for f,content in files.items():
        (OUTPUT/f).write_text(content)
    manifest={
      "schema":"NF730-original-HD-A-index-one-8-quad-binary-source-proposals-v1",
      "accepted_nf729_original_SOURCE_provenance_sha256":sha(SOURCE/"manifest.json"),
      "nf729_source_preflight_run":44767040253,
      "nf729_source_preflight_artifact_id":14645281954,
      "prior_original_lean_declarations":252,
      "prior_original_HD_index_one_gates":N,
      "prior_original_A_index_one_gates":N,
      "quads":[
        {"first_block":b,
         "first_coordinate":b*8,
         "end_coordinate":min((b+4)*8,N),
         "needed_numerical_theorems":[
            f"nf729OriginalHDQuad{b:03d}",
            f"nf729OriginalAQuad{b:03d}"]}
        for b in STARTS],
      "new_half_theorems":NAMES[:4],
      "new_universal_theorems":NAMES[4:],
      "source_files":{p:sha(OUTPUT/p) for p in files},
      "proof_status":"Four original half theorems and two original complete all-coordinate claims await Lean kernel acceptance and exact corresponding source-bound original quad gate inputs",
      "scope":"Only HD row index 1 and A column index 1; all remaining global original physical, vector/payment gates, global Weil positivity and RH remain open."
    }
    (OUTPUT/"manifest.json").write_text(json.dumps(manifest,sort_keys=True,indent=2)+"\n")
    source_verify()
    print("NF730 authentic NF729 prior SOURCE-bound original 8-quad HD/A proof candidates assembled into 4 actual half and 2 actual full theorem CANDIDATES; all six new Lean theorems pending kernel")


def source_verify():
    prior=input_audit()
    m=read(OUTPUT/"manifest.json")
    assert m["schema"]=="NF730-original-HD-A-index-one-8-quad-binary-source-proposals-v1"
    assert m["accepted_nf729_original_SOURCE_provenance_sha256"]==sha(SOURCE/"manifest.json")
    assert m["nf729_source_preflight_run"]==44767040253
    assert m["nf729_source_preflight_artifact_id"]==14645281954
    assert m["prior_original_lean_declarations"]==252
    assert m["prior_original_HD_index_one_gates"]==m["prior_original_A_index_one_gates"]==N
    assert m["source_files"]=={p:sha(OUTPUT/p) for p in m["source_files"]}
    assert m["new_half_theorems"]==NAMES[:4]
    assert m["new_universal_theorems"]==NAMES[4:]
    assert [(q["first_coordinate"],q["end_coordinate"]) for q in m["quads"]]==[
      (b*8,min((b+4)*8,N)) for b in STARTS]
    for side,qs in SIDES.items():
        content=(OUTPUT/f"Actual{side}.lean").read_text()
        assert re.findall(r"^theorem (nf730Original\w+)",content,re.M)==[
            f"nf730OriginalHD{side}",f"nf730OriginalA{side}"]
        for typ in ("HD","A"):
            names=re.findall(rf"^    (nf729Original{typ}Quad\d{{3}})$",content,re.M)
            assert names==[f"nf729Original{typ}Quad{b:03d}" for b in qs],(side,typ,names)
        assert not re.search(r"\b(sorry|admit|axiom|unsafe)\b",content)
    final=(OUTPUT/"ActualComplete.lean").read_text()
    assert re.findall(r"^theorem (nf730Original\w+)",final,re.M)==NAMES[4:]
    for name in NAMES[:4]:
        assert name in final
    assert not re.search(r"\b(sorry|admit|axiom|unsafe)\b",final)
    print("NF730 exact 8 original quad source coordinates; two HD/A original half and two complete original numerical theorems source preflight PASS; kernel UNPROVED")


def axioms(log,expected):
    text=Path(log).read_text()
    found={}
    for name,raw in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",text):
        if name in expected:
            assert name not in found
            found[name]=[x.strip() for x in raw.split(",") if x.strip()]
    for name in re.findall(r"'WeilDefect\.(\w+)' does not depend on any axioms",text):
        if name in expected:
            assert name not in found
            found[name]=[]
    assert set(found)==set(expected)
    assert all(set(v)<=ALLOWED for v in found.values())
    return found


def verify(which):
    source_verify()
    if which=="Complete":
        names=NAMES[4:]
    else:
        assert which in SIDES
        names=[f"nf730Original{typ}{which}" for typ in ("HD","A")]
    got=axioms(f"nf730-{which.lower()}-axioms.log",names)
    src=OUTPUT/f"Actual{which}.lean"
    out={
       "schema":"NF730-original-HD-A-8-quad-source-specific-kernel-proof-v1",
       "stage":which,
       "theorems":names,
       "axioms":got,
       "source_sha256":sha(src),
       "source_manifest_sha256":sha(OUTPUT/"manifest.json"),
       "numerical_original_gate_truth":True,
       "kernel_status":"LEAN PASS (verified by strict source-specific standard axiom audit)",
       "scope":"Only original index-one HD/A. The theorem is accepted if and only if its actual compiled Lean job and this axiom audit succeeds."
    }
    path=Path(f"nf730-{which.lower()}-audit.json")
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(f"NF730 {which}: two actual original HD/A source-bound numerical Lean theorems KERNEL PASS")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("prepare","source","verify"))
    p.add_argument("--which",choices=("Left","Right","Complete"))
    a=p.parse_args()
    if a.stage=="prepare":prepare()
    elif a.stage=="source":source_verify()
    else:
        assert a.which
        verify(a.which)
