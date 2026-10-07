#!/usr/bin/env python3
"""Finite supported-walk checks; not a density, analytic regularity or Lean certificate."""
from fractions import Fraction as F
import json
from certify_native_drive_cusp_geometry import log_interval


def check():
    a = F(97,100)
    A, B = log_interval(2), log_interval(3)
    width = A[0]+B[0], A[1]+B[1]
    assert width[1] < 2*a
    assert A[1] < width[0]
    assert not (width[1] < 2*F(4,5))  # narrow strip cannot contain this rotation
    m,n = 0,0
    counts = {"prime2_negative_step":0,"prime3_positive_step":0}
    for step in range(1024):
        # y=m log2+n log3, with m>=0 and n<=0 throughout.
        assert m>=0 and n<=0
        lo,hi = m*A[0]+n*B[1], m*A[1]+n*B[0]
        assert 0 <= lo <= hi < width[0]
        if hi < B[0]:
            m += 1
            counts["prime2_negative_step"] += 1
        else:
            assert lo > B[1], "log enclosure cannot resolve rotation branch"
            n -= 1
            counts["prime3_positive_step"] += 1
        newlo,newhi = m*A[0]+n*B[1], m*A[1]+n*B[0]
        assert 0 < newlo <= newhi < width[0]
        assert -a < a-newhi <= a-newlo < a
    assert all(counts.values())
    # Omitting the prime3 return from a point y>beta leaves the strip.
    witness = (B[1]+width[0])/2
    assert witness > B[1] and witness+A[0] > width[0]
    return {"scope":"finite exact supported-walk and threshold checks only",
            "reused_frontier":"97/100","verified_steps":1024,
            "step_counts":counts,"final_integer_coordinate":[m,n],
            "narrow_strip_control_rejected":True,
            "omitted_prime3_return_control_rejected":True,
            "infinite_density_computationally_certified":False,
            "actual_singular_null_vector_claimed":False,
            "critical_derivative_gate_closed":False,
            "new_aperture_certificate":False,"lean_certified":False}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
