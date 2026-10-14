"""RC264: nested Fourier tails in the actual augmented inverse comparison."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,hashlib,json
import validate_rpb108_rc263_high_mode_inverse as parent
coercive=parent.coercive;source=parent.parent;tail=parent.tail
ROOT=parent.ROOT;orig=parent.orig;B=parent.B
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc263_high_mode_inverse.json':'a6e56b014362250840fd52f17d19ea63c5fbd32f','notes/RPB108_RC263_HIGH_MODE_INVERSE_20261014.md':'2ab2668fea15370cd32ea17a505d05992988a2fb'})
HELPER_PINS['scripts/validate_rpb108_rc263_high_mode_inverse.py']='3820e4bbf3d83b07d7bb8d4c8eaf8444caea3732'

def high_trace(V,pi_upper,parity):
 first=1025 if parity else 1026;z=2*pi_upper*B*V
 df=factorial(2*first+1)//(2**first*factorial(first))
 ratio=z**4/F(((2*first+3)*(2*first+5))**2)
 assert 0<ratio<1
 raw=4*B*V*z**(2*first)/df**2/(1-ratio)
 # A positive contraction also bounds its compression's norm by one.
 K=min(F(1),up(raw))
 return K,dict(first_omitted_matching_degree=first,parity_series_ratio_upper=str(up(ratio)),Poisson_trace_upper_capped_at_one=str(K),contraction_cap_active=raw>=1)

def shell_lower(A,Y,R,K):
 triangle=down(max(F(0),rootdown(Y)-root(R))**2)
 cross=up(root(up((A-Y)*K*R)))
 trace=max(F(0),down(Y-2*cross))
 return max(triangle,trace),dict(triangle_lower=str(triangle),high_space_band_cross_absolute_upper=str(cross),high_space_trace_lower=str(trace))

def controls():
 p=coercive.p
 # Commuting full-line Fourier-shell projections, including an outside tail.
 masses=[F(1,5),F(2,7),F(1,11),F(1,13)]
 I=F(7);O=[F(1,3),F(2,5),F(1,2)]
 w=[1/I]+[1/v for v in O]
 X=[sum(masses[j+1:],F(0)) for j in range(3)]
 direct=sum((v*t for v,t in zip(w,masses)),F(0))
 telescoped=sum(masses,F(0))/I+(w[1]-w[0])*X[0]-sum(((w[j]-w[j+1])*X[j] for j in range(1,3)),F(0))
 assert direct==telescoped
 # With a positive coefficient use an upper tail, with a negative one a lower.
 bound=sum(masses,F(0))/I+(w[1]-w[0])*(X[0]+F(1,100))-sum(((w[j]-w[j+1])*max(F(0),X[j]-F(1,100)) for j in range(1,3)),F(0))
 assert direct<=bound
 c=parent.controls();c.update(exact_nested_shell_weight_telescoping=True,upper_and_lower_tail_signs_checked=True)
 return c

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('263_high_mode_inverse');r262=get('262_prime_tail_source_1024');r261=get('261_materialized_source_fourier');reference=get('256_retained_band_inverse');kernel=get('115_rational_fourier_adjoint');forms=get('247_materialized_four_trial_response')
 pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper']);e_lower=sum((F(1,factorial(k)) for k in range(30)),F(0));rows=[]
 for parity,r in enumerate(prior['high_mode_inverse_response_certificates']):
  ref=reference['retained_band_inverse_response_certificates'][parity];s=r262['prime_tail_source_response_certificates'][parity]
  a=[F(v['coefficient']) for v in r261['materialized_source_Fourier_response_certificates'][parity]['retained_physical_source_center_0_through_512']]+[F(0)]*512
  for v in s['physical_source_centers_513_through_1024']:a[v['degree']]=F(v['physical_source_center'])
  A=F(r['retained_physical_polynomial_energy']);R=F(r['omitted_model_physical_energy_above_1024_upper']);delta=F(r['complete_finite_and_global_physical_error_norm_upper']);U=F(ref['rational_half_bandwidth'])
  assert A==sum((orig.mass(n)*v*v for n,v in enumerate(a)),F(0))
  # At new frequencies no old RC261 numerical tail is available. The helper's
  # principal-512 check is supplied the independently valid Parseval [0,A512].
  A512=sum((orig.mass(n)*v*v for n,v in enumerate(a[:513])),F(0));control={'outside_physical_Fourier_energy_lower':'0','outside_physical_Fourier_energy_upper':str(A512)}
  shells=[]
  for ratio in [F(3,2),F(2)]:
   V=ratio*U;Y,Acheck,proof=source.fourier(a,parity,V,pi0,pierr,control,reverse);assert Acheck==A
   principal_lo=proof.pop('independent_RC261_degree_512_control_lower');principal_hi=proof.pop('independent_RC261_degree_512_control_upper');proof.pop('degree_512_control_intersects')
   proof.update(principal_512_Parseval_control_lower=principal_lo,principal_512_Parseval_control_upper=principal_hi,principal_512_control_origin='Parseval [0,A512], not an old RC261 tail at this new frequency',principal_512_physical_energy=str(A512))
   K,kproof=high_trace(V,pi0+pierr,parity);Mlo,lproof=shell_lower(A,Y[0],R,K)
   loglo,loghi,lp=coercive.log_interval(V+e_lower)
   shells.append(dict(bandwidth_ratio=str(ratio),rational_half_bandwidth=str(V),retained_Fourier_certificate=proof,high_mode_trace_certificate=kproof,model_outside_energy_lower=str(Mlo),model_lower_controls=lproof,outside_log_lower=str(loglo),outside_log_upper=str(loghi),outside_log_control=lp))
   print('RC264 '+r['parity']+' shell '+str(ratio)+' model outside lower '+str(float(Mlo)),flush=True)
  assert F(shells[0]['retained_Fourier_certificate']['outside_physical_Fourier_energy_lower'])>F(shells[1]['retained_Fourier_certificate']['outside_physical_Fourier_energy_upper'])
  choices=[]
  for k in range(1000,2000):
   t=coercive.retained_band(F(k,10000),F(ref['original_canonical_reference_floor']),F(ref['original_low_band_penalty']),F(ref['unchanged_actual_rational_augmentation_coefficient']),F(ref['complete_canonical_J_to_Fhat_error_squared_upper']),F(r['outside_log_lower']))
   I=F(t['physical_inside_band_multiplier_lower']);O=F(t['physical_outside_band_multiplier_lower']);eta=F(t['canonical_metric_floor'])
   if I<=O:continue
   weights=[1/O]+[1/(eta*F(v['outside_log_lower'])) for v in shells]
   assert 0<weights[2]<weights[1]<weights[0]
   deductions=[down((weights[j]-weights[j+1])*F(v['model_outside_energy_lower'])) for j,v in enumerate(shells)]
   flat=up((A+R)/I+F(r['model_outside_Fourier_energy_upper'])*(1/O-1/I));model=up(flat-sum(deductions,F(0)));assert 0<model<=flat
   weightedfault=up(delta*root(1/O));correction=up((root(model)+weightedfault)**2)
   choices.append((correction,F(t['tau']),t,model,flat,weights,deductions,weightedfault))
  if reverse:choices.reverse()
  correction,_,selected,model,flat,weights,deductions,weightedfault=min(choices,key=lambda v:(v[0],v[1]))
  center=F(ref['direct_inverse_response_upper'])-F(ref['actual_augmented_inverse_correction_upper']);candidate=up(center+correction);upper=min(F(r['actual_original_action_inverse_response_upper']),candidate)
  f0=forms['parity_materialized_four_trial_response_certificates'][parity]['original_trial_form_intervals'][0][0];gap=max(F(r['actual_signed_gap_lower']),down(F(f0[0])-upper))
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],retained_physical_polynomial_energy=str(A),omitted_model_physical_energy_above_1024_upper=str(R),complete_finite_and_global_physical_error_norm_upper=str(delta),additional_frequency_shells=shells,selected_retained_band_multiplier_certificate=selected,outside_shell_inverse_weights=list(map(str,weights)),certified_model_weight_deductions=list(map(str,deductions)),flat_model_inverse_weight_upper=str(flat),shell_model_inverse_weight_upper=str(model),weighted_finite_and_global_fault_norm_upper=str(weightedfault),actual_inverse_correction_upper=str(correction),candidate_inverse_response_upper=str(candidate),actual_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(upper),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_inverse_upper_improved=upper<F(r['actual_original_action_inverse_response_upper']),actual_signed_gap_lower=str(gap),actual_signed_gap_upper=r['actual_signed_gap_upper'],signed_gap_positive_certified=gap>0,all_original_and_rational_augmentation_faults_paid=True))
  print('RC264 '+r['parity']+' inverse upper '+str(float(upper)),flush=True)
 return dict(milestone='RC264',starting_commit='551c3c6ac13dbbf7972356a6f73bcdcc3dca26f4',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,frequency_shell_inverse_response_certificates=rows,exact_controls=controls(),actual_response_source_count=2,response_trials_per_parity=4,retained_physical_source_degree_unchanged=1024,prime_output_cutoff_unchanged=2048,source_and_trial_spaces_unchanged=True,chosen_rational_augmentation_unchanged=True,finite_and_global_faults_paid_after_weighted_model_bound=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC265: optimize the response trial or tighten the remaining original model tail and global faults; full signed gate remains open')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC264 VALIDATED: nested Fourier-shell inverse; Stage I open',flush=True)
