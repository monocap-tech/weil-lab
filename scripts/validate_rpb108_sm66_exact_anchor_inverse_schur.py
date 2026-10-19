#!/usr/bin/env python3
"""SM66: ACTUAL original source21 signed Schur with SM64 FULL 4x4 anchor inverse.

Rebuild the independently verified full original 25-source signed
two-sided enclosure L62<=Qactual<=U25 via the complete SM65 source
replay. SM64 focused Actions 39323057878 independently proves the
physical ORIGINAL four-source [g1,g2,g17,g22] signed anchor
Aactual>=A64>0, and all four exact Sylvester minors are positive.

With positive anchor P4=(1,2,17,22) and R21=other genuine original
supported SI10 physical source functions, the TRUE difference
F=Q-L62 satisfies 0<=F<=E=U-L62, whence each of the
4*21=84 actual physical source mixed elements satisfies
   |B_actual,ij| <= b_ij := |L62_ij|+sqrt_up(Eii Ejj).

Using the FULL exact 4x4 A64 inverse and Loewner inverse order
Aactual^-1<=A64^-1, all real complement vectors z obey
z^T B^T Aactual^-1 B z <= sum_{i,l}|A64^-1_il|
                                 (sum_j b_ij|zj|)
                                 (sum_k b_lk|zk|)
                         <= sum_j d_j zj²,
d_j=sum_{i,l} b_ij |A64^-1_il| sum_k b_lk.
The final row-sum domination uses symmetric nonnegative coupling,
the exact inequality 2|zj zk|<=zj²+zk², and outward rational
ceil on each d_j. Thus the ACTUAL signed Schur remainder satisfies
 S_actual >= L62[R21,R21] - diag(d_1,...,d_21).

For an independently valid SAME-ANCHOR comparator, also compute
SM65-style scalar Aactual^-1<=ell^-1 I4 from the 4x4 Gershgorin
margin and diagonal row-wise Cauchy, d_ell_j=
sum_i b_ij (sum_k b_ik)/ell. Compare full 21 entries in
true diagonal Loewner order; do NOT infer dominance from trace.

A negative lower-matrix pivot is NOT an actual negative mode or
negative index classification. Finite source25 actual negative
index <=21 holds independently by SM64. Complete 470 Astar
inverse/infinite orthogonal remainder, W-ODD-NEG O1/O2,
even/Weil CC27 RH and independent Fourier/form-domain audit OPEN.
"""
import argparse,json,hashlib
from fractions import Fraction as F
from validate_rpb108_sm43_positive_cell_envelope import ROOT,ceil_rat
from validate_rpb108_sm62_full25_338signed_positive import exact_inertia_general
from validate_rpb108_sm65_original_22schur_anisotropic import (
    main as replay_sm65, compact22, hash_matrix,
    SM62_HASH)

DEN=10**12
ANCHOR=(1,2,17,22)
REM=tuple(i for i in range(25) if i not in ANCHOR)
SM64_SHA256="a597efeaddbf690c82a8a1274fc4ba3e15d6a31eb3594db502e7f8c15544ce42"
SM64_SOURCE_ACTIONS=39323057878
SM64_A_STR=(
 ("510771828331/1000000000000","3199307/100000000","1440357/50000000","1197/25000000"),
 ("3199307/100000000","1077486938331/1000000000000","421561/100000000","-521/20000000"),
 ("1440357/50000000","421561/100000000","1446521648331/1000000000000","-2567/25000000"),
 ("1197/25000000","-521/20000000","-2567/25000000","19766848331/1000000000000"),
)
def up(x):return ceil_rat(x,DEN)
def symmetric(A):
    return all(A[i][j]==A[j][i] for i in range(len(A)) for j in range(len(A)))

def exact_inverse(A):
    n=len(A)
    assert n==4 and all(len(row)==4 for row in A) and symmetric(A)
    # Exact positive Sylvester via congruence Schur pivot elimination
    sch=[row[:] for row in A]
    leading=[]
    for k in range(n):
        pivot=sch[k][k]
        assert pivot>0, "Original SM64 four-source anchor must be SPD"
        leading.append(pivot)
        for i in range(k+1,n):
            for j in range(i,n):
                sch[i][j]-=sch[i][k]*sch[j][k]/pivot
                sch[j][i]=sch[i][j]
    X=[[A[i][j] for j in range(n)]+[F(1) if i==j else F(0) for j in range(n)]
       for i in range(n)]
    for k in range(n):
        piv=X[k][k]
        assert piv!=0
        X[k]=[x/piv for x in X[k]]
        for i in range(n):
            if i==k:continue
            factor=X[i][k]
            X[i]=[X[i][j]-factor*X[k][j] for j in range(2*n)]
    inv=[row[n:] for row in X]
    assert symmetric(inv)
    assert all(sum(A[i][k]*inv[k][j] for k in range(n))==
               (F(1) if i==j else F(0))
               for i in range(n) for j in range(n))
    return inv,leading

