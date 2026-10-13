"""Actual twenty-vector raw matrix; corrected Schur sign remains separate."""
import json
from certify_native_legendre_small_window import F,I,certificate as native_matrix,positive_pivots,sqrt_rational


def certificate():
    previous=I.grid
    I.grid=10**120
    try:
        raw=native_matrix(F(1,2),return_matrix=True,degree=19)
        matrix=[[sqrt_rational(F((2*i+1)*(2*j+1)))*raw[i][j] for j in range(20)] for i in range(20)]
        pivots=positive_pivots(matrix)
        tau=F(1,2000000)
        shifted=[row[:] for row in matrix]
        for i in range(20):
            shifted[i][i]-=tau
        shifted_pivots=positive_pivots(shifted)
        width=max(x.hi-x.lo for row in matrix for x in row)
        assert width<F(1,10**25)
        broken=[row[:] for row in matrix];broken[0][0]=I(-1)
        try:
            positive_pivots(broken)
        except ArithmeticError:
            pass
        else:
            raise AssertionError('Negative control accepted')
        return dict(status='certified actual raw twenty-vector matrix and finite positivity',
                    aperture='1/2',physical_degrees=list(range(20)),
                    physical_basis='sqrt(2n+1) P_n(2x) on [-1/2,1/2]',
                    matrix_intervals=[[[str(x.lo),str(x.hi)] for x in row] for row in matrix],
                    pivot_lower_bounds=[str(x.lo) for x in pivots],
                    pivot_lower_display=[float(x.lo) for x in pivots],
                    raw_physical_coercivity_lower_bound=str(tau),
                    shifted_pivot_lower_bounds=[str(x.lo) for x in shifted_pivots],
                    maximum_entry_width=str(width),maximum_entry_width_display=float(width),
                    exact_reflection_parity=True,prime_terms=[2],
                    exponential_order=80,bernoulli_pairs=60,gamma_order=12,
                    interval_grid_digits=120,negative_control_rejected=True,
                    corrected_twenty_schur_sign_certified=False,
                    remaining_twelve_schur_sign_certified=False,whole_domain_positivity=False)
    finally:
        I.grid=previous


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
