"""RC257: exact full retained-source Fourier tail and complete source envelope."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from functools import lru_cache
import argparse, hashlib, json
import validate_rpb108_rc256_retained_band_inverse as parent
import validate_rpb108_rc251_extended_coupled_residual as moment
import validate_rpb108_rc243_residual_augmented_actions as independent
orig=parent.orig; B=parent.B; up=parent.up; down=parent.down
root=parent.root; rootdown=parent.rootdown; ROOT=parent.ROOT
PINS=dict(parent.PINS); HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc256_retained_band_inverse.json':'7ccea9f125fbeb6ad8fc25f490b88c369dc017f0','notes/RPB108_RC256_RETAINED_BAND_INVERSE_20261014.md':'4c3ff7121f10f584bb875759c2ce0ad345ac55ab'})
HELPER_PINS['scripts/validate_rpb108_rc256_retained_band_inverse.py']='cefb3eec88b9f3d0a588e11e0c0f3276cbed267b'
@lru_cache(None)
def phase_pi():
 # Machin's identity with alternating arctangent remainder bounds.
 terms=600
 def atan(q):
  s=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(terms)),F(0))
  e=F(1,(2*terms+1)*q**(2*terms+1)); return s,s+e
 a=atan(5); b=atan(239)
 lo,hi=moment.outer_grid((16*a[0]-4*b[1],16*a[1]-4*b[0]),450)
 assert F(3)<lo<hi<F(22,7)
 return (lo+hi)/2,(hi-lo)/2
def leakage(a,parity,U,pi0,pierr,reverse=False):
 # Unscaled moments avoid unstable high-order asymptotic expansions.
 old=moment.band.CUT
 try:
  moment.band.CUT=len(a)-1; aa,bb=moment.band.spherical_polynomials()
 finally: moment.band.CUT=old
 A=[F(0)]*(len(a)+1); C=A.copy()
 for n,c in enumerate(a):
  if not c: continue
  assert n%2==parity
  sign=(-1)**((n-parity)//2)
  for k,v in enumerate(aa[n]): A[k]+=sign*c*v
  for k,v in enumerate(bb[n]): C[k]+=sign*c*v
 z=2*pi0*B*U; assert z>400
 turns=int(2*B*U+F(1,2)); pi1,pi1err=phase_pi()
 theta_exact=2*z-2*turns*pi1
 tl,th=moment.outer_grid((theta_exact,theta_exact),400); theta=(tl+th)/2
 thetaerr=(th-tl)/2+2*abs(turns)*pi1err; assert abs(theta)+thetaerr<F(22,7)
 terms=220
 ct=moment.ip(F(1)); st=moment.ip(theta); cv=ct; sv=st
 for k in range(1,terms):
  ct=moment.outer_grid(moment.isc(ct,-theta*theta/F((2*k-1)*(2*k))),800)
  st=moment.outer_grid(moment.isc(st,-theta*theta/F((2*k)*(2*k+1))),800)
  cv=moment.outer_grid(moment.ia(cv,ct),800); sv=moment.outer_grid(moment.ia(sv,st),800)
 # Pay phase reduction with a sharper independent Machin interval, while
 # retaining the original pinned pi error for the operator comparison.
 pe=F(22,7)**(2*terms)/factorial(2*terms)+F(22,7)**(2*terms+1)/factorial(2*terms+1)+thetaerr
 cosine=moment.outer_grid((cv[0]-pe,cv[1]+pe),800); sine=moment.outer_grid((sv[0]-pe,sv[1]+pe),800)
 L=520 if reverse else 500
 powers=[(2*z.numerator)**k for k in range(L)]
 rr,ii,rem=moment.ibp_parts(2,L,z,powers)
 R=(rr-rem,rr+rem); I=(ii-rem,ii+rem)
 re=moment.outer_grid(moment.isc(moment.ia(moment.im(cosine,R),moment.neg(moment.im(sine,I))),1/z**2),1600)
 im=moment.outer_grid(moment.isc(moment.ia(moment.im(sine,R),moment.im(cosine,I)),1/z**2),1600)
 moments={2:(re,im)}
 for m in range(3,2*len(a)+2):
  # (m-1) I_m = 2 i I_(m-1) + exp(2 i z) z^(1-m).
  nr=moment.isc(moment.ia(moment.isc(im,-2),moment.isc(cosine,z**(1-m))),F(1,m-1))
  ni=moment.isc(moment.ia(moment.isc(re,2),moment.isc(sine,z**(1-m))),F(1,m-1))
  re=moment.outer_grid(nr,1600); im=moment.outer_grid(ni,1600); moments[m]=(re,im)
 pa=orig.product(A,A); pb=orig.product(C,C); pc=orig.product(A,C)
 total=(F(0),F(0)); degrees=list(range(2,len(pa)))
 if reverse: degrees.reverse()
 for m in degrees:
  total=moment.ia(total,moment.ip((pa[m]+pb[m])/2*z**(1-m)/F(m-1)))
  total=moment.ia(total,moment.isc(moments[m][0],(pb[m]-pa[m])/2))
  total=moment.ia(total,moment.isc(moments[m][1],pc[m]))
 S=sum(map(abs,a),F(0)); pil=pi0-pierr
 fault=up(S*S*(4*B/pil*(2*B*U*pierr)+8*B*pierr/(pil*pi0)))
 raw=moment.isc(total,4*B/pi0)
 result=moment.band.outer24((raw[0]-fault,raw[1]+fault))
 mass=sum((orig.mass(n)*c*c for n,c in enumerate(a)),F(0))
 assert 0<result[0]<=result[1]<mass
 return result,dict(retained_degree=len(a)-1,all_mode_cross_terms_combined_before_squaring=True,oscillatory_moment_recurrence='(m-1) I_m = 2 i I_(m-1) + exp(2 i z) z^(1-m)',base_IBP_generation_terms=500,base_IBP_replay_terms=520,rational_phase_Taylor_terms=terms,phase_Machin_arctangent_terms=600,phase_pi_grid_digits=450,phase_argument_grid_digits=400,phase_grid_digits=800,unscaled_moment_grid_digits=1600,actual_pi_displacement_and_prefactor_squared_source_fault_upper=str(fault),physical_polynomial_energy=str(mass),outside_physical_Fourier_energy_lower=str(result[0]),outside_physical_Fourier_energy_upper=str(result[1]),inside_physical_Fourier_energy_lower=str(down(mass-result[1])),inside_physical_Fourier_energy_upper=str(up(mass-result[0])))
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes(); assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'): data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('256_retained_band_inverse'); centers=get('251_extended_coupled_residual'); metric=get('129_four_vector_joint_moment'); kernel=get('115_rational_fourier_adjoint')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B); sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B); sm=(sl+sh)/2
 harmonics=[F(0)]
 for n in range(1,257): harmonics.append(harmonics[-1]+F(1,n))
 bounds=get('232_augmented_polynomial_action')['polynomial_augmented_action_certificates'][0]
 toy=[F(1),F(0),F(-1,3)]
 toyargs=(toy,0,F(bounds['rational_frequency_half_bandwidth']),F(kernel['rational_pi']),F(kernel['rational_pi_error_upper']),reverse)
 control_new,_=leakage(*toyargs); control_old,_=independent.leakage(*toyargs)
 assert max(control_new[0],control_old[0])<=min(control_new[1],control_old[1])
 rows=[]
 for parity,r in enumerate(prior['retained_band_inverse_response_certificates']):
  c=centers['extended_coupled_residual_response_certificates'][parity]; a=[(harmonics[n]+sm)*F(v['coefficient']) for n,v in enumerate(c['extended_complete_direct_residual_center'])]
  tail,proof=leakage(a,parity,F(r['rational_half_bandwidth']),F(kernel['rational_pi']),F(kernel['rational_pi_error_upper']),reverse)
  src=r['actual_physical_residual_source_certificate']; finite=F(src['finite_coefficient_and_actual_s_uncertainty_physical_energy_upper']); omitted=F(src['complete_model_physical_output_beyond_256_upper']); fault=F(src['complete_global_physical_fault_norm_upper']); S=F(src['complete_actual_physical_source_energy_upper'])
  error=up(root(finite+omitted)+fault)
  X=min(S,up((root(tail[1])+error)**2)); Xlo=down(max(F(0),rootdown(tail[0])-error)**2)
  budget=r['conditional_two_band_budget']; limit=F(budget['sufficient_strict_outside_physical_Fourier_energy_upper']); inside=F(budget['inside_inverse_denominator']); outside=F(budget['outside_inverse_denominator']); assert inside>outside>0
  choices=[]
  for j in range(1000,2000):
   choice=parent.retained_band(F(j,10000),F(r['original_canonical_reference_floor']),F(r['original_low_band_penalty']),F(r['unchanged_actual_rational_augmentation_coefficient']),F(r['complete_canonical_J_to_Fhat_error_squared_upper']),F(r['log_U_lower']))
   I=F(choice['physical_inside_band_multiplier_lower']); O=F(choice['physical_outside_band_multiplier_lower'])
   if I>O: choices.append((up(S/I+X*(1/O-1/I)),F(choice['tau']),choice))
  if reverse: choices.reverse()
  correction,_,choice=min(choices,key=lambda v:(v[0],v[1]))
  oldcorr=F(r['actual_augmented_inverse_correction_upper']); centerupper=F(r['direct_inverse_response_upper'])-oldcorr
  candidate=up(centerupper+correction); Tupper=min(F(r['actual_original_action_inverse_response_upper']),candidate)
  # This is an obstruction to this particular triangle envelope only.
  envelope_floor=up(error*error); assert envelope_floor>limit
  forms=get('247_materialized_four_trial_response')['parity_materialized_four_trial_response_certificates'][parity]
  gaplower=max(F(r['actual_signed_gap_lower']),down(F(forms['original_trial_form_intervals'][0][0][0])-Tupper))
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],retained_physical_source_Fourier_certificate=proof,finite_and_omitted_source_error_orthogonal_before_global_faults=True,complete_physical_source_error_norm_upper=str(error),actual_full_source_outside_Fourier_energy_lower=str(Xlo),actual_full_source_outside_Fourier_energy_upper=str(X),strict_two_band_budget=str(limit),current_outside_envelope_meets_budget=X<limit,triangle_envelope_floor_with_zero_retained_leakage=str(envelope_floor),triangle_envelope_floor_exceeds_budget=envelope_floor>limit,actual_source_outside_energy_exceeds_budget_proved=Xlo>limit,selected_two_band_multiplier_certificate=choice,complete_two_band_inverse_correction_upper=str(correction),candidate_inverse_response_upper=str(candidate),actual_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(Tupper),previous_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_inverse_upper_improved=Tupper<F(r['actual_original_action_inverse_response_upper']),actual_signed_gap_lower=str(gaplower),actual_signed_gap_upper=r['actual_signed_gap_upper'],all_original_and_rational_augmentation_faults_paid=True))
  print('RC257 '+r['parity']+' retained Fourier tail '+str(float(tail[1]))+'; full upper '+str(float(X)),flush=True)
 return dict(milestone='RC257',starting_commit='08cd38aeefcaed789de95df6d1822db3d8035324',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,physical_source_Fourier_tail_certificates=rows,exact_controls=dict(independent_RC243_per_order_IBP_agrees_with_unscaled_forward_moment_recurrence=True,toy_aggregate_coefficients=list(map(str,toy))),actual_response_source_count=2,response_trials_per_parity=4,full_retained_source_degree=256,full_actual_source_outside_Fourier_energy_enclosed=True,source_and_trial_spaces_unchanged=True,chosen_rational_augmentation_unchanged=True,triangle_envelope_obstruction_not_actual_operator_obstruction=True,original_Weil_positive_floor_claimed=False,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC258: resolve omitted physical source output jointly in Fourier space or change the response trial; shrinking retained polynomial leakage alone cannot meet the present triangle-envelope budget')
if __name__=='__main__':
 ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--replay',action='store_true'); args=ap.parse_args(); result=run(args.replay)
 if args.replay: assert result==json.loads(args.output.read_text())
 else: args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC257 VALIDATED: full-source Fourier enclosure; two-band closure and Stage I open',flush=True)
