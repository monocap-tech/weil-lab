"""Exact aperture-dependent architecture controls; no global positivity claim."""
import json
from fractions import Fraction as F
from math import factorial,prod
from pathlib import Path
from certify_native_legendre_small_window import I,atan,sqrt_rational
from certify_native_exact_logarithm import log_rational
from certify_native_larger_aperture_complement import integrated_mass
I.grid=10**120
pi=16*atan(F(1,5),200)-4*atan(F(1,239),200)
a=F(21,20);k=112
Tcap=sqrt_rational(F(k*(k+1))).hi/(2*a*pi.lo)
B=F(json.loads(Path('notes/data/RPB108_PRIME8_WEIGHTED_DEPTH10_105_CERTIFICATE_20261008.json').read_text())['joint_prime_operator_norm_upper'])
ceiling=log_rational(Tcap,400).hi-B
checks=0
for kk in [1,2,10,40,112,200,500]:
 for aa in [F(1,2),F(21,20),F(3,2),F(10)]:
  T=F(kk,10)/aa
  rho=integrated_mass(aa,kk,T)
  coarse=F(245,552)*kk*F(33,35)**(2*kk)
  assert rho<=coarse
  assert prod(range(1,2*kk+2,2))>=2**kk*factorial(kk)
  checks+=2
# Generic support geometry and constant-vector norm lower at two arithmetic regimes.
rayleigh={}
for aa,powers in [(F(1),[2,3,4,5,7]),(a,[2,3,4,5,7,8])]:
 logs={n:log_rational(F(n),400) for n in powers}
 lambdas={2:logs[2],3:logs[3],4:logs[2],5:logs[5],7:logs[7]}
 if 8 in powers:lambdas[8]=logs[2]
 low=2*sum((lambdas[n].lo/sqrt_rational(F(n)).hi*(1-logs[n].hi/(2*aa)) for n in powers),F(0))
 assert low>0
 rayleigh[str(aa)]={'prime_operator_norm_lower':str(low),'display':float(low)}
checks+=2
out={'scope':'finite exact controls for analytic aperture-dependent criterion and method obstructions',
 'aperture':str(a),'retained_vectors':k,'positive_bessel_cutoff_strict_upper':str(Tcap),
 'three_band_complement_method_ceiling_upper':str(ceiling),'ceiling_display':float(ceiling),
 'old_complement_93_over_100_excluded_for_current_112_method':ceiling<F(93,100),
 'prime_constant_vector_lower_bounds':rayleigh,'undamped_uniform_mass_bound':'(245/552) k (33/35)^(2k) at T=k/(10a)',
 'native_and_source_geometric_remainder_requires_a_below':'3/2',
 'fixed112_positive_bessel_three_band_method_fails_at_a18':True,
 'exact_controls':checks,'all_aperture_positivity':False,'lean_formalized':False}
# At a=18 no allowed outer cutoff can reach the published |xi|>=1 high bound.
assert sqrt_rational(F(112*113)).hi < 2*F(18)*pi.lo
Path('notes/data/RPB108_APERTURE_SCALABILITY_CONTROLS_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['positive_bessel_cutoff_strict_upper','three_band_complement_method_ceiling_upper','prime_constant_vector_lower_bounds']},indent=2))
