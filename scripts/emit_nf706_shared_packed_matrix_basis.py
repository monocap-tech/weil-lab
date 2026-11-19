#!/usr/bin/env python3
"""NF706: shared fixed-base packing for four original matrix indices."""
import argparse,gzip,json,sys
from pathlib import Path
from fractions import Fraction as F
from emit_nf630_original_literal_payments import historical,payment_receipt,rat,array,filetext,sha
from verify_nf623_uniform_physical_payments import N,Q,FROZEN_SHA
sys.set_int_max_str_digits(0)
MOD="WeilDefect.Generated.NF706"
BASE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalPackedProducts"
W=8
INDICES=tuple(range(6,10))
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def dot(x,y):
    assert len(x)==len(y)
    return sum(a*b for a,b in zip(x,y))
def main():
    p=argparse.ArgumentParser()
    for k in ("root","historical","entries","payments","cache","output"):
        p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args()
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
    H={i:[lower[max(i,j)][min(i,j)] for j in range(N)] for i in INDICES}
    assert rat(pay["uniform_H_radius"])==F(EH,Q) and rat(pay["uniform_V_radius"])==F(EV,Q)
    HDrow={};HDcol={i:[] for i in INDICES};Acol={i:[] for i in INDICES}
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
            if i in INDICES: HDrow[i]=list(map(int,q["HD"]))
            for j in INDICES:
                HDcol[j].append(int(q["HD"][j]))
                Acol[j].append(int(q["A"][j]))
    assert set(HDrow)==set(INDICES)
    assert all(len(HDrow[i])==len(HDcol[i])==len(Acol[i])==N and HDrow[i][i]==HDcol[i][i] for i in INDICES)
    a.output.mkdir(parents=True,exist_ok=True)
    files=[];blocks=[]
    def write(name,imports,body):
        f=a.output/(name+".lean")
        f.write_text(filetext(imports,OPT+body))
        files.append({"file":f.name,"sha256":sha(f)})
    def vec(name,values,n):
        return (f"def {name}Data : Array ℤ := {array(values)}\n\n"
                f"def {name} (i : Fin {n}) : ℤ := {name}Data[i.val]!\n\n")
    common="""theorem nf706Packed_of_prepack {m n : ℕ}
    (x : Fin m → ℤ) (Y : Fin m → Fin n → ℤ) (z : Fin n → ℤ)
    (p : Fin m → ℤ) (X M Z B : ℤ) (hpos : 0 < B)
    (hX : ∑ k, |x k| ≤ X) (hM : 0 ≤ M)
    (hY : ∀ k j, |Y k j| ≤ M) (hZ : ∀ j, |z j| ≤ Z)
    (hB : X*M+Z < B)
    (hp : ∀ k, p k = neutralNF683Pack B (Y k))
    (he : neutralNF626Dot x p = neutralNF683Pack B z) :
    ∀ j, neutralNF626Dot x (fun k => Y k j) = z j := by
  have hfun : p = fun k => neutralNF683Pack B (Y k) := funext hp
  rw [hfun] at he
  exact neutralNF683PackedProducts x Y z X M Z B hpos hX hM hY hZ hB he

#print axioms nf706Packed_of_prepack

"""
    xs={f"H{i:03d}":H[i] for i in INDICES}
    xs.update({f"HD{i:03d}":HDcol[i] for i in INDICES})
    X=max(sum(map(abs,x)) for x in xs.values())
    common+=f"def nf706X : ℤ := ({X}:ℤ)\n\n"
    common_names=["nf706Packed_of_prepack"]
    for key,x in xs.items():
        name="nf706"+key
        common+=vec(name,x,N)
        common+=f"theorem {name}Mass : (∑ k, |{name} k|) ≤ nf706X := by\n  decide +kernel\n\n#print axioms {name}Mass\n\n"
        common_names.append(name+"Mass")
    write("Common",[BASE],common)
    for start in range(0,N,W):
        stop=min(start+W,N);w=stop-start
        block=f"Block{start//W:03d}";z="nf706"+block
        cols=[[D[k][j] for k in range(N)] for j in range(start,stop)]
        targets=[]
        for i in INDICES:
            hd=HDrow[i][start:stop]
            assert all(dot(H[i],c)==v for c,v in zip(cols,hd)),("HD",i,start)
            targets.append((i,"HD",f"H{i:03d}",hd))
            if stop>i:
                ac=Acol[i][start:stop]
                assert all(dot(c,HDcol[i])==v for c,v in zip(cols,ac)),("A",i,start)
                targets.append((i,"A",f"HD{i:03d}",ac))
        M=max(abs(v) for col in cols for v in col)
        Z=max(abs(v) for _,_,_,vs in targets for v in vs)
        B=1<<(X*M+Z).bit_length()
        assert B>0 and X*M+Z<B
        pack=lambda vs:sum(v*B**j for j,v in enumerate(vs))
        p=[pack([col[k] for col in cols]) for k in range(N)]
        body="".join(vec(f"{z}D{j}",col,N) for j,col in enumerate(cols))
        body+=f"def {z}Y (k : Fin 242) (j : Fin {w}) : ℤ :=\n  (#["
        body+=", ".join(f"{z}D{j}" for j in range(w))+f"] : Array (Fin 242 → ℤ))[j.val]! k\n\n"
        body+=vec(z+"PackedD",p,N)
        body+=f"""def {z}M : ℤ := ({M}:ℤ)
def {z}Z : ℤ := ({Z}:ℤ)
def {z}Base : ℤ := ({B}:ℤ)

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
theorem {z}BasePos : 0 < {z}Base := by
  decide +kernel
theorem {z}Gap : nf706X * {z}M + {z}Z < {z}Base := by
  decide +kernel
theorem {z}PrepackGate :
    (List.finRange 242).all (fun k =>
      decide ({z}PackedD k = neutralNF683Pack {z}Base ({z}Y k))) = true := by
  decide +kernel
theorem {z}Prepack (k : Fin 242) :
    {z}PackedD k = neutralNF683Pack {z}Base ({z}Y k) :=
  of_decide_eq_true ((List.all_eq_true.mp {z}PrepackGate) k (by simp))

"""
        names=[z+s for s in ("M_nonneg","OperandGate","OperandBound","BasePos","Gap","PrepackGate","Prepack")]
        receipts=[]
        for i,label,xkey,vs in targets:
            t=f"{z}{label}{i:03d}";target=t+"Target";xname="nf706"+xkey
            assert dot(xs[xkey],p)==pack(vs)
            body+=vec(target,vs,w)
            body+=f"""theorem {t}TargetGate :
    (List.finRange {w}).all (fun j => decide (|{target} j| ≤ {z}Z)) = true := by
  decide +kernel
theorem {t}TargetBound (j : Fin {w}) : |{target} j| ≤ {z}Z :=
  of_decide_eq_true ((List.all_eq_true.mp {t}TargetGate) j (by simp))
theorem {t}PackedEquality :
    neutralNF626Dot {xname} {z}PackedD =
      neutralNF683Pack {z}Base {target} := by
  decide +kernel
theorem {t}AllCoordinates (j : Fin {w}) :
    neutralNF626Dot {xname} (fun k => {z}Y k j) = {target} j :=
  nf706Packed_of_prepack {xname} {z}Y {target} {z}PackedD
    nf706X {z}M {z}Z {z}Base {z}BasePos {xname}Mass
    {z}M_nonneg {z}OperandBound {t}TargetBound {z}Gap {z}Prepack {t}PackedEquality j

"""
            names.extend(t+s for s in ("TargetGate","TargetBound","PackedEquality","AllCoordinates"))
            receipts.append({"index":i,"kind":label,"start":start,"stop":stop,
                             "coordinates":w,"lower_required":w if label=="HD" else stop-max(start,i),
                             "theorem":t+"AllCoordinates"})
        body+="\n".join("#print axioms "+n for n in names)+"\n"
        write(block,[MOD+".Common"],body)
        blocks.append({"module":block,"start":start,"stop":stop,"width":w,"base_bits":B.bit_length(),
                       "receipts":receipts,"theorems":names})
    rs=[r for b in blocks for r in b["receipts"]]
    for i in INDICES:
        assert [j for r in rs if r["index"]==i and r["kind"]=="HD" for j in range(r["start"],r["stop"])]==list(range(N))
        assert [j for r in rs if r["index"]==i and r["kind"]=="A" for j in range(max(i,r["start"]),r["stop"])]==list(range(i,N))
    assert sum(r["coordinates"] for r in rs)==1920
    assert sum(r["lower_required"] for r in rs)==1906
    assert len(rs)==246 and len(blocks)==31
    m={"schema":"NF706-shared-original-packed-matrix-v1","indices":list(INDICES),"width":W,
       "coordinates":1920,"triangular_required_coordinates":1906,"packed_equalities":len(rs),
       "shared_prepack_gates":len(blocks),"common_theorems":common_names,"blocks":blocks,
       "frame_sha256":frame,"historical_sha256":dh,"entry_sha256":eh,"cache_sha256":sha(a.cache),
       "payment_sha256":sha(a.payments),"files":files,
       "scope":"Four new local HD rows and lower A columns with boundary padding. Shared packing and bounds must pass Lean; global data projection remains open."}
    (a.output/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
    print("NF706 exact shared packed preflight PASS: 1920 local integer products, 1906 required triangular coordinates; Lean pending")
if __name__=="__main__": main()
