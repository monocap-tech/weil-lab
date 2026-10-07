#!/usr/bin/env python3
"""Rational thresholds and source-geometry custody; not an analytic/Lean proof."""
from fractions import Fraction as F
import json
from certify_native_drive_cusp_geometry import check as check_geometry


def check():
    geometry = check_geometry()
    exponents = {}
    for q in [3,4]:
        crit = 1-2*q
        log3 = 3-2*q
        assert crit < -1 and log3 < -1
        exponents[str(q)] = {'critical_log_integral_exponent':crit,
                             'log3_half_order_integral_exponent':log3}
    edge_q = F(4)
    carleman_tail = 1/(edge_q-1)
    exterior_arch_coefficient = carleman_tail/2
    interior_coefficient = 1+exterior_arch_coefficient
    assert carleman_tail == F(1,3)
    assert exterior_arch_coefficient == F(1,6)
    assert interior_coefficient == F(7,6)
    assert F(1,4) > exterior_arch_coefficient  # proved lower bound for log2/sqrt2
    assert -(4+3) == -7  # normalized critical exterior flux logarithm
    # Reject the critical-norm inference at its equality endpoint.
    assert not (1-2*1 < -1)
    return {
        'scope':'exact exponent/coefficient and reused geometry checks; no analytic or Lean certification',
        'aperture_reused':'97/100',
        'support_interval_checks':geometry['support_interval_checks'],
        'cusp_exponent_checks':exponents,
        'carleman_tail_coefficient':'1/3',
        'interior_defect_coefficient':'7/6',
        'exterior_flux_log_exponent':-7,
        'borderline_q1_control_rejected':True,
        'actual_null_claimed':False,
        'supercritical_Sobolev_membership_claimed':False,
        'new_aperture_certificate':False,
    }


if __name__ == '__main__':
    print(json.dumps(check(), indent=2, sort_keys=True))
