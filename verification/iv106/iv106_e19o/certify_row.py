"""Integer-only midpoint upper enclosure of E19N cell-zero Riesz defect.
Requires NumPy only for exact int64 array arithmetic; no floating quadrature.
Analytic derivations are given in accompanying note. Run with row_pilot.json.
"""
from fractions import Fraction as F
from math import factorial,isqrt
from pathlib import Path
import json,hashlib,sys
import numpy as np
Q=16384; M=128; S=2**20; B=2**60; h=F(11,3325)
p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('row_pilot.json')
raw=p.read_bytes(); assert hashlib.sha256(raw).hexdigest()=='37b6434006b5ef0d56e990e4993517cb22a83d38541f477f2995274ebee968ae'
d=json.loads(raw); x=list(map(F,d['x'])); g=list(map(F,d['g'])); inds=d['ix']; assert len(x)==665 and inds==list(range(-64,0))+list(range(665,729)) and d['target']==0
q={0:F(1),**{i:-v for i,v in zip(inds,g)}}
assert sum(map(abs,x))<1 and sum(map(abs,q.values()))<2
assert sum(v*v for v in x)<F(243,1000)**2
assert sum(v*v for v in q.values())<F(102,100)**2
assert sum((i*v)**2 for i,v in enumerate(x))<F(462,1000)**2
assert sum((i*v)**2 for i,v in q.items())<F(535,1000)**2
assert h<F(3,50)**2 and 1/(F(271828,100000)*h)<120
assert F(3,50)*(2*(F(102,100)+4*F(243,1000))+7*(F(535,1000)+4*F(462,1000))+60*(F(102,100)+F(243,1000)))<6
# Machin pi bounds; alternating series.
def atan_bounds(z):
    a=sum((-1)**n*z**(2*n+1)/(2*n+1) for n in range(30))
    return a,a+z**61/61
