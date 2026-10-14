# RPB108 — RC239: exterior band energy sharpens interior action tails

Date: 2026-10-14 UTC. Aperture B=11/10. Parent RC238: `392adda1bc45967e02e1ec0acb1f0ce5b39a0d37`. Branch: research/rpb108-route-consolidation.

RC239 certifies a positive lower bound for the energy that the ideal full-line band projection of each P0, P1, P2 and P3 sends outside [-B,B]. Subtracting this exterior energy tightens the complete interior augmentation-action tails. The ideal band projection remains a comparison tool; the chosen augmentation is the unchanged RC115 rational augmentation, with its complete operator error still paid.

The complete action squared-error bounds fall substantially. The same two original-action inverse responses improve more modestly. Neither signed-gap interval proves positivity or an actual negative original direction. The full auxiliary norm gate, Stage I, original positivity, RH, F4 and Lean remain open.

## Full-line versus interior band output

Extend P_d(x/B) by zero outside [-B,B], and let P_U be the orthogonal Fourier projection onto [-U,U] on the full line. Set

\[
h_d=P_U(\mathbf1_{[-B,B]}P_d),\qquad
C=J^*J=\mathbf1_{[-B,B]}P_U\mathbf1_{[-B,B]}.
\]

With the unchanged Fourier phase 2pi u x, the real kernel is

\[
K_U(y)=\frac{\sin(2\pi U y)}{\pi y},\qquad K_U(0)=2U.
\]

Plancherel and P_U^2=P_U give

\[
G_{dd}=\langle P_d,CP_d\rangle
=\|h_d\|_{L^2(\mathbb R)}^2
=\|CP_d\|_{L^2([-B,B])}^2
+\|h_d\|_{L^2(\mathbb R\setminus[-B,B])}^2.
\]

RC238 bounded the interior output by G_dd, discarding the last nonnegative term. RC239 obtains an explicit positive lower bound for that term. All quantities in this subtraction concern the same ideal band operator.

## Certified boundary value

At the right boundary, write alpha=2pi U, T=2B and expand P_d(1-v/B)=sum_k q_k v^k. Its constant coefficient is 1, so

\[
h_d(B)=\frac1\pi\left[
\operatorname{Si}(\alpha T)
+\sum_{k=1}^d q_k\alpha^{-k}
\int_0^{\alpha T}s^{k-1}\sin s\,ds\right].
\]

For W>0, integration by parts gives |integral_W^infinity sin(s)/s ds|<=2/W. Hence Si(W)/pi>=1/2-2/(pi W). For degrees one through three, the finite sine moments have respective absolute bounds 2, W+1 and W^2+2W+4. Use pi>3 and alpha>6U to pay all polynomial corrections by exact rational arithmetic. The resulting b_d>0 is a certified lower bound for h_d(B). The boundary-distance polynomials are independently checked against their explicit degree-at-most-three formulas.

## Exterior derivative and positive envelope

For B<=x<=2B, integration by parts in the physical convolution gives

\[
h_d'(x)=K_U(x+B)P_d(-1)-K_U(x-B)P_d(1)
+B^{-1}\int_{-B}^{B}K_U(x-t)P_d'(t/B)dt.
\]

The two endpoint terms have absolute bounds 1/(6B) and 2U. Also |K_U(y)|<=min(2U,1/(pi y)) for y>0. Integrating on [0,3B], splitting at 1/(2pi U), yields

\[
\int_0^{3B}|K_U(y)|dy
\le\pi^{-1}[1+\log(6\pi BU)]\le10/3.
\]

The final inequality uses pi in (3,4) and log(24BU)<9. The latter is checked for both actual bandwidths by the positive degree-20 rational series lower bound for exp(9), which exceeds 24BU. The exact derivative suprema on [-1,1] for d=0,1,2,3 are 0,1,3,6. Thus

\[
L_d=2U+\frac1{6B}+\frac{10}{3B}\|P_d'\|_\infty
\]

