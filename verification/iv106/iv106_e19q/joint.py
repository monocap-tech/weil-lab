"""Joint Loewner reserve for frozen E19P bank. Analytic conditional, not Lean.
Rational interval weights constant on each midpoint bin; integrate trigonometric
polynomials exactly via sinc(lag/Q). Integer FFT and bounded int64 products.
"""
from pathlib import Path
import hashlib,json
from fractions import Fraction as F
from math import factorial,isqrt
import numpy as np
p=Path(__file__).parent
src=p.parent/'iv106_e19p'
# Reuse authenticated E19P arithmetic primitives, not its midpoint output.
s=(src/'certify_bank.py').read_text(); prefix=s[s.index('from fractions'):s.index('# s is a rational pointwise')]
prefix=prefix.replace('p=Path(__file__).parent','p=src')
assert hashlib.sha256((src/'certify_bank.py').read_bytes()).hexdigest()=='814bb90590a546c67bce52659e612657a3e880754957c3aff2d8553391cc1f2a'
exec(prefix)
p=Path(__file__).parent
# u=(2i+1-Q)/(2Q); exact whole-bin upper on sinc^2.
u=2*np.arange(Q,dtype=np.int64)+1-Q
A=np.zeros(Q,np.int64);V=A.copy();C=A.copy()
def add_alias(m,L,U):
    s=np.full(Q,S,np.int64) if m==0 else ceildiv(S*(np.abs(u)+1)**2,(np.abs(2*Q*m+u)-1)**2)
    A[:]+=ceildiv(s*U,S);V[:]+=ceildiv(s*S,L);C[:]+=s
for m in range(M+1):
    L,U=wbins(m,2048 if m==0 else 16);add_alias(m,L,U)
    if m:add_alias(-m,L[::-1],U[::-1])
assert int(A.max())<20*S and int(V.max())<4*S and int(C.max())<4*S
assert all(np.array_equal(a,a[::-1]) for a in [A,V,C])
# Increase Toeplitz output precision; same fixed point FFT root recurrence.
H=2**30
e=F(1,B)
for _ in range(Q.bit_length()-1):e=(2+R)*e+20*R+F(2,B)
e=(1+R)*e+20*R+F(2,B)
# Exact bin integral has factor sinc(pi*n/Q). Taylor enclosure via pi interval.
sinc=[]
for n in range(N+2*E):
    lo,hi=pl*n/Q,pu*n/Q
    l=1-hi**2/6+lo**4/120-hi**6/5040
    u=1-lo**2/6+hi**4/120-lo**6/5040+hi**8/362880
    assert 0<l<=u<=1+F(1,10**10)
    sinc.append((l,u))
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
    out=[]; errs=[]
    for n,(l,u) in enumerate(sinc):
        v=F((-1)**n*cmul(a[n],roots[n])[0],B)
        lo=min((v-e)*l,(v-e)*u,(v+e)*l,(v+e)*u)
        hi=max((v-e)*l,(v-e)*u,(v+e)*l,(v+e)*u)
        k=floor(H*(lo+hi)/2);out.append(k);errs.append(max(k-floor(H*lo),ceil(H*hi)-k))
    return np.array(out,np.int64),max(errs)
