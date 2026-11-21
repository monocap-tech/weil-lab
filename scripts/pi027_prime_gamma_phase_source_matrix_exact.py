#!/usr/bin/env python3
"""PI027 exact rational source-phase / prime-isolation regression ONLY.

Genuine smooth theory (see matching PI027 memo):
  rho >=0, nonzero in Cc-infinity((0,d)), d=log(10/9);
  phi_m = D prod_(j<m)(D^2-(2j+1/2)^2) rho;
  C_m(u)=int phi_m(x)phi_m(x-u)dx, J=C_m(0)>0;
  s_beta,a=(phi_m+beta phi_m(.-a))/sqrt2.
Original signed Weil:
  W(h_beta,a)=W(C_m)+(B_m(a)-P_m(a))*Re(beta)
where B_m(a)=-int C_m(v)K(a+v)dv>0 for a>d,
P_m(a)=sum_(n>=2) Lambda(n)/sqrt(n)*C_m(log(n)-a).

At a=log(9/4), P=0, B>0.
At a=log3, P=(log3/sqrt3)*J, and B<J/9, P>J/3,
thus B-P<-2J/9.
At a=log9, P=(log3/3)*J and B<J/18, P>2J/9,
thus B-P<-J/6.

A continuous zero a* must therefore lie between log(27/10)
(the LEFT edge of the first n=3 sampling window) and log3.
This script checks exact rational inequalities/sign algebra and
finite positive Gamma coefficients. The logarithmic and smooth
analytic inequalities are PROVED in the memo and are not evaluated
numerically or replaced by floating-point tests.
No authentic zeta zeros, actual Masullo operator, Lean or Actions.
"""
from fractions import Fraction as Q
from functools import reduce

D_EXP=Q(10,9)
Q_GAP=Q(9,4)
Q_PRIME3=Q(3)
Q_PRIME9=Q(9)


def lam(n:int)->Q:
    return Q(2*n)+Q(1,2)


def gamma_poly(m:int,n:int)->Q:
    z=lam(n)
    return z*z*reduce(lambda x,j:x*(z*z-lam(j)**2)**2,range(m),Q(1))


def square_shift_weight(q:Q,n:int)->Q:
    """rational q^(-2n), omitting positive q^(-1/2)"""
    return q**(-2*n)


def main()->None:
    # Exact integer/prime-power sample windows; supports are OPEN
    # and their boundary samples therefore vanish.
    assert Q(2)<Q_GAP/D_EXP==Q(81,40)
    assert Q_GAP*D_EXP==Q(5,2)<Q(3)
    assert Q(2)<Q_PRIME3/D_EXP==Q(27,10)<Q(3)
    assert Q_PRIME3*D_EXP==Q(10,3)<Q(4)
    assert Q(8)<Q_PRIME9/D_EXP==Q(81,10)<Q(9)
    assert Q_PRIME9*D_EXP==Q(10)
    assert Q(2)<Q(27,10)/D_EXP==Q(243,100)
    assert Q(27,10)*D_EXP==Q(3)
    print("PI027 exact source support windows / first n=3 interaction: PASS")

    # Elementary ANALYTIC inequalities supported by rational checks:
    # log(10/9)<1/9; log3>2/3;
    # sqrt(3)<2; K(log2)=2sqrt2/3<1 (squared: 8/9<1);
    # K(log8)=16sqrt2/63<1/2 (squared: 512/3969<1/4).
    assert Q(8,9)<Q(1)  # K(log2)^2
    assert Q(512,3969)<Q(1,4)  # K(log8)^2
    assert Q(3)<Q(4)  # sqrt3<2
    d_bound=Q(1,9)
    b3_bound=d_bound*Q(1)       # B(log3)/J < 1/9
    kappa3_lower=Q(2,3)/Q(2)   # (log3)/sqrt3 > 1/3
    assert b3_bound-kappa3_lower==-Q(2,9)
    b9_bound=d_bound*Q(1,2)     # B(log9)/J < 1/18
    kappa9_lower=Q(2,3)/Q(3)   # (log3)/3 > 2/9
    assert b9_bound-kappa9_lower==-Q(1,6)
    assert 2*(b3_bound-kappa3_lower)==-Q(4,9)
    assert 2*(b9_bound-kappa9_lower)==-Q(1,3)
    print("PI027 rigorous sign-gap rational bounds: PASS")
    print("  W_3(h+)-W_3(h-) < -(4/9)*J")
    print("  W_9(h+)-W_9(h-) < -(1/3)*J")

    coefficients=0
    for m in range(1,9):
        for j in range(m):
            assert gamma_poly(m,j)==0
        for n in range(m,m+50):
            p=gamma_poly(m,n)
            assert p>0
            # Both exact rational-square source q=9/4 and q=9
            # have explicitly strictly positive physical mode terms.
            assert square_shift_weight(Q_GAP,n)*p>0
            assert square_shift_weight(Q_PRIME9,n)*p>0
            coefficients+=2
    assert coefficients==800
    print(f"PI027 {coefficients} exact positive Gamma-mode controls: PASS")

    # Fully exact formal phase linearity and independent original
    # source/Ch12/Ch13 (CONDITIONAL) channel matrix. Generic rational
    # amplitudes are TEST VALUES, not evaluations of smooth integrals.
    phases=[Q(1),Q(-1),Q(0),Q(3,5),Q(-3,5),Q(5,13),Q(-5,13)]
    check=0
    for B,P,base in [
        (Q(7,4),Q(0),Q(1,3)),
        (Q(1,20),Q(2,5),Q(-3,7)),
        (Q(1,25),Q(1,3),Q(2)),
        (Q(1,13),Q(2,7),Q(0)),
    ]:
        for rb in phases:
            # Diagonal W baseline + (Gamma - Prime)*Re(beta)
            W=base+(B-P)*rb
            assert W-base==(B-P)*rb
            # For D=h+ -h- the real difference is exactly 2*(B-P).
            Z12=2*(B-P)
            Z13=4*B-2*P
            assert Z13-Z12==2*B
            assert Z12==2*B-2*P
            assert W-(base+(B-P)*rb)==0
            check+=1
    assert check==28
    print("PI027 28 exact diagonal source/conditional spectral channel checks: PASS")

    # On the cancellation locus P=B>0:
    for B in (Q(1,100),Q(4,9),Q(7,3)):
        assert 2*(B-B)==0
        assert 4*B-2*B==2*B>0
    print("PI027 cancellation locus: original W(D)=0, literal Ch13 requires 2B>0")
    print("No actual zeta-zero sum or Ch13 trace theorem has been proved.")


if __name__=="__main__":
    main()
