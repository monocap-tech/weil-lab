#!/usr/bin/env python3
"""Rational critical signed-remainder audit only; not an analytic or Lean proof."""
from fractions import Fraction as F
import json


def check():
    B,s,r = F(3,8),F(1,4),F(1)
    pole_margin = 2-r
    cross_margin = 1+2*s-r
    assert pole_margin==1 and cross_margin==F(1,2)
    pole_coefficient = B*B/(2*pole_margin)
    cross_coefficient = 2*B/cross_margin
    assert pole_coefficient==F(9,128)
    assert cross_coefficient==F(3,2)
    assert r==2*F(1,2)  # critical source/Fourier order
    assert not (1+2*F(0)-r>0)  # no subcritical cross moment loses integrability
    return {
        "scope":"exact coefficient/exponent controls only; no analytic or Lean certificate",
        "transverse_bound":"3/8","source_order":"1","subcritical_s":"1/4",
        "cross_integral_margin":"1/2","pole_coefficient":"9/128",
        "cross_coefficient":"3/2","lost_cross_margin_control_rejected":True,
        "actual_eigenvector_numerically_computed":False,
        "zero_contact_critical_bound_certified":False,
        "new_aperture_certificate":False,"lean_certified":False
    }


if __name__ == "__main__":
    print(json.dumps(check(),indent=2,sort_keys=True))
