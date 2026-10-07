#!/usr/bin/env python3
"""Critical collar exponent/coefficient audit, not an analytic or Lean certificate."""
from fractions import Fraction as F
import json


def check():
    # Free heat multiplier |xi|^-t belongs to L2 exactly when 2t>1.
    assert 2*F(1)>1
    assert not (2*F(1,2)>1)
    # Integral sqrt(L+z) averaged against exp(-z) is bounded by sqrt(L)(1+1/(2L)).
    for L in (F(1),F(2),F(4),F(16),F(100)):
        assert 1+1/(2*L) <= F(3,2)
        assert 1/(2*L)>0
    physical_hardy_log = F(1)
    inverse_residual_log_growth = F(1,2)
    pairing_log_power = inverse_residual_log_growth-physical_hardy_log/2
    assert pairing_log_power == 0
    # Dropping the critical log leaves an unbounded sqrt(log) loss.
    lost_log_power = inverse_residual_log_growth
    assert lost_log_power > 0
    q = F(3,2)
    hardy_integral_power = 1-2*q
    assert hardy_integral_power < -1
    hardy_tail_power = hardy_integral_power+1
    assert hardy_tail_power/2 == F(-1,2)
    assert not (1-2*F(1)<-1)  # equality cusp does not have a finite critical Hardy tail
    return {
        "scope":"rational threshold/exponent audit only; no analytic or Lean certification",
        "heat_time_used":"1","heat_L2_equality_control_rejected":True,
        "critical_pairing_log_power":"0",
        "critical_Hardy_tail_square_root_tends_to_zero":True,
        "dropped_log_budget_rejected":True,
        "critical_q1_equality_control_rejected":True,
        "inverse_Xcrit_membership_assumed":False,
        "whole_kernel_critical_moment_certified":False,
        "new_aperture_certificate":False,
        "lean_certified":False
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
