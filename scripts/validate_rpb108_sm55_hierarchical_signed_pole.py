#!/usr/bin/env python3
"""SM55: hierarchical original signed-positive 3x3 pole Schur frontier.

SM54B exhausted all 243 positive pole cells of width 1/32 in [0,13],
but the larger full-matrix Loewner fee gave *worse* certified effective
pole Schur than SM54's first 96. Thus count of cells is NOT the
acceptance metric.

This validator inherits the passing full-original-frequency signed
3x3 Loewner LOWER from the 96-window SM54 Actions run 39212101376.
Retain all original negative contributions, signed [13,16] core,
all 49 old SM12/SM49 positive windows, and actual exceptional sinh
rank-one subtraction AS ALREADY PAID. No certified interval can be
credited again.

On each original 1/32 coarse cell [0,13]:
 - if among original 243 positive candidates but NOT among 96
   previously credited, try that coarse interval once;
 - if it failed the coarse whole-real signed acceptance, split
   into 8 TRUE ORIGINAL 1/256 rational children, certifying each
   directly from inherited SM52 all-seven-prime/digamma real lower;
 - if previously credited (top 96), exclude it entirely.
Any candidate/child meeting original true signed m>1/5 must be
disjoint from original 49 windows, original 96 positive cells, and
the original signed core [13,16].

Compute all actual three physical SI10 supported sine, xcos, and sinh
Fourier means plus complete 3x3 outward Loewner fee via SM53
pair_cell. Select only new cells with strictly positive *full 3x3
error-paid POLE-diagonal* gain, not raw pole scalar scores.
Sort deterministically by that gain, and assess every nested prefix
by the exact full 3x3 Schur margin after the entire Loewner fee.
Keep the prefix that gives the best strictly certified margin.
No floating optimization may influence exact source selection.

A negative effective Schur of this LOWER matrix is inconclusive for
the actual original odd operator's signed index, complete 25/470,
even, Weil, CC27, RH.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_sm43_positive_cell_envelope import ROOT,original_source_centered_windows,ceil_rat,floor_rat
from validate_rpb108_sm44_physical_fourier_cell_gram import quantize
from validate_rpb108_sm12_positive_reference_33 import CENTERS as OLD_C,RADIUS as OLD_R
from validate_rpb108_sm49_adaptive_positive_jensen import original_adaptive_candidate_cells
from validate_rpb108_sm52_original_coupled_sin_xcos import signed_m_lower
from validate_rpb108_sm53_original_3source_pole import pair_source,pair_cell
from validate_rpb108_sm54_original_pole_adaptive_Jensen import (
    discover_new_real_positive,det3,schur_exact
)
N=3
STEP=F(1,32)
CHILDREN=8
END=F(13)
TOTAL_COARSE=416
DEN=10**12

def up(x):return ceil_rat(x,DEN)
def down(x):return floor_rat(x,DEN)

def baseline():
    d=json.loads((ROOT/"certificates/rpb108_sm54_96_window_3source_signed.json").read_text())
    assert d["run_id"]==39212101376
    assert d["source_indices"]==[2,17,24]
    assert d["physical_center"]=="1845/128" and d["original_chosen_cells"]==96
    M=[[F(q) for q in row] for row in d["complete_signed_original_3source_LOEWNER_lower"]]
    assert len(M)==3 and all(len(row)==3 for row in M)
    assert all(M[i][j]==M[j][i] for i in range(N) for j in range(N))
    S,_,p=schur_exact(M)
    assert S==F(d["schur_exact"]) and S<0 and p>0
    return M,S

def all_prohibited_positive(centers,sources):
    old,_,_,_=original_adaptive_candidate_cells(centers,sources)
    assert len(old)==32
    bands=[(c-OLD_R,c+OLD_R) for c in OLD_C]
    bands.extend((w["a"],w["b"]) for w in old)
    bands.sort()
    assert len(bands)==49 and all(bands[i][1]<=bands[i+1][0] for i in range(48))
    all_pole_positive,coarse_stats=discover_new_real_positive(centers,sources)
    assert len(all_pole_positive)==243
    top96=all_pole_positive[:96]
    # Source evidence from original SM54 passing first-96 run.
    covered=[(q[1],q[2]) for q in top96]
    assert len(set(covered))==96
    assert all(all(b<=l or a>=r for l,r in bands) for a,b in covered)
    prohibited=bands+covered
    return all_pole_positive,covered,prohibited,coarse_stats

def candidates(centers,sources,indices):
    coarse,credited,prohibited,prior=all_prohibited_positive(centers,sources)
    passed={(q[1],q[2]):q for q in coarse}
    credited_set=set(credited)
    accepted=[]
    refined_scanned=0
    refined_positive=0
    refined_feepositive=0
    old_cells_excluded=0
    whole_real_signed_rejected=0
    cutoff_by_full_3error=0
    coarse_unused=0
    physical_source_second_improvements=0
    def disjoint(l,r):
        return all(r<=a or l>=b for a,b in prohibited)
    def test(l,r,level):
        nonlocal refined_positive,refined_feepositive,old_cells_excluded
        nonlocal whole_real_signed_rejected,cutoff_by_full_3error
        nonlocal physical_source_second_improvements
        if not disjoint(l,r):
            old_cells_excluded+=1
            return
        assert 0<=l<r<=END and r<=F(13)
        mlo=signed_m_lower(l,r)
        if mlo<=F(1,5):
            whole_real_signed_rejected+=1
            return
        if level=="refined":refined_positive+=1
        delta=down(mlo)
        assert delta>F(1,5) and delta<=mlo
        v,_aff,_epsA,epsMean,curvature=pair_cell(centers,sources,indices,l,r)
        physical_source_second_improvements+=curvature
        coef=2*(r-l)*delta
        fullfee=up(coef*epsMean)
        netpole=coef*v[2]**2-fullfee
        # Source-driven stop: a cell unable to improve pole diagonal
        # after the ENTIRE 3x3 Loewner fee is not selected.
        if netpole<=0:
            cutoff_by_full_3error+=1
            return
        if level=="refined":refined_feepositive+=1
        accepted.append((netpole,l,r,coef,fullfee,v,level))
    for k in range(TOTAL_COARSE):
        l=k*STEP;r=(k+1)*STEP
        assert (r-l)==STEP
        if (l,r) in credited_set:
            continue
        if (l,r) in passed:
            coarse_unused+=1
            test(l,r,"coarse")
        else:
            for j in range(CHILDREN):
                a=l+STEP*F(j,CHILDREN)
                b=l+STEP*F(j+1,CHILDREN)
                refined_scanned+=1
                test(a,b,"refined")
    assert len(credited_set)==96
    assert coarse_unused==len(coarse)-96
    assert refined_scanned==(TOTAL_COARSE-len(coarse))*CHILDREN
    assert accepted and refined_positive>0
    accepted.sort(key=lambda x:(-x[0],x[1]))
    intervals=sorted((a,b) for net,a,b,*_ in accepted)
    assert all(intervals[i][1]<=intervals[i+1][0] for i in range(len(intervals)-1))
    assert all(disjoint(a,b) for a,b in intervals)
    stats={
      "original_coarse_real_frequency_cells":TOTAL_COARSE,
      "whole_original_positive_coarse_cells":len(coarse),
      "old_original_SM54_positive_coarse_cells_already_credited":96,
      "old_coarse_signed_positive_but_not_credited":coarse_unused,
      "refinement_factor_on_old_coarse_rejections":CHILDREN,
      "new_exact_real_signed_refined_cells_examined":refined_scanned,
      "new_refined_true_real_signed_positive_cells":refined_positive,
      "new_refined_full_3x3_error_paid_pole_gain_positive_cells":refined_feepositive,
      "all_new_full_3x3_positive_pole_net_candidates":len(accepted),
      "old_already_credited_cells_and_windows_excluded":old_cells_excluded,
      "new_signed_m_lower_nonpositive_cells_excluded":whole_real_signed_rejected,
      "new_signed_positive_full_3x3_error_nonpositive_candidates_excluded":cutoff_by_full_3error,
      "original_physical_local_second_derivative_improvements":physical_source_second_improvements,
    }
    return accepted,stats

def exact_best_prefix(base,S0,rows):
    """All prefix Schur comparisons exact fractions on bona fide 3x3 LOWERS.

    For each original sign-positive, disjoint cell
      A_j=coef v_j v_j^T - up(coef epsMean) I3 <= true new contribution.
    The cumulative prefix is a full original signed 3D Loewner LOWER
    since old inherited frequencies/pole remain in passing base.
    """
    current=[[base[i][j] for j in range(N)] for i in range(N)]
    best=[[x for x in row] for row in current]
    bestS=S0;bestcount=0
    Schur_samples=[]
    for n,(net,l,r,coef,fee,v,level) in enumerate(rows,1):
        for i in range(N):
            for j in range(N):
                current[i][j]+=coef*v[i]*v[j]-(fee if i==j else F(0))
        assert all(current[i][j]==current[j][i] for i in range(N) for j in range(N))
        schur,_,minor=schur_exact(current)
        if schur>bestS:
            bestS=schur
            bestcount=n
            best=[[x for x in row] for row in current]
        if n in (1,16,32,64,96,128,192,256,384,512,768,len(rows)):
            Schur_samples.append([n,str(down(schur))])
    assert bestcount>0 and bestS>S0
    # Verify full Sylvester and Schur identity on exact best lower.
    d1=best[0][0]
    d2=d1*best[1][1]-best[0][1]**2
    d3=det3(best)
    assert d1>0 and d2>0 and d3==d2*bestS
    pd=d3>0
    full_error_paid_pole_gain=best[2][2]-base[2][2]
    assert full_error_paid_pole_gain>0
    return best,bestS,bestcount,(d1,d2,d3),Schur_samples

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="artifacts/sm55_original_hierarchical_signed_pole_3source.json")
    args=ap.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==m["objective"]["status"]=="open"
    assert m["governance"]["no_automatic_promotion"]
    assert all(k in odd["evidence"] for k in ("SM53","SM54","SM55"))
    centers,sources,_=original_source_centered_windows()
    inds,c=pair_source(centers,sources)
    assert tuple(inds)==(2,17,24) and c==F(1845,128)
    L0,S0=baseline()
    rows,stats=candidates(centers,sources,inds)
    L1,S1,n,principal,samples=exact_best_prefix(L0,S0,rows)
    # For compact, still exact: each selected coef, midpoint component
    # and paid fee has denominators <= quantized rational source mesh.
    out={
      "status":"CERTIFIED_SCOPED_ORIGINAL_SIGNED_3SOURCE_HIERARCHICAL_POLE_SCHUR_LOWER",
      "canonical_W_ODD_NEG":"OPEN",
      "source_indices":[2,17,24],
      "physical_center":"1845/128",
      "signed_core_original":"[13,16] inherited and unchanged",
      "original_full_negative_and_exceptional_pole":"fully charged by inherited SM54 96-window source certificate",
      "original_precredited_SM12_SM49_windows":49,
      **stats,
      "new_full_3x3_error_paid_candidates_best_prefix_count":n,
      "new_full_3x3_error_paid_candidates_total_count":len(rows),
      "full_pole_schur_sign_classification":"strict positive only when all three exact Sylvester minors positive",
      "old_original_complete_signed_3x3_Loewner_effective_pole_margin":str(S0),
      "new_original_complete_signed_3x3_Loewner_effective_pole_margin":str(down(S1)),
      "rigorously_increased_complete_3x3_effective_pole_margin":S1>S0,
      "exact_signed_pole_schur_strict_margin_improvement":str(down(S1-S0)),
      "exact_original_three_source_signed_LOEWNER_lower_matrix":[
          [str(x) for x in row] for row in L1],
      "exact_new_lower_3x3_leading_principal_minors":[str(x) for x in principal],
      "source_three_dimensional_original_signed_positive_definite_certified":principal[2]>0,
      "schur_selected_prefix_scan":[[t,v] for t,v in samples],
      "complete_original_25source_odd_inertia_certified":False,
      "complete_original_470_source_Astar_O1O2_even_Weil_CC27_RH":False,
      "independent_original_fourier_closed_form_domain_audit":"OPEN",
      "interpretation":"Fully original signed 3source matrix, with previous physical pole and all negative spectrum paid. Added only rigorously signed positive real frequency cells outside all earlier ones; each full3x3 source mean penalty outward, exact best Schur prefix. Negative LOWER margin is inconclusive for true original odd negative index."
    }
    path=ROOT/args.output
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("SM55 full original three-source hierarchical signed pole Schur:",json.dumps({
       "refined_scanned":stats["new_exact_real_signed_refined_cells_examined"],
       "refined_signed_positive":stats["new_refined_true_real_signed_positive_cells"],
       "candidate_full_error_paid":len(rows),
       "selected_best_prefix":n,
       "old_schur":float(S0),
       "new_schur":float(S1),
       "full3source_pd":principal[2]>0,
       "whole_original_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
