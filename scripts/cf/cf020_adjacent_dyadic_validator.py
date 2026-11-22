#!/usr/bin/env python3
"""CF020: local numerical checks of the separation-free reference kernel,
Carleman bound, and prime-silent dyadic shell mixed-form estimates.

This is exploratory quadrature. No formal proof or certified intervals; no
repository writes or network actions.
"""
import math
import numpy as np
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss


def residual(s):
    x = np.asarray(s, dtype=float)
    return np.exp(-2.5*x)/(-np.expm1(-2*x))


def kernel_original_prime_silent(s):
    return np.exp(np.asarray(s)/2) - residual(s)


def carleman_log_profile(L):
    # f(x) ~ x^{-1/2}, truncated across L logarithmic scales and L2-normalized.
    return quad(lambda z: (1-z/L)/(2*math.cosh(z/2)),
                0, L, epsabs=1e-12)[0]


def mixed_rectangle(a, b, c, d, n=140):
    """Two nonoverlapping L2-unit indicators on [a,b] and [c,d], b <= c.
    Returns (reference mixed, full prime-silent mixed), numerically.
    """
    assert 0 <= a < b <= c < d
    nodes, weights = leggauss(n)
    X = (a+b)/2 + (b-a)/2*nodes
    Y = (c+d)/2 + (d-c)/2*nodes
    WX = weights*(b-a)/2
    WY = weights*(d-c)/2
    dist = Y[None,:]-X[:,None]
    norm = math.sqrt((b-a)*(d-c))
    Q = (WX[:,None]*WY[None,:]*residual(dist)).sum()/norm
    E = (WX[:,None]*WY[None,:]*np.exp(dist/2)).sum()/norm
    return -Q, E-Q


def main():
    print('CF020 local verification — exploratory quadrature only')
    ss = np.logspace(-9,2,200)
    K = np.exp(-ss/2)/(-np.expm1(-2*ss))
    assert np.max(np.abs((K-np.exp(-ss/2))-residual(ss))) < 1e-7
    print('  max absolute subtraction residual:',float(np.max(np.abs((K-np.exp(-ss/2))-residual(ss)))))
    assert np.all(2*ss*residual(ss) <= 1+1e-12)
    print('PASS: exact kernel cancellation and q(s) <= 1/(2s)')

    print('Carleman logarithmic-profile ratio toward pi/2:')
    for L in (4,8,16,32,64):
        val=carleman_log_profile(L)
        print(f'  depth={L:2d}   coupling={val:.10f}   cap={math.pi/2:.10f}')
        assert val < math.pi/2

    # A positive narrow collar occupying only a fraction of the first prime shift.
    a_collar=.04
    data=[]
    for j in range(7):
        # Physical distance from right endpoint: [a*2^-j-1, a*2^-j]
        lo=a_collar*2**(-j-1)
        hi=a_collar*2**(-j)
        data.append((lo,hi))
    assert a_collar < math.log(2)
    max_ratios=[]
    for j in range(len(data)):
        for k in range(j+1,len(data)):
            lo_k,hi_k=data[k]  # closer to endpoint
            lo_j,hi_j=data[j]  # farther from endpoint
            ref,full=mixed_rectangle(lo_k,hi_k,lo_j,hi_j)
            bound=math.pi/2 if k-j==1 else 2**(-(k-j)/2)
            qpart=-ref
            # Weighted L2 norms are 1 by construction.
            assert qpart <= bound+2e-5,(j,k,qpart,bound)
            max_ratios.append(qpart/bound)
            if (j,k) in ((0,1),(0,2),(0,4),(2,5)):
                print(f'  shells {j},{k} q-coupling={qpart:.9f} '
                      f'bound={bound:.9f}; full mixed={full:.9f}')
            # Direct original Gamma+pole kernel is 2*cosh(s/2)-K(s).
            n=65
            x,w=leggauss(n)
            X=(lo_k+hi_k)/2+(hi_k-lo_k)/2*x
            Y=(lo_j+hi_j)/2+(hi_j-lo_j)/2*x
            W1=w*(hi_k-lo_k)/2
            W2=w*(hi_j-lo_j)/2
            s=Y[None,:]-X[:,None]
            original=(W1[:,None]*W2[None,:]*(2*np.cosh(s/2)-
                      np.exp(-s/2)/(-np.expm1(-2*s)))).sum()/math.sqrt(
                      (hi_k-lo_k)*(hi_j-lo_j))
            assert abs(full-original)<2e-3,(j,k,full,original)
    print('PASS: prime-silent full-kernel identity and dyadic geometry bounds')
    print('Largest sampled q-coupling / analytic bound:',round(max(max_ratios),7))

    # Arbitrary complex coefficient test, L2-unit constant packets each shell.
    rng=np.random.default_rng(1820)
    z=rng.normal(size=len(data))+1j*rng.normal(size=len(data))
    offdiag=0j
    for j in range(len(data)):
        for k in range(j+1,len(data)):
            lo_k,hi_k=data[k]
            lo_j,hi_j=data[j]
            _,full=mixed_rectangle(lo_k,hi_k,lo_j,hi_j)
            offdiag += 2*(z[j].conjugate()*z[k]*full).real
    bound=(math.pi+2+math.sqrt(2)+a_collar*math.exp(a_collar/2))*np.vdot(z,z).real
    assert abs(offdiag) <= bound
    print('PASS: complex phase-sensitive dyadic off-diagonal envelope')
    print(f'  |sum of offdiagonal terms|={abs(offdiag):.8f} '
          f'conservative L2 envelope={bound:.8f}')
    print('No global positivity, kernel acceptance, or RH conclusion.')


if __name__=='__main__':
    main()