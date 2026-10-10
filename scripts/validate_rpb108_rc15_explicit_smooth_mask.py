"""RC15 rational mask derivative, full remainder, and reference-floor bounds."""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    if not v: raise AssertionError(checks+1)
    checks+=1
def eb(x,n=64):
    p=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    return p,p+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
# Triangular base radius 4epsilon/5; smoothing radius epsilon/10.
radius_ratio=F(4,5)
mollifier_ratio=F(1,10)
check(radius_ratio+mollifier_ratio==F(9,10)<1)
triangle_norm_sq_ratio=2*radius_ratio/3
triangle_derivative_sq_ratio=2/radius_ratio
base_D_scaled=triangle_derivative_sq_ratio/triangle_norm_sq_ratio
check(base_D_scaled==F(75,16))
check(75<81)
norm_loss_upper=mollifier_ratio*F(9,4)
check(norm_loss_upper==F(9,40)<1)
norm_retention=1-norm_loss_upper
check(norm_retention==F(31,40))
mask_D_scaled=base_D_scaled/(norm_retention**2)
check(mask_D_scaled==F(7500,961))
split_derivative_cost=mask_D_scaled/4
check(split_derivative_cost==F(1875,961))
gamma=F(627,16000)
prime8_sum=F(12093,3740) # inherited actual coefficient enclosure
# Anchor cap, with a now explicit smooth mask.
B_anchor=F(53,50)
epsilon_anchor=F(1,1000*9**2)
check(eb(2*B_anchor)[1]<9)
check(eb(B_anchor)[1]<3)
check(eb(F(13))[0]>2*B_anchor/epsilon_anchor)
anchor_cost=4*B_anchor*7+13+2*prime8_sum+split_derivative_cost
check(anchor_cost<52)
anchor_floor=gamma/(gamma+20+52)
check(anchor_floor>F(1,1900))
eta=F(1,10**37)
check(eta/(eta+52)>F(1,53*10**37))
# Cap 1.10: actual native remainder and reference, no target positivity assumed.
B=F(11,10)
epsilon=F(1,1000*9**3)
check(eb(2*B)[0]>9)
check(eb(2*B)[1]<10)
check(eb(F(2))[1]<9) # L>2, hence 2B/L<2 and N_B=4
check(eb(B)[1]<F(10,3))
check(eb(B)[0]>3) # log3<11/10
check(eb(F(15))[0]>2*B/epsilon)
prime9_upper=F(11,30)
pole_upper=2*(F(10,3)-F(3,10))
check(pole_upper==F(91,15))
remainder_upper=8+2*(prime8_sum+prime9_upper)+pole_upper
check(remainder_upper<22)
correction_upper=4*B*(2*F(10,3)+1)+15+2*(prime8_sum+prime9_upper)+split_derivative_cost
check(correction_upper<58)
reference_floor=gamma/(gamma+22+58)
check(reference_floor==F(627,1280627)>F(1,2100))
# Scale laws: these are exact formula controls, not sampled smooth integrals.
for count in [3,4,8,16]:
    eps=F(1,1000*9**(count-1))
    radius=radius_ratio*eps
    smoothing=mollifier_ratio*eps
    norm_sq=2*radius/3
    derivative_sq=2/radius
    check(derivative_sq/norm_sq==base_D_scaled/(eps*eps))
    check(smoothing*F(9,4)/eps==norm_loss_upper)
    check(mask_D_scaled/(eps*eps)*eps*eps/4==split_derivative_cost)
print(json.dumps({'milestone':'RC15','status':'PASS','exact_rational_checks':checks,
 'mask':'triangle convolved with explicit normalized C-infinity probability bump',
 'D_epsilon_squared_upper':str(mask_D_scaled),
 'anchor_correction_norm_upper':52,'anchor_reference_canonical_floor':'1/1900',
 'cap':'11/10','cap_mask_half_width':str(epsilon),
 'cap_native_remainder_norm_upper':22,'cap_correction_norm_upper':58,
 'cap_reference_canonical_floor':'1/2100',
 'actual_correlation_spectrum_evaluated':False,'whole_tail_certified':False,
 'whole_centered_aperture_extended':False,'RH':False,'F4':False,'Lean':False},indent=2))
