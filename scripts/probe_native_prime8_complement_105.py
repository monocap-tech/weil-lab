"""Fixed-target complement probe; exact bounds, no finite/sign claim."""
import json
from math import factorial
from certify_native_legendre_small_window import F,I,log_rational
from certify_native_iterated_damped_mass_depth6 import integrated_iterated_mass
I.grid=10**80
a=F(21,20);k=112
out=[]
for t in [F(15),F(16),F(17),F(171,10),F(179,10)]:
 try:
  rho,details=integrated_iterated_mass(a,k,t,depth=6)
  out.append({'cut':str(t),'mass_upper':str(rho),'mass_display':float(rho),'details':details})
 except ValueError as e:out.append({'cut':str(t),'rejected':str(e)})
path='notes/data/RPB108_PRIME8_COMPLEMENT_PROBE_105_20261008.json'
open(path,'w').write(json.dumps({'aperture':str(a),'retained_vectors':k,'cuts':out},indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if k!='details' and k!='mass_upper'} for r in out]))