def compact21(A):
    n=len(A)
    assert n==21 and all(len(row)==n for row in A) and symmetric(A)
    q=[[F(round(A[i][j]*DEN),DEN) for j in range(n)] for i in range(n)]
    assert symmetric(q)
    err=up(max(sum(abs(A[i][j]-q[i][j]) for j in range(n))
               for i in range(n)))
    out=[[q[i][j]-(err if i==j else F(0))
          for j in range(n)] for i in range(n)]
    assert symmetric(out)
    return out,err

def calculate(source):
    assert source["status"]=="SCOPED_ACTUAL_ORIGINAL_22D_SIGNED_SCHUR_ANISOTROPIC_LOWER_NO_POSITIVITY"
    assert source["canonical_W_ODD_NEG"]=="OPEN"
    assert source["verified_original_SM58_negative_and_signed_all625_replay"]
    assert source["verified_original_SM62_complete_signed_all625_replay"]
    assert source["verified_original_SM63_direct_positive_3x3_replay"]
    assert source["positive_original_signed_physical_anchor"]==[1,2,17]
    assert len(REM)==21 and len(ANCHOR)==4
    A=[[F(x) for x in row] for row in SM64_A_STR]
    assert hash_matrix(A)==SM64_SHA256
    inv,pivots=exact_inverse(A)
    ell=min(A[i][i]-sum(abs(A[i][j]) for j in range(4) if j!=i)
            for i in range(4))
    assert ell>0
    # These arrays were independently regenerated from the *full*
    # SM58/SM62 genuine signed physical source25 L and SM41/42
    # original whole-frequency U, NOT an assumed infinite cutoff.
    L=[[F(x) for x in row] for row in source["true_original_25source_complete_signed_LOWER_rational"]]
    E=[F(x) for x in source["true_original_25source_two_sided_difference_upper_diagonal"]]
    assert len(L)==25 and all(len(row)==25 for row in L)
    assert symmetric(L) and hash_matrix(L)==SM62_HASH
    assert len(E)==25 and all(x>=0 for x in E)
    b=[]
    for i in ANCHOR:
        row=[]
        for j in REM:
            rad=up_sqrt(E[i]*E[j])
            x=abs(L[i][j])+rad
            assert x>=0
            row.append(x)
        b.append(row)
    assert len(b)==4 and all(len(row)==21 for row in b)
    rowsum=[sum(row,F(0)) for row in b]
    assert all(x>0 for x in rowsum)
    inverse_abs=[[abs(v) for v in row] for row in inv]
    weighted=[sum(inverse_abs[i][k]*rowsum[k] for k in range(4))
              for i in range(4)]
    exact=[sum(b[i][j]*weighted[i] for i in range(4)) for j in range(21)]
    dinv=[up(x) for x in exact]
    # Fully independent same-anchor positive inverse bound
    # Aactual^-1 <= ell^-1 I4: weighted row Cauchy.
    dell=[up(sum((b[i][j]*rowsum[i] for i in range(4)),F(0))/ell)
          for j in range(21)]
    dominance=all(dinv[j]<=dell[j] for j in range(21))
    lref=[[L[i][j] for j in REM] for i in REM]
    S_inv,err_inv=compact21([[lref[i][j]-(dinv[i] if i==j else F(0))
                             for j in range(21)] for i in range(21)])
    S_ell,err_ell=compact21([[lref[i][j]-(dell[i] if i==j else F(0))
                             for j in range(21)] for i in range(21)])
    indices=[exact_inertia_general(A) for A in (lref,S_inv,S_ell)]
    assert all(sum(x)==21 for x in indices)
    # For this exact 4x4 anchor, every exact inverse matrix source
    # row and all 84 signed mixed physical couplings are retained;
    # no 3D source-index statement is silently promoted to 4D.
    out={
      "status":"SCOPED_ACTUAL_ORIGINAL_21D_SIGNED_SCHUR_FOUR_SOURCE_EXACT_INVERSE",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_all_original_SM65_full_source25_signed_two_sided_replay":True,
      "verified_SM62_original_signed_25source_all625_hash":SM62_HASH,
      "verified_original_SM64_positive_4source_exact_matrix_sha256":SM64_SHA256,
      "source_SM64_true_original_signed_4plane_focused_Actions":SM64_SOURCE_ACTIONS,
      "true_original_positive_physical_anchor_sources":list(ANCHOR),
      "true_original_remaining_physical_source_indices":list(REM),
      "true_original_remaining_source_dimension":21,
      "true_actual_original_mixed_source_pairs_count":4*21,
      "original_positive_anchor_four_exact_rational_LDL_pivots":[str(x) for x in pivots],
      "original_positive_anchor_full_4x4_exact_inverse":[[str(x) for x in row] for row in inv],
      "original_positive_anchor_Gershgorin_lower":str(ell),
      "actual_all84_mixed_cross_row_sum_bounds":[str(x) for x in rowsum],
      "full_inverse_weighted_mixed_anchor_source_row_sums":[str(x) for x in weighted],
      "actual_21D_full_inverse_anisotropic_schur_penalty":[str(x) for x in dinv],
      "actual_21D_Gershgorin_anisotropic_schur_penalty":[str(x) for x in dell],
      "full_inverse_diagonal_UPPER_dominates_ell_scheme":dominance,
      "full_inverse_directions_not_worse_count":sum(dinv[j]<=dell[j] for j in range(21)),
      "full_inverse_schur_penalty_sum":str(sum(dinv,F(0))),
      "Gershgorin_schur_penalty_sum":str(sum(dell,F(0))),
      "full_inverse_schur_penalty_max":str(max(dinv)),
      "Gershgorin_schur_penalty_max":str(max(dell)),
      "original_signed_coordinate_reference_21D_inertia":{
          "positive":indices[0][0],"negative":indices[0][1],"zero":indices[0][2]},
      "full_inverse_TRUE_schur_21D_LOWER_inertia":{
          "positive":indices[1][0],"negative":indices[1][1],"zero":indices[1][2]},
      "Gershgorin_TRUE_schur_21D_LOWER_inertia":{
          "positive":indices[2][0],"negative":indices[2][1],"zero":indices[2][2]},
      "full_inverse_TRUE_signed_21D_Schur_LOEWNer_lower":[[str(x) for x in row] for row in S_inv],
      "full_inverse_true_Schur_lower_rational_export_fee":str(err_inv),
      "Gershgorin_true_Schur_lower_rational_export_fee":str(err_ell),
      "ACTUAL_21D_signed_Schur_PSD_certified":False,
      "ACTUAL_21D_signed_Schur_negative_index_exactly_classified":False,
      "verified_original_ACTUAL_25source_negative_index_upper_SM64":21,
      "complete_original_infinite_odd_negative_index_classified":False,
      "original_470_Astar_inverse_strong_orthogonal_remainder":False,
      "W_ODD_NEG_O1O2_even_Weil_CC27_RH":False,
      "independent_original_Fourier_closed_domain_audit":"OPEN",
      "interpretation":"True original signed 21D Schur lower using all84 physical P4×R21 mixed source bounds, exact full 4x4 SM64 positive source inverse and original SM62/SM41 full signed Loewner sandwich. Lower negative modes never negative actual operator witnesses. Whole infinite odd/even/Weil/RH OPEN."
    }
    return out

def up_sqrt(x):
    from validate_rpb108_sm44_physical_fourier_cell_gram import sqrt_upper
    return up(sqrt_upper(x))

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm66_actual_original_21D_signed_schur_four_source_inverse.json")
    args=p.parse_args()
    # The source-bound proof is recomputed from exact original
    # physical analytic Fourier and real-frequency interval code.
    replay_sm65()
    parent=ROOT/"artifacts/sm65_original_actual_22D_Schur_anisotropic.json"
    assert parent.exists()
    result=calculate(json.loads(parent.read_text()))
    target=ROOT/args.output
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,indent=2)+"\n")
    print("SM66 ACTUAL original 21D signed full four-anchor inverse Schur:",
          json.dumps({
             "anchor_positive_dim":4,
             "all_true_cross_pairs":84,
             "inverse_row_scheme_dominates_ell":result["full_inverse_diagonal_UPPER_dominates_ell_scheme"],
             "source21_lower_negative_inertia":result["full_inverse_TRUE_schur_21D_LOWER_inertia"]["negative"],
             "actual_25D_index_ceiling":21,
             "original_full_odd_Weil_RH":"OPEN"
          }),flush=True)
if __name__=="__main__":main()
