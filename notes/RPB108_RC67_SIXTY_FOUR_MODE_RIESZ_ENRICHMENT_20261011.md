# RPB108 RC67 — 64-mode Riesz enrichment

RC67 constructs rational 64-mode trials for all 22 actual native Riesz representatives. It certifies two full-matrix improvements:

1. The enriched actual canonical native Gram lower bound is Loewner larger than RC59's lower bound.
2. The enriched canonical Riesz-error Gram upper bound is Loewner smaller than RC60's error bound. Its physical transport upper bound improves by the same positive factor 252/257.

All 22 diagonal squared-error upper bounds improve. The reductions range from approximately 14.888% to 21.560%; equivalently the old-to-new bound factors range from 1.17493 to 1.27485. These are refinements of upper bounds, not assertions about the exact size or reduction of the unknown actual errors.

| Native feature | RC60 canonical squared-error upper | Enriched squared-error upper |
|---|---:|---:|
| 0 | 0.0001598042294870 | 0.0001355610716205 |
| 1 | 0.0001329693039086 | 0.0001131723459758 |
| 20 | 0.0001240195089625 | 0.0000972815119012 |
| 21 | 0.0001212999377059 | 0.0000952682391004 |

The actual 22-feature head and orthogonal projection are unchanged. The finite trial dimension grows from 32 to 64.

## Recentered actual metric

The 64 by 64 metric is rebuilt with RC56's sharply certified constant midpoint c_R, rather than the historical coarse midpoint. Its degree-192 kernel approximation and entry-rounding errors are paid. With D_64 the physical Legendre mass matrix, the recorded nominal center G satisfies

\[
G-\delta D_{64}\preceq G_{\mathrm{actual}}\preceq G+\delta D_{64},
\qquad\delta=1849/10^{30}=1.849\times10^{-27}.
\]

The error includes the constant radius, the uniform kernel tail, and the complete finite entry-rounding transport. The midpoint and constant-radius normalization remain exactly those of RC56. The historical 32-mode trial and metric files are not altered.

## Faster metric integration and independent replay

Let A_n(y)=P_n(2y-1), and define its polynomial convolution

\[
C_{ij}(t)=\int_0^t A_i(y)A_j(t-y)\,dy.
\]

For same-parity indices, the complete paired physical displacement overlap is

\[
\mathcal O_{ij}(r)=2R(-1)^i C_{ij}(1-r/R).
\]

For opposite parity it is zero. Convolution monomials integrate by exact factorial beta coefficients. Generation expands the displacement polynomial and integrates with precomputed ordinary and logarithmic kernel moments. It also checks the formula against the earlier overlap builder for every relevant column below degree eight.

Replay instead retains the convolution polynomial and integrates it using beta and logarithmic beta moments. These two calculations enclose the same entries. Precomputing moment families avoids repeating the full kernel integration for each pair. Endpoint logarithms are retained exactly through polynomial log moments; no sampling or fitted matrix is used.

## Rational enriched solve and Gram lower bound

Let X contain the exact physical pairings of the 64 Legendre trials with the first 22 native Chebyshev targets. The enriched coefficient matrix V is the exact nominal solve G^-1 X rounded to denominator 10^40. Opposite-parity coefficients remain zero.

The actual finite Ritz principle gives the actual native Gram lower bound

\[
M_{22}\succeq X^*(G+\delta D_{64})^{-1}X.
\]

After outward Loewner rounding, exact PSD verifies that the enriched lower matrix dominates RC59's lower matrix. The unknown actual Riesz representatives are not identified with the enriched finite trials.

## Correlated actual error refinement

Pad the historical 32-mode trial matrix V_old with zeros. Set W=V-V_old and E_old=R_actual-V_old. Then E_new=E_old-W. The canonical pairing with the actual representative is exact:

\[
\langle R_{\mathrm{actual}},W\rangle_{\mathrm{can}}=X^*W.
\]

Consequently the new error Gram has the identity

\[
E_{\mathrm{new}}^*E_{\mathrm{new}}
=E_{\mathrm{old}}^*E_{\mathrm{old}}
-X^*W-W^*X
+V_{\mathrm{old}}^*G_{\mathrm{actual}}W
+W^*G_{\mathrm{actual}}V_{\mathrm{old}}
+W^*G_{\mathrm{actual}}W.
\]

RC60's whole correlated E_old Gram bound is substituted in this identity. Replacing the actual trial metric with its recentered nominal center is paid by

\[
\delta\,(T_{\mathrm{old}}+2W^*D_{64}W).
\]

This follows from the mass-relative metric error and the exact quadratic inequality 2|<V_old,Delta W>| <= delta(||V_old||_phys^2+||W||_phys^2). A final diagonal row-sum rounding allowance yields the emitted canonical error upper matrix. Exact PSD checks verify it is positive and that the old-minus-new upper matrix is positive semidefinite.

Replay independently expands the difference of the old and enriched trial metric quadratics and physical target pairings. Its exact result equals the W-based formula before outward rounding. The executable also rechecks the complete Ritz lower comparison and all error PSD statements.

## Evidence boundary and next step

This pass certifies the enriched metric, trials, native Gram lower bound, and full correlated Riesz-error upper bounds. It does not evaluate the complete original source covariance on the new trials. RC66's actual projected-source upper bound 4187/256 remains the current certified source factor.

The old nominal source covariance cannot simply be combined with the new trial-error matrices: its source columns were evaluated on the historical trials. The next attachment must recompute or rigorously transport the original source covariance to the enriched trials and then rebuild the projected residual calculation.

No positive uniform 22-feature Weil floor, negative Weil direction, rank-22 complement floor, full 1250 projection, aperture extension, RH, or F4 conclusion is established. The low-eight positive floor and all historical actual source bounds remain valid.

## Added artifacts

- `scripts/validate_rpb108_rc67_sixty_four_riesz_enrichment.py`
- `certificates/rpb108_rc67_sixty_four_riesz_enrichment.json`
- This report.

Historical milestone artifacts remain unchanged.
