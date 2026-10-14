"""RC246: materialized band actions on exact residual-shaped inputs."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,hashlib,json
import validate_rpb108_rc245_source_refined_response as parent
aggregate=parent.parent.parent
band=aggregate.band;orig=parent.orig;p=parent.p;B=parent.B
up=parent.up;down=parent.down;root=parent.root
ip=band.ip;ia=band.ia;im=band.im;isc=band.isc;neg=band.neg
ROOT=Path(__file__).resolve().parents[1];CUT=128
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc245_source_refined_response.json':'1ff5b37eacbc359e22aade45cf109a4de5e79bea','notes/RPB108_RC245_SOURCE_REFINED_RESPONSE_20261014.md':'46ec2d8c28bf10132ec0cc9d8dda44f41890c744'})
HELPER_PINS['scripts/validate_rpb108_rc245_source_refined_response.py']='445d82c5f46e3dc3374118108c9509553598814a'
def band_column(a,parity,U,pi0,pierr,reverse):
 oldcut=band.CUT
 try:
  band.CUT=CUT;aa,bb=band.spherical_polynomials()
 finally:band.CUT=oldcut
 A=[F(0)]*66;C=[F(0)]*66
 for n,c in enumerate(a):
  if not c:continue
  sign=-1 if ((n-parity)//2)%2 else 1
  for k,v in enumerate(aa[n]):A[k]+=sign*c*v
  for k,v in enumerate(bb[n]):C[k]+=sign*c*v
 z=2*pi0*B*U;assert z>400;turns=int(2*B*U+F(1,2));theta=2*pi0*(2*B*U-turns);assert abs(theta)<F(22,7)
 cv=sum(((-1)**k*theta**(2*k)/factorial(2*k) for k in range(41)),F(0));sv=sum(((-1)**k*theta**(2*k+1)/factorial(2*k+1) for k in range(40)),F(0));phaseerr=abs(theta)**81/factorial(81)+2*abs(turns)*pierr
 cosine=ia(ip(cv),(-up(phaseerr),up(phaseerr)));sine=ia(ip(sv),(-up(phaseerr),up(phaseerr)))
 L=112 if reverse else 96;moments={}
 for m in range(2,CUT+68):
  rr=F(0);ii=F(0);rising=1
  for k in range(L):
   v=F(rising,2**(k+1))/z**k
   if k%4==0:ii+=v
   elif k%4==1:rr+=v
   elif k%4==2:ii-=v
   else:rr-=v
   rising*=m+k
  rem=F(rising,2**L)*z**(1-L)/F(m+L-1);Rr=ia(ip(rr),(-up(rem),up(rem)));Ii=ia(ip(ii),(-up(rem),up(rem)))
  moments[m]=(ia(im(cosine,Rr),neg(im(sine,Ii))),ia(im(sine,Rr),im(cosine,Ii)))
 pil=pi0-pierr;assert pil>3 and pi0+pierr<4
 S=sum(map(abs,a),F(0));fault=up(S*(4*B/pil*(2*B*U*pierr)+8*B*pierr/(pil*pi0)));gram=[]
 for n in range(CUT+1):
  if n%2!=parity:gram.append((F(0),F(0)));continue
  pa=orig.product(aa[n],A);pb=orig.product(bb[n],C);pc=band.polyadd(orig.product(aa[n],C),orig.product(bb[n],A));size=max(len(pa),len(pb),len(pc));pa+=[F(0)]*(size-len(pa));pb+=[F(0)]*(size-len(pb));pc+=[F(0)]*(size-len(pc));total=ip(F(0))
  degrees=list(range(2,size));degrees=degrees[::-1] if reverse else degrees
  for m in degrees:
   c0=(pa[m]+pb[m])/2;cc=(pb[m]-pa[m])/2;cs=pc[m]/2
   if c0:total=ia(total,ip(c0*z**(1-m)/F(m-1)))
   if cc:total=ia(total,im(ip(cc/z**m),moments[m][0]))
   if cs:total=ia(total,im(ip(cs/z**m),moments[m][1]))
  sign=-1 if ((n-parity)//2)%2 else 1;tail=ia(isc(total,sign*4*B/pi0),(-fault,fault));full=orig.mass(n)*(a[n] if n<len(a) else F(0));gram.append(band.outer24(ia(ip(full),neg(tail))))
  if n in [31,32,63,64,95,96,127,128]:print('RC246 '+('even' if parity==0 else 'odd')+' band output through '+str(n),flush=True)
 return gram,dict(generation_integration_by_parts_terms=96,replay_integration_by_parts_terms=112,pi_lower_limit_prefactor_error_upper=str(fault),phase_error_upper=str(up(phaseerr)),stored_band_Gram_grid='1/10^24',spherical_polynomial_boundary_derivative_controls_through_degree=CUT,all_input_modes_combined_before_output_pairing=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('243_residual_augmented_actions');original=get('242_residual_original_actions');bounds=get('232_augmented_polynomial_action');kernel=get('115_rational_fourier_adjoint');metric=get('129_four_vector_joint_moment');low=get('240_three_trial_signed_response')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper']);rows=[]
 for parity,r in enumerate(original['parity_residual_original_action_certificates']):
  old=prior['parity_residual_augmented_action_certificates'][parity];a=list(map(F,r['exact_input_Legendre_coefficients']));bound=bounds['polynomial_augmented_action_certificates'][parity];lam=F(bound['augmentation_coefficient']);U=F(bound['rational_frequency_half_bandwidth']);epsilon=F(bound['physical_Fhat_star_Fhat_to_J_star_J_operator_norm_upper'])
  gram,controls=band_column(a,parity,U,pi0,pierr,reverse);output=[isc(g,1/orig.mass(n)) for n,g in enumerate(gram)]
  # Pair the new column with its entire input; intersect the independent
  # aggregate physical Fourier energy partition from RC243.
  qlo=qhi=F(0)
  for n,c in enumerate(a):
   v=[c*gram[n][0],c*gram[n][1]];qlo+=min(v);qhi+=max(v)
  proof=old['aggregate_fourier_leakage_certificate'];qlo=max(qlo,F(proof['physical_band_energy_lower']));qhi=min(qhi,F(proof['physical_band_energy_upper']));assert 0<qlo<=qhi
  captured=sum((orig.mass(n)*band.minabs(g)**2 for n,g in enumerate(output)),F(0));tail=up(qhi-captured);assert tail>=0
  first=129 if parity else 130;omitted=up(lam*lam*tail/(orig.H(first)+sl));finite=F(0);aug=[];full=[]
  for n,g in enumerate(output):
   values=[lam*c/(orig.H(n)+s) for c in g for s in [sl,sh]];lo=min(values);hi=max(values);c=down((lo+hi)/2);rad=max(c-lo,hi-c);finite+=orig.mass(n)*(orig.H(n)+sh)*rad*rad;aug.append(dict(degree=n,coefficient=str(c),radius=str(up(rad))));o=r['finite_complete_original_D_action'][n];full.append(dict(degree=n,coefficient=str(F(o['coefficient'])+c),radius=str(up(F(o['radius'])+rad))))
  rational=F(old['rational_to_band_D_error_squared_upper']);AE=up((root(up(finite))+root(omitted)+root(rational))**2);E=up((root(F(r['complete_original_action_D_error_squared_upper']))+root(AE))**2)
  assert AE<F(old['complete_rational_augmentation_action_D_error_squared_upper']) and E<F(old['complete_augmented_action_D_error_squared_upper'])
  # Independent transpose data for the new R pairing with P4/P5.
  col=low['parity_three_trial_signed_response_certificates'][parity]['new_band_Gram_column'];l=h=F(0)
  for n,c in enumerate(a):
   v=[c*F(col[n]['lower']),c*F(col[n]['upper'])];l+=min(v);h+=max(v)
  g=gram[parity+4];assert max(l,g[0])<=min(h,g[1])
  rows.append(dict(parity=r['parity'],input=r['input'],actual_band_Gram_column=[dict(degree=n,lower=str(lo),upper=str(hi)) for n,(lo,hi) in enumerate(gram)],materialization_controls=controls,intersected_physical_band_input_form_lower=str(down(qlo)),intersected_physical_band_input_form_upper=str(up(qhi)),captured_band_output_physical_energy_lower=str(down(captured)),band_output_beyond_128_physical_energy_upper=str(tail),augmentation_D_omitted_output_energy_upper=str(omitted),augmentation_D_finite_rounding_energy_upper=str(up(finite)),unchanged_rational_to_band_D_error_squared_upper=str(rational),finite_augmentation_D_action=aug,finite_complete_augmented_D_action=full,previous_rational_augmentation_action_D_error_squared_upper=old['complete_rational_augmentation_action_D_error_squared_upper'],complete_rational_augmentation_action_D_error_squared_upper=str(AE),previous_complete_augmented_action_D_error_squared_upper=old['complete_augmented_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=str(E),relative_complete_augmented_action_D_error_squared_upper=str(up(E/F(r['input_D_energy_lower']))),independent_band_input_energy_partition_intersection=True,independent_P4_P5_band_transpose_intersection=True,ideal_band_operator_not_substituted_for_rational_augmentation=True))
 return dict(milestone='RC246',starting_commit='4ed17b420821251fcc95a2b5240f290b042b9315',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,retained_residual_augmented_action_degree=128,parity_materialized_residual_action_certificates=rows,complete_omitted_output_paid=True,rational_model_error_paid=True,opposite_parity_action_error_pairing_zero=True,same_parity_action_errors_assumed_orthogonal=False,enriched_inverse_response_recomputed=False,previous_response_bounds_preserved=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC247: reevaluate the four-trial original-action inverse responses with the materialized residual augmentation columns and refined source errors; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC246 VALIDATED: materialized complete residual augmentation actions; full signed gate open',flush=True)
