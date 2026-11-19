#!/usr/bin/env python3
"""Reconstruct original cache vector and defect numerator proof proposals.
No HD/A product correctness is asserted by a row's literal proof.
The full matrix/vector projection equality must still be attached.
"""
import argparse,gzip,hashlib,json,re,sys
from pathlib import Path
from emit_nf630_original_literal_payments import historical,payment_receipt,rat,array,filetext,sha
from verify_nf623_uniform_physical_payments import N,Q,FROZEN_SHA
sys.set_int_max_str_digits(0)
MOD="WeilDefect.Generated.NF680"
CORE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalCacheVectorReceipts"
SCALAR="WeilDefect.Generated.NF639"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def main():
    p=argparse.ArgumentParser()
    for k in ("root","historical","entries","payments","cache","scalar","output"):
        p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args()
    D,S,y,U,w,T,mid,rad,frame=historical(a.root,a.historical)
    assert N==242
    eh,dh=sha(a.entries),sha(a.historical)
    pay=payment_receipt(a.payments,eh,frame)
    m=json.loads((a.scalar/"manifest.json").read_text())
    assert sha(a.scalar/"manifest.json")=="efcb46ca6eabeae80d0beb21f8627773d23b71002c26fed82f68f47e56bbf896"
    assert (m["entry_sha256"],m["historical_sha256"],m["cache_sha256"],m["payment_sha256"])==(eh,dh,sha(a.cache),sha(a.payments))
    for o in m["files"]:
        if o["file"]!="Params.lean":
            assert sha(a.scalar/o["file"])==o["sha256"]
    ad=Q*S*S
    V=[]
    with gzip.open(a.entries,"rt") as f:
        h=json.loads(next(f))
        assert h["schema"]=="NF622-original-physical-entry-balls-v1" and h["scale"]=="10^2600"
        for i,line in enumerate(f):
            q=json.loads(line)
            assert q["row"]==i<N and len(q["V"])==4
            V.append([int(x) for x,e in q["V"]])
    assert len(V)==N
    # Keep only the Vw data from the first pass; stream the expensive A rows.
    with gzip.open(a.cache,"rt") as f:
        h=json.loads(next(f))
        assert h["schema"]=="NF626-integer-center-cache-v1"
        assert h["entry_sha256"]==eh and h["historical_sha256"]==dh
        assert h["frame_sha256"]==frame and h["frozen_sha256"]==FROZEN_SHA
        assert {k:int(v) for k,v in h["scales"].items()}==dict(S=S,Q=Q,T=T,U=U)
        assert list(map(int,h["y"]))==y and list(map(int,h["w"]))==w
        assert [rat(h[k]) for k in ("eH","eV","r")]==[rat(pay[k]) for k in ("uniform_H_radius","uniform_V_radius","r")]
        vw=[]
        for i,line in enumerate(f):
            q=json.loads(line)
            assert q["i"]==i<N
            vw.append(int(q["Vw"]))
    assert len(vw)==N
    a.output.mkdir(parents=True,exist_ok=True)
    files=[]
    def write(name,imports,body):
        f=a.output/(name+".lean")
        f.write_text(filetext(imports,OPT+body))
        files.append({"file":f.name,"sha256":sha(f)})
    body=""
    for name,values in [("Y",y),("W",w),("Vw",vw)]:
        body+=f"def nf680{name}Data : Array ℤ := {array(values)}\n\n"
        n=4 if name=="W" else N
        body+=f"def nf680{name} (i : Fin {n}) : ℤ := nf680{name}Data[i.val]!\n\n"
    body+="def nf680Den : ℤ := (nf639Q:ℤ)*nf639S*nf639S\n"
    write("Common",[CORE,SCALAR+".Params"],body)
    nrows=0
    with gzip.open(a.cache,"rt") as f:
        next(f)
        for i,line in enumerate(f):
            q=json.loads(line)
            assert q["i"]==i<N
            A=list(map(int,q["A"]))
            assert len(A)==N and len(q["HD"])==N
            dc=[r[i] for r in D]
            b,ay,dy=map(int,(q["b"],q["Ay"],q["Dy"]))
            de=sum(abs((ad if i==j else 0)-x) for j,x in enumerate(A))
            assert vw[i]==int(q["Vw"])==dot(V[i],w)
            assert b==dot(dc,vw) and ay==dot(A,y) and dy==dot(D[i],y)
            v=f"nf639Row{i:03d}";z=f"nf680Row{i:03d}"
            vals=list(map(int,re.findall(r"\((-?\d+):ℤ\)",(a.scalar/f"Row{i:03d}.lean").read_text())))
            assert len(vals)==9
            assert (vals[0],vals[6],vals[7],vals[8])==(de,b,ay,dy)
            body=""
            for name,vv in [("A",A),("Col",dc),("V",V[i])]:
                body+=f"def {z}{name}Data : Array ℤ := {array(vv)}\n\n"
                n=4 if name=="V" else N
                body+=f"def {z}{name} (j : Fin {n}) : ℤ := {z}{name}Data[j.val]!\n\n"
            body+=f"""theorem {z}Vw : nf680Vw ({i}:Fin 242) =
    neutralNF626Dot {z}V nf680W := by
  decide +kernel

theorem {z}B : {v}.b =
    neutralNF626Dot {z}Col nf680Vw := by
  decide +kernel

theorem {z}Ay : {v}.Ay =
    neutralNF626Dot {z}A nf680Y := by
  decide +kernel

theorem {z}Defect : {v}.defect =
    neutralNF680DefectRow ({i}:Fin 242) nf680Den {z}A := by
  decide +kernel

theorem {z}CacheLiterals : {v}.b = ({b}:ℤ) ∧
    {v}.Ay = ({ay}:ℤ) ∧ {v}.Dy = ({dy}:ℤ) := by
  decide +kernel

"""
            body+="\n".join("#print axioms "+z+s for s in ("Vw","B","Ay","Defect","CacheLiterals"))
            write(f"Row{i:03d}",[MOD+".Common",SCALAR+f".Row{i:03d}"],body)
            nrows+=1
    assert nrows==N
    report={"schema":"NF680-original-cache-vector-proposals-v1","rows":nrows,
            "entry_sha256":eh,"historical_sha256":dh,"cache_sha256":sha(a.cache),
            "payment_sha256":sha(a.payments),"scalar_manifest_sha256":sha(a.scalar/"manifest.json"),
            "frame_sha256":frame,"files":files,
            "scope":"Exact external vector and defect replay; local literal Lean proofs pending; HD/A product and global projections separate."}
    (a.output/"manifest.json").write_text(json.dumps(report,indent=2)+"\n")
    print("NF680 original 968 vector products and 242 defect numerators externally reconciled; 1210 local kernel proposals emitted",flush=True)
if __name__=="__main__": main()
