"""Boundary row 0, 665 original interior cells and exterior indicators.
Numerical quadrature is diagnostic, exact rational tail arithmetic separate.
Run with NumPy/SciPy. No claims of interval-certified finite-band integration.
"""
import numpy as np
from scipy.linalg import solve_toeplitz, solve
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path

h=11/3325
N=665
target=0

def grams(Q,M):
    u=np.arange(Q)/Q-.5
    W=np.zeros(Q); V=np.zeros(Q)
    for m in range(-M,M+1):
        x=u+m; s=np.sinc(x)**2; w=np.log(np.e+abs(x)/h)
        W+=s*w; V+=s/w
    def coeff(a):
        return h*np.fft.fft(a).real/Q*(-1.)**np.arange(Q)
    return coeff(W),coeff(V)

def run(Q,M,E):
    W,V=grams(Q,M)
    rhs=np.zeros(N); rhs[target]=h
    x=solve_toeplitz(W[:N],rhs)
    ix=np.r_[np.arange(-E,0),np.arange(N,N+E)]
    g=solve(V[np.abs(ix[:,None]-ix)],V[np.abs(ix-target)],assume_a='pos')
    # Freeze decimal rational coefficients.
    x=np.round(x,12); g=np.round(g,12)
    u=np.arange(Q)/Q-.5
    def fftseq(coeff,ids):
        a=np.zeros(Q,complex); a[ids%Q]=coeff*(-1.)**ids
        return np.fft.fft(a)
    X=fftseq(x,np.arange(N)); G=fftseq(g,ix)
    val=0.; val_no=0.; norm_raw=0.
    for m in range(-M,M+1):
        p=u+m; w=np.log(np.e+abs(p)/h); s=np.sinc(p)**2
        val+=np.sum(s*abs((1-G)/np.sqrt(w)-np.sqrt(w)*X)**2)*h/Q
        val_no+=np.sum(s*abs(1/np.sqrt(w)-np.sqrt(w)*X)**2)*h/Q
        norm_raw+=np.sum(s/w)*h/Q
    T=(M+.5)/h
    print(Q,M,E,T,norm_raw,val_no,val,flush=True)
    return x,g,ix,val,norm_raw,val_no

if __name__=='__main__':
    for Q,M,E in [(8192,32,32),(16384,64,32),(16384,128,64)]:
        x,g,ix,val,base,no=run(Q,M,E)
    xq=[F(str(v)) for v in x]; gq=[F(str(v)) for v in g]
    f=[F(0)]*793; f[64:729]=xq
    q=[F(0)]*793; q[64]=1
    for i,v in zip(ix,gq): q[int(i)+64]-=v
    def jump(v): return sum(abs(b-a) for a,b in zip([0]+v,v+[0]))
    jx,jg=jump(f),jump(q)
    T=F(257,2)/F(11,3325)
    assert 3**9<T and sum(F(11**n,factorial(n)) for n in range(31))>T+3
    # For step functions |hat f|<=Jf/(2*pi*abs(xi)).
    # Integral w(x)/x^2 dx on [T,infty) <= (w(T)+1)/T.
    # w(T) in (9,11), pi>3; use (a+b)^2<=2(a^2+b^2).
    a=jx*jx*12/(18*T); b=jg*jg/(18*T*9)
    reserve=2*(a+b)
    assert reserve<F(94,10000000)
    print('exact jumps',jx,jg,'tail rational',reserve,'display',float(reserve))
    Path('row_pilot.json').write_text(json.dumps(dict(target=target,x=list(map(str,xq)),
        g=list(map(str,gq)),ix=ix.tolist(),tail_upper_rational=str(reserve),
        finite_band_squared_diagnostic=val,raw_squared_diagnostic=base,
        no_exterior_squared_diagnostic=no),separators=(',',':')))
