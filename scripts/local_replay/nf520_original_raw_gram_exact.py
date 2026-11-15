#!/usr/bin/env python3
"""NF520: source-SHA-pinned original J242 raw physical Gram on three endpoints.

All 242 true original odd generators, including the actual sinh pole.
All acceptance arithmetic is exact integer outward fixed point at 10^420.
The sin/cos and exp values have explicit analytically paid series tails;
untrusted floating point is NEVER used in source matrix construction.
"""
import argparse,hashlib,json,math,pickle,time
from fractions import Fraction as F
from pathlib import Path
S=10**420
def const(q):
    if isinstance(q,int):return (q*S,q*S)
    q=F(q);v=q*S
    return v.numerator//v.denominator,-((-v.numerator)//v.denominator)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def divint(a,n):return a[0]//n,-((-a[1])//n)
def mulint(a,n):return (a[0]*n,a[1]*n) if n>=0 else (a[1]*n,a[0]*n)
def mul(a,b):
    z=[x*y for x in a for y in b]
    return min(z)//S,-((-max(z))//S)
def div(a,b):
    assert b[0]>0 or b[1]<0
    z=[F(x*S,y) for x in a for y in b]
    lo=min(z);hi=max(z)
    return lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)
def half(a):return divint(a,2)
def pi_interval():
    def atan(q,n):
        p=sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
        e=q**(2*n+1)/F(2*n+1)
        return (p,p+e) if n%2==0 else (p-e,p)
    a=atan(F(1,5),350);b=atan(F(1,239),350)
    lo=16*a[0]-4*b[1];hi=16*a[1]-4*b[0]
    assert hi-lo<F(1,10**450)
    return const(lo)[0],const(hi)[1]
PI=pi_interval()
def reduce(q):
    q=F(q);k=(q+1)//2
    z=q-2*k
    assert -1<=z<=1
    return z
