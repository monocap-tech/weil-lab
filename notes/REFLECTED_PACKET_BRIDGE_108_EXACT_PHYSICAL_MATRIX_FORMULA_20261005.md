# RPB108: exact physical formula for actual finite matrix entries

Base: research cf54bf9ace3711a347e930f815b8166833cfb18f.

## Theorem and computational outcome

For the actual supported Legendre trial vectors, every native mixed entry is an exact finite-interval integral of explicit correlation polynomials, plus native prime and pole terms. There is no omitted Fourier tail.

The apparent singularity at the integration origin is removable and can be cancelled algebraically. Correlation polynomials have exact rational coefficients before the basis normalization.

A reproducible physical-space pilot evaluates the formula and agrees with the earlier Fourier pilot after accounting for its tail. The values remain exploratory: no validated integration, special-function, rounding or spectral enclosure is supplied. No negative witness, exact null, all-domain positive certificate or endpoint exclusion is obtained.

## Terminology before use

**Symmetrized correlation:** the average of the two shifted physical mixed pairings in (1).

**Tail-free entry formula:** the exact native finite-interval formula (3), whose exterior integration tail is evaluated analytically.

**Removable-origin evaluation:** an algebraic arrangement that avoids subtracting two nearly equal floating constants near t=0; it is not itself validated interval arithmetic.

## Exact supported correlations

Use the lawful physical L2-orthonormal Legendre vectors v_i from the previous pilot. Define
\[
C_{ij}(s)=\tfrac12\left[
\int v_i(x)v_j(x-s)\,dx+
\int v_j(x)v_i(x-s)\,dx\right].
\tag{1}
\]
Then Cij(0)=delta_ij, and Cij(s)=0 for s>=2a.

For 0<=s<=2a, put u=s/a. An unsymmetrized term is
\[
\frac{\sqrt{(2i+1)(2j+1)}}2
\int_{u-1}^{1}P_i(r)P_j(r-u)\,dr.
\tag{2}
\]
The integral is a polynomial in u with rational coefficients. Symmetrization retains this property. Its degree is at most i+j+1.

Opposite parity gives zero symmetrized correlation, consistently with the full native parity decomposition. All vectors remain the original supported physical vectors with their actual positive and negative analyses.

## Euler pairing and exact finite archimedean integral

The actual archimedean symbol is
Re psi(1/4+i pi xi)-log pi. Use the existing Euler series
\[
\psi(z)=-\gamma+\sum_{n\ge0}
\left(\frac1{n+1}-\frac1{n+z}\right).
\]
For each reciprocal term, Laplace integration and Fourier pairing give
\[
\int\Re\frac1{n+1/4+i\pi\xi}
\overline{\widehat v_i}\widehat v_j\,d\xi
=\int_0^\infty e^{-(n+1/4)t}C_{ij}(t/2)\,dt.
\]
The constant term 1/(n+1) similarly has integral
integral_0^infinity exp(-(n+1)t)delta_ij dt.

Finite Euler sums may be paired directly by Fubini. Their limit is lawful on these logarithmic-domain vectors by the same bounded-logarithmic domination already proved for the actual symbol. Alternatively, the resulting correlation numerator vanishes to first order at t=0, so its summed geometric kernel is directly integrable there; outside the correlation support the tail is exponential.

Summing the geometric series gives the full archimedean entry
\[
(-\gamma-\log\pi)\delta_{ij}
+\int_0^\infty
\frac{e^{-t}\delta_{ij}-e^{-t/4}C_{ij}(t/2)}
{1-e^{-t}}\,dt.
\]
Since the correlation vanishes for t>=4a and
\[
\int_{4a}^\infty\frac{e^{-t}}{1-e^{-t}}\,dt
=-\log(1-e^{-4a}),
\]
the exact compact formula is
\[
\operatorname{Arch}_{ij}=
[-\gamma-\log\pi-\log(1-e^{-4a})]\delta_{ij}
+\int_0^{4a}
\frac{e^{-t}\delta_{ij}-e^{-t/4}C_{ij}(t/2)}
{1-e^{-t}}\,dt.
\tag{3}
\]

## Native prime and pole terms

The exact complete native matrix is
\[
Q_{ij}=\operatorname{Arch}_{ij}
-2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
C_{ij}(\log n)
+M_-(v_i)M_+(v_j)+M_+(v_i)M_-(v_j).
\tag{4}
\]
The threshold prime-power set and cross-pole normalization are unchanged. Equality thresholds cause zero correlation at the boundary, consistent with support custody.

The supported pole moments are the exact formulas already recorded using modified spherical Bessel functions. Their numerical floating evaluations still require enclosures for any sign certificate.

