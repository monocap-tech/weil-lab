# RPB108 — RC240: complete P4/P5 actions and three-trial signed response

Date: 2026-10-14 UTC. Aperture B=11/10. Parent RC239: `36e332a2f8bb8edfbabbda397561bde05cf9090c`. Branch: research/rpb108-route-consolidation.

RC240 certifies complete original and augmented actions on P4 and P5, including all cross entries with the previously certified trials. The response spaces become span{P0,P2,P4} even and span{P1,P3,P5} odd. The original-action sources remain N0 P0 and N0 P1: six action inputs and three trials per parity still represent only two response sources.

The richer trial spaces improve the retained source fit by about 25–26% and reduce the fully paid inverse-response upper bounds by about 15%. These are useful measurements on the same two sources. Neither signed-gap interval proves positivity or an actual negative original direction. The full 639-dimensional signed form, full original auxiliary norm gate, original positivity, Stage I, RH, F4 and Lean remain open.

## Complete new actions

Use the RC231 direct original identity

\[
N_0=I+D^{-1}(h-rI-K_{\rm reg}+K_{\rm prime}+K_{\rm pole}),
\quad r=789/125,
\quad DP_n=(H_n+s)P_n.
\]

The generic rational polynomial convolution from RC237 applies to d=4,5. Exact Legendre projection retains degrees through 64 and pays the entire remaining regular polynomial output. Independent direct integration checks the first twelve coefficients. All seven active prime powers with both translation orientations are accumulated on fifteen physical support segments before squared norms; cross-prime terms, coefficient uncertainty and moving support errors are paid. Segment reflection and affine-coordinate norm controls are inherited. Both signed pole terms use the actual new polynomial moment, degree-40 Taylor output and complete remainder bound.

For the new endpoint tails, use the RC238 summand inequality with the first omitted D weight:

\[
\sum_{n>64,\ n\equiv d\ (2)}
\frac{m_n}{H_n+s}
\left[\frac{2n+1}{(n-d)(n+d+1)}\right]^2
\le\frac{3B}{(H_{\rm first}+s_{\rm lower})(64-d)^2}.
\]

The required degree separation 65>=3d+1 is checked. This is a conservative full-output bound; the old P0–P3 columns retain their sharper RC238/239 endpoint refinements. Finite coefficient rounding, actual s, log2, regular kernel error, prime arithmetic and pole Taylor error remain paid. Component errors are added in norm before squaring.

Materialize the new ideal-band columns through degree 96 with the RC237/238 exact spherical-polynomial and oscillatory-tail machinery. Actual pi and phase errors remain included. The new complete augmentation output pays its retained degree-64 coefficient intervals, the weighted degrees 65–96, the full remainder, and the unchanged rational-to-band operator comparison.

## Exterior comparison through degree five

Extend the RC239 boundary argument to P4 and P5. Write P_d(1-v/B)=sum_k q_k v^k and let a=6U, T=2B. Rational bounds M_k for the scaled finite sine moments satisfy

\[
M_1=2/a,\qquad M_2=T/a+1/a^2,
\]

\[
M_k=T^{k-1}/a+(k-1)T^{k-2}/a^2
+(k-1)(k-2)M_{k-2}/a^2\quad(k\ge3).
\]

This follows by two integrations by parts of integral_0^(alpha T) s^(k-1) sin(s) ds, with alpha=2pi U>a. It yields the certified boundary lower bound

\[
b_d=\frac12-\frac{2}{3aT}-\frac13\sum_{k=1}^d|q_k|M_k>0.
\]

For these new inputs, bound the derivative on [-1,1] by the sum of absolute monomial derivative coefficients. This gives a conservative exact bound without assuming endpoint maxima. Together with the inherited absolute-kernel integral bound 10/3, it gives the exterior derivative bound

\[
L_d=2U+1/(6B)+(10/(3B))\sum_k k|[t^k]P_d(t)|.
\]

The positive exp(9) partial series again verifies the logarithm bound for each actual bandwidth. Downward-round w_d=b_d/L_d and verify w_d<=B. The two exterior edges contribute at least

\[
2[b_d^2w_d-b_dL_dw_d^2+L_d^2w_d^3/3].
\]

Subtract only this proved lower bound from the same band operator's full-line energy before bounding the unmaterialized interior tail. The ideal-band comparison is not substituted for the rational augmentation. The boundary lower bounds are approximately 0.36507 on P4 and 0.07786 on P5; the latter is deliberately conservative because the absolute polynomial corrections are large.

