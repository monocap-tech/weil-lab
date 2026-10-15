"""RC286: full P0/P1 cross-column Schur payment in reduced 301/317/334 references.

Bound the coupling to every other same-parity Legendre source using RC285's
paid G-inverse residual energy and RC278's exact rational trial coefficients.
No remaining principal-block positivity is asserted.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
THETA=F(3)
SCALE=10**20
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc278_smaller_positive_reference.json":"edc59d6cec516d597c2c7816bec2a38a2677e18d",
 "certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc285_degree_localized_transfer.json":"d2bee8272c341e571dedb1aa436bdca88b675c46",
 "notes/RPB108_RC285_DEGREE_LOCALIZED_TRANSFER_20261014.md":"cc17c9b3f9fecfdff0885d9ec30c57e0997c9d3f"
}
TARGETS={1:(F(4,5),F(3,4)),2:(F(3,4),F(2,3))}

def down(x):
    return F(x.numerator*SCALE//x.denominator,SCALE)

def up(x):
    return -down(-x)

def controls():
    # Subunit Schur payment is not positivity of an unknown principal block.
    gamma=F(1,4);cross=F(1,8);principal=F(0)
    assert 0<cross*cross/gamma<F(1)
    assert gamma*principal-cross*cross<0
    # Scalar matrix Young estimates the norm of the sum of center and
    # unknown projected inverse response without independence assumptions.
    a,b=F(1,5),F(2,7)
    assert (a+b)**2 <= (1+THETA)*a*a+(1+1/THETA)*b*b
    return {"subunit_cross_payment_not_full_Schur_positivity":True,
            "matrix_Young_amplitude_bound_checked":True}

def run(reverse=False):
    data={}
    for path,sha in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()==sha,("pin",path)
        if path.endswith(".json"):data[path]=json.loads(raw)
    def get(k):return data["certificates/rpb108_rc"+k+".json"]
    moment=get("129_four_vector_joint_moment")
    legacy=get("278_smaller_positive_reference")
    refs=get("283_reduced_reference")
    sources=get("285_degree_localized_transfer")
    slo=F(moment["actual_D_Gram_entry_lower"][0][0])/(2*B)
    shi=F(moment["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0<slo<=shi
    assert legacy["new_reference_rank"]==371
    assert refs["proposed_buffered_reference_rank"]==317
    assert sources["Stage_I_closed"] is False
    rows=[]
    for base in range(2):
        r=legacy["smaller_reference_certificates"][base]
        cut=refs["reduced_reference_options"][base]
        paid=sources["degree_localized_original_source_certificates"][base]
        parity=("even","odd")[base]
        assert r["parity"]==cut["parity"]==paid["parity"]==parity
        assert paid["source"]=="P"+str(base)
        z=[F(x) for x in r["exact_trial_Legendre_coefficients"]]
        assert len(z)==65 and z[base]!=0
        assert all(a==0 or j%2==base for j,a in enumerate(z))
        lam=F(r["augmentation_coefficient"])
        first=base+2
        dmin=down((F(3,2) if base==0 else F(11,6))+slo)
        assert dmin>0
        # The exact mass-normalized R-projection of the trial center:
        # ||P_R Z||^2 = sum_{j != base} m_j z_j^2.
        # All 65 trial degrees belong to every reduced reference.
        terms=[up(2*B*v*v/F(2*j+1)) for j,v in enumerate(z) if j!=base]
        if reverse:terms.reverse()
        center=up(sum(terms,F(0)))
        assert center>0
        models=[]
        for idx,(choice,gated) in enumerate(zip(
                cut["reduced_reference_options"],paid["parity_certificates"])):
            rank=choice["new_low_reference_rank"]
            assert gated["rank"]==rank
            assert choice["first_discarded_matching_degree"]>65
            assert choice["new_low_reference_rank"]-1>0
            gamma=F(gated["native_gate_lower"])
            q=F(gated["complete_original_inverse_residual_correction_upper"])
            assert gamma>0 and q>0 and gated["positive_native_pivot_certified"]
            # Let X=G_new^-1 D e, q >= <X,G_new X>.
            # G_new >= D on ALL retained Legendre directions, hence
            # ||P_R X||_physical^2 <= q / (H_first+s_lower).
            noise=up(q/dmin)
            # For the actual new auxiliary matrix K=Mass-lambda U*G^-1 U,
            # C_j=-lambda <P_j, Z+X>_physical. Cauchy/Young with
            # Gamma>=gamma gives the full remaining-range Mass bound.
            cost=up(lam*lam*((1+THETA)*center+
                         (1+1/THETA)*noise)/gamma)
            target=TARGETS.get(idx)
            goal=target[base] if target else None
            if goal is not None:
                assert 0<cost<goal<1
            models.append(dict(
                new_reference_rank=rank,
                positive_source_gate_native_lower=str(gamma),
                complete_source_inverse_correction_upper=str(q),
                remaining_auxiliary_dimension=rank-1,
                complete_trial_center_projection_mass_squared_upper=str(center),
                complete_inverse_residual_remainder_physical_mass_squared_upper=str(noise),
                entire_cross_Schur_payment_native_mass_strict_upper=str(cost),
                certificate_less_than_one=cost<1,
                rational_subunit_target=str(goal) if goal is not None else None,
                strict_target_pass=cost<goal if goal is not None else False))
        rows.append(dict(
            parity=parity,source="P"+str(base),
            first_remaining_Legendre_degree=first,
            retained_D_native_weight_lower=str(dmin),
            augmentation_coefficient=r["augmentation_coefficient"],
            Young_parameter=str(THETA),
            all_remaining_cross_columns_treated_collectively=True,
            source_response_certificates=models))
    controls()
    return dict(
        milestone="RC286",
        parent="be65d328ef63d6ac8ddf990d30af7d07c6ad94c8",
        input_git_blob_pins=PINS,
        new_rank317_positive_source_pivots=2,
        new_rank317_remaining_coupled_Schur_dimension=315,
        full_cross_column_Schur_payment_certificates=rows,
        opposite_parity_cross_exact_zero=True,
        all_same_parity_remaining_cross_columns_paid=True,
        remaining_315_principal_gate_certified_positive=False,
        new_original_Weil_actions_performed=False,
        Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor="RC287: establish the positive lower envelope for the remaining rank-317 principal gate or rebuild same-parity 3-source covariance; subunit cross payments alone do not close positivity."
    )

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--replay",action="store_true")
    args=parser.parse_args()
    result=run(reverse=args.replay)
    if args.replay:
        assert result==json.loads(args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("RC286 VALIDATED: whole remaining-range P0/P1 cross payments, "
          "full Schur gate OPEN",flush=True)
