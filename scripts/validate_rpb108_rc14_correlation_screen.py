"""RC14 exact constants and finite controls for the phase-correlation screen."""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    if not v: raise AssertionError(checks+1)
    checks+=1
def eb(x,n=60):
    p=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    return p,p+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
B=F(53,50)
r0=F(1,81000)
check(0<r0<2*B)
check(eb(B)[1]<3)
check(eb(F(13))[0]>2*B/r0)
check(eb(2*B)[1]<9)
# Inherited RC5 prime coefficient sum enclosure; no source rerun.
prime_sum_upper=F(12093,3740)
constant=4*B*7+13+2*prime_sum_upper
check(constant==F(459523,9350))
gamma=F(627,16000)
eta=F(1,10**37)
for derivative_ratio in [F(0),F(1),F(81000**2),F(100*81000**2)]:
    cost=constant+derivative_ratio*r0*r0/4
    canonical_floor=gamma/(gamma+20+cost)
    anchor_relative_floor=eta/(eta+cost)
    check(0<canonical_floor<1)
    check(canonical_floor*(1+(20+cost)/gamma)==1)
    check(0<anchor_relative_floor<1)
    check(anchor_relative_floor*(1+cost/eta)==1)
# Schur screen with a paid whole-tail and a paid cross block.
head=F(3,4)
tail_norm=F(1,10)
cross=F(1,5)
schur_floor=head-cross*cross/(1-tail_norm)
check(schur_floor==F(127,180)>0)
check(head*(1-tail_norm)-cross*cross==F(127,200)>0)
# A positive head alone does not screen an unexamined negative tail.
check(1+F(0)>0)
check(1-F(11,10)<0)
# Nor can the head and tail be certified independently while dropping mixing.
check(1>0)
check(1*1-2*2==-3<0)
# Compact finite controls permit contact and crossing; no arithmetic estimate here.
for parameter in [F(9,10),F(1),F(11,10)]:
    eigenvalue=1-parameter
    check(eigenvalue==F(1)-parameter)
check(1-F(9,10)>0)
check(1-F(1)==0)
check(1-F(11,10)<0)
print(json.dumps({'milestone':'RC14','status':'PASS','exact_rational_checks':checks,
 'anchor_correction_norm_bound':'459523/9350 + D*r0**2/4; r0=1/81000',
 'positive_reference':'whole phase-average form, not the original target',
 'target_screen':'I+K >= nu I with nu>0',
 'finite_certificate':'head floor > cross_norm**2/(1-tail_norm), tail_norm<1',
 'actual_correlation_spectrum_evaluated':False,'whole_tail_certified':False,
 'whole_centered_aperture_extended':False,'RH':False,'F4':False,'Lean':False},indent=2))
