#!/usr/bin/env python3
"""SM67: COUPLED PSD-COVARIANCE upper for the ACTUAL original 21D odd Schur.

Canonical original physical source25 two-sided interval L62<=Q<=U,
replayed end-to-end by SM65/SM66. Let F=Q-L62, 0<=F<=E=U-L62.
SM64 verified a complete positive ORIGINAL 4x4 physical source block
A_actual>=A64>0 on (1,2,17,22), so A_actual^-1<=A64^-1.

Split the ACTUAL 4x21 cross B=L_PR+F_PR. Crucially, do NOT bound
its 84 coefficients independently. PSD block Cauchy applied to
the complete 25x25 F proves, in 21D Loewner order,
 F_PR^T A64^-1 F_PR
   <= tr(A64^-1 F_PP) F_RR
   <= tr(A64^-1 E_PP) E_RR
 = sigma E_RR.
This preserves all 441 signed source covariance entries of the
entire R21 complement in E_RR, with no rowwise absolute-value
Cauchy inflation.

For every rational t>0, weighted matrix Young gives
 B^T A_actual^-1 B <=
    (1+t) L_RP A64^-1 L_PR + (1+1/t) sigma E_RR = W_t.
This is a COMPLETE original genuine signed 21x21 Schur penalty
UPPER (not mere entrywise control), and so
   S_actual >= L_RR-W_t.
Recompute t in a fixed finite rational grid, exact rational
21x21 outward compression, exact 21D inertia for each.

As independent comparator, compute SM66's exact inverse anchored
84-cross DIAGONAL UPPER D66 on the SAME original 4plane, and
test W_t<=D66 in true Loewner order via exact rational 21D
congruence. Never infer matrix order merely from traces.

All certified negativity belongs to a conservative LOWER, not
an actual negative signed mode. Finite original 25D source index
<=21 independently SM64; full odd operator / 470 Astar strong
inverse and infinite remainder, W-ODD-NEG O1/O2/even Weil
CC27/RH and original Fourier/form-domain premise audit OPEN.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_sm43_positive_cell_envelope import ROOT
from validate_rpb108_sm62_full25_338signed_positive import exact_inertia_general
from validate_rpb108_sm65_original_22schur_anisotropic import (
    main as replay_sm65, hash_matrix, SM62_HASH)
from validate_rpb108_sm66_exact_anchor_inverse_schur import (
    ANCHOR,REM,SM64_A_STR,SM64_SHA256,exact_inverse,
    compact21,calculate as calculate_SM66)

N=25
P=ANCHOR
R=REM
GRID=(F(1,8),F(1,4),F(1,2),F(1),F(2),F(4),F(8))

def sym(A):return all(A[i][j]==A[j][i] for i in range(len(A)) for j in range(len(A)))
def matmul(A,B):
    assert len(A)>0 and len(B)>0 and len(A[0])==len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A):return [list(row) for row in zip(*A)]
def counts(x):return {"positive":x[0],"negative":x[1],"zero":x[2]}
def result_from_inertia(A):
    assert sym(A)
    x=exact_inertia_general(A)
    assert sum(x)==len(A)
    return counts(x)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm67_original_actual_21D_coupled_psd_covariance_schur.json")
    args=p.parse_args()
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in ledger["obligations"] if x["id"]=="W-ODD-NEG")
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert ledger["objective"]["status"]==odd["status"]=="open"
    assert ledger["governance"]["no_automatic_promotion"]
    assert all(k in odd["evidence"] for k in ("SM58","SM62","SM64","SM65","SM66","SM67"))
    # Reconstruct the original physical 25D true Loewner enclosure
    # rather than trusting a stale report or an unchecked estimate.
    replay_sm65()
    source=json.loads((ROOT/"artifacts/sm65_original_actual_22D_Schur_anisotropic.json").read_text())
    assert source["status"]=="SCOPED_ACTUAL_ORIGINAL_22D_SIGNED_SCHUR_ANISOTROPIC_LOWER_NO_POSITIVITY"
    assert source["verified_original_SM58_negative_and_signed_all625_replay"]
    assert source["verified_original_SM62_complete_signed_all625_replay"]
    assert source["verified_original_SM63_direct_positive_3x3_replay"]
    assert source["original_source_count"]==25
    L=[[F(s) for s in row] for row in source["true_original_25source_complete_signed_LOWER_rational"]]
    E=[[F(s) for s in row] for row in source["true_original_25source_two_sided_difference_UPPER_matrix"]]
    assert len(L)==len(E)==25
    assert all(len(row)==25 for row in L+E)
    assert sym(L) and sym(E)
    assert hash_matrix(L)==SM62_HASH
    assert [E[i][i] for i in range(N)]==[
        F(s) for s in source["true_original_25source_two_sided_difference_upper_diagonal"]]
    # E=U-L>=0 follows mathematically from L<=Q<=U; exact 25D
    # rational inertia check guards the registered source replay.
    einertia=result_from_inertia(E)
    assert einertia["negative"]==0 and einertia["zero"]==0
    A64=[[F(x) for x in row] for row in SM64_A_STR]
    assert hash_matrix(A64)==SM64_SHA256
    Ainv,positive_pivots=exact_inverse(A64)
    assert min(positive_pivots)>0
    assert len(P)==4 and len(R)==21 and len(set(P+R))==N
    Epp=[[E[i][j] for j in P] for i in P]
    Err=[[E[i][j] for j in R] for i in R]
    Lpr=[[L[i][j] for j in R] for i in P]
    Lrp=transpose(Lpr)
    Lrr=[[L[i][j] for j in R] for i in R]
    assert sym(Epp) and sym(Err) and sym(Lrr)
    assert result_from_inertia(Epp)["negative"]==0
    assert result_from_inertia(Err)["negative"]==0
    # Nonnegative EXACT original full-covariance trace.
    sigma=sum((Ainv[i][j]*Epp[j][i] for i in range(4) for j in range(4)),F(0))
    assert sigma>0
    # PSD source P=L_RP A64^-1 L_PR, never a diagonal envelope.
    full_p=matmul(matmul(Lrp,Ainv),Lpr)
    assert sym(full_p)
    assert result_from_inertia(full_p)["negative"]==0
    # Independent exact diagonal comparator from SM66 on the SAME
    # FOUR-positive source anchor, no dissimilar threeplane schemes.
    old=calculate_SM66(source)
    assert old["status"]=="SCOPED_ACTUAL_ORIGINAL_21D_SIGNED_SCHUR_FOUR_SOURCE_EXACT_INVERSE"
    D=[F(s) for s in old["actual_21D_full_inverse_anisotropic_schur_penalty"]]
    assert len(D)==21 and all(d>=0 for d in D)
    options=[]
    for t in GRID:
        a=F(1)+t
        b=F(1)+F(1)/t
        W=[[a*full_p[i][j]+b*sigma*Err[i][j]
            for j in range(21)] for i in range(21)]
        assert sym(W)
        winertia=result_from_inertia(W)
        assert winertia["negative"]==0
        # Loewner matrix penalty comparator: old diagonal minus
        # true coupled PSD penalty; full 441 entries and inertia.
        difference=[[(D[i] if i==j else F(0))-W[i][j]
                     for j in range(21)] for i in range(21)]
        dom=result_from_inertia(difference)
        coupled_dominates_old=dom["negative"]==0
        raw=[[Lrr[i][j]-W[i][j] for j in range(21)]
             for i in range(21)]
        S,fee=compact21(raw)
        inert=result_from_inertia(S)
        options.append({
            "young_parameter":str(t),
            "true_full_coupled_21D_penalty_matrix_PSD":True,
            "full_coupled_penalty_exact_trace":str(sum(W[i][i] for i in range(21))),
            "old_exact_inverse_diagonal_penalty_trace":str(sum(D)),
            "coupled_upper_dominated_by_exact_inverse_diagonal_Loewner":coupled_dominates_old,
            "coupled_vs_exact_diagonal_difference_inertia":dom,
            "true_actual_21D_Schur_LOWER_inertia":inert,
            "source21_symmetric_outward_rational_compaction_fee":str(fee),
            "true_actual_21D_signed_Schur_LOWER":[[str(x) for x in row] for row in S]
        })
    best=min(options,key=lambda x:(x["true_actual_21D_Schur_LOWER_inertia"]["negative"],
               F(x["full_coupled_penalty_exact_trace"])))
    # Numerical lower inertia is reference-only, NEVER an actual
    # original signed negative witness, even if fully negative.
    out={
       "status":"SCOPED_ORIGINAL_ACTUAL_21D_SIGNED_SCHUR_FULL_COUPLED_PSD_COVARIANCE_UPPER",
       "canonical_W_ODD_NEG":"OPEN",
       "verified_original_SM65_true_complete_25D_two_sided_replay":True,
       "verified_original_SM62_true_full_25D_signed_lower_SHA256":SM62_HASH,
       "verified_original_SM64_true_positive_4x4_signed_anchor_SHA256":SM64_SHA256,
       "verified_original_SM64_actions_run":39323057878,
       "true_original_full25_error_covariance_exact_inertia":einertia,
       "true_positive_anchor_original_source_indices":list(P),
       "original_complement_real_source_indices":list(R),
       "true_actual_original_signed_cross_coefficients_covered":84,
       "positive_anchor_full_exact_inverse_four_pivots":[str(x) for x in positive_pivots],
       "positive_anchor_covariance_trace_sigma":str(sigma),
       "source_positive_anchor_lower_complete_4x4_inverse_verified":True,
       "complete_original_signed_21D_psd_covariance_majorization":True,
       "original_covariance_21x21_offdiagonal_entries_retained":441,
       "original_old_exact_inverse_diagonal_source21_penalties_reproduced":True,
       "tested_all_rational_Young_parameters":[str(x) for x in GRID],
       "all_true_full_coupled_Schur_lower_options":[
             {k:v for k,v in option.items() if k!="true_actual_21D_signed_Schur_LOWER"}
             for option in options],
       "best_parameter":best["young_parameter"],
       "best_true_signed_Schur_lower_21D_rational":best["true_actual_21D_signed_Schur_LOWER"],
       "best_lower_rational_21D_reference_inertia":best["true_actual_21D_Schur_LOWER_inertia"],
       "best_coupled_penalty_truly_Loewner_dominated_by_old_diagonal":
             best["coupled_upper_dominated_by_exact_inverse_diagonal_Loewner"],
       "verified_original_ACTUAL_25D_signed_negative_index_upper_SM64":21,
       "ACTUAL_source21_Schur_PSD_certified":False,
       "ACTUAL_source21_Schur_negative_index_exactly_classified":False,
       "complete_original_infinite_odd_negative_index_classified":False,
       "original_470_Astar_inverse_strong_orthogonal_remainder":False,
       "original_odd_O1O2_even_Weil_CC27_RH":False,
       "independent_original_Fourier_closed_domain_premise_audit":"OPEN",
       "interpretation":"Exact original full covariance E_RR and actual source25 PSD 0<=Q-L<=E give coupled matrix B^T Aactual^-1 B upper without independent 84 absolute row inflation. All negative lower directions are reference-only; complete infinite original odd/even Weil/RH still OPEN."
    }
    path=ROOT/args.output
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("SM67 TRUE complete PSD-coupled original source21 Schur:",json.dumps({
       "sigma":str(sigma),
       "tested_parameters":len(options),
       "best_parameter":best["young_parameter"],
       "best_lower_negative_inertia":best["true_actual_21D_Schur_LOWER_inertia"]["negative"],
       "actual_full_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
