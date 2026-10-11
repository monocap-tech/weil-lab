# RC81: direct residuals of the enriched Riesz trials

Date: 2026-10-11. RPB108 route consolidation. Status: PASS.

RC81 directly certifies the complete mixed physical operator-residual covariance for RC67's existing 64-dimensional, 22-column Riesz trials. It recenters the residual functions at RC56's corrected constant and replaces the earlier trial-difference transport with a direct residual certificate. The canonical and physical Riesz-error upper matrices improve in Loewner order over RC67.

The trial vectors themselves are unchanged. This is a stronger error enclosure, not a change in their actual errors.

| Quantity | Result |
| --- | --- |
| Physical trial dimension | 64 |
| Native target count | 22 |
| Same-parity upper-triangle entries evaluated | 132 |
| Opposite-parity upper-triangle entries, exactly zero | 121 |
| All diagonal canonical squared-error upper improvement factors | approximately 3.97 to 13.12 |
| Feature 20 canonical squared-error upper | approximately 7.47477e-6, previously 9.72816e-5 |
| Feature 21 canonical squared-error upper | approximately 7.26212e-6, previously 9.52683e-5 |
| Whole-matrix improvement over RC67 | exact rational PSD comparison passed |

The exact rationals and all diagonal comparisons appear in the certificate. Decimals summarize upper-enclosure values; no floating-point computation contributes to acceptance.

## Direct operator residuals

Let C be the exact native Chebyshev-to-Legendre conversion matrix from RC59. Let V_native be RC67's rounded 64-by-22 physical trial coefficient matrix. Compute V_leg=V_native*C^(-1) exactly and verify V_leg*C=V_native. This keeps all 64 trial modes and every native column unchanged.

Use the same canonical physical operator representation as RC60, with kernel order 192 and aperture B=11/10, R=2B=11/5. Replace RC60's old nominal constant center by RC56's certified midpoint c_mid. For each Legendre target q_j, reconstruct

f_j=q_j-L_nom V_leg,j

as A_j(y)+B_j(y)log(y)+C_j(y)log(1-y), with y=(x/B+1)/2. The polynomial and logarithmic coefficient arrays now retain the 64-mode trial rather than RC60's 32-mode trial. Legendre degree j fixes the reflection parity of each residual.

The degree-192 regular/log kernel expansion and its remainder estimate are unchanged in type. The generic bound is

epsilon_kernel=(4/3)*(192+64)*42^193/193!.

The constant-center shift that RC60 previously paid separately is absent because the nominal residual is now centered at c_mid. Its uncertainty remains paid.

## Mixed covariance and exact native conversion

All 132 same-parity upper-triangle residual inner products are enclosed with directed 220-digit interval arithmetic and the six established physical moment families for 1, log(y), log(1-y), log(y)^2, log(1-y)^2, and log(y)log(1-y). Parity forces the other 121 entries to zero.

Generation evaluates the full nine-term product of two polynomial/log residuals. Each saved interval is outward-rounded to denominator 10^20. Diagonal row sums pay every entry's half-width and yield a nominal Legendre residual Gram upper Q_leg,up. Exact congruence gives

Q_native,up=C* Q_leg,up C.

Both matrices are checked PSD. This controls every complex native coefficient vector, including all feature correlations, rather than only separate column errors.

## Actual operator correction and Riesz transport

Let c_rad be RC56's certified constant radius and T the exact physical trial Gram. The actual canonical operator correction is bounded by

delta=2*c_rad+epsilon_kernel.

The factor 2 is the established bound for the constant derivative I+Pi_e. The executable delta is approximately 1.0000000000001e-30. With t=1/65536, the actual physical operator-residual Gram is bounded by the outward-rounded matrix

B_res=(1+t)*Q_native,up+(1+1/t)*delta^2*T.

For the actual Riesz errors R_22-V_native and rho=252/257, the established physical-to-canonical residual transport yields

E_can <= rho*B_res,

E_phys <= rho^2*B_res.

The operator residual, canonical Riesz error, and physical Riesz error remain distinct objects. All three upper matrices are stored separately. An exact rational PSD test verifies that RC67's canonical error upper minus the new canonical error upper is PSD. Multiplication by rho gives the corresponding physical-error improvement.

## Independent replay

Replay rebuilds all residual forms, evaluates the covariance using the separate reflection-reduced five-term moment formula, and verifies every saved interval encloses its independently computed directed interval. It reconstructs the native congruence, computes the trial Gram by direct physical mass sums, checks the correction and Riesz transport, and verifies the whole-matrix comparison against RC67.

Generation and independent replay passed. The enclosures are narrow enough for the required 10^-20 entry grid. All transport rounding is paid by exact diagonal row-sum allowances, and all final matrix acceptance checks use rational PSD tests.

Inputs, in order: RC80, RC79, RC67, RC59, RC56. The certificate records five SHA-256 hashes and checks the boundary, source, enrichment, native, and precision provenance links relevant to these trials.

- scripts/validate_rpb108_rc81_direct_enriched_riesz_residuals.py
- certificates/rpb108_rc81_direct_enriched_riesz_residuals.json
- notes/RPB108_RC81_DIRECT_ENRICHED_RIESZ_RESIDUALS_20261011.md

Replay with default repository input paths:

`python scripts/validate_rpb108_rc81_direct_enriched_riesz_residuals.py --replay certificates/rpb108_rc81_direct_enriched_riesz_residuals.json`

## Scope and next attachment

RC81 replaces one of RC80's retained-data assumptions: the RC67 physical Riesz-error enclosure is now sharpened. RC80's boundary remains a valid statement about its fixed enclosure family, and its nominal-allowance comparison remains unchanged. It is not a universal obstruction.

The new error matrices have not yet been propagated into the complete original projected source covariance. RC79's existing source bound 417/512=0.814453125 remains valid and is not relabeled as improved by this certificate. The next attachment is to recompute the correlated source transfer with the new physical Riesz-error Gram while preserving the original source identity and the nominal 64-mode trial vectors.

The actual canonical target head remains rank 38, and the source input scope remains 22. The required scalar source budget, any actual rank-38 budget failure, a 38-input source covariance, and an enlarged Weil floor remain unresolved. No whole-aperture positivity extension, RH, F4, or Lean formalization is claimed.
