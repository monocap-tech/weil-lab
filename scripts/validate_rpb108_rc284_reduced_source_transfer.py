"""RC284: paid transfer enclosure for native low sources under the reduced reference.

The trial and residual are exactly unchanged for RC278's P0/P1 low-degree
polynomials. The INVERSE changes. Reweight inherited low-mode energies and
pay the remaining model globally to certify conservative original-source
response bounds for the rank-301/317/334 positive references.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
B = F(11, 10)
PINS = {
    "certificates/rpb108_rc129_four_vector_joint_moment.json": "33e681e688450c987993603354544fe3919b435f",
    "certificates/rpb108_rc278_smaller_positive_reference.json": "edc59d6cec516d597c2c7816bec2a38a2677e18d",
    "certificates/rpb108_rc283_reduced_reference.json": "1dc4bba375af6bfd7a274fccc07638e0eead56e6",
    "notes/RPB108_RC283_REDUCED_REFERENCE_20261014.md": "b1fac0c448719c6afd49bebb84505bf86f430253",
}
SCALE = 10 ** 20
YOUNG = F(1, 100)
TARGETS = [F(1, 10**6), F(1, 10**12)]


def down(x):
    return F(x.numerator * SCALE // x.denominator, SCALE)


def up(x):
    return -down(-x)


def chebyshev_budget(mu, nu, tolerance):
    """Valid D-normalized inverse polynomial bound, NOT executed actions.

    For positive selfadjoint A in [mu,nu], degree k-1 Chebyshev inverse
    approximant has operator error <= 2*q**k/mu, where
    q=(sqrt(kappa)-1)/(sqrt(kappa)+1). Replacing sqrt(kappa) with a
    larger *integer* gives an exact rational upper bound on q.
    """
    assert 0 < mu <= nu and tolerance > 0
    t = 1
    while mu * t * t < nu:
        t += 1
    assert mu * (t - 1)**2 < nu <= mu * t * t
    q = F(t - 1, t + 1)
    k = 1
    while 2 * q**k > mu * tolerance:
        k *= 2
    lower, upper = k//2, k
    while lower+1 < upper:
        m = (lower+upper)//2
        if 2*q**m <= mu*tolerance:
            upper=m
        else:
            lower=m
    k=upper
    assert 2*q**k <= mu*tolerance
    if k>1:
        assert 2*q**(k-1) > mu*tolerance
    return {
        "requested_absolute_D_inverse_operator_error": str(tolerance),
        "integer_upper_sqrt_condition": t,
        "rational_chebyshev_q_upper": str(q),
        "sufficient_inverse_polynomial_degree": k-1,
        "certified_absolute_error_upper": str(up(2*q**k/mu)),
        "polynomial_actions_executed": False,
    }


def checks():
    # A projection change supported on an orthogonal high coordinate
    # leaves a trial and its exact residual unchanged; inverse may change.
    G0 = [[F(3), F(1)], [F(1), F(2)]]
    lam = F(2)
    new = [[G0[0][0]+lam, G0[0][1]], [G0[1][0],G0[1][1]]]
    old = [[G0[0][0]+lam, G0[0][1]], [G0[1][0],G0[1][1]+lam]]
    z = [F(1, 3), F(0)]
    u = [F(1), F(0)]
    mult = lambda A,x:[sum(v*w for v,w in zip(row,x)) for row in A]
    assert mult(old,z)==mult(new,z)
    e=[u[i]-mult(new,z)[i] for i in range(2)]
    assert e==[u[i]-mult(old,z)[i] for i in range(2)]
    # A conservative weighted bound can fail to certify a positive gate
    # without producing a negative eigenvalue or an actual witness.
    assert old!=new
    return {"unchanged_supported_trial_action_and_residual_checked": True,
            "changed_inverse_not_identified_with_old_inverse": True}


def run(reverse=False):
    data={}
    for path,sha in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        actual=hashlib.sha1(
            b"blob "+str(len(raw)).encode()+bytes([0])+raw
        ).hexdigest()
        assert actual==sha,(path,"pin")
        if path.endswith(".json"):
            data[path]=json.loads(raw)
    metric=data["certificates/rpb108_rc129_four_vector_joint_moment.json"]
    old=data["certificates/rpb108_rc278_smaller_positive_reference.json"]
    reduced=data["certificates/rpb108_rc283_reduced_reference.json"]
    slo=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
    shi=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0<slo<=shi and old["new_reference_rank"]==371
    assert reduced["proposed_buffered_reference_rank"]==317
    assert not old["Stage_I_closed"] and not reduced["Stage_I_closed"]
    H=[F(0)]
    for n in range(1,460):
        H.append(H[-1]+F(1,n))
    rows=[]
    for base,(r,options) in enumerate(zip(
        old["smaller_reference_certificates"],
        reduced["reduced_reference_options"]
    )):
        parity=["even","odd"][base]
        assert r["parity"]==options["parity"]==parity
        lam=F(r["augmentation_coefficient"])
        z=list(map(F,r["exact_trial_Legendre_coefficients"]))
        assert len(z)==65 and z[base]!=0
        for n,c in enumerate(z):
            assert c==0 or n%2==base
        # As all new smaller projectors contain degree <=64,
        # (G_old-G_new)Z=0 exactly for the inherited trial.
        centers=r["retained_low_residual_certificate"]
        assert len(centers)==65
        lower_energy=F(0);upper_energy=F(0)
        for n,v in enumerate(centers):
            assert v["degree"]==n
            c=F(v["residual_center"])
            mass=2*B/F(2*n+1)
            lower_energy+=mass*(H[n]+slo)*c*c
            upper_energy+=mass*(H[n]+shi)*c*c
        lowlo=down(lower_energy);lowhi=up(upper_energy)
        M=F(r["complete_model_weighted_inverse_energy_upper"])
        assert 0<lowlo<=lowhi<M
        highbudget=M-lowlo
        assert highbudget>0
        globalfault=F(r["remaining_global_D_fault_norm_upper"])
        rounding=F(r["weighted_source_and_center_rounding_energy_upper"])
        source_mass=F(r["native_auxiliary_source_mass"])
        source_center_high=F(r["variational_inverse_center_upper"])
        upper_reference=F(r["full_D_reference_upper"])
        candidates=[]
        for choice in options["reduced_reference_options"]:
            mu=F(choice["certified_D_reference_floor_lower"])
            first=choice["first_discarded_matching_degree"]
            assert first>65 and 0<mu<1
            assert len([n for n in range(base,first,2)])==choice["new_low_reference_rank"]
            # For n<65, both W_old and W_new have weight D_n.
            # For all other n, W_new>=mu D and W_old<=D.
            # Old M bounds all W_old^-1 model energy. Therefore
            # M_new <= lowhi+(M-lowlo)/mu (full infinite tail included).
            newmodel=up(lowhi+highbudget/mu)
            fault=up(globalfault*globalfault/mu)
            # Rounding is supported in n<=64 and hence unchanged.
            # With sqrt(a)+sqrt(b)+sqrt(c), apply matrix-free Young:
            # (sum)^2 <= (1+eta)a +2(1+1/eta)(b+c).
            correction=up((1+YOUNG)*newmodel+
                          2*(1+1/YOUNG)*(rounding+fault))
            responsehi=up(source_center_high+correction)
            pivotlo=down(source_mass-lam*responsehi)
            choicesbudget=[
                chebyshev_budget(mu,upper_reference,t) for t in TARGETS
            ]
            candidates.append({
                "new_reference_rank":choice["new_low_reference_rank"],
                "first_omitted_degree":first,
                "global_reference_D_floor_lower":str(mu),
                "global_reference_D_upper":str(upper_reference),
                "new_complete_model_inverse_correction_upper":str(newmodel),
                "new_global_fault_inverse_payment_upper":str(fault),
                "new_total_inverse_correction_upper":str(correction),
                "actual_source_inverse_response_upper":str(responsehi),
                "actual_native_source_gate_lower":str(pivotlo),
                "positive_native_source_certified":pivotlo>0,
                "conditional_exact_action_budgets":choicesbudget,
            })
        rows.append({
            "parity":parity,"source":"P"+str(base),
            "inherited_original_trial_support_max_degree":64,
            "same_trial_and_actual_residual_under_reduced_reference":True,
            "variational_center_unchanged":True,
            "low_center_old_model_energy_lower":str(lowlo),
            "low_center_old_model_energy_upper":str(lowhi),
            "complete_inherited_old_model_upper":str(M),
            "entire_high_model_energy_budget_old_weighted_upper":str(highbudget),
            "low_center_rounding_energy_upper":str(rounding),
            "new_reference_response_enclosures":candidates
        })
    return {
        "milestone":"RC284",
        "starting_commit":"3651ac3a8f82d8f9357416a61d206dcb8b286232",
        "input_git_blob_pins":PINS,
        "certified_source_response_transfer":rows,
        "exact_controls":checks(),
        "full_global_prime_and_endpoint_tails_paid_via_RC278":True,
        "all_new_augmentation_action_inherited_on_supported_trials":True,
        "full_rank317_source_response_matrix_evaluated":False,
        "new_original_Weil_actions_performed":False,
        "positive_rank317_gate_certified":False,
        "Stage_I_closed":False,"RH":False,"F4":False,"Lean":False,
        "next_cursor":"RC285: replace coarse (M-low)/mu payment by degree-localized "
                      "RC274 residual shells under the rank-317 W weights; "
                      "recompute source gates then extend correlated trials."
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--replay",action="store_true")
    args=parser.parse_args()
    result=run(args.replay)
    if args.replay:
        assert result==json.loads(args.output.read_text())
    else:
        args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("RC284 VALIDATED: paid reduced-reference P0/P1 enclosures; "
          "positive source gate still OPEN",flush=True)
