#!/usr/bin/env python3
"""SM06-T: full positive Legendre degree>=2 residual of one signed band.

Exact rational Banach/Parseval tail operator norm. This does NOT bound the
full original negative multiplier on the interval, only its uniform
certified delta=7/5 lower-mass component; do not claim full K control.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import PI, B
from validate_rpb108_sm03_negative_packet_reference_nogo import (
    C as CENTER, RADIUS as R, DELTA
)

def validate():
    assert CENTER==F(147,40) and R==F(3,100)
    assert DELTA==F(7,5) and B==F(11,10)
    assert PI[1]<F(22,7)

    # H_o = L2([-B,B])_odd. h_xi(x)=sin(2π ξ x).
    # The full constant-delta original signed negative packet operator
    # is T_delta=2 delta int_[c-r,c+r] |h_xi><h_xi| dxi.
    # Let P_Legendre project L2([-1,1],du/2) onto span{1,u}.
    # For any physical f, v(u)=<f,h_(c+ru)>.
    # The first two *exact* Legendre coefficients give
    # T_delta= gamma0 |g0><g0|+gamma1 |g1><g1|+R_>=2
    # with R_>=2 >=0. Since P_Legendre is an orthogonal projection,
    # its error is <= the L2 error of the affine Taylor polynomial
    # v(0)+r*u*v'(0), and
    # |v(u)-v(0)-r*u*v'(0)| <= r^2 u^2/2 * ||f|| ||h''||.
    # ||h''_xi||² <= (2π)^4 int_[-B,B] x^4 dx
    #                 = (2π)^4 2 B^5/5.
    # E[u^4]=1/5. Multiply 4*r*delta to obtain the bound.
    gamma0=4*R*DELTA
    gamma1=gamma0/3
    operator_tail_upper=(DELTA*R**5*(2*PI[1])**4*2*B**5)/25
    assert gamma0==F(21,125) and gamma1==F(7,125)
    assert operator_tail_upper>0
    assert operator_tail_upper < F(7,10**6), (
        "SM06 constant signed band higher moments require sharper bound",
        float(operator_tail_upper)
    )
    # If a 3-source finite BS certificate gives normalized λ_max<0.993,
    # the remaining positivity margin ≥(1-λ)*kappa>7e-6
    # absorbs THIS entire constant-delta continuum residual.
    kappa=F(1,1000)
    gate=F(993,1000)
    assert (1-gate)*kappa == F(7,10**6)
    assert operator_tail_upper < (1-gate)*kappa
    print("SM06-T PASS: original signed interval's UNIFORM delta-band Legendre >=2 tail norm <",float(operator_tail_upper),flush=True)
    print("SM06-T mean/first moment exact weights:",float(gamma0),float(gamma1),flush=True)
    print("SM06-T conditional three-source BS row ceiling needed:",float(gate),flush=True)
    print("SM06-T excludes extra actual r(xi)-delta on J and all other signed-negative intervals; W-ODD-NEG OPEN.",flush=True)

if __name__=="__main__":
    validate()
