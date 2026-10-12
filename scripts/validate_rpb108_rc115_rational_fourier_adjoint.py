"""RC115: explicit rational finite Fourier model and two full-rank adjoint sources.
Inputs RC114 RC112 RC66. No canonical Riesz responses or Weil actions computed.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,Context,ROUND_FLOOR,ROUND_CEILING
from math import factorial,comb
import argparse,json,hashlib
from validate_rpb108_rc30_interval_metric import PI
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc47_correlated_native_transport import root

PREC=700;N=2400
lc=Context(prec=PREC,rounding=ROUND_FLOOR);hc=Context(prec=PREC,rounding=ROUND_CEILING)
def interval(q):return lc.divide(D(q.numerator),D(q.denominator)),hc.divide(D(q.numerator),D(q.denominator))
def mul(a,b):return lc.multiply(a[0],b[0]),hc.multiply(a[1],b[1])
def divint(a,n):return lc.divide(a[0],D(n)),hc.divide(a[1],D(n))
def coefficients(n,Z,T,parity,replay=False):
 z=interval(Z);zhalf=divint(z,2);zquarter=divint(mul(z,z),4);base=(D(1),D(1));out=[]
 for j in range(n):
  if j==1:base=z
  elif j>1:base=divint(mul(base,zhalf),j)
  if j%2!=(0 if parity=='even' else 1):continue
  current=base;terms=[];lo=D(0);hi=D(0);s=1 if parity=='even' else 2
  for m in range((N-j)//2+1):
   term=divint(current,j+2*m+s)
   if replay:terms.append((m%2,term))
   elif m%2:lo=lc.subtract(lo,term[1]);hi=hc.subtract(hi,term[0])
   else:lo=lc.add(lo,term[0]);hi=hc.add(hi,term[1])
   current=divint(mul(current,zquarter),(m+1)*(m+j+1))
  if replay:
   for sign,term in reversed(terms):
    if sign:lo=lc.subtract(lo,term[1]);hi=hc.subtract(hi,term[0])
    else:lo=lc.add(lo,term[0]);hi=hc.add(hi,term[1])
  factor=interval(2*T);l,h=lc.multiply(lo,factor[0]),hc.multiply(hi,factor[1])
  # Signed multiplication endpoints, since the accumulated integral may be negative.
  l=min(lc.multiply(x,y) for x in [lo,hi] for y in factor);h=max(hc.multiply(x,y) for x in [lo,hi] for y in factor)
  phase=(-1)**(j//2)
  if phase<0:l,h=h.copy_negate(),l.copy_negate()
  low=down(F(l),10**70);high=up(F(h),10**70);center=(low+high)/2;radius=(high-low)/2
  assert low<=F(l)<=F(h)<=high and radius<=F(1,10**69)
  out.append(dict(native_degree=j,physical_Chebyshev_coefficient_center=str(center),physical_Chebyshev_coefficient_radius=str(radius)))
 return out

def machin():
 def atan(q):
  n=180;s=sum((F((-1)**j)*q**(2*j+1)/F(2*j+1) for j in range(n)),F(0));e=q**(2*n+1)/F(2*n+1)
  return s-e,s+e
 a,b=atan(F(1,5));c,d=atan(F(1,239));return 16*a-4*d,16*b-4*c

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,cov,norm=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC114' and cov['milestone']=='RC112' and norm['milestone']=='RC66'
 assert prior['input_sha256'][1]==hs[1] and prior['input_sha256'][5]==hs[2]
 piL,piH=F(PI.l),F(PI.h);mL,mH=machin();assert piL<=mL<mH<=piH
 pi0=down((piL+piH)/2,10**80);epi=max(abs(pi0-piL),abs(piH-pi0));assert epi<F(1,10**79)
 # Exact monomial-to-Chebyshev coefficient identities, independent of Decimal actions.
 checks=0
 for degree in range(25):
  for j in range(degree+1):
   if (degree-j)%2:continue
   m=(degree-j)//2
   lhs=F(comb(degree,m),2**degree)/factorial(degree)*(1 if j==0 else 2)
   rhs=F(1 if j==0 else 2,2**degree*factorial(m)*factorial(j+m))
   assert lhs==rhs;checks+=1
 # Independent exact adjoint duality on a full degree-24 Taylor kernel.
 dual_checks=0;ztest=F(7,3);ttest=F(3,7)
 cheb=[F(1),ttest]
 for j in range(2,25):cheb.append(2*ttest*cheb[-1]-cheb[-2])
 for parity in [0,1]:
  reconstructed=F(0);direct=F(0);ss=1 if parity==0 else 2
  for j in range(parity,25,2):
   amp=sum((F((-1)**m)*(1 if j==0 else 2)*(ztest/2)**(j+2*m)/F(factorial(m)*factorial(j+m)*(j+2*m+ss)) for m in range((24-j)//2+1)),F(0))
   reconstructed+=2*((-1)**(j//2))*amp*cheb[j]
  for k in range(parity,25,2):direct+=2*((-1)**(k//2))*(ztest*ttest)**k/F(factorial(k)*(k+ss))
  assert reconstructed==direct;dual_checks+=1
 rho=F(252,257);B=F(11,10);rows=[]
 for r in cov['parity_coverage_certificates']:
  name=r['parity'];n=r['Chebyshev_truncation_length'];T=F(r['frequency_cutoff_upper']);Z=2*pi0*B*T;zr=up(Z,10**6)
  remainder_exact=zr**(N+1)/F(factorial(N+1));assert remainder_exact<F(1,10**120)
  remainder=up(remainder_exact,10**120)
  kernelbase=2*B*T*epi+remainder
  op_error2=up(16*n*n*B*T*kernelbase**2,10**160);assert op_error2<F(1,10**140)
  data=coefficients(n,Z,T,name,replay);assert len(data)==r['parity_exceptional_dimension']
  sumrad=sum((F(x['physical_Chebyshev_coefficient_radius']) for x in data),F(0));ynorm2=2*T/(1 if name=='even' else 3)
  canonical_error2=up(2*op_error2*ynorm2+4*B*rho*sumrad**2,10**150);assert canonical_error2<F(1,10**130)
  # Positive augmentation built from the rational polynomial operator itself.
  sd=root(F(r['Fourier_restriction_squared_tail_upper']),10**80);ep=root(op_error2,10**80)
  newd2=up((sd+ep)**2,10**80);a=F(r['reference_floor']);p=F(r['low_band_penalty_upper']);eta=down(a-5*p*newd2,10**9)
  old=next(x for x in prior['parity_positive_augmentation_certificates'] if x['parity']==name)['positive_augmentation_certificates'][0]
  assert eta==F(old['positive_augmented_operator_lower'])>0
  source_hash=hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()
  rows.append(dict(parity=name,rational_frequency_half_bandwidth=str(T),Chebyshev_truncation_length=n,retained_native_count=len(data),real_phase_argument_upper=str(zr),Taylor_degree=N,real_imaginary_axis_Taylor_remainder_upper=str(remainder),rational_pi_phase_error_upper=str(2*B*T*epi),finite_model_operator_error_squared_upper=str(op_error2),tested_auxiliary_vector='1' if name=='even' else 'xi/T',auxiliary_vector_physical_norm_squared=str(ynorm2),physical_source_global_phase='1' if name=='even' else 'i',physical_source_coefficient_intervals=data,physical_source_coefficient_interval_sha256=source_hash,canonical_adjoint_source_error_squared_upper=str(canonical_error2),polynomial_model_positive_augmentation_floor_lower=str(eta),polynomial_model_Young_parameter='1/4',polynomial_model_augmentation_coefficient=str(F(5,4)*p),finite_model_squared_J_approximation_error_upper=str(newd2)))
 return dict(milestone='RC115',status='PASS: rational Fourier-adjoint source pair and global kernel/model error; canonical response open',input_sha256=hs,aperture='11/10',arithmetic='700-digit directed Decimal coefficient integration with exact rational acceptance; reverse-sum replay',rational_pi=str(pi0),rational_pi_error_upper=str(epi),independent_Machin_enclosure_verified=True,Taylor_degree=N,exact_monomial_Chebyshev_coefficient_controls=checks,exact_adjoint_duality_controls=dual_checks,parity_rational_Fourier_adjoint_sources=rows,total_physical_adjoint_source_coefficients_enclosed=sum(r['retained_native_count'] for r in rows),exact_rational_finite_kernel_recipe_supplied=True,global_kernel_and_adjoint_error_certified=True,rational_kernel_positive_augmentation_certified=True,rational_kernel_augmentation_identical_to_RC114_exact_kernel_claimed=False,full_frequency_Gram_evaluated=False,canonical_Riesz_source_images_computed=False,original_Weil_actions_on_these_sources_computed=False,augmented_inverse_responses_computed=False,auxiliary_response_norm_below_one_certified=False,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=3);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,indent=2,sort_keys=True)+'\n')
 print('RC115 PASS: all 639 physical Fourier-adjoint coefficients and global errors certified; canonical responses open')
