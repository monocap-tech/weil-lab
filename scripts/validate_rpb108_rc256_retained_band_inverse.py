"""RC256: retain ideal-band positivity and bound the physical residual source."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc255_weighted_canonical_inverse_bound as parent
direct=parent.direct;orig=parent.orig;p=parent.p;B=parent.B
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc255_weighted_canonical_inverse_bound.json':'48f697a15708b8cfdcb32e72296254b541232ec0','notes/RPB108_RC255_WEIGHTED_CANONICAL_INVERSE_BOUND_20261014.md':'79627ee5724d1fba3030e585767c5aaa925b1f76'})
HELPER_PINS['scripts/validate_rpb108_rc255_weighted_canonical_inverse_bound.py']='dfbc0bc7e6b6d6efa3a7713596783568d6c96527'
def log_interval(U):
 v=U;k=0
 while v>=2:v/=2;k+=1
 assert 1<=v<2;x=(v-1)/(v+1);z=F(1,3)
 lo2=2*sum((z**(2*j+1)/F(2*j+1) for j in range(100)),F(0));hi2=lo2+2*z**201/(201*(1-z*z))
 lo=2*sum((x**(2*j+1)/F(2*j+1) for j in range(100)),F(0));hi=lo+2*x**201/(201*(1-x*x))
 return down(k*lo2+lo),up(k*hi2+hi),dict(power_of_two=k,reduced_argument=str(v),positive_atanh_terms=100)
def retained_band(tau,gamma,penalty,lam,delta2,logU):
 assert 0<tau<F(1,5);eta=down(gamma-lam*(1/tau-1)*delta2);beta=lam*(1-tau)-penalty;assert eta>0 and beta>0
 inside=down(eta+beta);outside=down(eta*logU);floor=min(inside,outside);assert floor>0
 return dict(tau=str(tau),canonical_metric_floor=str(eta),retained_ideal_band_coefficient=str(beta),physical_inside_band_multiplier_lower=str(inside),physical_outside_band_multiplier_lower=str(outside),global_physical_augmented_form_floor=str(floor))
def controls():
 # Reverse Young is exact after multiplying the slack by tau.
 j=[F(1,3),F(-2,5)];e=[F(-1,7),F(1,11)];norm=lambda v:sum((x*x for x in v),F(0))
 for tau in [F(1,10),F(3,20),F(197,1000)]:
  f=[a+b for a,b in zip(j,e)];slack=norm(f)-(1-tau)*norm(j)+(1/tau-1)*norm(e)
  assert tau*slack==norm([tau*a+b for a,b in zip(j,e)])>=0
 # A nonidentity canonical form and noncommuting actual augmentation retain the same band lower form.
 L=[[F(2),F(1,5)],[F(1,5),F(3)]];J=[[F(1,2),F(1,3)],[F(0),F(1,4)]];E=[[F(1,1000),F(0)],[F(-1,1500),F(1,1200)]];Fhat=p.add(J,E)
 gamma=F(1,10);penalty=F(2);lam=F(5,2);tau=F(3,20);delta2=F(1,100000)
 assert p.psd(p.add(p.scale(delta2,L),p.mm(p.trans(E),E),-1))
 A=p.add(p.scale(gamma,L),p.scale(penalty,p.mm(p.trans(J),J)),-1);G=p.add(A,p.scale(lam,p.mm(p.trans(Fhat),Fhat)));eta=gamma-lam*(1/tau-1)*delta2;beta=lam*(1-tau)-penalty
 assert p.psd(p.add(G,p.add(p.scale(eta,L),p.scale(beta,p.mm(p.trans(J),J))),-1))
 assert p.mm(A,p.mm(p.trans(Fhat),Fhat))!=p.mm(p.mm(p.trans(Fhat),Fhat),A)
 return dict(exact_reverse_Young_identity=True,nonidentity_canonical_metric_retained_band_lower_form=True,original_and_augmentation_not_assumed_commuting=True)
def physical_source(c,oldr,endpoint,primetail,lam,sl,sh,harmonics,reverse):
 sm=(sl+sh)/2;sr=(sh-sl)/2;terms=[];errors=[]
 for n,row in enumerate(c['extended_complete_direct_residual_center']):
  center=F(row['coefficient']);radius=F(row['radius']);d=harmonics[n]
  terms.append(up(orig.mass(n)*((d+sm)*center)**2));errors.append(up(orig.mass(n)*((d+sh)*radius+sr*abs(center))**2))
 if reverse:terms.reverse();errors.reverse()
 retained=up(sum(terms,F(0)));finite=up(sum(errors,F(0)))
 ep=endpoint['signed_endpoint_tail_certificate']['direct_uniform_moment_bound'];endpoint_physical=up(2*B*F(ep['uniform_combined_endpoint_bracket_upper'])**2*F(ep['parity_telescoping_weight_sum_upper']))
 prime_physical=F(primetail['coupled_original_output_tail_certificate']['prime_physical_omitted_energy_beyond_256_upper']);band_physical=up(lam*lam*F(c['band_output_beyond_256_physical_energy_upper']))
 omitted=up((root(endpoint_physical)+root(prime_physical)+root(band_physical))**2)
 components=oldr['original_combination_action_certificate']['component_D_energy_squared_errors'];faults={k:up(sl*F(components[k])) for k in ['regular_kernel','prime_arithmetic','pole_Taylor']};rational=up(sl*F(c['unchanged_rational_augmentation_comparison_D_error_squared_upper']))
 faultnorm=up(sum((root(v) for v in faults.values()),F(0))+root(rational));model=up((root(retained)+root(finite))**2+omitted);full=up((root(model)+faultnorm)**2)
 return full,dict(physical_source_identity='g_e=D e=G0 Pbase-G Z',retained_source_center_parameter=str(sm),retained_source_physical_energy_upper=str(retained),finite_coefficient_and_actual_s_uncertainty_physical_energy_upper=str(finite),endpoint_physical_output_beyond_256_upper=str(endpoint_physical),prime_physical_output_beyond_256_upper=str(prime_physical),augmentation_physical_output_beyond_256_upper=str(band_physical),complete_model_physical_output_beyond_256_upper=str(omitted),complete_model_physical_energy_upper=str(model),original_global_physical_squared_faults={k:str(v) for k,v in faults.items()},rational_augmentation_physical_squared_fault_upper=str(rational),complete_global_physical_fault_norm_upper=str(faultnorm),complete_actual_physical_source_energy_upper=str(full),finite_and_omitted_model_output_orthogonal=True,global_model_faults_paid_in_norm=True,endpoint_physical_tail_derived_from_bracket_and_telescoping_bound=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('255_weighted_canonical_inverse_bound');centers=get('251_extended_coupled_residual');endpoint=get('252_signed_endpoint_tail');primetail=get('250_coupled_original_output_tail');old=get('248_direct_coupled_residual');bound=get('232_augmented_polynomial_action');forms=get('247_materialized_four_trial_response');metric=get('129_four_vector_joint_moment');positive=get('114_positive_augmentation');kernel=get('115_rational_fourier_adjoint')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);harmonics=[F(0)]
 for n in range(1,257):harmonics.append(harmonics[-1]+F(1,n))
 rows=[]
 for parity,r in enumerate(prior['weighted_canonical_inverse_response_certificates']):
  b=bound['polynomial_augmented_action_certificates'][parity];k=kernel['parity_rational_Fourier_adjoint_sources'][parity];a=positive['parity_positive_augmentation_certificates'][parity];lam=F(b['augmentation_coefficient']);penalty=F(a['low_band_penalty']);gamma=F(a['reference_floor']);assert lam==F(5,4)*penalty
  contour=F(k['finite_model_squared_J_approximation_error_upper']);assert contour>=F(a['Fourier_approximation_squared_error_upper'])
  # Conservatively include the separate finite-kernel error again; valid
  # whether the pinned J-approximation field already combined it or not.
  delta2=up((root(contour)+root(F(k['finite_model_operator_error_squared_upper'])))**2)
  U=F(b['rational_frequency_half_bandwidth']);assert U==F(k['rational_frequency_half_bandwidth']);loglo,loghi,logproof=log_interval(U);assert loglo>1
  choices=[retained_band(F(j,10000),gamma,penalty,lam,delta2,loglo) for j in range(1000,2000)];choices=choices[::-1] if reverse else choices
  selected=max(choices,key=lambda row:(F(row['global_physical_augmented_form_floor']),-F(row['tau'])));floor=F(selected['global_physical_augmented_form_floor'])
  c=centers['extended_coupled_residual_response_certificates'][parity];assert c['selected_trial_coefficients']==r['selected_trial_coefficients']
  source,sourceproof=physical_source(c,old['selected_direct_residual_certificates'][parity],endpoint['signed_endpoint_tail_response_certificates'][parity],primetail['coupled_output_tail_response_certificates'][parity],lam,sl,sh,harmonics,reverse);correction=up(source/floor)
  pr=forms['parity_materialized_four_trial_response_certificates'][parity];F0=[[(F(a),F(b)) for a,b in row] for row in pr['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in pr['frequency_trial_Gram_intervals']];y=list(map(F,r['selected_trial_coefficients']));cl,ch=direct.center_intervals(F0,Gy,y,lam)
  th=up(ch+correction);u=[1-y[0],-y[1],-y[2],-y[3]];ql,qh=direct.quadratic(F0,u);al,ah=direct.quadratic(Gy,y);dl=down(ql+lam*al-correction)
  actualtl=F(r['actual_original_action_inverse_response_lower']);actualth=min(F(r['actual_original_action_inverse_response_upper']),th);actualdl=max(F(r['actual_signed_gap_lower']),dl,down(F0[0][0][0]-actualth));actualdh=F(r['actual_signed_gap_upper']);assert actualtl<=actualth and actualdl<=actualdh
  # Conditional stronger bound: source/inside + outside*(1/outside-1/inside).
  # The outside Fourier energy is not evaluated or certified in this pass.
  budgets=[]
  for row in choices:
   inside=F(row['physical_inside_band_multiplier_lower']);outside=F(row['physical_outside_band_multiplier_lower'])
   if inside<=outside:continue
   allowance=F0[0][0][0]-ch-source/inside
   if allowance<=0:continue
   limit=allowance/(1/outside-1/inside);assert 0<limit<source
   assert ch+source/inside+limit*(1/outside-1/inside)==F0[0][0][0]
   budgets.append(dict(tau=row['tau'],canonical_metric_floor=row['canonical_metric_floor'],retained_ideal_band_coefficient=row['retained_ideal_band_coefficient'],inside_inverse_denominator=str(inside),outside_inverse_denominator=str(outside),sufficient_strict_outside_physical_Fourier_energy_upper=str(limit)))
  budget=max(budgets,key=lambda row:(F(row['sufficient_strict_outside_physical_Fourier_energy_upper']),-F(row['tau'])))
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],original_canonical_reference_floor=str(gamma),original_low_band_penalty=str(penalty),unchanged_actual_rational_augmentation_coefficient=str(lam),complete_canonical_J_to_Fhat_error_squared_upper=str(delta2),rational_half_bandwidth=str(U),log_U_lower=str(loglo),log_U_upper=str(loghi),log_interval_control=logproof,retained_ideal_band_lower_form='G >= eta_tau L + beta_tau C_U',exact_lower_multiplier='eta_tau log(e+abs(xi)) + beta_tau 1_abs(xi)<=U',finite_tau_search=dict(first='1/10',last='1999/10000',step='1/10000',candidate_count=1000,continuous_optimality_claimed=False),selected_global_physical_floor_certificate=selected,actual_physical_residual_source_certificate=sourceproof,actual_augmented_inverse_correction_upper=str(correction),direct_inverse_response_upper=str(th),direct_signed_gap_lower=str(dl),actual_original_action_inverse_response_lower=str(actualtl),actual_original_action_inverse_response_upper=str(actualth),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(actualdl),actual_signed_gap_upper=str(actualdh),original_action_inverse_upper_improved=actualth<F(r['actual_original_action_inverse_response_upper']),conditional_two_band_budget=budget,outside_residual_source_Fourier_energy_evaluated=False,conditional_two_band_closure_certified=False,original_Weil_positive_floor_claimed=False,signed_gap_positive_certified=actualdl>0,actual_negative_gap_proved=actualdh<0))
 return dict(milestone='RC256',starting_commit='01192e3c18e404601983bf5ce545c5438d02fe3e',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,retained_band_inverse_response_certificates=rows,source_and_trial_spaces_unchanged=True,retained_residual_output_degree_unchanged=256,chosen_rational_augmentation_unchanged=True,positive_ideal_band_term_retained_by_reverse_Young=True,all_original_and_rational_augmentation_model_faults_preserved=True,exact_controls=controls(),new_response_enclosures_intersected_with_RC255=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC257: certify the full physical residual source Fourier energy outside U against the explicit two-band budget, or change the response trial; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC256 VALIDATED: retained-band positivity and physical-source inverse bounds; Stage I open',flush=True)