| New input | Original squared D error upper (approx.) | Augmentation squared D error upper (approx.) | Complete N squared D error upper (approx.) |
|---|---:|---:|---:|
| P4 | 0.002526135 | 0.015581419 | 0.030655187 |
| P5 | 0.003523095 | 0.016895455 | 0.035848947 |

Acceptance uses exact certificate endpoints rather than these approximate decimals.

## Coupled three-dimensional form and response

All original form entries F0=V*D N0 V and rational frequency Gram entries Gy=(Fhat V)*(Fhat V) are enclosed. Original pairings pay retained coefficient intervals and model faults; omitted projected outputs are orthogonal to each polynomial test input. Both transposed evaluations are intersected. Frequency entries likewise intersect transposed ideal-band values and pay the rational-to-band operator error times the two input masses. Every same-parity off-diagonal entry is retained.

The old two-by-two form blocks must equal their RC239 intervals exactly. Symmetric row-sum radii provide three-by-three Loewner bounds. The lower frequency Gram and lower augmented trial form F0+lambda Gy are checked positive definite by exact rational arithmetic. Complete action error columns are not assumed orthogonal: their joint error Gram is bounded by three times the diagonal of their squared error bounds.

For O=N0 P_base and Z=y0 P_base+y2 P_(base+2)+y4 P_(base+4), the complete residual e=O-NZ shares the first original action with its source. Its fault norm is bounded by

\[
|1-y_0|\sqrt{E_{0,0}}+
|y_2|\sqrt{E_{0,2}}+|y_4|\sqrt{E_{0,4}}+
\sum_{i\in\{0,2,4\}}|y_i|\sqrt{E_{a,i}}.
\]

Use the actual full residual D energy and inherited positive mu/nu bounds for its inverse correction. The inverse-response correction is added to the variational center. In the correlated signed identity, with u=e0-y,

\[
\Delta=u^*F_0u+\lambda y^*G_y y-
\langle e,N^{-1}e\rangle_D,
\]

the correction is subtracted. All interval cross terms retain their actual signs. Candidate trials include nominal least-residual and Galerkin proposals, rational interpolations and scalings, zero, and the full previous two-component upper trial extended by a zero third component. New certified enclosures are intersected with RC239; no actual-response optimality is claimed.

## Fit diagnostics and numerical results

For the fixed retained action centers and midpoint D weights, exact least-squares arithmetic computes the minimum retained residual energy on the old and new trial spaces. The three-trial minimum must lie between zero and the two-trial minimum. These values quantify the fit of the finite centers; they are not full actual-action residual certificates or full inverse-response values.

| Retained-center diagnostic (approx.) | Even | Odd |
|---|---:|---:|
| Two-trial nominal minimum D-midpoint residual energy | 0.021310679 | 0.023043989 |
| Three-trial nominal minimum D-midpoint residual energy | 0.016083214 | 0.016958340 |

The certified responses separately pay every omitted output, model fault and actual metric interval:

| Certified quantity | Even | Odd |
|---|---:|---:|
| RC239 inverse response upper, rounded upward | 27.409606521 | 34.033877539 |
| RC240 inverse response lower, rounded downward | 0.003684508 | 0.005386796 |
| RC240 inverse response upper, rounded upward | 23.389542374 | 29.021020187 |
| RC240 signed gap lower, rounded downward | -23.300983178 | -28.923937371 |
| RC240 signed gap upper, rounded upward | 0.084874688 | 0.091696020 |

Both signed-gap intervals still cross zero. The fit diagnostics support further trial enrichment or residual-shaped trial construction, but they do not predict how many passes would complete the full gate.

## Verification and remaining gate

The validator checks 155 pinned input/helper blobs. Exact replay reverses summation orders and strengthens band integration-by-parts evaluation from 48 to 56 terms, requiring certificate equality. Independent controls verify the three-dimensional signed residual identity in a nonidentity D metric with noncommuting original and augmented operators, and check all 64 symmetric interval vertices for the three-dimensional row-sum Loewner enclosure.

Publication adds this note, the validator and the certificate to RC239 while preserving existing repository blobs. The separate canonical eight-source metric-inverse width remains 485647/1000000. Full signed positivity still requires the complete 248-dimensional even and 391-dimensional odd parameter spaces, or an equivalent uniform proof. Six certified action inputs and two response sources do not establish that coverage.

Next: use the source-fit diagnostics to select richer actual trials or stronger complementary inverse estimates. Preserve the full signed criterion as the completion requirement.
