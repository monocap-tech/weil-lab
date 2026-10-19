#!/usr/bin/env python3
"""SM60: original 23D complement lower-reference NO-GO, exact rational.

The verified SM58 full original 25-physical-source signed Loewner LOWER
has one positive and 24 negative pivots. SM59A independently proves
that the ACTUAL source-restricted signed Wodd has a strictly positive
2-plane P2=span(original supported g2,g17) and hence actual source
negative index <=23, NOT that SM58 is positive on P2.

SM60 reconstructs the ORIGINAL SM58 coupled 25x25 signed LOWER from
the exact full SI10 973-leaf Fourier UPPER, original SM47+49
positive-LOW and true SM42 exceptional pole UPPER. It REQUIRES a
byte-for-byte canonical 625-entry SHA256 replay against original
passing SM58 Actions 39281588617.

In coefficient basis V25=P2 plus the remaining 23 genuine physical
original source coordinates {0,..,24}\{2,17}, take the 23x23
principal compression of the SM58 signed LOWER. Check, with exact
fractions only, the 23 successive negative LDL (no pivoting) Schur
pivots of this REFERENCE compression. This proves that this specific
lower reference is STRICTLY NEGATIVE definite on all 23 remaining
coordinate directions. It emphatically DOES NOT say that the TRUE
signed quadratic form, its true Schur complement C-B^T A^-1 B,
or the infinite odd operator are negative: Q_actual >= L_reference.

This is a method NO-GO: SM58's 25x25 lower cannot itself certify
positivity of ANY nonzero direction of this 23-dimensional coordinate
complement. New true signed cross and complement estimates are
obligatory; never splice the sharper SM52 positive 2x2 into the
full lower without controlling all off-diagonal blocks.

Original complete source-eliminated odd W-ODD-NEG O1/O2, 470 source
Astar strong inverse/orthogonal remainder, even, Weil, CC27/RH OPEN.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from validate_rpb108_sm43_positive_cell_envelope import ROOT,original_source_centered_windows
from validate_rpb108_sm42_original_physical_gram_and_low_gate import original_full_25_physical_interval_gram
from validate_rpb108_sm57_original_25source_negative_upper import (
    original_positive_low_25,pole_outer_upper,
    outward_compact_matrix,exact_symmetric_25source_inertia)
from validate_rpb108_sm58_original_coupled_25negative import original_complete_coupled_negative

N=25
ANCHOR=(2,17)
REM=tuple(i for i in range(N) if i not in ANCHOR)

def fingerprint(M):
    return hashlib.sha256(json.dumps(
        [[str(x) for x in row] for row in M],
        separators=(",",":"),ensure_ascii=True
    ).encode("utf-8")).hexdigest()

def strict_negative_LDL(M):
    """Negative definiteness iff every non-pivoted symmetric LDL
    scalar pivot of this ordered rational matrix is strictly negative.
    """
    n=len(M)
    assert n==23 and all(len(row)==n for row in M)
    a=[row[:] for row in M]
    pivots=[]
    for k in range(n):
        assert all(a[i][j]==a[j][i] for i in range(k,n) for j in range(k,n))
        p=a[k][k]
        # NO negative determinant or eigenvalue is inferred for Q_actual.
        assert p<0, ("SM58 23D LOWER reference no-go cannot be certified",k)
        pivots.append(p)
        for i in range(k+1,n):
            for j in range(i,n):
                # exact fraction congruence / negative LDL pivot
                a[i][j]-=a[i][k]*a[j][k]/p
                a[j][i]=a[i][j]
    assert len(pivots)==23 and max(pivots)<0
    return pivots

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default="artifacts/sm60_original_23source_complement_lower_nogo.json")
    args=parser.parse_args()
    obligations=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in obligations["obligations"] if x["id"]=="W-ODD-NEG")
    assert obligations["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==obligations["objective"]["status"]=="open"
    assert obligations["governance"]["no_automatic_promotion"]
    assert all(z in odd["evidence"] for z in ("SM52","SM57","SM58","SM59","SM60"))
    pin=json.loads((ROOT/"certificates/rpb108_sm58_full25_signed_summary.json").read_text())
    assert pin["actions_run_id"]==39281588617
    assert pin["artifact_id"]==12201213066
    assert pin["original_25x25_signed_lower_inertia_for_each_diagonal_mix"]["0"]=={
        "positive":1,"negative":24,"zero":0
    }
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==25 and sources[24][0]=="pole"
    assert sources[2][0]==sources[17][0]=="cluster"
    assert sources[2][2]==0 and sources[17][2]==1
    assert centers[sources[2][1]]==centers[sources[17][1]]==F(1845,128)
    G,actual,pole=original_full_25_physical_interval_gram()
    assert sources==actual
    U,stats=original_complete_coupled_negative(centers,sources)
    assert stats["whole_original_negative_frequency_leaves"]==973
    assert fingerprint(U)==pin["original_full25_coupled_negative_upper_all_625_entries_sha256"]
    P,pp=original_positive_low_25(centers,sources,G)
    pole_upper,pole_err=pole_outer_upper(G)
    exact=[[P[i][j]-U[i][j]-pole_upper[i][j]
            for j in range(N)] for i in range(N)]
    L,outward=outward_compact_matrix(exact)
    assert fingerprint(L)==pin["original_full25_signed_lower_all_625_entries_sha256"]
    inertia=exact_symmetric_25source_inertia(L)
    assert {k:inertia[k] for k in ("positive","negative","zero")}=={
        "positive":1,"negative":24,"zero":0}
    R=[[L[i][j] for j in REM] for i in REM]
    pivots=strict_negative_LDL(R)
    # The true Q restricted to this 23D coordinate subspace
    # is ABOVE R. Negative R does not imply Q is negative.
    out={
      "status":"CERTIFIED_ORIGINAL_23SOURCE_REFERENCE_LOWER_NEGATIVE_DEFINITE_NOGO_ONLY",
      "canonical_W_ODD_NEG":"OPEN",
      "physical_original_source_count":25,
      "actual_true_signed_positive_plane_original_indices":list(ANCHOR),
      "remaining_original_coordinate_source_indices":list(REM),
      "remaining_coordinate_dimension":23,
      "verified_SM58_Actions_id":39281588617,
      "all_625_entire_original_negative_UPPER_entries_exact_replay":True,
      "all_625_original_signed_LOWER_entries_exact_replay":True,
      "complete_SM58_original_lower_inertia":inertia,
      "23D_original_signed_LOWER_REFERENCE_exact_negative_LDL_pivots":[str(x) for x in pivots],
      "23D_original_signed_LOWER_REFERENCE_strict_negative_definite":True,
      "23D_original_signed_LOWER_REFERENCE_positive_directions":0,
      "23D_ACTUAL_original_signed_complement_negative_definite_proved":False,
      "23D_ACTUAL_original_signed_complement_positive_proved":False,
      "23D_ACTUAL_signed_Schur_complement_C_minus_Bt_Ainverse_B_certified":False,
      "actual_original_25D_source_negative_index_upper_SM59A":23,
      "actual_original_25D_source_negative_index_EXACTLY_classified":False,
      "complete_original_infinite_odd_negative_index_classified":False,
      "complete_original_470_Astar_inverse_orthogonal_remainder":False,
      "original_odd_O1O2_even_Weil_CC27_RH":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "next_original_complete_operator_acceptance":"Certify ACTUAL original signed 23x23 Schur remainder with original physical source coupling B,C and positive 2-plane A (do not splice two Loewner lower blocks); then entire infinite original 470-source/orthogonal remainder."
    }
    target=ROOT/args.output
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+"\n")
    print("SM60 original 23source signed LOWER reference no-go:",json.dumps({
       "all_625_entry_SM58_replay":True,
       "complement_lower_reference_inertia":{"negative":23,"positive":0,"zero":0},
       "max_exact_negative_LDL_pivot_approx":float(max(pivots)),
       "ACTUAL_23source_negative_index":"UNKNOWN",
       "ACTUAL_original_25D_negative_index_upper":23,
       "full_original_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
