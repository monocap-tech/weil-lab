#!/usr/bin/env python3
"""SM54: original TRUE SIGNED odd three-source pole-adaptive disjoint rescue.

Take certified SM53 full original odd signed 3x3 lower from PASSING
GitHub Actions 39208056922. It ALREADY pays every negative frequency,
signed core [13,16], and actual exceptional rank-one sinh pole.

Discover additional *previously UNCOUNTED* whole-real original
signed-positive windows on [0,13), each rigorously m_original(xi)>delta
via original SI06 seven-prime+SM39 arch/SM40 curvature. Exclude
every earlier 17 SM12 + 32 SM49 accepted source-positive interval.
Those nonoverlapping windows were not POSITIVELY credited in
SM53's full signed lower. Its exterior negative upper may still
pay a conservative nonnegative weight w on a cell: adding a true
positive delta source Jensen lower is valid because the NEW local
signed reference delta-w <= delta <= original m, with w>=0.
No original signed cell or exceptional pole is counted twice.

Select up to 96 cells based on rigorous TRUE sinh-pole source
Jensen contribution, but certify FULL 3x3 original sin/xcos/sinh
Fourier mean and all cross through SM53 pair_cell. Construct
  L54 = L53 + sum 2h delta vv^T - eps_full I,
where eps_full is full original 3x3 mean-square Loewner error,
outward exact rational. Thus L54 <= true ORIGINAL signed Wodd
on precisely the same actual 3D supported trial carrier.
Full Schur pole margin, Sylvester minors exact. A nonpositive
LOWER minor is INCONCLUSIVE about the actual negative index.
"""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    pole_sin,hyperbolic_interval,original_full_25_physical_interval_gram)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,ceil_rat,floor_rat)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    quantize,original_full_second_derivative_upper)
from validate_rpb108_sm12_positive_reference_33 import (
    CENTERS as SM12_CENTERS,RADIUS as SM12_RADIUS)
from validate_rpb108_sm49_adaptive_positive_jensen import (
    original_adaptive_candidate_cells)
from validate_rpb108_sm52_original_coupled_sin_xcos import signed_m_lower
from validate_rpb108_sm53_original_3source_pole import (
    pair_source,pair_cell)

DEN=10**12
N=3
WIDTH=F(1,32)
END=F(13)
MAX_EXTRA=96
def up(x):return ceil_rat(x,DEN)
def down(x):return floor_rat(x,DEN)

def original_pinned_sm53():
    d=json.loads((ROOT/"certificates/rpb108_sm53_true_original_signed_3source.json").read_text())
    assert d["source_run_id"]==39208056922
    assert d["original_source_indices"]==[2,17,24]
    assert d["center"]=="1845/128"
    assert d["core"]==["13","16"]
    A=[[F(x) for x in row] for row in d["matrix"]]
    assert len(A)==N and all(len(row)==N for row in A)
    assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
    d2=A[0][0]*A[1][1]-A[0][1]**2
    det=det3(A)
    assert d2==F(d["original_first_two_principal_minor"])
    assert det==F(d["original_full_determinant"])
    assert A[0][0]>0 and d2>0 and det<0
    return A

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def schur_exact(L):
    a=L[0][0];b=L[0][1];c=L[1][1]
    d=a*c-b*b
    assert a>0 and d>0
    p=L[0][2];q=L[1][2]
    compensation=(c*p*p-2*b*p*q+a*q*q)/d
    return L[2][2]-compensation,compensation,d

def discover_new_real_positive(centers,sources):
    selected_49,_available,_rejected,_center=original_adaptive_candidate_cells(
       centers,sources)
    assert len(selected_49)==32
    pre=[(c-SM12_RADIUS,c+SM12_RADIUS) for c in SM12_CENTERS]
    pre.extend((x["a"],x["b"]) for x in selected_49)
    pre.sort()
    assert len(pre)==49
    assert all(pre[i][1]<=pre[i+1][0] for i in range(48))
    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    K=original_full_second_derivative_upper(sources)[24]
    candidates=[];signed_positive=0;overlap_rejected=0;nonpositive=0
    for i in range(int(END/WIDTH)):
        left=i*WIDTH;right=(i+1)*WIDTH
        assert F(0)<=left<right<=END
        if any(not(right<=a or left>=b) for a,b in pre):
            overlap_rejected+=1
            continue
        mlo=signed_m_lower(left,right)
        if mlo<=F(1,5):
            nonpositive+=1;continue
        signed_positive+=1
        delta=down(mlo)
        assert delta>F(1,5) and delta<=mlo
        mid=(left+right)/2
        actual=pole_sin(mid,sh,ch)
        v=quantize(actual.mid())
        radius=ceil_rat(max(abs(actual.l-v),abs(actual.h-v)),10**9)
        freqhalf=WIDTH/2
        er=radius+K*freqhalf*freqhalf/6
        lower=2*WIDTH*delta*max(F(0),abs(v)-er)**2
        if lower>0:
            candidates.append((lower,left,right,delta))
    assert len(candidates)>0
    candidates.sort(key=lambda v:(-v[0],v[1]))
    chosen=candidates[:MAX_EXTRA]
    assert len(chosen)>0
    cells=sorted((x[1],x[2]) for x in chosen)
    assert all(cells[i][1]<=cells[i+1][0] for i in range(len(cells)-1))
    assert all(b<=END and a>=0 for a,b in cells)
    assert all(all(b<=p or a>=q for p,q in pre) for a,b in cells)
    return chosen,{
        "whole_real_scan_cells":int(END/WIDTH),
        "old_49_positive_window_overlapping_cells_discarded":overlap_rejected,
        "nonpositive_signed_lower_cells_discarded":nonpositive,
        "whole_real_strict_m_positive_new_candidate_cells":signed_positive,
        "true_pole_source_positive_score_cells":len(candidates)
    }

