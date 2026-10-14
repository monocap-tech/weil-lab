"""RC234: actual band-action coefficients, paid rational augmentation,
and rechecked augmented inverse responses; no full auxiliary norm gate."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
import argparse,hashlib,json
import validate_rpb108_rc233_augmented_inverse_response as parent
bridge=parent.bridge;orig=parent.original
up=bridge.up;down=bridge.down;root=bridge.rootup;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc233_augmented_inverse_response.json':'868fcfb1536e377a9eacb06e6976af46920ac589','notes/RPB108_RC233_ACTUAL_AUGMENTED_INVERSE_RESPONSE_ENCLOSURES_20261014.md':'5ee0c7dc1c5303b26ee5c55dac37f0bb11aa5b48'})
HELPER_PINS['scripts/validate_rpb108_rc233_augmented_inverse_response.py']='679e0e9029aadc7af548f4c6a2335bbecf4aa93d'
B=F(11,10);CUT=64
def ip(x):return down(x),up(x)
def ia(a,b):return down(a[0]+b[0]),up(a[1]+b[1])
def im(a,b):
 v=[x*y for x in a for y in b];return down(min(v)),up(max(v))
def isc(a,s):return im(a,ip(s))
def neg(a):return -a[1],-a[0]
def outer24(a):
 d=10**24
 return F(a[0].numerator*d//a[0].denominator,d),F(-(-a[1].numerator*d//a[1].denominator),d)
def polyadd(a,b):
 c=[F(0)]*max(len(a),len(b))
 for k,v in enumerate(a):c[k]+=v
 for k,v in enumerate(b):c[k]+=v
 return c
def spherical_polynomials():
 aa=[[F(0),F(1)],[F(0),F(0),F(1)]];bb=[[F(0)],[F(0),-F(1)]]
 for n in range(1,CUT):
  aa.append(polyadd([F(0)]+[(2*n+1)*v for v in aa[n]],[-v for v in aa[n-1]]))
  bb.append(polyadd([F(0)]+[(2*n+1)*v for v in bb[n]],[-v for v in bb[n-1]]))
 # Independent finite integration-by-parts boundary derivatives of P_n.
 for n in range(CUT+1):
  A=[F(0)]*(n+2);C=[F(0)]*(n+2)
  for k in range(n+1):
   d=F(factorial(n+k),2**k*factorial(k)*factorial(n-k))
   if (n+k)%2==0:A[k+1]=d*(-1)**((n-k)//2)
   else:C[k+1]=-d*(-1)**((n-k-1)//2)
  assert aa[n]+[F(0)]*(len(A)-len(aa[n]))==A
  assert bb[n]+[F(0)]*(len(C)-len(bb[n]))==C
 return aa,bb
def band_coefficients(U,j,pi0,pierr,aa,bb,reverse):
 z=2*pi0*B*U;assert z>400
 turns=int(2*B*U+F(1,2));theta=2*pi0*(2*B*U-turns);assert abs(theta)<F(22,7)
 cv=sum(((-1)**k*theta**(2*k)/factorial(2*k) for k in range(41)),F(0))
 sv=sum(((-1)**k*theta**(2*k+1)/factorial(2*k+1) for k in range(40)),F(0))
 phaseerr=abs(theta)**81/factorial(81)+2*abs(turns)*pierr
 cosine=ia(ip(cv),(-up(phaseerr),up(phaseerr)));sine=ia(ip(sv),(-up(phaseerr),up(phaseerr)))
 L=56 if reverse else 48;moments={}
 for m in range(2,CUT+4):
  rr=F(0);ii=F(0);rising=1
  for k in range(L):
   v=F(rising,2**(k+1))/z**k
   if k%4==0:ii+=v
   elif k%4==1:rr+=v
   elif k%4==2:ii-=v
   else:rr-=v
   rising*=m+k
  rem=F(rising,2**L)*z**(1-L)/F(m+L-1)
  Rr=ia(ip(rr),(-up(rem),up(rem)));Ii=ia(ip(ii),(-up(rem),up(rem)))
  moments[m]=(ia(im(cosine,Rr),neg(im(sine,Ii))),ia(im(sine,Rr),im(cosine,Ii)))
 # Actual pi changes the lower integration limit and physical prefactor.
 pil=pi0-pierr;assert pil>3 and pi0+pierr<4
 pi_fault=up(4*B/pil*(2*B*U*pierr)+8*B*pierr/(pil*pi0))
 gram=[]
 for n in range(CUT+1):
  if n%2!=j:gram.append((F(0),F(0)));continue
  a=orig.product(aa[n],aa[j]);b=orig.product(bb[n],bb[j]);c=polyadd(orig.product(aa[n],bb[j]),orig.product(bb[n],aa[j]))
  size=max(len(a),len(b),len(c));a+= [F(0)]*(size-len(a));b+=[F(0)]*(size-len(b));c+=[F(0)]*(size-len(c));total=ip(F(0))
  degrees=list(range(2,size));degrees=degrees[::-1] if reverse else degrees
  for m in degrees:
   c0=(a[m]+b[m])/2;cc=(b[m]-a[m])/2;cs=c[m]/2
   if c0:total=ia(total,ip(c0*z**(1-m)/F(m-1)))
   if cc:total=ia(total,im(ip(cc/z**m),moments[m][0]))
   if cs:total=ia(total,im(ip(cs/z**m),moments[m][1]))
  tail=isc(total,F(4)*B/pi0*(-1)**((n-j)//2));tail=ia(tail,(-pi_fault,pi_fault))
  g=ia(ip(orig.mass(j) if n==j else F(0)),neg(tail));gram.append(outer24(g))
 assert gram[j][0]>0 and gram[j][1]<orig.mass(j)
 return gram,dict(phase_reduction_turns=turns,pi_lower_limit_prefactor_error_upper=str(pi_fault),sin_cos_phase_error_upper=str(up(phaseerr)),stored_band_Gram_grid='1/10^24',generation_integration_by_parts_terms=48,replay_integration_by_parts_terms=56)
def recheck_inverse(j,A,E,flo,fhi,mu,nu,sl,sh,old):
 mass=orig.mass(j);glo=1/(orig.H(j)+sh);ghi=1/(orig.H(j)+sl);g=down((glo+ghi)/2);rad=max(g-glo,ghi-g)
 sourceerr=up(mass*(orig.H(j)+sh)*rad**2)
 def trial(t):
  v=[(g if n==j else F(0))-t*x for n,x in enumerate(A)]
  nl=sum((orig.mass(n)*(orig.H(n)+sl)*x*x for n,x in enumerate(v)),F(0));nh=sum((orig.mass(n)*(orig.H(n)+sh)*x*x for n,x in enumerate(v)),F(0))
  fault=root(sourceerr)+t*root(E);rl=down(max(F(0),parent.rootdown(nl)-fault)**2);rh=up((root(nh)+fault)**2)
  cl=down(2*t*mass-t*t*fhi);ch=up(2*t*mass-t*t*flo)
  return dict(trial_coefficient=str(t),residual_D_Gram_lower=str(rl),residual_D_Gram_upper=str(rh),signed_variational_center_lower=str(cl),signed_variational_center_upper=str(ch),added_residual_correction_lower=str(down(rl/nu)),added_residual_correction_upper=str(up(rh/mu)),response_lower=str(down(cl+rl/nu)),response_upper=str(up(ch+rh/mu)))
 trials=[trial(F(old['selected_lower_trial']['trial_coefficient'])),trial(F(old['selected_upper_trial']['trial_coefficient'])),trial(mass/fhi)]
 lower=max(trials,key=lambda r:F(r['response_lower']));upper=min(trials,key=lambda r:F(r['response_upper']))
 lo=max(F(old['actual_augmented_inverse_response_lower']),F(lower['response_lower']));hi=min(F(old['actual_augmented_inverse_response_upper']),F(upper['response_upper']))
 assert 0<lo<=hi<F(old['actual_augmented_inverse_response_upper'])
 return dict(source=old['actual_canonical_source'],selected_lower_trial=lower,selected_upper_trial=upper,actual_inverse_response_lower=str(lo),actual_inverse_response_upper=str(hi),previous_inverse_response_lower=old['actual_augmented_inverse_response_lower'],previous_inverse_response_upper=old['actual_augmented_inverse_response_upper'],actual_inverse_response_width_upper=str(up(hi-lo)),old_enclosure_intersected=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(raw) if path.endswith('.json') else raw.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 old=get('233_augmented_inverse_response');prev=get('232_augmented_polynomial_action');original=get('231_original_polynomial_action');kernel=get('115_rational_fourier_adjoint');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B)
 pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper']);aa,bb=spherical_polynomials();rows=[]
 for j in [0,1]:
  pr=prev['polynomial_augmented_action_certificates'][j];o=original['polynomial_original_action_certificates'][j];lam=F(pr['augmentation_coefficient']);U=F(pr['rational_frequency_half_bandwidth']);epsilon=F(pr['physical_Fhat_star_Fhat_to_J_star_J_operator_norm_upper'])
  gram,controls=band_coefficients(U,j,pi0,pierr,aa,bb,reverse);band=[isc(g,1/orig.mass(n)) for n,g in enumerate(gram)]
  captured=sum((orig.mass(n)*minabs(a)**2 for n,a in enumerate(band)),F(0))
  tail=up(gram[j][1]-captured);assert tail>=0
  first=CUT+1 if (CUT+1)%2==j else CUT+2;dtail=up(lam**2*tail/(orig.H(first)+sl))
  coeff=[];finite_error=F(0)
  for n,a in enumerate(band):
   if n%2!=j:coeff.append(dict(degree=n,coefficient='0',radius='0'));continue
   vals=[lam*v/(orig.H(n)+s) for v in a for s in [sl,sh]];lo=min(vals);hi=max(vals);c=down((lo+hi)/2);r=max(c-lo,hi-c);finite_error+=orig.mass(n)*(orig.H(n)+sh)*r*r
   coeff.append(dict(degree=n,coefficient=str(c),radius=str(up(r))))
  rational_error=up(lam**2*epsilon**2*orig.mass(j)/sl)
  augerror=up((root(up(finite_error))+root(dtail)+root(rational_error))**2)
  assert augerror<F(pr['actual_augmentation_action_D_error_squared_upper'])+F(pr['augmentation_trial_rounding_D_error_squared_upper'])
  E=up((root(F(o['complete_original_action_D_error_squared_upper']))+root(augerror))**2);assert E<F(pr['complete_augmented_action_D_error_squared_upper'])
  action=[]
  for x,y in zip(o['finite_original_D_action'],coeff):action.append(dict(degree=x['degree'],coefficient=str(F(x['coefficient'])+F(y['coefficient'])),radius=str(up(F(x['radius'])+F(y['radius'])))))
  # Omitted output has zero pairing with the input Pj. Only model faults
  # and the retained coefficient interval enter this sharper form bound.
  c=F(o['finite_original_D_action'][j]['coefficient']);r=F(o['finite_original_D_action'][j]['radius']);idl=F(o['input_D_energy_lower']);idh=F(o['input_D_energy_upper'])
  formvals=[v*w for v in [c-r,c+r] for w in [idl,idh]]
  d=o['D_energy_component_squared_errors'];ffault=sum((root(F(d[k])) for k in ['regular_kernel','prime_arithmetic','pole_Taylor']),F(0))*root(idh)
  original_lo=down(min(formvals)-ffault);original_hi=up(max(formvals)+ffault);assert original_lo>0
  flo=down(original_lo+lam*gram[j][0]-lam*epsilon*orig.mass(j));fhi=up(original_hi+lam*gram[j][1]+lam*epsilon*orig.mass(j));assert 0<flo<=fhi
  response=recheck_inverse(j,[F(r['coefficient']) for r in action],E,flo,fhi,F(pr['fresh_augmented_N_D_lower']),F(pr['fresh_augmented_N_D_upper']),sl,sh,old['parity_inverse_response_certificates'][j])
  rows.append(dict(parity=pr['parity'],input='P'+str(j),rational_band=str(U),actual_band_Gram_column=[dict(degree=n,lower=str(a),upper=str(b)) for n,(a,b) in enumerate(gram)],band_materialization_controls=controls,physical_band_action_tail_squared_upper=str(tail),augmentation_omitted_output_D_error_squared_upper=str(dtail),augmentation_finite_rounding_D_error_squared_upper=str(up(finite_error)),rational_to_band_augmentation_D_error_squared_upper=str(rational_error),actual_augmentation_action_D_error_squared_upper=str(augerror),previous_augmentation_action_D_error_squared_upper=pr['actual_augmentation_action_D_error_squared_upper'],finite_complete_augmented_D_action=action,complete_augmented_action_D_error_squared_upper=str(E),previous_complete_augmented_action_D_error_squared_upper=pr['complete_augmented_action_D_error_squared_upper'],relative_augmented_D_action_error_squared_upper=str(up(E/idl)),sharper_original_test_form_lower=str(original_lo),sharper_original_test_form_upper=str(original_hi),sharper_augmented_test_form_lower=str(flo),sharper_augmented_test_form_upper=str(fhi),updated_actual_augmented_inverse_response=response))
 return dict(milestone='RC234',starting_commit='a4da25ca2ed083616007e77d34c14d8d894c6cae',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_band_action_columns_materialized=True,actual_rational_augmentation_difference_paid=True,chosen_rational_operator_unchanged=True,output_degree_cutoff=64,spherical_polynomial_independent_boundary_controls=65,parity_materialized_augmented_action_certificates=rows,actual_augmented_inverse_response_lower=[[rows[0]['updated_actual_augmented_inverse_response']['actual_inverse_response_lower'],'0'],['0',rows[1]['updated_actual_augmented_inverse_response']['actual_inverse_response_lower']]],actual_augmented_inverse_response_upper=[[rows[0]['updated_actual_augmented_inverse_response']['actual_inverse_response_upper'],'0'],['0',rows[1]['updated_actual_augmented_inverse_response']['actual_inverse_response_upper']]],both_parity_complete_action_and_inverse_uppers_improved=True,all_complex_combinations_of_r0_r1_covered=True,opposite_parity_pairings_zero=True,full_639_auxiliary_range_enclosed=False,frequency_auxiliary_metric_evaluated=False,original_augmented_response_norm_below_one_certified=False,canonical_inverse_half_width_gate_transferred=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC235: use the materialized band-action interface for richer actual response/source trials and full-range residual/auxiliary metric contracts; tighter r0/r1 enclosures are not the full frequency norm gate')
def minabs(a):return F(0) if a[0]<=0<=a[1] else min(abs(a[0]),abs(a[1]))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();c=run(args.replay)
 if args.replay:assert c==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC234 PASS: materialized band actions tighten both actual augmented inverse-response enclosures; full auxiliary gate open',flush=True)
