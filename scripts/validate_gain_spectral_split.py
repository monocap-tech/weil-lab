#!/usr/bin/env python3
"""Exact rate-split controls; no actual response or arithmetic certificate."""
from fractions import Fraction as F
import json

def main():
    cases=0
    assert F(1,2)-F(1,24)==F(11,24)>F(1,4)
    for a in (F(-3,4),F(-1,2),F(0),F(1,2),F(3,4)):
        for n in (2,4,8,16,32,64):
            s=F(1,n)
            det=1-a*a; trace=s+1/s
            discr=trace*trace-4*det
            assert det>0 and discr==(s-1/s)**2+4*a*a>=0
            assert det/trace<=s and 1/s<=trace
            # v=(1,s), a varying vector outside the regular line.
            moving=s+2*a*s+s*s/s
            assert moving==2*(1+a)*s>0
            # Fixed rough vector (1,1): divergence is driven by 1/s.
            fixed=s+2*a+1/s
            assert fixed>=1/s-F(3,2)
            cases+=1
    print(json.dumps({'status':'rational_controls_pass','matrix_rate_cases':cases,
                      'cosine_floor':'11/24 > 1/4',
                      'scope':'algebra/rate controls only; sequencewise actual arithmetic bound unproved'},sort_keys=True))

if __name__=='__main__': main()
