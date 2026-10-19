#!/usr/bin/env python3
"""SM56: exact source-anisotropic original signed three-source Jensen error.

SM55 passed a complete original odd signed 3x3 LOEWNER LOWER on genuine
physically supported sin2/xcos17/sinh-pole24, with whole negative
frequency cover and actual exceptional pole already paid. Its 242
selected new positive signed whole-real intervals were certified using
a single scalar mean error epsilon*I_3 for each positive Jensen window.
This overcharges a source whose local original Fourier mean error is
small, especially the actual sinh pole direction.

For any true real mean Fourier source vector u on a new disjoint
whole-real signed-positive interval I, original SM53 interval formulas
rigorously establish |u_i-v_i|<=r_i. Thus with
   d_ij=|v_i|r_j+|v_j|r_i+r_i*r_j,
every entry of E=uu^T-vv^T satisfies |E_ij|<=d_ij. Exact
Cauchy/Young or Gershgorin implies, for all real z:
   z^T E z >= -sum_i (sum_j d_ij) z_i^2.
Consequently
   gamma*u*u^T >= gamma*v*v^T
                       -diag(gamma*sum_j d_ij)_i,
with individual fees outward-rounded UP to 1e-12.

Both this anisotropic matrix and the old scalar-error matrix are
independently valid complete 3x3 Loewner LOWERS, retaining all cross.
We replay the SM55 original 242-window prefix exactly, verifying
its matrix against the GitHub Actions artifact. Then compute scalar,
anisotropic and per-window greedy better-exact-Schur choices on the
SAME 242 disjoint true signed positive cells. Any chosen option is
a separately valid full original odd signed lower; comparing exact
Schur margins cannot introduce a false mathematical certificate.

A negative Schur of the LOWER proves no actual original negative
index or RH conclusion. Original 25 source/470 inverse/orthogonal
remainder, complete W-ODD-NEG O1/O2/even/Weil/CC27/RH remain OPEN.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,ceil_rat,floor_rat)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    quantize,original_full_second_derivative_upper)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_F3,original_third_spatial_moment)
from validate_rpb108_sm53_original_3source_pole import (
    B,PI,I,F0,F1,F2,pole_sin,pole_xcos,hyperbolic_interval,
    pair_source,pair_cell)
from validate_rpb108_sm54_original_pole_adaptive_Jensen import (
    det3,schur_exact)
from validate_rpb108_sm55_hierarchical_signed_pole import (
    baseline,candidates,exact_best_prefix)

N=3
DEN=10**12

def up(x):return ceil_rat(x,DEN)
def down(x):return floor_rat(x,DEN)

def initial_and_pinned():
    d=json.loads((ROOT/"certificates/rpb108_sm55_original_242prefix_3source_lower.json").read_text())
    assert d["source_actions_run_id"]==39265951866
    assert d["source_indices"]==[2,17,24]
    assert d["original_selected_real_positive_window_prefix"]==242
    M=[[F(x) for x in row] for row in d["original_old_true_full_3source_signed_lower_matrix"]]
    s,_,det2=schur_exact(M)
    floor=F(d["source_old_signed_lower_schur_down"])
    assert floor<=s<floor+F(1,DEN)
    return M,s

class MeanIntervals:
    """True original supported physical Fourier mean enclosures per source.

    Recompute the exact original SI10/SM42 signed Fourier cell value and
    second frequency derivatives. The linear frequency Taylor term
    cancels in the symmetric mean. Do not substitute point samples.
    """
    def __init__(self,centers,sources,indices):
        self.centers=centers;self.sources=sources;self.indices=indices
        self.center=centers[sources[2][1]]
        self.globalK=original_full_second_derivative_upper(sources)
        self.M3=original_third_spatial_moment(sources)
        self.sh=hyperbolic_interval(B/2,"sinh")
        self.ch=hyperbolic_interval(B/2,"cosh")
        self.pi=I(PI[0],PI[1])
        assert indices==(2,17,24)
        assert self.center==F(1845,128)

    def source_radii(self,l,r,source_vector):
        mid=(l+r)/2;h=(r-l)/2;c=self.center;pi=self.pi
        radii=[]
        for n,k in enumerate(self.indices):
            if k==2:
                value=(F0(c-mid)-F0(c+mid))/2
                second=2*pi*pi*(F2(c+mid)-F2(c-mid))
            elif k==17:
                value=(F1(mid+c)+F1(mid-c))/2
                second=-2*pi*pi*(original_F3(mid+c)+original_F3(mid-c))
            elif k==24:
                value=pole_sin(mid,self.sh,self.ch)
                second=None
            else:
                raise AssertionError("unexpected original physical source")
            v=quantize(value.mid())
            assert v==source_vector[n],("Physical Fourier midpoint disagrees with inherited SM53",n)
            ev=ceil_rat(max(abs(value.l-v),abs(value.h-v)),10**9)
            global_k=self.globalK[k]
            local_k=global_k if second is None else min(
                global_k,max(abs(second.l),abs(second.h))+self.M3[k]*h)
            assert F(0)<=local_k<=global_k
            radius=ev+local_k*h*h/6
            assert radius>=0
            radii.append(radius)
        return radii

def fees_for_cell(full_coef,v,radii):
    assert full_coef>0 and len(v)==len(radii)==N
    assert all(r>=0 for r in radii)
    # For all real true u with componentwise |u-v|<=r,
    # the symmetric error matrix has exact entry bound
    # d_ij=|vi|rj+|vj|ri+ri*rj.
    differences=[[abs(v[i])*radii[j]+abs(v[j])*radii[i]
                   +radii[i]*radii[j] for j in range(N)]
                 for i in range(N)]
    assert all(differences[i][j]==differences[j][i]
               for i in range(N) for j in range(N))
    row=[sum(differences[i],F(0)) for i in range(N)]
    fee=[up(full_coef*x) for x in row]
    assert all(x>=0 for x in fee)
    return fee,row

def add(original,coef,v,fees):
    result=[[original[i][j]+coef*v[i]*v[j]-
             (fees[i] if i==j else F(0))
             for j in range(N)] for i in range(N)]
    assert all(result[i][j]==result[j][i]
               for i in range(N) for j in range(N))
    return result

def validated_schur(matrix):
    a=matrix[0][0]
    minor=a*matrix[1][1]-matrix[0][1]**2
    if not(a>0 and minor>0):return None
    s,_,det2=schur_exact(matrix)
    assert det2==minor
    assert det3(matrix)==minor*s
    return s

def calculate():
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in manifest["obligations"] if o["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]==odd["status"]=="open"
    assert manifest["governance"]["no_automatic_promotion"]
    assert all(k in odd["evidence"] for k in ("SM53","SM54","SM55","SM56"))
    centers,sources,_=original_source_centered_windows()
    indices,center=pair_source(centers,sources)
    assert tuple(indices)==(2,17,24) and center==F(1845,128)
    base,s0=baseline()
    rows,prior=candidates(centers,sources,indices)
    scalar_sm55,orig_s55,prefix,_,_=exact_best_prefix(base,s0,rows)
    artifact_matrix,artifact_s55=initial_and_pinned()
    assert prefix==242 and len(rows)==288
    assert scalar_sm55==artifact_matrix and orig_s55==artifact_s55,(
       "Replayed source does not exactly reproduce original passing SM55 Actions certificate")
    means=MeanIntervals(centers,sources,indices)
    scalar=base;anisotropic=base;adaptive=base
    decisions={"componentwise":0,"scalar":0}
    anisotropic_pole_fee_improved=0
    anisotropic_pole_fee_worsened=0
    selected_pole_error_scalar=F(0)
    selected_pole_error_aniso=F(0)
    per_cell_anisotropic_pole_lower_gain=F(0)
    source_means_checked=0
    records=[]
    for j,(net,l,r,coef,scalar_fee,v,level) in enumerate(rows[:prefix],1):
        reconstructed_v,_,_,epsMean,_=pair_cell(centers,sources,indices,l,r)
        assert reconstructed_v==v
        assert scalar_fee==up(coef*epsMean)
        radii=means.source_radii(l,r,v)
        aniso_fee,rowfees=fees_for_cell(coef,v,radii)
        source_means_checked+=1
        selected_pole_error_scalar+=scalar_fee
        selected_pole_error_aniso+=aniso_fee[2]
        per_cell_anisotropic_pole_lower_gain+=coef*v[2]**2-aniso_fee[2]
        anisotropic_pole_fee_improved+=int(aniso_fee[2]<scalar_fee)
        anisotropic_pole_fee_worsened+=int(aniso_fee[2]>scalar_fee)
        scalar=add(scalar,coef,v,[scalar_fee]*N)
        anisotropic=add(anisotropic,coef,v,aniso_fee)
        # Both alternatives are complete, rigorously original
        # signed Loewner LOWER increments: choose purely by exact
        # Schur margin. One candidate is never added twice.
        trial_scalar=add(adaptive,coef,v,[scalar_fee]*N)
        trial_aniso=add(adaptive,coef,v,aniso_fee)
        s_a=validated_schur(trial_scalar)
        s_b=validated_schur(trial_aniso)
        assert s_a is not None or s_b is not None
        if s_b is not None and (s_a is None or s_b>s_a):
            adaptive=trial_aniso
            decisions["componentwise"]+=1
        else:
            adaptive=trial_scalar
            decisions["scalar"]+=1
        if j in (1,32,64,96,128,160,192,224,prefix):
            records.append({"prefix":j,
              "scalar_schur":str(down(validated_schur(scalar))),
              "anisotropic_schur":str(down(validated_schur(anisotropic))),
              "adaptive_schur":str(down(validated_schur(adaptive)))})
    assert scalar==artifact_matrix
    score_scalar=validated_schur(scalar)
    score_aniso=validated_schur(anisotropic)
    score_adapt=validated_schur(adaptive)
    assert score_scalar==artifact_s55
    assert source_means_checked==prefix
    candidate_scores=[("SM55 scalar",score_scalar,scalar)]
    if score_aniso is not None:candidate_scores.append(("anisotropic",score_aniso,anisotropic))
    if score_adapt is not None:candidate_scores.append(("error-type adaptive",score_adapt,adaptive))
    method,newscore,best=max(candidate_scores,key=lambda a:a[1])
    strict_gain=(newscore>score_scalar)
    assert newscore>=score_scalar
    original_minor=best[0][0]*best[1][1]-best[0][1]**2
    determinant=det3(best)
    assert original_minor>0 and determinant==original_minor*newscore
    out={
      "status":"CERTIFIED_ORIGINAL_SCOPED_THREE_SOURCE_ANISOTROPIC_LOEWNER_ERROR_SCHUR_AUDIT",
      "original_W_ODD_NEG":"OPEN",
      "source_indices":[2,17,24],
      "original_center":"1845/128",
      "replayed_SM55_Actions_id":39265951866,
      "exact_complete_original_SM55_signed_lower_replayed":True,
      "new_genuine_positive_real_cells_reenclosed":source_means_checked,
      "complete_original_3x3_1source_mean_cross_checked":True,
      "whole_real_signpositive_and_disjointness_inherited_and_rechecked_by_SM55_candidates":True,
      "scalar_signed_pole_schur_exact":str(score_scalar),
      "componentwise_signed_pole_schur_exact":str(score_aniso) if score_aniso is not None else None,
      "per_cell_exact_choice_signed_pole_schur_exact":str(score_adapt) if score_adapt is not None else None,
      "best_certified_schur_strategy":method,
      "strict_original_signed_complete_3x3_schur_improvement_over_SM55":strict_gain,
      "new_best_original_complete_3x3_schur_exact":str(newscore),
      "new_best_original_complete_3x3_schur_improvement":str(down(newscore-score_scalar)),
      "number_source_means_with_smaller_pole_component_fee_than_scalar":anisotropic_pole_fee_improved,
      "number_source_means_with_larger_pole_component_fee_than_scalar":anisotropic_pole_fee_worsened,
      "total_scalar_pole_error_paid":str(selected_pole_error_scalar),
      "total_anisotropic_pole_error_paid":str(selected_pole_error_aniso),
      "number_error_lower_certificates_selected":{"anisotropic":decisions["componentwise"],"scalar":decisions["scalar"]},
      "prefix_certified_schur_audit":records,
      "best_true_original_3x3_signed_LOEWNER_lower":[[str(x) for x in row] for row in best],
      "best_true_original_3x3_signed_LOEWNER_leading_minors":[
           str(best[0][0]),str(original_minor),str(determinant)],
      "strict_original_3source_positive_definite_certified":determinant>0,
      # Inertia comparison is valid on the SAME THREE-SOURCE
      # physical trial space: W_actual >= L_best, the leading
      # 2x2 L block is PD. The LDL Schur third pivot is det/minor2.
      # Thus L_best has at most one negative direction, and the
      # actual signed W restricted to this 3D span has negative
      # index at most one by the min-max/inertia monotonicity
      # theorem. This DOES NOT classify the full odd operator!
      "certified_actual_original_signed_3source_negative_index_upper_bound":
            0 if determinant>=0 else 1,
      "certified_actual_original_signed_3source_negative_index_exactly_one":False,
      "certified_complete_original_odd_operator_negative_index_upper_bound":None,
      "entire_25source_odd_index_and_strong_residual_closed":False,
      "original_470source_Astar_inverse_O1O2_even_Weil_CC27_RH":False,
      "independent_original_physical_Fourier_domain_audit":"OPEN",
      "proof_scope":"Every per-cell componentwise or scalar Loewner lower valid on original physically supported three-source signed odd form; actual original odd complete-spectrum negative region and sinh rankone already paid in unchanged SM55 base. Lower negative determinant is not true negativity."
    }
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm56_original_anisotropic_signed_pole_3source.json")
    args=p.parse_args()
    out=calculate()
    target=ROOT/args.output;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+"\n")
    print("SM56 original signed three-source componentwise full-matrix Loewner correction:",json.dumps({
        "source_replayed":out["exact_complete_original_SM55_signed_lower_replayed"],
        "source_means_checked":out["new_genuine_positive_real_cells_reenclosed"],
        "scalar_schur":float(F(out["scalar_signed_pole_schur_exact"])),
        "componentwise_schur":float(F(out["componentwise_signed_pole_schur_exact"])) if out["componentwise_signed_pole_schur_exact"] else None,
        "adapted_schur":float(F(out["per_cell_exact_choice_signed_pole_schur_exact"])) if out["per_cell_exact_choice_signed_pole_schur_exact"] else None,
        "best_schur":float(F(out["new_best_original_complete_3x3_schur_exact"])),
        "strategy":out["best_certified_schur_strategy"],
        "strict_schur_gain":out["strict_original_signed_complete_3x3_schur_improvement_over_SM55"],
        "true_3source_PD":out["strict_original_3source_positive_definite_certified"],
        "full_original_Wodd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
