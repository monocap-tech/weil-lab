"""RC263: high-Legendre band leakage and direct weighted source inverse bounds."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,hashlib,json
import validate_rpb108_rc262_prime_tail_source_1024 as parent
import validate_rpb108_rc256_retained_band_inverse as coercive
tail=parent.parent.parent
orig=parent.orig;B=parent.B;ROOT=parent.ROOT
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc262_prime_tail_source_1024.json':'00b1d3dfedcceda1f50289174a4d9bfe9294226f','notes/RPB108_RC262_PRIME_TAIL_SOURCE_1024_20261014.md':'9d0a5c3ceabef898a4496d885b021051ab4c357f'})
HELPER_PINS['scripts/validate_rpb108_rc262_prime_tail_source_1024.py']='ac22f7bf17d00733f1eeed4d7373f31dcbb6603f'
def controls():
 p=coercive.p;I=[[F(i==j) for j in range(3)] for i in range(3)]
 C=[[F(1,2),F(0),F(1,100)],[F(0),F(1,3),F(1,200)],[F(1,100),F(1,200),F(1,4)]];outside=p.add(I,C,-1)
 assert p.psd(C) and p.psd(outside) and p.mm(C,C)!=C
 inner=lambda a,M,b:sum((a[i]*M[i][j]*b[j] for i in range(3) for j in range(3)),F(0))
 v=[F(1),F(1),F(0)];q=[F(0),F(0),F(3,5)];A=inner(v,I,v);R=inner(q,I,q);Y=inner(v,outside,v);K=C[2][2];bandenergy=inner(v,C,v)
 assert inner(v,I,q)==0 and inner(q,C,q)<=K*R
 eps2=K*bandenergy*R;assert inner(v,C,q)**2<=eps2
 X=inner([a+b for a,b in zip(v,q)],outside,[a+b for a,b in zip(v,q)])
 assert Y-2*root(eps2)<=X<=Y+R+2*root(eps2)
 win=F(2);wout=F(5);W=p.add(p.scale(win,I),p.scale(wout-win,outside));M=win*(A+R)+(wout-win)*(Y+R+2*root(eps2))
 e=[F(1,1000),F(-1,1200),F(1,1500)];g=[a+b+c for a,b,c in zip(v,q,e)];delta=root(inner(e,I,e))
 assert inner(g,W,g)<=(root(M)+delta*root(wout))**2
 return dict(positive_compressed_band_not_assumed_projection=True,full_low_high_subspace_orthogonality=True,high_subspace_trace_band_energy_control=True,band_Cauchy_cross_bound=True,direct_weighted_global_fault_control=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('262_prime_tail_source_1024');reference=get('256_retained_band_inverse');kernel=get('115_rational_fourier_adjoint');forms=get('247_materialized_four_trial_response');e_lower=sum((F(1,factorial(k)) for k in range(30)),F(0));rows=[]
 for parity,r in enumerate(prior['prime_tail_source_response_certificates']):
  ref=reference['retained_band_inverse_response_certificates'][parity];fp=r['retained_source_Fourier_certificate'];A=F(fp['physical_polynomial_energy']);Ylo=F(fp['outside_physical_Fourier_energy_lower']);Yhi=F(fp['outside_physical_Fourier_energy_upper']);R=F(r['complete_model_physical_source_energy_beyond_1024_upper']);finite=F(r['retained_coefficient_uncertainty_physical_energy_upper']);fault=F(r['unchanged_global_physical_fault_norm_upper']);U=F(ref['rational_half_bandwidth']);lam=F(ref['unchanged_actual_rational_augmentation_coefficient'])
  # The same Poisson scalar is a trace upper bound for H C_U H on
  # matching-parity modes above 1024, with normalized Legendre basis.
  K,traceproof=tail.analytic_tail(U,F(kernel['rational_pi'])+F(kernel['rational_pi_error_upper']),F(1),parity)
  band_p=up(A-Ylo);eps=up(root(up(K*band_p*R)));assert 0<K<F(1,10**20)
  model_lo=max(F(0),down(Ylo-2*eps));model_hi=min(up(A+R),up(Yhi+R+2*eps));assert 0<=model_lo<=model_hi
  delta=up(root(finite)+fault);S=F(r['actual_full_source_physical_energy_upper'])
  Xlo=max(F(r['actual_full_source_outside_Fourier_energy_lower']),down(max(F(0),rootdown(model_lo)-delta)**2));Xhi=min(S,F(r['actual_full_source_outside_Fourier_energy_upper']),up((root(model_hi)+delta)**2));assert 0<=Xlo<=Xhi<=S
  loglo,loghi,logproof=coercive.log_interval(U+e_lower);assert loglo>F(ref['log_U_lower']);choices=[]
  for k in range(1000,2000):
   t=coercive.retained_band(F(k,10000),F(ref['original_canonical_reference_floor']),F(ref['original_low_band_penalty']),lam,F(ref['complete_canonical_J_to_Fhat_error_squared_upper']),loglo);inside=F(t['physical_inside_band_multiplier_lower']);outside=F(t['physical_outside_band_multiplier_lower'])
   if inside<=outside:continue
   model=up((A+R)/inside+model_hi*(1/outside-1/inside));weighted_fault=up(delta*root(1/outside));correction=up((root(model)+weighted_fault)**2)
   choices.append((correction,F(t['tau']),t,model,weighted_fault))
  if reverse:choices.reverse()
  correction,_,selected,modelweighted,weightedfault=min(choices,key=lambda v:(v[0],v[1]));center=F(ref['direct_inverse_response_upper'])-F(ref['actual_augmented_inverse_correction_upper']);candidate=up(center+correction);upper=min(F(r['actual_original_action_inverse_response_upper']),candidate);f0=forms['parity_materialized_four_trial_response_certificates'][parity]['original_trial_form_intervals'][0][0];gap=max(F(r['actual_signed_gap_lower']),down(F(f0[0])-upper))
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],retained_physical_source_degree_unchanged=1024,retained_physical_polynomial_energy=str(A),retained_outside_Fourier_energy_lower=str(Ylo),retained_outside_Fourier_energy_upper=str(Yhi),omitted_model_physical_energy_above_1024_upper=str(R),high_Legendre_compressed_band_trace_upper=str(K),unit_band_Poisson_trace_certificate=traceproof,retained_inside_band_physical_energy_upper=str(band_p),model_retained_omitted_band_cross_absolute_upper=str(eps),model_outside_Fourier_energy_lower=str(model_lo),model_outside_Fourier_energy_upper=str(model_hi),finite_physical_coefficient_uncertainty_energy_upper=str(finite),unchanged_global_physical_fault_norm_upper=str(fault),complete_finite_and_global_physical_error_norm_upper=str(delta),actual_full_source_physical_energy_upper=str(S),actual_full_source_outside_Fourier_energy_lower=str(Xlo),actual_full_source_outside_Fourier_energy_upper=str(Xhi),previous_full_source_outside_Fourier_energy_upper=r['actual_full_source_outside_Fourier_energy_upper'],outside_upper_improved=Xhi<F(r['actual_full_source_outside_Fourier_energy_upper']),exponential_one_positive_series_terms=30,exponential_one_lower=str(e_lower),outside_log_argument_lower=str(U+e_lower),outside_log_lower=str(loglo),outside_log_upper=str(loghi),outside_log_interval_control=logproof,selected_retained_band_multiplier_certificate=selected,weighted_model_source_inverse_correction_upper=str(modelweighted),weighted_finite_and_global_fault_norm_upper=str(weightedfault),actual_inverse_correction_upper=str(correction),candidate_inverse_response_upper=str(candidate),actual_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(upper),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_inverse_upper_improved=upper<F(r['actual_original_action_inverse_response_upper']),actual_signed_gap_lower=str(gap),actual_signed_gap_upper=r['actual_signed_gap_upper'],all_original_and_rational_augmentation_faults_paid=True,signed_gap_positive_certified=gap>0))
  print('RC263 '+r['parity']+' outside ['+str(float(Xlo))+','+str(float(Xhi))+']; inverse upper '+str(float(upper)),flush=True)
 return dict(milestone='RC263',starting_commit='7c7ed9587d0347daf2752d54447e556f690b6136',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,high_mode_inverse_response_certificates=rows,exact_controls=controls(),actual_response_source_count=2,response_trials_per_parity=4,source_and_trial_spaces_unchanged=True,retained_physical_source_degree_unchanged=1024,prime_output_cutoff_unchanged=2048,chosen_rational_augmentation_unchanged=True,high_mode_band_leakage_trace_paid=True,finite_and_global_faults_paid_after_weighted_model_bound=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC264: retain frequency variation in the inverse multiplier or optimize the response trial using the strengthened source bounds; full signed gate remains open')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC263 VALIDATED: high-mode band trace and weighted inverse bounds; Stage I open',flush=True)
