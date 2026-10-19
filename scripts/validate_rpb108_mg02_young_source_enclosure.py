#!/usr/bin/env python3
"""MG02: alternative complete-source Loewner error for SM62's 338 real windows.

Method gate, not theorem promotion. Compare SM62's scalar Cauchy mean
penalty to an independently valid Young rank-one/diagonal enclosure on
the SAME 338 true original positive windows, without changing the
original 973 negative leaves, 49 earlier positives, or exceptional pole.

For actual physical Fourier mean u=v+e with ||e||^2<=r^2, 0<t<1,
  uu^T >= (1-t) vv^T - (1/t-1) r^2 I.
Indeed the difference before replacing ee^T by r^2 I is
  (t*v+e)(t*v+e)^T/t >= 0.
This pays ALL 25 original source crosses. Each cell independently
chooses the certificate maximizing the exact trace LOWER on the
23-coordinate complement (a diagnostic, NOT a Loewner max).
The method must improve that trace relative to the identical SM62
scalar certificate, after paying all signed weights and rounding.
It may still fail PSD, as an indefinite LOWER is not a negative witness.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    hyperbolic_interval, original_full_25_physical_interval_gram)
from validate_rpb108_sm43_positive_cell_envelope import ROOT,ceil_rat,original_source_centered_windows
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    original_exact_physical_fourier_midpoint,original_full_second_derivative_upper,sqrt_upper)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_midpoint_derivative_intervals,original_third_spatial_moment)
from validate_rpb108_sm57_original_25source_negative_upper import (
    original_positive_low_25,pole_outer_upper,outward_compact_matrix,
    exact_symmetric_25source_inertia)
from validate_rpb108_sm58_original_coupled_25negative import original_complete_coupled_negative
from validate_rpb108_sm62_full25_338signed_positive import (
    all_338_disjoint_original_signed_positive,exact_inertia_general)

N=25
R=tuple(i for i in range(N) if i not in (2,17))
DEN=10**12
T_CHOICES=tuple(F(1,k) for k in (256,128,64,32,16,8,4,2))
def up(x): return ceil_rat(x,DEN)
def zero(): return [[F(0) for _ in range(N)] for _ in range(N)]
def fingerprint(A):
    s=json.dumps([[str(z) for z in row] for row in A],
                 separators=(",",":"),ensure_ascii=True)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()
def trace_R(A): return sum((A[i][i] for i in R),F(0))
def mat_plus(A,B,fee):
    C=[[A[i][j]+B[i][j]-(fee if i==j else 0)
        for j in range(N)] for i in range(N)]
    return outward_compact_matrix(C)
def inertia_R(A):
    P=[[A[i][j] for j in R] for i in R]
    plus,minus,zero=exact_inertia_general(P)
    return {"positive":plus,"negative":minus,"zero":zero}
def exact_young_regression():
    # A tiny exact algebraic test is supplemental; the displayed
    # sum-of-squares identity is the general proof.
    for t in T_CHOICES:
        for v,e in (([F(2),F(-3)],[F(1,7),F(1,5)]),
                    ([F(0),F(1)],[F(-1,3),F(0)])):
            d=[t*x+y for x,y in zip(v,e)]
            y=[[d[i]*d[j]/t for j in range(2)] for i in range(2)]
            assert y[0][0]>=0 and y[1][1]>=0
            assert y[0][0]*y[1][1]-y[0][1]**2==0
    return True
def candidate(v,radii,gamma):
    vn2=sum((a*a for a in v),F(0))
    er2=sum((a*a for a in radii),F(0))
    scalar_eta=2*sqrt_upper(vn2*er2)+er2
    scalar_fee=up(gamma*scalar_eta)
    vr2=sum((v[i]*v[i] for i in R),F(0))
    base_score=gamma*vr2-F(len(R))*scalar_fee
    best=(base_score,F(1),scalar_fee,"scalar")
    for t in T_CHOICES:
        w=1-t
        fee=up(gamma*(1/t-1)*er2)
        score=gamma*w*vr2-F(len(R))*fee
        if score>best[0]:
            best=(score,w,fee,str(t))
    assert best[0]>=base_score
    return (F(1),scalar_fee),(best[1],best[2]),best[3],best[0]-base_score

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/mg02_adaptive_young_full25_source.json")
    args=p.parse_args()
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert ledger["objective"]["status"]=="open"
    assert exact_young_regression()
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==N and sources[24][0]=="pole"
    gram,physical,_=original_full_25_physical_interval_gram()
    assert sources==physical
    negative,ns=original_complete_coupled_negative(centers,sources)
    assert ns["whole_original_negative_frequency_leaves"]==973
    positive,_=original_positive_low_25(centers,sources,gram)
    pole,_=pole_outer_upper(gram)
    Lraw=[[positive[i][j]-negative[i][j]-pole[i][j] for j in range(N)] for i in range(N)]
    L0,_=outward_compact_matrix(Lraw)
    pinned=json.loads((ROOT/"certificates/rpb108_sm58_full25_signed_summary.json").read_text())
    assert pinned["actions_run_id"]==39281588617
    assert fingerprint(negative)==pinned["original_full25_coupled_negative_upper_all_625_entries_sha256"]
    assert fingerprint(L0)==pinned["original_full25_signed_lower_all_625_entries_sha256"]
    signed,_=all_338_disjoint_original_signed_positive(centers,sources)
    assert len(signed)==338
    hyp=(hyperbolic_interval(B/2,"sinh"),hyperbolic_interval(B/2,"cosh"))
    second=original_full_second_derivative_upper(sources)
    third=original_third_spatial_moment(sources)
    scalar=zero()
    young=zero()
    fees=[F(0),F(0)]
    choices={}
    strict_count=0
    checkpoints=[]
    cumulative_gain=F(0)
    for n,(left,right,delta,_origin) in enumerate(signed,1):
        mid=(left+right)/2
        half=(right-left)/2
        physical_v=original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
        _derivs,local_seconds=original_midpoint_derivative_intervals(mid,centers,sources,hyp)
        v=[];r=[]
        for i in range(N):
            x,midrad=physical_v[i]
            k=second[i]
            if local_seconds[i] is not None:
                local=max(abs(local_seconds[i].l),abs(local_seconds[i].h))+third[i]*half
                k=min(k,local)
            v.append(x)
            r.append(midrad+k*half*half/6)
        gamma=2*(right-left)*delta
        assert gamma>0
        (w0,fee0),(w1,fee1),mode,gain=candidate(v,r,gamma)
        fees[0]+=fee0
        fees[1]+=fee1
        cumulative_gain+=gain
        choices[mode]=choices.get(mode,0)+1
        if mode!="scalar":strict_count+=1
        for i in range(N):
            for j in range(i,N):
                piece=gamma*v[i]*v[j]
                scalar[i][j]+=w0*piece
                young[i][j]+=w1*piece
        if n in (96,192,288,338):
            S=[row[:] for row in scalar]
            Y=[row[:] for row in young]
            for i in range(N):
                for j in range(i):
                    S[i][j]=S[j][i]
                    Y[i][j]=Y[j][i]
            S,round0=mat_plus(L0,S,fees[0])
            Y,round1=mat_plus(L0,Y,fees[1])
            tr0=trace_R(S);tr1=trace_R(Y)
            # Display rounding is paid: at worst 23 * each outward fee.
            assert tr1>=tr0-F(23)*(round0+round1)
            checkpoints.append({
                "cell_count":n,
                "scalar_23_complement_lower_trace":str(tr0),
                "young_23_complement_lower_trace":str(tr1),
                "adaptive_trace_advantage":str(tr1-tr0),
                "scalar_25_lower_inertia":{k:exact_symmetric_25source_inertia(S)[k] for k in ("positive","negative","zero")},
                "young_25_lower_inertia":{k:exact_symmetric_25source_inertia(Y)[k] for k in ("positive","negative","zero")},
                "scalar_23_lower_inertia":inertia_R(S),
                "young_23_lower_inertia":inertia_R(Y),
                "scalar_error_fee":str(fees[0]),
                "young_error_fee":str(fees[1]),
                "scalar_export_fee":str(round0),
                "young_export_fee":str(round1)
            })
    assert len(checkpoints)==4 and sum(choices.values())==338
    assert cumulative_gain>0 and strict_count>0
    final=checkpoints[-1]
    assert F(final["adaptive_trace_advantage"])>=-F(23)*(F(final["scalar_export_fee"])+F(final["young_export_fee"]))
    result={
        "status":"SCOPED_MG02_TRUE_ORIGINAL_25SOURCE_YOUNG_METHOD_GATE",
        "canonical_W_ODD_NEG":"OPEN",
        "baseline_original_SM58_625_entry_hashes_replayed":True,
        "original_negative_973_leaves_unchanged":True,
        "original_true_odd_pole_charged_once":True,
        "original_49_old_positive_windows_unchanged":True,
        "new_disjoint_original_positive_windows":338,
        "all_625_original_source_cross_terms_charged":True,
        "source_mean_error_bounded_in_full_25D":True,
        "young_rational_parameter_choices":[str(z) for z in T_CHOICES],
        "choice_counts":choices,
        "strict_young_selected_cells":strict_count,
        "certified_raw_23_trace_gain_before_compaction":str(cumulative_gain),
        "checkpoints":checkpoints,
        "actual_25D_source_positive_definite_certified":False,
        "actual_signed_23D_schur_positive_certified":False,
        "original_470_Astar_inverse_and_infinite_complement":"OPEN",
        "even_Weil_CC27_RH":"OPEN",
        "independent_original_Fourier_closed_domain_audit":"OPEN",
        "interpretation":"Independent full 25D Young vs scalar source-error enclosures on exact same original cells; compare 23D lower TRACE as viability diagnostic, never substitute reference inertia for actual signed negative index."
    }
    dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("MG02 original source method viability:",json.dumps({
        "selected_young":strict_count,
        "raw_complement_trace_improvement":float(cumulative_gain),
        "final_scalar_23_negative_lower_pivots":final["scalar_23_lower_inertia"]["negative"],
        "final_adaptive_23_negative_lower_pivots":final["young_23_lower_inertia"]["negative"],
        "full_original_odd_Weil_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":
    main()
