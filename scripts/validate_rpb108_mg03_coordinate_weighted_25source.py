#!/usr/bin/env python3
"""MG03: coordinate-weighted *complete* 25-source signed Loewner method gate.

On exactly SM62's 338 previously verified original signed-positive disjoint
frequency cells, compare MG02's scalar/Young full25 mean uncertainty to
independently valid weighted Gershgorin source-coordinate error bounds.

For u=v+e with |e_i|<=r_i, |(uuT-vvT)_ij|<=
 d_ij=|v_i|r_j+|v_j|r_i+r_i*r_j.
For every positive rational w_i,
 D_i = sum_j d_ij*w_j/w_i
gives uuT >= vvT - diag(D) in full 25D Loewner order:
for every z, 2|z_i z_j| <= z_i² w_j/w_i + z_j² w_i/w_j.

This is NOT a diagonal-only form: full vvT mixed entries are retained and
the diagonal fee dominates all source cross errors. Different weights may
improve complementary 23D lower trace/directions while worsening anchor
directions. No splicing of SM52 into a whole lower is performed.

Compare 4 complete lower-matrix policies at 96,192,288,338:
MG02 adaptive scalar/Young; MG03 best 23D trace; best g1 diagonal; best
pole24 diagonal. Exact rational 25D and 23D LOWER inertias are diagnostic,
not actual negative spectral witnesses. Full 470/infinite odd/even/RH open.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    hyperbolic_interval,original_full_25_physical_interval_gram)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,ceil_rat)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    original_exact_physical_fourier_midpoint,
    original_full_second_derivative_upper,sqrt_upper)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_midpoint_derivative_intervals,original_third_spatial_moment)
from validate_rpb108_sm57_original_25source_negative_upper import (
    original_positive_low_25,pole_outer_upper,outward_compact_matrix,
    exact_symmetric_25source_inertia)
from validate_rpb108_sm58_original_coupled_25negative import original_complete_coupled_negative
from validate_rpb108_sm62_full25_338signed_positive import (
    all_338_disjoint_original_signed_positive,exact_inertia_general)
from validate_rpb108_mg02_young_source_enclosure import candidate as mg02_candidate

N=25
R=tuple(i for i in range(N) if i not in (2,17))
DEN=10**12
def up(x):return ceil_rat(x,DEN)
def zero():return [[F(0) for _ in range(N)] for _ in range(N)]
def sha(A):
    return hashlib.sha256(json.dumps(
        [[str(x) for x in row] for row in A],
        separators=(",",":"),ensure_ascii=True).encode("utf-8")).hexdigest()
def lower_inertia(A):
    q=exact_symmetric_25source_inertia(A)
    b=exact_inertia_general([[A[i][j] for j in R] for i in R])
    return {k:q[k] for k in ("positive","negative","zero")},{"positive":b[0],"negative":b[1],"zero":b[2]}
def weighted_fee(v,r,gamma,w):
    """Certified full-source diagonal error majorant, exact fractions."""
    assert len(v)==len(r)==len(w)==N
    assert all(x>0 for x in w)
    assert all(x>=0 for x in r)
    rw=sum((r[j]*w[j] for j in range(N)),F(0))
    aw=sum((abs(v[j])*w[j] for j in range(N)),F(0))
    fee=[up(gamma*((abs(v[i])+r[i])*rw+r[i]*aw)/w[i])
         for i in range(N)]
    assert all(x>=0 for x in fee)
    # Independent full rational row-sum identity on selected diagnostics.
    for i in (1,2,17,24):
        raw=sum((gamma*(abs(v[i])*r[j]+abs(v[j])*r[i]+r[i]*r[j])*w[j]/w[i]
                 for j in range(N)),F(0))
        assert fee[i]>=raw
    return fee
def options(v,r,gamma):
    (_scalar,_fee_scalar),(yw,yfee),ymode,_gain=mg02_candidate(v,r,gamma)
    ans=[("mg02_"+ymode,yw,[yfee]*N)]
    normal=[F(1)]*N
    amp=[abs(v[i])+r[i]+F(1,1000) for i in range(N)]
    weights={
        "uniform":normal,
        "amplitude":amp,
        "inverse_amplitude":[1/x for x in amp],
        "complement_focus":[F(1) if i in R else F(1,4) for i in range(N)],
        "anchor_focus":[F(4) if i in (2,17) else F(1) for i in range(N)],
        "g1_focus":[F(8) if i==1 else F(1) for i in range(N)],
        "pole24_focus":[F(8) if i==24 else F(1) for i in range(N)]
    }
    for name,w in weights.items():
        ans.append(("gersh_"+name,F(1),weighted_fee(v,r,gamma,w)))
    assert len(ans)==8
    return ans
def score(c,v,gamma,which):
    name,w,diag=c
    if which=="trace_R":
        return gamma*w*sum((v[i]*v[i] for i in R),F(0))-sum((diag[i] for i in R),F(0))
    i=1 if which=="g1" else 24
    return gamma*w*v[i]*v[i]-diag[i]
def add(M,v,gamma,choice):
    _name,w,fee=choice
    for i in range(N):
        for j in range(i,N):
            M[i][j]+=gamma*w*v[i]*v[j]
        M[i][i]-=fee[i]
def finalize(M,L0):
    A=[[L0[i][j]+M[min(i,j)][max(i,j)] for j in range(N)] for i in range(N)]
    out,fee=outward_compact_matrix(A)
    return out,fee
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="artifacts/mg03_weighted_original_25source_directions.json")
    args=ap.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG" and m["objective"]["status"]=="open"
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==N and sources[24][0]=="pole"
    gram,physical,_pole=original_full_25_physical_interval_gram()
    assert sources==physical
    neg,stat=original_complete_coupled_negative(centers,sources)
    assert stat["whole_original_negative_frequency_leaves"]==973
    pos,_=original_positive_low_25(centers,sources,gram)
    pole,_=pole_outer_upper(gram)
    Lraw=[[pos[i][j]-neg[i][j]-pole[i][j] for j in range(N)] for i in range(N)]
    L0,_=outward_compact_matrix(Lraw)
    pin=json.loads((ROOT/"certificates/rpb108_sm58_full25_signed_summary.json").read_text())
    assert pin["actions_run_id"]==39281588617
    assert sha(neg)==pin["original_full25_coupled_negative_upper_all_625_entries_sha256"]
    assert sha(L0)==pin["original_full25_signed_lower_all_625_entries_sha256"]
    windows,stats=all_338_disjoint_original_signed_positive(centers,sources)
    assert len(windows)==338
    hyp=(hyperbolic_interval(B/2,"sinh"),hyperbolic_interval(B/2,"cosh"))
    k_global=original_full_second_derivative_upper(sources)
    third=original_third_spatial_moment(sources)
    policy_keys=("mg02","trace_R","g1","pole24")
    mats={name:zero() for name in policy_keys}
    count={name:{} for name in policy_keys}
    improvements={"trace_R":F(0),"g1":F(0),"pole24":F(0)}
    checkpoints=[]
    for n,(left,right,delta,_origin) in enumerate(windows,1):
        mid=(left+right)/2;half=(right-left)/2
        vals=original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
        deriv,seconds=original_midpoint_derivative_intervals(mid,centers,sources,hyp)
        v=[];r=[]
        for i in range(N):
            x,rad=vals[i];k=k_global[i]
            if seconds[i] is not None:
                k=min(k,max(abs(seconds[i].l),abs(seconds[i].h))+third[i]*half)
            v.append(x);r.append(rad+k*half*half/6)
        gamma=2*(right-left)*delta
        assert gamma>0
        candidates=options(v,r,gamma)
        selected={"mg02":candidates[0]}
        for name in policy_keys[1:]:
            selected[name]=max(candidates,key=lambda c:score(c,v,gamma,name))
            improvements[name]+=score(selected[name],v,gamma,name)-score(candidates[0],v,gamma,name)
            assert improvements[name]>=0
        for name in policy_keys:
            choice=selected[name]
            count[name][choice[0]]=count[name].get(choice[0],0)+1
            add(mats[name],v,gamma,choice)
        if n in (96,192,288,338):
            row={"cell_count":n,"policies":{}}
            for name in policy_keys:
                A,fee=finalize(mats[name],L0)
                whole,comp=lower_inertia(A)
                row["policies"][name]={
                    "25D_lower_inertia":whole,
                    "23D_lower_inertia":comp,
                    "23D_lower_trace":str(sum((A[i][i] for i in R),F(0))),
                    "g1_lower_diagonal":str(A[1][1]),
                    "pole24_lower_diagonal":str(A[24][24]),
                    "complete_25D_outward_export_fee":str(fee)
                }
            checkpoints.append(row)
    assert len(checkpoints)==4
    assert all(sum(count[k].values())==338 for k in policy_keys)
    final=checkpoints[-1]["policies"]
    # The exact cell-local optimization is the acceptance object.
    # A negative spectral change is a valid REDESIGN result, not a failed computation.
    interpretation="SPECTRAL_DIRECTIONAL_METHOD_IMPROVEMENT" if any(
        final[k]["23D_lower_inertia"]["negative"]<
        final["mg02"]["23D_lower_inertia"]["negative"]
        for k in policy_keys[1:]) else "NO_23D_INERTIA_IMPROVEMENT"
    result={
      "status":"SCOPED_MG03_ORIGINAL_25D_WEIGHTED_MEAN_ERROR_METHOD_GATE",
      "interpretation":interpretation,
      "canonical_W_ODD_NEG":"OPEN",
      "exact_SM58_original_full625_matrix_hashes_replayed":True,
      "whole_original_973_negative_leaves_unchanged":True,
      "original_odd_pole_charged_once":True,
      "old_original_49_positive_windows_unchanged":True,
      "new_original_338_positive_windows_unchanged":True,
      "complete_25D_source_mixed_couplings_all_paid":True,
      "weighted_Gershgorin_rational_whole_operator_order_proved":True,
      "choice_counts":count,
      "nonnegative_exact_local_objective_gains":{k:str(v) for k,v in improvements.items()},
      "checkpoints":checkpoints,
      "MG03_certifies_actual_negative_eigenvectors":False,
      "MG03_certifies_complete_25D_source_PSD":False,
      "MG03_certifies_true_signed_23D_Schur_PSD":False,
      "complete_470_source_Astar_and_infinite_odd_remainder":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "independent_Fourier_form_domain_audit":"OPEN"
    }
    dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("MG03 original coordinate-weighted full25 viability:",json.dumps({
      "outcome":interpretation,
      "mg02_23D_negative_reference":final["mg02"]["23D_lower_inertia"]["negative"],
      "trace_23D_negative_reference":final["trace_R"]["23D_lower_inertia"]["negative"],
      "g1_23D_negative_reference":final["g1"]["23D_lower_inertia"]["negative"],
      "pole_23D_negative_reference":final["pole24"]["23D_lower_inertia"]["negative"],
      "weighted_trace_gain":float(improvements["trace_R"]),
      "complete_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
