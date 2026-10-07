#!/usr/bin/env python3
"""Exact sign, pole and rate controls. No actual arithmetic flux bound."""
from fractions import Fraction as Q
import json

def main():
    pole=cosine=rates=0
    # Full-null derivative diagonal: 4*pi^2 I - P/4=0.
    # Store J=pi^2 I to keep arithmetic rational.
    for P in range(-32,33):
        J=Q(P,16)
        assert 4*J-Q(P,4)==0
        assert -2*J+Q(P,8)==0
        # Both integration-by-parts signs are needed.
        assert Q(1,2)*Q(-1,2)==Q(-1,4)
        pole+=1
    for n in range(1,129):
        u=Q(n,128)
        floor=u*u/2-u**4/24
        assert floor>=Q(11,24)*u*u>=u*u/4
        # cosh(t/2)-1 has leading coefficient 1/8.
        t=u
        assert t*t/8+t**4/384 <= t*t/4
        cosine+=1
    # Negative first-order or C1 flat controls obey an upper bound zero.
    # For t=1/n^2, -t^(3/2)/t^2=-n still diverges negatively.
    for n in range(2,130):
        t=Q(1,n*n)
        flat=-Q(1,n**3)
        regular=-t**3
        assert flat<=0 and flat/(t*t)==-n
        assert regular/(t*t)==-t
        # A trace with one regular and one rough mode cannot cancel.
        assert (flat+regular)/(t*t)==-n-t
        # Sign reversal would accept the rough control incorrectly.
        assert flat<=t*t and not flat>=-t*t
        rates+=1
    print(json.dumps(dict(status="rational_controls_pass",
        pole_cancellation_cases=pole, cosine_coefficient_cases=cosine,
        signed_rate_cases=rates,
        scope="controls only; actual quadratic lower subsequence unproved"),
        sort_keys=True))

if __name__ == "__main__":
    main()
