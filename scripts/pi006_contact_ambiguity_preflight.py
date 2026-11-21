#!/usr/bin/env python3
"""PI006 exact-rational identifiability and contact-subtraction preflight.

Tests only algebraic implications and finite-dimensional countermodels.
NO Lean certificate, no inversion theorem, no Masullo trace validation,
no claim that these toy matrices are the true signed Weil form.
"""
from fractions import Fraction as Q
from itertools import product


def gram(B, x, y):
    return sum((x[i] * B[i][j] * y[j] for i in range(2) for j in range(2)), Q())


def dot(x, y):
    return sum((x[i]*y[i] for i in range(2)), Q())


def check_contact_selector_invariance() -> None:
    # If A(eta)-A(xi)=-I(eta-xi) for selectors with eta(0)=xi(0)=1,
    # and R_eta(h)=I(h-h0*eta), then R_eta(h)-h0*A(eta)
    # is independent of the chosen selector.
    for h0, a_eta, a_xi, r_xi in product(
        [Q(-2),Q(0),Q(1,3),Q(5,4)],
        [Q(-3,7),Q(0),Q(7,2)],
        [Q(-8,9),Q(1,5)],
        [Q(-1),Q(0),Q(13,17)],
    ):
        int_eta_minus_xi = -(a_eta-a_xi)
        r_eta = r_xi - h0*int_eta_minus_xi
        assert r_eta-h0*a_eta == r_xi-h0*a_xi


def check_offdiagonal_information_loss() -> None:
    B0=((Q(1),Q(0)),(Q(0),Q(1)))
    Bscalar=((Q(-2),Q(0)),(Q(0),Q(-2)))
    Blocal=((Q(-2),Q(0)),(Q(0),Q(1)))
    e1,e2=(Q(1),Q(0)),(Q(0),Q(1))
    for B in (B0,Bscalar,Blocal):
        assert gram(B,e1,e2) == 0  # pair of disjoint physical cells
    assert gram(B0,e1,e1)>0 and gram(Bscalar,e1,e1)<0
    assert gram(B0,e2,e2)>0 and gram(Blocal,e1,e1)<0

    # Every orthogonal pair has identical entries under a scalar
    # mass shift Bscalar=B0-3*I. Distinct local potential does not.
    vectors=[(Q(i),Q(j)) for i in range(-4,5) for j in range(-4,5)]
    for x in vectors:
        for y in vectors:
            if dot(x,y)==0:
                assert gram(Bscalar,x,y) == gram(B0,x,y)
    x=(Q(1),Q(1))
    y=(Q(1),Q(-1))
    assert dot(x,y)==0
    assert gram(Blocal,x,y) == -3
    assert gram(B0,x,y) == 0


def check_real_place_anchor() -> None:
    # Independent exact normalization from the prior PI004 source test.
    q=Q(9)
    Kpos=Q(3,2)*(Q(1)/(q-1)+Q(1)/(q+1))
    Kneg=Q(1,6)*(q/(q-1)+q/(q+1))
    K=Q(1,3)/(1-Q(1,81))
    assert Kpos == Kneg == K == Q(27,80)


def main() -> None:
    check_contact_selector_invariance()
    check_offdiagonal_information_loss()
    check_real_place_anchor()
    print("PI006 EXACT RATIONAL PREFLIGHT: PASS")
    print("Contact-subtraction selector invariance: identity checked")
    print("Orthogonal-pair scalar-mass ambiguity: verified on exhaustive rational grid")
    print("Disjoint-support local-multiplier ambiguity: verified")
    print("Nonmatching inertia despite equal disjoint off-diagonals: verified")
    print("Original real-place kernel anchor K(+/-log9): 27/80")
    print("NOT CHECKED: source-specific gamma inversion, Masullo operator, Lean, RH")


if __name__ == "__main__":
    main()
