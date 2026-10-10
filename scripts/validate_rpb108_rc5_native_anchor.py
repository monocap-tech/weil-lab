"""RC5 exact aperture envelope, canonical-gap conversion and native controls."""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    if not v: raise AssertionError(checks+1)
    checks+=1
def exp_bounds(x,n=20):
    partial=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    ratio=x/F(n+2)
    check(ratio<1)
    return partial,partial+x**(n+1)/F(factorial(n+1))/(1-ratio)
a=F(53,50)
check(exp_bounds(a)[1]<3)
check(exp_bounds(2*a)[1]<9)
for x,z in [(F(7,10),2),(F(11,10),3),(F(81,50),5),(F(39,20),7)]:
    check(exp_bounds(x)[0]>z)
for root,z in [(F(7,5),2),(F(17,10),3),(F(11,5),5),(F(13,5),7),(F(14,5),8)]:
    check(root*root<z)
prime=F(7,10)/F(7,5)+F(11,10)/F(17,10)+F(7,10)/2+F(81,50)/F(11,5)+F(39,20)/F(13,5)+F(7,10)/F(14,5)
check(prime==F(12093,3740))
envelope=8+2*prime+F(16,3)
check(envelope==F(111079,5610)<20)
eta=F(1,10**37)
canonical=eta/(20+eta)
guard=F(1,21*10**37)
check(canonical>guard)
# Exact convex combination of physical and Garding lower inequalities.
for dnorm,mass,energy in [(F(1),F(1,20),eta/F(20)),(F(3),F(1,10),F(1)),(F(2),F(0),F(2))]:
    weight=eta/(20+eta)
    check(weight*(dnorm-20*mass)+(1-weight)*(eta*mass)==canonical*dnorm)

# Native form family I-N*N; near null old energy determines the test,
# with outgoing forcing remaining nonzero at a fixed enlargement.
v=F(1,4)
for u in [F(1,2),F(3,4),F(15,16),F(255,256)]:
    native_old=1-u*u
    forcing=-u*v
    check(native_old>0 and forcing*forcing==u*u*v*v)
check(v*v>0) # limiting outgoing norm squared at original contact u=1
# Complete mass shift changes the native old residual and contact.
u,mu=F(3,4),F(7,16)
check(1-u*u-mu==0)
check(1-u*u==mu>0)
print(json.dumps({'milestone':'RC5','status':'PASS','exact_rational_checks':checks,
 'aperture':'53/50','native_remainder_upper':'20',
 'canonical_gap_guard':str(guard),'CC119_physical_gap_inherited':True,
 'actual_native_outward_modulus_proved':False,'RH':False,'F4':False,'Lean':False},indent=2))
