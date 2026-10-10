#!/usr/bin/env python3
"""Exact sign-aware polynomial moment enclosures on a common rational grid."""
from fractions import Fraction as F

def outward_moments(moments,grid):
    assert grid>0
    return [(int((F(v.lo)*grid).__floor__()),int((F(v.hi)*grid).__ceil__())) for v in moments]

def integer_dot(coefficients,moments):
    assert len(coefficients)==len(moments)
    lo=hi=0
    for c,(l,h) in zip(coefficients,moments):
        assert isinstance(c,int) and l<=h
        if c>=0:lo+=c*l;hi+=c*h
        else:lo+=c*h;hi+=c*l
    assert lo<=hi
    return lo,hi
