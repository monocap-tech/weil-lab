#!/usr/bin/env python3
"""Signed cutoff budget controls; no arithmetic source trace estimate."""
from fractions import Fraction as F
from itertools import product
import json

def main():
    exponent=trace=0
    for r in (F(1,2),F(1),F(5,4),F(3,2),F(7,4),F(15,8)):
        # s=r/4 is subcritical and 1+2s-r=1-r/2>0.
        s=r/4
        assert 0<s<F(1,2) and 2-r>0 and 1+2*s-r>0
        exponent+=1
    assert 1+2*F(3,8)-F(3,2)==F(1,4)
    assert 2-F(2)==0  # cannot integrate the t^2 remainder at r=2.
    for w,L,b,d in product((F(0),F(1),F(8),F(64)),
                           (F(0),F(1),F(3)),
                           (F(0),F(1,4),F(1,2)),range(1,9)):
        # e >= w/2-L, with a nonnegative excess b*w.
        e=w/2-L+b*w
        assert e>=w/2-L
        assert d*e>=d*w/2-d*L
        assert e>=-L
        trace+=1
    # Fixed epsilon sums converge; explicit bounded multipliers preserve l2.
    finite=0
    for n in range(1,129):
        p=sum(F(1,2**j) for j in range(1,n+1))
        assert p<1
        bound=F(2**n)
        weighted=sum(bound*F(1,2**j) for j in range(1,n+1))
        assert weighted<bound
        finite+=1
    print(json.dumps(dict(status="rational_controls_pass",
        exponent_cases=exponent,trace_comparison_cases=trace,
        fixed_cutoff_cases=finite,scope="budget controls; no actual finite-liminf theorem"),
        sort_keys=True))
if __name__=="__main__": main()
