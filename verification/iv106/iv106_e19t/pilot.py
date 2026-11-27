"""E19T numerical pilot only: piecewise-linear interior hats, step collars.
No interval enclosure, graph-domain attachment or Schur certificate is asserted.
"""
import json, hashlib
import scipy
import numpy as np
from scipy.linalg import solve


def run(n, e, hats, Q=16384, M=128):
    d = 2.2/n
    u = np.arange(Q)/Q-.5
    a = np.zeros(Q); v = a.copy(); c = np.zeros(Q, complex)
    for m in range(-M,M+1):
        p=u+m; s=np.sinc(p); w=np.log(np.e+abs(p)/d)
        t=s*s if hats else s
        a += w*t*t; v += s*s/w
        c += t*s*(np.exp(1j*np.pi*p) if hats else 1)
    def coeff(z):
        return d*np.fft.fft(z).real/Q*(-1.)**np.arange(Q)
    a,v,c=map(coeff,(a,v,c))
    i=np.arange(1,n) if hats else np.arange(n)
    j=np.arange(n); k=np.r_[np.arange(-e,0),np.arange(n,n+e)]
    def mat(w,x,y): return w[(x[:,None]-y)%Q]
    A=mat(a,i,i); V=mat(v,k,k); C=mat(c,i,k)
    p=2*np.sinh((-1.1+(j+.5)*d)/2)
    rhs=np.r_[mat(c,i,j)@p,mat(v,k,j)@p]
    z=solve(np.block([[A,C],[C.T,V]]),rhs,assume_a='pos')
    x=np.round(z[:len(i)],12); g=np.round(z[len(i):],12)
    def fftseq(vals,ids):
        arr=np.zeros(Q,complex); arr[ids%Q]=vals*(-1.)**ids
        return np.fft.fft(arr)
    X=fftseq(x,i); B=fftseq(np.r_[p,-g],np.r_[j,k]); total=0.
    for m in range(-M,M+1):
        q=u+m; s=np.sinc(q); w=np.log(np.e+abs(q)/d)
        shape=s*s*np.exp(1j*np.pi*q) if hats else s
        total += d/Q*np.sum(abs(s*B/np.sqrt(w)-np.sqrt(w)*shape*X)**2)
    direct=p@mat(v,j,j)@p-2*z@rhs+z@np.block([[A,C],[C.T,V]])@z
    assert abs(direct-total)<1e-8,(direct,total)
    frozen=np.rint(10**12*np.r_[x,g]).astype("<i8")
    return dict(coefficient_sha256=hashlib.sha256(frozen.tobytes()).hexdigest(),n=n,collar_per_side=e,interior='hat' if hats else 'step',cutoff=(M+.5)/d,finite_band_squared=float(total),midpoint_physical_bound=1.2*d*np.sqrt(2.2/12),crosscheck_abs=float(abs(direct-total)))

if __name__=='__main__':
    rows=[run(665,64,False),run(665,64,True),run(1330,128,True),run(1330,256,True),run(1330,128,False),run(1330,256,False),run(2660,256,False)]
    print(json.dumps(dict(status='floating-point diagnostic only',numpy=np.__version__,scipy=scipy.__version__,rows=rows),indent=2))
