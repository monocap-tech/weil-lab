"""RC294: paid three-column original native action and rational seed optimization.

Build the rank-317 native reduced-reference action on span{P0,P2,P4}
from the three *already executed* RC279 original source columns.
Compute reproducible approximate 3-mode least-squares seed coefficients
ONLY to propose rational trial vectors. Certify the residual of each trial
exactly by rational arithmetic with full original infinite tails/faults.

Not an arbitrary-vector native operator oracle or Chebyshev recurrence.
"""
import argparse,hashlib,json,math
from pathlib import Path
from fractions import Fraction as F

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
DIGITS=10**20
SQ=10**18
DEGREES=(0,2,4)
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc279_six_mode_gate.json":"bd729c0f5a41debac61a0f3c37276bb94e7834e5",
 "certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc290_soft_source_decomposition.json":"c0d90be6ea686141f088f70eb4cf3821354671be",
 "certificates/rpb108_rc292_signed_inverse_action_contract.json":"a4e19528ab5b12d9651a29dbeb478d7844e05470",
 "certificates/rpb108_rc293_native_seed_action.json":"a941584436ba113e9f2f48039130b8bc02136449"
}
def up(v):return -F((-v).numerator*DIGITS//(-v).denominator,DIGITS)
def rt_up(v):
    if v==0:return F(0)
    assert v>0
    return F(math.isqrt(v.numerator*SQ*SQ//v.denominator)+1,SQ)
def solve3(A,b):
    # Float proposal only; no floating-point figure is used in a proof.
    Z=[row[:]+[v] for row,v in zip(A,b)]
    for j in range(3):
        k=max(range(j,3),key=lambda i:abs(Z[i][j]))
        assert abs(Z[k][j])>1e-22,("proposal Gram singular",j)
        Z[j],Z[k]=Z[k],Z[j]
        q=Z[j][j]
        Z[j]=[v/q for v in Z[j]]
        for i in range(3):
            if i==j:continue
            q=Z[i][j]
            Z[i]=[v-q*w for v,w in zip(Z[i],Z[j])]
    return [F(f"{Z[i][3]:.10f}") for i in range(3)]
def certified_residual(seed,source,profs,sl,sh,H,lam,reverse=False):
    sm=(sl+sh)/2
    y={d:v for d,v in zip(DEGREES,seed)}
    finite=[]
    for n in range(0,2049,2):
        main=-sum((y[d]*profs[d][0][n] for d in DEGREES),F(0))
        if n in DEGREES:
            main+=(source.get(n,F(0))-lam*y[n])/(H[n]+sm)
        w=up(2*B/F(2*n+1)*up(H[n]+sh))
        finite.append(up(w*main**2))
    if reverse:finite.reverse()
    model=up(sum(finite,F(0)))
    rounding=F(0)
    for n in DEGREES:
        k=source.get(n,F(0))-lam*y[n]
        deviation=max(abs(k/(H[n]+sl)-k/(H[n]+sm)),
                      abs(k/(H[n]+sh)-k/(H[n]+sm)))
        rounding+=up(2*B/F(2*n+1)*up(H[n]+sh)*deviation**2)
    rounding=up(rounding)
    tail=up(sum((abs(y[d])*rt_up(profs[d][2]) for d in DEGREES),F(0)))
    fault=up(sum((abs(y[d])*profs[d][1] for d in DEGREES),F(0)))
    amp=up(rt_up(model)+rt_up(rounding)+tail+fault)
    return dict(
        model_finite_D_residual_norm_squared_upper=str(model),
        s_interval_rounding_D_norm_squared_upper=str(rounding),
        combined_action_tail_D_norm_upper=str(tail),
        combined_action_fault_D_norm_upper=str(fault),
        actual_native_D_residual_norm_squared_upper=str(up(amp**2)),
        exact_rational_seed={"P"+str(d):str(y[d]) for d in DEGREES},
        signed_retained_rest_projection_physical_mass_squared="0"
        if seed[1]==0 else str(up(2*B/F(5)*seed[1]**2))
    )
def run(reverse=False):
    data={}
    for path,pin in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()==pin,path
        data[path]=json.loads(raw)
    def get(i):return data["certificates/rpb108_rc"+i+".json"]
    M=get("129_four_vector_joint_moment")
    A=get("279_six_mode_gate")["coupled_six_mode_gate_certificates"][0]["actual_polynomial_action_certificates"]
    ref=get("283_reduced_reference")["reduced_reference_options"][0]
    t=F(get("290_soft_source_decomposition")["exact_soft_mixing_parameter"])
    prev=get("293_native_seed_action")["two_seed_residual_audits"]
    targets=get("292_signed_inverse_action_contract")["integer_sufficient_Chebyshev_action_budgets"]
    assert [r["source"] for r in A]==["P0","P2","P4"]
    assert ref["reduced_reference_options"][1]["new_low_reference_rank"]==122
    lam=F(ref["parameter_lambda"])
    sl=F(M["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh=F(M["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0<sl<=sh and lam>0
    sm=(sl+sh)/2
    H=[F(0)]
    for i in range(1,2049):H.append(H[-1]+F(1,i))
    profiles={}
    for j,row in enumerate(A):
        deg=DEGREES[j]
        modes=row["finite_original_D_action"]
        assert len(modes)==2049 and [a["degree"] for a in modes]==list(range(2049))
        values=[F(a["coefficient"]) for a in modes]
        assert all(values[i]==0 for i in range(1,2049,2))
        fault=F(row["global_D_fault_norm_upper"])
        tail=F(row["model_D_energy_beyond_2048_upper"])
        assert fault>=0 and tail>=0
        profiles[deg]=(values,fault,tail)
    # For each true original-source v, propose a three-column least-
    # squares fit at s_mid using floats, round coefficient to 1e-10,
    # then independently certify its actual ORIGINAL residual in Q.
    results=[]
    for ix,old in enumerate(prev):
        source={int(k):F(v) for k,v in targets[ix]["original_source_Legendre_coefficients"].items()}
        assert source==({0:F(1)} if ix==0 else {0:-t,4:F(1)})
        r0=F(old["seed_in_original_Legendre_coordinates"]["P0"])
        r4=F(old["seed_in_original_Legendre_coordinates"]["P4"])
        baseline=certified_residual((r0,F(0),r4),source,profiles,sl,sh,H,lam,reverse)
        # Verify exactly that RC293's prior original-action residual
        # calculation is unchanged under the extended 3-column engine.
        assert F(baseline["actual_native_D_residual_norm_squared_upper"])>=F(
          old["actual_native_D_residual_norm_squared_upper"])*F(999999,1000000)
        assert F(baseline["actual_native_D_residual_norm_squared_upper"])<=F(
          old["actual_native_D_residual_norm_squared_upper"])*F(1000001,1000000)
        rows=[[] for _ in range(3)];rhs=[[] for _ in range(3)]
        for n in range(0,2049,2):
            w=float(2*B/F(2*n+1)*(H[n]+sm))
            Ni=[float(profiles[d][0][n]+(lam/(H[n]+sm) if n==d else 0))
                for d in DEGREES]
            bv=float(source.get(n,F(0))/(H[n]+sm))
            for i in range(3):
                rhs[i].append(w*Ni[i]*bv)
                rows[i].append([w*Ni[i]*Ni[j] for j in range(3)])
        gram=[[math.fsum(v[j] for v in rows[i]) for j in range(3)] for i in range(3)]
        rhsvec=[math.fsum(q) for q in rhs]
        proposal=solve3(gram,rhsvec)
        signed_cap=F(targets[ix]["required_approximate_signed_projection_mass_squared_strict"])
        m2=2*B/F(5)
        # Enforce the *actual* RC292 approximate signed-rest projection
        # cap before residual evaluation; y2 is the only rest coordinate.
        if m2*proposal[1]**2>=signed_cap:
            clipped=math.copysign(0.92*math.sqrt(float(signed_cap/m2)),float(proposal[1]))
            y2=F(f"{clipped:.10f}")
            rhs0=float(rhsvec[0])-float(gram[0][1])*float(y2)
            rhs4=float(rhsvec[2])-float(gram[2][1])*float(y2)
            det=gram[0][0]*gram[2][2]-gram[0][2]*gram[2][0]
            assert det>0
            y0=(rhs0*gram[2][2]-rhs4*gram[0][2])/det
            y4=(gram[0][0]*rhs4-gram[2][0]*rhs0)/det
            proposal=[F(f"{y0:.10f}"),y2,F(f"{y4:.10f}")]
        assert m2*proposal[1]**2<signed_cap
        proposed=certified_residual(proposal,source,profiles,sl,sh,H,lam,reverse)
        lower=F(targets[ix]["required_total_approximation_residual_D_norm_squared_strict"])
        baseline2=F(baseline["actual_native_D_residual_norm_squared_upper"])
        proposal2=F(proposed["actual_native_D_residual_norm_squared_upper"])
        chosen=proposed if proposal2<baseline2 else baseline
        c2=F(chosen["actual_native_D_residual_norm_squared_upper"])
        # The finite section is an actual three-COLUMN action,
        # *not* a full operator inverse or finite-only Weil proof.
        results.append(dict(
            source=old["source"],
            original_action_basis_degrees=list(DEGREES),
            predecessor_two_column_actual_D_residual_squared_upper=old["actual_native_D_residual_norm_squared_upper"],
            recomputed_predecessor_exact_certificate=baseline,
            floating_fit_only_as_seed_proposal=True,
            proposed_three_column_seed_exact_certificate=proposed,
            chosen_paid_seed_exact_certificate=chosen,
            improvement_over_predecessor= c2<F(old["actual_native_D_residual_norm_squared_upper"]),
            residual_acceptance_target_strict=str(lower),
            residual_acceptance_pass=c2<lower,
            RC292_signed_seed_projection_cap=str(signed_cap),
            chosen_signed_seed_projection_pass=(F(chosen["signed_retained_rest_projection_physical_mass_squared"])<signed_cap),
            exact_original_action_columns_reused=True,
            all_original_action_infinite_output_tails_paid=True,
            all_global_original_action_faults_paid=True,
            native_Chebyshev_inverse_recurrence_executed=False,
            signed_inverse_response_certified=False))
    assert all(x["improvement_over_predecessor"] and x["chosen_signed_seed_projection_pass"] and not x["residual_acceptance_pass"] for x in results)
    return dict(
        milestone="RC294",starting_commit="b0857a567f8ef9c6e0a39b867b3feea5fd90c589",
        input_git_blob_pins=PINS,original_action_basis_degrees=[0,2,4],
        native_action_linear_span_certified=True,
        native_action_arbitrary_recurrence_vectors_certified=False,
        complete_source_beyond_degree_2048_tails_paid=True,
        three_column_seed_certificates=results,
        all_RH_and_Stage_I_targets_open=True,
        Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor="RC295: use exact residual Gram for the three-column Galerkin space and assess whether additional original-action columns can reduce the native residual to RC292 strict acceptance before an operator-wide Chebyshev recurrence."
    )
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--replay",action="store_true")
    args=ap.parse_args()
    out=run(args.replay)
    if args.replay:assert out==json.loads(args.output.read_text(encoding="utf-8"))
    else:args.output.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print("RC294 VALIDATED: paid three-column original action; no inverse proof",flush=True)
