"""Shared integer Fourier contraction certificate for 665 frozen rows.
Analytic prerequisites: same midpoint and sinc majorants as E19O, centered
coefficient Parseval derivative bound and jump tails. NumPy int64 only for
bounded integer operations; no floating point quadrature enters the bounds.
"""
from fractions import Fraction as F
from math import factorial,isqrt
from pathlib import Path
import json, hashlib
import numpy as np
p=Path(__file__).parent
rec=json.loads((p/'row_bank_receipt.json').read_text()); raw=(p/'row_bank.npz').read_bytes();assert hashlib.sha256(raw).hexdigest()==rec['bank_sha256']
a=np.load(p/'row_bank.npz'); X=a['X'];G=a['G'];ext=a['ext'];D=int(a['scale']);N=665;E=64;Q=16384;M=128;S=2**20;B=2**60;P=2**18;H=2**22;h=F(11,3325);T=F(257,2)/h
assert X.shape==(N,N) and G.shape==(2*E,N) and list(ext)==list(range(-E,0))+list(range(N,N+E))
# Reuse elementary enclosure routines from the exact earlier verifier;
# no runtime dependency on its original candidate or computed results.
def atan_bounds(z):
    a=sum((-1)**n*z**(2*n+1)/(2*n+1) for n in range(30));return a,a+z**61/61
