#!/usr/bin/env python3
"""PI029: exact rational source-geometry and sign-margin regression only.

Mathematical source theorem (memo; NOT proved by this finite script):
For every integer N>=2, let d=log(10/9), Delta=d/(N+1),
ell=d/(100*N^2), and rho=sum_{j=1}^N b(x-j*Delta)
for the explicit nonnegative flat Cc-infinity bump b on (0,ell).
For every m>=1, phi_m=L_m rho with L_m=D prod_{j<m}(D^2-(2j+1/2)^2).
Its normalized autocorrelation C/J has peaks (N-k)/N at t=k*Delta.
On a=log3-t, 0<=t<=d, P=(log3/sqrt3)C and 0<B/J<1/(900*N).
Thus Theta=B-P changes sign in at least 2N-1 disjoint windows,
all with real n=3 prime contribution at the root.

This program checks exact support-channel and rational inequality consequences
for 2<=N<=128, without evaluating smooth integrals, zeta zeros, Lean, or CI.
"""
from fractions import Fraction as F


def source_channels(N: int, t: F, Delta: F, ell: F) -> list[tuple[int, F]]:
    """Possible nonzero shifted correlations; terms on endpoints are zero."""
    return [(k, F(N - abs(k), N))
            for k in range(-(N - 1), N)
            if abs(t - k * Delta) < ell]


def regression(N: int) -> int:
    assert N >= 2
    Delta = F(1, N + 1)    # all lengths in units of d
    ell = F(1, 100 * N * N)
    centers = [j * Delta for j in range(1, N + 1)]

    # rho_N fits in fixed (0,d), with disjoint, very narrow positive bumps.
    assert 0 < centers[0] < centers[-1] + ell < 1
    assert Delta > 2 * ell
    assert N * ell == F(1, 100 * N)

    # On a=log3-t with 0<=t<=d, only the source n=3 sample survives.
    assert F(3) / F(10, 9)**2 == F(243, 100) > 2
    assert F(3) * F(10, 9) == F(10, 3) < 4
    assert F(8, 9) < 1         # K(log2)^2<1
    # Analytic real-log inputs: d<1/9; log3/sqrt3>1/3.
    gamma_ceiling = N * ell / 9
    assert gamma_ceiling == F(1, 900 * N)

    assert source_channels(N, F(0), Delta, ell) == [(0, F(1))]
    assert source_channels(N, ell, Delta, ell) == []

    # For every satellite center: (N-k)/N normalized correlation peak;
    # its left/right boundaries sample ZERO original prime correlation.
    brackets_t = [(F(0), ell)]
    for k in range(1, N):
        t0 = k * Delta
        assert source_channels(N, t0, Delta, ell) == [
            (k, F(N - k, N))]
        assert source_channels(N, t0 - ell, Delta, ell) == []
        assert source_channels(N, t0 + ell, Delta, ell) == []
        brackets_t.extend([(t0 - ell, t0), (t0, t0 + ell)])

    # All positive t-brackets are disjoint and inside (0,d), aside from
    # the central bracket starting at t=0 (whose root is still interior).
    assert len(brackets_t) == 2 * N - 1
    assert all(hi - lo == ell for lo, hi in brackets_t)
    assert all(F(0) <= lo < hi < F(1) for lo, hi in brackets_t)
    assert all(brackets_t[j][1] <= brackets_t[j + 1][0]
               for j in range(len(brackets_t) - 1))

    # At each peak, Theta/J < 1/(900N) - (N-k)/(3N).
    # Uniform strict bound Theta/J < -299/(900N); at zero-sample
    # endpoints Theta=B>0 by the independent mathematical Gamma theorem.
    uniform_negative_margin = F(299, 900 * N)
    for k in range(N):
        theta_ceiling = gamma_ceiling - F(N - k, 3 * N)
        assert theta_ceiling <= -uniform_negative_margin

    # Mean-value theorem derivative witness magnitude > margin/ell:
    # this does NOT assert Theta'(root)!=0.
    slope_floor = uniform_negative_margin / ell
    assert slope_floor == F(299 * N, 9)
    return len(brackets_t)


def main() -> None:
    counts = [(N, regression(N)) for N in range(2, 129)]
    assert counts[0] == (2, 3)
    assert counts[1] == (3, 5)
    assert counts[-1] == (128, 255)
    assert all(count == 2*N-1 for N, count in counts)
    # This is finite exact-arithmetic regression, not a proof that the
    # infinite class N>=2 is exhausted by the loop.
    print("PI029 N=2..128 exact nonnegative support geometry: PASS")
    print("PI029 unique original n=3 sample and Gamma envelope: PASS")
    print("PI029 exact centers, endpoints, disjoint root brackets: PASS")
    print("PI029 uniform strict prime-dominance margin: PASS")
    print("PI029 mean-value slope witness rational algebra: PASS")
    print("Example lower bound N=128: at least 255 crossings")
    print("The all-N/all-m result uses the analytic proof in the memo.")
    print("No smooth-integral calculation, root transversality proof, actual spectral trace, Lean, or Actions.")


if __name__ == "__main__":
    main()
