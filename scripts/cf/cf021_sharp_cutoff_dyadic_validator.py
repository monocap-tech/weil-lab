#!/usr/bin/env python3
"""CF021 read-only, numerical controls for the analytic Gamma cutoff/dyadic lemmas.

Nothing in this script is an interval enclosure, Lean certificate, or RH test.
It uses the physical Gamma translation-energy normalization in the CF program.
"""
from __future__ import annotations

import math
import cmath
import numpy as np
from scipy.integrate import quad


def kg(s: float) -> float:
    if s <= 0:
        return math.inf
    return math.exp(-s / 2.0) / (-math.expm1(-2.0 * s))


def qres(s: float) -> float:
    if s <= 0:
        return math.inf
    return math.exp(-2.5 * s) / (-math.expm1(-2.0 * s))


def rectangle_gamma_energy(length: float) -> float:
    # ||1_I - translate_s 1_I||_2^2 = 2 min(s,length)
    first = quad(lambda s: 2 * kg(s) * s if s else 1.0, 0, length,
                 epsabs=2e-11, epsrel=2e-11)[0]
    second = quad(lambda s: 2 * kg(s) * length, length, np.inf,
                  epsabs=2e-11, epsrel=2e-11)[0]
    return first + second


def overlap_shifted(left: tuple[float, float], right: tuple[float, float], s: float) -> float:
    a,b=left; c,d=right
    return max(0., min(b+s,d)-max(a+s,c))


def cross_gamma(left: tuple[float,float], right: tuple[float,float]) -> float:
    # Integration of K(y-x) over x in left and y in right, left to right.
    a,b=left; c,d=right
    assert b <= c + 1e-13
    boundaries=sorted(set([max(0., c-b), c-a, d-b, d-a]))
    total=0.0
    for lo,hi in zip(boundaries[:-1],boundaries[1:]):
        if hi-lo <= 1e-15: continue
        def fun(s):
            if s == 0: return 1.0 # only possible when touching: K(s)*overlap(s) -> 1/2
            return kg(s) * overlap_shifted(left,right,s)
        total += quad(fun,lo,hi,epsabs=2e-11,epsrel=2e-11)[0]
    return total


def gamma_energy_autocorrelation(intervals: list[tuple[float,float]],amps: list[complex]) -> float:
    # Independent integral using ||f - tau_s f||^2 = 2 (||f||^2 - Re C_f(s)).
    mass=sum(abs(z)**2*(b-a) for (a,b),z in zip(intervals,amps))
    right_edge=max(b for a,b in intervals)
    left_edge=min(a for a,b in intervals)
    points={0.0, right_edge-left_edge}
    for a,b in intervals:
        for c,d in intervals:
            for z in (c-b,c-a,d-b,d-a):
                if 0 < z < right_edge-left_edge: points.add(z)
    brk=sorted(points)
    def corr(s:float) -> complex:
        return sum(np.conjugate(z1)*z2*overlap_shifted(I2,I1,s)
                   for I1,z1 in zip(intervals,amps)
                   for I2,z2 in zip(intervals,amps))
    subtotal=0.0
    for lo,hi in zip(brk[:-1],brk[1:]):
        def integrand(s):
            if s == 0.: return 0.0
            return 2*kg(s)*(mass-corr(s).real)
        subtotal += quad(integrand,lo,hi,epsabs=2e-10,epsrel=2e-10)[0]
    subtotal += quad(lambda s: 2*mass*kg(s),right_edge-left_edge,np.inf,
                     epsabs=2e-11,epsrel=2e-11)[0]
    return subtotal


def check():
    for s in (.0001,.01,.3,1.0,3.0,10.0):
        assert abs(kg(s)-qres(s)-math.exp(-s/2)) < 2e-12
        assert qres(s) <= .5/s + 1e-13
    print('PASS kernel: K_gamma = q_res + exp(-s/2), q_res <= 1/(2s)')
    L1, L2=.33,.57
    I1=(-L1,0.); I2=(0.,L2)
    z1,z2=1.2+0.7j,-0.4+1.1j
    E1=abs(z1)**2*rectangle_gamma_energy(L1)
    E2=abs(z2)**2*rectangle_gamma_energy(L2)
    pair=cross_gamma(I1,I2)
    Ewhole=gamma_energy_autocorrelation([I1,I2],[z1,z2])
    identity=E1+E2-Ewhole
    pred=2*(np.conjugate(z1)*z2).real*pair
    assert abs(identity-pred) < 3e-8, (identity,pred)
    carleman=(math.pi/2+1)*math.sqrt(L1*L2)
    assert pair<=carleman+1e-10
    print(f'PASS complex two-sided sharp split: identity={identity:.10f}; 2Re(cross)={pred:.10f}; abs error={abs(identity-pred):.2e}')
    print(f'PASS Carleman+rank-one interface bound: I_K={pair:.10f} <= {carleman:.10f}')
    a=0.25
    intervals=[(-a*2**(-j),-a*2**(-(j+1))) for j in range(5)]
    amps=[1+0.2j, -0.5+0.8j, 0.4-0.3j, 1.1-0.6j, -0.7-0.1j]
    shell_energies=[abs(z)**2*rectangle_gamma_energy(b-x) for (x,b),z in zip(intervals,amps)]
    total_shell=sum(shell_energies)
    total=gamma_energy_autocorrelation(intervals,amps)
    R=math.pi+2+math.sqrt(2)
    mass=sum(abs(z)**2*(b-x) for (x,b),z in zip(intervals,amps))
    assert total_shell <= total+(R+a)*mass+1e-9
    cross_exp=2*sum((np.conjugate(amps[i])*amps[j]).real*cross_gamma(intervals[i],intervals[j])
                    for i in range(len(intervals)) for j in range(i+1,len(intervals)))
    assert abs(total_shell-total-cross_exp)<2e-8
    print(f'PASS dyadic Gamma partition: sum shell E={total_shell:.10f}; full E={total:.10f}; cross reconstruction error={abs(total_shell-total-cross_exp):.2e}')
    print(f'PASS dyadic row bound: excess={total_shell-total:.10f} <= (pi+2+sqrt(2)+a)mass={(R+a)*mass:.10f}')
    print('NOTE: local numerical checks only; no actual neutral mode or RH test.')


if __name__=='__main__':
    check()
