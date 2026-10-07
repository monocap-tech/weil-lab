#!/usr/bin/env python3
"""Rational weak-tail, complete-prime and gamma-sign controls; not F4 certification."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'notes/data/RPB108_SUBLOG_PRIME_BULK_20261007.json').read_text())
for pin in m['internal_sources']:
    b=(root/pin['path']).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['blob_sha']
def raw_log_bounds(x,N=32):
    z=(x-1)/(x+1)
    assert 0<=z<=F(1,3)
    lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    return lo,lo+2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
L2,U2=raw_log_bounds(F(2))
assert F(2,3)<L2<U2<F(7,10)
def log_bounds(x):
    k=0
    while x>=2:x/=2;k+=1
    lo,hi=raw_log_bounds(x)
    return lo+k*L2,hi+k*U2
tail=moment=0
atoms=[(F(2**j),F(1,2**j),j) for j in range(1,129)]
for n in range(1,65):
    T=F(2**n)
    mu_tail=sum((mass for height,mass,j in atoms if height>T),F(0))
    assert T*mu_tail<=1
    tail+=1
    harmonic=sum((F(1,j) for j in range(1,n+1)),F(0))
    _,upper_log_n=log_bounds(F(n))
    # q_j=mu_j/(j log2); height*q_j=1/(j log2).
    actual_moment_upper=harmonic/L2
    theorem_budget=F(3,2)*(1+upper_log_n)
    assert actual_moment_upper<=theorem_budget
    moment+=1

# All prime powers obey Lambda(n)<=log n. Dyadic count plus
# 1/sqrt2<3/4 bounds the whole infinite series by sum_(k>=1)(k+1)(3/4)^k=15.
prime=0;r=F(3,4);partial=F(0)
for k in range(1,65):
    assert F(1,2**k)<r**(2*k)
    assert (k+1)*U2<k+1
    partial+=(k+1)*r**k
    exact_remaining=r**(k+1)*((k+2)/(1-r)+r/(1-r)**2)
    assert partial+exact_remaining==15
    prime+=1

def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
gamma=0
for n in range(1,65):
    t=F(n+2);ell=F(n,7)
    wp=(F(n-1,11),F(n+3,13));wm=(F(2-n,17),F(n-4,19))
    rp=(t,F(-1));rm=(-t,F(-1))
    total=mul(rp,wp)[0]*ell/2-mul(rm,wm)[0]*ell/2
    leading=t*ell*(wp[0]+wm[0])/2
    correction=ell*(wp[1]-wm[1])/2
    assert total==leading+correction
    assert abs(correction)<=ell*(abs(wp[1])+abs(wm[1]))/2
    gamma+=1
print(json.dumps({'weak_tail_checks':tail,'log_log_moment_budgets':moment,
    'complete_prime_dyadic_envelopes':prime,'two_sided_gamma_sign_checks':gamma,
    'verified_internal_pins':len(m['internal_sources']),
    'scope':'prime-bulk obstruction; actual sharp-return and F4 unproved'},indent=2))
