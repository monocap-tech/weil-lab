#!/usr/bin/env python3
"""NF9: exact rational prime-8 13-panel/degree-0,1 native PRIME block.
For a=53/50 vs certified anchor 21/20. This does not rebuild arch/poles,
the 112-vector native matrix, source Gram or infinite complement.
"""
from fractions import Fraction as F
from math import isqrt
import json

def interval(lo,hi=None):
    return (F(lo),F(lo if hi is None else hi))
def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def mul(x,y):
    q=[a*b for a in x for b in y]
    return min(q),max(q)
def div(x,y):
    assert y[0]>0
    return mul(x,(1/y[1],1/y[0]))
def scale(x,a):return mul(x,interval(a))
def plus(x,y):return add(x,y)
def sub(x,y):return add(x,neg(y))
def logn(n,N=220):
    q=F(n-1,n+1);p=q;s=F(0)
    for k in range(N):
        s+=2*p/F(2*k+1)
        p*=q*q
    e=2*p/(F(2*N+1)*(1-q*q))
    return s,s+e
def sqrt_n(n):
    g=10**45;k=isqrt(n*g*g)
    return F(k,g),F(k+1,g)
def power(x,n):
    a=interval(1)
    for _ in range(n):a=mul(a,x)
    return a
def round_out(x,places=28):
    g=10**places
    return [str((x[0]*g).__floor__())+'/'+str(g),
            str(-((-x[1]*g).__floor__()))+'/'+str(g)]

LOG={n:logn(n) for n in (2,3,5,7)}
LOG[4]=scale(LOG[2],2)
LOG[8]=scale(LOG[2],3)
LOG[9]=scale(LOG[3],2)
POWERS=(2,3,4,5,7,8)
BASE={2:2,3:3,4:2,5:5,7:7,8:2}

def compute(a):
    d=2*a
    assert LOG[8][1]<d<LOG[9][0]
    shift={n:div(LOG[n],interval(d)) for n in POWERS}
    cuts=[('0',interval(0),None),('1',interval(1),None)]
    for n in POWERS:
        cuts.append((f'1-log({n})/(2a)',sub(interval(1),shift[n]),(n,+1)))
        cuts.append((f'log({n})/(2a)',shift[n],(n,-1)))
    cuts.sort(key=lambda x:sum(x[1])/2)
    assert len(cuts)==14
    assert all(x[1][1]<y[1][0] for x,y in zip(cuts,cuts[1:]))
    panels=[]
    counter=0
    for k in range(13):
        mid=interval((cuts[k][1][1]+cuts[k+1][1][0])/2)
        active=[]
        for n in POWERS:
            for sign in (-1,1):
                t=add(mid,scale(shift[n],sign))
                inside=0<t[0] and t[1]<1
                outside=t[1]<0 or t[0]>1
                assert inside or outside
                counter+=1
                if inside:active.append(f'{n}:{sign:+d}')
        panels.append(active)
    for k in range(13):
        reflected={f'{int(e.split(":")[0])}:{-int(e.split(":")[1]):+d}' for e in panels[k]}
        assert reflected==set(panels[12-k])
        counter+=1
    z0=interval(0);z1=interval(0)
    for n in POWERS:
        q=shift[n]
        c=div(LOG[BASE[n]],sqrt_n(n))
        z0=add(z0,scale(mul(c,sub(interval(1),q)),-2))
        # One normalized odd Legendre prime overlap = 1-3q+2q³.
        odd=add(sub(interval(1),scale(q,3)),scale(power(q,3),2))
        z1=add(z1,scale(mul(c,odd),-2))
    assert z0[1]<0
    return dict(a=str(a),prime_powers=list(POWERS),panels=13,
      cut_labels=[p[0] for p in cuts],
      cut_intervals=[round_out(p[1]) for p in cuts],
      active_prime_shifts=panels,
      prime_degree0=round_out(z0),prime_degree1=round_out(z1),
      prime_cross_parity='exact_zero',exact_panel_checks=counter+13,
      source_scope='full six-prime signed translation block in normalized physical Legendre degrees 0,1 only')

def parse(z):return tuple(map(F,z))
def certificate():
    new=compute(F(53,50));old=compute(F(21,20))
    assert new['cut_labels']==old['cut_labels']
    assert new['active_prime_shifts']==old['active_prime_shifts']
    assert parse(new['prime_degree0'])[1]<parse(old['prime_degree0'])[0]
    assert parse(new['prime_degree1'])[0]>parse(old['prime_degree1'])[1]
    return dict(result='PASS',target=new,old_reference=dict(
      a=old['a'],prime_degree0=old['prime_degree0'],prime_degree1=old['prime_degree1']),
      exact_sign_changes={'even_prime_more_negative':True,'odd_prime_more_positive':True},
      complement_lower_certified=False,full_native_112_certified=False,
      target_original_sign_certified=False,RH_proved=False,lean_certified=False)

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
