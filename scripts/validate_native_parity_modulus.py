"""Rational controls for analytic actual-form modulus defects; no null computation."""
from fractions import Fraction as F
from math import factorial
import json

q=F(2,3)
exp_lower_log_bound=sum((q**j/factorial(j) for j in range(7)),F(0))+q**7/factorial(7)/(1-q/8)
assert exp_lower_log_bound<2
q=F(7,10)
exp_upper_log_bound=sum((q**j/factorial(j) for j in range(5)),F(0))
assert exp_upper_log_bound>2
exp_one_upper=sum((F(1,factorial(j)) for j in range(7)),F(0))+F(1,factorial(7))/(1-F(1,8))
assert exp_one_upper<3  # log 3 > 1, so no second active prime at a=1/2.
assert F(3,2)**2>2
eta=F(1,64)
assert eta<F(2,3)/12
assert F(2,3)/3-eta/2>0
assert 2*F(7,10)/3+eta/2<F(1,2)
assert F(7,10)/3+eta<F(2,3)
assert F(2,3)/3-eta>F(1,6)
odd_upper=64*eta-8*F(4,9)
assert odd_upper==F(-23,9)
even_kernel_upper=2+F(6,11)+F(6,19)
even_upper=8*even_kernel_upper-32
assert even_kernel_upper==F(598,209)
assert even_upper==F(-1904,209)<0
# The squared center exponentials are 8 and 32, neither an integer square.
assert 2**2<8<3**2 and 5**2<32<6**2
checks=0
for u in map(F,[-3,-1,0,1,3]):
 for v in map(F,[-3,-1,0,1,3]):
  opposite=4*abs(u*v) if u*v<0 else 0
  assert (u-v)**2-(abs(u)-abs(v))**2==opposite
  assert (u+v)**2-(abs(u)+abs(v))**2==-opposite
  assert u*v-abs(u)*abs(v)==-opposite/2
  checks+=3
print(json.dumps({
 "scope":"exact rational constants and two-point identities; analytic integrals proved in note",
 "log_two_bounds":["2/3","7/10"],
 "exp_two_thirds_upper":str(exp_lower_log_bound),
 "exp_seven_tenths_lower":str(exp_upper_log_bound),
 "exp_one_upper":str(exp_one_upper),
 "two_point_identity_checks":checks,
 "odd_eta":str(eta),"odd_defect_strict_upper":str(odd_upper),
 "even_defect_strict_upper_per_eta":str(even_upper),
 "equal_physical_masses":"4",
 "actual_prime_and_cross_pole_terms_used":True,
 "negative_native_energy_claimed":False,"null_vector_constructed":False,
 "lean_certified":False,"f4_closed":False,"full_transport_closed":False
},indent=2,sort_keys=True))
