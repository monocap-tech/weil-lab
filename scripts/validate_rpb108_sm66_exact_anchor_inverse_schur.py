#!/usr/bin/env python3
"""SM66: full EXACT positive-anchor inverse in true original 22D Schur.

SM65 source replay reconstructs actual true original signed source25
L62 <= Q <= U, with the independent SM63 original true-positive 3D
physical anchor A0 on indices 1,2,17, and 66 verified actual
anchor-to-22 physical source absolute cross bounds b_ij.

For every actual A=Q_PP >= A0 >0, inverse order gives
      A^-1 <= A0^-1
as quadratic forms. With exact rational 3x3 A0^-1 and full
66 b_ij, any z in the real 22-coordinate complement obeys
      z^T B^T A^-1 B z
       <= sum_{i,l} |(A0^-1)_il|
                         (sum_j b_ij |z_j|)
                         (sum_k b_lk |z_k|)
       <= sum_j d_j z_j^2,
  d_j = sum_{i,l} b_ij |(A0^-1)_il| sum_k b_lk.
Second inequality is exact matrix row diagonal domination, not
entrywise substitution in the actual signed operator.

This keeps the FULL exact original 3x3 anchor inverse rather
than SM65's crude A^-1<=ell^-1 I3. D_exact=diag(ceil(d_j)),
and actual 22D signed Schur
   S_actual >= L62[R,R]-D_exact.
Compact full 22x22 rational lower only with outward max-row fee.
Test whether exact-inverse D actually dominates SM65's earlier
D_ell in diagonal Loewner sense; do not assume dominance.
Classify inertia of the LOWER only; negative pivots are NOT
actual negative modes. Source25 actual index<=22 (SM63) remains.

Full original 470 Astar strong inverse/infinite orthogonal
remainder, complete W-ODD-NEG O1/O2, even, Weil CC27 RH OPEN.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_sm43_positive_cell_envelope import ROOT,ceil_rat
from validate_rpb108_sm62_full25_338signed_positive import exact_inertia_general
from validate_rpb108_sm65_original_22schur_anisotropic import (
    main as replay_sm65,
    compact22,
    SM63_HASH,
    hash_matrix,
    P,R)

DEN=10**12
def up(x):return ceil_rat(x,DEN)
def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
def invert3(A):
    assert len(A)==3 and all(len(r)==3 for r in A)
    assert A[0][1]==A[1][0] and A[0][2]==A[2][0] and A[1][2]==A[2][1]
    d=det3(A)
    assert A[0][0]>0
    assert A[0][0]*A[1][1]-A[0][1]**2>0
    assert d>0
    cof=[]
    for i in range(3):
        row=[]
        for j in range(3):
            sub=[[A[u][v] for v in range(3) if v!=j]
                 for u in range(3) if u!=i]
            row.append(((-1 if (i+j)%2 else 1)*
                        (sub[0][0]*sub[1][1]-sub[0][1]*sub[1][0])))
        cof.append(row)
    inverse=[[cof[j][i]/d for j in range(3)] for i in range(3)]
    assert all(inverse[i][j]==inverse[j][i] for i in range(3) for j in range(3))
    assert all(sum(A[i][k]*inverse[k][j] for k in range(3))==
               (F(1) if i==j else F(0))
               for i in range(3) for j in range(3))
    return inverse,d

def calculate(source):
    assert source["status"]=="SCOPED_ACTUAL_ORIGINAL_22D_SIGNED_SCHUR_ANISOTROPIC_LOWER_NO_POSITIVITY"
    assert source["canonical_W_ODD_NEG"]=="OPEN"
    assert source["verified_original_SM58_negative_and_signed_all625_replay"]
    assert source["verified_original_SM62_complete_signed_all625_replay"]
    assert source["verified_original_SM63_direct_positive_3x3_replay"]
    assert source["positive_original_signed_physical_anchor"]==list(P)==[1,2,17]
    assert source["remaining_original_signed_source_indices"]==list(R)
    assert len(R)==22
    A=[[F(x) for x in row] for row in source["true_original_3source_anchor_signed_LOWER_rational"]]
    assert hash_matrix(A)==SM63_HASH
    inverse,det=invert3(A)
    b=[[F(x) for x in row] for row in source["actual_original_3x22_mixed_source_absolute_UPPER_matrix"]]
    assert len(b)==3 and all(len(row)==22 for row in b)
    assert all(x>=0 for row in b for x in row)
    row_sum=[sum(row,F(0)) for row in b]
    assert row_sum==[F(x) for x in source["actual_source_anchor_mixed_row_absolute_bounds"]]
    absolute_inverse=[[abs(x) for x in row] for row in inverse]
    # all 3x3 true anchored inverse terms, including off-diagonals
    weighted=[sum(absolute_inverse[i][l]*row_sum[l] for l in range(3))
              for i in range(3)]
    exact=[sum(b[i][j]*weighted[i] for i in range(3)) for j in range(22)]
    bound=[up(v) for v in exact]
    ell=[F(x) for x in source["actual_22D_anisotropic_schur_diagonal_penalty_upper"]]
    assert len(ell)==22 and all(x>=0 for x in ell)
    Ddiag_all=[bound[j]<=ell[j] for j in range(22)]
    L=[[F(x) for x in row] for row in source["true_original_22coordinate_signed_LOWER_rational"]]
    assert len(L)==22 and all(len(row)==22 for row in L)
    assert all(L[i][j]==L[j][i] for i in range(22) for j in range(22))
    Sraw=[[L[i][j]-(bound[i] if i==j else F(0))
            for j in range(22)] for i in range(22)]
    S,err=compact22(Sraw)
    inertia=exact_inertia_general(S)
    old_inertia=source["actual_Schur_anisotropic_LOWER_inertia"]
    assert sum(inertia)==22
    assert sum(old_inertia[x] for x in ("positive","negative","zero"))==22
    # Both independent Schur UPPER penalties are actual whole
    # 22x22 diagonal Loewner majorants; compare each entry,
    # not just trace and never apply elementwise minima to PSD
    # matrices where this would be mathematically invalid.
    compare=[bound[j]-ell[j] for j in range(22)]
    out={
     "status":"SCOPED_TRUE_ORIGINAL_22D_SCHUR_FULL_EXACT_3SOURCE_ANCHOR_INVERSE",
     "canonical_W_ODD_NEG":"OPEN",
     "verified_original_source_25D_SM65_full_replay":True,
     "verified_original_SM63_signed_actual_3plane":True,
     "positive_anchor_true_original_source_indices":list(P),
     "remaining_true_original_physical_source_indices":list(R),
     "actual_full_cross_pair_bounds_count":3*22,
     "original_positive_anchor_exact_determinant":str(det),
     "original_positive_anchor_inverse_verified_exact":True,
     "original_true_3x3_anchor_inverse_full_rational":[[str(v) for v in row] for row in inverse],
     "actual_all_cross_row_sum_bounds":[str(x) for x in row_sum],
     "inverse_weighted_anchor_cross_row_sums":[str(x) for x in weighted],
     "true_original_22D_exact_inverse_schur_diagonal_upper":[str(x) for x in bound],
     "old_original_SM65_ell_diagonal_upper":[str(x) for x in ell],
     "all22_inverse_penalty_not_larger_than_SM65":all(Ddiag_all),
     "penalty_directions_improved_count":sum(v for v in Ddiag_all),
     "new_exact_inverse_penalty_max":str(max(bound)),
     "new_exact_inverse_penalty_sum":str(sum(bound,F(0))),
     "old_ell_penalty_max":str(max(ell)),
     "old_ell_penalty_sum":str(sum(ell,F(0))),
     "new_exact_inverse_LOEWNER_signed_Schur_lower_rational":[[str(v) for v in row] for row in S],
     "new_full22_symmetric_outward_compaction_fee":str(err),
     "new_exact_inverse_lower_reference_inertia":{
         "positive":inertia[0],"negative":inertia[1],"zero":inertia[2]},
     "old_ell_lower_reference_inertia":old_inertia,
     "actual_true_22D_signed_Schur_PSD_certified":False,
     "actual_true_22D_signed_Schur_exact_negative_index_classified":False,
     "verified_actual_original_source25_negative_index_upper_SM63":22,
     "original_infinite_odd_negative_index_classified":False,
     "original_470_Astar_inverse_and_strong_orthogonal_remainder":False,
     "original_odd_O1O2_even_Weil_CC27_RH":False,
     "original_Fourier_and_closed_form_domain_independent_audit":"OPEN",
     "interpretation":"Full original actual positive SM63 3x3 anchor inverse, all 66 true physical mixed-source intervals, weighted matrix row upper and genuine true original source22 signed Schur LOWER. Does not classify actual Schur PSD/index; negative lower is not actual negative witness."
    }
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm66_actual_22D_exact_anchor_inverse_schur.json")
    args=p.parse_args()
    # Recover original source matrix and 66 genuine signed cross bounds
    # by executing the underlying complete SM65 rational source proof,
    # NOT by guessing or downloading an unaudited mutable report.
    replay_sm65()
    base=ROOT/"artifacts/sm65_original_actual_22D_Schur_anisotropic.json"
    assert base.exists()
    source=json.loads(base.read_text())
    out=calculate(source)
    path=ROOT/args.output
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("SM66 original true 22D full anchor inverse Schur:",json.dumps({
      "exact_anchor_inverse":True,
      "source_cross_pairs":66,
      "diagonal_bound_dominates_ell_scheme":out["all22_inverse_penalty_not_larger_than_SM65"],
      "directions_no_worse":out["penalty_directions_improved_count"],
      "old_penalty_sum":out["old_ell_penalty_sum"],
      "new_penalty_sum":out["new_exact_inverse_penalty_sum"],
      "new_reference_negative_inertia":out["new_exact_inverse_lower_reference_inertia"]["negative"],
      "actual_full_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
