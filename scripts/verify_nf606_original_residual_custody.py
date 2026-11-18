#!/usr/bin/env python3
"""NF606: independent real residual certificate for the original solve.

Reconstruct fixed-frame N and rhs exactly as NF604. Use LU only to
choose a dyadic y0; the proof of containment uses row-defect and
residual upper bounds and a row-specific frame payment. All
inequalities are Arb-certified; the analytic input attachment to
Lean remains open. No original frozen data changes.
"""
import argparse, hashlib, json, time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb, arb_mat, ctx
import verify_rpb108_si29_full_J_L2_normalization as m
from verify_rpb108_original_signed_frame_transport import candidate
from verify_nf374_original_matched_curvature import load, dyad, RANK_SHA, PR355_SHA, NF369_SHA, TNUM
from verify_nf380_original_archived_signed_dual import FRAME_SHA

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "notes/data/provisional"
FROZEN_SHA = "0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"

def exact_dyad(p):
    a,e = int(p[0]),int(p[1])
    return F(a) * F(2)**e

def endpoints(row):
    mid,rad = map(exact_dyad,row)
    assert rad >= 0
    return mid-rad, mid+rad

def check_containment(old, new, label):
    lo,hi = endpoints(old)
    l,h = endpoints(new)
    assert lo <= l <= h <= hi, (label, "not contained")
    return {"index": label, "fresh_mid_radius": new,
            "frozen_contains_fresh": True, "strict_interior": lo < l and h < hi}

def terms(nodes, probes, freqs):
    J = [m.pole_terms() if c is None else m.source_terms(c,k) for c,k in nodes]
    Fs = []
    for probe in probes:
        t=[]
        for c,coef in zip(freqs,probe["sine_coefficients"]):
            t.extend((n,kind,f,v*m.a(F(coef)))
                     for n,kind,f,v in m.source_terms(F(c),0))
        t.extend((n,kind,f,v*m.a(F(probe["sinh_coefficient"])))
                 for n,kind,f,v in m.pole_terms())
        Fs.append(t)
    return J,Fs

def gram(J, kern):
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):
            H[i,j]=H[j,i]=m.gram(J[i],J[j],kern)
    return H

