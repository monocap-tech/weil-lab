#!/usr/bin/env python3
"""Exact scaling/gap controls for the localization-ceiling audit."""
from fractions import Fraction as F
import json

def main():
    scaling=ceiling=gap=0
    delta=F(3,10**29)
    for N in range(2,7):
        for L in range(2,34):
            bound=F(1,L**(2*N-1))
            assert bound==F(L,L**(2*N))<=F(1,L**3)
            scaling+=1
    # Conditional spectral/local sequences; no actual zero data.
    for L in range(2,130):
        native=F(1,L**3)
        local=delta+1-F(1,L)
        defect=local-native
        assert native>0 and local>=delta
        assert defect>delta
        ceiling+=1
    # A shifted far tail is controlled by the existing quartic height weight.
    for omega in (F(-3,2),F(-1,2),F(1,2),F(3,2)):
        for theta in range(-20,21):
            if abs(theta)>=max(2*abs(omega),1):
                distance=abs(F(theta)-omega)
                assert distance>=F(abs(theta),2)>=F(1+abs(theta),4)
                assert 1/distance**4<=F(256,(1+abs(theta))**4)
                gap+=1
    print(json.dumps(dict(status="rational_controls_pass",
        scaling_cases=scaling, ceiling_rejections=ceiling,
        shifted_tail_cases=gap,
        scope="algebra only; analytic actual zero-gap argument not Lean certified"),
        sort_keys=True))
if __name__=="__main__":
    main()
