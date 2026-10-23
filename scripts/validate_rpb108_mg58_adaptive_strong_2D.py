#!/usr/bin/env python3
"""MG58 — targeted original 24D corrected-action strong-moment positive-subspace gate.

MG57's exact accepted original physical [0,4] action moment lower has
inertia (1 positive,23 negative). No second strictly positive subspace
can be obtained merely by reselecting vectors inside that SAME lower.

MG58 independently rebuilds ONLY original 5/8–7/8 high-error physical
Fourier frequencies, replacing two old 1/8-wide cells by either 4 or 8
genuine source/multiplier subcells each. Reuses the independently
verified 12 MG57 cells on [1/8,1/2] and the other unaffected true
original MG29 cells. The actual pole correction and all 24 source
components remain, with a VALID complete-frequency action-moment lower
S_* >= S_[0,4] >= L.

For each NEW lower, exact rational full24 LDL determines positive
index. When >=2, a floating eigensolver may propose integer 2-plane
candidates, but their acceptance is EXCLUSIVELY exact rational
2x2 positive definiteness and a rigorous rational Euclidean
coercivity lower, independently replayed on physical original matrices.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg25_robust_source_aware_residual import T
from validate_rpb108_mg41_ideal_cross_error_feasibility import classify_ideal
import validate_rpb108_mg32_joint_fourier_residual as mg32
import validate_rpb108_mg57_pole_coupled_targeted_cells as mg57
N=24;P=23
ORIGINAL_TEST_VECTOR=(-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2)
def rd(A):
    Z=[[Q(z) for z in row] for row in A]
    assert len(Z)==N and all(len(z)==N for z in Z)
    return Z
def encoded(A):return [[str(z) for z in row] for row in A]
def trace(A):return sum((A[i][i] for i in range(N)),Q(0))
def qform(v,A,w=None):
    if w is None:w=v
    return sum((Q(v[i])*A[i][j]*Q(w[j])
                for i in range(N) for j in range(N)),Q(0))
def original_base(a57):
    initial,*_=mg32.exact_original_cells()
    assert len(initial)==32 and initial[0][0]==0 and initial[-1][1]==4
    archived=a57["MG57_refined_true_physical_fourier_source_cells"]
    assert len(archived)==12
    new=[]
    for rec in archived:
        new.append((Q(rec["left"]),Q(rec["right"]),
                    Q(rec["multiplier_lower"]),Q(rec["multiplier_upper"]),
                    [Q(z) for z in rec["source_midpoint"]],
                    [Q(z) for z in rec["source_derivative"]],
                    [Q(z) for z in rec["source_error"]]))
    full=[]
    for i,c in enumerate(initial):
        if i in (1,2,3):
            full.extend(new[(i-1)*4:i*4])
        else:full.append(c)
    assert len(full)==41
    assert all(full[i][1]==full[i+1][0] for i in range(40))
    assert full[0][0]==0 and full[-1][1]==4
    return full
def exact_signed_index(A):
    assert A==T(A)
    M=[row[:] for row in A]
    signs=[];zero=[]
    for k in range(N):
        d=M[k][k]
        if d==0:
            zero.append(k)
            break
        signs.append(1 if d>0 else -1)
        for i in range(k+1,N):
            for j in range(i,N):
                M[i][j]-=M[i][k]*M[k][j]/d
                M[j][i]=M[i][j]
    assert not zero,("zero pivot requires alternative congruence",zero)
    assert len(signs)==N
    return sum(x>0 for x in signs),sum(x<0 for x in signs),signs
def two_dimensional_integer_plane(A):
    import numpy as np
    matrix=np.array([[float(z) for z in row] for row in A])
    eigen,vector=np.linalg.eigh(matrix)
    if not eigen[-2]>0:
        return None
    for factor in (24,48,96,192,384,768):
        u=[int(round(float(z)*factor)) for z in vector[:,-1]]
        v=[int(round(float(z)*factor)) for z in vector[:,-2]]
        if not any(u) or not any(v):continue
        q00=qform(u,A);q11=qform(v,A);q01=qform(u,A,v)
        delta=q00*q11-q01*q01
        if q00<=0 or q11<=0 or delta<=0:continue
        uu=sum(x*x for x in u);vv=sum(x*x for x in v)
        assert uu>0 and vv>0
        # A direct and rigorous coefficient Euclidean bound:
        # lambda_min(Q2)>=det(Q2)/tr(Q2), lambda_max(U^T U)
        # <=tr(U^T U)=||u||²+||v||². Therefore
        # w^T A w >= c ||w||² for EVERY w∈span(u,v).
        constant=delta/((q00+q11)*(uu+vv))
        assert constant>0
        return {"first_integer_vector":[str(x) for x in u],
            "second_integer_vector":[str(x) for x in v],
            "gram_00":str(q00),"gram_01":str(q01),"gram_11":str(q11),
            "gram_determinant":str(delta),
            "first_integer_coefficient_norm_squared":str(uu),
            "second_integer_coefficient_norm_squared":str(vv),
            "normalized_2D_strict_lower_bound":str(constant),
            "exact_2D_positive_definite":True,
            "bound_applies_only_to_span_NOT_whole24":True}
    return None
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg24-json",required=True)
    p.add_argument("--verified-mg57-json",required=True)
    p.add_argument("--output",default="artifacts/mg58_original_targeted_2D_strong_moment.json")
    opt=p.parse_args()
    a24=json.loads((ROOT/opt.verified_mg24_json).read_text())
    a57=json.loads((ROOT/opt.verified_mg57_json).read_text())
    assert a24["canonical_W_ODD_NEG"]==a57["canonical_W_ODD_NEG"]=="OPEN"
    assert a57["status"]=="ORIGINAL_MG57_LOCAL_PHYSICAL_MULTIPLIER_POLE_COUPLED_STRONG_LOWER"
    hm,hr,herr=original_H24_from_physical_source()
    assert herr==Q(a24["physical_Gram_Loewner_row_error"])
    bmid=[hm[i][P] for i in range(N)]
    brad=[hr[i][P] for i in range(N)]
    baseline=original_base(a57)
    L57,U57,counts,rows,cost,sig,err=mg57.accumulate(baseline,bmid,brad,coupling=True)
    assert encoded(L57)==a57["refined_original_true_strong_lower"]
    assert encoded(U57)==a57["refined_original_true_strong_upper"]
    assert (len(baseline),sum(x>0 for x in exact_signed_index(L57)[2]))==(41,1)
    assert qform(ORIGINAL_TEST_VECTOR,L57)>0
    old_target=sum(Q(r["trace_error_penalty"]) for r in rows
        if Q(5,8)<=Q(r["left"]) and Q(r["right"])<=Q(7,8))
    assert old_target>Q(20)
    prep=mg32.original_partition_preparation()
    glob4=mg32.original_fourth_global(prep[1])
    results=[]
    for n in (4,8):
        newcells=[]
        for k in (5,6):
            left=Q(k,8)
            for j in range(n):
                x=left+Q(j,8*n);y=left+Q(j+1,8*n)
                assert y-x==Q(1,8*n)
                newcells.append(mg57.original_refined_true_source_cell(
                    x,y,prep,glob4))
        rebuilt=[]
        for cell in baseline:
            l,r=cell[:2]
            if l==Q(5,8):rebuilt.extend(newcells[:n])
            elif l==Q(3,4):rebuilt.extend(newcells[n:])
            else:rebuilt.append(cell)
        assert len(rebuilt)==41+2*(n-1)
        assert rebuilt[0][0]==0 and rebuilt[-1][1]==4
        assert all(rebuilt[i][1]==rebuilt[i+1][0]
                   for i in range(len(rebuilt)-1))
        L,U,tau,records,budget,signal,error=mg57.accumulate(
            rebuilt,bmid,brad,coupling=True)
        pos,neg,signs=exact_signed_index(L)
        classification,witness=classify_ideal(L)
        assert classification in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                                  "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
        if classification=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
            v=[Q(x) for x in witness["rational_vector"]]
            assert qform(v,L)==Q(witness["exact_negative_quadratic"])<0
        new_target=sum(Q(r["trace_error_penalty"]) for r in records
            if Q(5,8)<=Q(r["left"]) and Q(r["right"])<=Q(7,8))
        assert new_target>=0
        plane=two_dimensional_integer_plane(L) if pos>=2 else None
        if pos>=2:assert plane is not None
        report={
            "new_subdivisions_per_original_cell":n,
            "actual_new_original_fourier_source_cell_count":len(newcells),
            "total_true_original_source_cell_count":len(rebuilt),
            "new_full24_original_corrected_action_lower":encoded(L),
            "new_full24_original_corrected_action_upper":encoded(U),
            "original_full24_conservative_LDL_inertia":{"positive":pos,"negative":neg},
            "new_original_24D_lower_exact_inertia":classification,
            "new_original_24D_lower_exact_negative_ray_or_positive_LDL":witness,
            "positive_original_source_coordinate_diagonals":sum(L[i][i]>0 for i in range(N)),
            "positive_original_two_dimensional_source_plane":plane,
            "genuine_2D_positive_action_moment_CERTIFIED":plane is not None,
            "full24_strong_action_coercivity_CERTIFIED":pos==24,
            "true_original_strong_action_lower_trace":str(trace(L)),
            "original_baseline_two_highest_loss_cells_Young_charge":str(old_target),
            "new_physical_original_subcells_Young_charge":str(new_target),
            "focused_absolute_Young_charge_reduction":str(old_target-new_target),
            "total_original_source_Young_error_charge":str(error),
            "total_original_source_affine_signal_trace":str(signal),
            "MG57_previous_positive_integer_ray_under_new_lower":str(
                qform(ORIGINAL_TEST_VECTOR,L)),
            "new_actual_physical_fourier_source_cells":[{
              "left":str(c[0]),"right":str(c[1]),
              "multiplier_lower":str(c[2]),"multiplier_upper":str(c[3]),
              "source_midpoint":[str(x) for x in c[4]],
              "source_derivative":[str(x) for x in c[5]],
              "source_error":[str(x) for x in c[6]]}
                for c in newcells],
            "all_original_cell_boundaries_contiguous":True,
            "whole_source_true_original_pole_correction":True,
            "no_inference_full24_from_trace_or_single_ray":True
        }
        print("MG58 original physical refined 24D source",{
            "n":n,"cells":len(rebuilt),"trace":float(trace(L)),
            "young_target_old":float(old_target),
            "young_target_new":float(new_target),
            "signed_lower_index":(pos,neg),
            "positive2D":plane is not None,
            "full24":pos==24},flush=True)
        results.append(report)
    chosen=max(results,key=lambda x:(
        x["original_full24_conservative_LDL_inertia"]["positive"],
        Q(x["true_original_strong_action_lower_trace"])))
    result={
        "status":"ORIGINAL_MG58_TRUE_FOURIER_ADAPTIVE_2D_STRONG_SUBSPACE",
        "canonical_W_ODD_NEG":"OPEN",
        "verified_original_parents":{"MG24":39378465438,"MG57":39897754515},
        "original_real_positive_source_frequency_coverage":["0","4"],
        "original_SI10_25_physical_23adapted_plus_true_sinh_pole":True,
        "true_original_signed_7prime_digamma_action":True,
        "whole_real_frequency_strong_moment_lower_from_PSD_remaining_action":True,
        "MG57_independently_accepted_baseline_replayed":True,
        "original_MG57_baseline_conservative_index":{"positive":1,"negative":23},
        "original_MG57_baseline_lower_trace":str(trace(L57)),
        "original_targeted_source_interval":["5/8","7/8"],
        "new_source_sampling_not_just_reweight_existing_matrix":True,
        "all_new_matrices_rational_original_physical_source_Loewner_uppers_and_lowers":True,
        "selected_refinement_n":chosen["new_subdivisions_per_original_cell"],
        "selected_conservative_positive_index":
            chosen["original_full24_conservative_LDL_inertia"]["positive"],
        "selected_strict_original_2D_action_subspace_CERTIFIED":
            chosen["genuine_2D_positive_action_moment_CERTIFIED"],
        "original_full24_strong_moment_coercivity":
            chosen["full24_strong_action_coercivity_CERTIFIED"],
        "original_source_residual_24D_contraction":False,
        "original_full470_inverse":False,
        "original_signed_odd_51over56":False,
        "independent_original_Fourier_form_domain_audit":"OPEN",
        "even_Weil_CC27_RH":"OPEN",
        "candidates":results
    }
    path=ROOT/opt.output;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+"\n")
    print("MG58 ORIGINAL true physical adaptive Fourier full24 accept-gate BUILT",{
        "selected_n":result["selected_refinement_n"],
        "selected_positive_index":result["selected_conservative_positive_index"],
        "actual_two_dimensional_source_positive":
            result["selected_strict_original_2D_action_subspace_CERTIFIED"],
        "full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
