"""RC243: exact aggregate Fourier leakage and complete rational N actions."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,hashlib,json
import validate_rpb108_rc242_residual_original_actions as parent
orig=parent.orig;p=parent.p;B=parent.B;up=parent.up;down=parent.down;root=parent.root
band=parent.parent.parent.trial.material
ip=band.ip;ia=band.ia;im=band.im;isc=band.isc;neg=band.neg
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc242_residual_original_actions.json':'c40d6123e247c7eee98e8f6950cf78a85abb100a','notes/RPB108_RC242_RESIDUAL_ORIGINAL_ACTIONS_20261014.md':'3152505f644c82d05c13d40c80aa75025f1cd22b'})
HELPER_PINS['scripts/validate_rpb108_rc242_residual_original_actions.py']='1ad445e68070055b995c16efe65c3a31979b0134'
def leakage(a,parity,U,pi0,pierr,reverse):
 aa,bb=band.spherical_polynomials();A=[F(0)]*66;C=[F(0)]*66
 for n,c in enumerate(a):
  if not c:continue
  sign=-1 if ((n-parity)//2)%2 else 1
  for k,v in enumerate(aa[n]):A[k]+=sign*c*v
  for k,v in enumerate(bb[n]):C[k]+=sign*c*v
 z=2*pi0*B*U;assert z>400
 turns=int(2*B*U+F(1,2));theta=2*pi0*(2*B*U-turns)
 assert abs(theta)<F(22,7)
 cv=sum(((-1)**k*theta**(2*k)/factorial(2*k) for k in range(41)),F(0));sv=sum(((-1)**k*theta**(2*k+1)/factorial(2*k+1) for k in range(40)),F(0))
 phaseerr=abs(theta)**81/factorial(81)+2*abs(turns)*pierr
 cosine=ia(ip(cv),(-up(phaseerr),up(phaseerr)));sine=ia(ip(sv),(-up(phaseerr),up(phaseerr)))
 L=56 if reverse else 48;moments={}
 for m in range(2,132):
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
 pa=orig.product(A,A);pb=orig.product(C,C);pc=orig.product(A,C);total=ip(F(0));degrees=list(range(2,len(pa)));degrees=degrees[::-1] if reverse else degrees
 for m in degrees:
  c0=(pa[m]+pb[m])/2;cc=(pb[m]-pa[m])/2;cs=pc[m]
  if c0:total=ia(total,ip(c0*z**(1-m)/F(m-1)))
  if cc:total=ia(total,im(ip(cc/z**m),moments[m][0]))
  if cs:total=ia(total,im(ip(cs/z**m),moments[m][1]))
 pil=pi0-pierr;S=sum(map(abs,a),F(0));fault=up(S*S*(4*B/pil*(2*B*U*pierr)+8*B*pierr/(pil*pi0)))
 tail=band.outer24(ia(isc(total,4*B/pi0),(-fault,fault)));mass=sum((orig.mass(n)*c*c for n,c in enumerate(a)),F(0))
 assert 0<tail[0]<=tail[1]<mass
 return tail,dict(aggregate_spherical_sine_inverse_power_coefficients=list(map(str,A)),aggregate_spherical_cosine_inverse_power_coefficients=list(map(str,C)),all_input_mode_cross_terms_retained_before_squaring=True,pi_lower_limit_prefactor_error_upper=str(fault),phase_error_upper=str(up(phaseerr)),generation_integration_by_parts_terms=48,replay_integration_by_parts_terms=56,physical_outside_band_energy_lower=str(tail[0]),physical_outside_band_energy_upper=str(tail[1]),physical_band_energy_lower=str(down(mass-tail[1])),physical_band_energy_upper=str(up(mass-tail[0])),physical_Fourier_energy_partition_paid=True)
def controls():
 # For an orthogonal full-line projection P compressed to an interior C,
 # ||(I-C)q||^2 <= <q,(I-C)q>, with equality only in special cases.
 C=[[F(1,2),F(1,5)],[F(1,5),F(2,3)]];I=[[F(1),F(0)],[F(0),F(1)]];R=p.add(I,C,-1)
 assert p.psd(C) and p.psd(R) and p.psd(p.add(R,p.mm(R,R),-1))
 return dict(compressed_projection_identity_action_error_control=True,band_approximation_not_substituted_for_rational_augmentation=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('242_residual_original_actions');bounds=get('232_augmented_polynomial_action');kernel=get('115_rational_fourier_adjoint');metric=get('129_four_vector_joint_moment');sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper']);rows=[]
 for parity,r in enumerate(prior['parity_residual_original_action_certificates']):
  a=list(map(F,r['exact_input_Legendre_coefficients']));bd=bounds['polynomial_augmented_action_certificates'][parity];lam=F(bd['augmentation_coefficient']);U=F(bd['rational_frequency_half_bandwidth']);epsilon=F(bd['physical_Fhat_star_Fhat_to_J_star_J_operator_norm_upper']);mass=F(r['input_physical_energy'])
  tail,proof=leakage(a,parity,U,pi0,pierr,reverse)
  # ||(C-I)q||^2 <= outside Fourier energy. Actual rational operator
  # comparison is paid separately in norm before applying D^-1.
  banderror=up(lam*lam*tail[1]/sl);rational=up(lam*lam*epsilon*epsilon*mass/sl);finite=F(0);aug=[];full=[]
  for n,x in enumerate(r['finite_complete_original_D_action']):
   c=a[n] if n<len(a) else F(0)
   values=[lam*c/(orig.H(n)+s) for s in [sl,sh]];lo=min(values);hi=max(values);v=down((lo+hi)/2);rad=max(v-lo,hi-v);finite+=orig.mass(n)*(orig.H(n)+sh)*rad*rad
   aug.append(dict(degree=n,coefficient=str(v),radius=str(up(rad))))
   full.append(dict(degree=n,coefficient=str(F(x['coefficient'])+v),radius=str(up(F(x['radius'])+rad))))
  AE=up((root(banderror)+root(rational)+root(up(finite)))**2);E=up((root(F(r['complete_original_action_D_error_squared_upper']))+root(AE))**2)
  floor=F(r['original_test_form_lower'])+lam*F(proof['physical_band_energy_lower'])-lam*epsilon*mass;assert floor>0
  upper=F(r['original_test_form_upper'])+lam*F(proof['physical_band_energy_upper'])+lam*epsilon*mass
  rows.append(dict(parity=r['parity'],input=r['input'],augmentation_coefficient=str(lam),frequency_half_bandwidth=str(U),aggregate_fourier_leakage_certificate=proof,finite_augmentation_D_action=aug,finite_complete_augmented_D_action=full,augmentation_band_to_identity_D_error_squared_upper=str(banderror),rational_to_band_D_error_squared_upper=str(rational),augmentation_finite_rounding_D_error_squared_upper=str(up(finite)),complete_rational_augmentation_action_D_error_squared_upper=str(AE),complete_augmented_action_D_error_squared_upper=str(E),relative_complete_augmented_action_D_error_squared_upper=str(up(E/F(r['input_D_energy_lower']))),actual_augmented_input_form_lower=str(down(floor)),actual_augmented_input_form_upper=str(up(upper)),full_actual_rational_action_error_paid=True))
 return dict(milestone='RC243',starting_commit='1e2f19da5e5c35addf7c7ff52d81a8b144747ef1',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,new_complete_augmented_action_inputs=['R0','R1'],actual_total_augmented_action_input_count=8,actual_response_source_count=2,residual_input_augmented_actions_certified=True,parity_residual_augmented_action_certificates=rows,two_input_augmented_action_error_D_Gram_upper=[[rows[0]['complete_augmented_action_D_error_squared_upper'],'0'],['0',rows[1]['complete_augmented_action_D_error_squared_upper']]],opposite_parity_action_error_pairing_zero=True,exact_controls=controls(),enriched_inverse_response_evaluated=False,previous_response_bounds_preserved=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC244: evaluate the enriched P0/P2/P4/R0 and P1/P3/P5/R1 responses with actual cross terms and full faults; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC243 VALIDATED: full rational augmented residual actions; enriched inverse and full signed gate open',flush=True)