Equations (2)-(4) are actual entry identities, not a substitute selected-only quadratic.

## Stable arrangement at the origin

Write, with u=t/(2a),
\[
C_{ij}(t/2)=\delta_{ij}+uR_{ij}(u),
\]
where R is the known normalized polynomial. The integrand in (3) becomes
\[
e^{-t/4}
\frac{\operatorname{expm1}(-3t/4)\delta_{ij}
-uR_{ij}(u)}
{-\operatorname{expm1}(-t)}.
\tag{5}
\]
Both numerator and denominator vanish linearly, with finite limiting value. This avoids directly subtracting Cij from delta in floating arithmetic.

The script constructs all unnormalized polynomial coefficients with rational Fraction arithmetic and checks Cij(0) exactly, as well as exact opposite-parity cancellation. It then converts polynomials to Bernstein coordinates on [0,2] and evaluates them by de Casteljau recursion. This reduces numerical cancellation from power-basis evaluation.

Rational coefficient construction is exact. Conversion to float, exponential/logarithmic evaluation, quadrature and matrix eigenvalues are not certified; that distinction remains explicit in the output.

## Reproducible pilot

Script: scripts/explore_native_legendre_physical.py.
Output: notes/data/RPB108_PHYSICAL_MATRIX_PILOT_20261005.json.

The physical integration uses 128 Gauss-Legendre nodes, with 64 nodes as a repeat diagnostic. The physical basis has eight vectors, i=0,...,7.

| a | Smallest physical pilot value | 64/128-node matrix difference | Norm of physical minus previous truncated matrix |
|---|---:|---:|---:|
| 1/4 | 0.0334278223 | 1.07e-13 | 0.0133722 |
| 1/2 | 5.01935e-6 | 1.06e-13 | 0.0124027 |
| 3/4 | 1.08271e-6 | 1.05e-13 | 0.0118346 |
| 1 | 8.44340e-8 | 1.04e-13 | 0.0114332 |

The physical-minus-truncated matrix has a numerically tiny negative lower value of order 1e-14. This is not a proved violation of the positive-tail condition; neither computation has a validated error enclosure.

These are finite physical-basis Rayleigh values. Their positivity does not exclude negative directions outside the chosen trial space, and their smallness does not assert full native approximate weak-nullity.

## What was closed and what remains

The finite native entry formula is now exact and free of a Fourier cutoff. Validating it no longer requires controlling a long oscillatory tail. The remaining numerical sign task is finite-interval integration and certified elementary/special-function and spectral arithmetic.

Whole-domain positivity would still require the separate infinite-dimensional complement certificate. The exact finite trial formula does not provide that condition automatically. It also supplies no actual endpoint-null Gaussian upper bound.

Analytic formula closure is therefore narrower than carrier/factorization transport closure. FULL TRANSPORT CLOSED remains open.

## Validation and cursor

Executed the physical pilot under SciPy 1.17.0, with exact rational correlation-normalization and parity checks. Numerical output is exploratory. Analytic identities (2)-(5) are proved above. Lean source/workflow remains unchanged, with no new Lean/CI result. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At cf54bf9, actual supported Legendre matrix entries have a tail-free exact physical formula. Their symmetrized autocorrelations Cij(s) are explicit rational-coefficient polynomials times normalization on 0<=s<=2a. Euler digamma pairing gives arch_ij=(-gamma-log pi-log(1-exp(-4a)))delta_ij + integral_0^(4a) [exp(-t)delta_ij-exp(-t/4)Cij(t/2)]/(1-exp(-t))dt. Native prime terms are -2 sum Lambda(n)/sqrt(n) Cij(log n), and the unchanged pole moments are added exactly. The apparent singularity at t=0 is removable because Cij(0)=delta_ij. Rational polynomial coefficients are computed exactly, converted to Bernstein evaluation, and the cancellation is algebraically removed before floating integration. This eliminates the Fourier-tail error from finite matrix entry evaluation. A reproducible 64/128-node physical pilot gives positive smallest values about .0334278, 5.01935e-6, 1.08271e-6 and 8.44340e-8 at a=1/4,1/2,3/4,1, but arithmetic/integration/special-function/spectral errors remain unvalidated. The physical-minus-truncated matrix accounts for the prior omitted tail numerically, without a sign certificate. No negative witness, exact null, all-domain positivity or endpoint exclusion was obtained. This completes an exact entry formula, not actual numerical sign validation or FULL TRANSPORT CLOSED. Same-vector actual source custody and no assumed physical operator domain; Lean/CI unchanged.
