#!/usr/bin/env python3
"""NF20 strict hidden-residual controls with fixed first-two bounds.

Pure rational models, not original zeta native matrices. Show that one can
retain a positive high floor and the measured R2 brackets while the full
corrected sign is positive, null or negative. No arithmetic nonimplication
from the complete original Weil identities is claimed.
"""
from fractions import Fraction as F
import json

def controls():
    out=[]
    for p,b1,b2,lo,hi in [
        ("even",F(4514,10000),F(3150,10000),F(302,1000),F(303,1000)),
        ("odd",F(4535,10000),F(2634,10000),F(275,1000),F(276,1000))]:
        r=b1*b1+b2*b2
        assert lo<r<hi
        assert F(207,1000)<1
        row=[]
        for factor,required in [(F(1,2),"positive"),(F(1),"null"),(F(2),"negative")]:
            # The original first two high couplings remain fixed;
            # the previously unmeasured third high mode is altered.
            h=(1-r)/factor
            b3=1-r
            assert h>F(207,1000)
            sign=1-r-b3*b3/h
            assert (sign>0 if required=="positive" else sign==0 if required=="null" else sign<0)
            row.append(dict(unmeasured_reaction_factor=str(factor),
                third_high_diagonal=str(h),signed_remaining=str(sign),sign=required))
        out.append(dict(parity=p,first_two_reaction=str(r),cases=row))
    # Complete physical positive-level shift control: both diagonals move.
    mu=F(1,10**40);cross=1-mu
    assert 1-cross*cross>0
    assert (1-mu)*(1-mu)-cross*cross==0
    assert 1-mu>F(207,1000)
    return dict(status="PASS",checked_cases=6,unchanged_positive_first_two_response=True,
        high_physical_floor="207/1000",exact_hidden_crossing_controls=out,
        positive_level_shift_is_distinct_from_original_null=True,
        genuine_original_Weil_counterexample=False,whole_aperture_positive=False)

if __name__=="__main__":print(json.dumps(controls(),indent=2))
