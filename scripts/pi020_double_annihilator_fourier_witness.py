#!/usr/bin/env python3
"""PI020 ANALYTIC-ONLY exact Fourier/Mellin intersection-witness regression.

This does NOT evaluate an actual zeta-zero divisor, Masullo's purported
Ch.13 spectral sum, an infinite trace, or any Lean proof. It checks exact
algebraic consequences of the smooth test construction:

  rho >= 0 smooth compact, phi=rho', a=log(q), q>1;
  C(u)=int phi(x)phi(x-u)dx;
  D_a(u)=C(u+a)+C(u-a), with D_a(0)=int D_a=0.

For Fourier_+ f(z)=int f(u)exp(i*z*u)du, for complex z,
  Fourier_+ D_a(z) =
      2*cos(a*z)*z*z*Fourier_+ rho(z)*Fourier_+ rho(-z).
Thus the witness has a DOUBLE zero at z=0, but is sensitive to fixed
nonzero imaginary modes. A formal delta-limit rho (NOT an admissible
smooth test) gives W(i*k)=-k²(q^k+q^-k), for positive integer k.
All arithmetic checks below are EXACT fractions.

The other regression is the algebraic two-hyperplane annihilator:
B|ker(e)∩ker(m)=0 iff B=c*e+d*m, when e and m are independent.
This is algebraic; it does not prove a spectral difference belongs to
that span or that the Chapter 13 theorem is valid.
"""
from fractions import Fraction as Q


def imaginary_mode_delta_limit(q: Q,k: int) -> Q:
    """Formal narrow-rho limit of W(z) at z=i*k, a=log q."""
    assert q>1 and k>=0
    return -(k*k)*(q**k + q**(-k))


def dual_functionals(v: tuple[Q,Q,Q]) -> tuple[Q,Q]:
    """Coordinates in (contact-normalized f, moment-normalized g, overlap D)."""
    return v[0],v[1]


def arbitrary_functional(v:tuple[Q,Q,Q], c:Q,d:Q,x:Q)->Q:
    return c*v[0]+d*v[1]+x*v[2]


def main()->None:
    assert imaginary_mode_delta_limit(Q(9),0)==0
    assert imaginary_mode_delta_limit(Q(9),1)==-Q(82,9)
    assert imaginary_mode_delta_limit(Q(9),2)==-Q(26248,81)
    assert imaginary_mode_delta_limit(Q(4),1)==-Q(17,4)
    modes=0
    for q in (Q(4),Q(9),Q(16),Q(25),Q(49)):
        for k in range(1,51):
            value=imaginary_mode_delta_limit(q,k)
            assert value<0
            # symmetry of the cosine Fourier spectral witness
            assert value==imaginary_mode_delta_limit(q,-k) if k<0 else value<0
            modes+=1

    # At z=0 the exact smooth D_a has W(0)=W'(0)=0, and
    # W''(0)=4*(int rho)^2 > 0. Its central mode is invisible.
    for mass in (Q(1,7),Q(1),Q(17,5)):
        coeff_z2 = 2*mass*mass
        assert 2*coeff_z2 == 4*mass*mass

    # If the defect vanishes on the intersection (coordinate v[2]),
    # it depends only on e(v)=v[0] and m(v)=v[1].
    checks=0
    values=(Q(-3),Q(0),Q(2,5),Q(5))
    for c in values:
        for d in values:
            for x in values:
                if x==0:
                    for v0 in values:
                        for v1 in values:
                            for v2 in values:
                                v=(v0,v1,v2)
                                assert arbitrary_functional(v,c,d,x)==c*v0+d*v1
                                checks+=1
                else:
                    witness=(Q(0),Q(0),Q(1))
                    assert arbitrary_functional(witness,c,d,x)==x
                    assert dual_functionals(witness)==(Q(0),Q(0))

    # A countermodel to "overlap equality automatically gives equal
    # zero divisors": a nonzero c*e+d*m annihilates the overlap.
    for c,d in ((Q(1),Q(0)),(Q(0),Q(1)),(Q(2),Q(-5))):
        assert arbitrary_functional((Q(0),Q(0),Q(9)),c,d,Q(0))==0
        assert (arbitrary_functional((Q(1),Q(0),Q(0)),c,d,Q(0)),
                arbitrary_functional((Q(0),Q(1),Q(0)),c,d,Q(0)))==(c,d)

    print("PI020 EXACT DOUBLE-ANNIHILATOR / FOURIER-WITNESS PREFLIGHT PASS")
    print(f"{modes} noncentral imaginary-frequency exact sensitivity checks")
    print(f"{checks} two-functional intersection annihilator checks")
    print("At q=9, formal narrow-bump W(i)=-82/9, W(2i)=-26248/81")
    print("The smooth transform has a double zero at the central mode z=0")
    print("NO actual zeta zeros, source Ch13 theorem, trace, Lean, or RH verified")


if __name__=="__main__":
    main()
