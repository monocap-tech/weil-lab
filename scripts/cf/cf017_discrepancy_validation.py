#!/usr/bin/env python3
"""CF017 read-only checks of the complex-polarized pole/prime discrepancy.

Requires Python 3.10+ and scipy. No repository files, Actions, or network calls.
Angular Fourier convention: F(t)=int exp(-i*t*x) f(x) dx.
Hermitian convention here is linear in the first argument.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import exp, log, sqrt, pi
from scipy.integrate import quad


@dataclass(frozen=True)
class Step:
    intervals: tuple[tuple[float,float,complex], ...]

    def __post_init__(self):
        for l, r, z in self.intervals:
            assert l < r and isinstance(z, complex)


def moment(f: Step, alpha: float) -> complex:
    return sum(z * (exp(alpha*r)-exp(alpha*l))/alpha
               for l,r,z in f.intervals)


def corr(f: Step, g: Step, s: float) -> complex:
    """C_fg(s) = int f(x)*conj(g(x-s)) dx."""
    return sum(z*w.conjugate()*max(0.,min(r,R+s)-max(l,L+s))
               for l,r,z in f.intervals for L,R,w in g.intervals)


def sym_corr(f: Step, g: Step, s: float) -> complex:
    return (corr(f,g,s)+corr(f,g,-s))/2


def knots(f: Step,g: Step,span: float) -> list[float]:
    ends_f=[u for l,r,z in f.intervals for u in (l,r)]
    ends_g=[u for l,r,z in g.intervals for u in (l,r)]
    vals={0.,span}
    for x in ends_f:
        for y in ends_g:
            d=abs(x-y)
            if 0. < d < span:
                vals.add(d)
    return sorted(vals)


def integrate_corr(f:Step,g:Step,span:float,alpha:float)->complex:
    ks=knots(f,g,span)
    def part(component):
        return sum(quad(lambda s: exp(alpha*s)*component(sym_corr(f,g,s)),
                        ks[i],ks[i+1],epsabs=5e-12,epsrel=2e-12)[0]
                   for i in range(len(ks)-1))
    return complex(part(lambda z:z.real),part(lambda z:z.imag))


def prime_powers(span:float):
    nmax=int(exp(span)+1e-12)
    for n in range(2,nmax+1):
        p=None; q=n
        for k in range(2,n+1):
            if q%k==0:
                p=k
                while q%k==0:q//=k
                break
        if q==1 and log(n)<span-1e-12:
            yield n, log(p)/sqrt(n)


def cheb_W(s:float)->float:
    return sum(k for n,k in prime_powers(s+1e-10))-2*(exp(s/2)-1)


def pole(f:Step,g:Step)->complex:
    return moment(f,-.5)*moment(g,.5).conjugate()+moment(f,.5)*moment(g,-.5).conjugate()


def pcont(f:Step,g:Step,span:float)->complex:
    return -2*integrate_corr(f,g,span,.5)


def reference(f:Step,g:Step,span:float)->complex:
    return 2*integrate_corr(f,g,span,-.5)


def pprime(f:Step,g:Step,span:float)->complex:
    return -2*sum(k*sym_corr(f,g,log(n)) for n,k in prime_powers(span))


def discrepancy(f:Step,g:Step,span:float)->complex:
    return sum(k*sym_corr(f,g,log(n)) for n,k in prime_powers(span)) - integrate_corr(f,g,span,.5)


def w_by_parts(f:Step,g:Step,span:float)->complex:
    """-int_0^span W(s) d_s sym_corr(f,g,s) ds, with exact segment slopes.
    Split at the autocorrelation kinks and prime-power jumps.
    """
    ks=sorted(set(knots(f,g,span)+[log(n) for n,k in prime_powers(span)]))
    acc=0j
    for a,b in zip(ks[:-1],ks[1:]):
        if b-a<1e-12:continue
        mid=(a+b)/2
        h=min(1e-5,(b-a)/8)
        slope=(sym_corr(f,g,mid+h)-sym_corr(f,g,mid-h))/(2*h)
        weighted=quad(lambda s:cheb_W(s),a,b,epsabs=5e-11,epsrel=1e-11)[0]
        acc-=slope*weighted
    return acc


def close(label:str,a:complex,b:complex,tol:float=2e-8):
    err=abs(a-b)
    print(f'{label}: error={err:.3e}, values={a:.9g} / {b:.9g}')
    if err>tol: raise AssertionError(f'{label} failed: {err}')


def main():
    c=1.
    span=2*c
    f=Step(((-1.,-.3,1.+.75j),(-.3,.25,-.4+1.2j),(.25,1.,.6-.3j)))
    g=Step(((-1.,-.3,-.8+1.1j),(-.3,.25,1.2-.2j),(.25,1.,.35+.9j)))
    for aa,bb,name in ((f,f,'f,f'),(g,g,'g,g'),(f,g,'f,g'),(g,f,'g,f')):
        close(f'pole + continuous = reference [{name}]',pole(aa,bb)+pcont(aa,bb,span),reference(aa,bb,span))
        close(f'prime + pole = reference - 2D [{name}]',pprime(aa,bb,span)+pole(aa,bb),reference(aa,bb,span)-2*discrepancy(aa,bb,span))
        close(f'Chebyshev integration by parts [{name}]',discrepancy(aa,bb,span),w_by_parts(aa,bb,span),tol=3e-7)
    close('Hermitian D(f,g)',discrepancy(f,g,span),discrepancy(g,f,span).conjugate())
    c1=.4
    span1=2*c1
    freqs=[2*pi*j/log(2) for j in (50,100,200)]
    k=log(2)/sqrt(2)
    for t in freqs:
        continuous=((exp(span1/2)*(.5*__import__('math').cos(span1*t)+t*__import__('math').sin(span1*t))-.5)/(t*t+.25))
        d=k*__import__('math').cos(t*log(2))-continuous
        print(f'one-prime recurrence t={t:.3f}: d={d:.10f}, target={k:.10f}')
        assert abs(d-k)<.004
    print('PASS: all local CF017 identity and phase tests')


if __name__=='__main__':
    main()