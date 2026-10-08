#!/usr/bin/env python3
"""RPB108 IP8: exact-rational generic-IP7 feasibility and prime-8 chamber audit.

This is arithmetic and certification-design validation only. It does not
construct an actual native matrix at aperture 53/50 or prove positivity.
"""
from fractions import Fraction as F
from math import isqrt, factorial

def log_bounds(n, terms=24):
    x = F(n-1, n+1)
    lo = 2*sum((x**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    remainder = 2*x**(2*terms+1)/(F(2*terms+1)*(1-x*x))
    return lo,lo+remainder

def sqrt_upper(n,den=10**6):
    return F(isqrt(n*den*den)+1,den)

def sinh_lower(x):
    return sum((x**(2*k+1)/factorial(2*k+1) for k in range(4)),F(0))

B = F(53,50)
d = 2*B
log2lo,log2hi = log_bounds(2)
log3lo,log3hi = log_bounds(3)
assert 3*log2hi < d < 2*log3lo  # log8<2B<log9, rigorously
powers=(2,3,4,5,7,8)
base={2:2,3:3,4:2,5:5,7:7,8:2}
# Includes actual von Mangoldt prime-power weights, both shift orientations.
rprime_lo=2*sum((log_bounds(base[n])[0]/sqrt_upper(n)
                 for n in powers),F(0))
# The CC33 pole bound is +4*sinh B, independent of pole sign.
rpole_lo=4*sinh_lower(B)
r_lower=rprime_lo+rpole_lo
assert r_lower > F(57,5)
# r_B=r_*+2 sum Lambda(n)/sqrt(n)+4 sinh B; r_* >= 0.
# Any IP7 positive certificate necessarily has
# eta < g(r_B)=(1+r_B)/(r_B(1+2*r_B)), as
# lambda_min(A_F)<=||Q_B||<=1+r_B.
# g is strictly decreasing for r>0.
r=F(57,5)
g=(1+r)/(r*(1+2*r))
inv=1/g
assert inv>F(547,25)
# eta=tau+1/log(e+R)>1/log(e+R);
# therefore log(e+R)>inv>547/25.
# The finite positive exponential series proves exp(547/25)>3e9+3.
x=F(547,25)
exp_lower=sum((x**k/factorial(k) for k in range(110)),F(0))
assert exp_lower>F(3000000003)
# Since e<3, the generic construction requires R>3,000,000,000.
# The breakpoint functions log(n)/d and 1-log(m)/d cannot cross
# within log8<d<log9: collision would imply exp(d)=n*m, an integer
# strictly between 8 and 9. Thus the 13-panel ordering is stable.
for n in powers:
    for m in powers:
        assert n*m<=8 or n*m>=9


# CC37's globally valid |r_arch|<8 bound combines with the SAME
# six-prime coefficient rational upper sum for B=53/50, since B<log3.
assert log3lo>B
r_upper=F(8)+2*F(12093,3740)+F(16,3)
assert r_upper==F(111079,5610) and r_upper<F(20)
# When one USES the convenient rigorously admissible bound r=20,
# the IP7 sufficient-gate nonvacuity threshold is much more expensive.
r_eff=F(20)
g_eff=(1+r_eff)/(r_eff*(1+2*r_eff))
assert g_eff==F(21,820)
assert 1/g_eff==F(820,21)>F(39)
exp_39_lower=sum((F(39)**k/factorial(k) for k in range(100)),F(0))
assert exp_39_lower>F(80000000000000003)
# Hence the chosen effective-r=20 generic gate NECESSARILY has R>8e16.

print("PASS: log8 < 2*(53/50) < log9 by exact log intervals")
print("PASS: the 13 original prime-8 panel ordering is stable")
print("Certified lower bound on CC33 unsigned budget r_B:", float(r_lower))
print("Certified r_B > 57/5:", r_lower>r)
print("Necessary eta ceiling (weaker rational bound):",float(g))
print("Necessary 1/eta greater than:",float(inv))
print("PASS: IP7 generic low-frequency spectral test requires R>3e9")
print("SCOPE: no actual finite Weil matrix, complement certificate, or new sign")

print("PASS: CC37 inherited global remainder bound extends to B=53/50, r_B<20")
print("PASS: with effective Schur budget 20, generic construction requires R>8e16")
