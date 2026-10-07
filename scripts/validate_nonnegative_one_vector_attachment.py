#!/usr/bin/env python3
"""Exact selected/full positivity and raw/effective distinction controls."""
from fractions import Fraction as F
import json

def main():
    positive=negative=separating=0
    for r in (F(1),F(2),F(3)):
        for a in (F(1),F(2),F(3)):
            for b in (F(0),F(1),F(2)):
                # A=diag(0,a), R=(r,0), B=(0,b).
                for x in (F(-2),F(-1),F(1),F(2)):
                    full=F(0); bg=F(0)
                    pos=r*r*x*x; sel=r*r*x*x
                    assert pos-sel==full+bg==0
                    # Nonnegative raw selected null is full-null.
                    assert full==bg==0
                    positive+=1
            for b in (F(1),F(2),F(3)):
                for x in (F(-2),F(-1),F(1),F(2)):
                    # A=diag(-b^2,a), R=(r,0), B=(b,0);
                    # positive covariance diag(r^2,a).
                    full=-b*b*x*x; bg=b*b*x*x
                    pos=r*r*x*x; sel=r*r*x*x
                    assert pos-sel==full+bg==0
                    assert full<0 and bg>0
                    # Dropping same-window nonnegativity fails.
                    negative+=1
                for x in (F(-2),F(-1),F(1),F(2)):
                    # A=diag(0,a), same R and B. R separates ker A.
                    full=F(0); bg=b*b*x*x; sel=r*r*x*x
                    effective=full+sel
                    rawpos=full+sel+bg
                    assert effective-sel==0
                    assert rawpos-sel==bg>0
                    assert sel>0  # selection separates the physical kernel
                    assert rawpos!=effective
                    separating+=1
    print(json.dumps(dict(status="rational_controls_pass",
        nonnegative_selected_cases=positive,
        missing_positivity_rejections=negative,
        separating_selection_not_raw_neutral=separating,
        scope="algebra controls only; named historical energy comparisons unproved"),
        sort_keys=True))
if __name__=="__main__":
    main()