wa,ea=gram(A);wv,ev=gram(V);wc,ec=gram(C)
print('gram errors',ea,ev,ec,flush=True)
# Quantize at 2^20. Intermediate contractions are floored at scale 2^14
# and their exact error is charged to the final operator enclosure.
P=2**20; K=2**14; Hout=H//K; xx=X*P//D; qq=np.zeros((N+2*E,N),np.int64);qq[E:E+N]=P*np.eye(N,dtype=np.int64);qq[:E]=(-G[:E])*P//D;qq[E+N:]=(-G[E:])*P//D
sx=int(np.abs(xx).sum(axis=0).max());sq=int(np.abs(qq).sum(axis=0).max())
ids=np.arange(N);allids=np.arange(-E,N+E)
def quad(a,b,w,ii,jj):
    aa=int(np.abs(a).sum(axis=0).max());bb=int(np.abs(b).sum(axis=0).max());ww=int(np.abs(w).max());assert bb*ww<2**63
    assert aa*(bb*ww//K+1)<2**63
    return a.T@((w[np.abs(ii[:,None]-jj)]@b)//K)
qa=quad(xx,xx,wa,ids,ids);qv=quad(qq,qq,wv,allids,allids);qc=quad(xx,qq,wc,ids,allids)
assert int(np.abs(qa).max())+int(np.abs(qv).max())+2*int(np.abs(qc).max())<2**63
# Use symmetric part: doubled matrix avoids any rounding on symmetrization.
Mraw=qa+qv-qc-qc.T
assert 2*int(np.abs(Mraw).max())<2**63
Mmat=Mraw+Mraw.T;assert np.array_equal(Mmat,Mmat.T)
# Gershgorin upper; exact Python integer sums avoid row overflow.
row=[int(Mmat[i,i])+sum(abs(int(Mmat[i,j])) for j in range(N) if j!=i) for i in range(N)]
# Entry errors, operator norm via Schur bound on absolute coefficient maps.
def schur_sq(a):return int(np.abs(a).sum(axis=0).max())*int(np.abs(a).sum(axis=1).max())
def sqrtup(v,scale=10**9):
    assert v>=0; z=ceil(v*scale**2);a=isqrt(z);return F(a+(a*a<z),scale)
# Error Toeplitz entries <= e/H. Bound contractions by l1 maps / row sums.
# |c^* X^* E Q c| <= e/H ||Xc||_1||Qc||_1 <= e/H sqrt(nx*nq) ||X|| ||Q|| ||c||².
xop=sqrtup(F(schur_sq(xx),P*P));qop=sqrtup(F(schur_sq(qq),P*P))
# Better bound using column absolute sums (sqrt(N) max column l1).
x1=F(sx,P);q1=F(sq,P)
err=h*F(N,H)*(ea*x1*x1+ev*q1*q1+2*ec*x1*q1)
rounderr=h*F(N,Hout*P)*(x1+q1+2*x1)
mid=h*F(max(row),2*Hout*P*P)+err+rounderr
# Quantization error map via exact Schur test on integer remainder.
Xerr=X*P-xx*D
Qf=np.vstack([-G[:E],D*np.eye(N,dtype=np.int64),-G[E:]])
Qerr=Qf*P-qq*D
ex=sqrtup(F(schur_sq(Xerr),D*D*P*P));eq=sqrtup(F(schur_sq(Qerr),D*D*P*P))
pert=F(3,50)*(5*ex+2*eq)
finite=(sqrtup(mid)+pert)**2
# Tail of aggregate coefficient map via jump map and Cauchy Schwarz / Schur.
# Bound |sum jump_j exp(...)| <= sqrt(num jumps) * ||J c||_2;
# sharper bound directly ||J||_{2->1} <= sqrt(num columns)*max col sum.
def jump(a):return np.diff(np.vstack([np.zeros((1,N),np.int64),a,np.zeros((1,N),np.int64)]),axis=0)
JX=jump(X);JQ=jump(Qf)
# Integral over aliases beyond cutoff: exploit periodic jump polynomial Parseval
# instead of pointwise l1. For u in [-.5,.5] sum_{|m|>=129} 1/(m+u)^2 <= 2/128.5+2/128.5^2.
# Fourier step formula |hat f| = |jump polynomial|/(2*pi*|xi|).
# weighted tail bound via monotone integral for w(s)/s², plus first sample.
# w(T)<11; sum over m>=129 w((m-.5)/h)/(m-.5)^2 <= 11/(128.5)^2+12/128.5.
# raw inverse weighted sum <= (1/9)*(1/(128.5)^2+1/128.5).
L=F(257,2)
ax=F(schur_sq(JX),D*D);aq=F(schur_sq(JQ),D*D)
tail=2*h/F(36)*(2*(11/L**2+12/L)*ax+2*(1/L**2+1/L)/9*aq)
total=finite+tail
cert=dict(status='conditional analytic joint Loewner bound; integer replay not Lean',bank_sha256=hashlib.sha256((src/'row_bank.npz').read_bytes()).hexdigest(),gram_errors=[ea,ev,ec],gram_scale=H,coefficient_scale=P,gershgorin_upper=str(h*F(max(row),2*Hout*P*P)),gram_error=str(err),intermediate_rounding_upper=str(rounderr),quantization_norm=str(pert),finite_upper=str(finite),jump_operator_squared=[str(ax),str(aq)],tail_upper=str(tail),total_upper=str(total),norm_upper=str(sqrtup(total)),trace_individual=str(sum(F(r['total_upper']) for r in json.loads((src/'bank_certificate.json').read_text())['rows'])))
(p/'joint_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
np.savez_compressed(p/'joint_matrix.npz',M=Mmat,wa=wa,wv=wv,wc=wc)
print(json.dumps(cert,indent=2),flush=True)
for k in ['gershgorin_upper','gram_error','intermediate_rounding_upper','quantization_norm','finite_upper','tail_upper','total_upper','norm_upper','trace_individual']:print(k,float(F(cert[k])),flush=True)
