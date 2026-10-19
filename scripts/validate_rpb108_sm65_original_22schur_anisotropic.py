#!/usr/bin/env python3
"""SM65: actual original source22 Schur anisotropic mixed-coupling LOWER.

Verified SM63 genuine signed 3D source plane [g1,g2,g17] anchors
the ACTUAL signed 25-source operator (SM63 Actions39314851844 PASS);
verified SM62 gives genuine stronger all25 signed lower L62 with
338 new signed positive windows (Actions39311001837 PASS).
Whole-frequency analytic SM41+SM42 gives independent U25 actual
source upper. Hence for actual Q25:
          L62 <= Q25 <= U25,
with every all-original signed Fourier source/Pole charged.

Let P=[1,2,17], R=other22 original physical SI10 source indices.
Original SM63 actual signed A=Q_PP>=A63>0, with certified
Gershgorin A63>=ell I3. Let E=U25-L62>=Q-L62>=0,
so |B_actual(i,j)|<=b_ij := |L62_ij|+sqrt(Eii Ejj)
for all 66 mixed actual physical source coefficients.

Rather than SM61's huge isotropic source penalty
    gamma I22,  gamma=sum_ij b_ij²/ell,
use the COMPLETE ORIGINAL SOURCE-DEPENDENT diagonal dominance
    B^T A^-1 B <= diag_j [sum_i b_ij * sum_k b_ik / ell]
from weighted Cauchy on each signed anchor row:
    |sum_j B_ij z_j|²
       <= (sum_j b_ij) sum_j b_ij z_j².
Every individual penalty is rounded UP before export. This is
a valid ACTUAL original signed 22D Schur LOWER
    S_actual >= L62[R,R] - D_anisotropic.
It may still be indefinite; negative eigenvalues of this LOWER
are NOT negative actual Schur witnesses.

Require end-to-end re-evaluation and exact 625-entry SHA256 of
SM62 original signed source25 LOWER, original SM58 negative
frequency upper SHA256, genuine SM63 complete true signed positive
3x3 rational lower SHA256, and original 338 source positive
windows. Failing any check blocks result.

Full original 470 source Astar inverse/infinite orthogonal
remainder and canonical original W-ODD-NEG O1/O2,
even/Weil/CC27/RH remain OPEN, Fourier/domain premise audit OPEN.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,ceil_rat)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    original_full_25_physical_interval_gram)
from validate_rpb108_sm44_physical_fourier_cell_gram import sqrt_upper
from validate_rpb108_sm57_original_25source_negative_upper import (
    original_positive_low_25,pole_outer_upper,outward_compact_matrix)
from validate_rpb108_sm58_original_coupled_25negative import (
    original_complete_coupled_negative)
from validate_rpb108_sm62_full25_338signed_positive import (
    all_338_disjoint_original_signed_positive,
    selected_full25_source_extra,exact_inertia_general)
from validate_rpb108_sm61_actual_23schur_two_sided import (
    true_full25_analytic_signed_upper)

N=25
P=(1,2,17)
R=tuple(i for i in range(25) if i not in P)
DEN=10**12
SM62_HASH="87594b103a0575f1d5945e37cf16917c5184573acb6d305709b09d9eafb9971c"
SM63_HASH="dcbfb11ba91a04b32aeb5b437627c32d185a05f2a488080a80a7aad98a494d50"

SM63_LOWER_STR=(
 ("510849936037/1000000000000","3199307/100000000","1440357/50000000"),
 ("3199307/100000000","1077565046037/1000000000000","421561/100000000"),
 ("1440357/50000000","421561/100000000","1446599756037/1000000000000")
)

def up(x):return ceil_rat(x,DEN)
def hash_matrix(M):
    encoded=json.dumps([[str(x) for x in row] for row in M],
                       separators=(",",":"),ensure_ascii=True)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()
def symmetric(A):
    n=len(A)
    return all(A[i][j]==A[j][i] for i in range(n) for j in range(n))
def compact22(A):
    assert len(A)==22 and symmetric(A)
    q=[[F(round(A[i][j]*DEN),DEN) for j in range(22)] for i in range(22)]
    assert symmetric(q)
    err=up(max(sum(abs(A[i][j]-q[i][j]) for j in range(22))
               for i in range(22)))
    out=[[q[i][j]-(err if i==j else F(0))
           for j in range(22)] for i in range(22)]
    assert symmetric(out)
    return out,err
def certified_sm63_anchor():
    A=[[F(x) for x in row] for row in SM63_LOWER_STR]
    assert hash_matrix(A)==SM63_HASH
    def det(a):
        n=len(a)
        if n==1:return a[0][0]
        return sum(((-1 if j%2 else 1)*a[0][j]*
                   det([[a[i][k] for k in range(n) if k!=j]
                        for i in range(1,n)])
                    for j in range(n)),F(0))
    assert all(det([row[:k] for row in A[:k]])>0 for k in (1,2,3))
    ell=min(A[i][i]-sum(abs(A[i][j]) for j in range(3) if j!=i)
            for i in range(3))
    assert ell>0
    return A,ell

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm65_original_actual_22D_Schur_anisotropic.json")
    a=p.parse_args()
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in ledger["obligations"] if o["id"]=="W-ODD-NEG")
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==ledger["objective"]["status"]=="open"
    assert ledger["governance"]["no_automatic_promotion"]
    assert all(z in odd["evidence"] for z in ("SM58","SM61","SM62","SM63","SM65"))
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==25 and sources[24][0]=="pole"
    gram,actual,_=original_full_25_physical_interval_gram()
    assert actual==sources
    neg,stats=original_complete_coupled_negative(centers,sources)
    pin=json.loads((ROOT/"certificates/rpb108_sm58_full25_signed_summary.json").read_text())
    assert stats["whole_original_negative_frequency_leaves"]==973
    assert hash_matrix(neg)==pin["original_full25_coupled_negative_upper_all_625_entries_sha256"]
    pos,_=original_positive_low_25(centers,sources,gram)
    pole,_=pole_outer_upper(gram)
    baseline=[[pos[i][j]-neg[i][j]-pole[i][j]
               for j in range(N)] for i in range(N)]
    L0,_=outward_compact_matrix(baseline)
    assert hash_matrix(L0)==pin["original_full25_signed_lower_all_625_entries_sha256"]
    signed,_=all_338_disjoint_original_signed_positive(centers,sources)
    assert len(signed)==338
    blocks,_=selected_full25_source_extra(centers,sources,signed)
    X=blocks[338]["matrix"]
    eps=blocks[338]["total_extra_error_fee"]
    assert eps>0 and symmetric(X)
    # Same original full lower construction verified in SM62.
    full=[[L0[i][j]+X[i][j]-(eps if i==j else F(0))
           for j in range(N)] for i in range(N)]
    L,round_fee=outward_compact_matrix(full)
    assert hash_matrix(L)==SM62_HASH
    assert symmetric(L)
    U,alpha,tail,gramfee=true_full25_analytic_signed_upper(
            gram,centers,sources)
    E=[[U[i][j]-L[i][j] for j in range(N)] for i in range(N)]
    assert symmetric(E) and all(E[i][i]>=0 for i in range(N))
    A,ell=certified_sm63_anchor()
    # Q_actual>=A on its 3D source plane; all P sources are the
    # exact same three genuinely physical original SI10 sources.
    assert len(P)==3 and len(R)==22
    bound={}
    rowsums={i:F(0) for i in P}
    for i in P:
        for j in R:
            radius=up(sqrt_upper(E[i][i]*E[j][j]))
            bij=abs(L[i][j])+radius
            assert bij>=0
            bound[i,j]=bij
            rowsums[i]+=bij
    assert len(bound)==66 and all(rowsums[i]>0 for i in P)
    anisotropic={j:up(sum((rowsums[i]*bound[i,j] for i in P),F(0))/ell)
                 for j in R}
    scalar_gamma=up(sum((bound[i,j]**2 for i in P for j in R),F(0))/ell)
    assert scalar_gamma>0 and all(v>=0 for v in anisotropic.values())
    # Row-weighted true B mixed block Cauchy:
    # B^T A^-1 B <= D_anisotropic; also <=gamma I globally.
    actual_lower=[[L[i][j]-(anisotropic[i] if i==j else F(0))
                   for j in R] for i in R]
    isotropic_lower=[[L[i][j]-(scalar_gamma if i==j else F(0))
                      for j in R] for i in R]
    compacted,er=compact22(actual_lower)
    compact_scalar,er_scalar=compact22(isotropic_lower)
    inert=exact_inertia_general(compacted)
    inert_scalar=exact_inertia_general(compact_scalar)
    inert_base=exact_inertia_general([[L[i][j] for j in R] for i in R])
    assert sum(inert)==sum(inert_scalar)==sum(inert_base)==22
    result={
      "status":"SCOPED_ACTUAL_ORIGINAL_22D_SIGNED_SCHUR_ANISOTROPIC_LOWER_NO_POSITIVITY",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_original_SM58_negative_and_signed_all625_replay":True,
      "verified_original_SM62_complete_signed_all625_replay":True,
      "verified_original_SM63_direct_positive_3x3_replay":True,
      "original_source_count":25,
      "positive_original_signed_physical_anchor":[1,2,17],
      "remaining_original_signed_source_indices":list(R),
      "remaining_signed_source_dimension":22,
      "actual_all_real_analytic_positive_upper_alpha":str(alpha),
      "actual_all_real_analytic_infinite_tail":str(tail),
      "original_physical_Gram_interval_total_upper_error":str(gramfee),
      "actual_positive_anchor_signed_Gershgorin_eigen_lower":str(ell),
      "actual_mixed_physical_source_pairs_full_count":66,
      "actual_source_anchor_mixed_row_absolute_bounds":[str(rowsums[i]) for i in P],
      "actual_source_mixed_max_absolute_bound":str(up(max(bound.values()))),
      "actual_22D_anisotropic_schur_diagonal_penalty_upper":[
           str(anisotropic[j]) for j in R],
      "actual_22D_isotropic_schur_comparison_penalty":str(scalar_gamma),
      "actual_22D_anisotropic_penalty_max":str(max(anisotropic.values())),
      "actual_22D_anisotropic_penalty_sum":str(sum(anisotropic.values(),F(0))),
      "verified_338_positive_window_source25_Loewner_fee":str(eps),
      "source25_lower_complete_rational_export_fee":str(round_fee),
      "true_actual_22D_signed_Schur_LOEWNER_lower_rational":[
         [str(x) for x in row] for row in compacted],
      "true_actual_22D_signed_Schur_lower_export_fee":str(er),
      "original_22D_coordinate_reference_lower_inertia":{
         "positive":inert_base[0],"negative":inert_base[1],"zero":inert_base[2]},
      "actual_Schur_anisotropic_LOWER_inertia":{
         "positive":inert[0],"negative":inert[1],"zero":inert[2]},
      "actual_Schur_isotropic_LOWER_inertia":{
         "positive":inert_scalar[0],"negative":inert_scalar[1],"zero":inert_scalar[2]},
      "actual_original_22D_signed_Schur_PSD_certified":False,
      "actual_original_22D_signed_Schur_negative_index_exactly_classified":False,
      "actual_original_25D_source_negative_index_upper_SM63":22,
      "infinite_original_odd_negative_index_classified":False,
      "original_470_Astar_inverse_and_strong_orthogonal_remainder":False,
      "odd_O1O2_even_Weil_CC27_RH":False,
      "independent_original_Fourier_closed_domain_audit":"OPEN",
      "interpretation":"True ACTUAL 22-dimensional signed Schur lower with ALL 66 P3-to-R22 original physical mixed source cross bound by source-specific Cauchy row-weighted diagonal; exact verified SM58/62/63 source certificates. Negative LOWER directions say nothing about true source negativity; entire odd/even/Weil/RH OPEN."
    }
    path=ROOT/a.output;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+"\n")
    print("SM65 original actual 22D signed Schur anisotropic:",json.dumps({
       "mixed_true_source_crosses":66,
       "true_source_index_ceiling":22,
       "anisotropic_max":str(up(max(anisotropic.values()))),
       "isotropic_gamma":str(scalar_gamma),
       "anisotropic_lower_negative_inertia":inert[1],
       "isotropic_lower_negative_inertia":inert_scalar[1],
       "actual_Schur_PSD":False,
       "full_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
