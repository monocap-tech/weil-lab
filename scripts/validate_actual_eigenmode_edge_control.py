#!/usr/bin/env python3
"""Exact eigenmode subtraction/sign controls; no native eigenvector computation."""
from fractions import Fraction as F
import json

def main():
    mus=(F(3,10**29),F(1,10),F(1),F(2),F(10))
    flux=derivative=gaussian=0
    for mu in mus:
        for H2 in (F(1),F(2),F(3)):
            for Dmass in (F(0),F(1,8),F(1,4),F(1,2),F(1)):
                Dm=F(7,3); P=F(-2); cosh_minus=F(1,8)
                full=mu*H2-Dm+cosh_minus*P
                interior=mu*(H2-Dmass)
                outside=full-interior
                assert outside==-(Dm-mu*Dmass)+cosh_minus*P
                # The unshifted full action is not the exterior action.
                if Dmass<H2:
                    assert outside!=full
                flux+=1
        for P in range(-6,7):
            Hprime2=F(5,2)
            # J=pi^2 integral xi^2 (m-mu)|hhat|^2.
            J=F(P,16)
            Junshifted=J+mu*Hprime2/4
            assert 4*Junshifted-F(P,4)==mu*Hprime2
            assert -2*J+F(P,8)==0
            derivative+=1
        for M in (F(0),F(1,3),F(2)):
            for I in (F(-2),F(0),F(5)):
                for pole in (F(-1),F(0),F(1)):
                    actual=I+pole
                    exterior=actual-mu*M
                    assert exterior==(I-mu*M)+pole
                    gaussian+=1
    print(json.dumps(dict(status="rational_controls_pass",
        flux_subtraction_cases=flux, shifted_derivative_cases=derivative,
        gaussian_subtraction_cases=gaussian,
        scope="algebra only; no computed eigenmode or endpoint exclusion"),
        sort_keys=True))

if __name__ == "__main__":
    main()
