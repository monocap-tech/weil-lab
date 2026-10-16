#!/usr/bin/env python3
"""SI16: odd-parity time-bandwidth trace sharpens ORIGINAL supported inverse.

Uses the original signed SI13 all-point positive multiplier window and exact
fractional Fourier/pole bounds. Does not mistake the supported inverse for a
whole-line reciprocal or claim a true computed inverse residual.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import PI, B
from validate_rpb108_si12_even_supported_inverse import sinh_bounds, cosh_bounds
from validate_rpb108_si13_odd_fourier_reference import certify_window

KAPPA=F(1,1000)
DELTA=F(1399,1000)  # Inherited SI13: original signed m>1.4 on [.22,.38].
CENTER=F(3,10)
RADIUS=F(3,1000)
LEFT=CENTER-RADIUS
RIGHT=CENTER+RADIUS


def validate():
    # Replay the inherited complete original signed continuum certificate.
    assert certify_window()>F(7,5)
    assert F(11,50)<LEFT<CENTER<RIGHT<F(19,50)

    pilo,pihi=PI
    assert pilo>3
    # The compactly supported physical odd Fourier pole
    # s(x)=sinh(x/2) has exact center amplitude formula from SI13.
    theta_lo=F(4,25)*pilo
    theta_hi=F(4,25)*pihi
    clo,chi=cosh_bounds(B/2)
    slo,shi=sinh_bounds(B/2)
    k_lo=F(3,5)*pilo
    k_hi=F(3,5)*pihi
    center_amp_lo=2*(clo*(1-theta_hi**2/2)/2+
                      k_lo*slo*(theta_lo-theta_hi**3/6))/(F(1,4)+k_hi*k_hi)
    deriv_hi=2*pihi*(4*B*chi-8*slo)
    assert center_amp_lo>F(541,1000)
    assert 0<deriv_hi<F(2873,1000)

    # On J± = ±[.297,.303], |hat(Zs)(xi)| is strictly bounded below
    # by (center amplitude lower - global slope upper * radius).
    amp=F(541,1000)-F(2873,1000)*RADIUS
    assert amp>F(53,100)
    E=4*RADIUS*amp*amp
    assert E>F(33,10000)  # actual strict physical odd spectral mass lower

    # Odd parity is essential: for physical odd subspace H_odd,
    # T_J = Z*F^-1 1_J FZ positive trace-class and
    # Tr_Hodd T_J = int_J ||Podd(exp(2*pi*i*xi*x))||² dxi
    # with exact integrand B - sin(4*pi*B*xi)/(4*pi*xi).
    # Since |sin|<=1, pi>3 and |xi|>=LEFT:
    # 0<=T_J|H_odd<=tau I_odd, tau as below.
    tau=4*RADIUS*(B+F(1)/(4*3*LEFT))
    assert F(0)<tau<F(17,1000)<1

    # Original positive supported A=A0+2|cosh><cosh|, on odd H the
    # even pole vanishes, but the SIGNED original multiplier m>1.4
    # on J implies A_odd>=kappa I_odd+delta T_J|H_odd.
    #
    # On [0,tau], f(t)=1/(kappa+delta*t) is convex and beneath its
    # secant line joining t=0 to t=tau:
    # f(t)<=1/kappa - delta*t/[kappa*(kappa+delta*tau)].
    # Operator monotonic inverse and spectral calculus give the actual
    # supported comparison
    # 2<s,A^-1s> <= 2||s||²/kappa -
    #       2delta/[kappa*(kappa+delta*tau)] * <s,T_Js>.
    shB_lo,shB_hi=sinh_bounds(B)
    norm_hi=shB_hi-B
    assert F(0)<norm_hi<F(235648,1000000)
    scalar_upper=2*norm_hi/KAPPA
    gain=2*DELTA*E/(KAPPA*(KAPPA+DELTA*tau))
    new_upper=scalar_upper-gain
    assert gain>F(393,1)
    assert F(0)<new_upper<F(78,1)
    assert new_upper>1  # This *bound* remains far above the BS target.
    assert new_upper<F(412562,1000)

    # The old SI14 single-delta chord assumed ||T_J||<=1.
    # It does not use the much sharper ODD trace tau<0.017. Thus its
    # no-go is specifically about the old comparator, not this one.
    print("SI16 PASS: original supported odd time-bandwidth trace refinement")
    print("inherited signed positive full window min:",float(certify_window()))
    print("narrow symmetric J+:",float(LEFT),float(RIGHT))
    print("center Fourier amplitude rigorous lower:",float(center_amp_lo))
    print("odd Fourier energy E rigorous lower:",float(E))
    print("odd frequency concentration operator trace/norm upper:",float(tau))
    print("strict certified odd-pole inverse BS upper:",float(new_upper))
    print("certified improvement over SI12 scalar floor:",float(gain))
    print("No original full inverse vector, residual Gram, finite BS matrix, Stage I or RH.")


if __name__=="__main__":
    validate()
