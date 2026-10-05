"""Rational native twenty-vector restriction at aperture 11/20 including primes 2 and 3."""
import json
from certify_native_legendre_small_window import F, I, certificate as native_matrix, positive_pivots, sqrt_rational


def certificate(a=F(11,20)):
    if a not in (F(1,2), F(51,100), F(27,50), F(11,20)):
        raise ValueError('Unsupported twenty-vector aperture')
    previous = I.grid
    I.grid = 10**120
    try:
        raw = native_matrix(a, return_matrix=True, degree=19)
        matrix = [[sqrt_rational(F((2*i+1)*(2*j+1)))*raw[i][j]/(2*a)
                   for j in range(20)] for i in range(20)]
        pivots = positive_pivots(matrix)
        tau = F(1,2000000)
        while True:
            shifted = [row[:] for row in matrix]
            for i in range(20):
                shifted[i][i] -= tau
            try:
                shifted_pivots = positive_pivots(shifted)
                break
            except ArithmeticError:
                if tau < F(1,10**20):
                    raise
                tau /= 2
        width = max(x.hi-x.lo for row in matrix for x in row)
        assert width < F(1,10**25)
        assert all(matrix[i][j].lo == matrix[i][j].hi == 0
                   for i in range(20) for j in range(20) if (i+j)%2)
        broken = [row[:] for row in matrix]
        broken[0][0] = I(-1)
        try:
            positive_pivots(broken)
        except ArithmeticError:
            pass
        else:
            raise AssertionError('Negative diagonal control accepted')
        return dict(
            status='certified native finite restriction only', aperture=str(a),
            physical_degrees=list(range(20)),
            physical_basis='sqrt((2n+1)/(2a)) P_n(x/a) on [-a,a]',
            matrix_intervals=[[[str(x.lo),str(x.hi)] for x in row] for row in matrix],
            pivot_lower_bounds=[str(x.lo) for x in pivots],
            raw_physical_coercivity_lower_bound=str(tau),
            shifted_pivot_lower_bounds=[str(x.lo) for x in shifted_pivots],
            maximum_entry_width=str(width), prime_terms=([2,3] if a==F(11,20) else [2]),
            exact_reflection_parity=True, negative_control_rejected=True,
            exponential_order=80, bernoulli_pairs=60, gamma_order=12,
            interval_grid_digits=120, residual_gram_certified=False,
            corrected_schur_sign_certified=False, whole_domain_positivity=False,
            f4_entry_closed=False, full_transport_closed=False, lean_formalized=False)
    finally:
        I.grid = previous


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
