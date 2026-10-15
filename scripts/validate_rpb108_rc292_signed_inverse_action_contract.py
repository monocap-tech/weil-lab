"""RC292: exact action-budget contract for certifying signed P0 and soft P4-tP0 projections.

All statements concern the known positive D-normalized rank-317 reference.
No new Weil action or signed inverse response is executed. RC292 proves
a usable two-source conditional Schur criterion and exact sufficient
Chebyshev iteration budgets, with reserved native-action-error funds.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc278_smaller_positive_reference.json":"edc59d6cec516d597c2c7816bec2a38a2677e18d",
 "certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc290_soft_source_decomposition.json":"c0d90be6ea686141f088f70eb4cf3821354671be",
 "certificates/rpb108_rc291_soft_signed_envelope.json":"22c44c2535430133cc81f1a19be69cb685eabda8"
}

def choose_degree(mu,nu,b2,ideal2):
    # A degree (k-1) inverse Chebyshev polynomial has residual norm
    # ||I-N p_(k-1)(N)||_D <= 2*q_true**k.
    # q_true=(sqrt(nu/mu)-1)/(sqrt(nu/mu)+1).
    # Integer t >= sqrt(nu/mu) gives rational q >= q_true.
    assert 0<mu<=nu and b2>0 and ideal2>0
    t=1
    while mu*t*t<nu:t+=1
    assert mu*t*t>=nu and (t==1 or mu*(t-1)**2<nu)
    q=F(t-1,t+1)
    assert 0<q<1
    ok=lambda k:4*q**(2*k)*b2<ideal2
    k=1
    while not ok(k):k*=2
    lo=k//2;hi=k
    while lo+1<hi:
        m=(lo+hi)//2
        if ok(m):hi=m
        else:lo=m
    assert ok(hi)
    if hi>1:assert not ok(hi-1)
    return dict(
        rational_condition_sqrt_upper=t,
        rational_Chebyshev_q_upper=str(q),
        certified_sufficient_polynomial_degree=hi-1,
        certified_sufficient_operator_actions=hi-1,
        exact_ideal_Chebyshev_residual_D_norm_squared_upper=str(4*q**(2*hi)*b2),
        chosen_target_ideal_residual_D_norm_squared_strict=str(ideal2),
        all_polynomial_operator_actions_executed=False
    )

def run(reverse=False):
    objects={}
    for path,pin in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()==pin,(path,"pin")
        objects[path]=json.loads(raw)
    def get(x):return objects["certificates/rpb108_rc"+x+".json"]
    m=get("129_four_vector_joint_moment")
    old=get("278_smaller_positive_reference")
    ref=get("283_reduced_reference")
    soft=get("290_soft_source_decomposition")
    prior=get("291_soft_signed_envelope")
    assert old["new_reference_rank"]==371
    assert ref["proposed_buffered_reference_rank"]==317
    assert soft["reference_rank"]==prior["reference_rank"]==317
    assert soft["residual_projected_soft_direction_computed"] is False
    assert prior["no_signed_actual_inverse_response_certified"] is True
    s=F(m["actual_D_Gram_entry_lower"][0][0])/(2*B)
    assert s>0
    H2=F(3,2);H4=F(25,12)
    dR=H2+s
    assert dR>0
    ev=ref["reduced_reference_options"][0]
    lam=F(ev["parameter_lambda"])
    mu=F(ev["reduced_reference_options"][1]["certified_D_reference_floor_lower"])
    nu=F(old["smaller_reference_certificates"][0]["full_D_reference_upper"])
    assert 0<mu<nu and mu>F(1,200)
    assert ev["reduced_reference_options"][1]["new_low_reference_rank"]==122
    t=F(soft["exact_soft_mixing_parameter"])
    a=F(soft["exact_hard_pivot_native_floor"])
    delta=F(soft["exact_soft_schur_pivot_native_floor"])
    assert a>delta>0 and t>0
    # Correct action domain: N=D^-1 G with D-inner product. For native
    # source v, RHS is b=D^-1 v, so ||b||_D^2 =
    # sum LegendreMass_n * v_n^2 / (H_n+s_actual), bounded using s_lower.
    sources=[
        ("hard_P0",a,{0:F(1)}),
        ("soft_P4_minus_tP0",delta,{0:-t,4:F(1)})
    ]
    result=[]
    for label,gamma,coeff in sources:
        # Split the required subunit Mass cross majorant evenly between
        # the two positive SOURCE coordinates. The actual signed response
        # projection is not yet available.
        b2=sum((2*B/F(2*n+1)*c*c/((F(0) if n==0 else H4)+s)
                for n,c in coeff.items()),F(0))
        assert b2>0
        allotted_response_norm2=gamma/(2*lam*lam)
        approx_projection_norm2=allotted_response_norm2/4
        # For r=b-N*Yhat, N>=mu I_D:
        # ||P_R(Y-Yhat)||_physical <= ||r||_D/(mu*sqrt(dR)).
        residual_total2=mu*mu*dR*allotted_response_norm2/4
        # Exact ideal Chebyshev residual and actual-arithmetic action
        # error are each allotted ONE QUARTER of residual_total2.
        # By the triangle inequality, ||r_total||^2 < residual_total2.
        ideal2=residual_total2/4
        action_error2=residual_total2/4
        cheb=choose_degree(mu,nu,b2,ideal2)
        assert F(cheb["exact_ideal_Chebyshev_residual_D_norm_squared_upper"])<ideal2
        result.append(dict(
            source=label,
            original_source_Legendre_coefficients={str(k):str(v) for k,v in coeff.items()},
            certified_native_pivot_lower=str(gamma),
            rigorous_source_RHS_D_norm_squared_upper=str(b2),
            allocated_strict_projected_response_mass_squared_budget=str(allotted_response_norm2),
            required_approximate_signed_projection_mass_squared_strict=str(approx_projection_norm2),
            required_total_approximation_residual_D_norm_squared_strict=str(residual_total2),
            chosen_ideal_Chebyshev_residual_squared_budget_strict=str(ideal2),
            reserved_total_native_action_error_D_norm_squared_budget_strict=str(action_error2),
            Chebyshev_inverse_action_plan=cheb,
            signed_projected_response_currently_available=False,
            certified_native_operator_repeated_actions_performed=False,
            prime_archimedean_endpoint_infinite_tail_execution_errors_paid=False
        ))
    # Conditional acceptance proof (applies separately to both sources):
    # if ||P_R Yhat||² < T/4 and ||r||² < mu² dR T/4, then
    # ||P_R Y|| < sqrt(T)/2+sqrt(T)/2=sqrt(T).
    # Therefore lambda² ||P_R Y_i||² / gamma_i < 1/2 each.
    # Both sums <1 produces a collective Mass-subunit cross payment
    # only on successful *actual* signed inverse action outputs.
    assert len(result)==2
    return dict(
        milestone="RC292",
        starting_commit="c14663806869d60a988ecef2214b38bd161dfc7a",
        input_git_blob_pins=PINS,
        reference_rank=317,
        positive_joint_pivot_dimension=2,
        remaining_even_coordinates=120,
        exact_signed_dual_response_conditional_test_derived=True,
        physical_D_first_remaining_degree_lower=str(dR),
        global_even_reference_D_floor_lower=str(mu),
        global_even_reference_D_upper=str(nu),
        integer_sufficient_Chebyshev_action_budgets=result,
        if_both_signed_projection_and_action_residual_tests_pass_then_joint_even_cross_less_than_one_Mass=True,
        either_signed_projection_test_executed=False,
        true_new_even_joint_cross_subunit_certificate=False,
        remaining_314_principal_Schur_positive=False,
        original_prime_endpoint_operator_action_workload_not_executed=True,
        Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor="RC293: implement actual pinned G_new action on recurrence vectors for both P0 and P4-tP0, pay every native arithmetic and infinite-tail error in D, and test exact signed 120-mode projected outputs against RC292 thresholds."
    )

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True,type=Path)
    p.add_argument("--replay",action="store_true")
    args=p.parse_args()
    result=run(args.replay)
    print("RC292_CANDIDATE_JSON="+json.dumps(result,sort_keys=True),flush=True)
    if args.replay:
        assert result==json.loads(args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("RC292 VALIDATED: conditional two-source signed action budgets; Stage I OPEN.")
