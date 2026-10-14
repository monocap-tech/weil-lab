"""RC252: signed endpoint moments and a parity telescoping tail bound."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc251_extended_coupled_residual as parent
direct=parent.direct;native=direct.native;orig=parent.orig;p=parent.p;B=parent.B
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
ROOT=Path(__file__).resolve().parents[1];END=1024;ORDER=4
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc251_extended_coupled_residual.json':'1cf487bc35ff7aeef0cdf9cc63f324fdad0ccc65','notes/RPB108_RC251_EXTENDED_COUPLED_RESIDUAL_20261014.md':'6ea17fd15ee2e28157337ea3a9a013df67a987e5'})
HELPER_PINS['scripts/validate_rpb108_rc251_extended_coupled_residual.py']='8bf302a2f818633c5812833042507f947584ff23'
def tail_bound(a,first,sl,harmonics):
 x=F(first*(first+1));ts=[F(d*(d+1)) for d in range(len(a))];tmax=max(ts);assert x>tmax
 moments=[sum((c*t**k for c,t in zip(a,ts)),F(0)) for k in range(ORDER)]
 absolute=sum((abs(c)*t**ORDER for c,t in zip(a,ts)),F(0));remainder=absolute/(x**ORDER*(1-tmax/x))
 # x*sum a_d/(x-t_d) = sum M_k/x^k + remainder(x).
 # Signed M_k remain combined; only the final geometric remainder loses signs.
 lo=moments[0]+sum((min(F(0),moments[k])/x**k for k in range(1,ORDER)),F(0))-remainder
 hi=moments[0]+sum((max(F(0),moments[k])/x**k for k in range(1,ORDER)),F(0))+remainder
 assert 0<lo<=hi
 f=lambda n:F(1,n*n)-F(1,(n+1)**2)
 # f decreases, sum over both parities telescopes to 1/first^2,
 # and its alternating sum is at most f(first).
 parity_sum=(F(1,first*first)+f(first))/2
 energy=up(2*B*hi*hi*parity_sum/(harmonics[first]+sl))
 return energy,dict(first_omitted_degree=first,geometric_expansion_order=ORDER,signed_input_moments=list(map(str,moments)),absolute_order_four_moment=str(absolute),maximum_input_d_times_d_plus_one=str(tmax),uniform_geometric_remainder_upper=str(up(remainder)),uniform_combined_endpoint_bracket_lower=str(down(lo)),uniform_combined_endpoint_bracket_upper=str(up(hi)),positive_bracket_certified=True,parity_telescoping_weight_sum_upper=str(up(parity_sum)),harmonic_weight_lower=str(harmonics[first]+sl),endpoint_D_omitted_energy_upper=str(energy))
def endpoint_refinement(a,parity,sl,harmonics,reverse):
 first=257 if parity else 258;last=1023 if parity else 1024;nextfirst=1025 if parity else 1026
 simple,control=tail_bound(a,first,sl,harmonics);remaining,remaining_control=tail_bound(a,nextfirst,sl,harmonics)
 ll=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0));lh=ll+2*F(1,3)**201/(201*(1-F(1,9)));terms=[];coeff=[]
 degrees=list(range(first,last+1,2));degrees=degrees[::-1] if reverse else degrees
 for n in degrees:
  h,rad=native.endpoint(a,n,ll,lh);assert rad==0
  x=F(n*(n+1));direct_h=(2*n+1)*sum((c/(x-d*(d+1)) for d,c in enumerate(a)),F(0));assert h==direct_h
  bracket=x*h/F(2*n+1);assert F(control['uniform_combined_endpoint_bracket_lower'])<=bracket<=F(control['uniform_combined_endpoint_bracket_upper'])
  terms.append(dict(degree=n,endpoint_D_energy_upper=str(up(orig.mass(n)*h*h/(harmonics[n]+sl)))));coeff.append((n,h))
 terms.sort(key=lambda row:row['degree']);coeff.sort();energies=[F(row['endpoint_D_energy_upper']) for row in terms]
 if reverse:energies.reverse()
 explicit=up(sum(energies,F(0)));refined=up(explicit+remaining);accepted=min(simple,refined)
 digest=native.segment_digest([(F(first),F(last),[h for n,h in coeff])])
 return accepted,dict(direct_uniform_moment_bound=control,explicit_endpoint_output_energy_257_through_1024=terms,explicit_endpoint_coefficient_sha256=digest,explicit_endpoint_output_count=len(terms),explicit_endpoint_D_energy_upper=str(explicit),remaining_beyond_1024=remaining_control,explicit_plus_remaining_endpoint_D_energy_upper=str(refined),accepted_endpoint_D_energy_beyond_256_upper=str(accepted),all_input_cross_terms_retained_in_explicit_output=True,actual_log2_coefficient_uncertainty_zero_on_this_tail=True)
def controls():
 # Verify the geometric identity as a polynomial, for every actual input degree.
 for d in range(65):
  t=F(d*(d+1));q=[t**(ORDER-1-k) for k in range(ORDER)];identity=orig.product(q,[-t,F(1)]);identity[0]+=t**ORDER
  assert identity==[F(0)]*ORDER+[F(1)]
 # Clearing denominators in f(n)-f(n+1) yields a positive polynomial.
 a=orig.product([F(1),F(1)],[F(1),F(1)]);b=orig.product([F(2),F(1)],[F(2),F(1)]);c=[F(0),F(0),F(1)]
 ab=orig.product(a,b);cb=orig.product(c,b);ca=orig.product(c,a)
 numerator=[ab[k]-2*cb[k]+ca[k] for k in range(5)];assert numerator==[F(4),F(12),F(6),F(0),F(0)]
 for first in [257,258,1025,1026]:
  f=lambda n:F(1,n*n)-F(1,(n+1)**2)
  for count in [1,2,17]:assert sum((f(n) for n in range(first,first+count)),F(0))==F(1,first*first)-F(1,(first+count)**2)
 return dict(exact_geometric_polynomial_identity_all_input_degrees=True,positive_finite_difference_polynomial=True,telescoping_weight_identity=True,parity_alternating_tail_bound=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('251_extended_coupled_residual');old=get('248_direct_coupled_residual');tails=get('250_coupled_original_output_tail');forms=get('247_materialized_four_trial_response');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);harmonics=[F(0)]
 for n in range(1,END+3):harmonics.append(harmonics[-1]+F(1,n))
 for n in [257,258,1025,1026]:assert harmonics[n]==orig.H(n)
 rows=[]
 for parity,r in enumerate(prior['extended_coupled_residual_response_certificates']):
  oldr=old['selected_direct_residual_certificates'][parity];a=list(map(F,oldr['original_combination_action_certificate']['exact_original_combination_input']));endpoint,proof=endpoint_refinement(a,parity,sl,harmonics,reverse)
  oldproof=tails['coupled_output_tail_response_certificates'][parity]['coupled_original_output_tail_certificate'];oldendpoint=F(oldproof['endpoint_D_energy_beyond_256_upper']);endpoint=min(endpoint,oldendpoint);prime=F(oldproof['prime_weighted_D_energy_beyond_256_upper']);neworiginal=up((root(endpoint)+root(prime))**2);assert neworiginal<=F(r['original_combination_D_omitted_output_energy_upper'])
  augmentation=F(r['augmentation_D_omitted_output_energy_upper']);omitted=up((root(neworiginal)+root(augmentation))**2);finite=F(r['residual_finite_rounding_D_energy_upper']);fault=F(r['unchanged_original_model_fault_D_norm_upper']);rational=F(r['unchanged_rational_augmentation_comparison_D_error_squared_upper']);E=up((root(up(finite+omitted))+fault+root(rational))**2);assert E<=F(r['complete_direct_residual_D_error_squared_upper'])
  residual=r['extended_complete_direct_residual_center'];degrees=list(range(257));degrees=degrees[::-1] if reverse else degrees
  nl=sum((orig.mass(n)*(orig.H(n)+sl)*F(residual[n]['coefficient'])**2 for n in degrees),F(0));nh=sum((orig.mass(n)*(orig.H(n)+sh)*F(residual[n]['coefficient'])**2 for n in degrees),F(0));rl=down(max(F(0),rootdown(nl)-root(E))**2);rh=up((root(nh)+root(E))**2)
  b=bounds['polynomial_augmented_action_certificates'][parity];mu=F(b['fresh_augmented_N_D_lower']);nu=F(b['fresh_augmented_N_D_upper']);lam=F(b['augmentation_coefficient']);pr=forms['parity_materialized_four_trial_response_certificates'][parity];F0=[[(F(a),F(b)) for a,b in row] for row in pr['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in pr['frequency_trial_Gram_intervals']];y=list(map(F,r['selected_trial_coefficients']))
  cl,ch=direct.center_intervals(F0,Gy,y,lam);tl=down(cl+rl/nu);th=up(ch+rh/mu);u=[1-y[0],-y[1],-y[2],-y[3]];ql,qh=direct.quadratic(F0,u);al,ah=direct.quadratic(Gy,y);dl=down(ql+lam*al-rh/mu);dh=up(qh+lam*ah-rl/nu)
  actualtl=max(F(r['actual_original_action_inverse_response_lower']),tl);actualth=min(F(r['actual_original_action_inverse_response_upper']),th);actualdl=max(F(r['actual_signed_gap_lower']),dl,down(F0[0][0][0]-actualth));actualdh=min(F(r['actual_signed_gap_upper']),dh,up(F0[0][0][1]-actualtl));assert actualtl<=actualth and actualdl<=actualdh
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],unchanged_retained_residual_center_origin='RC251 degree 256',signed_endpoint_tail_certificate=proof,previous_endpoint_D_energy_beyond_256_upper=str(oldendpoint),accepted_endpoint_D_energy_beyond_256_upper=str(endpoint),unchanged_prime_D_energy_beyond_256_upper=str(prime),new_original_combination_D_energy_beyond_256_upper=str(neworiginal),unchanged_augmentation_D_energy_beyond_256_upper=str(augmentation),residual_model_omitted_output_D_energy_upper=str(omitted),complete_direct_residual_D_error_squared_upper=str(E),previous_direct_residual_D_error_squared_upper=r['complete_direct_residual_D_error_squared_upper'],complete_direct_residual_actual_D_energy_lower=str(rl),complete_direct_residual_actual_D_energy_upper=str(rh),direct_inverse_response_lower=str(tl),direct_inverse_response_upper=str(th),direct_signed_gap_lower=str(dl),direct_signed_gap_upper=str(dh),actual_original_action_inverse_response_lower=str(actualtl),actual_original_action_inverse_response_upper=str(actualth),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(actualdl),actual_signed_gap_upper=str(actualdh),original_action_inverse_upper_improved=actualth<F(r['actual_original_action_inverse_response_upper']),signed_gap_positive_certified=actualdl>0,actual_negative_gap_proved=actualdh<0))
 return dict(milestone='RC252',starting_commit='efc004271794aa8a893b3ced386adab079d01b9d',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,signed_endpoint_tail_response_certificates=rows,source_and_trial_spaces_unchanged=True,retained_direct_residual_output_degree_unchanged=256,endpoint_tail_explicit_degree=END,all_original_and_rational_augmentation_model_faults_preserved=True,exact_controls=controls(),new_response_enclosures_intersected_with_RC251=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC253: sharpen the remaining prime or band omitted output, or strengthen the residual inverse estimate; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC252 VALIDATED: signed endpoint moments and parity tail; full signed gate open',flush=True)
