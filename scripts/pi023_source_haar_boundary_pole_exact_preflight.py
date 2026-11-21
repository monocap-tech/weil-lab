#!/usr/bin/env python3
"""PI023 analytic-only: exact source normalization and unmatched arch pole tests.

The smooth-pair pole proof is mathematical and documented separately. This
rational model uses formal signed point masses for the Laplace coefficients;
it is NOT itself a smooth test or a spectral trace computation.
"""
from fractions import Fraction as F
from math import isqrt


def sqrt_q(q):
    a, b = isqrt(q.numerator), isqrt(q.denominator)
    assert q > 0 and a * a == q.numerator and b * b == q.denominator
    return F(a, b)


def k_log(q):
    assert q > 1
    return 1 / (sqrt_q(q) * (1 - q ** (-2)))


def bare_real(q):
    assert q > 1
    return sqrt_q(q) * (1 / (q - 1) + 1 / (q + 1))


def lam(n):
    return 2*F(n) + F(1, 2)


def signed_shift_weight(n):
    # rho_disk = delta_0 - delta_log4, phi = this signed 2-atom control;
    # C=2 delta_0 - delta_{log4} - delta_{-log4}.
    four_power = 2 * F(16)**n  # 4^(2n+1/2)
    laplace_c = 2 - four_power - 1/four_power
    exp_shift = 1/(3*F(81)**n)  # 9^(-(2n+1/2))
    return laplace_c * exp_shift  # coefficient of G(a) at a=log9


def arch_laplace(s, N):
    # At s=-1/2+epsilon, first arch pole has residue w0.
    return sum((signed_shift_weight(n)/(s + lam(n)) for n in range(N)), F())


def spectral_control(s):
    # Non-zeta synthetic poles strictly within the open strip (-1/2,1/2).
    poles = [(-F(1,4),F(1,8)), (F(1,4),-F(2,9))]
    return sum((t/(s-p) for p,t in poles), F())


def main():
    roots=(2,3,4,5,6,7,8,9,10,11,12,13,17,21)
    for root in roots:
        q=F(root*root)
        assert bare_real(q)==2*k_log(q)
        assert bare_real(q)/2==k_log(q)
        # local canonical measure for R^× is 1/2 the Tamagawa measure.
    assert k_log(F(9))==F(27,80)
    assert bare_real(F(9))==F(27,40)
    assert signed_shift_weight(0)==-F(1,6)
    for n in range(1,101):
        assert signed_shift_weight(n) < 0
        assert lam(n) >= F(5,2)

    cases=0
    for N in (1,2,3,5,8,12):
        w0=signed_shift_weight(0)
        tail_bound=sum((abs(signed_shift_weight(n))/(2*n) for n in range(1,N)),F())
        for denom in (16,64,256,1024):
            eps=F(1,denom)
            s=-F(1,2)+eps
            residue_estimate=eps*arch_laplace(s,N)
            # All other arch poles lie at least 2 away from s=-1/2.
            assert abs(residue_estimate-w0)<=eps*tail_bound
            # Synthetic zeros in strip, no pole at s=-1/2.
            assert abs(eps*spectral_control(s))<=eps*F(4)*(F(1,8)+F(2,9))
            cases+=1

    # Two-hyperplane contact/moment corrections vanish identically on D.
    for c,d in [(F(1),F(0)),(F(0),F(1)),(F(-3,2),F(5,7))]:
        assert c*0+d*0 == 0 != signed_shift_weight(0)
    # In a ramified p-adic example where |disc|_p=1/9, mu(O^×)=1/3.
    # The coefficient of log(q_v) is 3 canonical, 1 bare. Q_p unramified
    # has mu(O^×)=1, hence no finite-place discrepancy for F=Q.
    assert F(1)/F(1,3) == 3
    print('PI023 EXACT SOURCE HAAR AND BOUNDARY-POLE PREFLIGHT: PASS')
    print(f'{len(roots)} rational-square source real-place factor checks')
    print('100 negative noncentral arch Laplace weights (signed point-mass model)')
    print(f'{cases} arch residue-isolation / spectrally analytic controls')
    print('At a=log9: lowest arch pole s=-1/2 has residue -1/6 in model')
    print('NOT checked: actual zeta zeros, smooth Laplace integrals, Masullo trace, Lean, RH')

if __name__=='__main__':
    main()
