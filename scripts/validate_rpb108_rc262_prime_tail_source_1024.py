"""RC262: interval prime output through 2048 and physical-source Fourier through 1024."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc261_materialized_source_fourier as parent
prime=parent.parent.parent.prime
m=parent.m;band=parent.band;orig=parent.orig;B=parent.B;ROOT=parent.ROOT
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc261_materialized_source_fourier.json':'5693873ada4d7260e56930bb371f15f4103c156a','notes/RPB108_RC261_MATERIALIZED_SOURCE_FOURIER_20261014.md':'5f5491e92dabe57636f6f080e376cf65e3de75a7'})
HELPER_PINS['scripts/validate_rpb108_rc261_materialized_source_fourier.py']='27b23691e2df3589b817d4404e88929a9526a412'
END=2048
def legendre_intervals(b,reverse):
 grid=1540 if reverse else 1500;outgrid=140 if reverse else 120
 previous=m.ip(F(1));current=m.ip(b);values=[previous,current]
 for n in range(1,END):
  value=m.outer_grid(m.isc(m.ia(m.isc(current,(2*n+1)*b),m.isc(previous,-n)),F(1,n+1)),grid)
  values.append(m.outer_grid(value,outgrid));previous,current=current,value
 for n in range(8):
  exact=prime.evaluate(orig.legendre(n),b);assert values[n][0]<=exact<=values[n][1]
 assert all(v[1]-v[0]<F(1,10**110) for v in values)
 return values
def prime_window(a,parity,proof,source_controls,band_controls,lam,old_tail512,reverse):
 q=prime.native.input_poly(a);segments=prime.model_segments(q,proof['chosen_prime_model_parameters'],parity)
 assert prime.native.segment_digest(segments)==proof['prime_segment_polynomial_sha256']
 norm=B*sum((orig.integral(orig.product(v,v),l,r) for l,r,v in segments),F(0))
 assert str(down(norm))==proof['full_prime_output_physical_energy_lower'] and str(up(norm))==proof['full_prime_output_physical_energy_upper']
 boundaries=[];digits=140 if reverse else 120
 for i in range(len(segments)-1):
  b=segments[i][1]
  if b<0:continue
  jump=[x-y for x,y in zip(segments[i][2],segments[i+1][2])];jc=[orig.project(jump,d) for d in range(len(q))]
  assert not any(prime.native.addpoly(prime.native.input_poly(jc),[-v for v in jump]))
  exact=prime.legendre_values(b,len(q)-1);dv=[F(0)]+[d*(b*exact[d]-exact[d-1])/(b*b-1) for d in range(1,len(q))]
  jv=[m.outer_grid(m.ip(jc[d]*exact[d]),digits) for d in range(len(q))];jd=[m.outer_grid(m.ip(jc[d]*dv[d]),digits) for d in range(len(q))]
  boundaries.append((b,jv,jd,legendre_intervals(b,reverse)))
 assert len(boundaries)==7
 controls=[257,383,511] if parity else [258,384,512];oldsource={v['degree']:v for v in source_controls};oldband={v['degree']:v for v in band_controls};rows=[];captured=[]
 for n in controls+list(range(513,END+1)):
  if n%2!=parity:continue
  parts=[];ln=n*(n+1)
  for b,jv,jd,pn in boundaries:
   value=m.ip(F(0));slope=m.ip(F(0))
   for d in range(len(q)):
    value=m.ia(value,m.isc(jv[d],F(1,ln-d*(d+1))));slope=m.ia(slope,m.isc(jd[d],F(1,ln-d*(d+1))))
   dp=m.isc(m.ia(m.isc(pn[n],b),m.neg(pn[n-1])),F(n)/(b*b-1))
   parts.append(m.isc(m.ia(m.im(slope,pn[n]),m.neg(m.im(value,dp))),1-b*b))
  if reverse:parts.reverse()
  interval=m.ip(F(0))
  for v in parts:interval=m.ia(interval,v)
  interval=m.outer_grid(m.isc(interval,2*n+1),60);assert interval[1]-interval[0]<F(1,10**50)
  if n in controls:
   h,rad=prime.native.endpoint(a,n,F(0),F(0));assert rad==0;v=oldsource[n];g=oldband[n]
   old=(F(v['physical_model_source_center'])-F(v['radius'])-h+lam*F(g['lower'])/orig.mass(n),F(v['physical_model_source_center'])+F(v['radius'])-h+lam*F(g['upper'])/orig.mass(n))
   assert max(interval[0],old[0])<=min(interval[1],old[1])
  else:
   rows.append(dict(degree=n,lower=str(interval[0]),upper=str(interval[1])));captured.append(down(orig.mass(n)*band.minabs(interval)**2))
  if n in [511,512,767,768,1023,1024,1279,1280,1535,1536,1791,1792,2047,2048]:print('RC262 '+('odd' if parity else 'even')+' prime output through '+str(n),flush=True)
 if reverse:captured.reverse()
 capture=down(sum(captured,F(0)));tail=up(old_tail512-capture);assert 0<tail<old_tail512
 return rows,tail,dict(complete_prime_pairs=7,physical_segments=15,positive_boundaries=7,full_segment_digest_and_norm_replayed=True,boundary_jump_polynomials_exactly_reconstructed=True,Legendre_recurrence_generation_grid_digits=1500,Legendre_recurrence_replay_grid_digits=1540,boundary_static_and_value_generation_grid_digits=120,boundary_static_and_value_replay_grid_digits=140,stored_prime_coefficient_grid_digits=60,independent_RC259_prime_controls=controls,all_control_intervals_intersect=True,additional_captured_prime_physical_energy_lower=str(capture),remaining_prime_physical_energy_beyond_2048_upper=str(tail))
def fourier(a,parity,U,pi0,pierr,reference,reverse):
 z,j,dj=parent.parent.endpoint_values(U,pi0,pierr,reverse);digits=140 if reverse else 120
 j=[m.outer_grid(v,digits) for v in j];dj=[m.outer_grid(v,digits) for v in dj]
 sine=m.isc(j[0],z);cosine=m.ia(j[0],m.isc(j[1],-z));c2=m.ia(m.im(cosine,cosine),m.neg(m.im(sine,sine)));s2=m.isc(m.im(sine,cosine),2)
 L=520 if reverse else 500;rr,ii,rem=m.ibp_parts(2,L,z,[(2*z.numerator)**k for k in range(L)])
 real=m.isc(m.ia(m.im(c2,(rr-rem,rr+rem)),m.neg(m.im(s2,(ii-rem,ii+rem)))),1/z**2);J=[m.outer_grid(m.ia(m.ip(1/(2*z)),m.isc(real,-F(1,2))),digits)]
 for n in range(1024):
  sq=m.ia(m.im(j[n],j[n]),m.im(j[n+1],j[n+1]));J.append(m.outer_grid(m.isc(m.ia(m.isc(J[n],2*n+1),m.isc(sq,z)),F(1,2*n+3)),digits));assert J[-1][0]>0
 total=low=m.ip(F(0));degrees=[n for n,c in enumerate(a) if c];assert len(a)==1025 and all(n%2==parity for n in degrees)
 order=degrees[::-1] if reverse else degrees
 for n in order:
  t=m.isc(J[n],a[n]**2);total=m.outer_grid(m.ia(total,t),digits)
  if n<=512:low=m.outer_grid(m.ia(low,t),digits)
  inner=[d for d in degrees if d<n];inner=inner[::-1] if reverse else inner
  for d in inner:
   W=m.ia(m.im(dj[n],j[d]),m.neg(m.im(j[n],dj[d])));t=m.isc(W,-2*a[n]*a[d]*(-1)**((n-parity)//2+(d-parity)//2)*z*z/F(n*(n+1)-d*(d+1)))
   total=m.outer_grid(m.ia(total,t),digits)
   if n<=512:low=m.outer_grid(m.ia(low,t),digits)
  if n in [255,256,511,512,767,768,1023,1024]:print('RC262 '+('odd' if parity else 'even')+' Fourier pairs through '+str(n),flush=True)
 def finish(v,coeff):
  S=sum(map(abs,coeff),F(0));pil=pi0-pierr;fault=up(S*S*(4*B/pil*(2*B*U*pierr)+8*B*pierr/(pil*pi0)));v=m.isc(v,4*B/pi0)
  return band.outer24((v[0]-fault,v[1]+fault)),fault
 check,_=finish(low,a[:513]);assert max(check[0],F(reference['outside_physical_Fourier_energy_lower']))<=min(check[1],F(reference['outside_physical_Fourier_energy_upper']))
 result,fault=finish(total,a);A=sum((orig.mass(n)*v*v for n,v in enumerate(a)),F(0));assert 0<result[0]<=result[1]<A
 return result,A,dict(retained_source_degree=1024,all_mode_cross_terms_retained=True,stable_RC261_diagonal_recurrence_and_off_diagonal_boundary_identity=True,base_I2_generation_IBP_terms=500,base_I2_replay_IBP_terms=520,endpoint_diagonal_and_accumulator_generation_grid_digits=120,endpoint_diagonal_and_accumulator_replay_grid_digits=140,streaming_interval_accumulator_outward_rounded_each_term=True,independent_RC261_degree_512_control_lower=str(check[0]),independent_RC261_degree_512_control_upper=str(check[1]),degree_512_control_intersects=True,actual_pi_source_squared_fault_upper=str(fault),physical_polynomial_energy=str(A),outside_physical_Fourier_energy_lower=str(result[0]),outside_physical_Fourier_energy_upper=str(result[1]))
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('261_materialized_source_fourier');r260=get('260_projection_defect_free_tail');r259=get('259_coupled_augmentation_tail');r253=get('253_prime_boundary_tail');tail250=get('250_coupled_original_output_tail');old=get('248_direct_coupled_residual');ref256=get('256_retained_band_inverse');forms=get('247_materialized_four_trial_response');kernel=get('115_rational_fourier_adjoint');metric=get('129_four_vector_joint_moment');sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B)
 harmonic=[F(0)]
 for n in range(1,2051):harmonic.append(harmonic[-1]+F(1,n))
 rows=[]
 for parity,r in enumerate(prior['materialized_source_Fourier_response_certificates']):
  ref=ref256['retained_band_inverse_response_certificates'][parity];lam=F(ref['unchanged_actual_rational_augmentation_coefficient']);q=list(map(F,old['selected_direct_residual_certificates'][parity]['original_combination_action_certificate']['exact_original_combination_input']));p=r259['coupled_augmentation_tail_response_certificates'][parity];b260=r260['projection_defect_free_tail_response_certificates'][parity]
  pp=tail250['coupled_output_tail_response_certificates'][parity]['coupled_original_output_tail_certificate']['prime_controls'];oldprime=F(r253['prime_boundary_tail_response_certificates'][parity]['prime_physical_energy_beyond_512_upper'])
  pc,primetail,pcproof=prime_window(q,parity,pp,p['coupled_physical_model_output_257_through_512'],p['band_output_window_Gram_intervals'],lam,oldprime,reverse)
  first=2049 if parity else 2050;_,ep=prime.parent.tail_bound(q,first,sl,harmonic);endpoint=up(2*B*F(ep['uniform_combined_endpoint_bracket_upper'])**2*F(ep['parity_telescoping_weight_sum_upper']));original_remaining=up((root(endpoint)+root(primetail))**2)
  a=[F(v['coefficient']) for v in r['retained_physical_source_center_0_through_512']]+[F(0)]*512;bands={v['degree']:v for v in b260['band_output_Gram_window_513_through_1024']};source=[];uncertainty=[];original_high=[]
  for v in pc:
   n=v['degree'];h,rad=prime.native.endpoint(q,n,F(0),F(0));assert rad==0;original=(h+F(v['lower']),h+F(v['upper']))
   if n<=1024:
    g=bands[n];interval=(original[0]-lam*F(g['upper'])/orig.mass(n),original[1]-lam*F(g['lower'])/orig.mass(n));center=down((interval[0]+interval[1])/2);radius=up(max(center-interval[0],interval[1]-center));a[n]=center;source.append(dict(degree=n,physical_source_center=str(center),radius=str(radius)));uncertainty.append(up(orig.mass(n)*radius*radius))
   else:original_high.append(up(orig.mass(n)*max(map(abs,original))**2))
  if reverse:uncertainty.reverse();original_high.reverse()
  original1024=up(sum(original_high,F(0))+original_remaining);augmentation1024=up(lam*lam*F(b260['analytic_band_output_tail_certificate']['physical_band_output_energy_beyond_1024_upper']));R=up((root(original1024)+root(augmentation1024))**2);finite=up(F(r['retained_physical_coefficient_uncertainty_energy_upper'])+sum(uncertainty,F(0)));fault=F(r['unchanged_global_physical_fault_norm_upper'])
  Y,A,fp=fourier(a,parity,F(ref['rational_half_bandwidth']),F(kernel['rational_pi']),F(kernel['rational_pi_error_upper']),r['retained_physical_source_Fourier_certificate'],reverse)
  modelout,active=parent.parent.parent.parent.orthogonal_tail(A,Y[1],R);assert active
  S=min(F(r['actual_full_source_physical_energy_upper']),up((root(up((root(A)+root(finite))**2+R))+fault)**2));X=min(S,F(r['actual_full_source_outside_Fourier_energy_upper']),up((root(modelout)+root(finite)+fault)**2));Xlo=max(F(r['actual_full_source_outside_Fourier_energy_lower']),down(max(F(0),rootdown(Y[0])-root(up(finite+R))-fault)**2));assert 0<=Xlo<=X<=S
  choices=[]
  for k in range(1000,2000):
   t=parent.parent.parent.parent.band.retained_band(F(k,10000),F(ref['original_canonical_reference_floor']),F(ref['original_low_band_penalty']),lam,F(ref['complete_canonical_J_to_Fhat_error_squared_upper']),F(ref['log_U_lower']));I=F(t['physical_inside_band_multiplier_lower']);O=F(t['physical_outside_band_multiplier_lower'])
   if I>O:choices.append((up(S/I+X*(1/O-1/I)),F(t['tau']),t))
  if reverse:choices.reverse()
  correction,_,selected=min(choices,key=lambda v:(v[0],v[1]));center=F(ref['direct_inverse_response_upper'])-F(ref['actual_augmented_inverse_correction_upper']);upper=min(F(r['actual_original_action_inverse_response_upper']),up(center+correction));f0=forms['parity_materialized_four_trial_response_certificates'][parity]['original_trial_form_intervals'][0][0];gap=max(F(r['actual_signed_gap_lower']),down(F(f0[0])-upper))
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],prime_window_513_through_2048=pc,prime_boundary_interval_controls=pcproof,prime_physical_energy_beyond_2048_upper=str(primetail),previous_prime_physical_energy_beyond_512_upper=str(oldprime),endpoint_physical_energy_beyond_2048_upper=str(endpoint),endpoint_tail_control=ep,coupled_original_physical_energy_1025_through_2048_upper=str(up(sum(original_high,F(0)))),coupled_original_physical_energy_beyond_2048_upper=str(original_remaining),coupled_original_physical_energy_beyond_1024_upper=str(original1024),augmentation_physical_energy_beyond_1024_upper=str(augmentation1024),complete_model_physical_source_energy_beyond_1024_upper=str(R),physical_source_centers_513_through_1024=source,retained_prefix_0_through_512_origin='pinned RC261 exact coefficients',retained_coefficient_uncertainty_physical_energy_upper=str(finite),retained_source_Fourier_certificate=fp,unchanged_global_physical_fault_norm_upper=str(fault),actual_full_source_physical_energy_upper=str(S),actual_full_source_outside_Fourier_energy_lower=str(Xlo),actual_full_source_outside_Fourier_energy_upper=str(X),previous_full_source_outside_Fourier_energy_upper=r['actual_full_source_outside_Fourier_energy_upper'],selected_two_band_multiplier_certificate=selected,actual_inverse_correction_upper=str(correction),actual_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(upper),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_inverse_upper_improved=upper<F(r['actual_original_action_inverse_response_upper']),actual_signed_gap_lower=str(gap),actual_signed_gap_upper=r['actual_signed_gap_upper'],all_original_and_rational_augmentation_faults_preserved=True,signed_gap_positive_certified=gap>0))
  print('RC262 '+r['parity']+' prime tail2048 '+str(float(primetail))+'; inverse upper '+str(float(upper)),flush=True)
 return dict(milestone='RC262',starting_commit='a2fe7d7ca0653d2c3e17c2bc2efe7d771814c8de',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,prime_tail_source_response_certificates=rows,actual_response_source_count=2,response_trials_per_parity=4,retained_physical_source_degree=1024,prime_explicit_output_degree=2048,source_and_trial_spaces_unchanged=True,chosen_rational_augmentation_unchanged=True,compression_defect_free_analytic_band_remainder_preserved=True,exact_controls=parent.diagonal_control(),full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC263: sharpen the retained-source inverse frequency multiplier or change the response trial; remaining prime output and full signed gate remain open')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC262 VALIDATED: prime output 2048 and physical-source Fourier 1024; Stage I open',flush=True)
