#!/usr/bin/env python3
"""NF25: outward rational moments of the original three directional sources.
Preserves endpoint logs, all translation cells and signed poles. Constructs
the joint Gram of r=P_F Lp and G_j=P_F Lphi_j using the NF24 fixed target.
Arch kernel degree320 and pole degree40 errors are paid by the validator.
"""
from fractions import Fraction as F
from math import comb,factorial,isqrt
from functools import lru_cache
import argparse,json,gzip,time,hashlib
import certify_native_arch_source_uniform_nf22_106 as kernel
import certify_native_low112_nf17_106 as native

SCALE=10**280
class I:
    def __init__(self,a,b=None):
        if isinstance(a,I):self.l,self.h=a.l,a.h;return
        a=F(a);b=F(a if b is None else b)
        assert a<=b
        self.l=(a*SCALE).__floor__();self.h=(b*SCALE).__ceil__()
    @classmethod
    def raw(cls,l,h):
        q=cls.__new__(cls);q.l=l;q.h=h;assert l<=h;return q
    def __add__(self,b):
        b=iv(b);return I.raw(self.l+b.l,self.h+b.h)
    __radd__=__add__
    def __neg__(self):return I.raw(-self.h,-self.l)
    def __sub__(self,b):return self+-iv(b)
    def __rsub__(self,b):return iv(b)+-self
    def __mul__(self,b):
        b=iv(b);p=[self.l*b.l,self.l*b.h,self.h*b.l,self.h*b.h]
        return I.raw(min(p)//SCALE,-((-max(p))//SCALE))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=iv(b);assert b.l>0 or b.h<0
        z=SCALE*SCALE
        return self*I.raw(z//b.h,-((-z)//b.l))
    def __pow__(self,k):
        assert k>=0
        ans=I(1);v=self
        while k:
            if k%2:ans=ans*v
            k//=2
            if k:v=v*v
        return ans
    def ends(self):return [str(F(self.l,SCALE)),str(F(self.h,SCALE))]
    def absupper(self):return F(max(abs(self.l),abs(self.h)),SCALE)
    def mid(self):return F(self.l+self.h,2*SCALE)

def iv(v):return v if isinstance(v,I) else I(v)
def ni(v):return I(v.lo,v.hi)
def sq(v):
    v=iv(v)
    lo=0 if v.l<=0<=v.h else min(v.l*v.l,v.h*v.h)
    hi=max(v.l*v.l,v.h*v.h)
    return I.raw(lo//SCALE,-((-hi)//SCALE))
def sqrt_r(q):
    q=F(q);assert q>=0
    k=isqrt((q*SCALE*SCALE).__floor__())
    return I.raw(k,k+1)
@lru_cache(None)
def log2i():return log_unit(I(2))
def log_unit(q):
    z=(q-1)/(q+1);assert z.absupper()<F(1,2)
    power=z;total=I(0)
    for k in range(500):total=total+2*power/F(2*k+1);power=power*z*z
    # Bound the entire remaining atanh series, including power rounding.
    za=z.absupper();rem=2*power.absupper()/F(1001)/(1-za*za)
    return total+I(-rem,rem)
def logi(q):
    q=iv(q);assert q.l>0
    k=0
    while q.l>=2*SCALE:q=q/2;k+=1
    while q.l<SCALE:q=q*2;k-=1
    return log_unit(q)+k*log2i()

A=F(53,50);N=320
def trim(p):
    while len(p)>1 and p[-1].l==p[-1].h==0:p.pop()
    return p
def add(p,q):
    r=[I(0)]*max(len(p),len(q))
    for k,v in enumerate(p):r[k]=r[k]+v
    for k,v in enumerate(q):r[k]=r[k]+v
    return trim(r)
def scale(p,c):return [c*v for v in p]
def product(p,q):
    out=[I(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        if x.l or x.h:
            for j,y in enumerate(q):
                if y.l or y.h:out[i+j]=out[i+j]+x*y
    return trim(out)

@lru_cache(None)
def basis(n):
    norm=sqrt_r(F(2*n+1)/(2*A))
    return [norm*(v/A**k) for k,v in enumerate(native.P(n))]
def physical(ids,coeff):
    ans=[I(0)]
    for n,v in zip(ids,coeff):ans=add(ans,scale(basis(n),F(v)))
    return ans

def constants():
    pi=ni(16*native.atan(F(1,5))-4*native.atan(F(1,239)))
    B=native.bern(202)
    gamma=I(sum((F(1,k) for k in range(1,101)),F(0))-F(1,200))-ni(native.log(100))
    for k in range(1,101):gamma=gamma+B[2*k]/F(2*k*100**(2*k))
    rem=abs(B[202])/F(202*100**202)
    gamma=gamma+I(-rem,rem)
    return -gamma-logi(2*pi),pi

def singular(p):
    out=[I(0)]*len(p)
    for m,v in enumerate(p):
        if not(v.l or v.h):continue
        out[m]=out[m]+v*sum((F(1,k) for k in range(1,m+1)),F(0))
        for j in range(1,m,2):out[m-1-j]=out[m-1-j]-v*A**(j+1)/F(j+1)
    return out

def convolution(p):
    # Endpoint Taylor coefficients, then beta-integrated regular kernel.
    d=len(p)-1;h=[I(v) for v in kernel.kernel_coefficients(N)]
    left=[];right=[]
    for k in range(d+1):
        left.append(sum((p[m]*F(comb(m,k))*(-A)**(m-k) for m in range(k,d+1)),I(0)))
        right.append(sum((p[m]*F(comb(m,k))*A**(m-k)*(-1)**k for m in range(k,d+1)),I(0)))
    lc=[I(0)]*(N+d+1);rc=lc[:]
    for l in range(1,N+1):
        beta=F(1,l)
        for k in range(d+1):
            if k:beta*=F(k,l+k)
            lc[l+k]=lc[l+k]+h[l]*beta*left[k]
            rc[l+k]=rc[l+k]+h[l]*beta*right[k]
    out=[I(0)]*(N+d+1)
    for n in range(1,len(lc)):
        for j in range(n+1):
            out[j]=out[j]+(lc[n]+(-1)**j*rc[n])*F(comb(n,j))*A**(n-j)
    return trim(out)

def pole_moment(n):
    z=A/2;den=1
    for j in range(1,2*n+2,2):den*=j
    term=z**n/F(den);total=term
    for k in range(1,101):term*=z*z/F(2*k*(2*n+2*k+1));total+=term
    nxt=term*z*z/F(2*101*(2*n+203))
    return I(2*A*total,2*A*(total+2*nxt))

def shifted(p,t):
    powers=[I(1)]
    for k in range(1,len(p)):powers.append(powers[-1]*t)
    out=[I(0)]*len(p)
    for m,v in enumerate(p):
        if v.l or v.h:
            for k in range(m+1):out[k]=out[k]+v*F(comb(m,k))*powers[m-k]
    return out

@lru_cache(None)
def mass(n):return F(0) if n%2 else 2*A**(n+1)/F(n+1)
@lru_cache(None)
def harmonic(m):return sum((F(1,2*k-1) for k in range(1,m+2)),F(0))
@lru_cache(None)
def harmonic2(m):return sum((F(1,(2*k-1)**2) for k in range(1,m+2)),F(0))

def dot(p,q,mom):
    ans=I(0)
    for k,v in enumerate(product(p,q)):
        if v.l or v.h:ans=ans+v*mom[k]
    return ans

def moments(cuts,maxdeg,c,pi):
    Z=ni(native.log(2*A))
    M=[I(mass(n)) for n in range(maxdeg+1)]
    ML=[I(0) if n%2 else 2*mass(n)*(Z-harmonic(n//2)) for n in range(maxdeg+1)]
    ML2=[I(0) if n%2 else mass(n)*(4*sq(Z-harmonic(n//2))-sq(pi)/3+4*harmonic2(n//2)) for n in range(maxdeg+1)]
    allcell=[]
    for L,U in zip(cuts,cuts[1:]):
        # Exact polynomial antiderivatives and stable endpoint log primitive.
        mp=[];ml=[]
        def primitives(x):
            xp=[I(1)]
            for k in range(1,maxdeg+3):xp.append(xp[-1]*x)
            lp=None if x.l==x.h==int(-A*SCALE) else logi(I(A)+x)
            lm=None if x.l==x.h==int(A*SCALE) else logi(I(A)-x)
            vals=[];sums=[]
            for n in range(maxdeg+1):
                v=I(0)
                if n%2==0:
                    cp=xp[n+1]+A**(n+1);cm=xp[n+1]-A**(n+1)
                    if lp is not None:v=v+cp*lp
                    # At x=-a the exact coefficient x^(n+1)+a^(n+1)
                    # is zero; use that algebraic endpoint cancellation.
                    if lm is not None:v=v+cm*lm
                    # At x=a the exact coefficient x^(n+1)-a^(n+1)
                    # is zero, despite outward power rounding.
                else:
                    factor=xp[n+1]-A**(n+1)
                    if lp is not None and lm is not None:v=v+factor*(lp+lm)
                    # At either endpoint n+1 is even and this exact
                    # coefficient vanishes. The continuous limit is zero.
                subtotal=xp[n+1]/F(n+1)
                if n>=2:subtotal=subtotal+A*A*sums[n-2]
                sums.append(subtotal)
                v=v-2*subtotal
                vals.append(v/F(n+1))
            return xp,vals
        xl,vl=primitives(L);xu,vu=primitives(U)
        for n in range(maxdeg+1):mp.append((xu[n+1]-xl[n+1])/F(n+1));ml.append(vu[n]-vl[n])
        allcell.append((mp,ml))
    return M,ML,ML2,allcell

def gram_for(row,source):
    c,pi=constants();ids=row['retained_indices']+row['high_indices'];vs=row['retained_coefficients']+row['exact_rational_high_compensation']
    inputs=[(ids,vs),([row['high_indices'][0]],['1']),([row['high_indices'][1]],['1'])]
    lowids=row['retained_indices'];projection=[];proj_error=[]
    for col in range(3):
        if col==0:intervals=[I(*map(F,p)) for p in row['low_source_coordinates']]
        else:
            h=row['high_indices'][col-1]
            intervals=[I(*map(F,source[f'{i},{h}']['full'])) for i in lowids]
        centers=[z.mid() for z in intervals]
        projection.append(physical(lowids,centers))
        # sqrt(56)<8; midpoint projection centers are fixed rationals.
        proj_error.append(8*max(F(z.h-z.l,2*SCALE) for z in intervals))
    poly=[];logpoly=[];physical_inputs=[]
    parity=row['parity'];start=0 if parity=='even' else 1
    for col,(ii,vv) in enumerate(inputs):
        p=physical(ii,vv);physical_inputs.append(p)
        regular=add(scale(p,c),add(singular(p),scale(convolution(p),-1)))
        m=sum((F(v)*sqrt_r(F(2*i+1)/(2*A))*pole_moment(i) for i,v in zip(ii,vv)),I(0))
        pole=[I(0)]*41
        for k in range(start,41,2):pole[k]=2*(-1)**start*m/F(2**k*factorial(k))
        poly.append(add(add(regular,pole),scale(projection[col],-1)))
        logpoly.append(scale(p,F(-1,2)))
        print(parity,'constructed source',col,flush=True)
    powers=(2,3,4,5,7,8)
    logs={n:ni(native.log(n)) for n in powers}
    weights={n:(logs[2] if n in (4,8) else logs[n])/sqrt_r(F(n)) for n in powers}
    shifts=[(s*logs[n],weights[n]) for n in powers for s in (1,-1)]
    cuts=[I(-A),I(A)]+[I(A)-t if t.l>0 else I(-A)-t for t,w in shifts]
    cuts.sort(key=lambda v:v.l)
    assert all(l.h<u.l for l,u in zip(cuts,cuts[1:]))
    maxdeg=2*max(len(p)-1 for p in poly)
    M,ML,ML2,cm=moments(cuts,maxdeg,c,pi)
    shifted_inputs=[[scale(shifted(p,t),-w) for t,w in shifts] for p in physical_inputs]
    gram=[[I(0) for j in range(3)] for i in range(3)]
    native_checks=[]
    # Independently reproduce the actual original measured source pairings.
    # These tests use unsquared source moments, not the Gram identity.
    for col in range(3):
        for jj,test_id in enumerate(row['high_indices']):
            test=basis(test_id)
            pairing=dot(poly[col],test,M)+dot(logpoly[col],test,ML)
            for cell,(L,U) in enumerate(zip(cuts,cuts[1:])):
                mid=F(L.h+U.l,2*SCALE);prime=[I(0)]
                for kk,(t,w) in enumerate(shifts):
                    value=I(mid)+t
                    if -A<F(value.l,SCALE) and F(value.h,SCALE)<A:prime=add(prime,shifted_inputs[col][kk])
                pairing=pairing+dot(prime,test,cm[cell][0])
            if col==0:expected=I(*map(F,row['measured_high_source_coordinates'][jj]))
            else:
                a_id=row['high_indices'][col-1]
                expected=I(*map(F,source[f'{min(a_id,test_id)},{max(a_id,test_id)}']['full']))
            massbound=F(1001,1000) if col==0 else F(1)
            epsilon=4*F(106,125)**320/(1-F(106,125))
            er=massbound*(2*A*epsilon+16*(A/2)**41/F(factorial(41)))+proj_error[col]
            enlarged_pair=pairing+I(-er,er)
            assert enlarged_pair.l<=expected.h and enlarged_pair.h>=expected.l
            native_checks.append(dict(source_column=col,test_degree=test_id,
                reconstructed_pairing=pairing.ends(),original_pairing=expected.ends(),paid_L2_error=str(er)))
    for i in range(3):
        for j in range(i,3):
            val=dot(poly[i],poly[j],M)+dot(poly[i],logpoly[j],ML)+dot(logpoly[i],poly[j],ML)+dot(logpoly[i],logpoly[j],ML2)
            for cell,(L,U) in enumerate(zip(cuts,cuts[1:])):
                mid=F(L.h+U.l,2*SCALE)
                active=[]
                for k,(t,w) in enumerate(shifts):
                    shifted_mid=I(mid)+t
                    inside=(-A<F(shifted_mid.l,SCALE) and F(shifted_mid.h,SCALE)<A)
                    outside=(F(shifted_mid.h,SCALE)<-A or F(shifted_mid.l,SCALE)>A)
                    assert inside or outside
                    if inside:active.append(k)
                prime=[]
                for col in (i,j):
                    p=[I(0)]
                    for k in active:p=add(p,shifted_inputs[col][k])
                    prime.append(p)
                mp,ml=cm[cell]
                val=val+dot(poly[i],prime[1],mp)+dot(prime[0],poly[j],mp)+dot(prime[0],prime[1],mp)+dot(logpoly[i],prime[1],ml)+dot(prime[0],logpoly[j],ml)
            gram[i][j]=gram[j][i]=val
            print(parity,'integrated Gram',i,j,flush=True)
    return gram,proj_error,native_checks

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('targets');p.add_argument('e112');p.add_argument('first');p.add_argument('second');p.add_argument('--output',required=True);a=p.parse_args()
    traw=open(a.targets,'rb').read()
    assert hashlib.sha256(traw).hexdigest()=='6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00'
    targets=json.loads(traw);src={}
    hashes=['f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81','da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee','0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad']
    for (f,k),sha in zip([(a.e112,'complete_form'),(a.first,'original_full_source'),(a.second,'original_full_source')],hashes):
        raw=gzip.decompress(open(f,'rb').read());assert hashlib.sha256(raw).hexdigest()==sha
        src.update(json.loads(raw)[k])
    out=dict(milestone='NF25',aperture='53/50',regular_kernel_degree=N,interval_grid_digits=280,approximate_Gram_only=True,parities=[])
    for row in targets['authenticated_compensated_targets']:
        g,e,checks=gram_for(row,src)
        out['parities'].append(dict(parity=row['parity'],reconstructed_three_source_Gram=[[v.ends() for v in line] for line in g],projection_center_L2_errors=list(map(str,e)),independent_original_native_pairing_checks=checks))
        open(a.output,'w').write(json.dumps(out,indent=2)+'\n')
