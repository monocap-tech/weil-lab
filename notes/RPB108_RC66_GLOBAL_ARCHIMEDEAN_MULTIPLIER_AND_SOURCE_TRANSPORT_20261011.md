# RPB108 RC66 — global archimedean multiplier and source transport

RC66 proves a global physical archimedean remainder norm bound of 643/100 = 6.43, replacing the inherited bound 8. Transporting it through the actual rank-22 projected source calculation gives

\[
\boxed{\Gamma_{22}\preceq\frac{4187}{256}M_{22}},
\qquad 4187/256=16.35546875.
\]

The new complete residual matrix upper bound is Loewner smaller than RC65's matrix upper bound, with exact rational PSD verification. The uniform factor improves by 482/4669, approximately 10.3234%. The projection and actual source columns are unchanged.

## Global multiplier proof

Use the established Fourier convention exp(-2 pi i xi x), canonical weight w(xi)=log(e+|xi|), and original archimedean multiplier

\[
a(\xi)=\operatorname{Re}\psi(1/4+i\pi\xi)-\log\pi.
\]

The bounded physical remainder is the compression of the multiplier m=a-w to the support interval. We prove -6.43 <= m <= 4 on the whole real line, hence its physical operator norm is at most 6.43. This bound is independent of the chosen finite trial space.

Let z=1/4+i y and f(t)=1/(t+z). The Euler digamma identity is

\[
\psi(z)=\lim_{L\to\infty}\left(\log L-\sum_{n=0}^{L-1}f(n)\right).
\]

For each unit cell, the fundamental theorem of calculus bounds its sum-minus-integral discrepancy by the integral of |f'| over that cell. Summing and passing to the limit gives

\[
|\psi(z)-\log z|
\le\int_0^\infty\frac{dt}{(t+1/4)^2+y^2}
\le 4.
\]

For y != 0, enlarging the integration interval after substituting s=t+1/4 also gives the sharper bound pi/(2|y|). Thus, with x=|xi|>0,

\[
|\psi(1/4+i\pi x)-\log(1/4+i\pi x)|
\le\min(4,1/(2x)).
\]

The branch of log is the principal branch, valid throughout the right half-plane. Its real part is log|z|. Since |z| <= pi(e+x), the global upper bound m<=4 follows.

For the lower bound, Euler's series gives the nonnegative difference

\[
\operatorname{Re}\psi(1/4+i y)-\psi(1/4)
=\sum_{n\ge0}\frac{y^2}{(n+1/4)((n+1/4)^2+y^2)}\ge0.
\]

The established quarter identity is psi(1/4)=-gamma-pi/2-3 log 2. RC56's certified constant c_R=-gamma-log(2 pi R), with R=11/5, therefore encloses

\[
a(0)=c_R+\log(2R)-\pi/2-3\log2.
\]

Split at x_0=3/20. On 0<=x<=x_0, monotonicity gives

\[
m(x)\ge a(0)-\log(e+x_0)>-6.425897>-6.43.
\]

On x>=x_0, the Euler discrepancy estimate and |z|>=pi x give

\[
m(x)\ge-\log(1+e/x)-1/(2x)
\ge-\log(1+e/x_0)-1/(2x_0)>-6.284167>-6.43.
\]

Both lower expressions are checked with directed enclosures. Thus the entire physical multiplier remainder has modulus <=6.43. Extending a supported vector by zero, applying this Fourier multiplier, and restricting back to the interval preserves the same L2 norm bound. This is a bound on the bounded remainder; the full logarithmic archimedean operator remains unbounded.

## Actual source transport

Keep RC62's certified full paired-prime and signed-pole operator bounds. Replace only the archimedean contribution in each complete parity norm:

\[
k_{p,\mathrm{new}}=k_{p,\mathrm{old}}-8+643/100.
\]

The actual archimedean source approximation error remains paid with RC62's unchanged delta. RC60's full correlated physical Riesz error Gram remains unchanged. The source transfer bound is recomputed using the fixed rational Young parameter 1/65536, followed by the RC65 source-versus-representative parameter 1/16 and nominal-versus-error parameters 2 (even) and 3/2 (odd). All rounding carries diagonal row-sum Loewner allowances.

| Parity | Actual canonical projected residual upper factor |
|---|---:|
| Even | 4187/256 = 16.35546875 |
| Odd | 3193/256 = 12.47265625 |

Exact PSD checks prove the new source transfer matrix and final residual matrix are each Loewner smaller than their RC65 counterparts. Direct comparisons against RC59's actual canonical Gram lower matrix certify the displayed parity factors.

## Independent replay and boundary

Generation uses directed Decimal exp/log constants. Replay independently verifies the global-cap inequalities with exact rational Taylor bounds for e and positive atanh series for logarithms, with explicit geometric tail allowances. It also rechecks the final residual comparisons and matrix improvement after exact inverse Chebyshev-to-Legendre congruences. No floating eigenvalue is accepted as evidence.

The Euler discrepancy lemma is proved analytically above. The executable checks its constant consequences and finite matrix transport; it does not formalize complex analysis in Lean. RC56's quarter constant enclosure and the established original multiplier normalization are dependencies.

The scalar Schur budget ceiling remains approximately 1.70845e-11. The new bound does not certify that budget and does not prove actual residual failure. No positive uniform 22-feature Weil floor, rank-22 complement floor, negative Weil direction, full 1250 projection, new aperture positivity, RH, or F4 result is asserted.

The next substantive target is sharper correlated transport of the Riesz errors or improved Riesz trials, rather than expecting further scalar norm reductions to close the remaining scale gap.

## Added artifacts

- `scripts/validate_rpb108_rc66_arch_multiplier_transport.py`
- `certificates/rpb108_rc66_arch_multiplier_transport.json`
- This report.

Historical milestone artifacts remain unchanged.
