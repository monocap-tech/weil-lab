# RPB108 — RC238: weighted complete action tails

Date: 2026-10-14 UTC. Aperture B=11/10. Parent RC237: `867a8a506b1fffdb1c1a0d3f4454d2b5e1a31c31`. Branch: research/rpb108-route-consolidation.

RC238 reduces the complete action faults for P0, P1, P2 and P3 by weighting omitted output according to its degree. The degree-64 finite action centers, two original-action sources, two trials per parity, original trial forms, rational augmentation, and global positive augmented-inverse endpoints remain the same. Band coefficients through degree 96 are additional tail information, not new response sources or new action trials.

Both certified inverse-response upper bounds improve. Neither signed-gap interval proves positivity or an actual negative original direction. The full 639-dimensional signed form, original positivity, Stage I, RH, F4 and Lean remain open.

## Sharper original endpoint tail

For input P_d, d in {0,1,2,3}, the omitted same-parity endpoint coefficient before D^-1 is

\[
c_{n,d}=\frac{2n+1}{(n-d)(n+d+1)},\qquad n>64.
\]

Its D-energy contribution is m_n c_(n,d)^2/(H_n+s), where m_n=2B/(2n+1). The validator adds these exact positive terms, rounded individually upward to the rational grid, for degrees 65 through 256. Each term pays its own actual weight H_n+s_lower.

For n>d,

\[
\frac{2B(2n+1)}{(n-d)^2(n+d+1)^2}
\le\frac{6B}{(n-d)^3}.
\]

The inequality follows from (2n+1)(n-d)<=3(n+d+1)^2. Integrating the decreasing upper bound after M=256 and using H_n>=H_first on the remaining parity gives

\[
\sum_{n>M,\ n\equiv d\ (2)}
 \frac{m_n c_{n,d}^2}{H_n+s}
\le\frac{3B}{(H_{\rm first}+s_{\rm lower})(M-d)^2},
\]

where first is the first same-parity degree above M. Dropping parity in the scalar sum only increases the bound. Intersect with the previous endpoint-tail upper bound. All other original-action component errors are preserved; their norm bounds are added before squaring. This sharpens a complete original action, rather than assuming its projected output is the whole action.

## Weighted band-output tail

Using the pinned exact spherical-polynomial construction, extend each ideal-band Gram column G_(n,d)=<P_n,J*J P_d> through degree 96. Every retained entry through degree 64 must equal the previously certified interval exactly. The extension preserves the independent boundary-derivative checks, actual pi uncertainty, rational phase reduction, explicit oscillatory-tail remainder, and 10^-24 outer interval grid. Generation uses 48 integration-by-parts terms; replay uses 56.

Let a_n=G_(n,d)/m_n. Since C=J*J is a positive contraction, C^2<=C implies

\[
\|CP_d\|_2^2\le G_{dd}.
\]

Subtract the lower squared coefficient norms through degree 96 from the upper diagonal G_dd to obtain a physical energy upper bound R_96 for the remainder. For the omitted augmentation output after degree 64,

\[
\|\lambda D^{-1}(I-\Pi_{64})CP_d\|_D^2
\le\lambda^2\sum_{n=65}^{96}
\frac{m_n\max(|a_n^-|,|a_n^+|)^2}{H_n+s_{\rm lower}}
+\frac{\lambda^2 R_{96}}{H_{\rm first}+s_{\rm lower}}.
\]

Here first is the first same-parity degree above 96. The resolved portion is added with its actual degree weights; only the remaining output pays the degree-97/98 denominator. The diagonal interval and all subtracted retained norms refer to the same band operator. Intersect this bound with the old omitted-output bound. Finite coefficient rounding and the complete rational Fhat*Fhat-to-band operator error are preserved. They are added to the improved tail in norm before squaring. The chosen augmentation remains the exact rational RC115 augmentation.

| Input | RC237 original squared D error (approx.) | RC238 original squared D error (approx.) | RC237 complete N squared D error (approx.) | RC238 complete N squared D error (approx.) |
|---|---:|---:|---:|---:|
| P0 | 0.002962565 | 0.002071601 | 0.048863881 | 0.043830873 |
| P1 | 0.004070266 | 0.002996369 | 0.048411486 | 0.043513769 |
| P2 | 0.003013374 | 0.002072133 | 0.039995033 | 0.035284280 |
| P3 | 0.004130529 | 0.002996264 | 0.041414898 | 0.036715658 |

These decimals describe the changes; acceptance uses the certificate's exact rational endpoints. No independence of same-parity error columns is assumed. Their joint error Gram is bounded by twice the diagonal matrix of their complete squared error bounds.

## Original-action inverse responses

Reuse the RC237 coupled residual identity for the source O=N0 P_base and a two-component trial Z. The shared source/first-action original uncertainty is paid once with coefficient 1-y0. All original and augmentation faults remain full-output faults. The complete residual correction is added to the variational inverse center, and subtracted from the correlated signed-gap center. Every same-parity form cross entry remains paid.

The inherited candidate generator recomputes nominal least-residual and Galerkin proposals, interpolations and scalings. It receives the previous first-coordinate value as an additional scalar trial proposal. The full previous two-component certificate is preserved independently by intersecting the resulting enclosures with RC237; no candidate optimality is claimed.

| Quantity | Even | Odd |
|---|---:|---:|
| RC237 inverse response upper, rounded upward | 30.339060887 | 37.552320043 |
| RC238 inverse response lower, rounded downward | 0.001743553 | 0.003170373 |
| RC238 inverse response upper, rounded upward | 27.698181311 | 34.477580792 |
| RC238 signed gap lower, rounded downward | -27.609622114 | -34.380497976 |
| RC238 signed gap upper, rounded upward | 0.086815643 | 0.093912443 |

The small inherited global lower bound for N is unchanged. This pass improves the residual uncertainty that is divided by that lower bound; it does not certify a stronger complementary inverse floor. Both signed-gap intervals cross zero. The same two response sources remain a test instance of the full criterion, not exhaustive signed positivity.

## Verification and remaining work

The validator verifies 149 pinned input/helper blobs. Exact replay reverses summation order and increases the band integration-by-parts count, requiring equality with the stored certificate. Exact controls check weighted tail splitting with unequal metric weights and the signed residual identity for a nonidentity D metric with noncommuting original and augmented operators. Helper truncation globals are temporarily scoped to degree 96 and restored in a finally block; pinned helper files are unchanged.

Publication adds the validator, certificate and this note to RC237. Existing repository blobs are preserved. The separate canonical eight-source metric-inverse width stays 485647/1000000; it is not a bound for the original full auxiliary norm.

Next: reduce the remaining rational-to-band or complete-output uncertainty, certify richer residual-shaped actions, or obtain a stronger complementary inverse estimate. Completion still requires the complete signed form on the 248 even and 391 odd parameter channels, or an equivalent uniform certificate.
