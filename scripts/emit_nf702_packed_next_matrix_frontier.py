#!/usr/bin/env python3
"""NF702: exact next original HD row and A column via bounded signed-digit packing."""
import argparse,gzip,json,sys
from pathlib import Path
from fractions import Fraction as F
from emit_nf630_original_literal_payments import historical,payment_receipt,rat,array,filetext,sha
from verify_nf623_uniform_physical_payments import N,Q,FROZEN_SHA
sys.set_int_max_str_digits(0)
MOD="WeilDefect.Generated.NF702"
BASE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedProducts"
W=8
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def dot(x,y):
    assert len(x)==len(y)
    return sum(a*b for a,b in zip(x,y))
def main():
    p=argparse.ArgumentParser()
    for k in ("root","historical","entries","payments","cache","output"):
        p.add_argument("--"+k,type=Path,required=True)
    p.add_argument("--index",type=int,required=True,choices=range(2,6))
    a=p.parse_args()
    I=a.index
    D,S,y,U,w,T,mid,rad,frame=historical(a.root,a.historical)
    assert N==242
    eh,dh=sha(a.entries),sha(a.historical)
    pay=payment_receipt(a.payments,eh,frame)
    lower=[];EH=EV=0
    with gzip.open(a.entries,"rt") as f:
        h=json.loads(next(f))
        assert h["schema"]=="NF622-original-physical-entry-balls-v1" and h["scale"]=="10^2600"
        for i,line in enumerate(f):
            q=json.loads(line)
            assert q["row"]==i<N and len(q["H_lower"])==i+1 and len(q["V"])==4
            lower.append([int(x[0]) for x in q["H_lower"]])
            for x,e in q["H_lower"]:
                assert int(e)>=0
                EH=max(EH,int(e))
            for x,e in q["V"]:
                assert int(e)>=0
                EV=max(EV,int(e))
    assert len(lower)==N
    H0=[lower[max(I,j)][min(I,j)] for j in range(N)]
    assert rat(pay["uniform_H_radius"])==F(EH,Q) and rat(pay["uniform_V_radius"])==F(EV,Q)
    HDrow=[];HDcol=[];Acol=[]
    with gzip.open(a.cache,"rt") as f:
        h=json.loads(next(f))
        assert h["schema"]=="NF626-integer-center-cache-v1"
        assert h["entry_sha256"]==eh and h["historical_sha256"]==dh
        assert h["frame_sha256"]==frame and h["frozen_sha256"]==FROZEN_SHA
        assert {k:int(v) for k,v in h["scales"].items()}==dict(S=S,Q=Q,T=T,U=U)
        assert list(map(int,h["y"]))==y and list(map(int,h["w"]))==w
        assert [rat(h[k]) for k in ("eH","eV","r")]==[rat(pay[k]) for k in ("uniform_H_radius","uniform_V_radius","r")]
        for i,line in enumerate(f):
            q=json.loads(line)
            assert q["i"]==i<N and len(q["HD"])==N and len(q["A"])==N
            if i==I: HDrow=list(map(int,q["HD"]))
            HDcol.append(int(q["HD"][I]))
            Acol.append(int(q["A"][I]))
    assert len(HDrow)==len(HDcol)==len(Acol)==N
    assert HDrow[I]==HDcol[I]
    a.output.mkdir(parents=True,exist_ok=True)
    files=[];blocks=[]
    def write(name,imports,body):
        f=a.output/(name+".lean")
        f.write_text(filetext(imports,OPT+body))
        files.append({"file":f.name,"sha256":sha(f)})
    def vec(name,values,n):
        return (f"def {name}Data : Array ℤ := {array(values)}\n\n"
                f"def {name} (i : Fin {n}) : ℤ := {name}Data[i.val]!\n\n")
    common=vec("nf702HRow",H0,N)+vec("nf702HDCol",HDcol,N)
    write("Common",[BASE],common)
    for start in range(0,N,W):
        stop=min(start+W,N); w=stop-start
        block=f"Block{start//W:03d}"; z="nf702"+block
        cols=[[D[k][j] for k in range(N)] for j in range(start,stop)]
        hd=HDrow[start:stop]; ac=Acol[start:stop]
        assert all(dot(H0,c)==v for c,v in zip(cols,hd)),("HD",start)
        assert all(dot(c,HDcol)==v for c,v in zip(cols,ac)),("A",start)
        body="".join(vec(f"{z}D{j}",col,N) for j,col in enumerate(cols))
        body+=f"def {z}Y (k : Fin 242) (j : Fin {w}) : ℤ :=\n  (#["
        body+=", ".join(f"{z}D{j}" for j in range(w))+f"] : Array (Fin 242 → ℤ))[j.val]! k\n\n"
        body+=vec(z+"HDTarget",hd,w)+vec(z+"ATarget",ac,w)
        M=max(abs(v) for col in cols for v in col)
        body+=f"""def {z}M : ℤ := ({M}:ℤ)
theorem {z}M_nonneg : 0 ≤ {z}M := by
  decide +kernel
theorem {z}OperandGate :
    (List.finRange 242).all (fun k =>
      (List.finRange {w}).all (fun j => decide (|{z}Y k j| ≤ {z}M))) = true := by
  decide +kernel
theorem {z}OperandBound (k : Fin 242) (j : Fin {w}) :
    |{z}Y k j| ≤ {z}M := by
  have hk := (List.all_eq_true.mp {z}OperandGate) k (by simp)
  exact of_decide_eq_true ((List.all_eq_true.mp hk) j (by simp))

"""
        names=[z+s for s in ("M_nonneg","OperandGate","OperandBound")]
        sizes={}
        for label,x,targets,xname in (("HD",H0,hd,"nf702HRow"),("A",HDcol,ac,"nf702HDCol")):
            t=z+label; target=t+"Target"
            X=sum(map(abs,x)); Z=max(map(abs,targets)); B=1<<(X*M+Z).bit_length()
            assert B>0 and X*M+Z<B
            pack=lambda vs:sum(v*B**j for j,v in enumerate(vs))
            assert sum(x[k]*pack([c[k] for c in cols]) for k in range(N))==pack(targets)
            body+=f"""def {t}X : ℤ := ({X}:ℤ)
def {t}Z : ℤ := ({Z}:ℤ)
def {t}Base : ℤ := ({B}:ℤ)
theorem {t}Mass : (∑ k, |{xname} k|) ≤ {t}X := by
  decide +kernel
theorem {t}TargetGate :
    (List.finRange {w}).all (fun j => decide (|{target} j| ≤ {t}Z)) = true := by
  decide +kernel
theorem {t}TargetBound (j : Fin {w}) : |{target} j| ≤ {t}Z :=
  of_decide_eq_true ((List.all_eq_true.mp {t}TargetGate) j (by simp))
theorem {t}BasePos : 0 < {t}Base := by
  decide +kernel
theorem {t}Gap : {t}X * {z}M + {t}Z < {t}Base := by
  decide +kernel
theorem {t}PackedEquality :
    neutralNF626Dot {xname}
      (fun k => neutralNF683Pack {t}Base ({z}Y k)) =
      neutralNF683Pack {t}Base {target} := by
  decide +kernel
theorem {t}AllCoordinates (j : Fin {w}) :
    neutralNF626Dot {xname} (fun k => {z}Y k j) = {target} j :=
  neutralNF683PackedProducts {xname} {z}Y {target}
    {t}X {z}M {t}Z {t}Base {t}BasePos {t}Mass
    {z}M_nonneg {z}OperandBound {t}TargetBound {t}Gap {t}PackedEquality j

"""
            names += [t+s for s in ("Mass","TargetGate","TargetBound","BasePos","Gap","PackedEquality","AllCoordinates")]
            sizes[label]={"base_bits":B.bit_length(),"width":w}
        body+="\n".join("#print axioms "+name for name in names)+"\n"
        write(block,[MOD+".Common"],body)
        blocks.append({"module":block,"start":start,"stop":stop,"width":w,"HD":w,"A":w,"theorems":names,"sizes":sizes})
    assert sum(r["HD"] for r in blocks)==sum(r["A"] for r in blocks)==N
    m={"schema":"NF702-original-packed-next-matrix-frontier-v1","H_source_row":I,"HD_source_column":I,
       "HD_exact_external":N,"A_exact_external":N,"max_block_width":W,"blocks":blocks,
       "frame_sha256":frame,"historical_sha256":dh,"entry_sha256":eh,
       "cache_sha256":sha(a.cache),"payment_sha256":sha(a.payments),"files":files,
       "scope":"Next original HD row and A column, exact local integer products via bounded signed digits; global input projections remain open."}
    (a.output/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
    print("NF702 exact original next HD row and A column: 484 external products; 31 bounded packed blocks emitted; kernel pending")
if __name__=="__main__": main()