al,au=atan_bounds(F(1,5));bl,bu=atan_bounds(F(1,239));pl,pu=16*al-4*bu,16*au-4*bl
assert 3<pl<pu<F(22,7)
t=pl/Q
cs=sum((-1)**n*t**(2*n)/factorial(2*n) for n in range(6));sn=sum((-1)**n*t**(2*n+1)/factorial(2*n+1) for n in range(6))
assert (pu-pl)/Q+t**12/factorial(12)<F(1,B) and (pu-pl)/Q+t**13/factorial(13)<F(1,B)
root=(int(cs*B),int(-sn*B))
def cmul(a,b):return ((a[0]*b[0]-a[1]*b[1])//B,(a[0]*b[1]+a[1]*b[0])//B)
roots=[(B,0)]
for n in range(Q):roots.append(cmul(roots[-1],root))
assert 8*Q<B
R=F(12*Q,B)
def logsmall(t):
    z=(t-1)/(t+1);assert 0<=z<=F(1,3)
    a=2*sum(z**(2*n+1)/(2*n+1) for n in range(12));return a,a+2*z**25/(25*(1-z*z))
ll,lu=logsmall(F(2))
def logbounds(t):
    k=0
    while t>=2:t/=2;k+=1
    l,u=logsmall(t);return k*ll+l,k*lu+u
el,eu=F(271828,100000),F(271829,100000)
es=sum(F(1,factorial(i)) for i in range(12));assert el<es and es+F(2,factorial(12))<eu
assert logbounds(eu+T)[1]<11 and logbounds(el+T)[0]>9
assert h<F(3,50)**2 and 1/(el*h)<120
def floor(a):return a.numerator//a.denominator
def ceil(a):return -floor(-a)
def ceildiv(a,b):return (a+b-1)//b
def wbins(m,bins):
    lo=[];hi=[]
    for i in range(bins):
        a=F(m)-F(1,2)+F(i,bins);b=a+F(1,bins)
        l=0 if a<=0<=b else min(abs(a),abs(b));u=max(abs(a),abs(b))
        lo.append(max(S,floor(S*logbounds(el+l/h)[0])));hi.append(ceil(S*logbounds(eu+u/h)[1]))
    return np.repeat(np.array(lo,dtype=np.int64),Q//bins),np.repeat(np.array(hi,dtype=np.int64),Q//bins)
# s is a rational pointwise majorant of sinc^2, common to all three terms.
# A and V enclose sum s*w and sum s/w; C=sum s exactly. Nonnegative
# squared integrand allows replacing sinc^2 by s before expansion.
u=2*np.arange(Q,dtype=np.int64)+1-Q
A=np.zeros(Q,np.int64);V=A.copy();C=A.copy()
def add_alias(m,L,U):
    s=np.full(Q,S,np.int64) if m==0 else ceildiv(S*u*u,(2*Q*m+u)**2)
    A[:]+=ceildiv(s*U,S);V[:]+=ceildiv(s*S,L);C[:]+=s
for m in range(M+1):
    L,U=wbins(m,2048 if m==0 else 16);add_alias(m,L,U)
    if m:add_alias(-m,L[::-1],U[::-1])
assert int(A.max())<20*S and int(V.max())<4*S and int(C.max())<4*S
print('weight maxima',int(A.max()),int(V.max()),int(C.max()),flush=True)
# Compute real midpoint DFT coefficients of rational majorant weights.
# Input l1 <=20, twiddles exact to R. Each butterfly exact intermediate
# <=20, recurrence for complex error e_next <=(2+R)e+20R+2/B.
e=F(1,B)
for _ in range(Q.bit_length()-1):e=(2+R)*e+20*R+F(2,B)
e=(1+R)*e+20*R+F(2,B)
assert e<F(1,S)
Egram=ceil(H*e)+1 # integer units after flooring real coefficient
print('gram coefficient error units',Egram,flush=True)
def gram(weights):
    a=[(int(w)*B//(S*Q),0) for w in weights]
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
                x=a[i+j];y=cmul(a[i+j+half],roots[j*step]);a[i+j]=(x[0]+y[0],x[1]+y[1]);a[i+j+half]=(x[0]-y[0],x[1]-y[1])
        m*=2
    return np.array([((-1)**n*cmul(a[n],roots[n])[0])//(B//H) for n in range(N+2*E)],dtype=np.int64)
wa,wv,wc=map(gram,(A,V,C))
# Quantize frozen coefficients down to P; account for the difference in
# the majorant L2 norm by triangle, Parseval, and maxima of A,V.
assert int(np.abs(X).max())*P<2**63 and int(np.abs(G).max())*P<2**63
xx=X*P//D; qq=np.zeros((N+2*E,N),np.int64);qq[E:E+N,:]=P*np.eye(N,dtype=np.int64);qq[:E,:]=(-G[:E,:])*P//D;qq[E+N:,:]=(-G[E:,:])*P//D
sx=np.abs(xx).sum(axis=0);sq=np.abs(qq).sum(axis=0)
assert int(sx.max())<=P and int(sq.max())<=2*P
# Absolute bounds for all intermediate matrix products and row sums.
# Dot products with signs are safe as their absolute sum is bounded.
assert int(np.abs(wa).max())*P**2<2**63
assert int(np.abs(wv).max())*(2*P)**2<2**63
assert 2*int(np.abs(wc).max())*P*(2*P)<2**63
ids=np.arange(N); allids=np.arange(-E,N+E)
def diagquad(a,b,w,ii,jj):return np.sum(a*(w[np.abs(ii[:,None]-jj)]@b),axis=0)
qa=diagquad(xx,xx,wa,ids,ids);qv=diagquad(qq,qq,wv,allids,allids);qc=diagquad(xx,qq,wc,ids,allids)
# Convert numpy scalars to Python integer before combining.
def sqrtup(v,scale=10**9):
    assert v>=0
    z=ceil(v*scale**2);a=isqrt(z);return F(a+(a*a<z),scale)
# Norm perturbation under the majorant <= sqrt(h)*(sqrt(max A)*26+
# sqrt(max V)*29)/P, because 665<26^2 and 793<29^2.
pert=F(3,50)*(5*26+2*29)/P
# Exact centered derivative and tail checks independently reconstructed.
rows=[]
def jump(a):return sum(abs(b-a) for a,b in zip([0]+a,a+[0]))
for i in range(N):
    x=list(map(int,X[:,i]));g=list(map(int,G[:,i]));q=[-z for z in g[:E]]+[D if j==i else 0 for j in range(N)]+[-z for z in g[E:]]
    a,b,c,d=[sqrtup(F(v,D*D),10**6) for v in [sum(z*z for z in x),sum(z*z for z in q),sum(((j-i)*z)**2 for j,z in enumerate(x)),sum(((j-E-i)*z)**2 for j,z in enumerate(q))]]
    der=F(3,50)*(2*(b+4*a)+7*(d+4*c)+60*(b+a));assert der==F(rec['rows'][i]['derivative'])
    jx=F(jump(x),D);jq=F(jump(q),D);tail=2*(jx*jx*12/(18*T)+jq*jq/(18*T*9));assert tail==F(rec['rows'][i]['tail'])
    num=int(qa[i])+int(qv[i])-2*int(qc[i])+Egram*(int(sx[i])+int(sq[i]))**2
    mid=h*F(num,H*P*P);assert mid>=0
    finite=(sqrtup(mid)+pert+der/(2*Q))**2
    total=finite+tail
    rows.append(dict(row=i,quantized_midpoint_upper=str(mid),finite_upper=str(finite),tail_upper=str(tail),total_upper=str(total),norm_upper=str(sqrtup(total))))
cert=dict(status='integer contraction and analytic conditional bound; not Lean-certified',bank_sha256=rec['bank_sha256'],grid=Q,alias_radius=M,gram_scale=H,coefficient_scale=P,gram_error_units=Egram,quantization_norm_reserve=str(pert),rows=rows)
(p/'bank_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
for key in ['quantized_midpoint_upper','finite_upper','tail_upper','total_upper','norm_upper']:
    row=max(rows,key=lambda r:F(r[key]));print(key,row['row'],row[key],float(F(row[key])),flush=True)
print('row 0',rows[0]); print('row 332',rows[332]);print('PASS',len(rows))
