"""RC295: exact finite-output dual annihilator for all 3-column inverse seeds.

Attempts a uniform obstruction to the RC292 strict native residual tests
for ANY rational/real input seed supported on P0,P2,P4, using a dual
functional that annihilates the certified finite model action on three
columns. A failed upper-bound criterion is not a negative operator witness.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,math
ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc279_six_mode_gate.json":"bd729c0f5a41debac61a0f3c37276bb94e7834e5",
 "certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc290_soft_source_decomposition.json":"c0d90be6ea686141f088f70eb4cf3821354671be",
 "certificates/rpb108_rc292_signed_inverse_action_contract.json":"a4e19528ab5b12d9651a29dbeb478d7844e05470",
 "certificates/rpb108_rc294_three_column_seed_action.json":"a292611697b24926f7101fd57aed60ad979d7b82"
}
K=(0,2,4)
EXTRAS=(6,8,10,12,14,16,20,24,32,40,64,100,200,400)
SCALE=10**15
def rt_up(x):
    if not x:return F(0)
    assert x>0
    return F(math.isqrt(x.numerator*SCALE*SCALE//x.denominator)+1,SCALE)
def down(x):return F(x.numerator*SCALE//x.denominator,SCALE)
def up(x):return -down(-x)
def det3(A):
    (a,b,c),(d,e,f),(g,h,i)=A
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
def four_dual(A):
    assert len(A)==4 and all(len(row)==3 for row in A)
    q=[(-1 if k%2 else 1)*det3([row for j,row in enumerate(A) if j!=k]) for k in range(4)]
    den=max(map(abs,q))
    assert den>0
    q=[v/den for v in q]
    assert all(sum((q[i]*A[i][j] for i in range(4)),F(0))==0 for j in range(3))
    return q
def run(reverse=False):
    data={}
    for path,sha in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()==sha,("pin",path)
        data[path]=json.loads(raw)
    def get(s):return data["certificates/rpb108_rc"+s+".json"]
    mom=get("129_four_vector_joint_moment")
    orig=get("279_six_mode_gate")["coupled_six_mode_gate_certificates"][0]["actual_polynomial_action_certificates"]
    red=get("283_reduced_reference")["reduced_reference_options"][0]
    soft=F(get("290_soft_source_decomposition")["exact_soft_mixing_parameter"])
    targets=get("292_signed_inverse_action_contract")["integer_sufficient_Chebyshev_action_budgets"]
    prev=get("294_three_column_seed_action")
    assert prev["original_action_basis_degrees"]==list(K)
    assert not prev["native_action_arbitrary_recurrence_vectors_certified"]
    assert [x["source"] for x in orig]==["P0","P2","P4"]
    sl=F(mom["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh=F(mom["actual_D_Gram_entry_upper"][0][0])/(2*B)
    sm=(sl+sh)/2
    lam=F(red["parameter_lambda"])
    mu=F(red["reduced_reference_options"][1]["certified_D_reference_floor_lower"])
    assert 0<sl<=sm<=sh and mu>F(1,200) and lam>0
    H=[F(0)]
    for n in range(1,401):H.append(H[-1]+F(1,n))
    actions={}
    for index,row in enumerate(orig):
        assert row["source"]=="P"+str(K[index])
        assert len(row["finite_original_D_action"])==2049
        assert row["finite_original_D_action"][0]["degree"]==0
        actions[K[index]]=(row,F(row["global_D_fault_norm_upper"]))
    source_out=[]
    for which,tar in enumerate(targets):
        source={int(k):F(v) for k,v in tar["original_source_Legendre_coefficients"].items()}
        assert source==({0:F(1)} if which==0 else {0:-soft,4:F(1)})
        tol=F(tar["required_total_approximation_residual_D_norm_squared_strict"])
        assert 0<tol<F(1,1000)
        sqrt_tol=rt_up(tol)
        rhsnorm=rt_up(sum((2*B/F(2*n+1)*v*v/(H[n]+sl) for n,v in source.items()),F(0)))
        ynorm_bound=(rhsnorm+sqrt_tol)/mu
        bdy={}
        variation={}
        for deg in K:
            w=2*B/F(2*deg+1)*(H[deg]+sl)
            bdy[deg]=ynorm_bound/rt_up(w) if False else ynorm_bound*rt_up(1/w)
            variation[deg]=max(abs(1/(H[deg]+v)-1/(H[deg]+sm)) for v in (sl,sh))
        candidates=[]
        for extra in (reversed(EXTRAS) if reverse else EXTRAS):
            modes=(0,2,4,extra)
            A=[]
            for n in modes:
                vals=[]
                for deg in K:
                    value=F(actions[deg][0]["finite_original_D_action"][n]["coefficient"])
                    if n==deg:value+=lam/(H[deg]+sm)
                    vals.append(value)
                A.append(vals)
            q=four_dual(A)
            qnorm=rt_up(sum((v*v/(2*B/F(2*n+1)*(H[n]+sl)) for n,v in zip(modes,q)),F(0)))
            bmid=sum((q[i]*source.get(n,F(0))/(H[n]+sm) for i,n in enumerate(modes)),F(0))
            berr=sum((abs(q[i]*source.get(n,F(0)))*variation[n] for i,n in enumerate(modes) if n in source),F(0))
            acterrors=[]
            for deg in K:
                qvalue=q[modes.index(deg)]
                acterror=qnorm*actions[deg][1]+abs(qvalue)*lam*variation[deg]
                acterrors.append(acterror)
            seedcost=sum((bdy[deg]*acterrors[i] for i,deg in enumerate(K)),F(0))
            gap=abs(bmid)-berr-seedcost
            sufficient=(gap>qnorm*sqrt_tol)
            ratio=gap/(qnorm*sqrt_tol)
            candidates.append((ratio,modes,q,qnorm,bmid,berr,seedcost,gap,sufficient))
        best=max(candidates,key=lambda x:x[0])
        ratio,modes,q,qnorm,bmid,berr,seedcost,gap,sufficient=best
        # A positive ratio >1 uniformly excludes ALL 3-column seeds
        # with actual ||r||_D² < the strict RC292 acceptance tolerance.
        source_out.append(dict(
          source=tar["source"],original_source_coefficients={str(k):str(v) for k,v in source.items()},
          RC292_strict_residual_squared_target=str(tol),
          mode_search_candidates=list(EXTRAS),
          best_dual_row_degrees=list(modes),
          exact_dual_annihilator_coefficients=[str(x) for x in q],
          finite_model_annihilation_exact=True,
          dual_D_inverse_norm_upper=str(qnorm),
          RHS_model_signed_dual_value=str(bmid),
          complete_source_s_interval_dual_error_upper=str(berr),
          seed_D_norm_if_residual_below_target_upper=str(up(ynorm_bound)),
          all_column_fault_and_augmentation_dual_error_upper=str(up(seedcost)),
          strict_dual_lower_numerator=str(down(gap)),
          criterion_ratio_lower=str(down(ratio)),
          all_three_column_accepted_responses_excluded=bool(sufficient),
          maximum_tested_witness_criterion_pass=bool(sufficient),
          operator_native_inverse_or_recurrence_executed=False,
          no_original_negative_Witness_claim=True))
    return dict(milestone="RC295",
       starting_commit="85e01a8cdd663fdb817ca0dcc47bca0c0c3cff6b",
       input_git_blob_pins=PINS,
       certified_three_column_finite_dual_tests=source_out,
       three_column_universal_acceptance_exclusion_for_both=all(x["all_three_column_accepted_responses_excluded"] for x in source_out),
       three_action_columns_only=True,arbitrary_native_operator_action_evaluated=False,
       Stage_I_closed=False,RH=False,F4=False,Lean=False,
       next_cursor="RC296: enlarge original Weil source-action input span with newly paid columns if the finite dual test excludes all three-source responses, or tighten the dual/error certificate if inconclusive.")
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--output",required=True,type=Path);ap.add_argument("--replay",action="store_true")
    args=ap.parse_args();out=run(args.replay)
    assert out["three_column_universal_acceptance_exclusion_for_both"]
    assert all(F(x["criterion_ratio_lower"])>100 for x in out["certified_three_column_finite_dual_tests"])
    if args.replay:assert out==json.loads(args.output.read_text())
    else:args.output.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
