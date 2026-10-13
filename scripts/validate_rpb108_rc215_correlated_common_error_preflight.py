"""RC215: common canonical carrier and correlated eight-source error budget."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import up,sqrtup,psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import inv
ROOT=Path(__file__).resolve().parents[1]
PINS={'certificates/rpb108_rc213_eight_source_error_interface.json': '23aaa6e712fca038e87603471f59c08066d6a0a9', 'certificates/rpb108_rc214_correlated_difference_canonical_action.json': 'c2599b388cd75d0528635496d9418e061e9385db', 'certificates/rpb108_rc212_native_t10_canonical_action.json': '442f9963189a32fa8185daf5558e0673753ed0f1', 'certificates/rpb108_rc135_common_response_capture.json': '2de31504cf1bc7645d3dc850f147ad6bb0582cfb'}
HELPER_PINS={'scripts/validate_rpb108_rc127_enriched_even_endpoint_action.py': 'd5d82bf70c1a178f0fe1da61f27b8623e42ed361', 'scripts/validate_rpb108_rc129_four_vector_joint_moment.py': '1229dc4a9db7509b9f6afea7116349891b618f4c'}

def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def run(reverse=False):
    for path,sha in HELPER_PINS.items():assert blob((ROOT/path).read_bytes())==sha,(path,'helper Git blob mismatch')
    data={}
    for path,sha in PINS.items():
        raw=(ROOT/path).read_bytes();assert blob(raw)==sha,(path,'input Git blob mismatch');data[path]=json.loads(raw)
    get=lambda n:data['certificates/rpb108_rc'+n+'.json']
    old=get('213_eight_source_error_interface');delta=get('214_correlated_difference_canonical_action');t=get('212_native_t10_canonical_action');u=get('135_common_response_capture')
    order=['P0','psi0','f0','w14','v10','z_b6','t10','P2'];assert old['response_source_order']==order
    assert delta['complete_native_difference_canonical_action_certified'] and t['complete_native_t10_canonical_action_certified']
    assert t['full_common_input_source_hash_verified'] and t['full_common_input_source_sha256']==u['common_finite_source_coefficient_sha256']
    G=[[F(x) for x in row] for row in old['source_D_Gram_rational_floor']];U=[[F(x) for x in row] for row in old['expanded_source_D_Gram_upper']]
    assert psd(G);K=inv(G)
    eps=list(map(F,old['complete_canonical_column_error_norm_upper']));priorZ=eps[5];eps[5]=F(delta['complete_canonical_delta_action_D_error_norm_upper'])
    assert eps[4]==F(delta['inherited_v10_complete_canonical_action_error_norm_upper'])
    commonError=up(eps[4]+eps[5]/2);newZ=up(eps[4]+eps[5]);assert newZ==F(delta['rebuilt_correlated_z_action_D_error_norm_upper'])<priorZ
    # T maps native source coefficients to coefficients of the error generators.
    # New z trial = old v trial + the new difference trial, hence e_z=e_v+e_delta.
    T=[[F(i==j) for j in range(8)] for i in range(8)];T[4][5]=F(1)
    controls=[];masks=list(range(128));masks=masks[::-1] if reverse else masks
    for mask in masks:
        sign=[1 if i==0 or mask>>(i-1)&1 else -1 for i in range(8)]
        raw=[eps[i]*sign[i] if i!=6 else F(0) for i in range(8)]
        v=[sum(T[i][j]*raw[i] for i in range(8)) for j in range(8)]
        # Exact rank-one factor as a quadratic in the future t10 error budget tau.
        a=K[6][6];b=2*sign[6]*sum(v[j]*K[j][6] for j in range(8));c=sum(v[i]*K[i][j]*v[j] for i in range(8) for j in range(8))
        controls.append(dict(mask=mask,a=a,b=b,c=c,sign=sign))
    controls.sort(key=lambda r:r['mask'])
    def evaluate(tau):
        values=[(r['a']*tau*tau+r['b']*tau+r['c'],r['mask']) for r in controls]
        return max(values,key=lambda x:(x[0],-x[1]))
    worst,mask=evaluate(eps[6]);zero,zeroMask=evaluate(F(0));target=eps[6]/8;targetWorst,targetMask=evaluate(target)
    assert zero<F(1,2)<worst and targetWorst<F(1,2)
    beta=up(worst,10**6);zeroBeta=up(zero,10**6);targetBeta=up(targetWorst,10**6);assert targetBeta<F(1,2)
    # Exact integer-grid bisection brackets the largest budget for this fixed
    # sufficient envelope. The sign maximum is convex and even in tau, hence
    # nondecreasing for tau>=0. No actual-error lower bound follows.
    grid=10**12;lo=0;hi=(eps[6].numerator*grid+eps[6].denominator-1)//eps[6].denominator
    while hi-lo>1:
        mid=(lo+hi)//2
        if evaluate(F(mid,grid))[0]<=F(1,2):lo=mid
        else:hi=mid
    budget=F(lo,grid);failBudget=F(hi,grid);budgetFactor,budgetMask=evaluate(budget);failFactor,failMask=evaluate(failBudget)
    assert failBudget-budget==F(1,grid) and budgetFactor<=F(1,2)<failFactor
    witnessSign=controls[mask]['sign'];gen=[eps[i]*witnessSign[i] for i in range(8)];wv=[sum(T[i][j]*gen[i] for i in range(8)) for j in range(8)]
    x=[sum(K[i][j]*wv[j] for j in range(8)) for i in range(8)];q=lambda A:sum(x[i]*A[i][j]*x[j] for i in range(8) for j in range(8))
    assert q(G)==worst and sum(x[i]*wv[i] for i in range(8))==worst
    failed=worst/2-worst*worst;assert failed<0
    tOnly=eps[6]*eps[6]*K[6][6];assert tOnly>F(1,2)
    rebuiltMarginal=eps[:];rebuiltMarginal[5]=newZ;norms=[sqrtup(U[i][i]) for i in range(8)]
    sourcePay=[[up(norms[i]*rebuiltMarginal[j]) for j in range(8)] for i in range(8)]
    actionPay=[[up(2*norms[i]*rebuiltMarginal[j]+2*norms[j]*rebuiltMarginal[i]+rebuiltMarginal[i]*rebuiltMarginal[j]) for j in range(8)] for i in range(8)]
    commonCoefficients=[F(0)]*8;commonCoefficients[4]=commonCoefficients[5]=F(1,2)
    commonEnergy=lambda A:sum(commonCoefficients[i]*A[i][j]*commonCoefficients[j] for i in range(8) for j in range(8))
    result=dict(milestone='RC215',starting_commit='3bd7243d11cf758c6ec5bc16ff388b7a2ac474fe',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,
        response_source_order=order,source_Gram_rational_floor=ser(G),source_Gram_unchanged=True,
        common_native_source='u=(v10+z_b6)/2 with unchanged finite centers and averaged selected analytic tails',common_finite_source_sha256=t['full_common_input_source_sha256'],common_finite_source_hash_verified=True,
        represented_common_canonical_action='pinned RC203 v10 carrier + (1/2) RC214 delta carrier',
        complete_common_canonical_action_D_error_norm_upper=str(commonError),common_source_D_energy_lower=str(commonEnergy(G)),common_source_D_energy_upper=str(commonEnergy(U)),
        common_error_identity='e_u=e_v+(1/2)e_delta',rebuilt_z_error_identity='e_z=e_v+e_delta',
        common_carrier_uses_entire_native_sources_and_paid_infinite_tails=True,common_source_is_linear_combination_not_ninth_independent_source=True,
        error_generator_order=['e_P0','e_psi0','e_f0','e_w14','e_v10','e_delta','e_t10','e_P2'],error_generator_D_norm_upper=list(map(str,eps)),
        native_coefficients_to_error_generators=ser(T),signed_control_count=128,
        signed_t_error_budget_quadratics=[dict(mask=r['mask'],quadratic=str(r['a']),linear=str(r['b']),constant=str(r['c'])) for r in controls],
        prior_independent_marginal_error_factor_upper=old['certified_independent_marginal_error_factor_upper'],
        current_correlated_error_factor_exact=str(worst),current_correlated_error_factor_upper=str(beta),current_correlated_half_Gram_error_gate_passed=False,
        current_worst_signed_mask=mask,current_failed_envelope_probe_native_coefficients=list(map(str,x)),current_failed_envelope_probe_value=str(failed),
        t10_only_envelope_factor_exact=str(tOnly),t10_only_envelope_factor_upper=str(up(tOnly,10**6)),
        zero_t10_error_counterfactual_factor_exact=str(zero),zero_t10_error_counterfactual_factor_upper=str(zeroBeta),zero_t10_error_is_counterfactual=True,
        concrete_future_t10_error_target=str(target),target_is_one_eighth_of_current_t10_error_bound=True,target_counterfactual_error_factor_exact=str(targetWorst),target_counterfactual_error_factor_upper=str(targetBeta),target_half_Gram_error_margin_lower=str(F(1,2)-targetBeta),
        concrete_future_t10_target_has_been_certified_for_actual_action=False,
        largest_fixed_envelope_t10_budget_grid=grid,largest_fixed_envelope_t10_budget_lower=str(budget),largest_fixed_envelope_t10_budget_upper=str(failBudget),budget_lower_factor_exact=str(budgetFactor),budget_upper_factor_exact=str(failFactor),budget_lower_worst_mask=budgetMask,budget_upper_worst_mask=failMask,
        source_action_pairing_absolute_error_payment=ser(sourcePay),represented_action_pairing_absolute_error_payment=ser(actionPay),rebuilt_z_marginal_D_error_norm_upper=str(newZ),all_64_pairing_error_payments_supplied=True,
        nominal_mixed_or_action_Gram_centers_assembled=False,complex_response_mixtures_paid_by_real_imaginary_decomposition=True,error_generator_orthogonality_assumed=False,
        sufficient_envelope_failure_is_not_true_error_lower_bound=True,expanded_inverse_response_evaluated=False,accepted_six_source_inverse_width_unchanged='4361/10000',Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor='RC216: tighten complete t10 canonical action to the certified target (at most one eighth of the RC212 radius), then assemble compatible expanded mixed/action/residual centers and evaluate the inverse gate')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();d=run(a.replay)
    if a.replay:assert d==json.loads(a.output.read_text())
    else:a.output.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')
    print('RC215 PASS: correlated factor',d['current_correlated_error_factor_upper'],'future t10 target',d['concrete_future_t10_error_target'])
