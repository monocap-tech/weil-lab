#!/usr/bin/env python3
"""Exact original first complete HD row and first complete A column.
The 484 local products are independent kernel checks, not a full
cache proof. The existing NF626 matrix and input projection
equalities are explicit obligations.
"""
import argparse,gzip,json,sys
from pathlib import Path
from fractions import Fraction as F
from emit_nf630_original_literal_payments import historical,payment_receipt,rat,array,filetext,sha
from verify_nf623_uniform_physical_payments import N,Q,FROZEN_SHA
sys.set_int_max_str_digits(0)
MOD="WeilDefect.Generated.NF681"
BASE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMatrixProductReceipts"
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
    H0=[];EH=EV=0
    with gzip.open(a.entries,"rt") as f:
        h=json.loads(next(f))
        assert h["schema"]=="NF622-original-physical-entry-balls-v1" and h["scale"]=="10^2600"
        for i,line in enumerate(f):
            q=json.loads(line)
            assert q["row"]==i<N and len(q["H_lower"])==i+1 and len(q["V"])==4
            H0.append(int(q["H_lower"][0][0]))
            for x,e in q["H_lower"]:
                assert int(e)>=0
                EH=max(EH,int(e))
            for x,e in q["V"]:
                assert int(e)>=0
                EV=max(EV,int(e))
    assert len(H0)==N
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
            if i==0: HDrow=list(map(int,q["HD"]))
            HDcol.append(int(q["HD"][0]))
            Acol.append(int(q["A"][0]))
    assert len(HDrow)==len(HDcol)==len(Acol)==N
    assert HDrow[0]==HDcol[0]
    a.output.mkdir(parents=True,exist_ok=True)
    files=[]
    def write(name,imports,body):
        f=a.output/(name+".lean")
        f.write_text(filetext(imports,OPT+body))
        files.append({"file":f.name,"sha256":sha(f)})
    body=""
    for name,values in [("HRow0",H0),("HDCol0",HDcol),("HDRow0",HDrow),("ACol0",Acol)]:
        body+=f"def nf681{name}Data : Array ℤ := {array(values)}\n\n"
        body+=f"def nf681{name} (i : Fin 242) : ℤ := nf681{name}Data[i.val]!\n\n"
    write("Common",[BASE],body)
    for j in range(N):
        col=[r[j] for r in D]
        assert dot(H0,col)==HDrow[j],("HD",0,j)
        assert dot(col,HDcol)==Acol[j],("A",j,0)
        z=f"nf681Col{j:03d}"
        body=f"def {z}Data : Array ℤ := {array(col)}\n\n"
        body+=f"def {z} (k : Fin 242) : ℤ := {z}Data[k.val]!\n\n"
        body+=f"""theorem {z}HD :
    nf681HDRow0 ({j}:Fin 242) = neutralNF626Dot nf681HRow0 {z} := by
  decide +kernel

theorem {z}A :
    nf681ACol0 ({j}:Fin 242) = neutralNF626Dot {z} nf681HDCol0 := by
  decide +kernel

#print axioms {z}HD
#print axioms {z}A
"""
        write(f"Col{j:03d}",[MOD+".Common"],body)
    body="def nf681DCol : Fin 242 → Fin 242 → ℤ := fun j =>\n  (#["+", ".join(f"nf681Col{j:03d}" for j in range(N))+"] : Array (Fin 242 → ℤ))[j.val]!\n\n"
    for label,lhs,rhs in [("HD","nf681HDRow0 j","neutralNF626Dot nf681HRow0 (nf681DCol j)"),
                          ("A","nf681ACol0 j","neutralNF626Dot (nf681DCol j) nf681HDCol0")]:
        body+=f"theorem nf681All{label} : ∀ j : Fin 242, {lhs} = {rhs} := by\n  intro j\n  fin_cases j\n"
        for j in range(N):
            body+=f"  · exact nf681Col{j:03d}{label}\n"
        body+=f"\n#print axioms nf681All{label}\n\n"
    write("AllColumns",[MOD+f".Col{j:03d}" for j in range(N)],body)
    m={"schema":"NF681-original-matrix-frontier-v1","H_source_row":0,"HD_source_column":0,
       "HD_exact_external":N,"A_exact_external":N,"literal_gate_count":2*N,
       "frame_sha256":frame,"historical_sha256":dh,"entry_sha256":eh,
       "cache_sha256":sha(a.cache),"payment_sha256":sha(a.payments),"files":files,
       "scope":"First full HD row and A column only; global input projection and other products open."}
    (a.output/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
    print("NF681 original 242 HD row-zero and 242 A column-zero exact dot proposals generated after external replay; kernel pending")
if __name__=="__main__": main()
