"""Exact comparisons for the shifted archimedean contact control."""
from fractions import Fraction as F
from math import factorial
import json

exp_upper=sum((F(1,factorial(j)) for j in range(7)),F(0))+F(1,factorial(7))/(1-F(1,8))
assert exp_upper<F(11,4)
assert F(11,4)**3<25
checked=0
for left in [F(-3),F(-1),F(-1,4),F(0),F(1,4),F(1),F(3)]:
 for right in [F(-3),F(-1),F(-1,4),F(0),F(1,4),F(1),F(3)]:
  defect=(left-right)**2-(abs(left)-abs(right))**2
  assert defect>=0
  assert defect==(4*abs(left*right) if left*right<0 else 0)
  checked+=1
mass_signed=mass_modulus=F(2)
sign_energy_lower=F(4,5)
assert mass_signed==mass_modulus and sign_energy_lower>0
rejected=[]
for name,claim in [
 ("opposite_sign_energy_defect_is_zero", (F(1)-F(-1))**2==(abs(F(1))-abs(F(-1)))**2),
 ("ordered_pair_factor_is_eight", F(1,2)*2*4==8),
]:
 assert not claim
 rejected.append(name)
print(json.dumps({
 "scope":"comparison constants only; no actual zeta null vector or computed eigenvalue",
 "exp_one_rational_upper":str(exp_upper),
 "exp_three_halves_upper":"5",
 "modulus_identity_checks":checked,
 "equal_physical_masses":"2",
 "sign_energy_difference_lower":"4/5",
 "invalid_implications_rejected":rejected,
 "actual_arithmetic_terms_present":False,
 "lean_certified":False,"f4_closed":False,"full_transport_closed":False
},indent=2,sort_keys=True))
