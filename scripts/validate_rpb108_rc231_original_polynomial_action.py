"""RC231: original physical action on P0/P1, with complete D-energy errors.
The rational augmentation action and inverse response are not executed.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, comb
import argparse, hashlib, json
import validate_rpb108_rc230_augmentation_range_bridge as parent
ROOT=Path(__file__).resolve().parents[1];B=F(11,10);R=2*B;CUT=64
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({
 'certificates/rpb108_rc230_augmentation_range_bridge.json':'0c86b55b46e0608e4244945e8a8c6503c88176e8',
 'certificates/rpb108_rc42_native_signed_pole_head.json':'478c53d7d309d6921d7ba65274eef0feed5bc100',
 'certificates/rpb108_rc43_native_prime_head.json':'b4893953109e6fdc55d52b505c2bcfbf0d38281e',
 'certificates/rpb108_rc46_native_archimedean_head.json':'be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9',
 'certificates/rpb108_rc66_arch_multiplier_transport.json':'7cbccc7e2cba8a8714c43333e8a1d16866907cea',
 'notes/RPB108_RC46_ACTUAL_ARCHIMEDEAN_AND_COMPLETE_LOW_HEAD_20261010.md':'7a1b58255c29f6396622bbbc154afcc371722cab',
 'notes/RPB108_RC118_CANONICAL_METRIC_RESIDUAL_SOURCES_20261012.md':'71795de30804478d4b01e4b18bb0a322a5f6674b'})
HELPER_PINS['scripts/validate_rpb108_rc230_augmentation_range_bridge.py']='db5cdc3c6df5b89b8cd59bf796a85979b22c721c'
up=parent.up;down=parent.down;root=parent.rootup
def H(n):return sum((F(1,k) for k in range(1,n+1)),F(0))
def mass(n):return R/F(2*n+1)
def legendre(n):
 a=[F(1)];b=[F(0),F(1)]
 if n==0:return a
 for k in range(1,n):
  c=[F(0)]*(k+2)
  for j,v in enumerate(b):c[j+1]+=F(2*k+1,k+1)*v
  for j,v in enumerate(a):c[j]-=F(k,k+1)*v
  a,b=b,c
 return b
def integral(p,l=F(-1),r=F(1)):
 return sum((v*(r**(k+1)-l**(k+1))/F(k+1) for k,v in enumerate(p)),F(0))
def product(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  if v:
   for j,w in enumerate(b):
    if w:c[i+j]+=v*w
 return c
def dfact(n):
 v=1
 for k in range(n,0,-2):v*=k
 return v
def mono_moment(k,n):
 if k<n or (k-n)%2:return F(0)
 return F(2*factorial(k),dfact(k-n)*dfact(k+n+1))
def project(p,n):
 return F(2*n+1,2)*sum((v*mono_moment(k,n) for k,v in enumerate(p) if v),F(0))
def regular_source(j,reg):
 out=[F(0)]*(len(reg)+j+1)
 for p,a in enumerate(reg):
  c=a*B**(p+1)
  for k in range(p+2):
   val=c*comb(p+1,k)*(1+(-1)**k)/F(p+1)
   out[k+j]+=val
  if j:
   for k in range(p+3):out[k]+=c*comb(p+2,k)*((-1)**k-1)/F(p+2)
 assert all(v==0 for k,v in enumerate(out) if k%2!=j)
 return out
def prime_source(j,prime,reverse):
 terms=[];fault=F(0);qnorm=root(mass(j));A=F(1);der=F(j)/B
 for row in prime['active_prime_powers']:
  el,eh=map(F,[row['translation_lower'],row['translation_upper']]);cl,ch=map(F,[row['coefficient_lower'],row['coefficient_upper']])
  ell=(el+eh)/2;coeff=(cl+ch)/2;de=(eh-el)/2;dc=(ch-cl)/2
  fault+=2*(dc*qnorm+ch*root(2*de*A*A+R*de*de*der*der))
  for sign in [-1,1]:
   off=sign*ell/B;l=max(F(-1),-1-off);r=min(F(1),1-off)
   poly=[-coeff] if j==0 else [-coeff*off,-coeff]
   terms.append(dict(n=row['n'],orientation=sign,offset=off,left=l,right=r,coefficients=poly))
 knots=sorted({F(-1),F(1)}|{v for t in terms for v in [t['left'],t['right']]});segments=[]
 for l,r in zip(knots,knots[1:]):
  mid=(l+r)/2;p=[F(0)]*(j+1)
  for t in terms:
   if t['left']<mid<t['right']:
    for k,v in enumerate(t['coefficients']):p[k]+=v
  segments.append((l,r,p))
 assert len(segments)==15 and len(terms)==14
 for l,r,p in segments:
  mirrored=next(q for ll,rr,q in segments if ll==-r and rr==-l)
  assert mirrored==[(-1)**(j+k)*v for k,v in enumerate(p)]
 norm=B*sum((integral(product(p,p),l,r) for l,r,p in segments),F(0));assert norm>0
 coeff=[]
 for n in range(CUT+1):
  if n%2!=j:coeff.append(F(0));continue
  vals=[integral(product(p,legendre(n)),l,r) for l,r,p in segments]
  if reverse:vals.reverse()
  coeff.append(F(2*n+1,2)*sum(vals,F(0)))
 tail=norm-sum((mass(n)*x*x for n,x in enumerate(coeff)),F(0));assert tail>=0
 # Independent affine integration verifies each piece's norm.
 for l,r,p in segments:
  affine=[sum((p[k]*comb(k,i)*l**(k-i) for k in range(i,len(p))),F(0))*(r-l)**i for i in range(len(p))]
  assert integral(product(p,p),l,r)==(r-l)*sum((v/F(k+1) for k,v in enumerate(product(affine,affine))),F(0))
 return coeff,up(tail),up(fault),[dict(left=str(l),right=str(r),physical_t_polynomial=list(map(str,p))) for l,r,p in segments]
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 assert get('230_augmentation_range_bridge')['full_chosen_augmentation_rank']==639
 metric=get('129_four_vector_joint_moment');sl=F(metric['actual_D_Gram_entry_lower'][0][0])/R;sh=F(metric['actual_D_Gram_entry_upper'][0][0])/R;assert 0<sl<=sh
 # Exact positive atanh series with its geometric remainder.
 loglo=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0));loghi=loglo+2*F(1,3)**201/(201*(1-F(1,9)))
 reg=list(map(F,get('46_native_archimedean_head')['regular_kernel_coefficients']));assert len(reg)==193
 alternate=[]
 for n in range(194):alternate.append(F(1,2)*F(-1,2)**n/factorial(n)-sum((alternate[n-k]*F(-2)**k/factorial(k+1) for k in range(1,n+1)),F(0)))
 assert alternate[0]==F(1,2) and alternate[1:]==reg
 epsreg=F(get('46_native_archimedean_head')['regular_kernel_uniform_error_upper']);assert epsreg==F(375,4)*F(11,15)**193
 prime=get('43_native_prime_head');assert prime['complete_active_prime_set_certified'] and [x['n'] for x in prime['active_prime_powers']]==[2,3,4,5,7,8,9]
 expbound=sum((F(11,20)**k/factorial(k) for k in range(41)),F(0))+F(11,20)**41/factorial(41)/(1-F(11,840));assert expbound<2
 tau=2*F(11,20)**41/factorial(41);rows=[]
 for j in [0,1]:
  regular=regular_source(j,reg);rc=[project(regular,n) for n in range(len(regular))]
  # Orthogonal polynomial expansion is checked independently at low degrees.
  for n in range(12):assert project(regular,n)==F(2*n+1,2)*integral(product(regular,legendre(n)))
  rtail=sum((mass(n)*x*x for n,x in enumerate(rc) if n>CUT),F(0));rtail=up(rtail)
  pc,ptail,pfault,segs=prime_source(j,prime,reverse)
  phi=[F(11,20)**k/factorial(k) if k%2==j else F(0) for k in range(41)]
  moment=B*integral([F(0)]*j+phi);pole=[2*(-1)**j*moment*v for v in phi];oc=[project(pole,n) for n in range(CUT+1)]
  polefault=up(16*B*tau*root(mass(j)))
  action=[];roundsq=F(0)
  for n in range(CUT+1):
   if n%2!=j:action.append(dict(degree=n,coefficient='0',radius='0'));continue
   hconst=2*H(2*n)-2*H(n)+F(1,2*n+1) if n==j else F(2*n+1,abs(n-j)*(n+j+1))
   lo=hconst-(loghi if n==j else 0)-rc[n]+pc[n]+oc[n]-(F(789,125) if n==j else 0)
   hi=hconst-(loglo if n==j else 0)-rc[n]+pc[n]+oc[n]-(F(789,125) if n==j else 0)
   endpoints=[v/(H(n)+s) for v in [lo,hi] for s in [sl,sh]];al=min(endpoints)+(n==j);ah=max(endpoints)+(n==j)
   center=down((al+ah)/2);rad=max(center-al,ah-center);roundsq+=mass(n)*(H(n)+sh)*rad*rad
   action.append(dict(degree=n,coefficient=str(center),radius=str(up(rad))))
  first=CUT+1 if (CUT+1)%2==j else CUT+2
  endpoint=up(3*B/(sl*(CUT-j)**2))
  regtail=up(rtail/(H(first)+sl));primetail=up(ptail/(H(first)+sl))
  # Dividing by an upward sqrt would underpay. All physical errors are
  # instead squared and divided by the exact positive lower floor.
  regularfaultsq=up((R*epsreg)**2*mass(j)/sl);primefaultsq=up(pfault**2/sl);polefaultsq=up(polefault**2/sl)
  total=up((root(up(roundsq))+root(endpoint)+root(regtail)+root(primetail)+root(regularfaultsq)+root(primefaultsq)+root(polefaultsq))**2)
  inputlo=mass(j)*(H(j)+sl);inputhi=mass(j)*(H(j)+sh)
  rows.append(dict(parity='even' if j==0 else 'odd',input='P'+str(j),input_D_energy_lower=str(inputlo),input_D_energy_upper=str(inputhi),output_degree_cutoff=CUT,finite_original_D_action=action,prime_physical_segments=segs,regular_polynomial_degree=len(regular)-1,regular_omitted_physical_norm_squared_upper=str(rtail),prime_nominal_physical_omitted_norm_squared_upper=str(ptail),prime_actual_translation_coefficient_fault_physical_norm_upper=str(pfault),signed_pole_model_degree=40,signed_pole_sign=1 if j==0 else -1,signed_pole_actual_physical_error_norm_upper=str(polefault),D_energy_component_squared_errors=dict(finite_rounding=str(up(roundsq)),endpoint_omitted_output=str(endpoint),regular_omitted_output=str(regtail),prime_omitted_output=str(primetail),regular_kernel=str(regularfaultsq),prime_arithmetic=str(primefaultsq),pole_Taylor=str(polefaultsq)),complete_original_action_D_error_squared_upper=str(total),relative_to_input_D_error_squared_upper=str(up(total/inputlo)),all_component_cross_terms_paid_by_norm_triangle=True))
  print('RC231 original action',j,'certified',flush=True)
 k=get('66_arch_multiplier_transport')['complete_physical_operator_parity_norm_upper']
 relative=max(F(r['relative_to_input_D_error_squared_upper']) for r in rows)
 errorgram=[[rows[0]['complete_original_action_D_error_squared_upper'],'0'],['0',rows[1]['complete_original_action_D_error_squared_upper']]]
 return dict(milestone='RC231',starting_commit='5abf4006352a7def7aebd9c00e865e9a957aa56e',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,archimedean_exact_identity='L_arch=D+h-(789/125)I-K_reg',bounded_archimedean_remainder_exact_identity='K_arch=-K_reg-R_canonical',original_D_operator='N0=I+D^-1[h-(789/125)I-K_reg+K_prime+K_pole]',chosen_augmented_D_operator='N=N0+lambda D^-1 Fhat*Fhat',canonical_Poisson_remainder_cancels_exactly=True,canonical_M_action_required_by_direct_original_formula=False,whole_form_domain_identity_proved_in_note=True,complete_active_prime_powers=[2,3,4,5,7,8,9],complete_physical_K_parity_norm_upper=k,polynomial_original_action_certificates=rows,two_input_error_D_Gram_upper=errorgram,two_input_relative_D_action_error_squared_upper=str(relative),all_complex_combinations_of_P0_P1_covered=True,opposite_parity_error_pairing_exactly_zero=True,actual_original_physical_actions_performed=True,actual_original_D_energy_actions_enclosed=True,actual_action_test_dimension=2,all_639_source_actions_executed=False,actual_rational_augmentation_actions_performed=False,actual_augmented_inverse_responses_computed=False,original_augmented_response_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC232: certify rational augmentation actions and extend the direct original D-action interface to response trials/full-range residuals; no original inverse gate has yet been tested')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();c=run(args.replay)
 if args.replay:assert c==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC231 PASS: actual original P0/P1 D-action enclosures; augmentation/inverse gate open',flush=True)
