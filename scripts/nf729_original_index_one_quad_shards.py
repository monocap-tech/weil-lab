#!/usr/bin/env python3
"""NF729: split accepted ORIGINAL HD row-one and A column-one proofs into 8 quads.

This reuses *genuine* NF702 input / NF703 center cache / NF700 local products
and the 31 independently accepted NF715..NF720 original global product
declarations, as authenticated in NF728 original source preparation.

32-coordinate quads, except the final 18-coordinate quad:
  [0,32), [32,64), [64,96), [96,128),
  [128,160), [160,192), [192,224), [224,242).

Each quad produces:
  * a standalone Mathlib-only finite-index covering theorem, pending Lean;
  * 2 original HD/A numerical-gate range theorem candidates, pending Lean.
No proof is accepted merely by producing these files.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from emit_nf630_original_literal_payments import filetext

N=242
GROUPS=tuple((i,min(i+4,31)) for i in range(0,31,4))
ROOT=Path("WeilDefect/Generated")
OUT=ROOT/"NF729"
ORIGINAL=ROOT/"NF728"
ALLOWED={"propext","Classical.choice","Quot.sound"}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    return json.loads(Path(p).read_text())


def offset(b):
    return 8*b


def end(b):
    return min(offset(b+1),N)


def stage(i):
    return 715 if i==0 else 716 if i<4 else 717 if i<8 else (
        718 if i<16 else 719 if i<24 else 720)


def hyp(i):
    n=end(i)-offset(i)
    pos="k.val" if i==0 else f"{offset(i)} + k.val"
    return f"(h{i:03d} : ∀ k : Fin {n}, P (⟨{pos}, by omega⟩ : Fin 242))"


def at(i):
    pos="k.val" if i==0 else f"{offset(i)} + k.val"
    return f"(⟨{pos}, by omega⟩ : Fin 242)"


def actual_formula(t,index="j"):
    if t=="HD":
        return f"nf703OriginalCache.HDGate nf702OriginalInputs (1 : Fin 242) {index} = true"
    assert t=="A"
    return f"nf703OriginalCache.AGate nf702OriginalInputs {index} (1 : Fin 242) = true"


def original():
    prior=read(ORIGINAL/"manifest.json")
    assert prior["schema"]=="NF728-original-global-HD-A-binary-half-source-candidates-v1"
    assert prior["nf727_original_compiler_preflight_run"]==44760318280
    assert prior["nf727_original_preflight_artifact_id"]==14641426213
    assert prior["accepted_prior_global_product_theorem_declarations"]==252
    assert prior["accepted_original_index_one_HD_coordinate_gates"]==242
    assert prior["accepted_original_index_one_A_coordinate_gates"]==242
    assert len(prior["blocks"])==31
    assert prior["half_ranges"]==[
        {"part":"Left","first":0,"end":128},
        {"part":"Right","first":128,"end":242}]
    assert prior["files"]=={k:sha(ORIGINAL/k) for k in prior["files"]}
    originals=prior["blocks"]
    for i,b in enumerate(originals):
        assert (b["number"],b["first"],b["end"])==(i,offset(i),end(i))
        assert b["accepted_original_stage"]==f"NF{stage(i)}"
        assert b["globalHD"]==f"nf{stage(i)}Block{i:03d}GlobalHD"
        assert b["globalA"]==f"nf{stage(i)}Block{i:03d}GlobalA"
        src=ROOT/f"NF{stage(i)}"/f"Block{i:03d}.lean"
        assert src.is_file(),src
        content=src.read_text()
        for typ in ("HD","A"):
            assert f"theorem {b['global'+typ]}" in content,(i,typ)
            assert actual_formula(typ).split(" (1 : Fin 242)")[0].split(" i")[0] in (
              "nf703OriginalCache.HDGate nf702OriginalInputs",
              "nf703OriginalCache.AGate nf702OriginalInputs")
    assert [n for b in originals for n in range(b["first"],b["end"])]==list(range(N))
    return prior


def generic(i,j):
    assert (i,j) in GROUPS
    upper=end(j-1)
    title=f"nf729Quad{i:03d}Fin242"
    lines=[
      f"/-- Original bounded quad {i:03d}: exactly Fin 242 entries [{offset(i)},{upper}). -/",
      f"theorem {title}",
      "    (P : Fin 242 → Prop)",
      *[f"    {hyp(b)}" for b in range(i,j)],
      f"    (index : Fin 242) (hlo : {offset(i)} ≤ index.val) (hhi : index.val < {upper}) : P index := by"
    ]
    for k,b in enumerate(range(i,j)):
        indent="  "+"  "*k
        if b!=j-1:
            lines.append(indent+f"by_cases hs{b:03d} : index.val < {end(b)}")
            lines.append(indent+"·")
            indent+="  "
        # last branch sits one level deeper than prior else bullet
        n=end(b)-offset(b)
        term="index.val" if b==0 else f"index.val - {offset(b)}"
        lines.extend([
          indent+f"let k : Fin {n} := ⟨{term}, by omega⟩",
          indent+f"have hk : {at(b)} = index := by",
          indent+"  apply Fin.ext",
          indent+"  dsimp [k] <;> omega",
          indent+f"simpa only [hk] using h{b:03d} k",
        ])
        if b!=j-1:
            lines.append("  "+"  "*k+"·")
    return (
        "import Mathlib.Tactic\n\nnamespace WeilDefect\n\n"
        "/-! NF729 standalone exact original Fin242 quad-bound proof. "
        "No numerical matrix object is imported. -/\n\n"
        +"\n".join(lines)
        +f"\n\n#print axioms {title}\n\nend WeilDefect\n"
    )


def actual(i,j):
    assert (i,j) in GROUPS
    imports=[f"WeilDefect.Generated.NF729.Quad{i:03d}Finite"] + [
       f"WeilDefect.Generated.NF{stage(b)}.Block{b:03d}" for b in range(i,j)]
    title=f"nf729Quad{i:03d}Fin242"
    result="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
    result+=f"/-! NF729: genuine ORIGINAL HD/A numerical-product gates for [{offset(i)},{end(j-1)}). Four or fewer separately accepted literal global product proof families. Lean kernel acceptance pending. -/\n\n"
    for t in ("HD","A"):
        name=f"nf729Original{t}Quad{i:03d}"
        result+=(
            f"theorem {name} (index : Fin 242) (hlo : {offset(i)} ≤ index.val) "
            f"(hhi : index.val < {end(j-1)}) :\n"
            f"    {actual_formula(t,'index')} := by\n"
            f"  exact {title}\n"
            f"    (fun j : Fin 242 => {actual_formula(t,'j')})\n"
        )
        result+="".join(f"    nf{stage(b)}Block{b:03d}Global{t}\n" for b in range(i,j))
        result+="    index hlo hhi\n\n"
    result+=f"#print axioms nf729OriginalHDQuad{i:03d}\n"
    result+=f"#print axioms nf729OriginalAQuad{i:03d}\n"
    return filetext(imports,result)


def prepare():
    m=original()
    assert not OUT.exists(),OUT
    OUT.mkdir(parents=True)
    contents={}
    blocks=[]
    for i,j in GROUPS:
        for kind,txt in (("Finite",generic(i,j)),("Original",actual(i,j))):
            filename=f"Quad{i:03d}{kind}.lean"
            (OUT/filename).write_text(txt)
            contents[filename]=sha(OUT/filename)
        blocks.append({
            "first_block":i,"end_block":j,
            "first_coordinate":offset(i),
            "end_coordinate":end(j-1),
            "accepted_source_stages":[stage(b) for b in range(i,j)],
            "accepted_actual_global_HD":[m["blocks"][b]["globalHD"] for b in range(i,j)],
            "accepted_actual_global_A":[m["blocks"][b]["globalA"] for b in range(i,j)],
            "generic_theorem":f"nf729Quad{i:03d}Fin242",
            "actual_theorems":[f"nf729OriginalHDQuad{i:03d}",f"nf729OriginalAQuad{i:03d}"],
        })
    assert [k for v in blocks for k in range(v["first_coordinate"],v["end_coordinate"])]==list(range(N))
    manifest={
      "schema":"NF729-original-global-index-one-8-quads-source-custody-v1",
      "accepted_earlier_original_source_manifest_sha256":sha(ORIGINAL/"manifest.json"),
      "accepted_index_one_global_product_declarations":252,
      "accepted_original_index_one_HD_gates":N,
      "accepted_original_index_one_A_gates":N,
      "quad_count":8,
      "quads":blocks,
      "files":contents,
      "new_generic_lean_theorems":8,
      "new_genuine_original_source_specific_theorems":16,
      "proof_status":"24 new Lean declarations require independently passing kernel; original full row/column still pending",
      "scope":"Original source-specific HD row-one/A column-one only. Full numerical enclosure and global Weil positivity remain open.",
    }
    (OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
    print("NF729 SOURCE BOUND: genuine original 31 accepted HD/A gate blocks partitioned into 8 independent quads / 8 generic and 16 actual new Lean proof candidates, kernel pending")


def check_sources():
    m=original()
    cert=read(OUT/"manifest.json")
    assert cert["schema"]=="NF729-original-global-index-one-8-quads-source-custody-v1"
    assert cert["accepted_earlier_original_source_manifest_sha256"]==sha(ORIGINAL/"manifest.json")
    assert cert["files"]=={k:sha(OUT/k) for k in cert["files"]}
    assert len(cert["files"])==16
    assert len(cert["quads"])==8
    assert cert["quad_count"]==8
    assert [(x["first_block"],x["end_block"]) for x in cert["quads"]]==list(GROUPS)
    for x in cert["quads"]:
        i,j=x["first_block"],x["end_block"]
        assert x["first_coordinate"]==offset(i) and x["end_coordinate"]==end(j-1)
        assert x["accepted_actual_global_HD"]==[m["blocks"][b]["globalHD"] for b in range(i,j)]
        assert x["accepted_actual_global_A"]==[m["blocks"][b]["globalA"] for b in range(i,j)]
        generic_src=(OUT/f"Quad{i:03d}Finite.lean").read_text()
        actual_src=(OUT/f"Quad{i:03d}Original.lean").read_text()
        assert generic_src.startswith("import Mathlib.Tactic\n")
        assert re.findall(r"^theorem (nf729\w+)",generic_src,re.M)==[x["generic_theorem"]]
        assert re.findall(r"^theorem (nf729\w+)",actual_src,re.M)==x["actual_theorems"]
        assert not re.search(r"\b(sorry|admit|axiom|unsafe)\b",generic_src+actual_src)
        for b in range(i,j):
            assert hyp(b) in generic_src
            assert f"nf{stage(b)}Block{b:03d}GlobalHD" in actual_src
            assert f"nf{stage(b)}Block{b:03d}GlobalA" in actual_src
    assert [k for v in cert["quads"] for k in range(v["first_coordinate"],v["end_coordinate"])]==list(range(N))
    print("NF729 exact original source-specific HD/A gates 242/242 each, 8 finite quads and 16 original theorem candidates SOURCE PREFLIGHT PASS, no claim of new kernel truth")


def axioms(log_path,expected):
    log=Path(log_path).read_text()
    found={}
    for name,raw in re.findall(
        r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
        if name in expected:
            assert name not in found
            found[name]=[z.strip() for z in raw.split(",") if z.strip()]
    for name in re.findall(
        r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
        if name in expected:
            assert name not in found
            found[name]=[]
    assert set(found)==set(expected),(expected,found)
    assert all(set(v)<=ALLOWED for v in found.values())
    return found


def verify(i,kind):
    assert (i,i+4) in GROUPS or (i,31) in GROUPS
    check_sources()
    assert kind in ("Finite","Original")
    names=([f"nf729Quad{i:03d}Fin242"] if kind=="Finite" else
       [f"nf729Original{t}Quad{i:03d}" for t in ("HD","A")])
    got=axioms(f"nf729-{i:03d}-{kind.lower()}-axioms.log",names)
    receipt={
      "schema":"NF729-independent-original-quad-lean-kernel-audit-v1",
      "kind":kind,"quad_first_block":i,
      "quad_first_coordinate":offset(i),
      "quad_end_coordinate":end(next(j for a,j in GROUPS if a==i)-1),
      "theorems":names,"axioms":got,
      "source_sha256":sha(OUT/f"Quad{i:03d}{kind}.lean"),
      "manifest_sha256":sha(OUT/"manifest.json"),
      "status":"LEAN KERNEL PASS, source-specific global HD/A original gate claims" if kind=="Original" else "LEAN KERNEL PASS, finite index partition only"
    }
    Path(f"nf729-{i:03d}-{kind.lower()}-audit.json").write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print(f"NF729 quad {i:03d} {kind} kernel/strict axiom PASS; standalone new theorem(s) accepted")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("prepare","source","verify"))
    p.add_argument("--quad",type=int,choices=[i for i,_ in GROUPS])
    p.add_argument("--kind",choices=("Finite","Original"))
    a=p.parse_args()
    if a.stage=="prepare":prepare()
    elif a.stage=="source":check_sources()
    else:
        assert a.quad is not None and a.kind
        verify(a.quad,a.kind)
