#!/usr/bin/env python3
"""Rational exponent and artificial-location controls, not actual zeros."""
from fractions import Fraction as F
import json

for k in range(1,65):
    delta=F(k,512);sigma=F(1,2)+delta
    power=3*(1-sigma)/(2-sigma)
    assert power==1-2*delta/(F(3,2)-delta)
    assert power<=1-F(4,3)*delta
    assert (7-5*sigma)/(2-sigma)<=3
second=F(0)
for j in range(3,65):
    beta=F(1,j);count=j*2**j
    assert beta<=F(3,8)
    block=count*beta**2
    assert block==F(2**j,j)
    second+=block
    assert second<=8*F(2**j,j)
    inverse_height_lower=block/(1+2**(j+1))
    assert inverse_height_lower>=F(1,3*j)
print(json.dumps({"kind":"rational controls only, artificial locations",
 "uniform_density_exponent_checks":64,"location_blocks_checked":62,
 "inverse_height_block_lower":"1/(3j)","critical_source_bound_certified":False},
 indent=2,sort_keys=True))
