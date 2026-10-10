"""RC28 rational budget controls; no kernel entries or Riesz solve computed."""
from fractions import Fraction as F
from math import factorial
import json

def controls():
    B,delta,T,N=F(11,10),F(1,10000),F(100000),210000
    # exp(7/3)>10 proves log(10)<7/3 without floating arithmetic.
    exp_lower=sum((F(7,3)**j/factorial(j) for j in range(13)),F(0))
    assert exp_lower>10
    assert T/delta==10**9
    length_upper=F(21)
    h_upper=length_upper/N
    assert h_upper==F(1,10000)
    small_upper=3*delta  # e<3
    large_upper=4*B/T
    upper_error=small_upper+large_upper+h_upper
    assert small_upper==F(3,10000)
    assert large_upper==F(11,250000)
    assert upper_error==F(111,250000)
    assert upper_error<F(1,2000)
    assert h_upper<F(1,2000)
    # Monotone-factor variation: integral |(ab)'| <= 1+1.
    assert F(1,2)*2*h_upper==h_upper
    # Polynomial coefficient metric transport includes physical mass.
    D=[2*B/F(2*j+1) for j in range(8)]
    assert all(d>0 for d in D)
    assert all(upper_error*d<F(1,2000)*d for d in D)
    # An entry error alone is not an operator error for arbitrary dimension.
    assert 8*h_upper>F(1,2000)
    return dict(milestone='RC28',rational_controls=12,status='PASS',
                cauchy_atoms=N,lower_error_upper=str(h_upper),
                upper_error_upper=str(upper_error),
                actual_atoms_evaluated=False,actual_matrices_evaluated=False,
                Riesz_solve=False,aperture_extended=False)

if __name__=='__main__':
    print(json.dumps(controls(),indent=2))
