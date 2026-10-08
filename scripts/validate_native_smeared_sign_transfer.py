"""Finite rational controls for NF58; no actual spectral computation."""
from fractions import Fraction as F
import json

def run():
    checks=0
    def check(x):
        nonlocal checks
        assert x
        checks+=1
    # Normalized two-region Fourier measures with a stipulated finite moment.
    S,delta,L=F(3),F(1,10000),F(8)
    for k in [1,2,3]:
        for low,high in [(F(3,4),F(1,4)),(F(1,10),F(9,10))]:
            moment=low+high*(L/2)**(2*k)
            estimate=S*(F(32,3)*delta+2*moment*(2/L)**(2*k))
            actual_ceiling=S*(F(32,3)*delta*low+2*high)
            check(actual_ceiling<=estimate)
    # A full smeared lower bound minus a VALID eigenvector error transfers sign.
    for gamma,error in [(F(3,4),F(1,4)),(F(1,100),F(1,200))]:
        original=gamma-error
        check(original>0)
        B=F(7)
        canonical=original/(original+B)
        check(0<canonical<1)
        check(canonical*(1+B/original)==1)
    # Omitting the error would misclassify this negative original eigenvalue.
    gamma,error=F(1,4),F(1,2)
    original=gamma-error
    check(gamma>0 and original<0)
    check(original==gamma-error)
    # Retain the original physical eigenvalue in shifted comparisons.
    mu,mass=F(2,5),F(3,2)
    check(mu*mass!=0)
    return {'passed':True,'finite_checks':checks,
       'scope':'rational transfer and split-budget algebra only; no actual lower bound'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
