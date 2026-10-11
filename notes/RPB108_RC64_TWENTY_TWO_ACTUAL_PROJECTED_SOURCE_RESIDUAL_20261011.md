# RPB108 RC64 — actual rank-22 projected source residual

RC64 certifies an explicit Loewner upper bound for the original source after the actual canonical orthogonal projection onto native Riesz features 0 through 21. The resulting uniform bound is

\[
\Gamma_{22}\preceq \frac{230}{3}M_{22}.
\]

The prior RC62 unprojected bound was 8414545/65536, approximately 128.39577. The new projected bound is approximately 76.66667, a 40.29% reduction. It is a paid variational bound; the exact actual projection coefficients remain unknown.

## Attachment and proof

Write the original source as Sigma_plus = R + sigma, where R consists of the actual canonical Riesz representatives. Because R lies in the projection range, the projected residuals of Sigma_plus and sigma coincide.

The nominal physical original source is F_plus = q + K_nom V. RC61 supplies the physical trial archimedean and prime head intervals and signed pole moments; RC62 supplies the complete signed physical source covariance U. Their trial pairing is assembled as

\[
H=J^*+Q_{V,\mathrm{nom}}-V^*G_{\mathrm{nom}}V,
\qquad J=\langle q,V\rangle_{\mathrm{phys}}.
\]

The identity target q is included explicitly. The archimedean nominal head is the full trial form, so subtracting the nominal trial metric extracts its bounded remainder. The pole products retain their parity-dependent signs. All 22 by 22 ordered pairings are enclosed, including exact opposite-parity zeros.

A rounded exact rational trial coefficient matrix L is obtained from the paid trial canonical metric upper bound. For Y = i* F_plus - V L, its canonical Gram is bounded by

\[
Y^*Y\preceq \rho U-H^*L-L^*H+L^*G_{V,\mathrm{up}}L+\mathcal R,
\qquad \rho=252/257.
\]

The diagonal row-sum allowance R pays pairing interval widths. The actual metric error uses the inherited RC59 upper budget 10^-7. Every finite matrix rounding is transported by a diagonal row-sum Loewner allowance.

RC60's full correlated physical and canonical Riesz error matrices pay the two differences between this nominal variational residual and the actual source minus R L. RC62's complete parity operator bounds and corrected archimedean source approximation error pay the source transfer. Fixed Young parameters 1/32 for physical source approximation, 1 for source versus representative errors, and 1/4 for nominal versus error residuals yield the recorded matrix upper bound A.

Since the actual canonical orthogonal projection minimizes distance to its range, Gamma_22 is bounded by A. Exact rational PSD checks certify A <= 23 P_22. The inherited M_22 >= (3/10) P_22 then gives Gamma_22 <= (230/3) M_22. No approximate coefficient matrix is identified with the actual projection solve.

## Independent replay

Generation expands the variational quadratic. Replay instead completes the square around G_V,up^-1 H:

\[
\rho U-H^*G_{V,\mathrm{up}}^{-1}H
 +(L-G_{V,\mathrm{up}}^{-1}H)^*G_{V,\mathrm{up}}(L-G_{V,\mathrm{up}}^{-1}H).
\]

The exact rational results agree after the paid interval and rounding allowances. Replay also verifies provenance hashes and all PSD inequalities for the nominal residual, source transfer, representative error, combined error, and final uniform comparison. Floating arithmetic is not used as proof evidence.

## What remains open

RC63 limits the scalar Schur budget, using the inherited 1250-complement floor, to strictly below approximately 1.70845e-11. RC64's certified upper bound is approximately 4.48749e12 times that ceiling, so this bound does not certify the required budget. A large upper bound does not prove actual residual failure. The inherited complement floor concerns 1250 features; no rank-22 complement floor is asserted.

No positive uniform 22-feature Weil floor, negative Weil direction, full 1250 projection, aperture extension, RH, or F4 conclusion is established. The actual low-eight positive floor remains valid. The next useful refinement is sharper source projection transport or new actual complementary lower witnesses, together with tighter treatment of the weak head directions.

## Added artifacts

- `scripts/validate_rpb108_rc64_twenty_two_projected_source_residual.py`
- `certificates/rpb108_rc64_twenty_two_projected_source_residual.json`
- This report.

Historical milestone artifacts remain unchanged.
