#!/usr/bin/env python3
"""NF703: complete original NF626CenterCache and NF681 result projections."""
import argparse,gzip,json,sys
from pathlib import Path
from fractions import Fraction as F
from emit_nf630_original_literal_payments import historical,payment_receipt,rat,array,filetext,sha
from verify_nf623_uniform_physical_payments import N,Q,FROZEN_SHA
sys.set_int_max_str_digits(0)
MOD="WeilDefect.Generated.NF703Cache"
BASE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerCenters"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def dot(x,y):
    assert len(x)==len(y)
    return sum(a*b for a,b in zip(x,y))
def main():
    p=argparse.ArgumentParser()
    for k in ("root","historical","entries","payments","cache","frontier","output"):
        p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args()
    D,S,y,U,w,T,mid,rad,frame=historical(a.root,a.historical)
    assert N==242
    eh,dh=sha(a.entries),sha(a.historical)
    pay=payment_receipt(a.payments,eh,frame)
    V=[];EH=EV=0
    with gzip.open(a.entries,"rt") as f:
        h=json.loads(next(f))
        assert h["schema"]=="NF622-original-physical-entry-balls-v1" and h["scale"]=="10^2600"
        for i,line in enumerate(f):
            r=json.loads(line)
            assert r["row"]==i<N and len(r["H_lower"])==i+1 and len(r["V"])==4
            hh=[tuple(map(int,x)) for x in r["H_lower"]]
            vv=[tuple(map(int,x)) for x in r["V"]]
            assert all(e>=0 for _,e in hh+vv)
            EH=max(EH,max(e for _,e in hh));EV=max(EV,max(e for _,e in vv))
            V.append([x for x,_ in vv])
    assert len(V)==N
    assert rat(pay["uniform_H_radius"])==F(EH,Q) and rat(pay["uniform_V_radius"])==F(EV,Q)
    with gzip.open(a.cache,"rt") as f:
        h=json.loads(next(f))
        assert h["schema"]=="NF626-integer-center-cache-v1"
        assert h["entry_sha256"]==eh and h["historical_sha256"]==dh
        assert h["frame_sha256"]==frame and h["frozen_sha256"]==FROZEN_SHA
        assert {k:int(v) for k,v in h["scales"].items()}==dict(S=S,Q=Q,T=T,U=U)
        assert list(map(int,h["y"]))==y and list(map(int,h["w"]))==w
        assert [rat(h[k]) for k in ("eH","eV","r")]==[rat(pay[k]) for k in ("uniform_H_radius","uniform_V_radius","r")]
        rows=[json.loads(line) for line in f]
    assert [r["i"] for r in rows]==list(range(N))
    HD=[list(map(int,r["HD"])) for r in rows];A=[list(map(int,r["A"])) for r in rows]
    assert all(len(r)==N for r in HD+A)
    assert all(A[i][j]==A[j][i] for i in range(N) for j in range(i))
    vs={name:[int(r[name]) for r in rows] for name in ("Vw","b","Ay","Dy")}
    for i in range(N):
        assert vs["Vw"][i]==dot(V[i],w)
        assert vs["b"][i]==dot([r[i] for r in D],vs["Vw"])
        assert vs["Ay"][i]==dot(A[i],y)
        assert vs["Dy"][i]==dot(D[i],y)
    m=json.loads((a.frontier/"manifest.json").read_text())
    assert (m["entry_sha256"],m["historical_sha256"],m["cache_sha256"],m["payment_sha256"])==(eh,dh,sha(a.cache),sha(a.payments))
    hashes={r["file"]:r["sha256"] for r in m["files"]}
    assert sha(a.frontier/"Common.lean")==hashes["Common.lean"]
    a.output.mkdir(parents=True,exist_ok=True)
    files=[];mods=[]
    def write(name,imports,body):
        path=a.output/(name+".lean")
        path.write_text(filetext(imports,OPT+body))
        files.append({"file":path.name,"sha256":sha(path)})
    for k in range(0,N,4):
        name=f"Rows{k:03d}";body=""
        for i in range(k,min(k+4,N)):
            body+=f"def nf703HD{i:03d} : Array ℤ := {array(HD[i])}\n\n"
            body+=f"def nf703LowerA{i:03d} : Array ℤ := {array(A[i][:i+1])}\n\n"
        write(name,["Mathlib"],body);mods.append(name)
    body=""
    for key in ("HD","LowerA"):
        body+=f"def nf703{key}Parts : Array (Unit → Array ℤ) := #["
        body+=", ".join(f"fun _ => nf703{key}{i:03d}" for i in range(N))+"]\n\n"
        body+=f"def nf703{key}Read (i j : ℕ) : ℤ :=\n  (((nf703{key}Parts[i]?).getD (fun _ => #[])) ())[j]!\n\n"
    for k,values in vs.items():
        body+=f"def nf703Cache{k} : Array ℤ := {array(values)}\n\n"
    body+="""def nf703CacheA (i j : Fin 242) : ℤ :=
  nf703LowerARead (max i.val j.val) (min i.val j.val)

theorem nf703CacheA_symm (i j : Fin 242) : nf703CacheA i j = nf703CacheA j i := by
  unfold nf703CacheA
  rw [max_comm i.val j.val, min_comm i.val j.val]

def nf703OriginalCache : NF626CenterCache :=
  ⟨fun i j => nf703HDRead i.val j.val,
   nf703CacheA,
   fun i => nf703CacheVw[i.val]!,
   fun i => nf703Cacheb[i.val]!,
   fun i => nf703CacheAy[i.val]!,
   fun i => nf703CacheDy[i.val]!⟩

#print axioms nf703CacheA_symm
"""
    write("Data",[BASE]+[MOD+"."+x for x in mods],body)
    body="";names=["nf703CacheA_symm"]
    for label,left,right in (
        ("HDRow0","nf681HDRow0 j","nf703OriginalCache.HD 0 j"),
        ("HDCol0","nf681HDCol0 j","nf703OriginalCache.HD j 0"),
        ("ACol0","nf681ACol0 j","nf703OriginalCache.A j 0")):
        z="nf703"+label
        body+=f"""theorem {z}Gate :
    (List.finRange 242).all (fun j : Fin 242 => decide ({left} = {right})) = true := by
  decide +kernel

theorem {z}Projection (j : Fin 242) : {left} = {right} :=
  of_decide_eq_true ((List.all_eq_true.mp {z}Gate) j (by simp))

#print axioms {z}Gate
#print axioms {z}Projection

"""
        names.extend([z+"Gate",z+"Projection"])
    write("Frontier",[MOD+".Data","WeilDefect.Generated.NF681.Common"],body)
    out={"schema":"NF703-complete-original-cache-proposals-v1","rows":N,"HD_entries":N*N,
         "A_lower_entries":N*(N+1)//2,"external_A_symmetry":N*(N-1)//2,
         "external_vector_products":4*N,"frontier_projections":3*N,
         "entry_sha256":eh,"historical_sha256":dh,"cache_sha256":sha(a.cache),
         "payment_sha256":sha(a.payments),"frontier_manifest_sha256":sha(a.frontier/"manifest.json"),
         "data_modules":mods,"audit_theorems":names,"files":files,
         "scope":"Original cache literals with externally checked symmetric compression; kernel receipt result projections only, no global input or matrix validity."}
    (a.output/"manifest.json").write_text(json.dumps(out,indent=2)+"\n")
    print("NF703 complete original cache emitted; all 968 vector products externally reconciled; kernel pending")
if __name__=="__main__":main()