al,au=atan_bounds(F(1,5));bl,bu=atan_bounds(F(1,239));pl,pu=16*al-4*bu,16*au-4*bl
assert 3<pl<pu<F(22,7)
# root exp(-pi*i/Q) rounded down at scale B. Taylor remainder and pi interval included.
t=pl/Q
cs=sum((-1)**n*t**(2*n)/factorial(2*n) for n in range(6));sn=sum((-1)**n*t**(2*n+1)/factorial(2*n+1) for n in range(6))
assert (pu-pl)/Q+t**12/factorial(12)<F(1,B)
assert (pu-pl)/Q+t**13/factorial(13)<F(1,B)
root=(int(cs*B),int(-sn*B))
def cmul(a,b):return ((a[0]*b[0]-a[1]*b[1])//B,(a[0]*b[1]+a[1]*b[0])//B)
roots=[(B,0)]
for n in range(Q):roots.append(cmul(roots[-1],root))
# root error < 4/B in complex modulus; each multiplication roundoff < 2/B.
# With n<=Q, recurrence E_{n+1}<=(1+4/B) E_n+6/B implies E_n<=12Q/B.
assert 8*Q<B and F(12*Q,B)<F(1,2**40)
R=F(12*Q,B)
# FFT max-norm error recurrence per stage; input rotation error <= 2R+4/B.
# Each exact butterfly intermediate has magnitude <= sum absolute input < 2.
# e_next <= (2+R)e + 2R + 2/B. Bound using integer-friendly rational recurrence.
e=2*R+F(4,B)
for _ in range(Q.bit_length()-1):e=(2+R)*e+2*R+F(2,B)
assert e<F(1,S),e

def fft_mid(data):
    a=[(0,0)]*Q
    for j,c in data.items():
        rootj=roots[abs(j)]; rootj=(rootj[0],rootj[1] if j>=0 else -rootj[1]);
        z=cmul((int(c*B),0),rootj)
        a[j%Q]=z if j%2==0 else (-z[0],-z[1])
    j=0
    for i in range(1,Q):
        bit=Q>>1
        while j&bit:j^=bit;bit>>=1
        j^=bit
        if i<j:a[i],a[j]=a[j],a[i]
    m=2
    while m<=Q:
        half=m//2;step=2*Q//m
        for i in range(0,Q,m):
            for j in range(half):
                u=a[i+j];v=cmul(a[i+j+half],roots[j*step]);a[i+j]=(u[0]+v[0],u[1]+v[1]);a[i+j+half]=(u[0]-v[0],u[1]-v[1])
        m*=2
    return np.array([(a//(B//S),b//(B//S)) for a,b in a],dtype=np.int64)
# log upper/lower via exact atanh series, k log 2 + log of mantissa.
def logsmall(t):
    z=(t-1)/(t+1);assert 0<=z<=F(1,3)
    a=2*sum(z**(2*n+1)/(2*n+1) for n in range(12))
    return a,a+2*z**25/(25*(1-z*z))
ll,lu=logsmall(F(2))
def logbounds(t):
    k=0
    while t>=2:t/=2;k+=1
    l,u=logsmall(t);return k*ll+l,k*lu+u
el,eu=F(271828,100000),F(271829,100000)
es=sum(F(1,factorial(i)) for i in range(12));assert el<es and es+F(2,factorial(12))<eu
# All finite-band w<11 (and >=1). Rational log at endpoints, monotonicity inside bins.
T=F(2*M+1,2)/h
assert logbounds(eu+T)[1]<11

def floor(a):return a.numerator//a.denominator
def ceil(a):return -floor(-a)
def wbins(m,bins):
    lo=[];hi=[]
    for i in range(bins):
        a=F(m)-F(1,2)+F(i,bins);b=a+F(1,bins)
        l=0 if a<=0<=b else min(abs(a),abs(b));u=max(abs(a),abs(b))
        lo.append(max(S,floor(S*logbounds(el+l/h)[0])))
        hi.append(ceil(S*logbounds(eu+u/h)[1]))
    return np.repeat(np.array(lo,dtype=np.int64),Q//bins),np.repeat(np.array(hi,dtype=np.int64),Q//bins)
X=fft_mid(dict(enumerate(x)));Z=fft_mid(q)
assert np.max(np.abs(X))<S and np.max(np.abs(Z))<2*S
u=2*np.arange(Q,dtype=np.int64)+1-Q

def ceildiv(a,b):return (a+b-1)//b

def upper(m,L,U):
    mid=(L+U)//2; delta=np.maximum(mid-L,U-mid)
    # FFT samples have error <2/S in each real component. Bound residual Q-wX.
    r=np.abs(Z-(mid[:,None]*X)//S)+3+ceildiv(2*U[:,None],S)+ceildiv(delta[:,None]*np.abs(X),S)
    assert np.max(r)<15*S
    amp=ceildiv(np.sum(r*r,axis=1),L) # squared amplitude / w, in units 1/S
    if m==0:sinc=np.full(Q,S,dtype=np.int64)
    else:sinc=ceildiv(S*u*u,(2*Q*m+u)**2)
    prod=amp*sinc
    assert np.all(prod>=0) and int(prod.max())*Q<2**63
    return int(prod.sum())
acc=0
for m in range(M+1):
    L,U=wbins(m,2048 if m==0 else 16)
    acc+=upper(m,L,U)
    if m:acc+=upper(-m,L[::-1],U[::-1])
mid_bound=h*F(acc,Q*S*S)
# L2 midpoint error <= half mesh times ||F'|| <= 3/Q.
# use exact rational square root upper (ceil sqrt at scale 10^9).
def sqrtup(v):
    D=10**9;n=ceil(v*D*D);a=isqrt(n);return F(a+(a*a<n),D)
finite=(sqrtup(mid_bound)+F(3,Q))**2
# Independently reconstruct E19N step-function tail reserve.
f=[F(0)]*793; f[64:729]=x; qq=[q.get(i,F(0)) for i in range(-64,729)]
def jump(a):return sum(abs(b-a) for a,b in zip([0]+a,a+[0]))
assert logbounds(el+T)[0]>9
j1,j2=jump(f),jump(qq)
tail=2*(j1*j1*12/(18*T)+j2*j2/(18*T*9))
assert tail==F(d['tail_upper_rational'])
total=finite+tail
result=dict(midpoint_upper=str(mid_bound),midpoint_l2_discretization_upper=str(F(3,Q)),finite_band_squared_upper=str(finite),tail_squared_upper=str(tail),total_squared_upper=str(total),norm_upper=str(sqrtup(total)),integer_accumulator=acc,fft_error_upper=str(F(1,S)),grid=Q,alias_radius=M,source_sha256=hashlib.sha256(raw).hexdigest())
print(json.dumps(result,indent=2));print('display',float(mid_bound),float(finite),float(tail),float(total),float(sqrtup(total)))
Path(__file__).with_name('certificate.json').write_text(json.dumps(result,indent=2)+'\n')
