"""RC194: retain q185's signed endpoint-output moments, with the full remainder."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,up,down
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root

def inputs():
    base=Path(__file__).resolve().parents[1]/'certificates'
    return [base/('rpb108_rc'+n+'.json') for n in ['193_extended_f0_regular_action','185_five_source_focus_action','129_four_vector_joint_moment','121_diagonal_metric_equivalence']]

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];prior,old,joint,metric=map(json.loads,raw);hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert [d['milestone'] for d in [prior,old,joint,metric]]==['RC193','RC185','RC129','RC121']
    assert old['input_sha256'][13]==hs[2] and old['input_sha256'][16]==hs[3]
    assert prior['input_sha256'][4:]==hs[2:]
    assert metric['endpoint_form_bound']=='0 <= h <= J + 2 log(2) I <= D'
    q={row['degree']:F(row['coefficient_center']) for row in old['finite_focus_direction']}
    M=old['finite_input_degree'];O=old['endpoint_output_degree'];K=24
    assert M==256 and O==4094 and all(n%2==0 for n in q)
    lam=M*(M+1);first=O+2;rho=F(lam,first*(first+1));assert 0<rho<1
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    H=[F(0)]
    for n in range(1,O+1):H.append(H[-1]+F(1,n))
    jobs=sorted(q,reverse=replay);A=sum(abs(q[m]) for m in jobs)
    moments=[sum(q[m]*F(m*(m+1),lam)**k for m in jobs) for k in range(K+1)]
    # Outside the finite input, Cq_n = eta_n sum_m q_m/(1-lambda_m/lambda_n).
    # Geometric remainder <= A rho^(K+1)/(1-rho) at every omitted output n.
    T=up(B/((sl+H[O])*(O-1)*O));assert T>0
    remFactor=A*rho**(K+1)/(1-rho);tailError=up(root(T)*remFactor,10**80)
    omittedNorm=up(root(T)*A/(1-rho))
    assert omittedNorm<=F(old['endpoint_action_full_output_tail_D_norm_upper'])
    endpointEnergy=sum(2*B/F(2*row['degree']+1)*(sh+H[row['degree']])*F(row['coefficient_radius'])**2 for row in old['endpoint_action_polynomial'])
    negativeEnergy=sum(2*B/F(2*row['degree']+1)*(sh+H[row['degree']])*F(row['coefficient_radius'])**2 for row in old['negative_r_D_inverse_direction_polynomial'])
    endpointError=up(root(endpointEnergy+tailError**2))
    actionError=up(endpointError+root(negativeEnergy)+F(old['regular_action']['complete_D_inverse_regular_action_error_norm_upper']))
    assert endpointError<F(old['endpoint_action_full_D_error_norm_upper']) and actionError<F(old['complete_actual_canonical_q_action_D_error_norm_upper'])
    # Exact geometric identity controls at omitted modes; the proof is the
    # uniform geometric remainder above, not these independent spot checks.
    controls=[]
    for n in ([65536,8192,4096] if replay else [4096,8192,65536]):
        z=n*(n+1);direct=sum(q[m]*F(z,z-m*(m+1)) for m in jobs)
        retained=sum(moments[k]*F(lam,z)**k for k in range(K+1))
        exactRemainder=sum(q[m]*F(m*(m+1),z)**(K+1)/(1-F(m*(m+1),z)) for m in jobs)
        bound=A*F(lam,z)**(K+1)/(1-F(lam,z))
        assert direct-retained==exactRemainder and abs(exactRemainder)<=bound
        controls.append(dict(degree=n,exact_factor=str(direct),retained_factor=str(retained),remainder=str(exactRemainder),absolute_remainder_upper=str(bound)))
    controls.sort(key=lambda x:x['degree'])
    cq={row['degree']:F(row['coefficient_center']) for row in old['endpoint_action_polynomial']}
    nq={row['degree']:F(row['coefficient_center']) for row in old['negative_r_D_inverse_direction_polynomial']}
    rq={row['degree']:F(row['coefficient_center']) for row in old['regular_action']['D_inverse_regular_polynomial']}
    pairLo=pairHi=F(0)
    for n in jobs:
        product=2*B/F(2*n+1)*q[n]*(q[n]+cq.get(n,F(0))+nq.get(n,F(0))+rq.get(n,F(0)))
        left,right=product*(sl+H[n]),product*(sh+H[n]);pairLo+=min(left,right);pairHi+=max(left,right)
    pairError=root(F(old['finite_focus_D_energy_upper']))*actionError
    actualPairLo=down(pairLo-pairError);actualPairHi=up(pairHi+pairError)
    assert actualPairLo>F(metric['actual_canonical_diagonal_metric_lower'])*F(old['finite_focus_D_energy_upper'])
    assert actualPairHi<2*F(old['finite_focus_D_energy_lower'])
    transferred=up(actionError+2*F(old['actual_focus_to_q_D_error_norm_upper']))
    print('RC194 complete action old/new',float(F(old['complete_actual_canonical_q_action_D_error_norm_upper'])),float(actionError),'tail remainder',float(tailError),flush=True)
    return dict(milestone='RC194',status='PASS: signed analytic q185 endpoint-output tail retained with full remainder',starting_commit='fccad016257120934190076a8761c1b3a51ba07a',input_sha256=hs,aperture='11/10',canonical_operator='M=D^-1 L',norm='D energy',exact_q185_source_unchanged=True,finite_source_degree=M,retained_endpoint_prefix_degree=O,retained_endpoint_prefix_reference='RC185 endpoint_action_polynomial (bound by input_sha256[1])',analytic_tail_first_even_degree=first,analytic_tail_lambda=str(lam),analytic_tail_moments=[dict(order=k,exact_signed_coefficient=str(c)) for k,c in enumerate(moments)],analytic_tail_coefficient_formula='Cq185_n=eta_n*sum_{k=0}^{24} moment_k*(lambda/[n(n+1)])^k for even n>=4096',analytic_tail_formula_eta='eta_n=(2n+1)/(n(n+1)D_n)',common_eta_tail_D_energy_upper=str(T),input_absolute_coefficient_sum=str(A),geometric_ratio_upper=str(rho),full_analytic_endpoint_remainder_D_norm_upper=str(tailError),retained_endpoint_prefix_coefficient_error_D_energy_upper=str(up(endpointEnergy)),full_endpoint_action_D_error_norm_upper=str(endpointError),negative_r_coefficient_error_D_energy_upper=str(up(negativeEnergy)),retained_regular_action_D_error_norm_upper=old['regular_action']['complete_D_inverse_regular_action_error_norm_upper'],complete_actual_canonical_q_action_D_error_norm_upper=str(actionError),previous_same_source_complete_action_D_error_norm_upper=old['complete_actual_canonical_q_action_D_error_norm_upper'],previous_omitted_endpoint_tail_D_norm_upper=old['endpoint_action_full_output_tail_D_norm_upper'],finite_prefix_and_all_infinite_tails_paid=True,geometric_identity_controls=controls,actual_q_canonical_pairing_lower=str(actualPairLo),actual_q_canonical_pairing_upper=str(actualPairHi),actual_focus_residual_to_q_error_unchanged=old['actual_focus_to_q_D_error_norm_upper'],complete_actual_focus_residual_action_D_error_norm_upper=str(transferred),new_inverse_response_evaluated=False,latest_inverse_width_upper=prior['inherited_inverse_width_upper'],five_source_inverse_acceptance_closed=False,Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='rebuild complete five-source mixed rows and inverse with RC192 low actions, RC193 f0, and RC194 analytic q185 endpoint tail')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();result=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC194 PASS')
