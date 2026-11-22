#!/usr/bin/env python3
"""UOI049: exact rational arithmetic isolation for log(8^M) prime contact.
No Gamma norm, infinite-tail boundedness, Lean kernel, or source bridge is checked.
"""
from fractions import Fraction
import json
from pathlib import Path

delta = Fraction(1, 1000)
checks = []
for M in (1, 2, 3, 5, 10, 15, 30):
    N = 8 ** M
    ell = delta / N
    # For N >= 2, the nearest log of another integer lies at distance at least
    # log(1 + 1/N) >= 1/(N+1) from log N.
    # Difference of two packets each of diameter ell is contained in
    # (log N - ell, log N + ell). The inequality below is exact.
    assert ell < Fraction(1, N + 1)
    assert delta * (N + 1) < N
    # Gamma leakage upper coefficient from UOI048, exact rational.
    gamma_bound = Fraction(1, (8 ** M) * 32970)
    checks.append({
        'M': M,
        'N_prime_power': N,
        'N_factorization': f'2^(3*{M})',
        'mangoldt_at_N': 'log(2)',
        'prime_translation_weight': f'log(2)/sqrt({N})',
        'packet_diameter': str(ell),
        'nearest_integer_log_gap_lower': str(Fraction(1, N + 1)),
        'gap_comparison': 'PASS',
        'UOI048_Gamma_kappa_upper': str(gamma_bound),
    })

receipt = {
    'schema': 'uoi049-prime-power-contact-arithmetic-v1',
    'scope': 'exact rational log-gap isolation; the Gamma-energy lower bound is a separate analytic obligation',
    'geometry_assumption': 'centres x_j = a + j*log(8), collar widths at least delta*8^(-j), delta=1/1000',
    'contact': 'N=8^M is a genuine prime power, Lambda(N)=log(2)',
    'three_moments': 'physical differential operator D_x*(D_x^2-1/4) kills integrals against 1 and exp(+-x/2), by parts',
    'verified_Lean_kernel': False,
    'verified_source_to_native': False,
    'verified_infinite_prime_operator_compact': False,
    'checks': checks,
}
path=Path('/mnt/data/UOI049_prime_resonance_receipt.json')
path.write_text(json.dumps(receipt,indent=2)+'\n')
print('PASS:',len(checks),'exact rational log-gap contact checks; no Lean or analytical norm proof')
