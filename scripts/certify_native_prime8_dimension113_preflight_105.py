"""Smallest dimension-change complement probe after the exact 112-Schur failure."""
import json,hashlib
from pathlib import Path
from math import factorial
from certify_native_legendre_small_window import F,I,log_rational
from certify_native_iterated_damped_mass_depth6 import integrated_iterated_mass
saved=I.grid;I.grid=10**80
try:
 a=F(21,20);k=113;cuts=[F(15)*k/112,F(16)*k/112,F(17)*k/112]
 prime=Path('notes/data/RPB108_PRIME8_WEIGHTED_DEPTH10_105_CERTIFICATE_20261008.json').read_bytes();p=json.loads(prime)
 B=F(p['joint_prime_operator_norm_upper']);rho=[];details=[]
 for t in cuts:
  r,d=integrated_iterated_mass(a,k,t,depth=6);rho.append(r);details.append(d)
 high=[log_rational(t)-F(7,216)/t**2 for t in cuts]
 arch=high[-1].lo-(high[0].hi+F(27,5))*rho[0]
 for j in range(1,3):arch-=(high[j].hi-high[j-1].lo)*rho[j]
 pole=16*a*(a/2)**(2*k)/factorial(k)**2;lower=arch-B-pole
 c=F((lower*10**6).__floor__(),10**6)
 w=json.loads(Path('notes/data/RPB108_PRIME8_WHOLE112_105_VALIDATION_20261008.json').read_bytes());needed=F(w['required_scalar_complement_strict_lower'])
 out={'aperture':'21/20','retained_vectors':k,'physical_degrees':list(range(k)),'cutoffs':list(map(str,cuts)),
 'frequency_mass_upper':list(map(str,rho)),'complete_mass_details':details,
 'archimedean_high_intervals':[[str(x.lo),str(x.hi)]for x in high],'three_band_archimedean_lower':str(arch),
 'prime_input_sha256':hashlib.sha256(prime).hexdigest(),'prime_norm_upper':str(B),'pole_absolute_upper':str(pole),
 'physical_unrounded_lower':str(lower),'physical_lower':str(c),'physical_lower_display':float(lower),
 'exceeds_original112_witness_requirement':c>needed,'original112_witness_requirement':str(needed),
 'scope':'113-vector complement only; old 112-vector residual/finite data cannot certify the new decomposition',
 'native113_complete':False,'source113_complete':False,'residual113_complete':False,'whole_domain_positivity':False,
 'new_finite_conditioning_and_source_budget_pending':True,'f4_entry_closed':False,'lean_formalized':False}
 Path('notes/data/RPB108_PRIME8_DIMENSION113_105_PREFLIGHT_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'retained_vectors':k,'complement_lower':str(c),'display':float(lower),'old_witness_requirement_display':float(needed),'exceeds_old_witness_requirement':c>needed}))
finally:I.grid=saved
