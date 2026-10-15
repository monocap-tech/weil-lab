"""RC291: signed soft P4-tP0 cross-response feasibility and data sufficiency.

Exact rational interface between RC290 positive native source block and
the original inverse response projected onto 120 remaining even modes.

Neither signed inverse-response entries nor original Weil actions are
computed. An explicit ± ambiguity shows that a covariance *upper*
alone cannot certify cancellation. All thresholds are for the present
Mass-Loewner *sufficient method*, NOT necessary conditions on the Weil form.
"""
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10);SCALE=10**20
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc280_combined_jump_tail.json":"bb0dd3f6174761037ed0f20f17177ddad5749227",
 "certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc289_joint_cross_bottleneck.json":"22f1551e676d23427f7891e652be9450f638ff82",
 "certificates/rpb108_rc290_soft_source_decomposition.json":"c0d90be6ea686141f088f70eb4cf3821354671be"
}

def floor(x):return F(x.numerator*SCALE//x.denominator,SCALE)
def ceil(x):return -floor(-x)
def sqrt_bounds(x):
    assert x>=0
    if x==0:return F(0),F(0)
    n=math.isqrt(x.numerator*SCALE*SCALE//x.denominator)
    lo=F(n,SCALE);hi=F(n+1,SCALE)
    assert lo*lo<=x<=hi*hi
    return lo,hi

def run(reverse=False):
    objs={}
    for path,pin in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()==pin,("pin",path)
        objs[path]=json.loads(raw)
    def get(m):return objs["certificates/rpb108_rc"+m+".json"]
    m=get("129_four_vector_joint_moment")
    old=get("280_combined_jump_tail")
    red=get("283_reduced_reference")
    cross=get("289_joint_cross_bottleneck")
    soft=get("290_soft_source_decomposition")
    assert red["proposed_buffered_reference_rank"]==317
    assert soft["reference_rank"]==317 and cross["remaining_new_rank317_Schur_dimension"]==314
    assert soft["residual_projected_soft_direction_computed"] is False
    assert not soft["Stage_I_closed"]
    s_lo=F(m["actual_D_Gram_entry_lower"][0][0])/(2*B)
    s_hi=F(m["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0<s_lo<=s_hi
    even=cross["cross_mass_certificates"][0]
    old_even=old["combined_jump_tail_gate_certificates"][0]
    assert even["pivot_degrees"]==[0,4]
    assert even["remaining_reference_coordinates"]==120
    assert even["rank317_reference_parity_rank"]==122
    t=F(soft["exact_soft_mixing_parameter"])
    a=F(soft["exact_hard_pivot_native_floor"])
    delta=F(soft["exact_soft_schur_pivot_native_floor"])
    lam=F(red["reduced_reference_options"][0]["parameter_lambda"])
    assert a>delta>0 and lam>0
    assert F(soft["exactly_diagonalized_native_gate_Loewner_lower"][1][1])==delta
    # Exact trial polynomial for each source; source labels are distinct
    # from the 0/2/4 indices used in the earlier six-source matrix.
    Z0=list(map(F,old_even["combined_trial_tail_certificates"][0]["exact_trial_Legendre_coefficients"]))
    Z4=list(map(F,old_even["combined_trial_tail_certificates"][2]["exact_trial_Legendre_coefficients"]))
    assert len(Z0)==len(Z4)==65
    assert old_even["combined_trial_tail_certificates"][2]["source"]=="P4"
    assert all(Z0[n]==Z4[n]==0 for n in range(1,65,2))
    all_even=[2*k for k in range(122)]
    remaining=[n for n in all_even if n not in (0,4)]
    assert len(remaining)==120 and remaining[0]==2
    terms=[(2*B/F(2*n+1))*(Z4[n]-t*Z0[n])**2 for n in remaining if n<65]
    A=sum(reversed(terms) if reverse else terms,F(0))
    assert A==F(soft["orthogonalized_center_projection_Gram"][1][1])
    T=delta/lam**2
    assert A>T>0
    # For a SOFT contribution lambda² ||P_R(Zsoft+Xsoft)||²/delta<1,
    # its signed projected total physical norm² must be <T.
    # This ALONE is not full three-pivot cross positivity, which also
    # requires a paid nonnegative hard contribution.
    ra_lo,ra_hi=sqrt_bounds(A)
    rt_lo,rt_hi=sqrt_bounds(T)
    lowE=floor((ra_lo-rt_hi)**2)
    highE=ceil((ra_hi+rt_hi)**2)
    assert 0<lowE<A<highE
    # Geometric possibility of cancellation requires X amplitude
    # to fall in the interval (sqrt(A)-sqrt(T),sqrt(A)+sqrt(T)).
    # An upper bound Q >> this window does not determine the sign.
    section=even["correlated_residual_inverse_Gram_selected"]
    Sm=[[F(v) for v in row] for row in section]
    assert Sm[0][1]==Sm[1][0] and Sm[0][0]>0
    assert Sm[1][1]-Sm[1][0]**2/Sm[0][0]>0
    d=F(even["rigorous_remaining_D_weight_floor"])
    assert d>0
    soft_cov=F(soft["orthogonalized_correlated_residual_Gram"][1][1])
    Q=soft_cov/d
    assert Q>highE*F(19)
    # The existing covariance *upper matrix* admits abstract projected
    # residuals with either sign: X0=0 and X4=±P_R(Z4-tZ0).
    # Choose the physical comparison energy D on the projected modes.
    H=[F(0)]
    for n in range(1,65):H.append(H[-1]+F(1,n))
    candidate_D_energy=sum(
       ((2*B/F(2*n+1))*(H[n]+s_hi)*(Z4[n]-t*Z0[n])**2
        for n in remaining if n<65),F(0))
    # Error Gram for this *formal abstract example* equals diag(0,E).
    # S - diag(0,E) is positive. This is only a DATA-INFORMATION
    # countercontrol: it is not an alternative actual Weil operator.
    slack=Sm[1][1]-candidate_D_energy-Sm[1][0]**2/Sm[0][0]
    assert candidate_D_energy>0 and slack>0
    # Plus sign yields projected norm² =4A, minus yields 0,
    # consistent with exactly the same covariance upper enclosure.
    assert 4*A>T and F(0)<T
    # Signed cross term Bsoft=<P_R Zsoft,P_R Xsoft> is currently
    # unmeasured. If Esoft=||P_R Xsoft||² then the sharp target is
    # A+2Bsoft+Esoft<T, not separate A+Q.
    # Cauchy only gives |Bsoft|<=sqrt(A Esoft), which is sharp.
    old_center_only=F(even["pretrace_center_contribution"])
    assert 0<old_center_only
    return dict(
       milestone="RC291",starting_commit="a967d9095e353a49bf9b998e7fa62f7578c84d51",
       input_git_blob_pins=PINS,reference_rank=317,
       positive_soft_pivot_source="P4-t*P0",
       exact_mixing_parameter=str(t),
       exact_native_soft_gate_lower=str(delta),
       exact_augmentation_coefficient=str(lam),
       remaining_even_coordinates=120,
       exact_soft_trial_projection_physical_mass_squared=str(A),
       soft_only_Mass_subunit_response_norm_squared_target_strict=str(T),
       zero_hard_contribution_is_only_optimistic_sufficient_test=True,
       soft_only_target_trial_center_exceeds_limit=True,
       required_projected_soft_residual_energy_cancellation_window_outward=dict(
           lower=str(lowE),upper=str(highE)),
       current_certified_soft_inverse_residual_mass_squared_upper=str(ceil(Q)),
       current_residual_bound_over_cancellation_window_upper_endpoint_exceeds_19=True,
       exact_rational_abstract_sign_indeterminacy_test=dict(
           plus_sign_projected_response_mass_squared=str(4*A),
           minus_sign_projected_response_mass_squared="0",
           comparator_D_energy_for_plus_or_minus=str(ceil(candidate_D_energy)),
           inherited_full_two_source_covariance_matrix_slack_schur_lower=str(floor(slack)),
           full_covariance_upper_allows_both_signs=True,
           not_a_second_Weil_model_or_original_action_claim=True),
       missing_signed_projection_object="U_R*G_new^-1*(P4-t*P0)",
       missing_mixed_inner_product="physical_inner_product(P_R Zsoft,P_R Xsoft)",
       source_matrix_operator_actions_on_inverted_residual_not_yet_certified=True,
       rank317_three_pivot_cross_payment_subunit_certified=False,
       rank317_remaining_314_Schur_principal_positive=False,
       new_original_Weil_actions_performed=False,
       Stage_I_closed=False,RH=False,F4=False,Lean=False,
       next_cursor="RC292: generate certified signed 120-coordinate soft-source inverse response by validated resolvent/Chebyshev action with full prime/endpoint tail payment; compute Z+X cross cancellation and charge hard direction separately."
    )
if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("--output",required=True,type=Path)
    a.add_argument("--replay",action="store_true")
    q=a.parse_args()
    result=run(q.replay)
    print("RC291_CANDIDATE_JSON="+json.dumps(result,sort_keys=True),flush=True)
    if q.replay:assert result==json.loads(q.output.read_text(encoding="utf-8"))
    else:q.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("RC291 VALIDATED: signed soft-source information gate; Stage I OPEN")
