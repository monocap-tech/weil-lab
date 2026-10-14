"""RC242: full original Weil actions on RC241's residual-shaped polynomials."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
import argparse,hashlib,json
import validate_rpb108_rc241_three_trial_tuning_obstruction as parent
orig=parent.orig;p=parent.p;B=parent.B;up=parent.up;down=parent.down;root=parent.root
ROOT=Path(__file__).resolve().parents[1];OUT=128;END=256
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc241_three_trial_tuning_obstruction.json':'01e4fb43f72782488712e2718a06ed71460853c6','notes/RPB108_RC241_THREE_TRIAL_TUNING_OBSTRUCTION_20261014.md':'1a7a41215678f6ba1b9ca3f570500f85569f1e52'})
HELPER_PINS['scripts/validate_rpb108_rc241_three_trial_tuning_obstruction.py']='d539efd9e1f4e5a9533aed2b64706229deb66cf3'
def addpoly(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 return c
def input_poly(a):
 q=[F(0)]*len(a)
 for n,c in enumerate(a):
  for k,v in enumerate(orig.legendre(n)):q[k]+=c*v
 return q
def segment_digest(segments):
 h=hashlib.sha256()
 for l,r,v in segments:
  for x in [l,r]+v:
   h.update(b'-' if x<0 else b'+')
   for integer in [abs(x.numerator),x.denominator]:
    b=integer.to_bytes(max(1,(integer.bit_length()+7)//8),'big');h.update(len(b).to_bytes(8,'big'));h.update(b)
 return h.hexdigest()
def regular(q,parity,reg):
 v=[sum((q[k]*comb(k,m)*2**m*(-1)**(k-m) for k in range(m,len(q))),F(0)) for m in range(len(q))]
 left=[F(0)]*(len(reg)+len(q))
 for k,c in enumerate(reg):
  for m,b in enumerate(v):
   if b:left[k+m+1]+=2*B*c*(2*B)**k*b*F(factorial(k)*factorial(m),factorial(k+m+1))
 result=[sum((left[k]*comb(k,l)/2**k for k in range(l,len(left))),F(0))*(1+(-1)**(parity+l)) for l in range(len(left))]
 assert all(v==0 for n,v in enumerate(result) if n%2!=parity)
 return result
def prime_action(q,a,parity,prime,reverse):
 A=sum(map(abs,a),F(0));der=sum((abs(c)*n*(n+1)/2 for n,c in enumerate(a)),F(0))/B
 mass=sum((orig.mass(n)*c*c for n,c in enumerate(a)),F(0));fault=F(0);terms=[];parameters=[];grid=10**16
 for row in prime['active_prime_powers']:
  el,eh=F(row['translation_lower']),F(row['translation_upper']);cl,ch=F(row['coefficient_lower']),F(row['coefficient_upper']);em=(el+eh)/2;cm=(cl+ch)/2
  ell=F(em.numerator*grid//em.denominator,grid);c=F(cm.numerator*grid//cm.denominator,grid);de=max(abs(el-ell),abs(eh-ell));dc=max(abs(cl-c),abs(ch-c));assert 0<ell<2*B and c>0
  parameters.append(dict(n=row['n'],chosen_translation=str(ell),chosen_coefficient=str(c),actual_translation_distance_upper=str(up(de)),actual_coefficient_distance_upper=str(up(dc))))
  fault+=2*(dc*root(mass)+ch*root(2*de*A*A+2*B*de*de*der*der))
  for sign in [-1,1]:
   off=sign*ell/B;l=max(F(-1),-1-off);r=min(F(1),1-off)
   v=[-c*sum((q[k]*comb(k,m)*off**(k-m) for k in range(m,len(q))),F(0)) for m in range(len(q))];terms.append((l,r,v))
 knots=sorted({F(-1),F(1)}|{x for l,r,_ in terms for x in [l,r]});segments=[]
 for l,r in zip(knots,knots[1:]):
  mid=(l+r)/2;v=[sum((w[k] for ll,rr,w in terms if ll<mid<rr),F(0)) for k in range(len(q))];segments.append((l,r,v))
 assert len(terms)==14 and len(segments)==15
 for l,r,v in segments:
  reflected=next(w for ll,rr,w in segments if ll==-r and rr==-l);assert reflected==[(-1)**(parity+k)*x for k,x in enumerate(v)]
 norm=B*sum((orig.integral(orig.product(v,v),l,r) for l,r,v in segments),F(0));coeff=[]
 # Cache exact segment monomial integrals once; then project their moment
 # vectors against P_n. This is the same polynomial integral, avoiding
 # repeated high powers and convolution for every output degree.
 segment_moments=[]
 for l,r,v in segments:
  if r<=0:continue
  multiplicity=1 if l<0 else 2
  powers_l=[F(1)];powers_r=[F(1)]
  for k in range(len(v)+OUT):powers_l.append(powers_l[-1]*l);powers_r.append(powers_r[-1]*r)
  integrals=[(powers_r[k+1]-powers_l[k+1])/F(k+1) for k in range(len(v)+OUT)]
  segment_moments.append([multiplicity*sum((c*integrals[j+k] for j,c in enumerate(v) if c),F(0)) if k%2==parity else F(0) for k in range(OUT+1)])
 if reverse:segment_moments.reverse()
 combined_moments=[sum((m[k] for m in segment_moments),F(0)) for k in range(OUT+1)]
 for n in range(OUT+1):
  if n%2!=parity:coeff.append(F(0));continue
  pn=orig.legendre(n);value=sum((c*combined_moments[k] for k,c in enumerate(pn) if c),F(0))
  if n<8:assert value==sum((orig.integral(orig.product(v,pn),l,r) for l,r,v in segments),F(0))
  coeff.append(F(2*n+1,2)*value)
 tail=norm-sum((orig.mass(n)*c*c for n,c in enumerate(coeff)),F(0));assert tail>=0
 for l,r,v in segments:
  affine=[sum((v[k]*comb(k,m)*l**(k-m) for k in range(m,len(v))),F(0))*(r-l)**m for m in range(len(v))]
  assert orig.integral(orig.product(v,v),l,r)==(r-l)*sum((c/F(k+1) for k,c in enumerate(orig.product(affine,affine))),F(0))
 return coeff,up(tail),up(fault),dict(input_physical_sup_abs_upper=str(A),input_physical_derivative_abs_upper=str(der),full_prime_output_physical_energy_lower=str(down(norm)),full_prime_output_physical_energy_upper=str(up(norm)),prime_segment_polynomial_sha256=segment_digest(segments),segment_digest_encoding='sign byte; numerator and denominator big-endian bytes with unsigned 8-byte lengths; segment endpoints then polynomial coefficients',model_prime_parameter_grid='1/10^16',chosen_prime_model_parameters=parameters,extra_prime_parameter_rounding_paid=True,complete_prime_pairs=7,support_segment_count=15,all_cross_prime_terms_paid=True,affine_segment_norm_replay=True,segment_monomial_projection_low_degree_replay=True)
def endpoint(a,n,loglo,loghi):
 center=F(0);rad=F(0)
 for d,c in enumerate(a):
  if not c or (n-d)%2:continue
  if n==d:
   h=2*orig.H(2*n)-2*orig.H(n)+F(1,2*n+1)-(loglo+loghi)/2;rad+=abs(c)*(loghi-loglo)/2
  else:h=F(2*n+1,abs(n-d)*(n+d+1))
  center+=c*h
 return center,rad
def endpoint_tail(a,parity,sl,loglo,loghi,reverse):
 terms=[]
 for n in range(OUT+1,END+1):
  if n%2!=parity:continue
  v,rad=endpoint(a,n,loglo,loghi);assert rad==0;terms.append(up(orig.mass(n)*v*v/(orig.H(n)+sl)))
 if reverse:terms.reverse()
 first=END+1 if (END+1)%2==parity else END+2
 remaining=up(sum((abs(c)*root(3*B/((orig.H(first)+sl)*(END-d)**2)) for d,c in enumerate(a) if c),F(0))**2)
 return up(sum(terms,F(0))+remaining),dict(explicit_tail_sum_through_degree=END,combined_endpoint_tail_D_energy_through_256_upper=str(up(sum(terms,F(0)))),beyond_256_endpoint_D_energy_upper=str(remaining),endpoint_input_cross_terms_retained_through_256=True)
def controls():
 # Laplace's polynomial identity: the complex integrand's modulus is <=1
 # for t in [-1,1], so this identity proves |P_n(t)|<=1.
 # Independently verify the polynomial and positive derivative expansion
 # for every degree occurring in either residual-shaped input.
 for n in range(65):
  q=[F(0)]*(n+1)
  for k in range(n//2+1):
   factor=F(comb(n,2*k)*(-1)**k*comb(2*k,k),4**k)
   for j in range(k+1):q[n-2*k+2*j]+=factor*comb(k,j)*(-1)**j
  assert q==orig.legendre(n)
  derivative=[(k+1)*v for k,v in enumerate(orig.legendre(n)[1:])];rhs=[F(0)]*n
  for k in range(n):
   if (n-k)%2:
    for j,v in enumerate(orig.legendre(k)):rhs[j]+=(2*k+1)*v
  assert derivative==rhs and sum((2*k+1 for k in range(n) if (n-k)%2),0)==n*(n+1)//2
 for n in range(6):
  q=orig.legendre(n);reg=[F(1,2),-F(1,3),F(1,7)]
  assert regular(q,n%2,reg)==parent.parent.trial.regular_poly(n,reg)+[F(0)]*(len(q)+len(reg)-len(parent.parent.trial.regular_poly(n,reg)))
 return dict(Laplace_polynomial_identity_checked_through_degree=64,positive_Legendre_derivative_expansion_checked_through_degree=64,generic_regular_convolution_low_degree_controls=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin');data[path]=json.loads(raw) if path.endswith('.json') else raw.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('241_three_trial_tuning_obstruction');metric=get('129_four_vector_joint_moment');reg=list(map(F,get('46_native_archimedean_head')['regular_kernel_coefficients']));eps=F(get('46_native_archimedean_head')['regular_kernel_uniform_error_upper']);prime=get('43_native_prime_head')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B)
 ll=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0));lh=ll+2*F(1,3)**201/(201*(1-F(1,9)));rows=[]
 for parity,r in enumerate(prior['parity_tuning_obstruction_certificates']):
  a=list(map(lambda x:F(x['coefficient']),r['residual_shaped_next_trial_proposal']));assert len(a)==65 and all(c==0 for n,c in enumerate(a) if n%2!=parity);q=input_poly(a)
  mass=sum((orig.mass(n)*c*c for n,c in enumerate(a)),F(0));energylo=sum((orig.mass(n)*(orig.H(n)+sl)*c*c for n,c in enumerate(a)),F(0));energyhi=sum((orig.mass(n)*(orig.H(n)+sh)*c*c for n,c in enumerate(a)),F(0));assert mass==B*orig.integral(orig.product(q,q)) and energylo>0
  regpoly=regular(q,parity,reg);rc=[orig.project(regpoly,n) for n in range(len(regpoly))]
  for n in range(8):assert rc[n]==F(2*n+1,2)*orig.integral(orig.product(regpoly,orig.legendre(n)))
  rtail=up(sum((orig.mass(n)*c*c for n,c in enumerate(rc) if n>OUT),F(0)));print('RC242 regular residual action '+r['parity']+' complete',flush=True)
  pc,ptail,pfault,pcontrol=prime_action(q,a,parity,prime,reverse);print('RC242 prime residual action '+r['parity']+' complete',flush=True)
  phi=[F(11,20)**k/factorial(k) if k%2==parity else F(0) for k in range(41)];moment=B*orig.integral(orig.product(q,phi));pole=[2*(-1)**parity*moment*v for v in phi];oc=[orig.project(pole,n) for n in range(OUT+1)];tau=2*F(11,20)**41/factorial(41);polefault=up(16*B*tau*root(mass))
  coeff=[];rounding=F(0)
  for n in range(OUT+1):
   if n%2!=parity:coeff.append(dict(degree=n,coefficient='0',radius='0'));continue
   h,hr=endpoint(a,n,ll,lh);identity=a[n] if n<len(a) else F(0);v=h-rc[n]+pc[n]+oc[n]-F(789,125)*identity
   values=[x/(orig.H(n)+s)+identity for x in [v-hr,v+hr] for s in [sl,sh]];lo=min(values);hi=max(values);center=down((lo+hi)/2);rad=max(center-lo,hi-center);rounding+=orig.mass(n)*(orig.H(n)+sh)*rad*rad;coeff.append(dict(degree=n,coefficient=str(center),radius=str(up(rad))))
  first=OUT+1 if (OUT+1)%2==parity else OUT+2;etail,econtrol=endpoint_tail(a,parity,sl,ll,lh,reverse)
  components=dict(finite_rounding=up(rounding),endpoint_omitted_output=etail,regular_omitted_output=up(rtail/(orig.H(first)+sl)),prime_omitted_output=up(ptail/(orig.H(first)+sl)),regular_kernel=up((2*B*eps)**2*mass/sl),prime_arithmetic=up(pfault*pfault/sl),pole_Taylor=up(polefault*polefault/sl));E=up(sum((root(v) for v in components.values()),F(0))**2)
  # Sharp source pairing: projection tails are orthogonal to the exact input.
  form=F(0);frad=F(0)
  for n,c in enumerate(a):
   v=F(coeff[n]['coefficient']);rad=F(coeff[n]['radius']);wlo=orig.mass(n)*(orig.H(n)+sl);whi=orig.mass(n)*(orig.H(n)+sh);values=[c*x*w for x in [v-rad,v+rad] for w in [wlo,whi]];form+=(min(values)+max(values))/2;frad+=(max(values)-min(values))/2
  frad+=root(energyhi)*sum((root(components[k]) for k in ['regular_kernel','prime_arithmetic','pole_Taylor']),F(0))
  centerlo=sum((orig.mass(n)*(orig.H(n)+sl)*F(x['coefficient'])**2 for n,x in enumerate(coeff)),F(0));centerhi=sum((orig.mass(n)*(orig.H(n)+sh)*F(x['coefficient'])**2 for n,x in enumerate(coeff)),F(0))
  rows.append(dict(parity=r['parity'],input='R'+str(parity),exact_input_Legendre_coefficients=list(map(str,a)),input_physical_energy=str(mass),input_D_energy_lower=str(energylo),input_D_energy_upper=str(energyhi),finite_complete_original_D_action=coeff,D_energy_component_squared_errors={k:str(v) for k,v in components.items()},complete_original_action_D_error_squared_upper=str(E),relative_original_action_D_error_squared_upper=str(up(E/energylo)),original_test_form_lower=str(down(form-frad)),original_test_form_upper=str(up(form+frad)),complete_original_output_D_energy_lower=str(down(max(F(0),parent.rootdown(centerlo)-root(E))**2)),complete_original_output_D_energy_upper=str(up((root(centerhi)+root(E))**2)),prime_controls=pcontrol,endpoint_tail_controls=econtrol,regular_output_polynomial_degree=max(n for n,v in enumerate(regpoly) if v),regular_polynomial_tail_physical_energy_upper=str(rtail),prime_projection_tail_physical_energy_upper=str(ptail),signed_pole_sign=(-1)**parity,original_action_not_augmented_action=True))
 return dict(milestone='RC242',starting_commit='7ab2888f9c9e7fd76468ccb66d3387c24d641b69',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,new_complete_original_action_inputs=['R0','R1'],actual_total_original_action_input_count=8,new_complete_augmented_action_inputs=[],actual_response_source_count=2,residual_proposal_input_rounding_not_added_as_action_uncertainty=True,source_polynomials_are_exact_rational_inputs=True,retained_original_action_degree=OUT,all_prime_pairs_and_cross_terms_paid=True,both_signed_poles_retained=True,parity_residual_original_action_certificates=rows,opposite_parity_action_error_pairing_zero=True,two_input_original_action_error_D_Gram_upper=[[rows[0]['complete_original_action_D_error_squared_upper'],'0'],['0',rows[1]['complete_original_action_D_error_squared_upper']]],exact_controls=controls(),residual_trials_augmented_actions_certified=False,new_augmented_inverse_response_evaluated=False,previous_response_bounds_preserved=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC243: certify the actual rational augmentation actions on R0/R1, then evaluate the enriched residual-shaped trial response; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC242 VALIDATED: full original residual-shaped actions; augmentation and full signed gate open',flush=True)
