"""All 665 cell rows: floating-point candidate generation, integer coefficient reserves.
No interval finite-band certificate is asserted for these newly generated rows.
"""
import numpy as np
from scipy.linalg import solve_toeplitz,solve
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
h=11/3325; N=665; E=64; Q=16384; M=128; D=10**12
u=np.arange(Q)/Q-.5
W=np.zeros(Q); V=np.zeros(Q); U=np.zeros(Q)
for m in range(-M,M+1):
    p=u+m; s=np.sinc(p)**2; w=np.log(np.e+abs(p)/h)
    W+=s*w; V+=s/w; U+=s
def coeff(a):return h*np.fft.fft(a).real/Q*(-1.)**np.arange(Q)
w,v,b=map(coeff,(W,V,U)); ids=np.arange(N); ext=np.r_[np.arange(-E,0),np.arange(N,N+E)]
idx=np.abs(ids[:,None]-ids); exidx=np.abs(ext[:,None]-ext); cross=np.abs(ext[:,None]-ids)
X=np.rint(D*solve_toeplitz(w[:N],h*np.eye(N))).astype(np.int64)
G=np.rint(D*solve(v[exidx],v[cross],assume_a='pos')).astype(np.int64)
x=X/D; g=G/D
# Quadratic expansion of finite-band residual including cross term.
no=v[0]+np.sum(x*(w[idx]@x),axis=0)-2*np.sum(x*b[idx],axis=0)
y=no+np.sum(g*(v[exidx]@g),axis=0)-2*np.sum(g*v[cross],axis=0)+2*np.sum(g*(b[cross]@x),axis=0)
assert np.all(y>=0)
# Exact step jump and centered coefficient moment bounds. Python ints avoid overflow.
T=F(257,2)/F(11,3325)
from math import factorial,isqrt
assert 3**9<T and sum(F(11**n,factorial(n)) for n in range(31))>T+3
records=[]
def up(v,scale=10**6):
    a=isqrt((v.numerator*scale**2+v.denominator-1)//v.denominator);return F(a+(F(a*a,scale**2)<v),scale)
def jump(a):return sum(abs(b-a) for a,b in zip([0]+a,a+[0]))
for t in range(N):
    xx=list(map(int,X[:,t])); gg=list(map(int,G[:,t])); q=[-a for a in gg[:E]]+[D if i==t else 0 for i in range(N)]+[-a for a in gg[E:]]
    jx=F(jump(xx),D); jq=F(jump(q),D)
    tail=2*(jx*jx*12/(18*T)+jq*jq/(18*T*9))
    a,b0,c,d=map(up,[F(sum(z*z for z in xx),D*D),F(sum(z*z for z in q),D*D),F(sum(((i-t)*z)**2 for i,z in enumerate(xx)),D*D),F(sum(((i-E-t)*z)**2 for i,z in enumerate(q)),D*D)])
    deriv=F(3,50)*(2*(b0+4*a)+7*(d+4*c)+60*(b0+a))
    records.append(dict(row=t,finite_band=float(y[t]),no_exterior=float(no[t]),tail=str(tail),derivative=str(deriv),l1x=str(F(sum(map(abs,xx)),D)),l1q=str(F(sum(map(abs,q)),D))))
# Save integer candidate arrays, not floating coefficients.
p=Path(__file__).parent
np.savez_compressed(p/'row_bank.npz',X=X,G=G,ext=ext,scale=D)
(p/'row_bank_receipt.json').write_text(json.dumps(dict(status='numerical finite-band diagnostics; exact coefficient tail and derivative arithmetic',Q=Q,M=M,scale=D,bank_sha256=hashlib.sha256((p/'row_bank.npz').read_bytes()).hexdigest(),rows=records),indent=2)+'\n')
print('max diagnostics',y.max(),y.argmax(),'min',y.min(),y.argmin(),'max tail',max(float(F(r['tail'])) for r in records),'max derivative',max(float(F(r['derivative'])) for r in records),'max l1',max(float(F(r['l1x'])) for r in records),max(float(F(r['l1q'])) for r in records))
for t in [0,1,10,100,332,664]:print(t,records[t])
print('reflection max differences',abs(X-X[::-1,::-1]).max(),abs(G-G[::-1,::-1]).max())
