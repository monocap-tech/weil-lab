#!/usr/bin/env python3
"""Integer fixed-point NF592 arithmetic, cached NF617 residual table replay.
All radii are outward; this is external numerical evidence, not a Lean proof.
"""
import argparse, gzip, json, re, time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from math import factorial

Q=10**2600
N=1200
M=2000
ZERO=(0,0); ONE=(Q,0)

def ceildiv(a,b):
    assert b>0
    return -((-a)//b)
def exact(q):
    q=F(q); m,r=divmod(q.numerator*Q,q.denominator)
    return (m,int(r!=0))
def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[0],a[1]
def mul(a,b):
    m,r=a; n,s=b
    return m*n//Q,ceildiv(abs(m)*s+abs(n)*r+r*s,Q)+1
def div(a,k): return a[0]//k,ceildiv(a[1],k)+1
def real(q): return exact(q),ZERO
def zadd(a,b): return add(a[0],b[0]),add(a[1],b[1])
def zneg(a): return neg(a[0]),neg(a[1])
def zmul(a,b): return add(mul(a[0],b[0]),neg(mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0])))
def small(z):
    s=(ZERO,ZERO); t=(ONE,ZERO)
    for n in range(N):
        s=zadd(s,t)
        if n+1<N:
            u=zmul(t,z); t=div(u[0],n+1),div(u[1],n+1)
    return tuple((m,r+1) for m,r in s)
def atan(p):
    b=ZERO; power=p
    for n in range(M):
        b=add(b,exact(F((-1)**n,power*(2*n+1))))
        power*=p*p
    return b[0],b[1]+1
@lru_cache(maxsize=1)
def pi(): return add(mul(exact(16),atan(5)),neg(mul(exact(4),atan(239)))
def reduced(f):
    u=f*F(11,10); return u-(u+F(1,2))//1
def phase(f): return phase_reduced(reduced(f))
@lru_cache(maxsize=1280)
def phase_reduced(u):
    a=small((ZERO,mul(pi(),exact(u/2))))
    b=zmul(a,a); return zmul(b,b)
@lru_cache(maxsize=5)
def real_exp(h):
    a=small(real(h*F(11,20))); return zmul(a,a)
def endpoint(h,f): return zmul(real_exp(h),phase(f))
def upper(a): return sum(abs(m)+r for m,r in a)

def canonical(h,f): return (-h,-f) if f<0 or (f==0 and h<0) else (h,f)

def inventory(root):
    src=root/'WeilDefect/Arithmetic'
    sig=(src/'ActualZetaOriginalJ242ExponentialSignature.lean').read_text()
    data=(src/'ActualZetaOriginalNF407FrozenData.lean').read_text()
    groups=[(F(f),int(m)-1) for f,m in re.findall(r'\(\((\d+(?:/\d+)?)\s*:\s*ℚ\),\s*(\d+)\)',sig)]
    freq=data.split('def neutralNF587CriticalFrequencies',1)[1].split(']',1)[0]
    crit=[(F(f),0) for f in re.findall(r'\((\d+(?:/\d+)?)\)',freq)]
    assert len(groups)==67 and len(crit)==32
    assert sum(n+1 for _,n in groups)==241
    def terms(g): return [(F(0),s*f,n) for f,n in g for s in (-1,1)]+[(F(s,2),F(0),0) for s in (-1,1)]
    S,C=terms(groups),terms(crit); raw={}; keys={}
    for T in (S,C):
        for h,f,n in S:
            for j,g,m in T:
                k=h+j,f+g; raw[k]=max(raw.get(k,0),n+m)
                k=canonical(*k); keys[k]=max(keys.get(k,0),n+m)
    assert len(raw)==15671 and len(keys)==7836
    assert sum(n+1 for n in raw.values())==76015
    assert sum(n+1 for n in keys.values())==38021
    print('source schedule:',len(raw),'signed keys,',len(keys),'canonical keys,',sum(n+1 for n in keys.values()),'rows',flush=True)
    phases={reduced(f) for h,f in raw}
    assert len(phases)==1276
    print('distinct reduced phases:',len(phases),flush=True)
    return keys

def table(h,f,K):
    assert abs(h)<=1 and (h or f)
    d=max(abs(h),6*abs(f)); z=exact(h),mul(pi(),exact(2*f)); pos=endpoint(h,f); negend=endpoint(-h,-f)
    zr,zi=z[0][0],z[1][0]; den=zr*zr+zi*zi; assert den
    prev=(0,0); prevR=0; rows=[]
    for n in range(K+1):
        b=zadd(zmul(real(F(11,10)**n),pos),zneg(zmul(real(F(-11,10)**n),negend)))
        ar=b[0][0]-n*prev[0]; ai=b[1][0]-n*prev[1]
        x=(ar*zr+ai*zi)*Q//den; y=(ai*zr-ar*zi)*Q//den
        q=((x,0),(y,0))
        r=zadd(b,zneg(zmul(z,q)))
        if n: r=zadd(r,zneg(zmul(real(n),((prev[0],0),(prev[1],0)))))
        fee=upper(r)+n*prevR
        R=ceildiv(fee*d.denominator,d.numerator)+1
        assert fee*d.denominator<=R*d.numerator
        rows.append((x,y,R)); prev=(x,y); prevR=R
    return rows

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path); ap.add_argument('--output',type=Path); ap.add_argument('--shard',help='index/count of complete canonical nonzero key inventory'); args=ap.parse_args()
    assert 2*Q<=factorial(N) and all(Q<=p**(2*M+1)*(2*M+1) for p in (5,239))
    cases=[(F(0),F(37,32),26),(F(1,2),F(37,64),13),(F(0),F(7,704),3)]
    if args.root:
        keys=inventory(args.root)
        assert all(keys[(h,f)]==n for h,f,n in cases)
    if args.shard:
        assert args.root and args.output
        i,k=map(int,args.shard.split('/')); assert 0<=i<k
        cases=sorted((h,f,n) for (h,f),n in keys.items() if h or f)[i::k]
    data=[]; t=time.monotonic()
    for h,f,n in cases:
        rows=table(h,f,n); maxR=max(r for _,_,r in rows)
        print(f'key=({h},{f}) degrees 0..{n}: {len(rows)} payments PASS; max radius < 10^{len(str(maxR))-2600}',flush=True)
        data.append({'h':str(h),'f':str(f),'rows':[[str(x),str(y),str(r)] for x,y,r in rows]})
    print(f'{sum(len(k["rows"]) for k in data)} rows PASS; {time.monotonic()-t:.2f}s',flush=True)
    if args.output:
        with gzip.open(args.output,'wt') as out: json.dump({'scale':'10^2600','exp_terms':N,'atan_terms':M,'evidence':'external exact integer replay','tables':data},out)
if __name__=='__main__': main()
