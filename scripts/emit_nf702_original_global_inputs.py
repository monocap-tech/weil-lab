#!/usr/bin/env python3
"""NF702 original complete scaled inputs and exact physical row attachment pilot."""
import argparse,gzip,json,sys
from pathlib import Path
from fractions import Fraction as F
from emit_nf630_original_literal_payments import historical,payment_receipt,rat,array,filetext,sha,qlit
from verify_nf623_uniform_physical_payments import N,Q,FROZEN_SHA
sys.set_int_max_str_digits(0)
MOD="WeilDefect.Generated.NF702Inputs"
CORE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerCenters"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def main():
    p=argparse.ArgumentParser()
    for k in ("root","historical","entries","payments","prior","output"):
        p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args()
    D,S,y,U,w,T,mid,rad,frame=historical(a.root,a.historical)
    eh=sha(a.entries)
    pay=payment_receipt(a.payments,eh,frame)
    assert N==242 and len(D)==N and all(len(row)==N for row in D)
    H=[];V=[];EH=EV=0
    with gzip.open(a.entries,"rt") as f:
        h=json.loads(next(f))
        assert h["schema"]=="NF622-original-physical-entry-balls-v1" and h["scale"]=="10^2600"
        for i,line in enumerate(f):
            r=json.loads(line)
            assert r["row"]==i<N and len(r["H_lower"])==i+1 and len(r["V"])==4
            hh=[tuple(map(int,x)) for x in r["H_lower"]];vv=[tuple(map(int,x)) for x in r["V"]]
            assert all(e>=0 for _,e in hh+vv)
            H.append([x for x,_ in hh]);V.append([x for x,_ in vv])
            EH=max(EH,max(e for _,e in hh));EV=max(EV,max(e for _,e in vv))
    assert len(H)==len(V)==N
    assert rat(pay["uniform_H_radius"])==F(EH,Q) and rat(pay["uniform_V_radius"])==F(EV,Q)
    old=json.loads((a.prior/"manifest.json").read_text())
    assert old["widened_digest"]==eh and [r["row"] for r in old["rows"]]==list(range(8))
    assert F(old["physical_eH"])==F(EH,Q) and F(old["physical_eV"])==F(EV,Q)
    for r in old["rows"]:
        assert sha(a.prior/r["file"])==r["sha256"]
    a.output.mkdir(parents=True,exist_ok=True)
    files=[];modules=[]
    def write(name,imports,body):
        path=a.output/(name+".lean")
        path.write_text(filetext(imports,OPT+body))
        files.append({"file":path.name,"sha256":sha(path)})
    for k in range(0,N,4):
        name=f"Rows{k:03d}";body=""
        for i in range(k,min(k+4,N)):
            for key,values in (("D",D[i]),("LowerH",H[i]),("V",V[i])):
                body+=f"def nf702{key}{i:03d} : Array ℤ := {array(values)}\n\n"
        write(name,["Mathlib"],body);modules.append(name)
    body=""
    for key in ("D","LowerH","V"):
        body+=f"def nf702{key}Parts : Array (Unit → Array ℤ) := #["
        body+=", ".join(f"fun _ => nf702{key}{i:03d}" for i in range(N))+"]\n\n"
        body+=f"def nf702{key}Read (i j : ℕ) : ℤ :=\n  (((nf702{key}Parts[i]?).getD (fun _ => #[])) ())[j]!\n\n"
    body+=f"""def nf702InputH (i j : Fin 242) : ℤ :=
  nf702LowerHRead (max i.val j.val) (min i.val j.val)

theorem nf702InputH_symm (i j : Fin 242) : nf702InputH i j = nf702InputH j i := by
  unfold nf702InputH
  rw [max_comm i.val j.val, min_comm i.val j.val]

def nf702InputY : Array ℤ := {array(y)}
def nf702InputW : Array ℤ := {array(w)}

def nf702OriginalInputs : NF626ScaledInputs :=
  ⟨fun i j => nf702DRead i.val j.val,
   nf702InputH,
   fun i j => nf702VRead i.val j.val,
   fun i => nf702InputY[i.val]!,
   fun i => nf702InputW[i.val]!,
   {S}, {Q}, {U}, {T}, {qlit(F(EH,Q))}, {qlit(F(EV,Q))}, {qlit(rat(pay["r"]))}⟩

theorem nf702OriginalW : nf702OriginalInputs.wCheck = true := by
  decide +kernel

#print axioms nf702InputH_symm
#print axioms nf702OriginalW
"""
    write("Data",[CORE]+[MOD+"."+m for m in modules],body)
    projections=[]
    for i in range(8):
        stem=f"nf702Attach{i:03d}";v=f"nf695Row{i:03d}";src=v+"Payment"
        body=f"""theorem {stem}HRowGate :
    (List.finRange 242).all (fun j =>
      decide ({src}.H0 ({i}:Fin 242) j =
        nf702OriginalInputs.payment.H0 ({i}:Fin 242) j)) = true := by
  decide +kernel

theorem {stem}HColGate :
    (List.finRange 242).all (fun j =>
      decide ({src}.H0 j ({i}:Fin 242) =
        nf702OriginalInputs.payment.H0 j ({i}:Fin 242))) = true := by
  decide +kernel

theorem {stem}VGate :
    (List.finRange 4).all (fun j =>
      decide ({src}.V0 ({i}:Fin 242) j =
        nf702OriginalInputs.payment.V0 ({i}:Fin 242) j)) = true := by
  decide +kernel

theorem {stem}EH : {src}.eH = nf702OriginalInputs.payment.eH := by
  decide +kernel
theorem {stem}EV : {src}.eV = nf702OriginalInputs.payment.eV := by
  decide +kernel

theorem {stem}ActualPayment :
    neutralNF674OriginalRowCheck
      (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
      nf702OriginalInputs.payment ({i}:Fin 242) = true := by
  apply {v}PaymentTransport
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp {stem}HRowGate) j (by simp))
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp {stem}HColGate) j (by simp))
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp {stem}VGate) j (by simp))
  · exact {stem}EH
  · exact {stem}EV

"""
        names=[stem+s for s in ("HRowGate","HColGate","VGate","EH","EV","ActualPayment")]
        body+="\n".join("#print axioms "+n for n in names)+"\n"
        name=f"Attach{i:03d}"
        write(name,[MOD+".Data",f"WeilDefect.Generated.NF695.Row{i:03d}"],body)
        projections.append({"row":i,"module":name,"theorems":names})
    m={"schema":"NF702-original-global-input-projection-v1","rows":N,"source_frame_sha256":frame,
       "historical_sha256":sha(a.historical),"entries_sha256":eh,"payment_sha256":sha(a.payments),
       "prior_manifest_sha256":sha(a.prior/"manifest.json"),"input_modules":modules,
       "projection_rows":projections,"files":files,
       "scope":"Complete original scaled input object and first eight original full-payment row gates; no cache validity or full entry custody."}
    (a.output/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
    print("NF702 exact complete original input literals and eight full-payment projection candidates emitted")
if __name__=="__main__":main()
