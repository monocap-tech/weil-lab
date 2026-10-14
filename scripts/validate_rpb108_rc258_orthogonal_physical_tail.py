"""RC258: coupled physical output and orthogonality-constrained Fourier tails."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc257_physical_source_fourier_tail as parent
band=parent.parent; orig=parent.orig; B=parent.B; ROOT=parent.ROOT
up=parent.up; down=parent.down; root=parent.root
PINS=dict(parent.PINS); HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc257_physical_source_fourier_tail.json':'9da30c97acf824a5925a4d6f2e0b68a643cee395','notes/RPB108_RC257_PHYSICAL_SOURCE_FOURIER_TAIL_20261014.md':'8d135c0990c172048b01dea318f374d21769b1c4'})
HELPER_PINS['scripts/validate_rpb108_rc257_physical_source_fourier_tail.py']='19d19fe1ff8fba55ad8d812d2df08182eadc7880'
def orthogonal_tail(A,Y,R):
 # For p perpendicular q, ||p||^2=A, ||q||^2<=R and
 # ||P_out p||^2<=Y, duality over unit outside vectors gives
 # sup_{0<=t<=sqrt(Y/A)} sqrt(A)t+sqrt(R)sqrt(1-t^2).
 assert 0<Y<A and R>=0
 if Y*(A+R)<=A*A:
  return up((root(Y)+root((1-Y/A)*R))**2),True
 return up(A+R),False
def controls():
 # A sharp rational nontrivial angle, and a counterexample to dropping
 # the orthogonality hypothesis. Projection is onto the first coordinate.
 p=[F(4),F(3)];q=[F(3,5),F(-4,5)]; norm=lambda v:sum((x*x for x in v),F(0))
 assert sum((x*y for x,y in zip(p,q)),F(0))==0
 bound,active=orthogonal_tail(norm(p),p[0]**2,norm(q))
 assert active and bound==(p[0]+q[0])**2==F(529,25)
 aligned=[F(4,5),F(3,5)];assert norm(aligned)==norm(q) and (p[0]+aligned[0])**2>bound
 saturated,active=orthogonal_tail(F(25),F(16),F(16));assert not active and saturated==41
 return dict(sharp_rational_projection_control=True,nonorthogonal_counterexample_rejected=True,large_remainder_total_energy_fallback=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('257_physical_source_fourier_tail'); physical=get('256_retained_band_inverse'); coupled=get('253_prime_boundary_tail'); forms=get('247_materialized_four_trial_response'); metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B); harmonics=[F(0)]
 for n in range(1,515):harmonics.append(harmonics[-1]+F(1,n))
 rows=[]
 for parity,r in enumerate(prior['physical_source_Fourier_tail_certificates']):
  old=physical['retained_band_inverse_response_certificates'][parity]; src=old['actual_physical_residual_source_certificate']; c=coupled['prime_boundary_tail_response_certificates'][parity]
  assert r['selected_trial_coefficients']==old['selected_trial_coefficients']==c['selected_trial_coefficients']
  terms=[]
  # The pinned per-mode bound is explicitly mass*v^2/(H_n+sl).
  # Multiplication recovers its physical numerator, not a generic D-to-L2
  # conversion applied to arbitrary errors.
  for t in c['coupled_original_output_energy_257_through_512']:
   n=t['degree'];assert 256<n<=512 and n%2==parity
   terms.append(up(F(t['combined_original_D_energy_upper'])*(harmonics[n]+sl)))
  if reverse:terms.reverse()
  explicit=up(sum(terms,F(0))); ep=c['endpoint_remaining_beyond_512_control']
  assert ep['first_omitted_degree']==(513 if parity else 514)
  endpoint=up(2*B*F(ep['uniform_combined_endpoint_bracket_upper'])**2*F(ep['parity_telescoping_weight_sum_upper']))
  prime=F(c['prime_physical_energy_beyond_512_upper']); beyond512=up((root(endpoint)+root(prime))**2)
  original=up(explicit+beyond512)
  oldoriginal=up((root(F(src['endpoint_physical_output_beyond_256_upper']))+root(F(src['prime_physical_output_beyond_256_upper'])))**2)
  accepted_original=min(original,oldoriginal)
  R=min(F(src['complete_model_physical_output_beyond_256_upper']),up((root(accepted_original)+root(F(src['augmentation_physical_output_beyond_256_upper'])))**2))
  fp=r['retained_physical_source_Fourier_certificate']; A=F(fp['physical_polynomial_energy']); Y=F(fp['outside_physical_Fourier_energy_upper'])
  finite=F(src['finite_coefficient_and_actual_s_uncertainty_physical_energy_upper']);fault=F(src['complete_global_physical_fault_norm_upper'])
  model_out,active=orthogonal_tail(A,Y,R);assert active
  S=min(F(src['complete_actual_physical_source_energy_upper']),up((root(up((root(A)+root(finite))**2+R))+fault)**2))
  X=min(S,F(r['actual_full_source_outside_Fourier_energy_upper']),up((root(model_out)+root(finite)+fault)**2))
  plain=up((root(Y)+root(R))**2);assert model_out<=plain
  choices=[]
  for j in range(1000,2000):
   t=band.retained_band(F(j,10000),F(old['original_canonical_reference_floor']),F(old['original_low_band_penalty']),F(old['unchanged_actual_rational_augmentation_coefficient']),F(old['complete_canonical_J_to_Fhat_error_squared_upper']),F(old['log_U_lower']))
   I=F(t['physical_inside_band_multiplier_lower']);O=F(t['physical_outside_band_multiplier_lower'])
   if I>O:choices.append((up(S/I+X*(1/O-1/I)),F(t['tau']),t))
  if reverse:choices.reverse()
  correction,_,selected=min(choices,key=lambda v:(v[0],v[1]))
  center=F(old['direct_inverse_response_upper'])-F(old['actual_augmented_inverse_correction_upper']); candidate=up(center+correction)
  upper=min(F(r['actual_original_action_inverse_response_upper']),candidate)
  f0=forms['parity_materialized_four_trial_response_certificates'][parity]['original_trial_form_intervals'][0][0]
  gap=max(F(r['actual_signed_gap_lower']),down(F(f0[0])-upper))
  # Recompute the sufficient outside-energy budget using the smaller S.
  budgets=[]
  for _,_,t in choices:
   I=F(t['physical_inside_band_multiplier_lower']);O=F(t['physical_outside_band_multiplier_lower']);allow=F(f0[0])-center-S/I
   if allow>0:budgets.append((allow/(1/O-1/I),-F(t['tau']),t['tau']))
  limit,_,budget_tau=max(budgets)
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],coupled_original_physical_energy_257_through_512_upper=str(explicit),endpoint_physical_energy_beyond_512_upper=str(endpoint),prime_physical_energy_beyond_512_upper=str(prime),coupled_original_physical_energy_beyond_512_upper=str(beyond512),accepted_original_physical_energy_beyond_256_upper=str(accepted_original),previous_original_physical_energy_beyond_256_upper=str(oldoriginal),complete_model_physical_energy_beyond_256_upper=str(R),previous_complete_model_physical_energy_beyond_256_upper=src['complete_model_physical_output_beyond_256_upper'],retained_polynomial_physical_energy=str(A),retained_polynomial_outside_Fourier_energy_upper=str(Y),orthogonal_projection_nonsaturated_regime_certified=active,orthogonal_model_outside_Fourier_energy_upper=str(model_out),plain_triangle_model_outside_Fourier_energy_upper=str(plain),finite_coefficient_and_actual_s_error_squared_upper=str(finite),unchanged_global_physical_fault_norm_upper=str(fault),actual_full_source_physical_energy_upper=str(S),actual_full_source_outside_Fourier_energy_lower=r['actual_full_source_outside_Fourier_energy_lower'],actual_full_source_outside_Fourier_energy_upper=str(X),previous_actual_full_source_outside_Fourier_energy_upper=r['actual_full_source_outside_Fourier_energy_upper'],outside_upper_improved=X<F(r['actual_full_source_outside_Fourier_energy_upper']),strict_sufficient_outside_Fourier_budget=str(limit),budget_tau=budget_tau,outside_budget_met=X<limit,selected_two_band_multiplier_certificate=selected,actual_inverse_correction_upper=str(correction),candidate_inverse_response_upper=str(candidate),actual_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(upper),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_inverse_upper_improved=upper<F(r['actual_original_action_inverse_response_upper']),actual_signed_gap_lower=str(gap),actual_signed_gap_upper=r['actual_signed_gap_upper'],all_original_and_rational_augmentation_model_faults_paid=True,signed_gap_positive_certified=gap>0))
  print('RC258 '+r['parity']+': outside upper '+str(float(X))+'; inverse upper '+str(float(upper)),flush=True)
 return dict(milestone='RC258',starting_commit='a20af51b6db12c82cf5e9bde3d524f10fb13de77',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,orthogonal_physical_tail_response_certificates=rows,exact_controls=controls(),full_actual_source_outside_Fourier_energy_enclosed=True,actual_response_source_count=2,response_trials_per_parity=4,source_and_trial_spaces_unchanged=True,retained_source_output_degree_unchanged=256,prime_output_tail_interface_degree=512,chosen_rational_augmentation_unchanged=True,retained_Fourier_integrals_reused_from_pinned_RC257=True,original_Weil_positive_floor_claimed=False,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC259: materialize augmentation output beyond 256 or control complete omitted-source Fourier leakage directly; the two source signed gaps and full rank-639 gate remain open')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC258 VALIDATED: orthogonal physical/Fourier source bounds; Stage I open',flush=True)
