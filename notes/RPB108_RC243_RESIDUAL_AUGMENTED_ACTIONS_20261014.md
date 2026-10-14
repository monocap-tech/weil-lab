# RPB108 — RC243: rational augmented actions on residual-shaped trials

Date: 2026-10-14 UTC. Parent RC242: `1e2f19da5e5c35addf7c7ff52d81a8b144747ef1`. Branch: research/rpb108-route-consolidation. Aperture B=11/10.

RC243 certifies the complete actual rational augmentation and augmented N actions on the exact R0/R1 inputs from RC241/242. It computes their aggregate outside-band Fourier energy, retaining every cross term among the input Legendre modes before squaring. These two new actions are ready for a subsequent enriched inverse-response calculation, which is not executed here.

The previous original-action inverse-response enclosures remain unchanged. The response sources are still N0 P0 and N0 P1. Eight inputs now have both original and augmented actions in this cohort. Full signed positivity, the original whole-space positivity gate, Stage I, RH, F4 and Lean remain open.

## Aggregate Fourier energy

For one parity input q=sum_n a_n P_n(x/B), the physical Fourier transform on its support is

\[
\widehat q(u)=2B\sum_n a_n(-i)^n j_n(2\pi Bu).
\]

Within either parity, factor out the common phase (-i)^p. The remaining signs are (-1)^((n-p)/2). Use the RC234 exact spherical-polynomial expansion j_n(s)=A_n(1/s) sin(s)+C_n(1/s) cos(s), independently checked against Legendre boundary derivatives through degree 64. Sum the signed input modes into A_q and C_q **before** forming A_q^2, C_q^2 and A_q C_q.

The complete physical outside-band energy is

\[
\tau_q=\frac{4B}{\pi}\int_{2\pi BU}^{\infty}
[A_q(1/s)\sin s+C_q(1/s)\cos s]^2ds.
\]

Every squared-input cross term is present. The nonoscillatory inverse-power moments integrate exactly. Oscillatory exp(2is) moments use the pinned finite integration-by-parts expansion and explicit remainder, with 48 terms in generation and 56 in replay. Scaled moments and outward rational rounding avoid loss from tiny inverse powers. Rational phase reduction, sine/cosine Taylor remainders, actual pi uncertainty and the physical prefactor are paid.

For the actual pi comparison, |sum a_n phase_n j_n(s)|<=sum|a_n|. Its full integral energy is bounded by the corresponding physical input norm, conservatively by 2B(sum|a_n|)^2. The RC234 lower-limit and prefactor error therefore scales by (sum|a_n|)^2. The stored outside-band energy interval uses grid 10^-24. Its lower endpoint is positive and its upper endpoint is below the exact full input physical energy. Subtracting from the latter gives a certified ideal-band input-form interval.

## Complete rational augmentation action

Let C=J*J be the ideal-band operator compressed to the physical interval. Since it is a positive contraction,

\[
\|(I-C)q\|_2^2\le\langle q,(I-C)q\rangle=\tau_q.
\]

The proof follows from (I-C)^2<=I-C; an independent exact matrix control checks this compression inequality. It is a full-output estimate, not a retained-frequency-only error.

The chosen actual rational augmentation Ahat=Fhat*Fhat satisfies the unchanged pinned operator comparison ||Ahat-C||<=epsilon. Approximate its D action by lambda D^-1 q and pay

\[
E_{\rm band}\le\lambda^2\tau_q/s_{\rm lower},
\qquad
E_{\rm rational}\le\lambda^2\epsilon^2\|q\|_2^2/s_{\rm lower}.
\]

Finite lambda/(H_n+s) coefficient intervals pay the actual s uncertainty and rounding. Add these three fault norms before squaring. The actual rational augmentation remains unchanged; the ideal band is a comparison operator, not a replacement.

Combine this complete augmentation fault norm with the RC242 complete original-action fault norm to obtain the complete augmented action. Its center is the RC242 original degree-128 output plus lambda D^-1 q, with the identity augmentation supported only in the input degrees through 64. Its complete error pays every unrepresented band output and the rational comparison.

| Certified quantity | R0 (even) | R1 (odd) |
|---|---:|---:|
| Outside-band physical energy upper, rounded upward | 0.000130899 | 0.000122146 |
| Rational augmentation squared D error upper, rounded upward | 0.005960492 | 0.006321410 |
| Complete N squared D error upper, rounded upward | 0.007504730 | 0.007873485 |
| Complete squared error / input D energy, rounded upward | 0.466618770 | 0.464283898 |
| Actual augmented input form lower, rounded downward | 0.032444262 | 0.034216826 |
| Actual augmented input form upper, rounded upward | 0.032679530 | 0.034739325 |

The form bounds add the RC242 actual original form to lambda times the band input form, and pay the actual rational-to-band form error lambda epsilon ||q||_2^2. Both lower endpoints are positive. These are two input-form tests, not the full auxiliary operator norm or an enriched inverse response.

Opposite parity makes the two new complete-action error cross pairing zero. No same-parity independence is assumed when these new columns are combined with older trials. The input-normalized action errors above are different quantities from the earlier canonical eight-source metric-inverse width and from a signed-gap positivity margin; a value below 0.5 here does not close Stage I.

## Verification and remaining step

The validator checks 164 pinned input/helper blobs. Exact replay reverses input-mode tail summation and increases the integration-by-parts count, requiring equality with the stored certificate. Spherical-polynomial boundary-derivative identities and a compression inequality provide independent exact controls. The complete physical Fourier energy partition is checked for both actual bandwidths.

Publication adds the validator, certificate and this note to RC242 while preserving existing repository blobs. The canonical eight-source metric-inverse width remains the separate 485647/1000000. The original residual trial span retains the RC242 D-form floor 61/250.

Next: evaluate the same two original-action sources on the enriched trial spaces span{P0,P2,P4,R0} and span{P1,P3,P5,R1}, enclosing all actual form cross terms and full action faults. Full signed positivity still requires the complete 248 even and 391 odd parameter channels, or an equivalent uniform proof.
