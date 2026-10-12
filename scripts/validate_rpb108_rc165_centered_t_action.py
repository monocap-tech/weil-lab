"""RC165: direct Ct prefix, captured output moments, centered input tail."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,mul,div,bounds,up,down,sqrtup,psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import inv,add

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    old,joint,delta,interface,assembly,gram,prior=map(json.loads,raw)
    assert [x['milestone'] for x in (old,joint,delta,interface,assembly,gram,prior)]==['RC137','RC136','RC163','RC155','RC158','RC159','RC164']
    hs=[hashlib.sha256(b).hexdigest() for b in raw];directory=Path(paths[0]).parent
    assert old['input_sha256'][0]==hs[1]
    assert delta['input_sha256'][1:4]==[hs[i] for i in (3,4,5)]
    assert prior['input_sha256'][0]==hs[2] and prior['input_sha256'][4:6]==[hs[4],hs[5]]
    assert assembly['input_sha256'][2]==hs[3]
    # Recover all prescribed canonical source coefficients, retaining every
    # predecessor hash check. The cut precedes the expensive matrix assembly.
    candidates=list(directory.glob('*.json'));dependencies=[]
    for digest in joint['input_sha256']:
        matches=[p for p in candidates if hashlib.sha256(p.read_bytes()).hexdigest()==digest]
        assert len(matches)==1;dependencies.append(str(matches[0]))
    path=Path(__file__).with_name('validate_rpb108_rc136_seven_vector_joint_matrices.py');src=path.read_text();ns={'__file__':str(path)}
    exec(compile(src[:src.index('\n amps=')]+'\n return locals()\n','RC165-source-reconstruction','exec'),ns)
    d=ns['run'](dependencies,reverse)
    L=4094;O=8190;K=24;lam=L*(L+1);rho=F(lam,(O+2)*(O+3))
    source={n:F(v[0]) for n,v in d['vec'][6].items() if n<=L}
    assert all(v[0]==v[1] for n,v in d['vec'][6].items()) and min(source.values())>0
    jobs=sorted(source,reverse=reverse);payload=[];rounding=F(0)
    for n in range(0,O+1,2):
        value=Z
        for m in jobs:
            entry=d['diagonal'][n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=plus(value,mul(entry,rat(source[m])))
        lo,hi=bounds(div(value,d['dn'][n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
        rounding+=up(2*B/F(2*n+1)*F(d['dn'][n][1])*radius*radius,10**100)
        payload.append(dict(degree=n,center=str(center),radius=str(radius)))
        if n and n%4096==0:print('RC165 direct Ct finite output through',n,flush=True)
    moments=[]
    for k in range(K+2):
        exact=sum(source[m]*F(m*(m+1),lam)**k for m in jobs)
        center=down(exact);radius=up(exact-center)
        assert exact>0 and radius>=0
        moments.append(dict(order=k,center=str(center),radius=str(radius)))
    # The first omitted output degree is 8192, sharing the RC131 eta tail.
    T=F(d['finite']['leading_new_output_tail_D_energy_upper'])
    momentRounding=up(T*sum(F(moments[k]['radius'])*rho**k for k in range(K+1))**2,10**100)
    remainderAmplitude=up((F(moments[K+1]['center'])+F(moments[K+1]['radius']))*rho**(K+1)/(1-rho))
    remainder=up(T*remainderAmplitude**2,10**100)
    inputTail=F(joint['endpoint_omitted_finite_and_analytic_source_D_energy_upper'][6])
    assert inputTail==F(old['Ct_omitted_input_action_D_energy_upper'])
    # t=p+r, q_t=Q_24(p)+r/2. There is no projection residual and no
    # old fitted-trial tail in this changed physical action approximation.
    error=up(sqrtup(rounding)+sqrtup(momentRounding)+sqrtup(remainder)+sqrtup(inputTail)/2)
    assert error<F(old['full_Ct_trial_D_norm_error_upper'])
    nativeTail=list(map(F,d['nut']))
    # For n>8190 the canonical t source remains its finite polynomial
    # through 16382, then eta times the RC135 t analytic polynomial.
    finite=[]
    for v in payload:
        n=v['degree'];finite.append(dict(degree=n,center=str(F(v['center'])+(F(d['vec'][6][n][0])/2 if n>L else 0))))
    digest=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    # Record the output-action moments and centered source separately,
    # because their canonical finite/analytic transition degrees differ.
    G=[[F(x) for x in row] for row in gram['conditioned_source_Gram_lower']]
    Y=[[F(x) for x in row] for row in assembly['trial_source_frame_coefficients']]
    eps=list(map(F,interface['action_column_D_norm_error_upper']));eps[4]=error;eps[6]=F(delta['full_Cdelta_trial_D_norm_error_upper'])
    assert F(interface['action_column_D_norm_error_upper'][4])==F(old['full_Ct_trial_D_norm_error_upper'])
    Gi=inv(G);signs=[(1,)+s for s in product((-1,1),repeat=6)]
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
    assert beta<F(delta['new_inverse_trial_marginal_error_factor_upper'])
    spectral=[F(0),F(1,7),F(1,2),F(9,10),F(1)]
    for c in spectral:assert (c-F(1,2))**2<=F(1,4)
    return dict(milestone='RC165',status='PASS: direct centered Ct trial with paid complete source and output tails',
      starting_commit='de4c7c60be8e12dda81711cea2522db7ac2c0d50',input_sha256=hs,RC136_dependency_sha256=joint['input_sha256'],aperture='11/10',
      source='t10',source_prefix_degree=L,output_prefix_degree=O,canonical_t_finite_degree=16382,
      trial_definition='q_t_new=Q_24(t10[0..4094])+(1/2)*t10[4096..infinity]; Q_24 finite direct Ct centers through 8190 plus 25 positive eta output moments beyond 8190',
      action_output_eta_definition='eta_n=(2*n+1)/(n*(n+1)*D_n), r_n=4094*4095/[n*(n+1)], even n>=8192; Q_24(p)_n=eta_n sum mu_k*r_n^k',
      centered_source_tail_definition='use half canonical t10 finite centers at degrees 4096..16382, then half its prescribed RC135 eta polynomial beyond 16382',
      finite_Ct_action_center_radius_sha256=digest(payload),finite_corrected_trial_center_sha256=digest(finite),
      finite_Ct_action_coefficient_count=len(payload),analytic_output_moments=moments,
      canonical_t_analytic_moment_centers=list(map(str,nativeTail)),canonical_t_tail_Lambda=str(d['lam']),
      output_geometric_ratio_upper=str(rho),leading_output_eta_tail_D_energy_upper=str(T),
      omitted_full_t_source_D_energy_upper=str(inputTail),centered_omitted_t_squared_error_upper=str(inputTail/4),
      finite_action_rounding_D_energy_upper=str(rounding),output_moment_rounding_D_energy_upper=str(momentRounding),
      output_geometric_remainder_D_energy_upper=str(remainder),full_Ct_trial_D_norm_error_upper=str(error),
      previous_Ct_trial_D_norm_error_upper=old['full_Ct_trial_D_norm_error_upper'],
      norm_improvement_factor=str(F(old['full_Ct_trial_D_norm_error_upper'])/error),
      squared_error_improvement_factor=str(F(old['full_Ct_trial_D_norm_error_upper'])**2/error**2),
      old_finite_projection_residual_replaced_by_direct_action=True,old_fitted_action_trial_tail_not_reused=True,
      centered_spectral_controls=[dict(eigenvalue=str(c),squared_factor=str((c-F(1,2))**2)) for c in spectral],
      no_cutoff_commutation_or_mixed_error_sign_assumed=True,
      source_frame_dimension_unchanged=7,inverse_source_coefficient_matrix_unchanged_but_physical_action_trials_changed=True,
      new_inverse_trial_signed_controls=controls,signed_control_count=len(controls),
      new_inverse_trial_marginal_error_factor_exact=str(exact),new_inverse_trial_marginal_error_factor_upper=str(beta),
      previous_inverse_trial_marginal_error_factor_upper=delta['new_inverse_trial_marginal_error_factor_upper'],
      new_inverse_trial_error_Gram_upper=ser(E),updated_action_column_D_norm_error_upper=list(map(str,eps)),
      required_pairing_rebase='replace old native Ct approximation by q_t_new; pay its seven source pairings, five old-trial pairings and mixed q_psi/q_delta/q_t Gram entries; rebuild endpoint approximation and nominal residual with three separate non-native action columns',
      new_t_trial_mixed_pairings_evaluated=False,old_t_trial_pairings_reused_for_new_t_trial=False,new_inverse_enclosure_certified=False,
      retained_reference_inverse_width_upper=prior['relative_inverse_width_upper'],half_Gram_inverse_width_gate_closed=False,Stage_I_closed=False,
      original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='pay q_t_new trial-source and mixed trial Gram entries against the RC164 q_delta and RC154 q_psi; reassemble the changed three-action endpoint and residual interface')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=7)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC165 PASS: direct centered t action',flush=True)
