"""Independent recurrence/mass/tail audit of the smallest dimension-change probe."""
import json,hashlib
from pathlib import Path
from math import factorial,prod
from certify_native_legendre_small_window import F,I,atan,log_rational
from validate_native_prime5_depth6_complement_097 import polynomial
p=Path('notes/data/RPB108_PRIME8_DIMENSION113_105_PREFLIGHT_20261008.json');b=p.read_bytes();c=json.loads(b)
assert c['aperture']=='21/20' and c['retained_vectors']==113 and c['physical_degrees']==list(range(113))
a=F(21,20);k=113;I.grid=10**120;pi=16*atan(F(1,5),180)-4*atan(F(1,239),180)
cuts=list(map(F,c['cutoffs']));assert cuts==[F(15)*k/112,F(16)*k/112,F(17)*k/112]
high=[log_rational(t,350)-F(7,216)/t**2 for t in cuts];intervals=[tuple(map(F,x))for x in c['archimedean_high_intervals']]
assert all(lo<=x.lo<=x.hi<=hi for (lo,hi),x in zip(intervals,high))
checks=0
for t,r,d in zip(cuts,c['frequency_mass_upper'],c['complete_mass_details']):
 assert d['degrees']==list(range(k,k+48)) and d['iteration_depth']==6
 U=F(d['positive_region_argument_squared_upper']);assert (2*a*t*pi.hi)**2<=U<k*(k+1)
 y=2*a*t*pi.lo
 for i,n in enumerate(d['degrees']):
  H=polynomial(n,6)
  rate=F(d['integrated_rate_lower'][i]);exact=F(2*n+1)-sum(power*v*U**(power//2)for power,v in H.items())
  assert rate==F((exact*10**80).__floor__(),10**80)>0
  exponent=F(d['squared_damping_exponent_lower'][i]);assert 0<exponent<=sum(v*y**power for power,v in H.items())
  den=sum((exponent**j/factorial(j)for j in range(101)),F(0));D=prod(range(1,2*n+2,2))
  assert F(d['individual_integrated_term_upper'][i])>=4*a*t*(2*n+1)*U**n/(rate*D*D*den);checks+=1
 upper=2*a*F(22,7)*t;n=k+48;ratio=upper**2/F((2*n+1)*(2*n+3));assert 0<ratio<1
 tail=F(d['infinite_undamped_tail_upper']);assert tail>=4*a*t*upper**(2*n)/(prod(range(1,2*n+2,2))**2*(1-ratio))
 assert F(r)==sum(map(F,d['individual_integrated_term_upper']),F(0))+tail
rho=list(map(F,c['frequency_mass_upper']));arch=intervals[-1][0]-(intervals[0][1]+F(27,5))*rho[0]
for j in range(1,3):arch-=(intervals[j][1]-intervals[j-1][0])*rho[j]
assert arch==F(c['three_band_archimedean_lower'])
pole=16*a*(a/2)**(2*k)/factorial(k)**2;assert pole==F(c['pole_absolute_upper']) and a/2<log_rational(F(2),350).lo
lower=arch-F(c['prime_norm_upper'])-pole;assert lower==F(c['physical_unrounded_lower'])>F(c['physical_lower'])>F(c['original112_witness_requirement'])
out={'aperture':'21/20','retained_vectors':113,'preflight_sha256':hashlib.sha256(b).hexdigest(),'independent_damped_degree_checks':checks,
 'independent_infinite_tails_checked':3,'physical_complement_lower':c['physical_lower'],'comparison_with_original112_witness_only':True,
 'native113_complete':False,'source113_complete':False,'residual113_complete':False,'whole_domain_positivity':False,'lean_formalized':False}
print(json.dumps(out,indent=2))
