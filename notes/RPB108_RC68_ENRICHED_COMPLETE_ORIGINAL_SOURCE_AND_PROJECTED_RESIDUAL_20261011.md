# RPB108 RC68 — enriched complete original source and projected residual

RC68 attaches the complete signed original source covariance to RC67's rational 64-mode trials for the first 22 native Riesz representatives. It rebuilds the canonical variational projected-source residual with those trials and their certified enriched errors.

The certified bound is

\[
\boxed{\Gamma_{22}\preceq\frac{471}{32}M_{22}},
\qquad 471/32=14.71875.
\]

This improves RC66's factor 4187/256 = 16.35546875 by exactly 419/4187, approximately 10.0072%. The even factor is 471/32; the odd factor is 5873/512 = 11.470703125. The actual nominal-source approximation operator error is bounded by 2.077637e-24 after recentering and paying the regular-kernel omission.

The actual source columns and actual rank-22 orthogonal projection remain the same. This pass changes their finite trial approximations and certified upper bounds.

## Enriched source construction

The nominal physical source is F_plus,nom = q + K_nom V_64, where q contains the native physical Chebyshev targets, V_64 is the RC67 trial matrix, and K_nom is the bounded archimedean remainder plus the full paired-prime and signed-pole operators.

The archimedean source uses RC56's precise constant midpoint. Its logarithmic kernel coefficients and polynomial regular-kernel convolution are rebuilt for all 64 trial modes. The endpoint singularity cancels in the bounded archimedean remainder before source integration. The actual physical native target q is retained explicitly; no auxiliary Legendre target is substituted for it.

The nominal regular archimedean kernel in this implementation contains degrees 0 through 191. The absolute contribution of the omitted degree-192 coefficient is paid separately, together with RC46's remainder after degree 192. The source approximation norm allowance also includes the corrected constant radius and the metric-series operator tail. This makes the source covariance's approximation convention explicit.

## Complete covariance and pairings

All 253 upper-triangle entries of the complete signed physical source Gram are enclosed. The 121 mixed-parity entries are exactly zero; the 132 same-parity entries are evaluated. The assembly retains the covariance of q plus the bounded archimedean source, the prime covariance, their signed cross term, the pole covariance, and every pole cross term.

The full paired-prime operator uses the inherited 14 oriented translations across 15 physical support segments. Pole sources retain their positive even and negative odd signs, and the distinct cosh and sinh physical norms.

The physical pairing matrix H = <V_64,F_plus,nom> is evaluated on the enriched trials. Its bounded-remainder part is symmetric. Its target part has the exact pairing J^*, so the ordered opposite triangle is recovered by adding the exact difference J_ij-J_ji. The resulting generally nonsymmetric full source pairing matrix is not replaced by a symmetric head matrix.

## Actual canonical projected residual

The actual source is Sigma_plus = i*(q+K_actual iR), where R consists of the actual canonical Riesz representatives. Sigma_plus=R+sigma, and the rank-22 projection removes R exactly.

For a fixed rational coefficient matrix L, the nominal variational residual is i* F_plus,nom - V_64 L. Its Gram upper bound uses the complete physical covariance U, the physical pairing H, and the actual trial canonical metric upper bound:

\[
Y\preceq\rho U-H^*L-L^*H+L^*G_{V,\mathrm{up}}L+\mathcal R,
\qquad\rho=252/257.
\]

The diagonal row-sum allowance R pays every pairing interval and finite center rounding. L is obtained from an exact rational solve and rounded to denominator 10^24; it is not identified with the unknown actual orthogonal projection coefficients.

The actual source transfer uses RC67's enriched physical Riesz error Gram and RC66's complete parity operator norms. The representative-coefficient term uses RC67's enriched canonical error Gram. The corrected nominal source approximation error is paid separately. Fixed rational Young parameters 1/65536, 1/16, and 2 (even) or 3/2 (odd) retain all three error splits.

The final parity matrices are compared directly against RC67's enriched actual native Gram lower bound by exact rational PSD checks. The variational distance to the actual Riesz range bounds the actual orthogonally projected source residual.

## Independent replay

Generation integrates all nine logarithmic products for the archimedean covariance. Replay uses the five-product reflection reduction. Prime covariance and trial-head generation use physical polynomial primitives; replay uses affine unit-interval integrations. Mixed prime/archimedean terms replay with reflected logarithmic moments. Exponential and pole moments use separate closed-primitive and Taylor integrations with explicit tails.

The projected residual generation expands its variational quadratic; replay independently completes the square around the trial-metric minimizer. The final canonical comparisons are also replayed after exact inverse Chebyshev-to-Legendre congruences. Certificate hashes tie the calculation to the exact enriched trials and historical operator bounds. Floating arithmetic supplies no proof evidence.

## Evidence boundary

The required scalar Schur source budget remains below approximately 1.70845e-11. The new certified upper bound does not certify that budget; a large upper bound does not prove actual residual failure. This is a comparison of uniform upper factors, not a claim that the new residual matrix dominates or is dominated by every historical matrix bound.

No positive uniform 22-feature Weil floor, negative Weil direction, rank-22 complement floor, full 1250 projection, aperture extension, RH, or F4 conclusion is established. The low-eight positive floor and RC63's obstruction to extending its old floor remain valid.

## Added artifacts

- `scripts/validate_rpb108_rc68_enriched_original_source_covariance.py`
- `certificates/rpb108_rc68_enriched_original_source_covariance.json`
- This report.

Historical milestone artifacts remain unchanged.