def compute():
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in manifest["obligations"] if x["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==manifest["objective"]["status"]=="open"
    assert all(z in odd["evidence"] for z in ("SM52C","SM53","SM54"))
    centers,sources,_=original_source_centered_windows()
    indices,c=pair_source(centers,sources)
    assert indices==(2,17,24) and c==F(1845,128)
    physical,src,_=original_full_25_physical_interval_gram()
    assert src==sources and len(src)==25
    previous=original_pinned_sm53()
    chosen,stats=discover_new_real_positive(centers,sources)
    P=[[F(0)]*N for _ in range(N)];eps=F(0);strict_derivative=0
    pole_conservative=F(0)
    for score,l,r,delta in chosen:
        assert r<=F(13) and l>=F(0)
        assert signed_m_lower(l,r)>=delta>0
        v,_aff,_eaff,emean,improved=pair_cell(
           centers,sources,indices,l,r)
        strict_derivative+=improved
        coef=2*(r-l)*delta
        for i in range(N):
            for j in range(N):P[i][j]+=coef*v[i]*v[j]
        eps+=coef*emean
        pole_conservative+=score
    eps_full=up(eps)
    # Full three-dimensional Loewner error is paid on ALL directions.
    shifted=[[previous[i][j]+P[i][j]-(eps_full if i==j else F(0))
              for j in range(N)] for i in range(N)]
    assert all(shifted[i][j]==shifted[j][i] for i in range(N) for j in range(N))
    # Convert huge inner rational coefficients into compact export
    # while retaining the original Loewner lower via row-norm fee.
    q=[[quantize(shifted[i][j]) for j in range(N)] for i in range(N)]
    exportfee=up(max(sum(abs(shifted[i][j]-q[i][j])
                         for j in range(N)) for i in range(N)))
    L=[[q[i][j]-(exportfee if i==j else F(0))
        for j in range(N)] for i in range(N)]
    assert all(L[i][j]==L[j][i] for i in range(N) for j in range(N))
    old_schur,old_comp,old_minor=schur_exact(previous)
    d1=L[0][0]
    d2=d1*L[1][1]-L[0][1]**2
    d3=det3(L)
    positive_block=(d1>0 and d2>0)
    schur=None;comp=None
    if positive_block:
        schur,comp,_=schur_exact(L)
        assert d3==d2*schur
    positive_pd=positive_block and d3>0
    # One full 3D matrix lower, not isolated scalar source gain.
    pole_gain=L[2][2]-previous[2][2]
    assert pole_gain>0,("Added true signed original positivity failed to improve pole diagonal",float(pole_gain))
    result={
        "status":"CERTIFIED_SCOPED_ORIGINAL_3SOURCE_POLE_ADAPTIVE_POSITIVE_JENSEN_LOWER",
        "original_W_ODD_NEG":"OPEN",
        "original_input_source_indices":list(indices),
        "original_3source_current_core":["13","16"],
        **stats,
        "new_selected_real_positive_outside_old_core_and_all_old_positive_bands":len(chosen),
        "new_all_original_source_cross_included":True,
        "new_full_3x3_positive_mean_error_up":str(eps_full),
        "new_3x3_complete_export_outward_row_error":str(exportfee),
        "new_original_pole_source_scalar_Jensen_gain_scores_lower":str(down(pole_conservative)),
        "old_original_3x3_pole_source_Loewner_lower":str(previous[2][2]),
        "new_original_3x3_pole_source_Loewner_lower":str(L[2][2]),
        "new_3x3_pole_diagonal_improvement_lower":str(down(pole_gain)),
        "original_3x3_unchanged_reference_LOEWNER_lower": [
          [str(x) for x in row] for row in previous],
        "new_complete_original_3x3_true_signed_LOEWNER_lower": [
          [str(x) for x in row] for row in L],
        "old_original_true_signed_lower_effective_pole_Schur_margin":str(old_schur),
        "new_original_true_signed_lower_effective_pole_Schur_margin":str(schur) if schur is not None else None,
        "original_new_3source_signed_leading_principal_minors":[
            str(d1),str(d2),str(d3)],
        "full_original_3source_positive_definite_certified":bool(positive_pd),
        "entire_original_25_odd_source_PSD_negative_index_certified":False,
        "complete_original_470_source_residual_O1O2_even_Weil_CC27_RH_certified":False,
        "independent_original_form_domain_audit":"OPEN",
        "interpretation":"Added new real sign-positive original Fourier windows to already certified complete signed original 3source lower, disjoint from all previously credited regions. Full cross and outward error paid; sign of lower's Schur margin is NOT actual negative eigenvalue proof."
    }
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default="artifacts/sm54_original_signed_pole_adaptive_3source.json")
    a=parser.parse_args()
    d=compute()
    dest=ROOT/a.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(d,indent=2)+"\n")
    print("SM54 true original three-source pole adaptive positive:",json.dumps({
        "selected":d["new_selected_real_positive_outside_old_core_and_all_old_positive_bands"],
        "pole_old":d["old_original_3x3_pole_source_Loewner_lower"],
        "pole_new":d["new_original_3x3_pole_source_Loewner_lower"],
        "pole_gain":d["new_3x3_pole_diagonal_improvement_lower"],
        "schur_old":d["old_original_true_signed_lower_effective_pole_Schur_margin"],
        "schur_new":d["new_original_true_signed_lower_effective_pole_Schur_margin"],
        "full_3source_pd":d["full_original_3source_positive_definite_certified"],
        "original_full_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
