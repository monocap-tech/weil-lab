#!/usr/bin/env python3
"""EF03: entire ORIGINAL signed-negative EVEN upper operator / coupled tail.

Full original seven-prime SI10 rational frequency cover. Retains every
negative-frequency interval, includes the kappa height correction, forms the
physical EVEN cosine Taylor carrier, and pays all low/high coupling through
Young's Loewner inequality. Computes necessary finite-gate budget, but does
NOT compute the actual supported A_e inverse matrix/eigenvalue or close RH.
"""
from fractions import Fraction as F

from validate_rpb108_si10_complement_positivity import (
    KAPPA, protected_inner_cover, protected_outer_band,
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si06_negative_band import B

DIMENSION_CEILINGS = {20: 780, 24: 890, 32: 1075}
TAU_CHOICE = {20: F(1,1024), 24: F(1,65536), 32: F(1,65536)}


def cross_term_sign_regression():
    """A finite rational witness that low/high cross terms cannot vanish."""
    # R=(1,1) and P=diag(1,0), K=R* R
    K = [[F(1),F(1)],[F(1),F(1)]]
    naive = [[F(1),F(0)],[F(0),F(1)]]
    x = (F(1),F(1))
    q = lambda A: sum(x[i]*A[i][j]*x[j] for i in range(2) for j in range(2))
    assert q(K)==4 and q(naive)==2
    for tau in (F(1,4),F(1,1024),F(1,65536)):
        young = [[1+tau,F(0)],[F(0),1+1/tau]]
        assert (1+tau)*(1+1/tau)-1 > 0
        assert q(young) >= q(K)
        # Exact matrix Loewner determinant for Young - K:
        diff11=young[0][0]-K[0][0]
        diff22=young[1][1]-K[1][1]
        off=young[0][1]-K[0][1]
        assert diff11>0 and diff22>0 and diff11*diff22-off**2 == 0


def validate():
    outer_count,outer_min=protected_outer_band()
    assert outer_count==2535 and outer_min>KAPPA
    groups,width,mass,leaves,protected=protected_inner_cover()
    assert len(groups)==107 and leaves==973 and protected==9261
    assert width==F(973,32) and mass==F(1203060883,32000000)
    assert KAPPA==F(1,1000) and B==F(11,10)

    # All reflected frequencies; original r=(kappa-m)_+ <= w, including
    # when m is positive but less than kappa.
    cap_mass=mass+KAPPA*width
    assert cap_mass==F(1204033883,32000000)
    assert F(37)<cap_mass<F(38)
    print("EF03 original full signed upper envelope mass:",float(cap_mass),flush=True)

    for bits,dim in DIMENSION_CEILINGS.items():
        orders=[taylor_order(hi-lo,bits)[0] for lo,hi,_ in groups]
        d=sum(orders)
        assert d==dim
        # Even physical projected derivatives ∂^k_ξ cos(2πξx)|_{center}.
        # All are even in x, mirror clusters require no second column.
        eps2=2*B*cap_mass*F(1,2**(2*bits))
        tau=TAU_CHOICE[bits]
        delta=(1+1/tau)*eps2
        relative=delta/KAPPA
        # Finite sufficient gate:
        # (1+tau)*lambda_max(Kcap,P^1/2 U* A_e^-1 U Kcap,P^1/2)
        #  + delta/KAPPA <=1.
        allowed=(1-relative)/(1+tau)
        assert eps2>0 and delta>eps2 and 0<allowed<1
        print("EF03 bits",bits,"even physical rank <=",d,
              "tau",str(tau),"cap tail epsilon^2",float(eps2),
              "Young whole-tail",float(delta),
              "Young/kappa",float(relative),
              "finite cap inverse gate lambda <=",float(allowed),
              flush=True)
        if bits==20:
            assert tau==F(1,1024) and relative<F(78,10**6)
            assert allowed>F(9989,10000)
        if bits==24:
            assert tau==F(1,65536)
            assert delta<F(193,10**10)        # <1.93e-8
            assert relative<F(193,10**7)      # <1.93e-5
            assert allowed>F(99996,100000)   # >0.99996
            # Convenient rational *sufficient* threshold on the *unknown*
            # finite full-supported cap Gram eigenvalue, not its measured value.
            assert (1+tau)*F(9999,10000)+relative<1
            assert (1+tau)*F(99996,100000)+relative<1
            print("EF03 b24 sufficient *conditional* finite cap lambda <=0.99996",
                  flush=True)
        if bits==32:
            assert relative<F(3,10**10)
            assert allowed>F(99998,100000)

    # Same b=24, other SM09 tau: EF03's smaller tau improves finite
    # threshold, though it increases the still-rigorous infinite tail.
    e24=2*B*cap_mass*F(1,2**48)
    oldtau=F(1,1024)
    oldallowed=(1-(1+1/oldtau)*e24/KAPPA)/(1+oldtau)
    newtau=TAU_CHOICE[24]
    newallowed=(1-(1+1/newtau)*e24/KAPPA)/(1+newtau)
    assert newallowed>oldallowed+F(9,10000)

    cross_term_sign_regression()
    print("EF03 PASS (REDUCTION ONLY): full original signed EVEN negative",
          "continuum dominated by finite physical upper cap plus rigorous",
          "Young-paid infinite tail, all cross terms retained.",flush=True)
    print("W-EVEN-FORM OPEN: finite cap true A_e supported inverse/eigenvalue",
          "uncertified; no whole form, Lean or RH claim.",flush=True)


if __name__=="__main__":
    validate()
