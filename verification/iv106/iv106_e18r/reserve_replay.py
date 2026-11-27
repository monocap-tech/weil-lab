#!/usr/bin/env python3
"""Exact rational conditional reserve replay; not a native or Schur certificate."""
from fractions import Fraction as F
from math import ceil, factorial
import sys
sys.set_int_max_str_digits(0)

h = F(11, 3325)
L = F(4393, 4000)
ell = -F(11, 10) + h

# All first 34 cells lie more than 2 units to the left of the collar.
# The absolute kernel is then <1 (e>2), |v_h|<=722 by its literal
# factored derivative coefficients, and the L1 mass of u_i is 1/(1000k).
# Hence |A_ij|<=3/(1000k)<1, conditional on the actual response identity.
assert -F(11, 10)+35*h < L-2
assert h*722 < 3

def exponent(x):
    e = max(0, len(str(x.denominator))-len(str(x.numerator)))
    while x*10**e < 1:
        e += 1
    while e and x*10**(e-1) >= 1:
        e -= 1
    assert x*10**e >= 1
    assert not e or x*10**(e-1) < 1
    return e

def reserve(k):
    q = F(3, 2000*k)
    rates = [2*n+F(1,2) for n in range(1,k+1)]
    d = F(1)
    for s in rates:
        # E18C weight enclosure: normalized bump mass, seed beta integral
        # 1/2772, and exp(1)<3.
        d *= h**4*(s**3-s/4)/F(2772*1000*k)/3**ceil(s*(L+q-ell))
    for i in range(k):
        for j in range(i+1,k):
            diff = rates[j]-rates[i]
            d *= diff*h*diff*q/3**ceil(rates[j]*q)
    # Single ordered tuple only: deliberately pay k!, rather than assume
    # the yet unstaged all-permutations reserve.
    r = d/factorial(k)
    assert r > 0
    # Cofactor upper from |A_ij|<1: (k-1)!.
    # Inverse ENTRY bound, not an operator norm or actual inverse magnitude.
    U = F(factorial(k-1),1)/r
    return (k,exponent(d),exponent(r),exponent(1/U))

expected = [
(1,19,19,19),(2,44,44,44),(3,77,77,78),(4,116,118,119),
(5,164,166,167),(6,218,220,223),(7,278,282,285),(8,346,351,355),
(9,421,427,431),(10,503,509,515),(11,591,599,605),(12,686,695,703),
(13,789,799,807),(14,897,908,918),(15,1013,1025,1036),(16,1135,1148,1160),
(17,1264,1278,1292),(18,1399,1415,1430),(19,1542,1559,1574),(20,1690,1708,1726),
(21,1845,1865,1883),(22,2007,2028,2048),(23,2176,2198,2219),(24,2351,2374,2397),
(25,2532,2557,2581),(26,2720,2746,2772),(27,2914,2942,2969),(28,3115,3145,3173),
(29,3322,3353,3383),(30,3536,3568,3599),(31,3756,3790,3822),(32,3982,4018,4052),
(33,4215,4252,4287),(34,4454,4493,4530)]
if __name__ == "__main__":
    rows = [reserve(k) for k in range(1,35)]
    assert rows == expected
    print("k, tuple exponent, determinant lower exponent, inverse entry upper exponent")
    for row in rows:
        print(*row)
    print("34/34 conditional rational reserve cases PASS")
