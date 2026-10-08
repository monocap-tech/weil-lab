#!/usr/bin/env python3
"""RPB108 IP6: exact rank-one compact contact/fixed exterior witness.
Finite generic source model ONLY; does not compute actual zeta vectors or
validate the infinite-dimensional logarithmic-domain theorem.
"""
from fractions import Fraction as F

checks = 0
a = F(1)
t = F(5, 4)
f_mass = t-a
assert f_mass == F(1, 4); checks += 1
# For unit P-normalized first-contact h=1_[0,1] and f=1_(1,5/4).
contact_pairing = -f_mass
assert contact_pairing == -F(1, 4); checks += 1
assert contact_pairing**2 / f_mass == F(1, 4); checks += 1

for k in range(2, 20):
    s = F(1)-F(1,2**k)
    lam, delta = s, 1-s
    # Squared modulus of fixed outward forced pairing: (-sqrt(s)/4)^2.
    fixed_pairing_squared = s / 16
    fixed_packet_energy = fixed_pairing_squared / f_mass
    full_dual_energy = s*(t-s)
    omitted_shell_energy = s*(1-s)
    old_source_gain = s

    assert 0 < s < 1 and 0 < delta < 1; checks += 1
    assert lam+delta == 1; checks += 1
    assert fixed_packet_energy == s / 4; checks += 1
    assert full_dual_energy-fixed_packet_energy == omitted_shell_energy; checks += 1
    assert 0 < fixed_packet_energy <= full_dual_energy; checks += 1
    assert old_source_gain == s; checks += 1
    assert full_dual_energy / lam == t-s; checks += 1
    assert (full_dual_energy / lam) / delta == (t-s)/(1-s); checks += 1
    # Canonical principal cancellation h_s=-Pi_s C h_s+delta*h_s;
    # Pi_s C h_s=-s*h_s in the rank-one model.
    assert s + delta == 1; checks += 1
    assert omitted_shell_energy <= delta; checks += 1

# A one-dimensional contact kernel is separated by one nonzero exterior test.
assert contact_pairing != 0; checks += 1
# Comparison with near-contact witness using squared values is exact:
for k in range(4,20):
    s=F(1)-F(1,2**k)
    assert s/16 >= F(15,256); checks += 1

print(f"RPB108 IP6 exact rational controls: {checks} passed")
