#!/usr/bin/env python3
"""Exact coefficient checks only; not an analytic or Lean proof."""
from fractions import Fraction as F
import json


def coefficients(q):
    if q <= 1:
        raise ValueError("absolute center inverse moment requires q>1")
    c = 1/(2*(q-1))
    return ((1+c,c),(c,1+c))


def check():
    rows = []
    for q in (F(3,2), F(2), F(3), F(4), F(17,3)):
        B = coefficients(q)
        sym = q/(q-1)
        assert B[0][0]+B[0][1] == sym
        assert B[0][0]-B[0][1] == 1
        assert B[0][0]*B[1][1]-B[0][1]*B[1][0] == sym
        endpoint = (2*q-1)/(2*(q-1))
        assert B[0][0] == endpoint > 0
        # Tail cancellation by opposite amplitudes leaves a nonzero residual.
        assert B[0][0]-B[0][1] != 0
        rows.append({"q":str(q), "symmetric_eigenvalue":str(sym),
                     "antisymmetric_eigenvalue":"1",
                     "inward_endpoint_coefficient":str(endpoint)})
    for invalid in (F(1), F(1,2)):
        try:
            coefficients(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid inverse-moment regime accepted")
    return {"scope":"rational coefficient checks; no analytic or Lean certification",
            "coefficients":rows, "invalid_q_regimes_rejected":True,
            "general_kernel_classification_claimed":False,
            "critical_derivative_gate_closed":False,
            "new_aperture_certificate":False}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
