"""RC237: complete P2/P3 actions and two trials per parity for the
original-action inverse sources. All acceptance uses actual D metrics."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
import argparse,hashlib,json
import validate_rpb108_rc236_full_range_signed_response as previous
material=previous.parent.parent;bridge=previous.bridge;orig=previous.orig;p=bridge.p
up=bridge.up;down=bridge.down;root=bridge.rootup;rootdown=previous.rootdown
ip=material.ip;ia=material.ia;im=material.im;isc=material.isc;neg=material.neg;outer24=material.outer24;polyadd=material.polyadd
ROOT=Path(__file__).resolve().parents[1];B=F(11,10);CUT=64
PINS=dict(previous.PINS);HELPER_PINS=dict(previous.HELPER_PINS)
PINS.update({'certificates/rpb108_rc236_full_range_signed_response.json':'5f7ddc20d11c114ad1f124b64cf14fe668ff7a87','notes/RPB108_RC236_EXHAUSTIVE_PHYSICAL_PARAMETERIZATION_AND_SIGNED_RESPONSE_20261014.md':'1151f0f7fa0aa56acf8b21869a9bc0e1baf272e6'})
HELPER_PINS['scripts/validate_rpb108_rc236_full_range_signed_response.py']='60711dbb1937730d9260343828332555b5569d6d'
def regular_poly(d,reg):
 q=orig.legendre(d)
 v=[sum((q[k]*comb(k,m)*2**m*(-1)**(k-m) for k in range(m,len(q))),F(0)) for m in range(len(q))]
 left=[F(0)]*(len(reg)+d+1)
 for k,a in enumerate(reg):
  for m,b in enumerate(v):left[k+m+1]+=2*B*a*(2*B)**k*b*F(factorial(k)*factorial(m),factorial(k+m+1))
 out=[sum((left[k]*comb(k,l)/2**k for k in range(l,len(left))),F(0))*(1+(-1)**(d+l)) for l in range(len(left))]
 assert all(v==0 for k,v in enumerate(out) if (k-d)%2)
 return out
def prime_poly(d,prime,reverse):
 q=orig.legendre(d);A=sum(map(abs,q),F(0));der=sum((k*abs(v) for k,v in enumerate(q)),F(0))/B;fault=F(0);terms=[]
 for row in prime['active_prime_powers']:
  el,eh=map(F,[row['translation_lower'],row['translation_upper']]);cl,ch=map(F,[row['coefficient_lower'],row['coefficient_upper']]);ell=(el+eh)/2;c=(cl+ch)/2;de=(eh-el)/2;dc=(ch-cl)/2
  fault+=2*(dc*root(orig.mass(d))+ch*root(2*de*A*A+2*B*de*de*der*der))
  for sign in [-1,1]:
   off=sign*ell/B;l=max(F(-1),-1-off);r=min(F(1),1-off)
   poly=[-c*sum((q[k]*comb(k,m)*off**(k-m) for k in range(m,len(q))),F(0)) for m in range(len(q))]
   terms.append((l,r,poly))
 knots=sorted({F(-1),F(1)}|{v for l,r,_ in terms for v in [l,r]});segments=[]
 for l,r in zip(knots,knots[1:]):
  mid=(l+r)/2;poly=[sum((q[k] for a,b,q in terms if a<mid<b),F(0)) for k in range(d+1)];segments.append((l,r,poly))
 assert len(terms)==14 and len(segments)==15
 for l,r,q in segments:
  other=next(v for a,b,v in segments if a==-r and b==-l);assert other==[(-1)**(d+k)*v for k,v in enumerate(q)]
 norm=B*sum((orig.integral(orig.product(q,q),l,r) for l,r,q in segments),F(0));coeff=[]
 for n in range(CUT+1):
  if (n-d)%2:coeff.append(F(0));continue
  terms=[orig.integral(orig.product(q,orig.legendre(n)),l,r) for l,r,q in segments]
  if reverse:terms.reverse()
  coeff.append(F(2*n+1,2)*sum(terms,F(0)))
 tail=norm-sum((orig.mass(n)*v*v for n,v in enumerate(coeff)),F(0));assert tail>=0
 for l,r,q in segments:
  affine=[sum((q[k]*comb(k,m)*l**(k-m) for k in range(m,len(q))),F(0))*(r-l)**m for m in range(len(q))]
  assert orig.integral(orig.product(q,q),l,r)==(r-l)*sum((v/F(k+1) for k,v in enumerate(orig.product(affine,affine))),F(0))
 return coeff,up(tail),up(fault),[dict(left=str(l),right=str(r),polynomial=list(map(str,q))) for l,r,q in segments]
def new_original_action(d,reg,prime,eps,sl,sh,reverse):
 assert d in [2,3] and CUT+1>=3*d+1
 q=regular_poly(d,reg);rc=[orig.project(q,n) for n in range(len(q))]
 for n in range(12):assert rc[n]==F(2*n+1,2)*orig.integral(orig.product(q,orig.legendre(n)))
 rtail=up(sum((orig.mass(n)*v*v for n,v in enumerate(rc) if n>CUT),F(0)))
 pc,ptail,pfault,segments=prime_poly(d,prime,reverse)
 phi=[F(11,20)**k/factorial(k) if k%2==d%2 else F(0) for k in range(41)]
 moment=B*orig.integral(orig.product(orig.legendre(d),phi));pole=[2*(-1)**d*moment*v for v in phi];oc=[orig.project(pole,n) for n in range(CUT+1)]
 tau=2*F(11,20)**41/factorial(41);polefault=up(16*B*tau*root(orig.mass(d)))
 ll=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0));lh=ll+2*F(1,3)**201/(201*(1-F(1,9)));out=[];rounding=F(0)
 for n in range(CUT+1):
  if (n-d)%2:out.append(dict(degree=n,coefficient='0',radius='0'));continue
  h=2*orig.H(2*n)-2*orig.H(n)+F(1,2*n+1) if n==d else F(2*n+1,abs(n-d)*(n+d+1))
  lo=h-(lh if n==d else 0)-rc[n]+pc[n]+oc[n]-(F(789,125) if n==d else 0);hi=h-(ll if n==d else 0)-rc[n]+pc[n]+oc[n]-(F(789,125) if n==d else 0)
  values=[v/(orig.H(n)+s)+(n==d) for v in [lo,hi] for s in [sl,sh]];a=min(values);b=max(values);c=down((a+b)/2);r=max(c-a,b-c);rounding+=orig.mass(n)*(orig.H(n)+sh)*r*r
  out.append(dict(degree=n,coefficient=str(c),radius=str(up(r))))
 first=CUT+1 if (CUT+1-d)%2==0 else CUT+2
 components=dict(finite_rounding=up(rounding),endpoint_omitted_output=up(3*B/(sl*(CUT-d)**2)),regular_omitted_output=up(rtail/(orig.H(first)+sl)),prime_omitted_output=up(ptail/(orig.H(first)+sl)),regular_kernel=up((2*B*eps)**2*orig.mass(d)/sl),prime_arithmetic=up(pfault**2/sl),pole_Taylor=up(polefault**2/sl))
 total=up(sum((root(v) for v in components.values()),F(0))**2)
 return dict(input='P'+str(d),input_degree=d,parity='even' if d%2==0 else 'odd',input_D_energy_lower=str(orig.mass(d)*(orig.H(d)+sl)),input_D_energy_upper=str(orig.mass(d)*(orig.H(d)+sh)),finite_original_D_action=out,D_energy_component_squared_errors={k:str(v) for k,v in components.items()},complete_original_action_D_error_squared_upper=str(total),prime_segments=segments,complete_prime_pairs=7,signed_pole_sign=(-1)**d)

def extended_band_coefficients(U,j,pi0,pierr,aa,bb,reverse):
 z=2*pi0*B*U;assert z>400
 turns=int(2*B*U+F(1,2));theta=2*pi0*(2*B*U-turns);assert abs(theta)<F(22,7)
 cv=sum(((-1)**k*theta**(2*k)/factorial(2*k) for k in range(41)),F(0))
 sv=sum(((-1)**k*theta**(2*k+1)/factorial(2*k+1) for k in range(40)),F(0))
 phaseerr=abs(theta)**81/factorial(81)+2*abs(turns)*pierr
 cosine=ia(ip(cv),(-up(phaseerr),up(phaseerr)));sine=ia(ip(sv),(-up(phaseerr),up(phaseerr)))
 L=56 if reverse else 48;moments={}
 for m in range(2,CUT+j+3):
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
  if n%2!=j%2:gram.append((F(0),F(0)));continue
  a=orig.product(aa[n],aa[j]);b=orig.product(bb[n],bb[j]);c=polyadd(orig.product(aa[n],bb[j]),orig.product(bb[n],aa[j]))
  size=max(len(a),len(b),len(c));a+= [F(0)]*(size-len(a));b+=[F(0)]*(size-len(b));c+=[F(0)]*(size-len(c));total=ip(F(0))
  degrees=list(range(2,size));degrees=degrees[::-1] if reverse else degrees
  for m in degrees:
   c0=(a[m]+b[m])/2;cc=(b[m]-a[m])/2;cs=c[m]/2
   if c0:total=ia(total,ip(c0*z**(1-m)/F(m-1)))
   if cc:total=ia(total,im(ip(cc/z**m),moments[m][0]))
   if cs:total=ia(total,im(ip(cs/z**m),moments[m][1]))
  tail=isc(total,F(4)*B/pi0*(-1 if ((n-j)//2)%2 else 1));tail=ia(tail,(-pi_fault,pi_fault))
  g=ia(ip(orig.mass(j) if n==j else F(0)),neg(tail));gram.append(outer24(g))
 assert gram[j][0]>0 and gram[j][1]<orig.mass(j)
 return gram,dict(phase_reduction_turns=turns,pi_lower_limit_prefactor_error_upper=str(pi_fault),sin_cos_phase_error_upper=str(up(phaseerr)),stored_band_Gram_grid='1/10^24',generation_integration_by_parts_terms=48,replay_integration_by_parts_terms=56)

def augmentation(d,gram,lam,epsilon,sl,sh):
 band=[isc(a,1/orig.mass(n)) for n,a in enumerate(gram)]
 captured=sum((orig.mass(n)*material.minabs(a)**2 for n,a in enumerate(band)),F(0));tail=up(gram[d][1]-captured);assert tail>=0
 first=CUT+1 if (CUT+1-d)%2==0 else CUT+2;dtail=up(lam**2*tail/(orig.H(first)+sl));finite=F(0);coeff=[]
 for n,a in enumerate(band):
  if (n-d)%2:coeff.append(dict(degree=n,coefficient='0',radius='0'));continue
  v=[lam*x/(orig.H(n)+s) for x in a for s in [sl,sh]];lo=min(v);hi=max(v);c=down((lo+hi)/2);r=max(c-lo,hi-c);finite+=orig.mass(n)*(orig.H(n)+sh)*r*r
  coeff.append(dict(degree=n,coefficient=str(c),radius=str(up(r))))
 rational=up(lam**2*epsilon**2*orig.mass(d)/sl);E=up((root(up(finite))+root(dtail)+root(rational))**2)
 return coeff,E,dict(physical_band_output_tail_squared_upper=str(tail),augmentation_D_omitted_output_squared_upper=str(dtail),augmentation_D_finite_rounding_squared_upper=str(up(finite)),rational_to_band_D_error_squared_upper=str(rational))
def original_entry(i,column,sl,sh):
 row=column['finite_original_D_action'][i];c=F(row['coefficient']);r=F(row['radius']);w=[orig.mass(i)*(orig.H(i)+s) for s in [sl,sh]]
 values=[a*b for a in [c-r,c+r] for b in w];errors=column['D_energy_component_squared_errors']
 fault=sum((root(F(errors[k])) for k in ['regular_kernel','prime_arithmetic','pole_Taylor']),F(0))*root(w[1])
 return down(min(values)-fault),up(max(values)+fault)
def loewner(intervals):
 C=[[(a+b)/2 for a,b in row] for row in intervals];r=[sum(((b-a)/2 for a,b in row),F(0)) for row in intervals]
 L=[[C[i][j]-(r[i] if i==j else 0) for j in range(2)] for i in range(2)];H=[[C[i][j]+(r[i] if i==j else 0) for j in range(2)] for i in range(2)]
 return L,H
def quadratic(intervals,v):
 lo=hi=F(0)
 for i in range(2):
  for j in range(2):
   a,b=intervals[i][j];w=v[i]*v[j];lo+=min(w*a,w*b);hi+=max(w*a,w*b)
 return down(lo),up(hi)
def response(base,columns,F0,Gy,lam,mu,nu,sl,sh,prior,reverse):
 O=[[F(r['coefficient']) for r in c['original']['finite_original_D_action']] for c in columns]
 A=[[F(r['coefficient']) for r in c['finite_complete_augmented_D_action']] for c in columns]
 Eo=[F(c['original']['complete_original_action_D_error_squared_upper']) for c in columns];Ea=[F(c['augmentation_action_D_error_squared_upper']) for c in columns]
 sm=(sl+sh)/2
 AG=[[sum((orig.mass(n)*(orig.H(n)+sm)*A[i][n]*A[k][n] for n in range(CUT+1)),F(0)) for k in range(2)] for i in range(2)]
 b=[sum((orig.mass(n)*(orig.H(n)+sm)*O[0][n]*A[i][n] for n in range(CUT+1)),F(0)) for i in range(2)]
 assert p.psd(AG) and p.inv(AG)
 least=p.mm(p.inv(AG),[[v] for v in b]);least=[down(v[0]) for v in least]
 GM=[[(F0[i][k][0]+F0[i][k][1]+lam*(Gy[i][k][0]+Gy[i][k][1]))/2 for k in range(2)] for i in range(2)]
 fm=[(F0[i][0][0]+F0[i][0][1])/2 for i in range(2)];gal=[down(v[0]) for v in p.mm(p.inv(GM),[[v] for v in fm])]
 old=[F(prior['selected_inverse_upper_trial']['trial_coefficient']),F(0)]
 choices={tuple(old),(F(0),F(0)),tuple(least),tuple(gal)}
 for k in range(-10,21):choices.add(tuple(down(old[i]+F(k,10)*(least[i]-old[i])) for i in range(2)))
 for k in range(8,13):
  choices.add(tuple(down(F(k,10)*v) for v in least));choices.add(tuple(down(F(k,10)*v) for v in gal))
 def trial(y):
  v=[O[0][n]-sum((y[i]*A[i][n] for i in range(2)),F(0)) for n in range(CUT+1)]
  terms=[(n,orig.mass(n)*x*x) for n,x in enumerate(v)]
  if reverse:terms.reverse()
  nl=sum((x*(orig.H(n)+sl) for n,x in terms),F(0));nh=sum((x*(orig.H(n)+sh) for n,x in terms),F(0))
  fault=abs(1-y[0])*root(Eo[0])+abs(y[1])*root(Eo[1])+sum((abs(y[i])*root(Ea[i]) for i in range(2)),F(0))
  rl=down(max(F(0),rootdown(nl)-fault)**2);rh=up((root(nh)+fault)**2)
  u=[1-y[0],-y[1]];qlo,qhi=quadratic(F0,u);alo,ahi=quadratic(Gy,y);gaplo=down(qlo+lam*alo-rh/mu);gaphi=up(qhi+lam*ahi-rl/nu)
  # Entrywise signed center: preserves F0 and augmentation cross entries.
  cl=ch=F(0)
  for i in range(2):
   for k in range(2):
    w=(y[k] if i==0 else 0)+(y[i] if k==0 else 0)-y[i]*y[k]
    a,b=F0[i][k];cl+=min(w*a,w*b);ch+=max(w*a,w*b)
    w=-lam*y[i]*y[k];a,b=Gy[i][k];cl+=min(w*a,w*b);ch+=max(w*a,w*b)
  return dict(trial_coefficients=list(map(str,y)),actual_residual_D_Gram_lower=str(rl),actual_residual_D_Gram_upper=str(rh),shared_fault_D_norm_upper=str(up(fault)),original_action_inverse_response_lower=str(down(cl+rl/nu)),original_action_inverse_response_upper=str(up(ch+rh/mu)),coupled_signed_gap_lower=str(gaplo),coupled_signed_gap_upper=str(gaphi))
 trials=[trial(y) for y in sorted(choices)];lower=max(trials,key=lambda r:F(r['original_action_inverse_response_lower']));upper=min(trials,key=lambda r:F(r['original_action_inverse_response_upper']))
 tl=max(F(prior['actual_original_action_inverse_response_lower']),F(lower['original_action_inverse_response_lower']));th=min(F(prior['actual_original_action_inverse_response_upper']),F(upper['original_action_inverse_response_upper']))
 dl=max(F(prior['actual_signed_response_gap_lower']),max(F(r['coupled_signed_gap_lower']) for r in trials),down(F0[0][0][0]-th));dh=min(F(prior['actual_signed_response_gap_upper']),min(F(r['coupled_signed_gap_upper']) for r in trials),up(F0[0][0][1]-tl));assert tl<=th and dl<=dh
 return dict(source='N0 P'+str(base),response_trial_basis=['P'+str(base),'P'+str(base+2)],nominal_least_residual_proposal=list(map(str,least)),nominal_Galerkin_proposal=list(map(str,gal)),candidate_count=len(trials),selected_inverse_lower_trial=lower,selected_inverse_upper_trial=upper,actual_original_action_inverse_response_lower=str(tl),actual_original_action_inverse_response_upper=str(th),previous_original_action_inverse_response_upper=prior['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(dl),actual_signed_gap_upper=str(dh),previous_signed_gap_lower=prior['actual_signed_response_gap_lower'],original_action_inverse_upper_improved=th<F(prior['actual_original_action_inverse_response_upper']),signed_gap_lower_improved=dl>F(prior['actual_signed_response_gap_lower']),signed_gap_positive_certified=dl>0,actual_negative_gap_proved=dh<0)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(raw) if path.endswith('.json') else raw.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('236_full_range_signed_response');old=get('231_original_polynomial_action');aug=get('234_materialized_band_action');bounds=get('232_augmented_polynomial_action');kernel=get('115_rational_fourier_adjoint');metric=get('129_four_vector_joint_moment')
 assert prior['full_parameter_dimension']==639 and prior['full_frequency_range_exhausted_by_physical_parameterization']
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);reg=list(map(F,get('46_native_archimedean_head')['regular_kernel_coefficients']));eps=F(get('46_native_archimedean_head')['regular_kernel_uniform_error_upper']);prime=get('43_native_prime_head')
 for j in [0,1]:assert regular_poly(j,reg[:12])==orig.regular_source(j,reg[:12])
 aa,bb=material.spherical_polynomials();pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper']);parities=[]
 for base in [0,1]:
  d=base+2;pr=bounds['polynomial_augmented_action_certificates'][base];lam=F(pr['augmentation_coefficient']);U=F(pr['rational_frequency_half_bandwidth']);epsilon=F(pr['physical_Fhat_star_Fhat_to_J_star_J_operator_norm_upper'])
  new=new_original_action(d,reg,prime,eps,sl,sh,reverse);print('RC237 original action P'+str(d)+' complete',flush=True)
  gram,controls=extended_band_coefficients(U,d,pi0,pierr,aa,bb,reverse);ac,AE,abudget=augmentation(d,gram,lam,epsilon,sl,sh)
  full=[dict(degree=x['degree'],coefficient=str(F(x['coefficient'])+F(y['coefficient'])),radius=str(up(F(x['radius'])+F(y['radius'])))) for x,y in zip(new['finite_original_D_action'],ac)]
  E=up((root(F(new['complete_original_action_D_error_squared_upper']))+root(AE))**2)
  columns=[dict(original=old['polynomial_original_action_certificates'][base],finite_complete_augmented_D_action=aug['parity_materialized_augmented_action_certificates'][base]['finite_complete_augmented_D_action'],augmentation_action_D_error_squared_upper=aug['parity_materialized_augmented_action_certificates'][base]['actual_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=aug['parity_materialized_augmented_action_certificates'][base]['complete_augmented_action_D_error_squared_upper']),dict(original=new,finite_complete_augmented_D_action=full,augmentation_action_D_error_squared_upper=str(AE),complete_augmented_action_D_error_squared_upper=str(E))]
  degrees=[base,d];F0=[[(F(0),F(0))]*2 for _ in range(2)];Gy=[[(F(0),F(0))]*2 for _ in range(2)]
  bandcols=[[(F(r['lower']),F(r['upper'])) for r in aug['parity_materialized_augmented_action_certificates'][base]['actual_band_Gram_column']],gram]
  for i in range(2):
   for k in range(i,2):
    a=original_entry(degrees[i],columns[k]['original'],sl,sh);b=original_entry(degrees[k],columns[i]['original'],sl,sh);v=(max(a[0],b[0]),min(a[1],b[1]));assert v[0]<=v[1];F0[i][k]=F0[k][i]=v
    a=bandcols[k][degrees[i]];b=bandcols[i][degrees[k]];lo=max(a[0],b[0]);hi=min(a[1],b[1]);assert lo<=hi
    fault=up(epsilon*root(orig.mass(degrees[i])*orig.mass(degrees[k])));v=(down(lo-fault),up(hi+fault));Gy[i][k]=Gy[k][i]=v
  FL,FH=loewner(F0);YL,YH=loewner(Gy);GL=p.add(FL,p.scale(lam,YL));GH=p.add(FH,p.scale(lam,YH));assert p.psd(YL) and p.inv(YL) and p.psd(GL) and p.inv(GL)
  result=response(base,columns,F0,Gy,lam,F(pr['fresh_augmented_N_D_lower']),F(pr['fresh_augmented_N_D_upper']),sl,sh,prior['two_source_original_action_inverse_response_certificates'][base],reverse)
  errors=[[str(2*F(columns[0]['complete_augmented_action_D_error_squared_upper'])),'0'],['0',str(2*E)]]
  parities.append(dict(parity='even' if base==0 else 'odd',response_trial_basis=['P'+str(n) for n in degrees],new_complete_original_action=new,new_band_Gram_column=[dict(degree=n,lower=str(a),upper=str(b)) for n,(a,b) in enumerate(gram)],new_band_controls=controls,new_augmentation_action_budget=abudget,new_augmentation_action_D_error_squared_upper=str(AE),new_complete_augmented_D_action=full,new_complete_augmented_D_action_D_error_squared_upper=str(E),original_trial_form_intervals=[[[str(a),str(b)] for a,b in row] for row in F0],frequency_trial_Gram_intervals=[[[str(a),str(b)] for a,b in row] for row in Gy],original_trial_form_Loewner_lower=p.ser(FL),original_trial_form_Loewner_upper=p.ser(FH),actual_frequency_trial_Gram_Loewner_lower=p.ser(YL),actual_frequency_trial_Gram_Loewner_upper=p.ser(YH),actual_augmented_trial_form_Loewner_lower=p.ser(GL),actual_augmented_trial_form_Loewner_upper=p.ser(GH),complete_two_trial_action_error_D_Gram_upper=errors,source_inverse_response=result))
 return dict(milestone='RC237',starting_commit='6100c1496dd1e90c6070ae58f1602c5424dd0027',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_new_original_and_augmented_action_inputs=['P2','P3'],actual_total_action_input_count=4,actual_response_source_count=2,actual_response_source_order=['N0 P0','N0 P1'],response_trials_per_parity=2,parity_two_trial_signed_response_certificates=parities,all_same_parity_cross_terms_paid=True,same_parity_action_errors_assumed_orthogonal=False,shared_source_original_action_error_coupled=True,actual_complete_prime_pairs=7,both_signed_poles_retained=True,new_response_enclosures_intersected_with_RC236=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,two_test_signed_gap_positive_certified=all(r['source_inverse_response']['signed_gap_positive_certified'] for r in parities),actual_negative_original_direction_proved=any(r['source_inverse_response']['actual_negative_gap_proved'] for r in parities),original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC238: use the validated coupled action/form interface for residual-shaped richer trials or stronger complementary inverse bounds; retain full 639-dimensional signed-gap coverage as the completion requirement')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();c=run(args.replay)
 if args.replay:assert c==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC237 VALIDATED: complete new actions and coupled two-trial signed responses; full gap open',flush=True)
