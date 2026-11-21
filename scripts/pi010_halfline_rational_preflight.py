#!/usr/bin/env python3
"""PI010 exact-rational algebraic check for complex Fourier half-line pair.

Not a Lean kernel proof, not a numerical approximation of an integral.
Checks exact rational complex reciprocals and equality to PI008 Gamma atom.
"""
from fractions import Fraction as F


def reciprocal(a: F, b: F) -> tuple[F, F]:
    """1/(a+i*b), returned as rational real and imaginary parts."""
    denom = a*a+b*b
    assert denom > 0
    return a/denom, -b/denom


def main() -> None:
    count=0
    for n in range(128):
        alpha=2*F(n)+F(1,2)
        a=F(n)+F(1,4)
        assert alpha == 2*a and alpha>0
        for r in (F(-5),F(-3,2),F(-1,7),F(0),F(2,9),F(9)):
            pos=reciprocal(alpha,-r)
            neg=reciprocal(alpha,r)
            combined=(pos[0]+neg[0],pos[1]+neg[1])
            expected=2*alpha/(alpha*alpha+r*r)
            digamma_atom=a/(a*a+(r/2)**2)
            assert combined == (expected,F(0))
            assert expected == digamma_atom
            count+=1

    assert count==768
    print("PI010 INDEPENDENT FRACTION PREFLIGHT: PASS")
    print("768 parameter pairs: complex half-line sum and PI008 atom agree")
    print("No floating-point inputs or fabricated Fourier integrals")
    print("NOT checked: actual Lean build/axioms, full-real-line split, Masullo trace, RH")


if __name__=="__main__":
    main()
