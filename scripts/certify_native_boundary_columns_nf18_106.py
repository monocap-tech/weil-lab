#!/usr/bin/env python3
"""NF18: complete original native mixed E112 x {e112,e113} source rows.

Uses SAME exact kernel, digamma, six-prime and signed-pole arithmetic
as NF17, but only 114 genuinely new normalized Legendre mixed/diagonal
entries. Does not evaluate complete F112 inverse or prove whole sign.
Requires original E112 archive and its exact immutable SHA.
"""
import argparse,time,json,gzip,pathlib,hashlib
from fractions import Fraction as F
from math import factorial
import certify_native_low112_nf17_106 as n

PARENT_SHA='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
A=n.A;N=n.N;K=n.K

def build(old112):
    t=time.monotonic()
    with gzip.open(old112,'rb') as f: raw=f.read()
    assert hashlib.sha256(raw).hexdigest()==PARENT_SHA
    old=json.loads(raw)
    assert old['aperture']=='53/50' and old['dim']==112
    assert len(old['complete_form'])==3192
    L=4*A;B=n.bern(2*K+2)
    pi=16*n.atan(F(1,5))-4*n.atan(F(1,239))
    g=n.I(sum((F(1,k) for k in range(1,101)),F(0))-F(1,200))-n.log(100,terms=270)
    for k in range(1,21):g+=B[2*k]/F(2*k*100**(2*k))
    e=abs(B[42])/F(42*100**42);g+=n.I(-e,e)
    e1=sum(((-L)**k/factorial(k) for k in range(N+1)),F(0))
    ee=F(70)*L**(N+1)/factorial(N+1)
    constant=-g-n.logI(pi)-n.logI(n.I(1-e1-ee,1-e1+ee))
    ker=[F(0)]*(2*K+1);ker[0]=1;ker[1]=L/2
    for k in range(1,K+1):ker[2*k]=B[2*k]*L**(2*k)/factorial(2*k)
    kerr=4*(L/6)**(2*K+2)/(1-(L/6)**2)
    fn=n.make_integrator(ker,[(-L/4)**k/factorial(k) for k in range(N+1)],2*113+4)
    exp=[(A/2)**k/factorial(k) for k in range(N+1)]
    poles=[]
    for i in range(114):
        p=n.P(i);pr=n.mul(p,exp)
        value=A*sum((2*c/F(k+1) for k,c in enumerate(pr) if k%2==0),F(0))
        error=4*A*sum(map(abs,p))*(A/2)**(N+1)/factorial(N+1)
        poles.append(n.I(value-error,value+error))
    powers=(2,3,4,5,7,8)
    logs={m:n.log(m) for m in powers}
    coeffs={m:(logs[2] if m in (4,8) else logs[m])/n.sq(m) for m in powers}
    out={}
    for j in (112,113):
        for i in range(j+1):
            if (i+j)%2:continue
            c=[A*x*2**k for k,x in enumerate(n.corr(n.P(i),n.P(j)))]
            delta=F(2*A,2*i+1) if i==j else F(0)
            assert c[0]==delta
            integral=fn(c,delta);csum=sum(map(abs,c))
            exp_err=70*L**(N+1)/factorial(N+1)*(delta+csum/F(4**(N+1)))
            ab=F(3,4)*L*delta+sum(map(abs,c[1:]))
            err=F(53,10)*exp_err+ab*kerr
            arch=delta*constant+n.I(integral-err,integral+err)
            pole=(int((-1)**i)+int((-1)**j))*poles[i]*poles[j]
            prime=n.I(0)
            for m in powers:
                q=logs[m]/n.I(2*A);v=n.I(0)
                for k in reversed(c):v=v*q+k
                prime+=2*coeffs[m]*v
            norm=n.sq((2*i+1)*(2*j+1))/n.I(2*A)
            channels={'arch':norm*arch,'pole':norm*pole,
                      'prime':-norm*prime,'full':norm*(arch+pole-prime)}
            out[f'{i},{j}']={kind:[str(x.lo),str(x.hi)] for kind,x in channels.items()}
    assert len(out)==114
    payload=dict(aperture='53/50',parent_sha256=PARENT_SHA,
                 basis='physical-normalized Legendre',new_columns=[112,113],
                 original_full_source=out,
                 truncation={'N':N,'K':K,'grid_digits':280})
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    return raw,round(time.monotonic()-t,2)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('original_e112_json_gz')
    p.add_argument('--output',required=True)
    a=p.parse_args()
    raw,secs=build(a.original_e112_json_gz)
    pathlib.Path(a.output).write_bytes(gzip.compress(raw,mtime=0))
    print(json.dumps(dict(status='COMPLETE 114 signed mixed/diagonal intervals',
        sha256=hashlib.sha256(raw).hexdigest(),seconds=secs,
        output=a.output,whole_aperture_positive=False),indent=2))
