"""RC183: complete actual canonical action on native w14 with paid tails."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,rat,mul,div,bounds,down,up,sqrtup
from validate_rpb108_rc171_regular_legendre_projection import rat as hrat,divide,endpoints
from validate_rpb108_rc179_focus_residual_canonical_action import regular_action
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];last,endpoint,joint,response,old,regular,compression=map(json.loads,raw);hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert [x['milestone'] for x in (last,endpoint,joint,response,old,regular,compression)]==['RC182','RC130','RC129','RC128','RC127','RC170','RC174']
    assert last['input_sha256'][8:11]==hs[2:5] and last['input_sha256'][14]==hs[1]
    assert endpoint['input_sha256']==hs[2:5] and compression['input_sha256'][4]==hs[5] and compression['input_sha256'][-1]==hs[2]
    # Recover both historical finite endpoint columns and verify their digest.
    path=Path(__file__).with_name('validate_rpb108_rc130_remaining_covariance.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    marker=' # Lower H2 entries retain positive finite input/output. Upper entries pay all errors.';assert src.count(marker)==1
    ns={'__file__':str(path)};exec(compile(src.replace(marker,' return locals()',1),'RC130 materialization','exec'),ns)
    d=ns['run'](paths[2:5],replay)
    payload=[dict(degree=n,centers=[str(d['trial'][j][n]) for j in range(2)]) for n in range(0,d['O']+1,2)]
    digest=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert digest==endpoint['finite_action_trial_coefficient_sha256'] and list(map(str,d['errors']))==endpoint['full_action_D_norm_error_upper']
    print('RC183 historical endpoint carrier reproduced',flush=True)
    g=d['g'];M=256;alpha={n:g[n] for n in range(0,M+1,2)};r=F(789,125)
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    gl=F(joint['actual_D_Gram_entry_lower'][3][3]);gh=F(joint['actual_D_Gram_entry_upper'][3][3]);prefix=F(0)
    for n,c in alpha.items():prefix+=down(2*B/F(2*n+1)*F(d['dn'][n][0])*c*c)
    tailEnergy=up(gh-prefix);assert tailEnergy>0
    firstInput=M+2;H=sum(F(1,n) for n in range(1,firstInput+1));Dfirst=sl+H
    e=F(regular['e_upper']);p=F(regular['pi_upper']);I2=up(e*p*p/3);U=F(M+1)/(6*p*B)
    phi2=up(min(r*r,4*B*I2*up(F(11,12)**(2*(M+1)),10**80)+e*e/(U*U)))
    inputError=up(root(phi2*tailEnergy/(sl*Dfirst)))
    reg=regular_action(alpha,regular,joint,replay)
    regularError=up(inputError+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
    relativeRegular=up(regularError/lower_root(gl));regularBudget=F(1,1000)
    assert relativeRegular<regularBudget
    # C(g+wtail) is approximated by the old finite Cg trial + wtail/2.
    # The full-domain positive contraction 0<=C<=I pays this midpoint.
    inputW=F(endpoint['input_w_tail_D_energy_upper']);roundC=F(endpoint['finite_action_rounding_D_energy_upper'][1]);outputC=F(endpoint['finite_action_output_tail_D_energy_upper'][1])
    endpointError=up(sqrtup(roundC)+sqrtup(outputC)+sqrtup(inputW)/2)
    oldError=F(endpoint['full_action_D_norm_error_upper'][1]);assert endpointError<oldError
    correction=[];correctionEnergy=F(0)
    jobs=sorted(g,reverse=replay)
    for n in jobs:
        value=divide(hrat(-r*g[n]),d['dn'][n]);lo,hi=endpoints(value);center=(lo+hi)/2;radius=(hi-lo)/2
        correction.append(dict(degree=n,coefficient_center=str(center),coefficient_radius=str(radius)))
        correctionEnergy+=up(2*B/F(2*n+1)*F(d['dn'][n][1])*radius*radius)
    correction.sort(key=lambda x:x['degree'])
    completeError=up(endpointError+regularError+root(correctionEnergy));relativeComplete=up(completeError/lower_root(gl))
    assert completeError<F(2,10000)
    cw={n:d['trial'][1][n] for n in d['trial'][1]};mu=list(map(F,response['collective_response_enrichment_budgets'][2]['analytic_moment_center_coefficients']));lam=F(response['tail_lambda'])
    assert len(mu)==15 and lam==977132
    carrier=dict(milestone='RC183-w14-carrier',native_w14_finite_coefficient_degree='even 0..4094',native_w14_finite_coefficient_centers=[str(g[n]) for n in range(0,4095,2)],
      native_w14_analytic_tail='eta_n*sum_k=0..14 mu_k*(lambda/(n(n+1)))^k, even n>=4096',analytic_moment_centers=list(map(str,mu)),analytic_lambda=str(lam),
      Cg_finite_output_degrees='even 0..8190',Cg_finite_coefficient_centers=[str(cw[n]) for n in range(0,8191,2)],historical_two_column_endpoint_sha256=digest,
      centered_Cw_trial='stored Cg polynomial + (1/2)*native w14 analytic tail',negative_r_D_inverse_w14_finite_polynomial=correction,
      exact_negative_r_analytic_tail='-r/D_n times native w14 analytic tail; actual D_n=H_n+s retained',D_inverse_regular_polynomial=reg['D_inverse_regular_polynomial'],
      canonical_w14_trial='native w14 + stored Cg polynomial + (1/2)*native w14 analytic tail + stored negative-r finite correction + exact negative-r analytic tail + stored regular polynomial',
      canonical_action_D_error_norm_upper=str(completeError))
    carrierBytes=(json.dumps(carrier,sort_keys=True,indent=2)+'\n').encode()
    result=dict(milestone='RC183',status='PASS: complete native w14 canonical action and local regular precision contract',starting_commit='b807491342015b78fde263646f74439212714eac',input_sha256=hs,
      native_source='w14, unchanged RC128/RC129 finite plus analytic carrier',native_D_energy_lower=str(gl),native_D_energy_upper=str(gh),retained_regular_input_degree=M,
      omitted_regular_input_D_energy_upper=str(tailEnergy),regular_input_tail_action_D_error_norm_upper=str(inputError),regular_input_tail_smoothing_squared_factor_upper=str(phi2),
      regular_action=reg,complete_D_inverse_Rw14_error_norm_upper=str(regularError),regular_relative_D_norm_error_upper=str(relativeRegular),local_regular_relative_norm_budget=str(regularBudget),local_regular_acceptance_ratio_upper=str(up(relativeRegular/regularBudget)),local_regular_component_contract_closed=True,
      old_Cw14_error_norm_upper=str(oldError),new_centered_Cw14_error_norm_upper=str(endpointError),same_source_endpoint_error_improvement_factor_lower=str(down(oldError/endpointError)),
      negative_r_finite_coefficient_error_D_energy_upper=str(up(correctionEnergy)),complete_canonical_w14_action_D_error_norm_upper=str(completeError),complete_canonical_w14_relative_D_norm_error_upper=str(relativeComplete),
      materialized_canonical_carrier_sha256=hashlib.sha256(carrierBytes).hexdigest(),complete_canonical_w14_carrier_realized=True,all_input_and_output_tails_paid=True,endpoint_input_tail_commutation_assumed=False,
      w14_inverse_response_evaluated=False,four_source_inverse_width_preserved=last['relative_inverse_width_upper'],next_source_family_inverse_width=None,native_seven_source_frame_changed=False,
      Stage_I_closed=False,full_native_seven_source_inverse_certified=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='add the unchanged native w14 source and its centered endpoint/regular carrier to the actual canonical inverse family, pay all mixed rows, and test the five-source half-Gram gate')
    return result,carrier

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--carrier-output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=7)
    args=p.parse_args();result,carrier=run(args.inputs,args.replay)
    if args.replay:
        assert json.loads(Path(args.output).read_text())==result and json.loads(Path(args.carrier_output).read_text())==carrier
    else:
        Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');Path(args.carrier_output).write_text(json.dumps(carrier,sort_keys=True,indent=2)+'\n')
    print('RC183 PASS: complete native w14 canonical action with all tails paid')
