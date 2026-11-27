import numpy as np
from scipy.linalg import solve_toeplitz, solve
from fractions import Fraction
h=11/3325; N=665; target=0
# Integrate in u=h*xi, period 1 for integer-shifted indicators.
# Trapezoid is diagnostic only; no certified finite quadrature error.
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
    Vmat=V[np.abs(ix[:,None]-ix)]
    b=V[np.abs(ix-target)]
    g=solve(Vmat,b,assume_a='pos')
    # Freeze decimal rationals, do not claim exact optimality.
    x=np.round(x,12); g=np.round(g,12)
    # Reconstruct actual residual finite-band norm including cross terms.
    # full physical inner products interior/exterior are zero, but finite-band are not.
    Q2=Q; u=np.arange(Q2)/Q2-.5
    def fftseq(coeff,ids):
        a=np.zeros(Q2,complex); a[ids%Q2]=coeff*(-1.)**ids
        return np.fft.fft(a)
    X=fftseq(x,np.arange(N)); G=fftseq(g,ix)
    raw=1-G # target=0
    val=0.; val_no=0.; norm_raw=0.
    for m in range(-M,M+1):
        p=u+m; w=np.log(np.e+abs(p)/h); s=np.sinc(p)**2
        val+=np.sum(s*abs(raw/np.sqrt(w)-np.sqrt(w)*X)**2)*h/Q2
        val_no+=np.sum(s*abs(1/np.sqrt(w)-np.sqrt(w)*X)**2)*h/Q2
        norm_raw+=np.sum(s/w)*h/Q2
    # jumps of step coefficients for f, and g_target - g_ext.
    full=np.zeros(N+2*E); full[E:E+N]=x
    rawcoeff=np.zeros_like(full); rawcoeff[E+target]=1; rawcoeff[ix+E]-=g
    Jx=np.sum(np.abs(np.diff(np.r_[0,full,0]))); Jg=np.sum(np.abs(np.diff(np.r_[0,rawcoeff,0])))
    T=(M+.5)/h
    # conservative pi>3 and log(e+T) bound computed via integer powers of e.
    # weighted tail <= Jx^2/(2*pi^2*T)*(w(T)+1), raw <= Jg^2/(2*pi^2*T*w(T)).
    a=Jx**2/(18*T)*(np.log(np.e+T)+1); btail=Jg**2/(18*T*np.log(np.e+T))
    tail=(np.sqrt(a)+np.sqrt(btail))**2
    print(f'{Q=} {M=} {E=} T={T:.3f} raw2={norm_raw:.12g} no_ext2={val_no:.12g} residual2={val:.12g} tail_upper_display={tail:.12g} Jx={Jx:.9g} Jg={Jg:.9g}',flush=True)
    return x,g,ix,val,tail,norm_raw,val_no
if __name__=='__main__':
    for Q,M,E in [(8192,32,32),(16384,64,32),(16384,128,64)]:
        x,g,ix,val,tail,base,no=run(Q,M,E)
    np.savez('/mnt/data/iv106_e19n/row_pilot.npz',x=x,g=g,ix=ix)
    # exact rational jump calculation for frozen decimal coefficients
    xq=[Fraction(str(v)) for v in x]; gq=[Fraction(str(v)) for v in g]
    f=[Fraction(0)]*793; f[64:729]=xq
    q=[Fraction(0)]*793; q[64]=1
    for i,v in zip(ix,gq): q[int(i)+64]-=v
    def jump(v): return sum(abs(b-a) for a,b in zip([0]+v,v+[0]))
    jx,jg=jump(f),jump(q); T=Fraction(257,2)/Fraction(11,3325)
    # w(T)>9 from e<3, 3^9<T; w(T)<11 by exp partial series.
    from math import factorial
    assert 3**9<T and sum(Fraction(11**n,factorial(n)) for n in range(31))>T+3
    a=jx*jx*12/(18*T); b=jg*jg/(18*T*9)
    # (sqrt(a)+sqrt(b))^2 <= 2(a+b)
    reserve=2*(a+b)
    print('exact jumps',jx,jg,'tail rational',reserve,'display',float(reserve))
    import json
    with open('/mnt/data/iv106_e19n/row_pilot.json','w') as o: json.dump({'target':target,'x':[str(v) for v in xq],'g':[str(v) for v in gq],'ix':ix.tolist(),'tail_upper_rational':str(reserve),'finite_band_squared_diagnostic':val,'raw_squared_diagnostic':base,'no_exterior_squared_diagnostic':no},o,separators=(',',':'))
