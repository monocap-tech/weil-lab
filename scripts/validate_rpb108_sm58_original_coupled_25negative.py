#!/usr/bin/env python3
"""SM58: first original full-source COUPLED negative Fourier covariance UPPER.

On ALL 973 actual original SI10 whole-real signed-negative cover leaves,
certify the true original 25-component physical Fourier vector using
SM42 analytic sine/xcos/sinh values and SM46 1st/2nd frequency
derivatives. The entire original negative operator is upper-bounded:
 K_neg,25 = 2 int (kappa-m(xi))_+ T(xi)T(xi)^T dxi
          <= U58 = 2 sum_I |I| w_I
                (v_I v_I^T + (|I|^2/12) d_I d_I^T + e_I I25).
All original signed-negative multipliers w_I are TRUE whole-real
UPPER on their dyadic leaves. The complete Fourier Taylor error
e_I=2 sqrt(V2*R2)+R2 is true Loewner; R2=sum_i R_i² where
R_i=e_value_i + e_deriv_i*r + K_i*r²/2.
V2=sum_i(v_i²+d_i²*r²/3).
The derivative term's mean is EXACTLY zero in the symmetric
frequency cell. The upper matrix retains ALL 625 mixed original
physical source correlations, 16 sin, 8 xcos, true sinh pole.

SM57 independently gives a (likely loose) true diagonal upper
D57 on the SAME original entire signed negative source operator.
For any rational t in [0,1], U_t=(1-t)U58+t D57 is also valid.
Do NOT claim U58<=D57 unless a PSD proof actually verifies it.
Construct signed lower L_t=positiveLOW_25-U_t-poleUPPER,
symmetrically compact/export with outward max-row-sum fee.
Classify inertia of LOWER only. True signed negative index of actual
25-dimensional restricted form is at most nneg(L_t), NOT exactly
this number; negative LOWER eigenvalues are no witnesses.
Full original 470 Astar/infinite orthogonal remainder, odd O1/O2,
even/Weil/CC27/RH remain OPEN.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B,PI
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    hyperbolic_interval,original_full_25_physical_interval_gram)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,ceil_rat)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    original_exact_physical_fourier_midpoint,
    original_full_second_derivative_upper,quantize,sqrt_upper)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_midpoint_derivative_intervals,original_third_spatial_moment)
from validate_rpb108_sm57_original_25source_negative_upper import (
    complete_original_negative_upper_diagonal,original_positive_low_25,
    pole_outer_upper,outward_compact_matrix,exact_symmetric_25source_inertia)

N=25
DEN=10**9
OUT=10**12
def up(x):return ceil_rat(x,DEN)
def zeros():return [[F(0)]*N for _ in range(N)]
def add_weighted(m,v,d,half,coefficient):
    dcoeff=coefficient*half*half/3
    for i in range(N):
        for j in range(i,N):
            m[i][j]+=coefficient*v[i]*v[j]+dcoeff*d[i]*d[j]

def original_complete_coupled_negative(centers,sources):
    clusters,W,Mneg,mass=full_upper_leaves()
    leaves=[c for cluster in clusters for c in cluster]
    assert len(clusters)==107 and len(leaves)==973 and W==F(973,32)
    assert len(sources)==N and sources[24][0]=="pole"
    hyp=(hyperbolic_interval(B/2,"sinh"),hyperbolic_interval(B/2,"cosh"))
    K_global=original_full_second_derivative_upper(sources)
    K3=original_third_spatial_moment(sources)
    matrix=zeros();fee=F(0);local_second_improved=0
    intervals=0;mass_paid=F(0)
    max_cell_error=F(0)
    for a,b,h in leaves:
        half=(b-a)/2
        mid=(a+b)/2
        assert half>0
        # This coefficient is an original all-real signed NEGATIVE
        # spectral weight UPPER for EVERY xi in the entire dyadic leaf.
        weight=up(h+KAPPA)
        assert weight>=h+KAPPA>0
        vals=original_exact_physical_fourier_midpoint(
            mid,centers,sources,hyp)
        derivs,secs=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        assert len(vals)==len(derivs)==len(secs)==N
        v=[];d=[];rem=[]
        for i in range(N):
            vi,e0=vals[i]
            deriv=derivs[i]
            di=quantize(deriv.mid())
            ed=up(max(abs(deriv.l-di),abs(deriv.h-di)))
            k=K_global[i]
            if secs[i] is not None:
                k=min(k,max(abs(secs[i].l),abs(secs[i].h))+K3[i]*half)
            assert 0<=k<=K_global[i]
            local_second_improved+=int(k<K_global[i])
            vi=F(vi);di=F(di)
            ri=up(e0+ed*half+k*half*half/2)
            assert ri>=0
            v.append(vi);d.append(di);rem.append(ri)
        V2=sum((v[i]*v[i]+d[i]*d[i]*half*half/3 for i in range(N)),F(0))
        R2=sum((x*x for x in rem),F(0))
        # This bounds the Loewner error of TRUE cell integrated
        # full 25x25 Fourier Gram vs exactly integrated affine proxy.
        er=up(2*sqrt_upper(V2*R2)+R2)
        assert er>=0
        coefficient=2*(b-a)*weight
        add_weighted(matrix,v,d,half,coefficient)
        fee+=coefficient*er
        mass_paid+=coefficient
        max_cell_error=max(max_cell_error,er)
        intervals+=1
    assert intervals==973 and mass_paid>=mass
    # Exact affine proxy sums computed in upper triangular part to
    # save time; restore all mixed entries before adding a scalar fee.
    for i in range(N):
        for j in range(i):
            matrix[i][j]=matrix[j][i]
        matrix[i][i]+=fee
    assert all(matrix[i][j]==matrix[j][i] for i in range(N) for j in range(N))
    assert all(matrix[i][i]>=0 for i in range(N))
    # Compact only after complete rational proof; MAX ROW SUM error
    # charged upward makes the OUTPUT another genuine UPPER.
    q=[[quantize(matrix[i][j]) for j in range(N)] for i in range(N)]
    assert all(q[i][j]==q[j][i] for i in range(N) for j in range(N))
    maxerr=max(sum(abs(q[i][j]-matrix[i][j]) for j in range(N)) for i in range(N))
    export_fee=ceil_rat(maxerr,OUT)
    upper=[[q[i][j]+(export_fee if i==j else F(0))
             for j in range(N)] for i in range(N)]
    assert all(upper[i][j]==upper[j][i] for i in range(N) for j in range(N))
    return upper,{
        "whole_original_negative_frequency_leaves":intervals,
        "whole_original_negative_frequency_clusters":len(clusters),
        "true_original_25source_full_coupled_Fourier_and_derivatives":True,
        "full_original_physical_Fourier_2nd_derivative_local_improvements":local_second_improved,
        "total_original_negative_weighted_affine_source_Gram_error":str(ceil_rat(fee,OUT)),
        "max_original_25source_cell_Fourier_remainder_Loewner_error":str(ceil_rat(max_cell_error,OUT)),
        "negative_full25_source_coupled_rational_export_upper_fee":str(export_fee),
        "full_25source_negative_frequency_coupled_upper_rational":[
            [str(x) for x in row] for row in upper]
    }

def matrix_mix(a,b,t):
    assert 0<=t<=1
    return [[(1-t)*a[i][j]+t*b[i][j] for j in range(N)]
            for i in range(N)]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm58_original_complete_coupled_negative_25source.json")
    args=p.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]==odd["status"]=="open"
    assert m["governance"]["no_automatic_promotion"]
    assert "SM57" in odd["evidence"] and "SM58" in odd["evidence"]
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==N
    gram,src,pole=original_full_25_physical_interval_gram()
    assert src==sources
    U,ustats=original_complete_coupled_negative(centers,sources)
    D,diagstats=complete_original_negative_upper_diagonal(centers,sources)
    P,pstats=original_positive_low_25(centers,sources,gram)
    polemat,poleerr=pole_outer_upper(gram)
    diag_up=[[D[i] if i==j else F(0) for j in range(N)] for i in range(N)]
    # Both full original NEGATIVE operator UPPER bounds hold separately.
    # Convex interpolation is therefore valid for every t; never
    # assert one dominates the other unless proven.
    tested=[]
    for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        neg=matrix_mix(U,diag_up,t)
        low=[[P[i][j]-neg[i][j]-polemat[i][j] for j in range(N)]
             for i in range(N)]
        compact,err=outward_compact_matrix(low)
        inertia=exact_symmetric_25source_inertia(compact)
        tested.append({
            "mix_with_SM57_diagonal_negative_UPPER":str(t),
            "true_signed_lower_inertia":inertia,
            "true_signed_lower_trace":str(sum((compact[i][i] for i in range(N)),F(0))),
            "true_signed_lower_source2":str(compact[2][2]),
            "rational_lower_matrix_outward_fee":str(err),
            "matrix":compact
        })
    best=min(tested,key=lambda x:(x["true_signed_lower_inertia"]["negative"],
                   -F(x["true_signed_lower_trace"])))
    chosen=best["matrix"]
    best_t=F(best["mix_with_SM57_diagonal_negative_UPPER"])
    assert all(chosen[i][j]==chosen[j][i] for i in range(N) for j in range(N))
    best_inertia=best["true_signed_lower_inertia"]
    assert sum(best_inertia[k] for k in ("positive","negative","zero"))==N
    out={
       "status":"SCOPED_ORIGINAL_FULL_25SOURCE_COUPLED_NEGATIVE_FOURIER_UPPER_AND_SIGNED_LOWER",
       "canonical_W_ODD_NEG":"OPEN",
       "original_real_supported_physical_source_count":N,
       "original_sources":"16 sin, 8 xcos, one genuine sinh pole",
       "whole_negative_true_original_operator_coupled_upper_proved":True,
       "original_entire_pole_rankone_upper_paid":True,
       **ustats,
       "original_SM57_diagonal_comparison":{
           "full_negative_diagonal_upper":[str(x) for x in D],
           "same_original_negative_frequency_leaves":diagstats["original_negative_true_whole_real_cover_leaves"]},
       "original_positive_low_25source_provenance":{
           "original_positive_full25_source2_diagonal_lower":
                pstats["original_positive_full25_source2_diagonal_lower"],
           "full_25_source_error":pstats["complete_25_positive_source_Gram_and_Jensen_Loewner_error"]},
       "original_pole_rankone_upper_error":str(poleerr),
       "convex_true_negative_upper_mixing_tested":[{
           k:v for k,v in item.items() if k!="matrix"} for item in tested],
       "chosen_true_signed_25source_lower_mixing_coefficient":str(best_t),
       "chosen_true_signed_lower_25source_rational_matrix":[
           [str(x) for x in row] for row in chosen],
       "chosen_true_signed_lower_25source_exact_inertia":best_inertia,
       "certified_actual_original_25source_restricted_negative_index_UPPER":
            best_inertia["negative"],
       "exact_original_25source_actual_negative_index_proved":False,
       "complete_infinite_original_odd_negative_index_proved":False,
       "complete_original_470source_Astar_and_orthogonal_remainder":False,
       "original_odd_O1O2_even_Weil_CC27_RH":False,
       "independent_original_Fourier_closed_domain_audit":"OPEN",
       "interpretation":"True original full 25x25 signed lower via complete 973-leaf coupled Fourier negative UPPER, independent diagonal comparator, 49-window entire positive LOWER, true pole UPPER. Negative inertia ONLY of lower; actual 25D negative index at most its count; infinite-dimensional original odd/even/Weil/RH all OPEN."
    }
    target=ROOT/args.output
    target.parent.mkdir(exist_ok=True,parents=True)
    target.write_text(json.dumps(out,indent=2)+"\n")
    print("SM58 full original 25source coupled negative Fourier:",json.dumps({
      "negative_real_leaves":ustats["whole_original_negative_frequency_leaves"],
      "local_second_derivative_improvements":ustats["full_original_physical_Fourier_2nd_derivative_local_improvements"],
      "negative_scalar_25source_Loewner_fee":ustats["total_original_negative_weighted_affine_source_Gram_error"],
      "chosen_true_source_lower_mix":str(best_t),
      "chosen_lower_negative_inertia":best_inertia["negative"],
      "chosen_lower_positive_inertia":best_inertia["positive"],
      "full_original_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
