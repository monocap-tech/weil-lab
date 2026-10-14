# RPB108 — RC246: materialized residual band actions

Date: 2026-10-14 UTC. Parent RC245: `4ed17b420821251fcc95a2b5240f290b042b9315`. Branch: research/rpb108-route-consolidation. Aperture B=11/10.

RC246 materializes the ideal-band action on the exact residual-shaped inputs R0 and R1 through output degree 128, then pays the complete omitted output and the unchanged rational-to-band operator comparison. The resulting complete actual rational augmented-action squared errors are approximately 79–80% smaller than RC243's identity-action approximation errors.

The enriched inverse responses are not recomputed in this pass. Their previous certified upper bounds remain those of RC245. The source count stays two and there are four response trials per parity. Full signed positivity, original whole-space positivity, the full auxiliary norm gate, Stage I, RH, F4 and Lean remain open.

## Direct aggregate output pairings

For q=sum_d a_d P_d of parity p, form the same aggregate spherical-polynomial pair as RC243,

\[
A_q=\sum_d a_d(-1)^{(d-p)/2}A_d,
\qquad C_q=\sum_d a_d(-1)^{(d-p)/2}C_d.
\]

Here j_d(s)=A_d(1/s) sin(s)+C_d(1/s) cos(s). Spherical recurrences through output degree 128 are independently verified against the exact finite Legendre boundary-derivative formula. The helper truncation parameter is temporarily scoped and restored; its pinned source file is unchanged.

For each output degree n of the same parity, compute the outside-band cross integral directly from the products A_n A_q, C_n C_q and A_n C_q+C_n A_q. The physical coefficient pairing is

\[
G_{nq}=\langle P_n,Cq\rangle
=m_n a_n-\frac{4B}{\pi}(-1)^{(n-p)/2}
\int_{2\pi BU}^{\infty}j_n(s)
[A_q(1/s)\sin s+C_q(1/s)\cos s]ds.
\]

The full-line term m_n a_n vanishes above input degree 64. Opposite-parity entries are exactly zero. All input coefficients enter the aggregate polynomial before output pairing, so cross-mode cancellations in the actual source are preserved.

Integrate the nonoscillatory inverse-power terms exactly. Oscillatory exp(2is) moments use scaled integration-by-parts formulas with an explicit remainder, now with 96 terms in generation and 112 in replay. Cache the moments through the required input/output product degree. Rational phase reduction and sine/cosine Taylor errors are paid.

The actual pi lower integration limit and physical prefactor are paid for every output pairing. The pointwise aggregate bound is sum_d |a_d| because |j_d|<=1. Cauchy–Schwarz and the complete spherical Fourier-energy integrals give the corresponding prefactor bound. The pi interval is checked inside (3,4). Store outward Gram intervals on grid 10^-24. The ideal-band action coefficients are G_nq/m_n.

## Independent input-form and transpose checks

Pair the new output column with the entire exact input q. Intersect this interval with RC243's independent input physical energy minus its aggregate outside-band Fourier energy. This checks the same ideal-band input form through two separate computations.

Also pair the old materialized P4/P5 column with the full R input, and intersect it with the new column's P4/P5 output entry. Selfadjointness requires agreement; both parity checks pass. These checks help prevent a phase-sign or cross-mode error in the aggregate output construction.

## Full output tail and rational augmentation

For C=J*J, positivity and contractivity give C^2<=C and hence

\[
\|Cq\|_2^2\le\langle q,Cq\rangle.
\]

Subtract the lower squared norm of the retained band output through degree 128 from the upper intersected input form. The nonnegative difference bounds the entire remaining physical band output. Applying D^-1 and the actual augmentation coefficient gives

\[
E_{\rm omitted}\le
\frac{\lambda^2 E_{\rm physical,>128}}
{H_{\rm first}+s_{\rm lower}},
\]

where first is 130 even and 129 odd. Retained coefficients pay the actual s interval and rational rounding. The unchanged complete rational-to-band error from RC243 remains paid. Add finite-rounding, omitted-output and rational-model fault norms before squaring.

The chosen operator is still the exact RC115 rational augmentation. The ideal band serves as a rigorously bounded approximation and is not substituted for it. Add this complete augmentation fault norm to the unchanged RC242 original-action fault norm to obtain the full actual N-action error.

| Certified quantity, rounded upward | R0 (even) | R1 (odd) |
|---|---:|---:|
| Physical band output energy beyond degree 128 | 0.000043457 | 0.000042545 |
| Complete rational augmentation squared D error | 0.000858870 | 0.001011688 |
| RC243 complete N squared D error | 0.007504730 | 0.007873485 |
| RC246 complete N squared D error | 0.001500176 | 0.001683658 |
| Complete squared error divided by input D energy | 0.093275865 | 0.099281946 |

Acceptance uses the certificate's exact rational endpoints. The error reduction is measured for the same inputs, operators and D norm, while the finite approximation center is materially improved. The new input-normalized action-error numbers are not inverse-response widths or signed positivity margins.

Opposite parity makes the two-input complete-action error Gram diagonal. No same-parity independence is assumed when these columns are combined with older response trials. All unrepresented output remains paid.

## Verification and next step

The validator checks 173 pinned input/helper blobs. Exact replay reverses inverse-power summation and increases the integration-by-parts count from 96 to 112, requiring certificate equality. Independent controls verify every spherical-polynomial boundary formula through degree 128, the band input-form agreement with RC243, and the P4/P5 transpose agreement. Both complete action-error upper bounds must strictly improve on RC243.

Publication adds the validator, certificate and this note to RC245 while preserving existing repository blobs. The residual original trial span retains its D-form floor 61/250. The separate canonical eight-source metric-inverse width remains 485647/1000000. Previous original-action inverse-response upper bounds remain 7.395622002 even and 9.616684253 odd when rounded upward.

Next: reevaluate the same four-trial responses with the improved residual augmentation centers, their full errors, and the RC245 refined original-source bounds. Complete signed positivity still requires all 248 even and 391 odd parameter channels, or an equivalent uniform proof.
