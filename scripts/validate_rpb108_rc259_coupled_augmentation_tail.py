"""RC259: materialize band output 257..512 and couple the physical source tail."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,hashlib,json
import validate_rpb108_rc258_orthogonal_physical_tail as parent
import validate_rpb108_rc253_prime_boundary_tail as prime
fourier=parent.parent; m=fourier.moment; band=m.band
orig=parent.orig;B=parent.B;ROOT=parent.ROOT
up=parent.up;down=parent.down;root=parent.root
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc258_orthogonal_physical_tail.json':'8b1c466bcac6fcffbd3047bc2a30b58aa54de270','notes/RPB108_RC258_ORTHOGONAL_PHYSICAL_TAIL_20261014.md':'3d3633823c5a8e2d8fcac250657107fdb6fe0819'})
HELPER_PINS['scripts/validate_rpb108_rc258_orthogonal_physical_tail.py']='97afbf0fbc69d202f08b75e52992e9c526c7cc77'
END=512
def bessel_values(U,pi0,reverse):
 z=2*pi0*B*U;assert z>400;turns=int(B*U+F(1,2));pi1,pi1err=fourier.phase_pi()
 tl,th=m.outer_grid((z-2*turns*pi1,z-2*turns*pi1),400);theta=(tl+th)/2;thetaerr=(th-tl)/2+2*abs(turns)*pi1err
 assert abs(theta)+thetaerr<F(22,7)
 ct=m.ip(F(1));st=m.ip(theta);cv=ct;sv=st
 terms=240 if reverse else 220
 for k in range(1,terms):
  ct=m.outer_grid(m.isc(ct,-theta*theta/F((2*k-1)*(2*k))),800);st=m.outer_grid(m.isc(st,-theta*theta/F((2*k)*(2*k+1))),800)
  cv=m.outer_grid(m.ia(cv,ct),800);sv=m.outer_grid(m.ia(sv,st),800)
 pe=F(22,7)**(2*terms)/factorial(2*terms)+F(22,7)**(2*terms+1)/factorial(2*terms+1)+thetaerr
 cosine=m.outer_grid((cv[0]-pe,cv[1]+pe),800);sine=m.outer_grid((sv[0]-pe,sv[1]+pe),800)
 digits=620 if reverse else 600
 j=[m.outer_grid(m.isc(sine,1/z),digits),m.outer_grid(m.ia(m.isc(sine,1/z**2),m.isc(cosine,-1/z)),digits)]
 for n in range(1,END):j.append(m.outer_grid(m.ia(m.isc(j[n],F(2*n+1)/z),m.neg(j[n-1])),digits))
 derivative=[m.neg(j[1])]+[m.outer_grid(m.ia(j[n-1],m.isc(j[n],-F(n+1)/z)),digits) for n in range(1,END+1)]
 return z,j,derivative
def ode_controls(aa,bb):
 def dp(A):return [F(0)]+[-k*c for k,c in enumerate(A)]
 def derivative(A,C):return band.polyadd(dp(A),[-v for v in C]),band.polyadd(A,dp(C))
 for n in [0,1,2,64,128,256,512]:
  A,C=aa[n],bb[n];dA,dC=derivative(A,C);ddA,ddC=derivative(dA,dC)
  for v,dv,ddv in [(A,dA,ddA),(C,dC,ddC)]:
   result=band.polyadd(band.polyadd(ddv,[F(0)]+[2*x for x in dv]),band.polyadd(v,[F(0),F(0)]+[-n*(n+1)*x for x in v]));assert not any(result)
 return True
def window(a,parity,U,pi0,pierr,oldgram,reverse):
 oldcut=band.CUT
 try:band.CUT=END;aa,bb=band.spherical_polynomials()
 finally:band.CUT=oldcut
 assert len(a)==65;assert ode_controls(aa,bb)
 z,j,dj=bessel_values(U,pi0,reverse);pil=pi0-pierr;S=sum(map(abs,a),F(0))
 fault=up(S*(4*B/pil*(2*B*U*pierr)+8*B*pierr/(pil*pi0)))
 output=[];controls=[parity+66,parity+128,255 if parity else 256]
 degrees=sorted(set(controls+list(range(257,END+1))))
 for n in degrees:
  if n%2!=parity:continue
  terms=[];assert n>64
  for d,c in enumerate(a):
   if not c:continue
   assert d%2==n%2
   # Same-parity asymptotics give lim t^2 W(t)=0. The spherical
   # Sturm--Liouville identity integrates the off-diagonal product exactly.
   W=m.ia(m.im(dj[n],j[d]),m.neg(m.im(j[n],dj[d])))
   terms.append(m.isc(W,c*(-1)**((n-parity)//2+(d-parity)//2)*4*B/pi0*z*z/F(n*(n+1)-d*(d+1))))
  if reverse:terms.reverse()
  total=m.ip(F(0))
  for term in terms:total=m.ia(total,term)
  g=band.outer24((total[0]-fault,total[1]+fault));assert g[1]-g[0]<F(1,10**20)
  if n<=256:
   old=oldgram[n];assert max(g[0],F(old['lower']))<=min(g[1],F(old['upper']))
  else:output.append(dict(degree=n,lower=str(g[0]),upper=str(g[1])))
  if n in [255,256,319,320,383,384,447,448,511,512]:print('RC259 '+('odd' if parity else 'even')+' band output through '+str(n),flush=True)
 return output,dict(output_first_degree=257,output_last_degree=END,off_diagonal_spherical_Sturm_Liouville_boundary_identity=True,exact_spherical_ODE_controls=True,same_parity_infinite_boundary_Wronskian_zero=True,all_output_degrees_exceed_input_degree=True,Bessel_recurrence_generation_grid_digits=600,Bessel_recurrence_replay_grid_digits=620,phase_pi_Machin_terms=600,phase_pi_grid_digits=450,phase_argument_grid_digits=400,phase_Taylor_generation_terms=220,phase_Taylor_replay_terms=240,phase_interval_grid_digits=800,stored_band_Gram_grid_digits=24,actual_pi_prefactor_and_lower_limit_fault_upper=str(fault),all_mode_cross_terms_retained=True,low_output_controls_intersect_pinned_RC251=controls,spherical_boundary_derivative_controls_through_degree=END)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('258_orthogonal_physical_tail');old=get('248_direct_coupled_residual');tail250=get('250_coupled_original_output_tail');centers=get('251_extended_coupled_residual');pcert=get('253_prime_boundary_tail');source256=get('256_retained_band_inverse');kernel=get('115_rational_fourier_adjoint');bounds=get('232_augmented_polynomial_action');forms=get('247_materialized_four_trial_response')
 rows=[]
 for parity,r in enumerate(prior['orthogonal_physical_tail_response_certificates']):
  c=centers['extended_coupled_residual_response_certificates'][parity];o=old['selected_direct_residual_certificates'][parity];b=bounds['polynomial_augmented_action_certificates'][parity];lam=F(b['augmentation_coefficient']);U=F(b['rational_frequency_half_bandwidth']);a=list(map(F,o['exact_Z_input_Legendre_coefficients']))
  high,control=window(a,parity,U,F(kernel['rational_pi']),F(kernel['rational_pi_error_upper']),c['extended_band_Gram_column'],reverse)
  captured_terms=[down(band.minabs((F(g['lower']),F(g['upper'])))**2/orig.mass(g['degree'])) for g in high]
  if reverse:captured_terms.reverse()
  captured=down(sum(captured_terms,F(0)));qhi=F(c['intersected_physical_band_input_form_upper']);lowcapture=F(c['captured_band_output_physical_energy_lower'])
  bandtail=up(qhi-lowcapture-captured);assert bandtail>=0
  # This remains a C^2<=C bound. The compression defect is not silently
  # discarded, nor is the ideal band operator substituted for Fhat*Fhat.
  inputq=list(map(F,o['original_combination_action_certificate']['exact_original_combination_input']));pp=tail250['coupled_output_tail_response_certificates'][parity]['coupled_original_output_tail_certificate']['prime_controls']
  rawprime,physical,primecontrol=prime.prime_boundary(inputq,parity,pp,reverse)
  assert prime.native.segment_digest([(F(0),F(END),rawprime)])==pcert['prime_boundary_tail_response_certificates'][parity]['prime_boundary_projection_certificate']['prime_coefficients_through_512_sha256']
  assert physical==F(pcert['prime_boundary_tail_response_certificates'][parity]['prime_physical_energy_beyond_512_upper'])
  coupled=[];energy=[]
  for g in high:
   n=g['degree'];h,hr=prime.native.endpoint(inputq,n,F(0),F(0));assert hr==0
   aug=(lam*F(g['lower'])/orig.mass(n),lam*F(g['upper'])/orig.mass(n));original=h+rawprime[n]
   interval=(original-aug[1],original-aug[0]);v=down((interval[0]+interval[1])/2);radius=up(max(v-interval[0],interval[1]-v));e=up(orig.mass(n)*max(abs(interval[0]),abs(interval[1]))**2)
   coupled.append(dict(degree=n,physical_model_source_center=str(v),radius=str(radius),physical_model_energy_upper=str(e)));energy.append(e)
  if reverse:energy.reverse()
  explicit=up(sum(energy,F(0)));original512=F(r['coupled_original_physical_energy_beyond_512_upper']);augmentation512=up(lam*lam*bandtail);remaining=up((root(original512)+root(augmentation512))**2);proposed=up(explicit+remaining);R=min(F(r['complete_model_physical_energy_beyond_256_upper']),proposed)
  A=F(r['retained_polynomial_physical_energy']);Y=F(r['retained_polynomial_outside_Fourier_energy_upper']);finite=F(r['finite_coefficient_and_actual_s_error_squared_upper']);fault=F(r['unchanged_global_physical_fault_norm_upper']);modelout,active=parent.orthogonal_tail(A,Y,R);assert active
  S=min(F(r['actual_full_source_physical_energy_upper']),up((root(up((root(A)+root(finite))**2+R))+fault)**2));X=min(S,F(r['actual_full_source_outside_Fourier_energy_upper']),up((root(modelout)+root(finite)+fault)**2))
  old256=source256['retained_band_inverse_response_certificates'][parity];choices=[]
  for j in range(1000,2000):
   t=parent.band.retained_band(F(j,10000),F(old256['original_canonical_reference_floor']),F(old256['original_low_band_penalty']),lam,F(old256['complete_canonical_J_to_Fhat_error_squared_upper']),F(old256['log_U_lower']));I=F(t['physical_inside_band_multiplier_lower']);O=F(t['physical_outside_band_multiplier_lower'])
   if I>O:choices.append((up(S/I+X*(1/O-1/I)),F(t['tau']),t))
  if reverse:choices.reverse()
  correction,_,selected=min(choices,key=lambda v:(v[0],v[1]));center=F(old256['direct_inverse_response_upper'])-F(old256['actual_augmented_inverse_correction_upper']);candidate=up(center+correction);upper=min(F(r['actual_original_action_inverse_response_upper']),candidate);f0=forms['parity_materialized_four_trial_response_certificates'][parity]['original_trial_form_intervals'][0][0];gap=max(F(r['actual_signed_gap_lower']),down(F(f0[0])-upper))
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],band_output_window_Gram_intervals=high,band_window_controls=control,additional_band_output_physical_energy_lower=str(captured),band_output_physical_energy_beyond_512_upper=str(bandtail),augmentation_physical_energy_beyond_512_upper=str(augmentation512),coupled_physical_model_output_257_through_512=coupled,coupled_physical_model_energy_257_through_512_upper=str(explicit),coupled_physical_model_energy_beyond_512_upper=str(remaining),proposed_model_physical_energy_beyond_256_upper=str(proposed),complete_model_physical_energy_beyond_256_upper=str(R),previous_model_physical_energy_beyond_256_upper=r['complete_model_physical_energy_beyond_256_upper'],model_tail_improved=R<F(r['complete_model_physical_energy_beyond_256_upper']),prime_raw_coefficients_512_digest_matches_RC253=True,prime_boundary_controls=primecontrol,orthogonal_model_outside_Fourier_energy_upper=str(modelout),actual_full_source_physical_energy_upper=str(S),actual_full_source_outside_Fourier_energy_upper=str(X),previous_full_source_outside_Fourier_energy_upper=r['actual_full_source_outside_Fourier_energy_upper'],selected_two_band_multiplier_certificate=selected,actual_inverse_correction_upper=str(correction),actual_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(upper),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_inverse_upper_improved=upper<F(r['actual_original_action_inverse_response_upper']),actual_signed_gap_lower=str(gap),actual_signed_gap_upper=r['actual_signed_gap_upper'],all_original_and_rational_augmentation_faults_preserved=True,signed_gap_positive_certified=gap>0))
  print('RC259 '+r['parity']+' model tail '+str(float(R))+'; inverse upper '+str(float(upper)),flush=True)
 return dict(milestone='RC259',starting_commit='428b8ff70e918a7bdcdb6827d3d190f8cc4ffd60',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,coupled_augmentation_tail_response_certificates=rows,actual_response_source_count=2,response_trials_per_parity=4,retained_physical_source_polynomial_degree_unchanged=256,explicit_coupled_tail_output_degree=512,chosen_rational_augmentation_unchanged=True,all_high_output_endpoint_prime_band_cross_terms_retained=True,compressed_band_C_squared_not_identified_with_C=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC260: control the compressed-band projection defect or full omitted-source Fourier leakage, or change the response trial; full signed gate remains open')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC259 VALIDATED: coupled augmentation output; Stage I open',flush=True)
