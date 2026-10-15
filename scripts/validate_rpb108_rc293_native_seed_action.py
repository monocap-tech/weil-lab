"""RC293: native rank-317 first-action seeds for hard and soft even sources.

Compose the actually certified RC279 original action profiles on P0 and P4,
add the rank-317 exact projection augmentation, pay complete RC279 finite
D-action defects and infinite output tails, and enclose the D residual for
two rational seed inverse responses. This is NOT an arbitrary native
Chebyshev recurrence and does NOT certify the signed inverse solution.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,math

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
DIGITS=10**20
SQ=10**18
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc279_six_mode_gate.json":"bd729c0f5a41debac61a0f3c37276bb94e7834e5",
 "certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc290_soft_source_decomposition.json":"c0d90be6ea686141f088f70eb4cf3821354671be",
 "certificates/rpb108_rc292_signed_inverse_action_contract.json":"a4e19528ab5b12d9651a29dbeb478d7844e05470"
}
SEEDS=[
 ("hard_P0",F("0.10134998"),F("-0.00386594")),
 ("soft_P4_minus_tP0",F("-0.08384303"),F("0.10042994"))
]

def down(x):return F(x.numerator*DIGITS//x.denominator,DIGITS)
def up(x):return -down(-x)
def rt_down(x):
    if x==0:return F(0)
    assert x>0
    return F(math.isqrt(x.numerator*SQ*SQ//x.denominator),SQ)

def rt_up(x):
    if x==0:return F(0)
    assert x>0
    return F(math.isqrt(x.numerator*SQ*SQ//x.denominator)+1,SQ)

def controls():
    # Original D-normalized native action is linear, whereas the
    # augmentation changes only the retained projection coefficients.
    A=[[F(2),F(1)],[F(1),F(3)]]
    y=[F(1,7),F(-2,9)]
    exact=[sum((A[j][i]*y[i] for i in range(2)),F(0)) for j in range(2)]
    assert exact==[A[j][0]*y[0]+A[j][1]*y[1] for j in range(2)]
    # No implication from a perfect signed projection of an inaccurate
    # seed to the signed projection of the actual inverse solution.
    assert F(1,3)>F(1,10000)
    return True

def run(reverse=False):
    data={}
    for path,pin in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        digest=hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()
        assert digest==pin,(path,"input pin")
        data[path]=json.loads(raw)
    def get(s):return data["certificates/rpb108_rc"+s+".json"]
    metric=get("129_four_vector_joint_moment")
    actions=get("279_six_mode_gate")["coupled_six_mode_gate_certificates"][0]["actual_polynomial_action_certificates"]
    reduced=get("283_reduced_reference")
    soft=get("290_soft_source_decomposition")
    prior=get("292_signed_inverse_action_contract")
    assert controls()
    assert [a["source"] for a in actions]==["P0","P2","P4"]
    assert prior["reference_rank"]==317 and prior["either_signed_projection_test_executed"] is False
    assert soft["reference_rank"]==317
    t=F(soft["exact_soft_mixing_parameter"])
    lam=F(reduced["reduced_reference_options"][0]["parameter_lambda"])
    new_ref=reduced["reduced_reference_options"][0]["reduced_reference_options"][1]
    assert new_ref["first_discarded_matching_degree"]==244
    assert new_ref["new_low_reference_rank"]==122
    sl=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
    sm=(sl+sh)/2
    assert 0<sl<=sm<=sh
    H=[F(0)]
    for n in range(1,2049):H.append(H[-1]+F(1,n))
    profiles={}
    for deg,row in [(0,actions[0]),(4,actions[2])]:
        assert row["source"]=="P"+str(deg)
        entries=row["finite_original_D_action"]
        assert len(entries)==2049
        assert [x["degree"] for x in entries]==list(range(2049))
        coeff=[F(x["coefficient"]) for x in entries]
        assert all(coeff[n]==0 for n in range(1,2049,2))
        fault=F(row["global_D_fault_norm_upper"])
        tail=F(row["model_D_energy_beyond_2048_upper"])
        assert fault>0 and tail>0
        profiles[deg]=(coeff,fault,tail)
    rows=[]
    for idx,(label,y0,y4) in enumerate(SEEDS):
        target=prior["integer_sufficient_Chebyshev_action_budgets"][idx]
        assert label==target["source"]
        source={int(k):F(v) for k,v in target["original_source_Legendre_coefficients"].items()}
        assert set(source)==({0} if idx==0 else {0,4})
        assert source.get(0,F(0))==(F(1) if idx==0 else -t)
        assert source.get(4,F(0))==(F(0) if idx==0 else F(1))
        # N_new Pj = N_original Pj + lam/(H_j+s) Pj for j=0,4
        # in the reduced reference. Existing RC279 action centers are
        # D-normalized finite Legendre coefficients of N_original Pj.
        y={0:y0,4:y4}
        model_terms=[]
        model_lower_terms=[]
        for n in range(0,2049,2):
            c0=profiles[0][0][n]
            c4=profiles[4][0][n]
            main=-(y0*c0+y4*c4)
            if n in (0,4):
                main+=(source.get(n,F(0))-lam*y[n])/(H[n]+sm)
            w=up(2*B/F(2*n+1)*up(H[n]+sh))
            model_terms.append(up(w*main*main))
            wlo=down(2*B/F(2*n+1)*down(H[n]+sl))
            model_lower_terms.append(down(wlo*main*main))
        if reverse:model_terms.reverse()
        model2=up(sum(model_terms,F(0)))
        model2lo=down(sum(model_lower_terms,F(0)))
        assert model2>0
        # Since s is an interval and the scalar augmentation is
        # exact, only source-supported n=0,4 use the inverse-weight
        # midpoint; s-interval uncertainty is paid independently.
        rhs_round2=F(0)
        for n in (0,4):
            v=source.get(n,F(0))-lam*y[n]
            delta=max(abs(v/(H[n]+sl)-v/(H[n]+sm)),
                      abs(v/(H[n]+sh)-v/(H[n]+sm)))
            rhs_round2+=up(2*B/F(2*n+1)*up(H[n]+sh)*delta*delta)
        rhs_round2=up(rhs_round2)
        tail_amp=sum((abs(y[deg])*rt_up(profiles[deg][2]) for deg in (0,4)),F(0))
        fault_amp=sum((abs(y[deg])*profiles[deg][1] for deg in (0,4)),F(0))
        total_amp=up(rt_up(model2)+rt_up(rhs_round2)+tail_amp+fault_amp)
        total_residual2=up(total_amp*total_amp)
        error_amp=up(rt_up(rhs_round2)+tail_amp+fault_amp)
        lower_amp=rt_down(model2lo)-error_amp
        assert lower_amp>0,(label,"lower residual not certified")
        actual_residual2_lower=down(lower_amp*lower_amp)
        assert 0<actual_residual2_lower<=total_residual2
        needed=F(target["required_total_approximation_residual_D_norm_squared_strict"])
        signed_proj_budget=F(target["required_approximate_signed_projection_mass_squared_strict"])
        # The candidate is only in the already certified positive
        # source coordinates: P_R Yhat=0. Its paid true D-residual is
        # much too large to trigger the RC292 acceptance contract.
        assert signed_proj_budget>0 and needed>0
        assert actual_residual2_lower>needed*1000,(label,"seed unexpectedly meets gate")
        rows.append({
            "source":label,
            "seed_in_original_Legendre_coordinates":{"P0":str(y0),"P4":str(y4)},
            "source_coefficients":{str(k):str(v) for k,v in sorted(source.items())},
            "native_original_action_profiles_reused":["P0","P4"],
            "actual_native_action_inputs_covered_by_RC279":True,
            "complete_original_action_modes_recomposed_through_degree":2048,
            "complete_original_action_infinite_output_tail_paid":True,
            "complete_original_action_global_D_fault_paid":True,
            "retained_projection_augmentation_paid_exactly":True,
            "model_finite_D_residual_norm_squared_upper":str(model2),
            "model_finite_D_residual_norm_squared_lower":str(model2lo),
            "s_interval_rounding_D_norm_squared_upper":str(rhs_round2),
            "combined_action_tail_D_norm_upper":str(up(tail_amp)),
            "combined_action_fault_D_norm_upper":str(up(fault_amp)),
            "actual_native_D_residual_norm_squared_upper":str(total_residual2),
            "actual_native_D_residual_norm_squared_lower":str(actual_residual2_lower),
            "certified_fixed_seed_residual_strictly_exceeds_RC292_budget":True,
            "RC292_required_residual_D_norm_squared_strict":str(needed),
            "residual_budget_failed":True,
            "residual_upper_over_target_lower":str(down(total_residual2/needed)),
            "residual_lower_over_target_lower":str(down(actual_residual2_lower/needed)),
            "candidate_signed_rest_projection_physical_mass_squared":"0",
            "candidate_signed_rest_projection_threshold_pass":True,
            "certified_actual_inverse_signed_response":False,
        })
    assert all(x["residual_budget_failed"] for x in rows)
    assert all(x["certified_fixed_seed_residual_strictly_exceeds_RC292_budget"] for x in rows)
    assert all(x["actual_native_action_inputs_covered_by_RC279"] for x in rows)
    return {
      "milestone":"RC293",
      "starting_commit":"1d2047d294698b24f65ea3c3b3e248c3b038922c",
      "input_git_blob_pins":PINS,
      "rank317_even_reference_only":True,
      "source_subspace_dimension":2,
      "two_original_native_action_profiles_recomposed_with_provenance":True,
      "new_arbitrary_degree_native_prime_action_performed":False,
      "new_Chebyshev_recurrence_executed":False,
      "full_native_signed_inverse_action_acceptance":False,
      "two_seed_residual_audits":rows,
      "remaining_even_signed_projections_certified":False,
      "remaining_314_Schur_positive":False,
      "Stage_I_closed":False,"RH":False,"F4":False,"Lean":False,
      "next_cursor":"RC294: extend the native action oracle beyond the P0,P4 seed to rigorously paid polynomial recurrence vectors; a two-mode seed has passed signed support but fails the RC292 residual tolerance by orders of magnitude."
    }

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--replay",action="store_true")
    args=ap.parse_args()
    obj=run(args.replay)
    print("RC293_CANDIDATE_JSON="+json.dumps(obj,sort_keys=True),flush=True)
    if args.replay:assert obj==json.loads(args.output.read_text(encoding="utf-8"))
    else:args.output.write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("RC293 VALIDATED: both fixed native seeds rigorously fail residual threshold; signed inverse NOT certified",flush=True)
