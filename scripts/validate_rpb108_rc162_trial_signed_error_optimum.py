"""RC162: sharp uniform conditioned-trial error bound from column norms."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import psd,ser,up
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,inv

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths];prior,transport,assembly,gram=map(json.loads,raw)
    assert [d['milestone'] for d in (prior,transport,assembly,gram)]==['RC161','RC160','RC158','RC159']
    assert prior['input_sha256']==[hashlib.sha256(x).hexdigest() for x in raw[1:]]
    path=Path(__file__).with_name('validate_rpb108_rc161_combined_endpoint_functional.py');src=path.read_text()
    ns={'__file__':str(path)}
    exec(compile(src[:src.index('\n    candidates=[]')]+'\n    return locals()\n','RC162-reconstruction','exec'),ns)
    d=ns['run'](paths[1:],reverse)
    mat=lambda doc,key:[[F(x) for x in row] for row in doc[key]]
    G=d['GLo'];K=inv(G);Y=d['Y'];eps=d['eps'];weighted=d['weighted']
    signs=[(1,)+s for s in product((-1,1),repeat=6)]
    if reverse:signs.reverse()
    controls=[]
    for s in signs:
        # For inverse coefficients c, the action-error norm is bounded by
        # sum eps_i |(Yc)_i| = max_sign z_sign^T c, z=Y^T(sign*eps).
        z=[sum(Y[i][j]*F(s[i])*eps[i] for i in range(7)) for j in range(7)]
        energy=sum(z[i]*K[i][j]*z[j] for i in range(7) for j in range(7))
        controls.append(dict(sign=list(s),transformed_error_functional=list(map(str,z)),relative_rank_one_factor=str(energy)))
    controls.sort(key=lambda x:x['sign'])
    worst=max(controls,key=lambda x:(F(x['relative_rank_one_factor']),x['sign']))
    exact=F(worst['relative_rank_one_factor']);beta=up(exact,10**6)
    E=[[beta*x for x in row] for row in G]
    for control in controls:
        z=list(map(F,control['transformed_error_functional']))
        assert psd(add(E,[[x*y for y in z] for x in z],-1))
    # A rank-one marginal control realizes the optimum: choose the error
    # vectors sign_i eps_i times one real unit vector. This control checks
    # sharpness of column-norm information only, not the native C operator.
    z=list(map(F,worst['transformed_error_functional']));c=[row[0] for row in mm(K,[[x] for x in z])]
    yc=[row[0] for row in mm(Y,[[x] for x in c])]
    aligned=sum(F(worst['sign'][i])*eps[i]*yc[i] for i in range(7))
    budget=sum(eps[i]*abs(yc[i]) for i in range(7))
    qg=sum(c[i]*G[i][j]*c[j] for i in range(7) for j in range(7))
    assert aligned==budget and qg==exact and aligned*aligned/qg==exact
    oldUniform=d['r']['width'](weighted);assert beta<oldUniform
    # Convex blends retain both valid matrix error bounds. Test their
    # geometry in the same combined endpoint functional, not just beta.
    candidates=[];best=None
    alphas=[F(0),F(1,4),F(1,2),F(3,4),F(1)]
    gammas=[F(1),F(2),F(4)]
    if reverse:alphas.reverse();gammas.reverse()
    for alpha in alphas:
        error=add([[alpha*x for x in row] for row in weighted],[[(1-alpha)*x for x in row] for row in E])
        for gamma in gammas:
            deviation=add([[gamma*x/2 for x in row] for row in error],[[x/(2*gamma) for x in row] for row in d['GY']])
            HL=add(d['approximateLo'],deviation,-1);HU=add(d['approximateHi'],deviation)
            assert psd(HU) and psd(add(HU,HL,-1))
            width=d['r']['width'](add(HU,HL,-1))
            candidates.append(dict(weighted_fraction=str(alpha),gamma=str(gamma),relative_endpoint_width_upper=str(width)))
            if best is None or (width,alpha,gamma)<best[0]:best=((width,alpha,gamma),HL,HU,error)
    (endpointWidth,alpha,gamma),HL,HU,error=best
    assert endpointWidth<=F(prior['relative_endpoint_width_upper'])
    LLo,LHi=add(d['r']['GL'],HU,-1),add(d['r']['GU'],HL,-1)
    lower=LLo if psd(LLo) else [[x/2 for x in row] for row in G]
    inverseCandidates=[];bestInverse=None
    taus=[F(1,4),F(1,2),F(1),F(2),F(4)]
    if reverse:taus.reverse()
    for tau in taus:
        residual=add([[(1+tau)*x for x in row] for row in d['r']['NHi']],[[(1+1/tau)*x for x in row] for row in error])
        upper=add(LHi,residual);gap=add(upper,lower,-1);assert psd(gap)
        width=d['r']['width'](gap);inverseCandidates.append(dict(tau=str(tau),relative_inverse_width_upper=str(width)))
        if bestInverse is None or (width,tau)<bestInverse[0]:bestInverse=((width,tau),upper)
    baseline=d['r']['width'](add(d['GHi'],lower,-1))
    if baseline<bestInverse[0][0]:inverseWidth=baseline;upper=d['GHi']
    else:inverseWidth=bestInverse[0][0];upper=bestInverse[1]
    if F(prior['relative_inverse_width_upper'])<inverseWidth:
        inverseWidth=F(prior['relative_inverse_width_upper'])
        lower=mat(prior,'conditioned_reference_inverse_lower');upper=mat(prior,'conditioned_reference_inverse_upper')
        selection='retained RC161 inverse enclosure'
    else:selection='new blended-error inverse enclosure'
    assert psd(lower) and psd(add(upper,lower,-1))
    assert psd(add([[inverseWidth*x for x in row] for row in G],add(upper,lower,-1),-1))
    candidates.sort(key=lambda x:(F(x['weighted_fraction']),F(x['gamma'])));inverseCandidates.sort(key=lambda x:F(x['tau']))
    return dict(milestone='RC162',status='PASS: sharp marginal-norm trial error optimum and blend audit',
      starting_commit='f6d54d831136c0d6d110814d8a806250ded3e71b',input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],
      RC158_dependency_sha256=assembly['input_sha256'],aperture='11/10',
      signed_trial_error_controls=controls,signed_control_count=64,
      exact_optimal_uniform_trial_error_factor=str(exact),uniform_trial_error_factor_upper=str(beta),
      previous_weighted_error_uniform_factor_upper=str(oldUniform),
      sharp_marginal_control_sign=worst['sign'],sharp_marginal_control_inverse_coefficients=list(map(str,c)),
      marginal_column_norm_control_realizes_exact_optimum=True,
      native_endpoint_operator_realizes_marginal_control_assumed=False,
      new_uniform_error_Gram_upper=ser(E),endpoint_blend_candidates=candidates,
      selected_weighted_fraction=str(alpha),selected_endpoint_gamma=str(gamma),
      relative_endpoint_width_upper=str(endpointWidth),previous_relative_endpoint_width_upper=prior['relative_endpoint_width_upper'],
      combined_variational_lower_psd_verified=psd(LLo),inverse_candidates=inverseCandidates,
      selected_inverse_enclosure=selection,relative_inverse_width_upper=str(inverseWidth),
      conditioned_reference_inverse_lower=ser(lower),conditioned_reference_inverse_upper=ser(upper),
      half_Gram_inverse_width_gate_passed=psd(add([[F(1,2)*x for x in row] for row in G],add(upper,lower,-1),-1)),
      new_native_action_coefficients_evaluated=False,
      true_inverse_uncertainty_or_impossibility_lower_bound_inferred=False,
      original_Weil_or_augmented_actions_performed=False,
      whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='obtain sharper actual action norms or paid correlations beyond the seven marginal norm bounds on the conditioned inverse trials; retain all pairing and Gram certificates')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=4)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC162 PASS: sharp conditioned-trial marginal error bound')