bounds |h_d'| throughout the stated exterior interval. For 0<=r<=w_d<=b_d/L_d, h_d(B+r)>=b_d-L_d r>=0. Take w_d as the downward-rounded b_d/L_d and verify w_d<=B. Reflection gives the same energy at the left boundary, including odd d. Integrating the two linear envelopes provides the exterior energy lower bound

\[
\ell_d=2\left(b_d^2w_d-b_dL_dw_d^2+
\frac{L_d^2w_d^3}{3}\right)>0.
\]

All rounding in ell_d is downward. This is a rigorous exterior energy estimate, not a sampled boundary profile. No orthogonality between different same-parity input errors is inferred.

| Input | Boundary value lower (approx.) | Two-edge exterior energy lower (approx.) | RC238 physical tail after degree 96 (approx.) | RC239 physical tail after degree 96 (approx.) |
|---|---:|---:|---:|---:|
| P0 | 0.499213 | 0.000645837 | 0.000812442 | 0.000166605 |
| P1 | 0.498525 | 0.000395925 | 0.000518050 | 0.000122125 |
| P2 | 0.492122 | 0.000577807 | 0.000809093 | 0.000231287 |
| P3 | 0.481303 | 0.000332170 | 0.000515839 | 0.000183670 |

The table describes exact certificate endpoints; its displayed decimals are approximate.

## Complete action and response consequences

Subtract ell_d from the RC238 upper bound G_dd minus captured interior energy through degree 96. The result is asserted nonnegative and bounds the unmaterialized interior physical output. Apply the same degree-97/98 D^-1 weight, then add the unchanged degree-65-through-96 weighted output bound. Finite rounding and rational-to-band faults remain paid in norm. Original action errors retain the RC238 weighted endpoint refinement.

| Input | RC238 complete N squared D error (approx.) | RC239 complete N squared D error (approx.) |
|---|---:|---:|
| P0 | 0.043830873 | 0.020852199 |
| P1 | 0.043513769 | 0.024944301 |
| P2 | 0.035284280 | 0.017538254 |
| P3 | 0.036715658 | 0.023007215 |

The same-parity two-column error Gram remains bounded by twice the diagonal matrix of the complete squared errors. The finite degree-64 action centers, original form intervals and frequency trial Gram intervals remain unchanged. Reuse the RC237 coupled source/action residual formula, including coefficient 1-y0 for the shared original uncertainty. Signed cross terms and the full positive augmented-inverse mu/nu correction remain paid. Preserve RC238 by interval intersection. Trial candidates establish enclosures, not optimality.

| Quantity | Even | Odd |
|---|---:|---:|
| RC238 inverse response upper, rounded upward | 27.698181311 | 34.477580792 |
| RC239 inverse response lower, rounded downward | 0.001747068 | 0.003175237 |
| RC239 inverse response upper, rounded upward | 27.409606521 | 34.033877539 |
| RC239 signed gap lower, rounded downward | -27.321047325 | -33.936794723 |
| RC239 signed gap upper, rounded upward | 0.086812128 | 0.093907579 |

The modest response improvement despite much smaller action tails indicates a remaining limitation in the present source fit and original-action uncertainty. It does not quantify the number of further passes needed. The actual response sources remain N0 P0 and N0 P1, with two polynomial trials per parity; this is still a small test of the complete RC236 signed criterion.

## Verification and remaining gate

The validator checks 152 pinned input/helper blobs and requires exact equality on replay with reversed inherited residual summation. The mathematical tail bounds use explicit analytic inequalities and exact rational endpoint calculations. An independent rational orthogonal-projection control checks the full-line/interior/exterior energy split and conservative exterior subtraction; derivative suprema and boundary-distance polynomials are checked separately. No helper source files are changed.

Publication adds the validator, certificate and this note to RC238 while preserving existing repository blobs. The canonical eight-source metric-inverse width remains 485647/1000000; it concerns a separate operator and source family. Full original auxiliary norm below one still requires signed positivity over the complete 248-dimensional even and 391-dimensional odd parameter spaces, or an equivalent uniform bound.

Next: improve the exterior envelope if useful, certify residual-shaped richer actions, or strengthen complementary inverse estimates. A two-source improvement alone does not close Stage I.
