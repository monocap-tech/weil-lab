#!/usr/bin/env python3
"""Actual 84-source enclosure at 93/100 with checked new kernel constants."""
import json
from functools import lru_cache
from math import factorial
import certify_native_prime3_source36 as source
from certify_native_legendre_small_window import F,I,bernoulli
from certify_native_exact_logarithm import log_rational
from certify_native_prime5_source_codec import compact_sources


def certificate():
    a=F(93,100);d=2*a;K=100
    B=bernoulli(2*K+2)
    coefficients=[abs(B[2*k]*(2*d)**(2*k)/factorial(2*k)) for k in range(1,K+1)]
    assert all(y<x for x,y in zip(coefficients,coefficients[1:]))
    assert all((B[2*k]>0)==(k%2==1) for k in range(1,K+1))
    # Alternating decreasing pairs give 0<BP(s)<=1+d*s+d^2*s^2/3 on [0,1].
    assert (1+d+d*d/3)/2 < F(9,4)
    assert d/2<1 and d<3
    previous=I.grid;old_log=source.log_rational;old_interval=source.log_interval
    I.grid=10**400
    source.log_rational=lru_cache(maxsize=None)(lambda x,terms=220:log_rational(x,terms))
    source.log_interval=lambda x:I(source.log_rational(x.lo).lo,source.log_rational(x.hi).hi)
    try:
        result=compact_sources(source.quantize(source.compute(degree=83,a=a),digits=40))
        result.update(source_log_series_terms=220,kernel_taylor_ceiling='9/4',
                      alternating_kernel_coefficient_controls_passed=True,
                      coefficient_rounding_budget_retained=True,
                      whole_domain_positivity=False,whole_domain_positivity_frontier='23/25',
                      f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
        return result
    finally:
        I.grid=previous;source.log_rational=old_log;source.log_interval=old_interval


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
