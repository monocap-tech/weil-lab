"""Exact finite symbol/background/inverse controls; not a whole positivity certificate."""
from fractions import Fraction as F
import json


def run():
    checks=0
    def check(v):
        nonlocal checks
        assert v
        checks+=1
    q=lambda j:F(4*j+1,4)
    # z=pi^2 xi^2 is symbolic, instantiated rationally to check exact algebra.
    for j in range(16):
        for z in [F(0),F(1,16),F(1),F(100)]:
            term=z/(q(j)*(q(j)**2+z))
            check(term==1/q(j)-q(j)/(q(j)**2+z))
            check(0<=term<=1/q(j))
            check(term<=z/q(j)**3)
    # Actual previously certified joint bound at a=21/20.
    joint=F(1063939,500000)
    lower_constant=-F(27,5)+sum((1/q(j) for j in range(32)),F(0))
    check(lower_constant-joint>F(157,1000))
    # Background inverse Neumann-series remainder is geometric, not a kernel
    # distance Maclaurin expansion. J counts ALL prime-path lengths.
    for scalar,budget in [(F(3),joint),(F(5),F(3)),(F(8),F(7))]:
        delta=scalar-budget
        r=budget/scalar
        check(0<r<1)
        for J in [0,1,4,16]:
            partial=sum((r**j/scalar for j in range(J+1)),F(0))
            check(1/delta-partial==r**(J+1)/delta)
    # Exact pole-resolvent rank-one formula, scalar control with both signs.
    for base,c,s in [(F(3),F(2),F(1)),(F(5),F(1),F(3))]:
        inverse=1/base-2*(c/base)**2/(1+2*c*c/base)
        check(inverse==1/(base+2*c*c))
        check((base+2*c*c)-2*s*s<base+2*c*c)
    for N in [1,2,8,32,128]:
        b=q(N)
        for power in [2,3]:
            partial=sum((1/q(j)**power for j in range(N,N+100)),F(0))
            majorant=1/b**power+1/F(power-1)/b**(power-1)
            check(partial<majorant)
    # Shifted positive eigenlevel is not an original zero level.
    mu=F(3,2)
    for gap in [F(1,2),F(1,10),F(1,100)]:
        original=mu-gap
        check(original>0)
        check(original-mu==-gap<0)
    return {'passed':True,'finite_checks':checks,
            'target_aperture':'21/20','archimedean_terms':32,
            'bounded_background_floor_strict_lower':'157/1000',
            'background_scope':'scalar arch plateau minus complete prime operator; compact terms retained separately',
            'full_compact_gain_certified':False,'new_aperture_certificate':False,
            'lean_certified':False}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
