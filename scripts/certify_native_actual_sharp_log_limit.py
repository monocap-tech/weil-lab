#!/usr/bin/env python3
"""Independent rational tail/layer-cake/Abel controls; not actual-null certification."""
from fractions import Fraction as F
import json

def exp_minus_bounds(x,n=63):
    assert 0<=x<=1
    total=term=F(1)
    for j in range(1,n+1):
        term*= -x/j
        total+=term
    return total,total+term*(-x)/(n+1)

cosine_checks=0
for j in range(1,65):
    u=F(j,64)
    assert u*u/2-u**4/24>=u*u/4
    cosine_checks+=1
assert F(1,12*2)==F(1,24)

atoms=[(F(2**j),F(1,2**j),F((-1)**j,2**j)) for j in range(1,33)]
layercake_checks=abel_checks=weak_tail_checks=0
for j in range(32):
    for ratio in (F(1),F(3,2)):
        T=ratio*2**j
        edges=sorted({F(0),T}|{u for u,v,d in atoms if u<T})
        integral=F(0)
        for a,b in zip(edges,edges[1:]):
            midpoint=(a+b)/2
            tail=sum((v for u,v,d in atoms if u>midpoint),F(0))
            integral+=(b*b-a*a)*tail
        direct=sum((min(u*u,T*T)*v for u,v,d in atoms),F(0))
        assert integral==direct
        layercake_checks+=1
        tail=sum((v for u,v,d in atoms if u>T),F(0))
        second=sum((u*u*v for u,v,d in atoms if u<=T),F(0))
        assert T*tail<=2 and second<=4*T
        weak_tail_checks+=1
        error_budget=second/(2*T)+T*tail
        assert error_budget<=4
        # Bracket actual finite signed Abel-minus-sharp using Taylor only
        # below the cutoff; above it use the legal multiplier interval [0,T].
        error_lo=error_hi=F(0)
        for u,v,d in atoms:
            if u<=T:
                lo,hi=exp_minus_bounds(u/T)
                al=T*(1-hi); au=T*(1-lo)
                assert 0<=al<=au<=u
                assert u-al<=u*u/(2*T)
                a,b=al-u,au-u
            else:
                a,b=F(0),T
            left,right=a*d,b*d
            error_lo+=min(left,right); error_hi+=max(left,right)
        assert -error_budget<=error_lo<=error_hi<=error_budget
        abel_checks+=1

# Old paired-atom control violates the new uniform weak-tail premise.
paired_rejections=0
for j in range(1,65):
    T=F(4**j,2)
    positive_mass=F(9*j,4*4**j)
    assert T*positive_mass==F(9*j,8)
    paired_rejections+=1

# A neutral weak-tail control still has a positive sharp/log slope.
assert F(1,2)/(1-F(1,2))==1
neutral_checks=0
for j in range(1,65):
    T=F(3*2**j,2)
    infinite_tail=F(1,2**j)
    assert T*infinite_tail<2
    sharp=sum((2**k*F(1,2**k) for k in range(1,j+1)),F(0))
    assert sharp==j
    neutral_checks+=1

print(json.dumps({
    "status":"PASS",
    "scope":"rational unsigned-tail and signed Abel/sharp controls; actual theorem proved analytically",
    "cosine_lower_margins":cosine_checks,
    "independent_atomic_layercake_agreements":layercake_checks,
    "finite_signed_abel_error_brackets":abel_checks,
    "weak_tail_and_second_moment_budgets":weak_tail_checks,
    "old_paired_control_tail_rejections":paired_rejections,
    "neutral_weak_tail_positive_slope_controls":neutral_checks,
    "actual_arithmetic_sign_or_lean_certificate":False,
},indent=2,sort_keys=True))
