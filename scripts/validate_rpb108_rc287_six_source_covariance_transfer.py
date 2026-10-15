"""RC287: unchanged six trial centers and a rigorous covariance-transfer gap.

Mathematical scope: algebraic transfer identities and a *failed sufficient*
global-inverse comparison for the RC280 six-mode positive block. These
negative lower envelopes are NOT actual negative witnesses.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F

ROOT=Path(__file__).resolve().parents[1]
SCALE=10**20
PINS={
 "certificates/rpb108_rc280_combined_jump_tail.json":"bb0dd3f6174761037ed0f20f17177ddad5749227",
 "certificates/rpb108_rc278_smaller_positive_reference.json":"edc59d6cec516d597c2c7816bec2a38a2677e18d",
 "certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc286_full_cross_payment.json":"bbcbe94608550c4fcb9df21dae8b2cf0d81a76c1"
}

def down(x):return F(x.numerator*SCALE//x.denominator,SCALE)
def up(x):return -down(-x)

def controls():
    # D<=G_old<=nu D and G_new>=mu D entail
    # G_new^-1 <= (nu/mu) G_old^-1 by genuine inverse Loewner order.
    # Full Schur coupling can overturn two individually positive blocks.
    W=[[F(3),F(1)],[F(1),F(3)]]
    det=W[0][0]*W[1][1]-W[0][1]**2
    assert det>0
    inv=[[W[1][1]/det,-W[0][1]/det],[-W[1][0]/det,W[0][0]/det]]
    assert inv[0][0]>0 and inv[0][1]!=0
    A=[[F(1),F(2)],[F(2),F(1)]]
    assert A[0][0]>0 and A[1][1]>0 and A[0][0]*A[1][1]-A[0][1]**2<0
    return True

def run(reverse=False):
    data={}
    for path,pin in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        digest=hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()
        assert digest==pin,("pin",path)
        data[path]=json.loads(raw)
    def get(k):return data["certificates/rpb108_rc"+k+".json"]
    old=get("280_combined_jump_tail")
    refs=get("278_smaller_positive_reference")
    reduced=get("283_reduced_reference")
    passed=get("286_full_cross_payment")
    assert old["positive_auxiliary_block_dimension"]==5
    assert refs["new_reference_rank"]==reduced["old_reference_rank"]==371
    assert reduced["proposed_buffered_reference_rank"]==317
    assert passed["new_rank317_positive_source_pivots"]==2
    assert passed["new_rank317_remaining_coupled_Schur_dimension"]==315
    assert not old["Stage_I_closed"] and not passed["Stage_I_closed"]
    assert controls()
    rows=[]
    for base in range(2):
        source=old["combined_jump_tail_gate_certificates"][base]
        original=refs["smaller_reference_certificates"][base]
        new=reduced["reduced_reference_options"][base]
        parity=("even","odd")[base]
        assert source["parity"]==original["parity"]==new["parity"]==parity
        lam=F(original["augmentation_coefficient"])
        nu=F(original["full_D_reference_upper"])
        floor=F(source["positive_block_native_floor_lower"])
        assert floor>0 and lam>0 and nu>0
        modes=source["positive_block_degrees"]
        assert modes==([0,4] if base==0 else [1,3,5])
        pivots=[(k-base)//2 for k in modes]
        for trial in source["combined_trial_tail_certificates"]:
            coeff=[F(x) for x in trial["exact_trial_Legendre_coefficients"]]
            assert len(coeff)==65
            assert all(not c or n%2==base for n,c in enumerate(coeff))
        threshold=down(floor/lam)
        assert threshold>0
        options=[]
        for option in new["reduced_reference_options"]:
            newrank=option["new_low_reference_rank"]
            first=option["first_discarded_matching_degree"]
            mu=F(option["certified_D_reference_floor_lower"])
            assert first>65 and mu>0 and nu>mu
            # Every six old rational trial polynomials belongs to the
            # new physical projection, hence its exact augmented action
            # and variational center are the same as under the old ref.
            kappa=nu/mu
            diags=[]
            for j,mode in zip(pivots,modes):
                oldg=F(source["actual_native_gate_Loewner_lower"][j][j])
                s=F(source["complete_inverse_residual_covariance_upper"][j][j])
                assert oldg>0 and s>0
                # Old residual covariance E_old <= S; the unchanged
                # actual residual under new inverse obeys E_new<=kappa*S.
                # K_new >= L_old -lam*(kappa-1)*S as a MATRIX.
                # This scalar diagonal of the lower matrix is negative.
                coarse=oldg-lam*(kappa-1)*s
                assert coarse<0
                diags.append(dict(
                    mode=mode,
                    old_gate_diagonal_lower=str(down(oldg)),
                    old_inverse_covariance_diagonal_upper=str(up(s)),
                    coarse_new_gate_diagonal_lower=str(down(coarse)),
                ))
            options.append(dict(
                new_reference_rank=newrank,
                global_reference_D_lower=str(down(mu)),
                global_reference_D_upper=str(up(nu)),
                coarse_inverse_comparison_factor_upper=str(up(kappa)),
                selected_legacy_positive_pivot_diagonals=diags,
                all_coarse_new_pivot_diagonal_lowers_negative=True,
                entire_new_positive_block_established=False,
            ))
        rows.append(dict(
            parity=parity,
            old_positive_source_modes=modes,
            original_old_gate_native_floor_lower=str(down(floor)),
            augmentation_coefficient=str(lam),
            strict_added_residual_covariance_identity_budget_native_Loewner=str(threshold),
            old_complete_inverse_covariance_psd_pinned=True,
            all_trial_polynomials_supported_in_new_reference=True,
            old_variational_center_gram_invariant=True,
            old_actual_residual_vectors_invariant=True,
            new_inverse_covariance_not_invariant=True,
            reduced_reference_diagnostics=options
        ))
    return dict(
        milestone="RC287",
        starting_commit="023801851ee560e09878e6af2d50faf615dcb439",
        input_git_blob_pins=PINS,
        legacy_six_trial_center_invariance_certified=True,
        full_new_317_source_covariance_reconstructed=False,
        old_positive_pivots_not_transferred=True,
        global_spectral_comparison_insufficient_for_six_mode_joint_positivity=True,
        exact_covariance_transfer_obligation="E_new <= S_old + Delta with 0 <= Delta < floor_old/lambda * I on the old certified positive source subset",
        parity_transfer_audits=rows,
        rank317_P0_P1_pivots_from_RC285_preserved=True,
        rank317_P0_P1_cross_payment_from_RC286_preserved=True,
        rank317_remaining_Schur_dimension=315,
        Stage_I_closed=False,F4=False,RH=False,Lean=False,
        next_cursor="RC288: recalculate degree-localized complete 3x3 residual covariance under rank-317 W, or optimize new mixed trials; old centers and original action inputs may be reused but old inverse covariance cannot."
    )

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True,type=Path)
    ap.add_argument("--replay",action="store_true")
    args=ap.parse_args()
    output=run(args.replay)
    if args.replay:
        assert output==json.loads(args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(output,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("RC287 VALIDATED: six trial centers invariant; global covariance "
          "transfer inconclusive; Stage I OPEN",flush=True)
