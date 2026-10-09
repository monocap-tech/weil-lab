#!/usr/bin/env python3
"""NF24: exact original native source projections beyond compensated H2.
Only new offdiagonal entries against the 58 input modes are generated.
Their squares give Bessel lower bounds, not an inverse-response upper.
"""
from fractions import Fraction as F
from math import factorial
import argparse,json,hashlib,time
import certify_native_low112_nf17_106 as n

def pole_moment(i):
    # Rodrigues + n integrations by parts gives
    # int_-a^a exp(x/2) P_i(x/a) dx
    # =2a sum_k (a/2)^(i+2k)/(2^k k! (2i+2k+1)!!).
    z=n.A/2;odd=1
    for j in range(1,2*i+2,2):odd*=j
    term=z**i/F(odd);total=term
    for k in range(1,81):
        term*=z*z/F(2*k*(2*i+2*k+1));total+=term
    nextterm=term*z*z/F(2*81*(2*i+163))
    # Subsequent positive term ratios are <1/2.
    assert z*z/F(2*82*(2*i+165))<F(1,2)
    return n.I(2*n.A*total,2*n.A*(total+2*nextterm))

def build(high):
    t=time.monotonic();A=n.A;L=4*A;N=n.N;K=n.K
    assert all(h>=116 for h in high)
    B=n.bern(2*K+2)
    ker=[F(0)]*(2*K+1);ker[0]=1;ker[1]=L/2
    for k in range(1,K+1):ker[2*k]=B[2*k]*L**(2*k)/factorial(2*k)
    kerr=4*(L/6)**(2*K+2)/(1-(L/6)**2)
    fn=n.make_integrator(ker,[(-L/4)**k/factorial(k) for k in range(N+1)],max(high)+114+4)
    powers=(2,3,4,5,7,8);logs={m:n.log(m) for m in powers}
    weights={m:(logs[2] if m in (4,8) else logs[m])/n.sq(m) for m in powers}
    out={}
    for j in high:
        for i in range(j%2,116,2):
            c=[A*x*2**k for k,x in enumerate(n.corr(n.P(i),n.P(j)))]
            assert c[0]==0
            integral=fn(c,F(0));csum=sum(map(abs,c))
            exp_err=70*L**(N+1)/factorial(N+1)*csum/F(4**(N+1))
            err=F(53,10)*exp_err+sum(map(abs,c[1:]))*kerr
            arch=n.I(integral-err,integral+err)
            pole=2*(-1)**i*pole_moment(i)*pole_moment(j)
            prime=n.I(0)
            for m in powers:
                q=logs[m]/n.I(2*A);v=n.I(0)
                for k in reversed(c):v=v*q+k
                prime+=2*weights[m]*v
            norm=n.sq((2*i+1)*(2*j+1))/n.I(2*A)
            terms={'arch':norm*arch,'prime':-norm*prime,'pole':norm*pole,'full':norm*(arch-prime+pole)}
            out[f'{i},{j}']={k:[str(v.lo),str(v.hi)] for k,v in terms.items()}
        print('completed original source projection column',j,flush=True)
    print('elapsed seconds',round(time.monotonic()-t,2),flush=True)
    return dict(milestone='NF24',aperture='53/50',projection_degrees=high,
        complete_original_signed_source=out,N=N,K=K,grid_digits=280,
        whole_aperture_positive=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--high',type=int,nargs='+',required=True);p.add_argument('--output',required=True)
    a=p.parse_args();raw=json.dumps(build(a.high),sort_keys=True,separators=(',',':')).encode()
    open(a.output,'wb').write(raw)
    print('source SHA256',hashlib.sha256(raw).hexdigest(),flush=True)
