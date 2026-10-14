"""RC266: integrated rational-ellipse bounds for the unchanged augmentation."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc265_coupled_shell_remainder as parent
coercive=parent.coercive;ROOT=parent.ROOT;B=parent.parent.B;orig=parent.orig
up=parent.up;down=parent.down;root=parent.root
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc265_coupled_shell_remainder.json':'1971463e921046b0211c34a33ed9bf1d56e8d6e3','notes/RPB108_RC265_COUPLED_SHELL_REMAINDER_20261014.md':'3c654c5f49827e6f0ad47f94cd2d95f174de581d'})
HELPER_PINS['scripts/validate_rpb108_rc265_coupled_shell_remainder.py']='f7e14100e803dca0aecbf7a7615ee8b01cbbd916'

def grid(x,digits,upper):
 s=10**digits;return F(-((-x.numerator*s)//x.denominator) if upper else (x.numerator*s)//x.denominator,s)

def exp_negative_interval(x,reverse):
 assert 0<x<100
 N=440 if reverse else 400;digits=140 if reverse else 120
 lo=hi=F(1);lower=[lo];upper=[hi]
 for k in range(1,N):
  lo=grid(lo*x/k,digits,False);hi=grid(hi*x/k,digits,True);lower.append(lo);upper.append(hi)
 if reverse:lower.reverse();upper.reverse()
 elo=sum(lower,F(0));next_hi=grid(hi*x/N,digits,True);ratio=x/F(N+1);assert 0<ratio<1
 ehi=sum(upper,F(0))+next_hi/(1-ratio);assert 0<elo<ehi
 return grid(1/ehi,80,False),grid(1/elo,80,True)

def contour(radius,n,parity,U,pi_upper,reverse,parity_tail=True):
 assert radius>1
 loglo,loghi,lp=coercive.log_interval(radius);b=(radius-1/radius)/2;z=2*pi_upper*B*U
 first=n+(n%2!=parity) if parity_tail else n
 gap=first*loglo-z*b;assert gap>0
 enlo,enhi=exp_negative_interval(2*gap,reverse)
 factor=1/(1-1/radius**2) if parity_tail else radius/(radius-1)
 rectangle=up(16*B*U*factor**2*enhi)
 # Integrate exp(4*pi_upper*B*b*abs(xi)) before dropping its -1 term.
 integrated=up(4*factor**2*enhi/(pi_upper*b));assert 0<integrated<rectangle
 return integrated,dict(rational_contour_radius=str(radius),truncation_length_unchanged=n,first_omitted_degree=first,matching_parity_tail_only=parity_tail,log_radius_lower=str(loglo),log_radius_upper=str(loghi),log_radius_control=lp,ellipse_imaginary_semiaxis=str(b),phase_endpoint_upper=str(z),exponent_gap_lower=str(gap),negative_twice_gap_exponential_lower=str(enlo),negative_twice_gap_exponential_upper=str(enhi),positive_exponential_generation_terms=400,positive_exponential_replay_terms=440,positive_exponential_generation_grid_digits=120,positive_exponential_replay_grid_digits=140,geometric_Chebyshev_tail_factor=str(factor),physical_rectangle_Hilbert_Schmidt_squared_upper=str(rectangle),frequency_integrated_physical_Hilbert_Schmidt_squared_upper=str(integrated),frequency_integral_negative_one_discarded=True)

def controls():
 # Exact monomial/Chebyshev parity and physical moment annihilation.
 T=[[F(1)],[F(0),F(1)]]
 for n in range(1,10):
  v=[F(0)]+[2*c for c in T[n]]
  for j,c in enumerate(T[n-1]):v[j]-=c
  T.append(v)
 for n,t in enumerate(T):
  assert all(c==0 for k,c in enumerate(t) if k%2!=n%2)
  assert orig.integral(orig.product(t,[F(0),F(1)]))==0 if n%2==0 else orig.integral(t)==0
 for r in [F(3,2),F(8,5),F(2)]:
  for n in [5,6]:
   # First omitted matching degree and ratio r^-2 give the exact scalar sum.
   for parity in [0,1]:
    first=n+(n%2!=parity);partial=sum((r**(-j) for j in range(first,first+20,2)),F(0))
    assert partial+r**(-(first+20))/(1-r**-2)==r**(-first)/(1-r**-2)
 # Scalar J=1, E!=0 checks the actual product comparison, not a substitution.
 for J,E,z in [(F(1),F(-1,100),F(2,7)),(F(3,5),F(1,70),F(-3,11))]:
  d=abs(E);assert abs(((J+E)**2-J**2)*z)<=d*(2+d)*abs(z)
 c=parent.controls();c.update(exact_matching_parity_Chebyshev_tail_sum=True,opposite_parity_physical_moments_vanish=True,actual_rational_product_error_bound=True,canonical_error_uses_physical_inclusion_norm_at_most_one=True)
 return c

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('265_coupled_shell_remainder');r263=get('263_high_mode_inverse');r256=get('256_retained_band_inverse');r262=get('262_prime_tail_source_1024');kernel=get('115_rational_fourier_adjoint');oldtrial=get('248_direct_coupled_residual');forms=get('247_materialized_four_trial_response');rows=[]
 pi_upper=F(kernel['rational_pi'])+F(kernel['rational_pi_error_upper'])
 for parity,r in enumerate(prior['coupled_shell_remainder_response_certificates']):
  ref=r256['retained_band_inverse_response_certificates'][parity];src=kernel['parity_rational_Fourier_adjoint_sources'][parity];old=r263['high_mode_inverse_response_certificates'][parity]
  assert src['parity']==r['parity'];U=F(ref['rational_half_bandwidth']);n=src['Chebyshev_truncation_length'];lam=F(ref['unchanged_actual_rational_augmentation_coefficient']);assert U==F(src['rational_frequency_half_bandwidth'])
  # Radius-two all-degree rectangle recovers the inherited contour setup.
  _,legacy=contour(F(2),n,parity,U,pi_upper,reverse,False)
  assert F(legacy['physical_rectangle_Hilbert_Schmidt_squared_upper'])<F(src['finite_model_squared_J_approximation_error_upper'])
  ellipses=[contour(F(k,100),n,parity,U,pi_upper,reverse) for k in range(145,181)]
  if reverse:ellipses.reverse()
  hs,selected=min(ellipses,key=lambda v:(v[0],F(v[1]['rational_contour_radius'])))
  # Re-derive a physical kernel bound for X_exact-Xhat, including pi/Taylor.
  e0=F(src['rational_pi_phase_error_upper'])+F(src['real_imaginary_axis_Taylor_remainder_upper'])
  finite=16*n*n*B*U*e0*e0
  finite=max(finite,F(src['finite_model_operator_error_squared_upper']))
  delta2=up((root(hs)+root(finite))**2);assert 0<delta2<F(ref['complete_canonical_J_to_Fhat_error_squared_upper'])
  physical_delta=root(delta2);epsilon=up(physical_delta*(2+physical_delta))
  Z=list(map(F,oldtrial['selected_direct_residual_certificates'][parity]['exact_Z_input_Legendre_coefficients']));massZ=sum((orig.mass(j)*v*v for j,v in enumerate(Z)),F(0))
  rational=up(lam*lam*epsilon*epsilon*massZ)
  physical=ref['actual_physical_residual_source_certificate'];original_faults=physical['original_global_physical_squared_faults'];oldrational=F(physical['rational_augmentation_physical_squared_fault_upper']);assert rational<oldrational
  original_fault_norm=up(sum((root(F(v)) for v in original_faults.values()),F(0)));globalnorm=up(original_fault_norm+root(rational))
  finite_source=F(r262['prime_tail_source_response_certificates'][parity]['retained_coefficient_uncertainty_physical_energy_upper']);delta=up(root(finite_source)+globalnorm);assert delta<F(r['complete_finite_and_global_physical_error_norm_upper'])
  A=F(r['retained_physical_polynomial_energy']);R=F(r['omitted_model_physical_energy_above_1024_upper']);shells=r['frequency_shells'];gamma=F(ref['original_canonical_reference_floor']);penalty=F(ref['original_low_band_penalty'])
  taus={F(k,10000) for k in range(1000,2000)}|{F(k,10**j) for j in range(3,10) for k in range(1,100)};choices=[]
  for tau in sorted(taus,reverse=reverse):
   if gamma-lam*(1/tau-1)*delta2<=0:continue
   t=coercive.retained_band(tau,gamma,penalty,lam,delta2,F(old['outside_log_lower']));I=F(t['physical_inside_band_multiplier_lower']);O=F(t['physical_outside_band_multiplier_lower']);eta=F(t['canonical_metric_floor'])
   if I<=O:continue
   weights=[1/O]+[1/(eta*F(v['outside_log_lower'])) for v in shells]
   model,constant,flat,coef,details=parent.joint_bound(A,R,F(old['retained_outside_Fourier_energy_upper']),F(old['model_retained_omitted_band_cross_absolute_upper']),I,weights,shells)
   wf=up(delta*root(1/O));correction=up((root(model)+wf)**2);choices.append((correction,tau,t,model,coef,details,weights,wf))
  correction,_,t,model,coef,details,weights,wf=min(choices,key=lambda v:(v[0],v[1]))
  center=F(ref['direct_inverse_response_upper'])-F(ref['actual_augmented_inverse_correction_upper']);candidate=up(center+correction);upper=min(F(r['actual_original_action_inverse_response_upper']),candidate)
  f0=forms['parity_materialized_four_trial_response_certificates'][parity]['original_trial_form_intervals'][0][0];gap=max(F(r['actual_signed_gap_lower']),down(F(f0[0])-upper))
  assert F(r['actual_original_action_inverse_response_lower'])<=upper and gap<=F(r['actual_signed_gap_upper'])
  if gap>0:assert upper<F(f0[0])
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],radius_two_all_degree_contour_control=legacy,rational_ellipse_candidate_count=len(ellipses),all_rational_ellipse_certificates=[v[1] for v in sorted(ellipses,key=lambda v:F(v[1]['rational_contour_radius']))],selected_integrated_contour_certificate=selected,finite_rational_kernel_physical_error_squared_upper=str(finite),complete_physical_and_canonical_J_to_Fhat_error_squared_upper=str(delta2),previous_canonical_J_to_Fhat_error_squared_upper=ref['complete_canonical_J_to_Fhat_error_squared_upper'],unchanged_Z_physical_energy=str(massZ),physical_Fhat_product_to_ideal_band_operator_norm_upper=str(epsilon),rational_augmentation_physical_squared_fault_upper=str(rational),previous_rational_augmentation_physical_squared_fault_upper=str(oldrational),unchanged_original_global_physical_squared_faults=original_faults,unchanged_original_global_physical_fault_norm_upper=str(original_fault_norm),complete_global_physical_fault_norm_upper=str(globalnorm),unchanged_finite_coefficient_uncertainty_physical_energy_upper=str(finite_source),complete_finite_and_global_physical_error_norm_upper=str(delta),previous_complete_finite_and_global_physical_error_norm_upper=r['complete_finite_and_global_physical_error_norm_upper'],retained_physical_polynomial_energy=str(A),omitted_model_physical_energy_above_1024_upper=str(R),tau_candidate_count=len(taus),admissible_tau_candidate_count=len(choices),selected_retained_band_multiplier_certificate=t,outside_shell_inverse_weights=list(map(str,weights)),selected_joint_shell_controls=details,joint_omitted_energy_quadratic_coefficient=str(coef),coupled_shell_model_inverse_upper=str(model),weighted_finite_and_global_fault_norm_upper=str(wf),actual_inverse_correction_upper=str(correction),candidate_inverse_response_upper=str(candidate),actual_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(upper),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_inverse_upper_improved=upper<F(r['actual_original_action_inverse_response_upper']),actual_signed_gap_lower=str(gap),actual_signed_gap_upper=r['actual_signed_gap_upper'],signed_gap_positive_certified=gap>0,all_original_and_rational_augmentation_faults_paid=True))
  print('RC266 '+r['parity']+' comparison delta squared '+str(float(delta2))+'; inverse upper '+str(float(upper))+'; signed gap lower '+str(float(gap)),flush=True)
 return dict(milestone='RC266',starting_commit='e27e100e5e3e32d3d8c2d53244fad2d3771e1428',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,integrated_contour_response_certificates=rows,exact_controls=controls(),individual_source_signed_gap_positive_certified_parities=[r['parity'] for r in rows if r['signed_gap_positive_certified']],actual_response_source_count=2,response_trials_per_parity=4,retained_physical_source_degree_unchanged=1024,prime_output_cutoff_unchanged=2048,source_and_trial_spaces_unchanged=True,chosen_rational_augmentation_unchanged=True,rational_augmentation_not_replaced_by_ideal_band=True,canonical_and_physical_operator_comparison_rederived=True,finite_and_global_faults_paid_after_weighted_model_bound=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC267: improve the remaining even source inverse bound or optimize its response trial, and extend beyond the two source tests; full signed gate remains open')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC266 VALIDATED: integrated contour for unchanged rational augmentation; Stage I open',flush=True)
