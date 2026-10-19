#!/usr/bin/env python3
"""SM59B: per-SI10-leaf actual original 25-source NEGATIVE UPPER HYBRID.

Both SM57 original source-cap diagonal and SM58 original physical
Fourier 25x25 covariance are individually certified Loewner UPPERs
on EVERY original SI10 whole-real negative-frequency dyadic leaf,
not merely after summing. The exact arithmetic permits selecting
which upper to use on each leaf independently, without the false
claim that lower TRACE entails Loewner dominance.

For each of all 973 leaves compute:
    U_i^aff = 2h w [vvT + r²/3 ddT + error*I25]  (SM58)
    U_i^cap = diag_j(2h w s_j sum_k s_k)         (SM57),
with all original analytic Fourier values/derivatives, sinh input
and true signed weight whole-real bounds and outward errors.
Choose by exact (a) TRACE, (b) source2 diagonal, (c) source17
diagonal, (d) physical pole24 diagonal. Each sum of selected
local UPPERs is a valid full original 25x25 signed-negative
UPPER, including ALL mixed source coefficients, irrespective
of comparisons among these different upper matrices.

Add full SM47+SM49 original 25x25 positiveLOW and subtract true
SM42 sinh pole UPPER, pay entire 25x25 rational export fee,
classify exact rational LOWER inertia per selector. No actual
negative mode follows from negative LOWER eigenvalues.

SM59A *independently* proves the original actual physically
supported 25D negative index <=23 from an SM52 coupled positive
2-plane; never splice this 2x2 result into the larger Loewner
LOWER without real mixed-source estimates. Full odd source-
eliminated infinite remainder, O1/O2, even/Weil/CC27/RH OPEN.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    hyperbolic_interval,original_full_25_physical_interval_gram)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,source_window_support_envelopes,
    ceil_rat)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    original_exact_physical_fourier_midpoint,
    original_full_second_derivative_upper,quantize,sqrt_upper)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_midpoint_derivative_intervals,original_third_spatial_moment)
from validate_rpb108_sm57_original_25source_negative_upper import (
    original_positive_low_25,pole_outer_upper,
    outward_compact_matrix,exact_symmetric_25source_inertia)

N=25
PREC=10**9
OUT=10**12
METHODS=("trace","source2","source17","pole24")
def zeros():return [[F(0)]*N for _ in range(N)]
def up(x,den=PREC):return ceil_rat(x,den)
def rawtrace(M):return sum((M[i][i] for i in range(N)),F(0))
def symmetric(M):return all(M[i][j]==M[j][i] for i in range(N) for j in range(N))
def upper_export(M):
    assert symmetric(M)
    q=[[quantize(M[i][j]) for j in range(N)] for i in range(N)]
    assert symmetric(q)
    err=up(max(sum(abs(M[i][j]-q[i][j]) for j in range(N)) for i in range(N)),OUT)
    U=[[q[i][j]+(err if i==j else F(0)) for j in range(N)] for i in range(N)]
    assert symmetric(U)
    return U,err

def leafwise_full_original_signed_negative(centers,sources):
    clusters,W,Mneg,mass=full_upper_leaves()
    assert len(clusters)==107 and W==F(973,32)
    leaves=[leaf for cl in clusters for leaf in cl]
    assert len(leaves)==973 and len(sources)==N
    hyp=(hyperbolic_interval(B/2,"sinh"),
         hyperbolic_interval(B/2,"cosh"))
    K=original_full_second_derivative_upper(sources)
    K3=original_third_spatial_moment(sources)
    coupled=zeros()
    diagonal=[F(0)]*N
    replaces={m:zeros() for m in METHODS}
    selected={m:0 for m in METHODS}
    local_gain={m:F(0) for m in METHODS}
    local_improvements=0
    sum_width=F(0);sum_weight=F(0);count=0
    local_extra_fee=F(0)
    for left,right,h in leaves:
        length=right-left;half=length/2;mid=(left+right)/2
        assert 0<=left<right<=896
        weight=up(h+KAPPA)
        assert weight>=h+KAPPA>0
        coefficient=2*length*weight
        caps0=source_window_support_envelopes(left,right,centers,sources)
        caps=[up(x) for x in caps0]
        assert len(caps)==N and all(c>=c0>0 for c,c0 in zip(caps,caps0))
        capsum=sum(caps,F(0))
        cap_diag=[coefficient*caps[i]*capsum for i in range(N)]
        vals=original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
        deriva,sec=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        assert len(vals)==len(deriva)==len(sec)==N
        v=[];d=[];R=[]
        for i in range(N):
            vi,e0=vals[i]
            di=quantize(deriva[i].mid())
            ed=up(max(abs(deriva[i].l-di),abs(deriva[i].h-di)))
            ki=K[i]
            if sec[i] is not None:
                ki=min(ki,max(abs(sec[i].l),abs(sec[i].h))+K3[i]*half)
            assert 0<=ki<=K[i]
            local_improvements+=int(ki<K[i])
            v.append(F(vi));d.append(F(di))
            R.append(up(e0+ed*half+ki*half*half/2))
        V2=sum((v[i]**2+d[i]**2*half*half/3 for i in range(N)),F(0))
        R2=sum((ri**2 for ri in R),F(0))
        er=up(2*sqrt_upper(V2*R2)+R2)
        assert er>=0
        local_extra_fee+=coefficient*er
        affine_diag=[coefficient*(v[i]**2+d[i]**2*half*half/3+er)
                     for i in range(N)]
        affine_trace=sum(affine_diag,F(0))
        cap_trace=sum(cap_diag,F(0))
        scores={
          "trace":(affine_trace,cap_trace),
          "source2":(affine_diag[2],cap_diag[2]),
          "source17":(affine_diag[17],cap_diag[17]),
          "pole24":(affine_diag[24],cap_diag[24])
        }
        choices={m:cap<aff for m,(aff,cap) in scores.items()}
        for m in METHODS:
            if choices[m]:
                selected[m]+=1
                local_gain[m]+=scores[m][0]-scores[m][1]
        dcoef=coefficient*half*half/3
        # All original 625 signed source mixed Fourier entries are kept.
        for i in range(N):
            for j in range(i,N):
                x=coefficient*v[i]*v[j]+dcoef*d[i]*d[j]
                if i==j:x+=coefficient*er
                coupled[i][j]+=x
                for m in METHODS:
                    if choices[m]:
                        # Replace a whole-cell complete affine
                        # covariance UPPER by the independent complete
                        # cap-diagonal UPPER, NOT an entrywise minimum.
                        diff=(cap_diag[i] if i==j else F(0))-x
                        replaces[m][i][j]+=diff
        for i in range(N):diagonal[i]+=cap_diag[i]
        sum_width+=length
        sum_weight+=coefficient
        count+=1
    assert count==973 and 2*sum_width==W and sum_weight>=mass
    # Finish symmetric upper parts only after summing exact leaves.
    for mat in [coupled]+list(replaces.values()):
        for i in range(N):
            for j in range(i):mat[i][j]=mat[j][i]
        assert symmetric(mat)
    Dmat=[[diagonal[i] if i==j else F(0) for j in range(N)] for i in range(N)]
    original_coupled,Ufee=upper_export(coupled)
    original_diag=[up(x,OUT) for x in diagonal]
    assert all(original_diag[i]>=diagonal[i] for i in range(N))
    options={
      "original_SM58_coupled":(coupled,original_coupled,Ufee),
      "original_SM57_diagonal":(Dmat,Dmat,None)
    }
    for m in METHODS:
        raw=[[coupled[i][j]+replaces[m][i][j] for j in range(N)]
             for i in range(N)]
        assert symmetric(raw)
        U,e=upper_export(raw)
        options["leafwise_"+m]=(raw,U,e)
    assert local_gain["trace"]>=0
    assert rawtrace(options["leafwise_trace"][0])<=rawtrace(coupled)
    assert rawtrace(options["leafwise_trace"][0])<=rawtrace(Dmat)
    assert selected["trace"]>=0
    return options,{
      "all_original_negative_whole_real_leaves":count,
      "negative_107_original_clusters":len(clusters),
      "negative_one_sided_width":str(sum_width),
      "physical_all25_analytic_local_second_derivative_improvements":local_improvements,
      "original_negative_coupled_total_Loewner_remainder":str(up(local_extra_fee,OUT)),
      "per_leaf_cap_selection_counts":selected,
      "per_leaf_exact_targeted_raw_gain":{k:str(up(v,OUT)) for k,v in local_gain.items()},
      "pure_coupled_exact_negative_raw_trace":str(up(rawtrace(coupled),OUT)),
      "pure_diagonal_exact_negative_raw_trace":str(up(rawtrace(Dmat),OUT)),
      "locally_trace_chosen_exact_negative_raw_trace":str(up(rawtrace(options["leafwise_trace"][0]),OUT)),
      "source_coupled_original_25x25_all_mixed_entries_charged":True
    }

def calculate():
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in manifest["obligations"] if o["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]==odd["status"]=="open"
    assert all(k in odd["evidence"] for k in ("SM57","SM58","SM59"))
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==N and sources[24][0]=="pole"
    options,stats=leafwise_full_original_signed_negative(centers,sources)
    pin=json.loads((ROOT/"certificates/rpb108_sm58_full25_signed_summary.json").read_text())
    assert pin["actions_run_id"]==39281588617
    # Original SM58 upper is EXACTLY the same computation with
    # no per-leaf substitutions; match its final 25D UPPER trace
    # from the source artifact, not a floating approximation.
    original_coupled=options["original_SM58_coupled"][1]
    assert rawtrace(original_coupled)==F(pin["negative_entire_upper_trace_coupled"])
    assert sum((up(x,OUT) for x in [options["original_SM57_diagonal"][0][i][i] for i in range(N)]),F(0))>=F(pin["negative_entire_upper_trace_SM57_diagonal"])
    gram,actual,pole=original_full_25_physical_interval_gram()
    assert actual==sources
    positive,positivestats=original_positive_low_25(centers,sources,gram)
    poleupper,poleerr=pole_outer_upper(gram)
    accepted=[]
    for name,(raw,U,fee) in options.items():
        if name=="original_SM57_diagonal":
            diag=[up(raw[i][i],OUT) for i in range(N)]
            U=[[diag[i] if i==j else F(0) for j in range(N)] for i in range(N)]
            fee=F(0)
        exact=[[positive[i][j]-poleupper[i][j]-U[i][j]
                for j in range(N)] for i in range(N)]
        L,rounding=outward_compact_matrix(exact)
        inertia=exact_symmetric_25source_inertia(L)
        assert sum(inertia[x] for x in ("positive","negative","zero"))==N
        accepted.append({
          "name":name,
          "original_full_source_negative_upper_trace":str(rawtrace(U)),
          "original_full_signed_lower_trace":str(rawtrace(L)),
          "exact_rational_signed_LOWER_inertia":inertia,
          "source2_original_lower":str(L[2][2]),
          "source17_original_lower":str(L[17][17]),
          "pole24_original_lower":str(L[24][24]),
          "negative_matrix_outward_export_fee":str(fee),
          "signed_lower_outward_export_fee":str(rounding),
          "full_signed_lower_matrix":L
        })
    original=next(x for x in accepted if x["name"]=="original_SM58_coupled")
    assert original["exact_rational_signed_LOWER_inertia"]==pin["original_25x25_signed_lower_inertia_for_each_diagonal_mix"]["0"]
    best=min(accepted,key=lambda x:(
      x["exact_rational_signed_LOWER_inertia"]["negative"],
      -F(x["original_full_signed_lower_trace"])
    ))
    assert best["exact_rational_signed_LOWER_inertia"]["negative"]<=24
    out={
      "status":"CERTIFIED_SCOPED_ORIGINAL_25SOURCE_PER_LEAF_COUPLED_NEGATIVE_UPPER_AUDIT",
      "canonical_W_ODD_NEG":"OPEN",
      "actual_physical_source_count":25,
      **stats,
      "source_verified_SM58_25source_Actions_id":39281588617,
      "source_verified_SM57_25source_Actions_id":39275848672,
      "all_full25_original_true_negative_frequency_upper_options_valid":True,
      "signed_positive_full25_LOWER_provenance":positivestats,
      "true_physical_sinh_pole_upper_paid_once":True,
      "pole_upper_outward_fee":str(poleerr),
      "all_methods_complete_25source_signed_lower_inertia":[
          {k:v for k,v in x.items() if k!="full_signed_lower_matrix"} for x in accepted],
      "best_complete_25source_negative_upper_method":best["name"],
      "best_complete_25source_rational_signed_lower_matrix":[
          [str(x) for x in row] for row in best["full_signed_lower_matrix"]],
      "best_original_25source_reference_signed_lower_exact_inertia":
          best["exact_rational_signed_LOWER_inertia"],
      "best_lower_negative_index_upper_on_restricted_source25":
          best["exact_rational_signed_LOWER_inertia"]["negative"],
      "independently_proved_actual_original_25D_negative_index_upper_from_SM52_plane":23,
      "best_available_actual_original_25D_negative_index_upper":
          min(23,best["exact_rational_signed_LOWER_inertia"]["negative"]),
      "actual_original_25D_index_exactly_classified":False,
      "original_infinite_odd_operator_negative_index_classified":False,
      "original_full470_Astar_odd_O1O2_orthogonal_remainder":False,
      "even_Weil_CC27_RH":False,
      "independent_original_Fourier_domain_audit":"OPEN",
      "interpretation":"Every selected original leaf local covariance or source-cap diagonal is separately Loewner upper on all 25 genuine physical sources, all negative real frequencies and pole paid. Inertia belongs only to a signed LOWER. Independent actual positive 2-plane bounds true source25 negative index <=23. Infinite-dimensional original odd operator remains OPEN."
    }
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm59b_original_25source_leafwise_negative_upper.json")
    args=p.parse_args()
    out=calculate()
    path=ROOT/args.output;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("SM59B original full25 leafwise Fourier upper:",json.dumps({
       "whole_negative_leaves":out["all_original_negative_whole_real_leaves"],
       "choice_counts":out["per_leaf_cap_selection_counts"],
       "best_method":out["best_complete_25source_negative_upper_method"],
       "best_signed_lower_inertia":out["best_original_25source_reference_signed_lower_exact_inertia"],
       "actual_restricted_25D_negative_index_ceiling":out["best_available_actual_original_25D_negative_index_upper"],
       "full_original_odd_negative_index":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
