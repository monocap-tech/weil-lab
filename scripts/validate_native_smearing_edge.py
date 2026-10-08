"""Finite edge and sign controls; analytic actual-packet limits are not certified."""
from fractions import Fraction as F
import json

def run():
    checks=0
    def check(x):
        nonlocal checks
        assert x
        checks+=1
    b,delta=F(1,8),F(1,64)
    # Averaging a correlation of support [-2b,2b] has nonzero points past 2b.
    u,v=2*b+delta/4,-3*delta/4
    check(u>2*b)
    check(-delta<v<delta)
    check(-2*b<u+v<2*b)
    for alpha,J,H in [(F(101,100),F(2),F(1,100)),(F(5,4),F(3),F(1,2))]:
        prime=2*(alpha*J-H)
        pole=-2*alpha*J
        check(prime+pole==-2*H<0)
        check(prime+2*H+pole==0)
    # Zero-head-to-zero and a negative continuous gap contribution coexist.
    m0,sigma=F(-3),F(99,100)
    check(m0*(1-sigma)<0)
    # The changed pole and added halo require additional error terms.
    S,S_halo=F(6),F(13,2)
    check(S_halo>S)
    check((F(101,100)-1)*F(4)>0)
    return {'passed':True,'finite_checks':checks,
       'scope':'finite support/sign/error controls only; no actual spectral certificate'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
