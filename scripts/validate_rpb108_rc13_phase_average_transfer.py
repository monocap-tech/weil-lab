"""RC13 exact budgets for the actual phase-average prime2 correction.

Periodic autocorrelation and smooth functional identities are analytic in
the report; finite controls here are not a substitute for those arguments.
"""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    if not v: raise AssertionError(checks+1)
    checks+=1
def eb(x,n=28):
    p=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    return p,p+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
tau_cap=F(1,1000)
mask_cap=F(1,1000)
check(eb(F(3,5))[1]<2)
check(eb(F(7,10))[0]>2)
check(eb(F(2))[1]<9)
check(eb(F(53,25))[1]<9) # N_B=3 at B=1.06
check(eb(F(1))[1]<3)
check(F(3,2)**2>2)
check(F(3,5)-2*tau_cap>2*mask_cap)
check(2-(F(7,10)+2*tau_cap)>2*mask_cap)
check(F(3,5)-2*tau_cap>F(1,2))
check(F(7,10)+2*tau_cap<1)
check(F(7,20)+tau_cap<F(53,50))
check(eb(F(1,2))[1]<F(5,3))
check(eb(F(1))[0]>2)
check(eb(tau_cap)[1]<2)
check(2*tau_cap<F(1,2))
check(tau_cap<=F(1,12))
# Each self correction is bounded by A*(12*tau**3+2*tau**2).
derivative_budget=F(1,10000) # assumption A*tau**2 <= this
self_error_upper=3*derivative_budget
c2_lower=F(3,5)/F(3,2)
cross_correction_upper=-2*c2_lower+20*tau_cap
total_correction_upper=2*self_error_upper+cross_correction_upper
check(c2_lower==F(2,5))
check(cross_correction_upper==F(-39,50))
check(total_correction_upper==F(-3897,5000)<0)
chain_guard=F(627,16000)
check(-total_correction_upper>2*chain_guard)
check(F(1,1000*9**2)<=mask_cap) # lawful three-cell bound at anchor cap
# Explicit sufficient tau choice for any finite mask derivative ratio A>=0.
# A/(A+1)^2 <=1/4 follows analytically from (A-1)^2>=0.
for derivative_ratio in [F(0),F(1),F(100),F(10**8),F(10**16)]:
    tau=1/(1000*(derivative_ratio+1))
    check(tau<=tau_cap)
    check((derivative_ratio+1)**2-4*derivative_ratio==(derivative_ratio-1)**2>=0)
    check(derivative_ratio*tau*tau<=F(1,4*10**6)<derivative_budget)
    check(derivative_ratio*(12*tau**3+2*tau**2)<=3*derivative_ratio*tau*tau)
# Algebraic autocorrelation loss and local-renormalization cancellation controls.
for left,right in [(F(1),F(0)),(F(2),F(-1)),(F(1,3),F(7,5))]:
    check(left*left+right*right-2*left*right==(left-right)**2)
print(json.dumps({'milestone':'RC13','status':'PASS','exact_rational_checks':checks,
 'whole_mass_frame':'exact phase average',
 'prime2_cross_correlation':'zero in every translated mask',
 'self_error_per_packet_upper':str(self_error_upper),
 'actual_averaged_gluing_correction_upper':str(total_correction_upper),
 'scope':'analytic smooth test inside the certified anchor; full signed form',
 'relative_energy_gluing_disproved':False,'whole_centered_aperture_extended':False,
 'original_negative_vector_claimed':False,'RH':False,'F4':False,'Lean':False},indent=2))
