"""RC163: midpoint omitted delta plus analytic finite-prefix output tail."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse, hashlib, json
from validate_rpb108_rc127_enriched_even_endpoint_action import up,down,sqrtup,psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import add,inv

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    old,interface,assembly,gram,prior=map(json.loads,raw)
    assert [x['milestone'] for x in (old,interface,assembly,gram,prior)]==['RC153','RC155','RC158','RC159','RC162']
    directory=Path(paths[0]).parent
    names=['rpb108_rc129_four_vector_joint_moment.json','rpb108_rc132_balanced_action_shared_covariance.json',
           'rpb108_rc131_finite_part_response_capture.json','rpb108_rc134_correlated_six_input_covariance.json',
           'rpb108_rc151_complement_schur.json','rpb108_rc152_complement_action_budget.json']
    dependencies=[directory/n for n in names]
    assert old['input_sha256']==[hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies]
    assert prior['input_sha256'][2:]==[hashlib.sha256(raw[i]).hexdigest() for i in (2,3)]
    path=Path(__file__).with_name('validate_rpb108_rc153_correlated_difference_action.py')
    src=path.read_text();ns={'__file__':str(path)}
    exec(compile(src[:src.index('\n    eps=')]+'\n    return locals()\n','RC163-reconstruction','exec'),ns)
    d=ns['run'](dependencies,reverse)
    digest=lambda p:hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert digest(d['output'])==old['finite_Cdelta_trial_center_radius_sha256']
    assert d['error']==F(old['full_Cdelta_trial_D_norm_error_upper'])
    L=d['L'];O=d['O'];lam=L*(L+1);rho=d['rho'];K=24
    delta=d['delta'];jobs=sorted((n for n in delta if n<=L),reverse=reverse)
    # For n>O, Cp_n=-eta_n sum_k mu_k (lam/[n(n+1)])^k.
    # The retained prefix is negative; all mu_k are positive exact rationals.
    moments=[]
    for k in range(K+2):
        exact=sum((-delta[m])*F(m*(m+1),lam)**k for m in jobs)
        center=down(exact);radius=up(exact-center)
        assert 0<=radius and exact>=0
        moments.append(dict(order=k,center=str(center),radius=str(radius)))
    T=F(d['capture']['leading_new_output_tail_D_energy_upper'])
    momentRounding=up(T*sum(F(moments[k]['radius'])*rho**k for k in range(K+1))**2,10**100)
    # mu_(K+1) controls every higher moment, since m(m+1)/lam<=1.
    remainderAmplitude=up((F(moments[K+1]['center'])+F(moments[K+1]['radius']))*rho**(K+1)/(1-rho))
    remainder=up(T*remainderAmplitude**2,10**100)
    omitted=d['omittedInput'];rounding=d['rounding']
    error=up(sqrtup(rounding)+sqrtup(momentRounding)+sqrtup(remainder)+sqrtup(omitted)/2)
    midpointOnly=up(sqrtup(rounding)+sqrtup(d['outputTail'])+sqrtup(omitted)/2)
    assert error<midpointOnly<d['error']
    finite=[dict(degree=v['degree'],center=str(F(v['center'])+(delta[v['degree']]/2 if v['degree']>L else 0))) for v in d['output']]
    poly=list(map(F,d['cov']['z_minus_v_combined_tail_polynomial']))
    tail=[(poly[k]/2 if k<len(poly) else 0)-(F(moments[k]['center']) if k<=K else 0) for k in range(max(len(poly),K+1))]
    # The same inverse-source coefficients define new physical inverse trials.
    # This error-only diagnostic is valid for them; old Q/R are not reused.
    G=[[F(x) for x in row] for row in gram['conditioned_source_Gram_lower']]
    Y=[[F(x) for x in row] for row in assembly['trial_source_frame_coefficients']]
    eps=list(map(F,interface['action_column_D_norm_error_upper']));assert eps[-1]==d['error']
    eps[-1]=error;Gi=inv(G)
    signs=[(1,)+s for s in product((-1,1),repeat=6)]
    if reverse:signs.reverse()
    controls=[]
    for sign in signs:
        z=[sum(Y[i][j]*sign[i]*eps[i] for i in range(7)) for j in range(7)]
        factor=sum(z[i]*Gi[i][j]*z[j] for i in range(7) for j in range(7))
        controls.append(dict(sign=list(sign),relative_rank_one_factor=str(factor)))
    controls.sort(key=lambda c:c['sign']);exact=max(F(c['relative_rank_one_factor']) for c in controls);beta=up(exact,10**6)
    E=[[beta*x for x in row] for row in G]
    for sign in signs:
        z=[sum(Y[i][j]*sign[i]*eps[i] for i in range(7)) for j in range(7)]
        assert psd(add(E,[[x*y for y in z] for x in z],-1))
    assert beta<F(prior['uniform_trial_error_factor_upper'])
    return dict(milestone='RC163',status='PASS: centered delta input tail and captured analytic output tail',
      starting_commit='e96b53e7f35cda26f436b626d559dd85167d7c57',aperture='11/10',
      input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],RC153_dependency_sha256=old['input_sha256'],
      trial_definition='q_delta_new=Q_24(delta[0..4094])+(1/2)*delta[4096..infinity]; Q_24 finite RC153 centers through 8190, negative eta output moments beyond 8190',
      analytic_tail_definition='eta_n times tail_polynomial evaluated at 4094*4095/[n*(n+1)], even n>=8192',
      finite_trial_center_sha256=digest(finite),finite_trial_coefficient_count=len(finite),
      inherited_finite_action_center_radius_sha256=digest(d['output']),
      analytic_output_moments=moments,analytic_trial_tail_polynomial=list(map(str,tail)),
      output_tail_geometric_ratio_upper=str(rho),source_omitted_full_D_energy_upper=str(omitted),
      centered_omitted_source_squared_error_upper=str(omitted/4),
      finite_action_rounding_D_energy_upper=str(rounding),output_moment_rounding_D_energy_upper=str(momentRounding),
      output_geometric_remainder_D_energy_upper=str(remainder),full_Cdelta_trial_D_norm_error_upper=str(error),
      midpoint_only_D_norm_error_upper=str(midpointOnly),previous_Cdelta_trial_D_norm_error_upper=str(d['error']),
      norm_improvement_factor=str(d['error']/error),squared_error_improvement_factor=str(d['error']**2/error**2),
      centered_spectral_factor='1/2',centered_spectral_factor_uniformly_sharp=True,
      no_cutoff_commutation_assumed=True,source_finite_and_analytic_tail_both_paid=True,
      inverse_trial_coefficient_matrix_unchanged_but_physical_trials_changed=True,
      new_inverse_trial_signed_controls=controls,signed_control_count=len(controls),
      new_inverse_trial_marginal_error_factor_exact=str(exact),new_inverse_trial_marginal_error_factor_upper=str(beta),
      previous_inverse_trial_marginal_error_factor_upper=prior['uniform_trial_error_factor_upper'],
      new_inverse_trial_error_Gram_upper=ser(E),
      required_pairing_rebase='h=q_delta_new-q_delta_old; Q_new=Q_old+<h,source> in delta row; R_new delta cross adds <h,q_j>; R_new delta diagonal adds 2<h,q_delta_old>+<h,h>; recompute nominal residual and combined endpoint functional',
      old_trial_source_and_trial_Gram_pairings_reused_for_new_trial=False,
      new_trial_mixed_pairings_evaluated=False,new_inverse_enclosure_certified=False,
      retained_reference_inverse_width_upper=prior['relative_inverse_width_upper'],Stage_I_closed=False,
      original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='pay new delta trial-source and trial-trial pairings, then rebuild nominal residual and endpoint functional; retain RC162 inverse enclosure until that rebase passes')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=5)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC163 PASS: centered analytic delta action',flush=True)
