"""Independent closed moment allowances, refined guards and Bernoulli controls."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from certify_native_legendre_small_window import I,bernoulli,sqrt_rational
from certify_native_exact_logarithm import log_rational
saved=I.grid;I.grid=10**180
try:
 raw=Path('notes/data/RPB108_PRIME8_TRUNCATION_105_PREFLIGHT_20261008.json').read_bytes();c=json.loads(raw)
 a=F(21,20);d=2*a;k=112
 assert c['aperture']==str(a) and c['exponential_guard']==67
 assert log_rational(F(66),500).hi<4*a<log_rational(F(67),500).lo
 assert log_rational(F(8),500).hi<d<log_rational(F(9),500).lo
 assert (1+d+d*d/3)/2==F(457,200)<F(23,10)
 checks=0
 for key,entry in c['source_analytic_allowances'].items():
  N,K=map(int,key.split('/'));ce=F(23,10)*(d/2)**(N+1)/factorial(N+1)
  cb=4*(d/3)**(2*K+2)/(1-(d/3)**2);ep=2*(d/4)**(N+1)/factorial(N+1)
  H=2*(ce/(N+1)+cb/(2*K+2))+10*d*ep;A=2*(ce/(N+2)+cb/(2*K+3))
  squared=k*k*H*H+k*k*(k*k-1)*H*A+F(k*k*(k*k-1)**2,3)*A*A
  assert squared==F(entry['squared_analytic_map_allowance'])<=F(entry['upper'])**2;checks+=1
 assert F(c['source_analytic_allowances']['90/114']['upper'])>F(1,10**35)
 assert F(c['source_analytic_allowances']['100/130']['upper'])<F(1,10**35)
 # Separate Akiyama recurrence, all source/native constants (through 802).
 base=bernoulli(842);A=[]
 for m in range(843):
  A.append(F(1,m+1))
  for j in range(m,0,-1):A[j-1]=j*(A[j-1]-A[j])
  assert (-A[0] if m==1 else A[0])==base[m]
 coeff=[abs(base[2*j]*(2*d)**(2*j)/factorial(2*j)) for j in range(1,131)]
 assert all(y<x for x,y in zip(coeff,coeff[1:]))
 assert all((base[2*j]>0)==(j%2==1) for j in range(1,422))
 rawg=Path('notes/data/RPB108_PRIME8_GARDING_105_CERTIFICATE_20261008.json').read_bytes();g=json.loads(rawg)
 p=json.loads(Path('notes/data/RPB108_PRIME8_WEIGHTED_DEPTH10_105_CERTIFICATE_20261008.json').read_bytes())
 logs={n:log_rational(F(n),500) for n in [2,3,5,7,8,9]}
 amps=[logs[2]/sqrt_rational(F(2)),logs[3]/sqrt_rational(F(3)),logs[2]/2,logs[5]/sqrt_rational(F(5)),logs[7]/sqrt_rational(F(7)),logs[2]/sqrt_rational(F(8))]
 assert len(p['amplitude_upper'])==6 and all(x.hi<=F(y) for x,y in zip(amps,p['amplitude_upper']))
 assert 2*sum(map(F,p['amplitude_upper']),F(0))==F(g['crude_prime_loss_upper'])<7
 assert a<logs[3].lo and 4*a*3<13 and g['garding_constant']==6+7+13==26
 out={'aperture':str(a),'truncation_sha256':hashlib.sha256(raw).hexdigest(),'closed_weighted_moment_sums_checked':checks,
 'independent_akiyama_bernoulli_checks':843,'source_alternating_pairs_checked':130,'native_even_signs_checked':421,
 'independent_prime_amplitude_inclusions':6,'garding26_verified':True,'exponential67_guard_verified':True,
 'source_kernel_ceiling_guard_verified':True,'actual_source_error_complete':False,'whole_domain_positivity':False}
 print(json.dumps(out,indent=2))
finally:I.grid=saved
