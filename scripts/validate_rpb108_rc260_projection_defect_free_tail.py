"""RC260: direct band-output tail, separated from the compression defect."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
from functools import lru_cache
import argparse,hashlib,json
import validate_rpb108_rc259_coupled_augmentation_tail as parent
m=parent.m;band=parent.band;orig=parent.orig;B=parent.B;ROOT=parent.ROOT
up=parent.up;down=parent.down;root=parent.root
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc259_coupled_augmentation_tail.json':'347281f68fc8076380d0b4afb71647c6683239f1','notes/RPB108_RC259_COUPLED_AUGMENTATION_TAIL_20261014.md':'586ee840a7cde3881fb41d2e4ccf7a769d0e7f19'})
HELPER_PINS['scripts/validate_rpb108_rc259_coupled_augmentation_tail.py']='90d7efa9501e1ffecb8c8b1d55b90296943e0263'
END=1024
@lru_cache(None)
def phase_pi():
 def atan(q):
  s=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(600)),F(0));return s,s+F(1,1201*q**1201)
 a=atan(5);b=atan(239);lo,hi=m.outer_grid((16*a[0]-4*b[1],16*a[1]-4*b[0]),750)
 assert 3<lo<hi<F(22,7);return lo,hi
def endpoint_values(U,pi0,pierr,reverse):
 z=2*pi0*B*U;assert z>400;pl,ph=phase_pi();assert pi0-pierr<=pl<ph<=pi0+pierr
 turns=int(B*U+F(1,2));tl,th=m.outer_grid((z-turns*(pl+ph),z-turns*(pl+ph)),700);theta=(tl+th)/2;thetaerr=(th-tl)/2+abs(turns)*(ph-pl);assert abs(theta)+thetaerr<F(22,7)
 terms=440 if reverse else 420;ct=m.ip(F(1));st=m.ip(theta);cv=ct;sv=st
 for k in range(1,terms):
  ct=m.outer_grid(m.isc(ct,-theta*theta/F((2*k-1)*(2*k))),1200);st=m.outer_grid(m.isc(st,-theta*theta/F((2*k)*(2*k+1))),1200)
  cv=m.outer_grid(m.ia(cv,ct),1200);sv=m.outer_grid(m.ia(sv,st),1200)
 pe=F(22,7)**(2*terms)/factorial(2*terms)+F(22,7)**(2*terms+1)/factorial(2*terms+1)+thetaerr
 cosine=m.outer_grid((cv[0]-pe,cv[1]+pe),1200);sine=m.outer_grid((sv[0]-pe,sv[1]+pe),1200);digits=1240 if reverse else 1200
 j=[m.outer_grid(m.isc(sine,1/z),digits),m.outer_grid(m.ia(m.isc(sine,1/z**2),m.isc(cosine,-1/z)),digits)]
 for n in range(1,END):j.append(m.outer_grid(m.ia(m.isc(j[n],F(2*n+1)/z),m.neg(j[n-1])),digits))
 dj=[m.neg(j[1])]+[m.outer_grid(m.ia(j[n-1],m.isc(j[n],-F(n+1)/z)),digits) for n in range(1,END+1)]
 return z,j,dj
def window(a,parity,U,pi0,pierr,oldwindow,reverse):
 assert len(a)==65 and all(not c or n%2==parity for n,c in enumerate(a))
 z,j,dj=endpoint_values(U,pi0,pierr,reverse);pil=pi0-pierr;S=sum(map(abs,a),F(0));fault=up(S*(4*B/pil*(2*B*U*pierr)+8*B*pierr/(pil*pi0)))
 old={g['degree']:g for g in oldwindow};control_degree=511 if parity else 512;rows=[]
 for n in [control_degree]+list(range(513,END+1)):
  if n%2!=parity:continue
  contributions=[]
  for d,c in enumerate(a):
   if not c:continue
   W=m.ia(m.im(dj[n],j[d]),m.neg(m.im(j[n],dj[d])))
   contributions.append(m.isc(W,c*(-1)**((n-parity)//2+(d-parity)//2)*4*B/pi0*z*z/F(n*(n+1)-d*(d+1))))
  if reverse:contributions.reverse()
  g=m.ip(F(0))
  for t in contributions:g=m.ia(g,t)
  g=band.outer24((g[0]-fault,g[1]+fault));assert g[1]-g[0]<F(1,10**20)
  if n==control_degree:assert max(g[0],F(old[n]['lower']))<=min(g[1],F(old[n]['upper']))
  else:rows.append(dict(degree=n,lower=str(g[0]),upper=str(g[1])))
  if n in [511,512,639,640,767,768,895,896,1023,1024]:print('RC260 '+('odd' if parity else 'even')+' band output through '+str(n),flush=True)
 return rows,dict(same_off_diagonal_boundary_identity_as_RC259=True,independent_RC259_output_control_degree=control_degree,phase_pi_Machin_terms=600,phase_pi_grid_digits=750,phase_argument_grid_digits=700,phase_Taylor_generation_terms=420,phase_Taylor_replay_terms=440,phase_interval_grid_digits=1200,Bessel_recurrence_generation_grid_digits=1200,Bessel_recurrence_replay_grid_digits=1240,stored_Gram_grid_digits=24,original_pi_displacement_and_prefactor_fault_upper=str(fault))
def analytic_tail(U,pi_upper,q_upper,parity):
 # Poisson/Rodrigues integral: |j_n(t)| <= |t|^n/(2n+1)!!.
 # Cauchy--Schwarz and integration in frequency cancel the factor 2n+1:
 # mass(n)*|CZ_n|^2 <= q_upper*4 B U*z_max^(2n)/((2n+1)!!)^2.
 first=1025 if parity else 1026;z=2*pi_upper*B*U;df=factorial(2*first+1)//(2**first*factorial(first));assert df*2**first*factorial(first)==factorial(2*first+1)
 term=z**(2*first)/df**2;ratio=z**4/F(((2*first+3)*(2*first+5))**2);assert 0<ratio<1
 result=up(q_upper*4*B*U*term/(1-ratio));assert 0<result<F(1,10**20)
 return result,dict(first_omitted_matching_degree=first,real_spherical_Bessel_Poisson_bound='abs(j_n(t)) <= abs(t)^n/(2n+1)!!',frequency_endpoint_upper=str(z),first_scalar_series_term_upper=str(up(term)),parity_series_ratio_upper=str(up(ratio)),same_parity_geometric_series=True,source_band_energy_upper=str(q_upper),physical_band_output_energy_beyond_1024_upper=str(result),compressed_projection_defect_not_used=True)
def norm_interval(rows,reverse):
 terms=[]
 for g in rows:
  n=g['degree'];v=(F(g['lower']),F(g['upper']));terms.append((down(band.minabs(v)**2/orig.mass(n)),up(max(map(abs,v))**2/orig.mass(n))))
 if reverse:terms.reverse()
 return down(sum((v[0] for v in terms),F(0))),up(sum((v[1] for v in terms),F(0)))
def controls():
 # Exact beta integral normalization in the Poisson representation.
 for n in range(9):
  integral=sum((F(2*(-1)**k*comb(n,k),2*k+1) for k in range(n+1)),F(0));assert integral==F(2**(2*n+1)*factorial(n)**2,factorial(2*n+1))
  assert integral/F(2**(n+1)*factorial(n))==F(2**n*factorial(n),factorial(2*n+1))
 return dict(exact_Poisson_weight_beta_integral_normalization=True,physical_Legendre_mass_cancels_frequency_power_denominator=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('259_coupled_augmentation_tail');r258=get('258_orthogonal_physical_tail');r256=get('256_retained_band_inverse');old=get('248_direct_coupled_residual');centers=get('251_extended_coupled_residual');kernel=get('115_rational_fourier_adjoint');bounds=get('232_augmented_polynomial_action');forms=get('247_materialized_four_trial_response');rows=[]
 for parity,r in enumerate(prior['coupled_augmentation_tail_response_certificates']):
  c=centers['extended_coupled_residual_response_certificates'][parity];o=old['selected_direct_residual_certificates'][parity];b=bounds['polynomial_augmented_action_certificates'][parity];lam=F(b['augmentation_coefficient']);U=F(b['rational_frequency_half_bandwidth']);a=list(map(F,o['exact_Z_input_Legendre_coefficients']));pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper'])
  new,control=window(a,parity,U,pi0,pierr,r['band_output_window_Gram_intervals'],reverse)
  low=norm_interval(c['extended_band_Gram_column'],reverse);middle=norm_interval(r['band_output_window_Gram_intervals'],reverse);high=norm_interval(new,reverse)
  qlo=F(c['intersected_physical_band_input_form_lower']);qhi=F(c['intersected_physical_band_input_form_upper']);analytic,proof=analytic_tail(U,pi0+pierr,qhi,parity)
  tail512=min(F(r['band_output_physical_energy_beyond_512_upper']),up(high[1]+analytic));tail256=up(middle[1]+tail512)
  normlo=down(low[0]+middle[0]+high[0]);normhi=up(low[1]+middle[1]+high[1]+analytic)
  defectlo=max(F(0),down(qlo-normhi));defecthi=up(qhi-normlo);assert 0<defectlo<=defecthi
  previous=r258['orthogonal_physical_tail_response_certificates'][parity];original512=F(previous['coupled_original_physical_energy_beyond_512_upper']);augmentation512=up(lam*lam*tail512);remaining=up((root(original512)+root(augmentation512))**2)
  explicit=F(r['coupled_physical_model_energy_257_through_512_upper']);R=min(F(r['complete_model_physical_energy_beyond_256_upper']),up(explicit+remaining))
  A=F(previous['retained_polynomial_physical_energy']);Y=F(previous['retained_polynomial_outside_Fourier_energy_upper']);finite=F(previous['finite_coefficient_and_actual_s_error_squared_upper']);fault=F(previous['unchanged_global_physical_fault_norm_upper']);modelout,active=parent.parent.orthogonal_tail(A,Y,R);assert active
  S=min(F(r['actual_full_source_physical_energy_upper']),up((root(up((root(A)+root(finite))**2+R))+fault)**2));X=min(S,F(r['actual_full_source_outside_Fourier_energy_upper']),up((root(modelout)+root(finite)+fault)**2))
  reference=r256['retained_band_inverse_response_certificates'][parity];choices=[]
  for k in range(1000,2000):
   t=parent.parent.band.retained_band(F(k,10000),F(reference['original_canonical_reference_floor']),F(reference['original_low_band_penalty']),lam,F(reference['complete_canonical_J_to_Fhat_error_squared_upper']),F(reference['log_U_lower']));I=F(t['physical_inside_band_multiplier_lower']);O=F(t['physical_outside_band_multiplier_lower'])
   if I>O:choices.append((up(S/I+X*(1/O-1/I)),F(t['tau']),t))
  if reverse:choices.reverse()
  correction,_,selected=min(choices,key=lambda v:(v[0],v[1]));center=F(reference['direct_inverse_response_upper'])-F(reference['actual_augmented_inverse_correction_upper']);upper=min(F(r['actual_original_action_inverse_response_upper']),up(center+correction));f0=forms['parity_materialized_four_trial_response_certificates'][parity]['original_trial_form_intervals'][0][0];gap=max(F(r['actual_signed_gap_lower']),down(F(f0[0])-upper))
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],band_output_Gram_window_513_through_1024=new,band_window_controls=control,band_window_physical_energy_513_through_1024_lower=str(high[0]),band_window_physical_energy_513_through_1024_upper=str(high[1]),analytic_band_output_tail_certificate=proof,actual_ideal_band_output_physical_energy_beyond_512_upper=str(tail512),previous_defect_contaminated_band_tail_512_upper=r['band_output_physical_energy_beyond_512_upper'],actual_ideal_band_output_physical_energy_beyond_256_upper=str(tail256),complete_ideal_band_output_physical_energy_lower=str(normlo),complete_ideal_band_output_physical_energy_upper=str(normhi),compressed_band_projection_defect_energy_lower=str(defectlo),compressed_band_projection_defect_energy_upper=str(defecthi),positive_compression_defect_certified=True,band_tail_bound_excludes_compression_defect=True,augmentation_physical_energy_beyond_512_upper=str(augmentation512),coupled_physical_model_energy_beyond_512_upper=str(remaining),complete_model_physical_energy_beyond_256_upper=str(R),previous_model_physical_energy_beyond_256_upper=r['complete_model_physical_energy_beyond_256_upper'],actual_full_source_physical_energy_upper=str(S),actual_full_source_outside_Fourier_energy_upper=str(X),previous_full_source_outside_Fourier_energy_upper=r['actual_full_source_outside_Fourier_energy_upper'],selected_two_band_multiplier_certificate=selected,actual_inverse_correction_upper=str(correction),actual_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(upper),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_inverse_upper_improved=upper<F(r['actual_original_action_inverse_response_upper']),actual_signed_gap_lower=str(gap),actual_signed_gap_upper=r['actual_signed_gap_upper'],all_original_and_rational_augmentation_faults_preserved=True,signed_gap_positive_certified=gap>0))
  print('RC260 '+r['parity']+' band tail512 '+str(float(tail512))+'; defect lower '+str(float(defectlo))+'; inverse upper '+str(float(upper)),flush=True)
 return dict(milestone='RC260',starting_commit='7c6d3cc1405caae7b822a0ea86e190998b31d812',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,projection_defect_free_tail_response_certificates=rows,exact_controls=controls(),actual_response_source_count=2,response_trials_per_parity=4,retained_physical_source_polynomial_degree_unchanged=256,explicit_band_output_degree=END,analytic_infinite_band_output_remainder_paid=True,chosen_rational_augmentation_unchanged=True,ideal_band_operator_not_substituted_for_actual_rational_augmentation=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC261: use the materialized physical residual output through 512 in the Fourier/residual inverse calculation, or control the remaining original prime output directly; full signed gate remains open')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC260 VALIDATED: direct band tail separated from compression defect; Stage I open',flush=True)
