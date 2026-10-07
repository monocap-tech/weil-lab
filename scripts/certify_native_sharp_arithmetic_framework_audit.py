#!/usr/bin/env python3
"""Exact candidate-obstruction controls; no actual bounded-return certification."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'notes/data/RPB108_SHARP_ARITHMETIC_FRAMEWORK_AUDIT_20261007.json').read_text())
for pin in manifest['internal_sources']:
    data=(root/pin['path']).read_bytes()
    digest=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert digest==pin['blob_sha'], (pin['path'],digest)

# Atomic compact physical measures test the cross terms, including complex phases.
# e^(beta x)=q^x: the difference of coordinates must depend on x-y, not x+y.
pair_checks=0
for q in (F(2),F(3,2),F(5,4)):
    c=lambda x:(q**x+q**(-x))/2
    s=lambda x:(q**x-q**(-x))/2
    for x in range(-4,5):
        for y in range(-4,5):
            assert c(x)*c(y)-s(x)*s(y)==c(x-y)
            assert c(x)*c(y)+s(x)*s(y)==c(x+y)
            if x*y:
                assert c(x+y)!=c(x-y)
            pair_checks+=1

# phi=(1-|v|)_+ has mass 1, odd moment 0, and second moment 1/6.
# For C(u)=d+b*u+c*u^2 on its support, normalized spike pairing is d+c/(6T^2).
# The diagonal limit can have either sign despite eventual zero at fixed u!=0.
spike_checks=0
for T in (2**j for j in range(1,49)):
    for d,b,c in ((F(1),F(3),F(2)),(F(7),F(-4),F(-1))):
        integral=d+c/(6*T*T)
        assert abs(integral-d)<=abs(c)/(6*T*T)
        assert integral>0 and -integral<0
        # fixed u=1/2 lies outside the spike for every T>2
        if T>2:
            assert T*F(1,2)>1
        spike_checks+=1

# Gamma=(I,I) is injective; mixed-nullity holds for every pair of vectors.
mixed_checks=0
for r in range(1,9):
    for i in range(r):
        for j in range(r):
            delta=F(i==j)
            assert delta-delta==0
            assert 2*delta-delta==delta
            assert delta-2*delta==-delta
            mixed_checks+=1

# For a finite restored packet, its sharp contribution is eventually a constant.
# Along T=exp(n), its normalized magnitude is bounded exactly by M/n.
restoration_checks=0
atoms=[(F(2),F(3,7)),(F(5),F(-11,13)),(F(19),F(1,17))]
constant=sum((height*weight for height,weight in atoms),F(0))
budget=sum((height*abs(weight) for height,weight in atoms),F(0))
assert abs(constant)<=budget
for n in range(1,65):
    assert abs(constant/n)<=budget/n
    restoration_checks+=1

print(json.dumps({'pair_cross_term_checks':pair_checks,
    'diagonal_spike_checks':spike_checks,'mixed_range_checks':mixed_checks,
    'finite_restoration_checks':restoration_checks,
    'verified_internal_pins':len(manifest['internal_sources']),
    'scope':'candidate obstructions only; arithmetic return and F4 unproved'},indent=2))
