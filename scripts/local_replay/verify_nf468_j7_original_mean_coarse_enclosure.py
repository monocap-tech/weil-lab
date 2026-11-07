#!/usr/bin/env python3
"""NF468 exact rational original J7 inherited mean enclosure; no compact-kernel quadrature."""
from fractions import Fraction as F
import json
a=F(26,25);b=F(53,50);L=b-a
zlo=F(13,200000000000);zhi=F(9,100000000000)
M=F(30000)
radius=M*L/2
assert L==F(1,50) and radius==300
assert zlo==F(65,10**12)
assert zhi==F(9,10**11)
lower=zlo-radius;upper=zhi+radius
assert lower<0<upper
assert radius/zlo>10**12
print(json.dumps({"pass":"NF468","standing":"source-inherited coarse interval; derivative-only METHOD STOP",
"panel":["26/25","53/50"],"length":"1/50",
"mean_lower":str(lower),"mean_upper":str(upper),
"mean_uncertainty_radius":"300",
"NF446_compact_arch_integral_evaluated":False,
"decision_quality":False,"W-ODD-NEG":"OPEN"},indent=2))