def frame_check(D):
    digest=hashlib.sha256()
    for i in range(242):
        for j in range(242):
            digest.update((json.dumps(m.dyadic(D[i,j]),separators=(",",":"))+"\n").encode())
    assert digest.hexdigest()==FRAME_SHA

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--bits",type=int,default=8192)
    p.add_argument("--output",required=True)
    args=p.parse_args()
    assert flint.__version__=="0.8.0" and args.bits>=8192
    start=time.monotonic()
    frozen_bytes=(DATA/"NF407_original_fourth_physical_coefficients_native.json").read_bytes()
    assert hashlib.sha256(frozen_bytes).hexdigest()==FROZEN_SHA
    frozen=json.loads(frozen_bytes)
    rank=load(str(DATA/"parents/pr350_original_BS_pruned_rank_bound.json"),RANK_SHA)
    source=load(str(DATA/"nf372_pr355_fields.json"),PR355_SHA)["data"]
    parent=load(str(DATA/"nf372_nf369_fields.json"),NF369_SHA)["data"]
    assert parent["selected_rank"]==242
    assert [frozen["original_rank_sha256"], frozen["original_source_sha256"],
            frozen["nf369_parent_sha256"], frozen["original_frame_sha256"]]==[RANK_SHA,PR355_SHA,NF369_SHA,FRAME_SHA]
    nodes=[]
    for (c,maxk),count in zip(rank["original_nodes"],rank["selected_multiplicities"]):
        assert 0<=count<=maxk
        nodes.extend((F(c),k) for k in range(count))
    assert len(nodes)==241 and rank["retained_original_pole"]
    nodes.append((None,None))
    probes=source["target_probes"]
    freqs=source["target_sine_frequencies"]
    assert len(probes)==4 and freqs==[str(F(5*j,11)) for j in range(1,33)]
    assert [[str(c) if c is not None else "pole",k] for c,k in nodes]==frozen["original_selected_generator_node_orders"]
    assert probes==frozen["original_source_critical_sines_and_pole_coefficients"]
    assert freqs==frozen["original_source_critical_sine_frequencies"]

    # Historic frame generated at its ORIGINAL precision, not a new frame.
    ctx.prec=4096
    J,_=terms(nodes,probes,freqs)
    D0=candidate(gram(J,m.Integrals()))
    frame_check(D0)
    frame=[[m.dyadic(D0[i,j]) for j in range(242)] for i in range(242)]
    print("NF606 original exact frame SHA verified",flush=True)

    # Re-evaluate every analytic entry from scratch at higher precision.
    ctx.prec=args.bits
    D=arb_mat([[arb((int(a),int(e))) for a,e in row] for row in frame])
    frame_check(D)
    J,Fs=terms(nodes,probes,freqs)
    kern=m.Integrals()
    H=gram(J,kern)
    V=arb_mat([[m.gram(s,f,kern) for f in Fs] for s in J])
    N=D.transpose()*H*D
    err=max(sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0))
            for i in range(242))
    assert err<arb("0.01") # invertibility of exact transformed Gram
    Y0=parent["nf369_quotient_response_exact_dyadic_coefficients"]
    C=arb_mat([[dyad(v)+int(i==j) for j,v in enumerate(row)] for i,row in enumerate(Y0)])
    T=arb_mat([[m.a(F(v,2**20)) for v in row] for row in TNUM])
    M=C*T
    fourth=arb_mat([[M[j,3]] for j in range(4)])
    # Solve only the TRUE fourth column as a single RHS. This is the same
    # exact vector as rawX * fourth by linearity, without four separate
    # enormous raw coordinate columns.
    rhs=D.transpose()*(V*fourth)
    y=N.solve(rhs,algorithm="lu")
    y0=arb_mat([[y[i,0].mid()] for i in range(242)])
    assert all(y0[i,0].is_exact() for i in range(242))
    err_res=rhs-N*y0
    # Take the maximum of exact outward dyadic upper endpoints,
    # avoiding comparisons between overlapping interval balls.
    rdyad=max((m.dyadic(abs(err_res[i,0]).upper()) for i in range(242)),
              key=exact_dyad)
    rm,re=map(int,rdyad)
    r=arb((rm,re))
    assert r.is_exact() and r>=0
    assert all(abs(err_res[i,0])<=r for i in range(242))
    defect_rows=[]
    for i in range(242):
        row=sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0))
        assert row<arb(1)/100
        defect_rows.append(m.dyadic(row.upper()))
    raw0=D*y0
    sel=[]
    for i,row in enumerate(frozen["original_exact_native_raw_selected_coefficients_mid_radius"]):
        (mm,me),(rr,rr_e)=[list(map(int,p)) for p in row]
        mid=arb((mm,me)); rad=arb((rr,rr_e))
        assert mid.is_exact() and rad.is_exact() and rad>=0
        frame_cost=sum((abs(D[i,j]) for j in range(242)),arb(0))*2*r
        pay=abs(raw0[i,0]-mid)+frame_cost
        assert pay<rad, ("NF606 row payment exceeds original radius",i)
        # Store separately the quantities used by the real residual theorem.
        sel.append({"index":i,"candidate_raw_mid_radius":m.ball(raw0[i,0]),
                    "frame_payment_upper":m.dyadic(frame_cost.upper()),
                    "total_payment_upper":m.dyadic(pay.upper()),
                    "frozen_radius":row[1]})
    b=[T[j,3]-M[j,3] for j in range(4)]
    crit=[check_containment(old,m.ball(b[i]),i) for i,old in
          enumerate(frozen["original_exact_native_original_four_critical_coefficients_mid_radius"])]
    out={"pass":"NF606-original-residual-containment",
         "frozen_sha256":FROZEN_SHA,"frame_sha256":FRAME_SHA,
         "precision_bits":args.bits,"row_defect_threshold":"1/100",
         "row_defect_upper":defect_rows,"transformed_candidate":[m.dyadic(y0[i,0]) for i in range(242)],
         "transformed_rhs_residual_upper":rdyad,
         "selected":sel,"critical":crit,
         "all_246_residual_box_payments_pass":True,
         "evidence_kind":"Arb enclosures of real residual hypotheses; not Lean analytic attachment"}
    Path(args.output).write_text(json.dumps(out,indent=2)+"\n")
    print("NF606 all 242 residual row payments and 4 exact critical coordinates PASS",round(time.monotonic()-start,2),flush=True)

if __name__=="__main__":
    main()
