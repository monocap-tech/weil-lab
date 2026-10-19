#!/usr/bin/env python3
"""SM62: lift 338 genuine original signed-positive real windows to ALL
25 physically supported odd SI10 sources; target complement C, not
merely mixed-block B.

SM58 original Q_25 >= L58 is a full original 25x25 Loewner LOWER.
Its positive part already credits exactly 17 SM12 and 32 SM49
original positive windows, plus the baseline kappa*physical Gram.
SM54 (96 original sign-positive windows) and SM55 (242 additional
disjoint original sign-positive cells) were previously proved only
in a 3-source trial subspace. Each of the 338 new cells can ALSO
contribute to the original full 25x25 positive source lower, but
with complete 25-source physical Fourier mean and approximation
errors, including every original offdiagonal.

For each original true signed m(xi)>=m_lower(I)>1/5 and kappa,
a_o=max(kappa,m)>=kappa+(m_lower-kappa) on the ENTIRE real cell.
SM58's positive source baseline already pays kappa*H, hence the
only new positively credited weight is delta=m_lower-kappa, NOT
the entire signed m_lower (which would double-count kappa H).

On I=[c-r,c+r], true original 25-vector physical Fourier mean u
is enclosed by exact rational v and sourcewise
|u_i-v_i|<=midpoint_error_i+K_i*r²/6,
where K_i are SM44/46 whole-real 2nd-derivative bounds.
Therefore true signed excess source contribution >=
 gamma*(v v^T - eta I25),
 gamma=2|I|delta, eta=2 sqrt(||v||²||e||²)+||e||²,
by vector Cauchy, with all 25 mixed source couplings paid.
A disjoint union of these extra positive contributions may be
added to the verified SM58 true signed Loewner LOWER without
altering its original 973-leaf negative upper, old 49 windows or
exceptional sinh pole correction.

Evaluate 96 base SM54 cells and the 242 SM55 best-prefix windows
at cumulative checkpoints (96,192,288,338), exporting each
whole 25x25 rational LOWER with full symmetric max-row-error fee.
Exact 25D inertia and the 23-source coordinate compression inertia
are measured separately and compared to verified SM58 reference.
Never infer a negative ACTUAL direction from an indefinite lower.
True 23D signed Schur C-B^T A^-1 B is NOT classified. Complete
original 470 Astar inverse/infinite odd orthogonal remainder,
even, Weil/CC27/RH stay OPEN. Original Fourier/domain premises
still need independent mathematical audit.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    hyperbolic_interval,original_full_25_physical_interval_gram)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,ceil_rat)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    original_exact_physical_fourier_midpoint,
    original_full_second_derivative_upper,sqrt_upper)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_midpoint_derivative_intervals,original_third_spatial_moment)
from validate_rpb108_sm54_original_pole_adaptive_Jensen import (
    discover_new_real_positive)
from validate_rpb108_sm55_hierarchical_signed_pole import (
    candidates,baseline,exact_best_prefix)
from validate_rpb108_sm53_original_3source_pole import pair_source
from validate_rpb108_sm49_adaptive_positive_jensen import (
    original_adaptive_candidate_cells)
from validate_rpb108_sm12_positive_reference_33 import CENTERS as OLD_C,RADIUS as OLD_R
from validate_rpb108_sm57_original_25source_negative_upper import (
    original_positive_low_25,pole_outer_upper,
    outward_compact_matrix,exact_symmetric_25source_inertia)
from validate_rpb108_sm58_original_coupled_25negative import (
    original_complete_coupled_negative)

N=25
COORD_REM=tuple(i for i in range(N) if i not in (2,17))
DEN=10**12
def up(x):return ceil_rat(x,DEN)
def sym(A):return all(A[i][j]==A[j][i] for i in range(len(A)) for j in range(len(A)))
def sha(M):
    return hashlib.sha256(json.dumps([[str(z) for z in row] for row in M],
                 separators=(",",":"),ensure_ascii=True).encode("utf-8")).hexdigest()
def zeros():return [[F(0) for j in range(N)] for i in range(N)]

def all_338_disjoint_original_signed_positive(centers,sources):
    original54,stats=discover_new_real_positive(centers,sources)
    assert len(original54)==243
    top96=original54[:96]
    indices,c=pair_source(centers,sources)
    assert indices==(2,17,24) and c==F(1845,128)
    rows,sm55stats=candidates(centers,sources,indices)
    base,s0=baseline()
    candidate,_s,n,_minors,_samples=exact_best_prefix(base,s0,rows)
    assert n==242 and len(rows)==288
    # Original 3source verified SM55 provenance: first n=242
    # are exactly the original chosen signed positive prefix.
    new=[]
    for value,a,b,old_delta in top96:
        assert old_delta>F(1,5)
        delta=old_delta-KAPPA
        assert delta>0
        new.append((a,b,delta,"SM54_96"))
    for _value,a,b,coefficient,_fee,_v,_level in rows[:n]:
        signed_delta=coefficient/(2*(b-a))
        assert signed_delta>F(1,5)
        delta=signed_delta-KAPPA
        assert delta>0
        new.append((a,b,delta,"SM55_242"))
    assert len(new)==338
    original49,_avail,_r,_c=original_adaptive_candidate_cells(centers,sources)
    assert len(original49)==32
    old_bands=[(c-OLD_R,c+OLD_R) for c in OLD_C]
    old_bands.extend((w["a"],w["b"]) for w in original49)
    assert len(old_bands)==49
    original=[(l,r) for l,r,delta,typ in new]
    ordered=sorted(original)
    assert len(set(ordered))==338
    assert all(ordered[i][1]<=ordered[i+1][0] for i in range(337))
    assert all(F(0)<=l<r<=F(13) for l,r in ordered)
    assert all(all(r<=a or l>=b for a,b in old_bands) for l,r in ordered)
    return new,{"sm54_selected_disjoint_signed_cells":96,
                "sm55_selected_additional_signed_cells":242,
                "already_credited_original_positive_windows":49,
                "new_original_full25_sign_positive_disjoint_cells":338,
                "sm55_original_refined_real_signed_cells_examined":
                   sm55stats["new_exact_real_signed_refined_cells_examined"]}

def selected_full25_source_extra(centers,sources,intervals):
    hyp=(hyperbolic_interval(B/2,"sinh"),
         hyperbolic_interval(B/2,"cosh"))
    K_global=original_full_second_derivative_upper(sources)
    third=original_third_spatial_moment(sources)
    assert len(K_global)==len(third)==N
    P=zeros();fee=F(0);strict_local=0
    checkpoints={}
    counts={"SM54_96":0,"SM55_242":0}
    maximum_cell_fee=F(0)
    for n,(l,r,delta,origin) in enumerate(intervals,1):
        assert F(0)<=l<r<=13 and delta>0
        counts[origin]+=1
        mid=(l+r)/2;half=(r-l)/2
        vals=original_exact_physical_fourier_midpoint(
            mid,centers,sources,hyp)
        derivs,seconds=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        assert len(vals)==len(derivs)==len(seconds)==N
        v=[];radii=[]
        for i in range(N):
            vi,mid_rad=vals[i]
            curvature=K_global[i]
            if seconds[i] is not None:
                local=max(abs(seconds[i].l),abs(seconds[i].h))+third[i]*half
                curvature=min(curvature,local)
            assert 0<=curvature<=K_global[i]
            strict_local+=int(curvature<K_global[i])
            radius=mid_rad+curvature*half*half/6
            assert radius>=0
            v.append(vi);radii.append(radius)
        v2=sum((z*z for z in v),F(0))
        e2=sum((z*z for z in radii),F(0))
        eta=2*sqrt_upper(v2*e2)+e2
        gamma=2*(r-l)*delta
        eps=up(gamma*eta)
        assert eps>=gamma*eta>=0
        fee+=eps
        maximum_cell_fee=max(maximum_cell_fee,eps)
        for i in range(N):
            for j in range(i,N):
                P[i][j]+=gamma*v[i]*v[j]
        if n in (96,192,288,338):
            current=[[P[i][j] for j in range(N)] for i in range(N)]
            for i in range(N):
                for j in range(i):
                    current[i][j]=current[j][i]
            checkpoints[n]={"matrix":current,"total_extra_error_fee":fee}
    for i in range(N):
        for j in range(i):
            P[i][j]=P[j][i]
    assert sym(P)
    assert counts=={"SM54_96":96,"SM55_242":242}
    assert set(checkpoints)=={96,192,288,338}
    return checkpoints,{
      "new_source_positive_checked":sum(counts.values()),
      "new_source_positive_by_original_front":counts,
      "strict_original_25D_source_local_curvature_improvements":strict_local,
      "max_one_original_signed_real_window_25D_Loewner_fee":str(up(maximum_cell_fee)),
      "total_338_original_full25_mean_Loewner_error":str(fee)
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm62_original_338_signed_positive_full25_lower.json")
    args=p.parse_args()
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in ledger["obligations"] if o["id"]=="W-ODD-NEG")
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==ledger["objective"]["status"]=="open"
    assert ledger["governance"]["no_automatic_promotion"]
    assert all(k in odd["evidence"] for k in ("SM47","SM49","SM55","SM58","SM59","SM60","SM61","SM62"))
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==25 and sources[24][0]=="pole"
    gram,physical,_pole=original_full_25_physical_interval_gram()
    assert sources==physical
    Nupper,negstat=original_complete_coupled_negative(centers,sources)
    assert negstat["whole_original_negative_frequency_leaves"]==973
    Pbase,posstat=original_positive_low_25(centers,sources,gram)
    pole,polefee=pole_outer_upper(gram)
    L_exact=[[Pbase[i][j]-Nupper[i][j]-pole[i][j] for j in range(N)]
             for i in range(N)]
    L0,rounding=outward_compact_matrix(L_exact)
    pin=json.loads((ROOT/"certificates/rpb108_sm58_full25_signed_summary.json").read_text())
    assert pin["actions_run_id"]==39281588617
    assert sha(Nupper)==pin["original_full25_coupled_negative_upper_all_625_entries_sha256"]
    assert sha(L0)==pin["original_full25_signed_lower_all_625_entries_sha256"]
    inertia0=exact_symmetric_25source_inertia(L0)
    assert (inertia0["positive"],inertia0["negative"],inertia0["zero"])==(1,24,0)
    signed,stats=all_338_disjoint_original_signed_positive(centers,sources)
    checkpoints,extras=selected_full25_source_extra(centers,sources,signed)
    choices=[]
    for n in (96,192,288,338):
        P=checkpoints[n]["matrix"]
        eps=checkpoints[n]["total_extra_error_fee"]
        true_low=[[L0[i][j]+P[i][j]-(eps if i==j else F(0))
                   for j in range(N)] for i in range(N)]
        out,export=outward_compact_matrix(true_low)
        inertia=exact_symmetric_25source_inertia(out)
        R=[[out[i][j] for j in COORD_REM] for i in COORD_REM]
        inertia_R=exact_symmetric_25source_inertia(
            [[R[i][j] if i==j else R[i][j] for j in range(23)]
             for i in range(23)]+[[F(0)]*25 for _ in ()]
        ) if False else None
        # Exact square-free 23D inertia via rational 1x1/2x2
        # congruence implemented with a dimension-generic helper.
        rcounts=exact_inertia_general(R)
        assert sum(rcounts)==23
        assert sum(inertia[k] for k in ("positive","negative","zero"))==25
        choices.append({
          "count":n,
          "whole_25D_signed_lower_exact_inertia":inertia,
          "23D_coordinate_complement_lower_exact_inertia":{
              "positive":rcounts[0],"negative":rcounts[1],"zero":rcounts[2]},
          "complete_25D_source_positive_added_mean_Loewner_fee":str(eps),
          "signed_full25_outward_rational_rounding_fee":str(export),
          "signed_lower_trace":str(sum((out[i][i] for i in range(25)),F(0))),
          "source2_signed_lower_diagonal":str(out[2][2]),
          "source17_signed_lower_diagonal":str(out[17][17]),
          "source24_pole_signed_lower_diagonal":str(out[24][24]),
          "matrix":out
        })
    best=min(choices,key=lambda a:(a["whole_25D_signed_lower_exact_inertia"]["negative"],
                      -F(a["signed_lower_trace"])))
    out={
     "status":"SCOPED_ORIGINAL_338_NEW_TRUE_SIGNED_POSITIVE_WINDOWS_FULL_25SOURCE_LOEWNer_LOWER",
     "canonical_W_ODD_NEG":"OPEN",
     "whole_real_negative_operator_973_leaves_and_original_pole_unchanged":True,
     "original_source_count":25,
     "original_25x25_SM58_negative_upper_hash_replayed":True,
     "original_25x25_SM58_signed_lower_hash_replayed":True,
     "source_full25_prior_signed_lower_inertia":inertia0,
     "original_baseline_49_positive_windows_already_paid":True,
     **stats,**extras,
     "new_original_25source_signed_positive_added_only_excess_over_kappa":True,
     "new_original_25source_complete_Fourier_offdiagonals_and_outward_errors_paid":True,
     "checkpoints_inertias":[{k:v for k,v in a.items() if k!="matrix"} for a in choices],
     "best_checkpoint":best["count"],
     "best_complete_original_25D_signed_LOWER_inertia":best["whole_25D_signed_lower_exact_inertia"],
     "best_complete_original_23D_coordinate_LOWER_inertia":best["23D_coordinate_complement_lower_exact_inertia"],
     "best_complete_signed_25D_LOWER_matrix":[[str(x) for x in row] for row in best["matrix"]],
     "best_actual_source25_negative_index_upper_via_LOWER":best["whole_25D_signed_lower_exact_inertia"]["negative"],
     "actual_original_25D_source_negative_index_upper_SM59A":23,
     "best_total_original_25D_negative_index_upper":min(
        23,best["whole_25D_signed_lower_exact_inertia"]["negative"]),
     "actual_signed_23D_Schur_PSD_or_index_certified":False,
     "complete_infinite_original_odd_negative_index_certified":False,
     "original_470_Astar_inverse_and_strong_orthogonal_remainder":False,
     "even_Weil_CC27_RH":False,
     "independent_original_Fourier_form_domain_audit":"OPEN",
     "interpretation":"New original 338 strict signed-positive disjoint real cells from SM54/SM55 lifted to all 25 original source Fourier coefficients after subtracting already paid kappa, each complete 25D Jensen mean error and all offdiagonals charged; no actual negative witness or entire odd Schur proof from a negative LOWER."
    }
    target=ROOT/args.output
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+"\n")
    print("SM62 original additional 338 signed windows full25:",json.dumps({
      "extra_windows":338,
      "baseline_lower_neg_inertia":inertia0["negative"],
      "best_checkpoint":best["count"],
      "best_lower_negative_inertia":best["whole_25D_signed_lower_exact_inertia"]["negative"],
      "best_23coordinate_lower_negative_inertia":best["23D_coordinate_complement_lower_exact_inertia"]["negative"],
      "true_restricted_source_negative_index_upper":out["best_total_original_25D_negative_index_upper"],
      "full_actual_schur_and_odd_Weil_RH":"OPEN"
    }),flush=True)

def exact_inertia_general(M):
    a=[row[:] for row in M];n=len(a);plus=minus=zero=0
    while n:
        diag=next((i for i in range(n) if a[i][i]!=0),None)
        if diag is not None:
            if diag:
                a[0],a[diag]=a[diag],a[0]
                for row in a:row[0],row[diag]=row[diag],row[0]
            p=a[0][0]
            if p>0:plus+=1
            else:minus+=1
            a=[[a[i][j]-a[i][0]*a[0][j]/p for j in range(1,n)]
               for i in range(1,n)]
            n-=1
        else:
            pair=next(((i,j) for i in range(n) for j in range(i+1,n) if a[i][j]!=0),None)
            if pair is None:zero+=n;break
            ii,jj=pair
            order=[ii,jj]+[k for k in range(n) if k not in pair]
            b=[[a[i][j] for j in order] for i in order]
            p=b[0][1]
            a=[[b[i][j]-(b[i][0]*b[1][j]+b[i][1]*b[0][j])/p for j in range(2,n)]
               for i in range(2,n)]
            plus+=1;minus+=1;n-=2
    assert plus+minus+zero==len(M)
    return (plus,minus,zero)

if __name__=="__main__":main()