def sincos(q):
    # sin/cos(pi*q): exact rational phase reduction before Taylor.
    y=mul(const(reduce(q)),PI)
    mid=(y[0]+y[1])//2
    assert y[1]-y[0]<=5 and abs(mid)<4*S
    ysq=mid*mid//S
    sn=mid;st=mid;cs=S;ct=S
    for k in range(1,161):
        st=-(st*ysq//(S*(2*k)*(2*k+1)));sn+=st
        ct=-(ct*ysq//(S*(2*k-1)*(2*k)));cs+=ct
    # Taylor remainder <4^323/323!<1e-470; 161 terms,
    # integer rounding and phase error together <1e-410.
    # Per-step quantization error <100 fixed-point units:
    # sum of propagated magnitudes < 161*100*exp(4)+5 <10^10.
    assert F(4)**323/math.factorial(323)<F(1,10**470)
    assert 161*100*55+5<10**10
    E=10**10
    return (sn-E,sn+E),(cs-E,cs+E)
def expint(q):
    q=F(q);assert abs(q)<=F(6,5)
    z=const(q);assert z[1]-z[0]<=1
    x=(z[0]+z[1])//2;term=total=S
    for k in range(1,301):
        term=(term*x)//(S*k)
        total+=term
    assert F(3)*F(6,5)**301/math.factorial(301)<F(1,10**570)
    # 300 floor roundings amplified by exp(1.2)<4,
    # coefficient rounding <=1/S and tail <1e-570:
    # 10^10 units is a conservative absolute enclosure.
    E=10**10
    return total-E,total+E
def moment_table(f,b):
    f=F(f);b=F(b)
    if not f:
        return [(const(2*b**(n+1)/F(n+1)) if n%2==0 else (0,0))
                for n in range(27)],[(0,0)]*27
    sn,cs=sincos(2*f*b)
    omega=mulint(mul(const(f),PI),2)
    C=[(0,0)]*27;T=[(0,0)]*27
    C[0]=div(mulint(sn,2),omega)
    for n in range(1,27):
        bp=const(b**n)
        if n%2:
            T[n]=div(add(neg(mulint(mul(bp,cs),2)),
                         mulint(C[n-1],n)),omega)
        else:
            C[n]=div(sub(mulint(mul(bp,sn),2),
                         mulint(T[n-1],n)),omega)
    return C,T
def complexsub(a,b):return sub(a[0],b[0]),sub(a[1],b[1])
def complexdiv(a,z):
    d=add(mul(z[0],z[0]),mul(z[1],z[1]))
    return (div(add(mul(a[0],z[0]),mul(a[1],z[1])),d),
            div(sub(mul(a[1],z[0]),mul(a[0],z[1])),d))
def pole_moments(f,b):
    f=F(f);b=F(b)
    sn,cs=sincos(2*f*b)
    ep=expint(b/2);em=expint(-b/2)
    pplus=(mul(ep,cs),mul(ep,sn))
    mplus=(mul(em,cs),neg(mul(em,sn)))
    pminus=(mul(em,cs),mul(em,sn))
    mminus=(mul(ep,cs),neg(mul(ep,sn)))
    wi=mulint(mul(const(f),PI),2)
    def moments(z,ep,em):
        a=[complexdiv(complexsub(ep,em),z)]
        for k in range(1,14):
            bk=const(b**k)
            edge=complexsub((mul(bk,ep[0]),mul(bk,ep[1])),
                  (mulint(mul(bk,em[0]),(-1)**k),
                   mulint(mul(bk,em[1]),(-1)**k)))
            edge=complexdiv(edge,z)
            prev=complexdiv((mulint(a[-1][0],k),
                             mulint(a[-1][1],k)),z)
            a.append(complexsub(edge,prev))
        return a
    plus=moments((const(F(1,2)),wi),pplus,mplus)
    minus=moments((const(F(-1,2)),wi),pminus,mminus)
    return [complexsub(plus[k],minus[k]) for k in range(14)]
def gram_at(b,nodes):
    t=time.time();fs=sorted(set(F(f) for f,k in nodes if f!='pole'))
    freq=sorted(set(abs(a-c) for a in fs for c in fs)
                |set(a+c for a in fs for c in fs))
    ms={f:moment_table(f,b) for f in freq}
    pc={f:pole_moments(f,b) for f in fs}
    pole=sub(half(sub(expint(b),expint(-b))),const(b))
    out=[]
    for i,(fi,k) in enumerate(nodes):
        row=[]
        for j,(fj,l) in enumerate(nodes[:i+1]):
            if fi=='pole' and fj=='pole':v=pole
            elif fi=='pole' or fj=='pole':
                f=F(fj) if fi=='pole' else F(fi)
                order=l if fi=='pole' else k
                v=half(pc[f][order][1] if order%2==0 else pc[f][order][0])
            else:
                f,g=F(fi),F(fj);d=abs(f-g);u=f+g;p=k+l
                if k%2==l%2==0:
                    v=half(sub(ms[d][0][p],ms[u][0][p]))
                elif k%2 and l%2:
                    v=half(add(ms[d][0][p],ms[u][0][p]))
                elif k%2==0:
                    v=half(add(ms[u][1][p],
                      mulint(ms[d][1][p],1 if f>=g else -1)))
                else:
                    v=half(add(ms[u][1][p],
                      mulint(ms[d][1][p],1 if g>=f else -1)))
            row.append(v)
        out.append(row)
    print('Original 242D source Gram b',b,'complete in',
          round(time.time()-t,1),'s',flush=True)
    return out
SOURCE_SHA='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf505',required=True);p.add_argument('--workdir',required=True)
    a=p.parse_args();root=Path(a.workdir);root.mkdir(parents=True,exist_ok=True)
    raw=Path(a.nf505).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SOURCE_SHA
    j=json.loads(raw)
    assert j['pass']=='NF504-native' and j['original_selected_J_dimension']==242
    assert j['original_original_D_frame_SHA256']=='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
    assert j['source_original_NF407_sha256']==SRC
    assert j['source_original_NF406_sha256']==SEAM
    nodes=j['original_source_basis_nodes']
    assert len(nodes)==242 and nodes[-1]==['pole',None]
    data={'pass':'NF520-original-source-exact-physical-gram-oracle',
          'nf505_raw_sha256':SOURCE_SHA,'nf407_source_sha256':SRC,
          'nf406_source_sha256':SEAM,'old_full_selected_dimension':242,
          'scale':str(S),'Gram':{}}
    bo=F(549,500);h=bo/4096
    for k in (0,1,2):
        g=gram_at(bo-k*h,nodes)
        pth=root/f'G{k}_oracle.pkl'
        pth.write_bytes(pickle.dumps(g,protocol=4))
        width=max(y-x for row in g for x,y in row)
        assert width<S//10**400
        data['Gram'][str(k)]={
          'true_positive_endpoint':str(bo-k*h),
          'original_source_interval_file_sha256':
             hashlib.sha256(pth.read_bytes()).hexdigest(),
          'max_raw_Gram_interval_width_as_fraction':str(F(width,S))}
    (root/'nf520_original_gram_custody.json').write_text(
       json.dumps(data,indent=2)+'\n')
    print('NF520 true original 242D raw Gram 3 endpoints SOURCE-EXACT PASS')
if __name__=='__main__':main()
