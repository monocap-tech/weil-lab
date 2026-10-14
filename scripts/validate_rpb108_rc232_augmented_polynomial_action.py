"""RC232: paid rational augmentation and complete augmented P0/P1 actions.
Uses a band-projection comparison, not dense rational Fourier multiplication.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc231_original_polynomial_action as parent
bridge=parent.parent;p=bridge.p;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({
 'certificates/rpb108_rc231_original_polynomial_action.json':'e00d0b8544f74efc8dce3d0ea073894d083a5b5d',
 'notes/RPB108_RC231_DIRECT_ORIGINAL_POLYNOMIAL_ACTIONS_20261014.md':'83173dae9bf6a0072ba65560ce421bdc05618881'})
HELPER_PINS['scripts/validate_rpb108_rc231_original_polynomial_action.py']='590de78c2725f9462e451490ab52a332999cb98d'
up=bridge.up;down=bridge.down;root=bridge.rootup
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(raw) if path.endswith('.json') else raw.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 old=get('231_original_polynomial_action');cov=get('230_augmentation_range_bridge');kernel=get('115_rational_fourier_adjoint');metric=get('129_four_vector_joint_moment');norm=get('66_arch_multiplier_transport')
 assert old['actual_original_D_energy_actions_enclosed'] and old['all_complex_combinations_of_P0_P1_covered']
 assert cov['full_chosen_augmentation_rank']==639 and kernel['rational_kernel_positive_augmentation_certified']
 B=F(11,10);sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B)
 pil=F(kernel['rational_pi'])-F(kernel['rational_pi_error_upper']);assert pil>3
 rho=F(252,257);a=F(32125,230953);rows=[]
 for j in [0,1]:
  parity='even' if j==0 else 'odd';src=next(r for r in kernel['parity_rational_Fourier_adjoint_sources'] if r['parity']==parity)
  original=next(r for r in old['polynomial_original_action_certificates'] if r['parity']==parity)
  U=F(src['rational_frequency_half_bandwidth']);lam=F(src['polynomial_model_augmentation_coefficient']);delta2=F(src['finite_model_squared_J_approximation_error_upper']);delta=root(delta2)
  # Integration by parts pays the oscillatory tail without sampled phases.
  tail=up(1/(pil**2*U)+1/(2*pil**3*B*U**2)+(F(2,3)/(pil**4*B**2*U**3) if j else 0))
  mass=2*B/F(2*j+1);assert 0<tail<mass
  epsilon=up(delta*(2+delta));f2=up((1+delta)**2)
  physical=up((root(tail)+epsilon*root(mass))**2)
  augmentation_error=up(lam**2*physical/sl)
  # The trial is lambda D^-1 Pj, with actual s interval paid separately.
  al=lam/(parent.H(j)+sh);ah=lam/(parent.H(j)+sl);center=down((al+ah)/2);rad=max(center-al,ah-center)
  rounding=up(mass*(parent.H(j)+sh)*rad**2)
  combined=up((root(F(original['complete_original_action_D_error_squared_upper']))+root(augmentation_error)+root(rounding))**2)
  inputlo=F(original['input_D_energy_lower']);inputhi=F(original['input_D_energy_upper'])
  assert inputlo==mass*(parent.H(j)+sl) and inputhi==mass*(parent.H(j)+sh)
  action=[dict(r) for r in original['finite_original_D_action']]
  for r in action:
   if r['degree']==j:
    r['coefficient']=str(F(r['coefficient'])+center)
    r['radius']=str(up(F(r['radius'])+rad))
  coef=F(action[j]['coefficient']);formerr=root(combined)*root(inputhi)
  formlo=down(min(coef*inputlo,coef*inputhi)-formerr);formhi=up(max(coef*inputlo,coef*inputhi)+formerr)
  assert formlo>0
  kappa=F(norm['complete_physical_operator_parity_norm_upper'][j]);x2=up(rho*f2)
  eta=F(src['polynomial_model_positive_augmentation_floor_lower']);bhat=up(1+rho*kappa+lam*x2);mu=down(a*eta);nu=2*bhat
  previous=next(r for r in cov['parity_source_range_and_bridge_certificates'] if r['parity']==parity);assert bhat<F(previous['fresh_rational_H_upper'])
  sourcebound=up(f2/sl)
  rows.append(dict(parity=parity,input='P'+str(j),rational_frequency_half_bandwidth=str(U),augmentation_coefficient=str(lam),physical_polynomial_mass=str(mass),physical_outside_band_Fourier_energy_upper=str(tail),physical_Fhat_to_J_band_error_squared_upper=str(delta2),physical_Fhat_star_Fhat_to_J_star_J_operator_norm_upper=str(epsilon),augmentation_trial_coefficient=str(center),augmentation_trial_coefficient_radius=str(up(rad)),augmentation_trial_rounding_D_error_squared_upper=str(rounding),actual_augmentation_action_D_error_squared_upper=str(augmentation_error),finite_complete_augmented_D_action=action,complete_augmented_action_D_error_squared_upper=str(combined),input_D_energy_lower=str(inputlo),input_D_energy_upper=str(inputhi),relative_augmented_D_action_error_squared_upper=str(up(combined/inputlo)),augmented_test_form_lower=str(formlo),augmented_test_form_upper=str(formhi),uniform_all_input_rational_to_band_augmented_D_operator_error_norm_upper=str(up(lam*epsilon/sl)),fresh_canonical_H_lower=str(eta),fresh_canonical_H_upper=str(bhat),fresh_H_upper_derivation='1+rho*kappa+lambda*rho*(1+delta)^2, using actual physical K and Fhat bounds',fresh_augmented_N_D_lower=str(mu),fresh_augmented_N_D_upper=str(nu),previous_conservative_N_D_upper=previous['D_energy_augmented_N_upper'],conditional_exact_N_action_inverse_budgets=bridge.polynomial_budgets(mu,nu,sourcebound,lam),full_action_errors_added_in_norm_not_squared=True))
 # Positive exact adjoint-product control, in a nonidentity physical metric.
 G=[[F(2),F(1,3)],[F(1,3),F(3)]];Q=[[F(1,2),F(1,5)],[F(1,7),F(1,3)]];E=[[F(1,100),F(1,200)],[-F(1,300),F(1,400)]]
 Qe=p.add(Q,E);Qs=p.mm(p.inv(G),p.trans(Q));Es=p.mm(p.inv(G),p.trans(E));Qes=p.mm(p.inv(G),p.trans(Qe))
 exact=p.add(p.mm(Qes,Qe),p.mm(Qs,Q),-1)
 expansion=p.add(p.add(p.mm(Es,Qe),p.mm(Qs,E)),[[F(0)]*2 for _ in range(2)])
 assert exact==expansion
 # Error-Gram and form enclosures cover all combinations by parity.
 rel=max(F(r['relative_augmented_D_action_error_squared_upper']) for r in rows)
 errors=[[rows[0]['complete_augmented_action_D_error_squared_upper'],'0'],['0',rows[1]['complete_augmented_action_D_error_squared_upper']]]
 return dict(milestone='RC232',starting_commit='6ea782e1029624c8a969dd8ad70849eaaebe0672',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,chosen_augmentation='same exact RC115 rational Hhat; not replaced by the ideal band operator',band_comparison_error_paid=True,actual_rational_augmentation_action_enclosures_certified=True,dense_exact_rational_kernel_multiplication_performed=False,actual_complete_augmented_P0_P1_action_enclosures_certified=True,polynomial_augmented_action_certificates=rows,two_input_augmented_D_action_error_Gram_upper=errors,two_input_relative_augmented_D_action_error_squared_upper=str(rel),all_complex_combinations_of_P0_P1_covered=True,opposite_parity_augmented_error_pairing_zero=True,full_range_augmentation_to_band_model_error_certified=True,full_range_augmentation_to_identity_model_error_claimed=False,all_639_source_augmented_actions_executed=False,native_frequency_Gram_evaluated=False,actual_augmented_inverse_responses_computed=False,original_augmented_response_norm_below_one_certified=False,exact_nonidentity_metric_adjoint_product_identity_verified=True,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC233: improve/materialize augmented actions on actual response/source trials and certify full-range inverse residuals; P0/P1 action tests are not exhaustive auxiliary coverage')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();c=run(args.replay)
 if args.replay:assert c==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC232 PASS: complete augmented P0/P1 action enclosures; full inverse-response gate open',flush=True)
