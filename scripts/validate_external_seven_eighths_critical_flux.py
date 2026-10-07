#!/usr/bin/env python3
"""Strip arithmetic and signed source flux controls, not actual zeta data."""
from fractions import Fraction as F
from itertools import product
import json

def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def scale(a,x): return (a*x[0],a*x[1])
def conj(x): return (x[0],-x[1])
def norm(x): return x[0]**2+x[1]**2

def main():
    flux=strip=tail=0
    vals=[(F(a),F(b)) for a,b in product((-1,0,1),repeat=2)]
    for p,n,u,v in product(vals,vals,(F(-1),F(-1,2),F(0),F(1,2),F(1)),(F(-1,2),F(-1,4),F(0),F(1,4),F(1,2))):
        c=(1-u*u)/(1+u*u); s=2*u/(1+u*u)
        ch=(1+v*v)/(1-v*v); sh=2*v/(1-v*v)
        phase=(c,s)
        pt=mul(phase,add(scale(ch,p),scale(sh,n)))
        nt=mul(phase,add(scale(sh,p),scale(ch,n)))
        real=mul(conj(p),pt)[0]-mul(conj(n),nt)[0]
        j=mul(p,conj(n))[1]; d=norm(p)-norm(n)
        assert real==ch*c*d+2*sh*s*j
        assert j*j<=norm(p)*norm(n)
        flux+=1
    B=F(3,8)
    assert B/F(1,2)==F(3,4) and B*B/F(1,4)==F(9,16)
    for k in range(129):
        sig=F(1,8)+F(3*k,4*128)
        assert sig<=F(7,8) and 1-sig<=F(7,8)
        assert abs(sig-F(1,2))<=B
        strip+=1
    for n in range(1,129):
        positive=sum(F(1,2**j) for j in range(1,n+1))
        missing=F(1,2**n)
        assert positive+missing==1
        critical=sum(F(2**j)*F(1,2**j) for j in range(1,n+1))
        assert critical==n
        tail+=1
    print(json.dumps(dict(status="rational_controls_pass",flux_cases=flux,
        strip_cases=strip,neutral_tail_cases=tail,
        scope="algebra/abstract controls; no actual critical bound or derivative promotion"),
        sort_keys=True))
if __name__=="__main__": main()
