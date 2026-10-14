"""RC250: couple original output tails and refine their harmonic weights."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,hashlib,json
import validate_rpb108_rc249_scalar_residual_tuning as parent
direct=parent.parent;native=direct.native;orig=parent.orig;p=parent.p;B=parent.B
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
ROOT=Path(__file__).resolve().parents[1];END=256
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc249_scalar_residual_tuning.json':'c53546dd136e0f42b693598dc2501e468ea72c94','notes/RPB108_RC249_SCALAR_RESIDUAL_TUNING_20261014.md':'76403aef2a71adc63fe56990bb035152382f7582'})
HELPER_PINS['scripts/validate_rpb108_rc249_scalar_residual_tuning.py']='c3d69f66e8ea5440483242f7b1b2d1211835be93'
def extended_prime(q,a,parity,prime,reverse):
 old=native.OUT
 try:
  native.OUT=END;return native.prime_action(q,a,parity,prime,reverse)
 finally:native.OUT=old
def original_tail(r,parity,prime,reg,sl,sh,reverse):
 a=list(map(F,r['original_combination_action_certificate']['exact_original_combination_input']));q=native.input_poly(a)
 pc,pt,pfault,proof=extended_prime(q,a,parity,prime,reverse)
 assert native.OUT==128
 assert proof==r['original_combination_action_certificate']['prime_controls']
 print('RC250 prime projections through 256 '+r['parity']+' complete',flush=True)
 rp=native.regular(q,parity,reg);rc=[orig.project(rp,n) for n in range(len(rp))];assert all(x==0 for x in rc[END+1:])
 ll=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0));lh=ll+2*F(1,3)**201/(201*(1-F(1,9)))
 phi=[F(11,20)**k/factorial(k) if k%2==parity else F(0) for k in range(41)];moment=B*orig.integral(orig.product(q,phi));pole=[2*(-1)**parity*moment*v for v in phi]
 # Replay every retained original coefficient with the extended prime model.
 for n,row in enumerate(r['finite_original_combination_D_action']):
  if n%2!=parity:assert row==dict(degree=n,coefficient='0',radius='0');continue
  h,hr=native.endpoint(a,n,ll,lh);identity=a[n] if n<len(a) else F(0);v=h-rc[n]+pc[n]+orig.project(pole,n)-F(789,125)*identity
  values=[x/(orig.H(n)+s)+identity for x in [v-hr,v+hr] for s in [sl,sh]];lo=min(values);hi=max(values);c=down((lo+hi)/2);rad=max(c-lo,hi-c)
  assert row==dict(degree=n,coefficient=str(c),radius=str(up(rad)))
 controls=r['original_combination_action_certificate'];comp={k:F(v) for k,v in controls['component_D_energy_squared_errors'].items()}
 assert up(pfault*pfault/sl)==comp['prime_arithmetic']
 endpoint_remaining=F(controls['endpoint_tail_controls']['beyond_256_endpoint_D_energy_upper']);first=257 if parity else 258
 prime_remaining=up(pt/(orig.H(first)+sl));endpoint_prime_regular=[];prime_terms=[];coupled_terms=[];rounded_terms=[]
 for n in range(129,END+1):
  if n%2!=parity:assert pc[n]==rc[n]==0;continue
  h,hr=native.endpoint(a,n,ll,lh);assert hr==0;v=h-rc[n]+pc[n]
  c=down(v);rad=up(abs(v-c));endpoint_prime_regular.append(dict(degree=n,combined_model_output_numerator_center=str(c),combined_model_output_numerator_radius=str(rad)))
  prime_terms.append(orig.mass(n)*pc[n]**2/(orig.H(n)+sl));coupled_terms.append(orig.mass(n)*v*v/(orig.H(n)+sl));rounded_terms.append(orig.mass(n)*(abs(c)+rad)**2/(orig.H(n)+sl))
 if reverse:prime_terms.reverse();coupled_terms.reverse();rounded_terms.reverse()
 weighted_prime=up(sum(prime_terms,F(0))+prime_remaining);assert weighted_prime<=comp['prime_omitted_output']
 explicit=up(sum(coupled_terms,F(0)));assert explicit<=up(sum(rounded_terms,F(0)))
 remainder=up((root(endpoint_remaining)+root(prime_remaining))**2)
 coupled=up(explicit+remainder)
 oldnorm=sum((root(comp[k]) for k in ['endpoint_omitted_output','regular_omitted_output','prime_omitted_output']),F(0));old=up(oldnorm*oldnorm);accepted=min(old,coupled)
 # RC248's stored omitted-output bound encloses (oldnorm+augmentation_norm)^2.
 # Taking an upward root and subtracting its exact oldnorm recovers a valid
 # upper bound on that inherited augmentation norm without rerunning it.
 augmentation_norm=up(root(F(r['residual_model_omitted_output_D_energy_upper']))-oldnorm);assert augmentation_norm>=0
 new_omitted=up((root(accepted)+augmentation_norm)**2)
 return new_omitted,dict(prime_projection_cutoff=END,prime_controls=proof,prime_model_coefficient_sha256=native.segment_digest([(F(0),F(END),pc)]),retained_original_coefficients_exactly_replayed=True,combined_original_model_output_129_through_256=endpoint_prime_regular,all_prime_endpoint_regular_cross_terms_retained_on_explicit_output_block=True,explicit_output_blocks_orthogonal_to_beyond_256=True,regular_model_output_beyond_256_exactly_zero=True,prime_physical_omitted_energy_beyond_256_upper=str(pt),prime_weighted_D_energy_beyond_256_upper=str(prime_remaining),prime_weighted_D_energy_129_through_infinity_upper=str(weighted_prime),previous_prime_omitted_D_energy_upper=str(comp['prime_omitted_output']),endpoint_D_energy_beyond_256_upper=str(endpoint_remaining),explicit_combined_original_D_energy_129_through_256_upper=str(explicit),combined_original_D_energy_beyond_256_upper=str(remainder),new_combined_original_omitted_D_energy_upper=str(coupled),previous_separate_original_omitted_D_energy_upper=str(old),accepted_original_omitted_D_energy_upper=str(accepted),inherited_augmentation_omitted_D_norm_upper=str(augmentation_norm),new_complete_model_omitted_output_D_energy_upper=str(new_omitted),prime_parameter_rounding_fault_preserved=True)
def controls():
 # Finite orthogonal output blocks retain signed cross terms within each block.
 a=[F(2),F(-1),F(3),F(1)];b=[F(-1),F(1,2),F(-2),F(1)];w=[F(1),F(2),F(3),F(4)]
 v=[x+y for x,y in zip(a,b)];energy=sum((w[n]*v[n]**2 for n in range(4)),F(0))
 assert energy==sum((w[n]*(a[n]**2+2*a[n]*b[n]+b[n]**2) for n in range(4)),F(0))
 assert energy==sum((w[n]*v[n]**2 for n in range(2)),F(0))+sum((w[n]*v[n]**2 for n in range(2,4)),F(0))
 assert energy<=(root(sum((w[n]*a[n]**2 for n in range(4)),F(0)))+root(sum((w[n]*b[n]**2 for n in range(4)),F(0))))**2
 assert orig.H(258)>orig.H(130)>0 and orig.H(257)>orig.H(129)>0
 return dict(signed_component_cross_terms_and_orthogonal_output_blocks=True,monotone_harmonic_tail_weights=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('249_scalar_residual_tuning');old=get('248_direct_coupled_residual');forms=get('247_materialized_four_trial_response');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment');regular=get('46_native_archimedean_head');prime=get('43_native_prime_head')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);reg=list(map(F,regular['regular_kernel_coefficients']));rows=[]
 for parity,r in enumerate(old['selected_direct_residual_certificates']):
  omitted,proof=original_tail(r,parity,prime,reg,sl,sh,reverse)
  finite=F(r['residual_finite_model_rounding_D_energy_upper']);fault=F(r['original_combination_model_fault_D_norm_upper']);rational=F(r['rational_augmentation_comparison_D_error_squared_upper'])
  proposed=up((root(up(finite+omitted))+fault+root(rational))**2);E=min(F(r['complete_direct_residual_D_error_squared_upper']),proposed)
  ec=r['complete_direct_residual_center'];terms=list(range(129));terms=terms[::-1] if reverse else terms
  nl=sum((orig.mass(n)*(orig.H(n)+sl)*F(ec[n]['coefficient'])**2 for n in terms),F(0));nh=sum((orig.mass(n)*(orig.H(n)+sh)*F(ec[n]['coefficient'])**2 for n in terms),F(0));rl=down(max(F(0),rootdown(nl)-root(E))**2);rh=up((root(nh)+root(E))**2)
  b=bounds['polynomial_augmented_action_certificates'][parity];mu=F(b['fresh_augmented_N_D_lower']);nu=F(b['fresh_augmented_N_D_upper']);lam=F(b['augmentation_coefficient']);y=list(map(F,r['selected_trial_coefficients']));pr=forms['parity_materialized_four_trial_response_certificates'][parity]
  F0=[[(F(a),F(b)) for a,b in row] for row in pr['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in pr['frequency_trial_Gram_intervals']]
  cl,ch=direct.center_intervals(F0,Gy,y,lam);tl=down(cl+rl/nu);th=up(ch+rh/mu);u=[1-y[0],-y[1],-y[2],-y[3]];ql,qh=direct.quadratic(F0,u);al,ah=direct.quadratic(Gy,y);dl=down(ql+lam*al-rh/mu);dh=up(qh+lam*ah-rl/nu)
  prev=prior['scalar_residual_tuning_certificates'][parity];actualtl=max(F(prev['actual_original_action_inverse_response_lower']),tl);actualth=min(F(prev['actual_original_action_inverse_response_upper']),th);actualdl=max(F(prev['actual_signed_gap_lower']),dl,down(F0[0][0][0]-actualth));actualdh=min(F(prev['actual_signed_gap_upper']),dh,up(F0[0][0][1]-actualtl));assert actualtl<=actualth and actualdl<=actualdh
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],unchanged_retained_direct_residual_center_origin='RC248',coupled_original_output_tail_certificate=proof,complete_direct_residual_D_error_squared_upper=str(E),previous_direct_residual_D_error_squared_upper=r['complete_direct_residual_D_error_squared_upper'],complete_direct_residual_actual_D_energy_lower=str(rl),complete_direct_residual_actual_D_energy_upper=str(rh),direct_inverse_response_lower=str(tl),direct_inverse_response_upper=str(th),direct_signed_gap_lower=str(dl),direct_signed_gap_upper=str(dh),actual_original_action_inverse_response_lower=str(actualtl),actual_original_action_inverse_response_upper=str(actualth),previous_original_action_inverse_response_upper=prev['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(actualdl),actual_signed_gap_upper=str(actualdh),original_action_inverse_upper_improved=actualth<F(prev['actual_original_action_inverse_response_upper']),signed_gap_positive_certified=actualdl>0,actual_negative_gap_proved=actualdh<0))
 return dict(milestone='RC250',starting_commit='c518f086e9a5f30c745e6212f3801073b5980022',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,coupled_output_tail_response_certificates=rows,source_and_trial_spaces_unchanged=True,retained_action_degree_unchanged=128,original_model_tail_explicit_degree=END,all_prime_pairs_and_model_faults_paid=True,exact_controls=controls(),new_response_enclosures_intersected_with_RC249=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC251: materialize further coupled residual output or strengthen residual inverse coercivity; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC250 VALIDATED: coupled original output tails; full signed gate open',flush=True)
