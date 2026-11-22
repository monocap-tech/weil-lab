#!/usr/bin/env python3
"""CF019 local read-only numerical controls; not interval or kernel certified.
Fourier convention: angular t for gamma and prime cos(t log n).
Two L2-normalized positive rectangular packets with left [0,ell], right [a,a+ell].
"""
from __future__ import annotations
from math import exp, expm1, log, sqrt, sinh, cosh
from scipy.integrate import quad


def gamma_k(s: float) -> float:
    return exp(-s/2) / (-expm1(-2*s))


def residual_q(s: float) -> float:
    return exp(-2.5*s) / (-expm1(-2*s))


def triangular_integral(kernel, ell, gap):
    """Integral over two packets [0,ell] and [gap+ell,gap+2ell]."""
    # separation gap + r+s, r,s in [0,ell]
    def triangle(z):
        return z if z <= ell else 2*ell-z
    return (quad(lambda z: triangle(z)*kernel(gap+z), 0, ell,
                 epsabs=2e-12, epsrel=2e-12)[0]
            +quad(lambda z: triangle(z)*kernel(gap+z), ell, 2*ell,
                  epsabs=2e-12, epsrel=2e-12)[0]) / ell


def pole_mixed(ell,a):
    # For left=[0,ell], right=[a,a+ell], a > ell.
    # Hermitian pole mixed = two products of exponential moments.
    m_plus_left = 2*expm1(ell/2)/sqrt(ell)
    m_minus_left = -2*expm1(-ell/2)/sqrt(ell)
    m_plus_right = exp(a/2)*m_plus_left
    m_minus_right = exp(-a/2)*m_minus_left
    return m_minus_left*m_plus_right+m_plus_left*m_minus_right


def continuum_mixed(ell,a):
    # -double integral e^((y-x)/2)dxdy / ell; a>ell
    return -(4.0/ell)*exp(a/2)*(1-exp(-ell/2))*expm1(ell/2)


def main():
    print('CF019 exact reference-kernel controls (noncertifying)')
    for s in (0.05,0.2,log(2),1.8,4.0):
        k=gamma_k(s); q=residual_q(s)
        assert abs((k-exp(-s/2))-q) <= 2e-15
        series=sum(exp(-(2*j+0.5)*s) for j in range(1, 700))
        assert abs(q-series)<3e-13
        print(f's={s:7.4f}, K_gamma={k:.9f}, q=K_gamma-exp(-s/2)={q:.9f}, relative_tail={q/k:.8f}')
    print('Adjacent packets: B_ref=negative integral q(r+s)/ell')
    for ell in (0.2,0.1,0.04,0.01,0.002):
        adjacent=-triangular_integral(residual_q,ell,0.0)
        print(f'ell={ell:7.4f}, B_ref={adjacent: .9f}, limit={-log(2): .9f}, error={adjacent+log(2):.7f}')
        assert abs(adjacent+log(2)) < 2.5*ell
    print('Prime-separated one-prime pair c=0.4, a=log(2)')
    a=log(2); kap=a/sqrt(2.0)
    for ell in (0.02,0.005,0.001):
        gap=a-ell
        gamma_cross=-triangular_integral(gamma_k,ell,gap)
        pole_cross=pole_mixed(ell,a)
        ref_cross=-triangular_integral(residual_q,ell,gap)
        cont_cross=continuum_mixed(ell,a)
        prime_cross=-kap
        native_cross=gamma_cross+pole_cross+prime_cross
        discrepancy=kap/2+cont_cross/2  # D=prime jump/2 - continuum reference/2
        rewritten_cross=ref_cross-2*discrepancy
        assert abs(native_cross-rewritten_cross) < 3e-12, (native_cross,rewritten_cross)
        d_exact=kap/2-(8*sqrt(2)/ell)*sinh(ell/4)**2
        assert abs(discrepancy-d_exact) < 4e-12
        print(f'ell={ell:.4f}: gamma={gamma_cross:+.9f}, pole={pole_cross:+.9f}, '
              f'prime={prime_cross:+.9f}, B_ref={ref_cross:+.9f}, D={discrepancy:+.9f}, '
              f'B_W={native_cross:+.9f}, B_ref/ell={ref_cross/ell:+.9f}')
        assert abs(ref_cross/ell + 1/(3*sqrt(2))) < 3*ell
    # complex phase test, mixed pairing is anti-linear in first slot
    theta=1.2
    from cmath import exp as cexp
    u_phase=cexp(1j*theta)
    ell=0.01
    B_real=-triangular_integral(residual_q,ell,log(2)-ell)
    assert abs(u_phase.conjugate()*B_real-B_real*cexp(-1j*theta)) < 1e-14
    print('PASS gamma tail cancellation, Laplace series, adjacent limit, original-vs-discrepancy mixed forms, complex polarization.')

if __name__ == '__main__':
    main()