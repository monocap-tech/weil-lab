#!/usr/bin/env python3
"""SM61: first TRUE original signed 23D Schur LOWER with all cross charged.

The original SM58 full physical 25x25 SI10 signed form admits a genuine
Loewner LOWER L25<=Q_actual, with all 973 negative-frequency whole-real
leaves, complete positive LOW source bands and true sinh-pole penalty.
An independently whole-frequency rigorous UPPER follows from SM41:

 Q_actual = A_o - K_neg - 2ppT <= A_o,
 A_o[0,Lambda] <= (17+ln Lambda)H,
 A_o[Lambda,infinity] <= SM41_TAIL * I25,
 H <= Hq+epsH I25 (entire actual SM42 physical Gram).

For Lambda=4096, a power of two, original SI06 ln2<347/500:
  alpha=17+12*(347/500)
  tail=2*(202/25)*(18+12*347/500)/4096.
Thus U25=alpha Hq+(alpha epsH+tail)I25 is a valid
ALL-FREQUENCY signed operator upper, not a finite FFT cut.

With L25<=Q_actual<=U25, E=U25-L25>=0, P=Q_actual-L25
satisfies 0<=P<=E. For every actual cross source pair i,j:
 |Q_actual,ij-L25,ij|²<=Pii Pjj<=Eii Ejj.
Hence original mixed block B between SM52's true-positive
two-source anchor indices (2,17) and remaining 23 genuine
source coordinates obeys |Bij|<=|Lij|+sqrt_upper(Eii Ejj).

The ACTUAL anchor A=Q_actual|P2 >= passing SM52 coupled
A52>0. Gershgorin supplies ell>0 with A52>=ell I2.
Thus for any actual 2x23 mixed B,
  B^T A^-1 B <= (sum_ij |Bij|_upper²/ell) I23.
The ACTUAL Schur S=C-B^T A^-1 B then obeys full
  S >= L25[R,R] - gamma I23.
Every source cross and true original exceptional pole was charged.
This is a rigorous ACTUAL signed 23D SCHUR lower, not a
Schur computed by splicing unrelated lower 2x2 and 25x25 blocks.

This crude U25 may make gamma enormously conservative and its
23D LOWER negative definite. That does NOT prove actual 23D
negative index or a negative eigenvalue: Q_actual>=L and S>=SLOW.
Full original odd infinite strong orthogonal remainder/470 inverse
and even/Weil/CC27/RH remain OPEN. Independent original physical
Fourier and closed-domain mathematical premise audit separate.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import LN
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,ceil_rat)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    original_full_25_physical_interval_gram)
from validate_rpb108_sm44_physical_fourier_cell_gram import sqrt_upper
from validate_rpb108_sm47_original_full_low_jensen import full_original_rational_gram
from validate_rpb108_sm57_original_25source_negative_upper import (
    original_positive_low_25,pole_outer_upper,
    outward_compact_matrix,exact_symmetric_25source_inertia)
from validate_rpb108_sm58_original_coupled_25negative import original_complete_coupled_negative
from validate_rpb108_sm60_23complement_lower_nogo import strict_negative_LDL

N=25
ANCHOR=(2,17)
REM=tuple(i for i in range(N) if i not in ANCHOR)
DEN=10**12

def up(x):return ceil_rat(x,DEN)
def fingerprint(M):
    data=json.dumps([[str(z) for z in row] for row in M],
                    separators=(",",":"),ensure_ascii=True)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()
def symmetric(M):
    return all(M[i][j]==M[j][i] for i in range(len(M))
               for j in range(len(M)))
def exact_23_lower_compact(M):
    n=len(M)
    assert n==23 and symmetric(M)
    # All rational 23x23 entries are an exact genuine Schur LOWER
    # before outward matrix rounding. Compact rational display is
    # only valid after charging full max-absolute-row-sum error.
    q=[[F(round(M[i][j]*DEN),DEN) for j in range(n)] for i in range(n)]
    assert symmetric(q)
    fee=up(max(sum(abs(q[i][j]-M[i][j]) for j in range(n))
               for i in range(n)))
    out=[[q[i][j]-(fee if i==j else F(0))
          for j in range(n)] for i in range(n)]
    assert symmetric(out)
    return out,fee

def true_full25_analytic_signed_upper(gram):
    """True Q<=U from SM41 whole-frequency Ao and SM42 full Gram."""
    assert LN[2][1]<F(347,500)
    cutoff=4096
    assert cutoff==2**12
    log_upper=12*F(347,500)
    alpha=F(17)+log_upper
    # exact SM41 original supported source bounds:
    # 16 sin with u=1/2, 8 xcos with u=7/10,
    # real supported sinh pole with u=2/5.
    energy=16*F(1,2)**2+8*F(7,10)**2+F(2,5)**2
    assert energy==F(202,25)
    # 2*energy*(18+ln cutoff)/cutoff is an actual original
    # all-real high-frequency positive Ao Fourier form upper.
    tail=2*energy*(18+log_upper)/cutoff
    assert alpha>0 and 0<tail<1
    Hq,epsH=full_original_rational_gram(gram)
    assert len(Hq)==N and epsH>=0 and symmetric(Hq)
    scalar=alpha*epsH+tail
    U=[[alpha*Hq[i][j]+(scalar if i==j else F(0))
        for j in range(N)] for i in range(N)]
    assert symmetric(U)
    return U,alpha,tail,epsH

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm61_actual_original_23D_signed_Schur_two_sided.json")
    a=p.parse_args()
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in manifest["obligations"] if x["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==manifest["objective"]["status"]=="open"
    assert manifest["governance"]["no_automatic_promotion"]
    assert all(z in odd["evidence"] for z in ("SM52","SM58","SM59","SM60","SM61"))
    pin=json.loads((ROOT/"certificates/rpb108_sm58_full25_signed_summary.json").read_text())
    assert pin["actions_run_id"]==39281588617
    assert pin["source_indices"] if "source_indices" in pin else True
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==N and sources[24][0]=="pole"
    G,actual,pole=original_full_25_physical_interval_gram()
    assert actual==sources
    negative,neg_stats=original_complete_coupled_negative(centers,sources)
    assert neg_stats["whole_original_negative_frequency_leaves"]==973
    assert fingerprint(negative)==pin[
        "original_full25_coupled_negative_upper_all_625_entries_sha256"]
    positive,_=original_positive_low_25(centers,sources,G)
    pole_upper,_=pole_outer_upper(G)
    L_exact=[[positive[i][j]-negative[i][j]-pole_upper[i][j]
              for j in range(N)] for i in range(N)]
    L,Lfee=outward_compact_matrix(L_exact)
    assert fingerprint(L)==pin[
        "original_full25_signed_lower_all_625_entries_sha256"]
    U,alpha,tail,epsH=true_full25_analytic_signed_upper(G)
    E=[[U[i][j]-L[i][j] for j in range(N)] for i in range(N)]
    assert symmetric(E)
    assert all(E[i][i]>=0 for i in range(N))
    # For all z, 0<= Q-L <= E. Cauchy of the actual PSD
    # error Q-L supplies sourcewise cross enclosures.
    SM52=json.loads((ROOT/"certificates/rpb108_sm52_original_coupled_source_matrix.json").read_text())
    assert SM52["source_indices"]==list(ANCHOR)
    anchor=[[F(x) for x in row] for row in SM52["matrix"]]
    assert len(anchor)==2 and anchor[0][1]==anchor[1][0]
    assert anchor[0][0]>0
    assert anchor[0][0]*anchor[1][1]-anchor[0][1]**2==F(
         SM52["original_sylvester_determinant"])>0
    ell=min(anchor[i][i]-abs(anchor[i][1-i]) for i in range(2))
    assert ell>0
    # Exact rational enlarged |B|_ij on all 2x23 mixed source
    # directions. These are TRUE bounds on the actual signed B,
    # not inherited uncorrected negative lower-matrix cross entries.
    radius={}
    sum_cross=F(0)
    max_cross=F(0)
    for i in ANCHOR:
        for j in REM:
            rad=up(sqrt_upper(E[i][i]*E[j][j]))
            bound=abs(L[i][j])+rad
            assert bound>=abs(L[i][j])
            radius[(i,j)]=bound
            sum_cross+=bound**2
            max_cross=max(max_cross,bound)
    assert len(radius)==2*23
    gamma=up(sum_cross/ell)
    assert gamma>=0
    # The ACTUAL Schur S=C-B^T A^-1 B is bounded below:
    # C>=L[R,R], A^-1 <=ell^-1 I2, B^T B <=||B||F² I23.
    S_exact=[[L[i][j]-(gamma if i==j else F(0))
              for j in REM] for i in REM]
    S,fee=exact_23_lower_compact(S_exact)
    pivots=strict_negative_LDL(S)  # strictly NEGATIVE LOWER only
    assert len(pivots)==23 and max(pivots)<0
    # SM60's lower-reference complement is itself negative.
    # A further nonnegative cross fee cannot make this lower PD.
    result={
      "status":"CERTIFIED_ACTUAL_ORIGINAL_23D_SIGNED_SCHUR_TWO_SIDED_LOWER_NO_POSITIVITY",
      "canonical_W_ODD_NEG":"OPEN",
      "original_physical_source_count":25,
      "original_positive_anchor_source_indices":list(ANCHOR),
      "actual_source_coordinate_complement_indices":list(REM),
      "actual_coordinate_complement_dimension":23,
      "original_all625_negative_UPPER_hash_replay":True,
      "original_all625_signed_LOWER_hash_replay":True,
      "original_full_signed_LOWER_accepted_SM58_Actions_id":39281588617,
      "original_all_real_positive_multiplier_SM41_upper":"a_o<=17+log xi for xi>=1",
      "original_analytic_low_band_cutoff":4096,
      "original_analytic_low_band_alpha":str(alpha),
      "original_analytic_high_tail_operator_upper_I":str(tail),
      "original_full25_physical_Gram_interval_export_fee":str(epsH),
      "original_full25_signed_two_sided_Loewner_enclosure":True,
      "original_signed_upper_pole_subtraction_and_negative_operator":"both nonpositive, therefore U25 bounds Q",
      "original_2x2_actual_positive_anchor_Loewner_Gershgorin_lower":str(ell),
      "actual_source_mixed_cross_interval_pairs_certified":len(radius),
      "actual_source_mixed_cross_max_absolute_bound":str(up(max_cross)),
      "actual_source_mixed_cross_Frobenius_squared_upper":str(up(sum_cross)),
      "actual_Schur_negative_compensation_upper_I":str(gamma),
      "actual_Schur_23x23_lower_outward_compaction_fee":str(fee),
      "actual_signed_23D_Schur_true_LOEWNer_lower_matrix":[[str(x) for x in row] for row in S],
      "actual_signed_23D_Schur_LOWER_reference_negative_pivots":[str(x) for x in pivots],
      "ACTUAL_original_23D_signed_Schur_PSD_certified":False,
      "ACTUAL_original_23D_signed_Schur_negative_index_classified":False,
      "original_actual_25D_source_negative_index_upper_bound":23,
      "actual_complete_infinite_original_odd_negative_index_classified":False,
      "original_470_source_Astar_strong_inverse_and_orthogonal_remainder":False,
      "original_odd_O1O2_even_Weil_CC27_RH":False,
      "independent_original_Fourier_closed_domain_premise_audit":"OPEN",
      "interpretation":"All original source B and C genuinely bounded with two-sided entire signed operator order, true anchor inverse paid, producing valid ACTUAL signed 23D Schur LOWER. Its negative pivots are solely a lower-reference limitation, NOT actual negative directions. Entire infinite original odd/even/Weil/RH still open."
    }
    target=ROOT/a.output;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,indent=2)+"\n")
    print("SM61 original TRUE signed 23D Schur interval:",json.dumps({
       "full_actual_B_cross_pairs":len(radius),
       "analytic_alpha":float(alpha),
       "whole_actual_schur_cross_fee":float(gamma),
       "actual_Schur_LOWER_negative_pivots":len(pivots),
       "actual_Schur_positive":False,
       "complete_odd_Weil_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":main()
