#!/usr/bin/env python3
"""Create an exact width-four packed-product pilot from NF681's pinned literals.

No original product equality is used as a premise of the packed proof.
Bounds and the packed identity are kernel-decided, not assumed.
The direct reference uses the identical literal data and targets.
"""
import argparse,hashlib,json,re,sys
from pathlib import Path
from emit_nf630_original_literal_payments import filetext
sys.set_int_max_str_digits(0)
MOD="WeilDefect.Generated.NF683"
CORE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedProducts"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
N=242
W=4
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def vec(src,name):
    m=re.search(r"def "+name+r"Data : Array ℤ := #\[(.*?)\]",src,re.S)
    assert m,name
    vals=list(map(int,re.findall(r"\((-?\d+):ℤ\)",m.group(1))))
    assert len(vals)==N,(name,len(vals))
    return vals
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--frontier",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    m=json.loads((a.frontier/"manifest.json").read_text())
    assert m["schema"]=="NF681-original-matrix-frontier-v1"
    assert (m["HD_exact_external"],m["A_exact_external"],m["literal_gate_count"])==(242,242,484)
    hashes={r["file"]:r["sha256"] for r in m["files"]}
    for name in ["Common.lean",*[f"Col{i:03d}.lean" for i in range(W)]]:
        assert sha(a.frontier/name)==hashes[name],name
    common=(a.frontier/"Common.lean").read_text()
    cols=[(a.frontier/f"Col{i:03d}.lean").read_text() for i in range(W)]
    D=[vec(c,f"nf681Col{i:03d}") for i,c in enumerate(cols)]
    h=vec(common,"nf681HRow0")
    pcol=vec(common,"nf681HDCol0")
    hd=vec(common,"nf681HDRow0")[:W]
    ar=vec(common,"nf681ACol0")[:W]
    a.output.mkdir(parents=True,exist_ok=True)
    files=[]
    def write(name,imports,body):
        q=a.output/(name+".lean")
        q.write_text(filetext(imports,OPT+body),encoding="utf8")
        files.append({"file":q.name,"sha256":sha(q)})
    # Copy the exact original definitions, not any proof of the direct products.
    def body_of(s):
        return s.split("namespace WeilDefect\n",1)[1].rsplit("end WeilDefect",1)[0].strip()
    body=body_of(common)
    for i,c in enumerate(cols):
        body+="\n\n"+body_of(c).split(f"theorem nf681Col{i:03d}HD",1)[0].strip()
    body+="\n\ndef nf683Y (k : Fin 242) (j : Fin 4) : ℤ :=\n"
    body+="  (#[nf681Col000, nf681Col001, nf681Col002, nf681Col003] : Array (Fin 242 → ℤ))[j.val]! k\n"
    body+="\ndef nf683HDTarget (j : Fin 4) : ℤ := nf681HDRow0 ⟨j.val, by omega⟩\n"
    body+="\ndef nf683ATarget (j : Fin 4) : ℤ := nf681ACol0 ⟨j.val, by omega⟩\n"
    write("Data",[CORE],body)
    M=max(abs(v) for col in D for v in col)
    Mlit=f"({M}:ℤ)"
    bounds=f"""def nf683M : ℤ := {Mlit}
theorem nf683M_nonneg : 0 ≤ nf683M := by
  decide +kernel
theorem nf683OperandGate :
    (List.finRange 242).all (fun k =>
      (List.finRange 4).all (fun j => decide (|nf683Y k j| ≤ nf683M))) = true := by
  decide +kernel
theorem nf683OperandBound (k : Fin 242) (j : Fin 4) :
    |nf683Y k j| ≤ nf683M := by
  have hk := (List.all_eq_true.mp nf683OperandGate) k (by simp)
  exact of_decide_eq_true ((List.all_eq_true.mp hk) j (by simp))

#print axioms nf683M_nonneg
#print axioms nf683OperandGate
#print axioms nf683OperandBound
"""
    write("Bounds",[MOD+".Data"],bounds)
    audit=[]
    sizes={}
    for label,x,z,xname,zname in (("HD",h,hd,"nf681HRow0","nf683HDTarget"),
                                   ("A",pcol,ar,"nf681HDCol0","nf683ATarget")):
        X=sum(map(abs,x)); Z=max(map(abs,z)); B=1<<(X*M+Z).bit_length()
        assert B>0 and X*M+Z<B
        assert all(sum(xi*yi for xi,yi in zip(x,col))==v for col,v in zip(D,z))
        pack=lambda vs:sum(v*B**i for i,v in enumerate(vs))
        assert sum(x[k]*pack([D[j][k] for j in range(W)]) for k in range(N))==pack(z)
        z0=f"nf683{label}"
        body=f"""def {z0}X : ℤ := ({X}:ℤ)
def {z0}Z : ℤ := ({Z}:ℤ)
def {z0}Base : ℤ := ({B}:ℤ)

theorem {z0}Mass : (∑ k, |{xname} k|) ≤ {z0}X := by
  decide +kernel
theorem {z0}TargetGate :
    (List.finRange 4).all (fun j => decide (|{zname} j| ≤ {z0}Z)) = true := by
  decide +kernel
theorem {z0}TargetBound (j : Fin 4) : |{zname} j| ≤ {z0}Z :=
  of_decide_eq_true ((List.all_eq_true.mp {z0}TargetGate) j (by simp))
theorem {z0}BasePos : 0 < {z0}Base := by
  decide +kernel
theorem {z0}Gap : {z0}X * nf683M + {z0}Z < {z0}Base := by
  decide +kernel
theorem {z0}PackedEquality :
    neutralNF626Dot {xname}
      (fun k => neutralNF683Pack {z0}Base (nf683Y k)) =
      neutralNF683Pack {z0}Base {zname} := by
  decide +kernel

theorem {z0}AllCoordinates (j : Fin 4) :
    neutralNF626Dot {xname} (fun k => nf683Y k j) = {zname} j :=
  neutralNF683PackedProducts {xname} nf683Y {zname}
    {z0}X nf683M {z0}Z {z0}Base {z0}BasePos {z0}Mass
    nf683M_nonneg nf683OperandBound {z0}TargetBound {z0}Gap {z0}PackedEquality j

"""
        names=[z0+s for s in ("Mass","TargetGate","TargetBound","BasePos","Gap","PackedEquality","AllCoordinates")]
        body+="\n".join("#print axioms "+name for name in names)
        write("Packed"+label,[MOD+".Bounds"],body)
        audit+=names
        body=f"""theorem {z0}Direct (j : Fin 4) :
    neutralNF626Dot {xname} (fun k => nf683Y k j) = {zname} j := by
  fin_cases j <;> decide +kernel

#print axioms {z0}Direct
"""
        write("Direct"+label,[MOD+".Data"],body)
        audit.append(z0+"Direct")
        sizes[label]={"base_bits":B.bit_length(),"packed_width":W,"products":N*W}
    audit+=["nf683M_nonneg","nf683OperandGate","nf683OperandBound"]
    audit+=["neutralNF683Pack_succ","neutralNF683Pack_zero_small","neutralNF683Pack_sub","neutralNF683Pack_injective_bounded","neutralNF683Pack_dot","neutralNF683Dot_error_bound","neutralNF683PackedProducts"]
    (a.output/"manifest.json").write_text(json.dumps(
        {"schema":"NF683-packed-original-frontier-pilot-v1","frontier_manifest_sha256":sha(a.frontier/"manifest.json"),"original_sources":{k:hashes[k] for k in ["Common.lean",*[f"Col{i:03d}.lean" for i in range(W)]]},"files":files,
         "audit_theorems":audit,"width":W,"coordinate_identities":2*W,"sizes":sizes,
         "scope":"Actual original first four frontier coordinates per matrix; direct and packed proof candidates only."},indent=2)+"\n")
    print("NF683 eight authentic original products externally replayed; packed and direct Lean candidates emitted",sizes)
if __name__=="__main__":main()
