# RPB108 — RC237: complete P2/P3 actions and two-trial signed response

Date: 2026-10-14 UTC. Aperture B=11/10. Parent RC236: `6100c1496dd1e90c6070ae58f1602c5424dd0027`. Branch: research/rpb108-route-consolidation.

RC237 certifies complete original and augmented actions on P2 and P3. Adding these as response trials tightens the RC236 enclosures for the same two original-action sources N0 P0 and N0 P1. There are now four action inputs, two response sources, and two trials per parity. This does not evaluate the complete 639-dimensional signed matrix established in RC236.

## Complete new actions

Write m_n=2B/(2n+1), D P_n=(H_n+s)P_n, with the actual pinned interval for s. Use the direct RC231 original form identity

\[
N_0=I+D^{-1}(h-rI-K_{\rm reg}+K_{\rm prime}+K_{\rm pole}),
\qquad r=789/125.
\]

The regular convolution is computed for a general polynomial input. If P_d(2y-1)=sum_m v_m y^m and the regular kernel is sum_k a_k u^k, the left convolution has coefficient

\[
2B\,a_k(2B)^k v_m\frac{k!m!}{(k+m+1)!}
\]

at degree k+m+1 in y. Reflection supplies the right convolution with parity d. Exact Legendre projection separates the retained degrees through 64 from the full polynomial tail. The generic formula replays the established P0/P1 formulas, and its first twelve new projection coefficients are independently integrated.

All seven active prime powers, each with both translation orientations, are accumulated on the fifteen support segments before taking norms. Thus same-input cross-prime terms are retained. Moving logarithmic supports and coefficient intervals are paid in a complete physical error bound. Segment reflection and independent affine-coordinate norm integration are checked exactly. Both signed pole contributions use degree-40 Taylor polynomials, their actual moment against P_d, and an explicit full-output Taylor error.

The endpoint matrix uses the exact off-diagonal coefficient (2n+1)/(|n-d|(n+d+1)), with the pinned diagonal log2 enclosure. Its omitted D-output bound is 3B/[s_lower(64-d)^2]; the degree condition 65>=3d+1 is checked. Finite coefficient intervals pay the actual s interval and rational rounding. Complete errors include endpoint, regular and prime omitted outputs, kernel approximation, prime arithmetic, and pole Taylor remainder.

The RC234 ideal-band materialization extends to columns d=2,3. The spherical-polynomial product moments are cached through the required degree 64+d+2; parity uses d modulo two and all phase factors remain exact rationals, including entries n<d. Generation uses 48 integration-by-parts terms; replay uses 56. Actual pi uncertainty and phase reduction errors are included. The stored band Gram intervals have grid 10^-24.

For the band operator C=J*J, positivity and C^2<=C bound the omitted physical output by G_dd minus the retained output norm. Applying D^-1 and the actual augmentation coefficient gives its D-energy tail. The pinned operator error between Fhat*Fhat and J*J is also paid. The complete N action combines the original and augmentation fault norms by the triangle inequality.

| New input | Original squared D error upper (approx.) | Augmentation squared D error upper (approx.) | Complete N squared D error upper (approx.) |
|---|---:|---:|---:|
| P2 | 0.003013374 | 0.021052089 | 0.039995034 |
| P3 | 0.004130529 | 0.019387030 | 0.041414898 |

Exact rational endpoints, retained coefficients and segment polynomials are in the certificate. These displayed decimals are descriptive.

## Coupled forms and response trials

For each parity set V=(P_base,P_(base+2)). The actual original form F0=V*D N0 V and frequency Gram Gy=(Fhat V)*(Fhat V) retain all same-parity cross entries. Each original entry pairs the retained action coefficient with the actual D weight; omitted projected outputs are orthogonal to the test polynomial. Only model faults, rather than omitted-output faults, enter this form pairing. Both transposed evaluations are intersected. Frequency cross entries likewise intersect the two materialized columns and pay the rational-to-band operator error.

Entrywise intervals give Loewner bounds using diagonal row-sum radii. The frequency and augmented trial-form lower matrices are checked positive definite exactly. Complete action errors are not assumed orthogonal: their two-column error Gram is bounded by twice the diagonal matrix of their squared error bounds.

For O=N0 P_base and trial Z=y0 P_base+y2 P_(base+2), let e=O-NZ. The original source shares its action error with the first trial action. Its complete residual fault norm is bounded by

\[
|1-y_0|\sqrt{E_{0,\rm base}}+|y_2|\sqrt{E_{0,\rm new}}
+|y_0|\sqrt{E_{a,\rm base}}+|y_2|\sqrt{E_{a,\rm new}}.
\]

Forward and reverse triangle bounds enclose the complete residual D energy. With the inherited actual mu D<=DN<=nu D bounds, the inverse response is enclosed by the trial center plus the residual correction between ||e||_D^2/nu and ||e||_D^2/mu. The correction is added to the inverse response.

For u=(1-y0,-y2), the signed gap uses the correlated identity

\[
\Delta=u^*F_0u+\lambda y^*G_y y-\langle e,N^{-1}e\rangle_D.
\]

Only in this signed-gap expression is the residual correction subtracted. Signed entrywise interval quadratics pay every cross term. Candidate trials include exact nominal least-residual and Galerkin proposals, rational interpolations and scalings, the old one-trial choice, and zero. Proposals do not establish optimality. Acceptance uses full certified errors. New enclosures are intersected with RC236.

| Quantity | Even | Odd |
|---|---:|---:|
| RC236 inverse response upper | 33.165073156 | 42.510248123 |
| RC237 inverse response lower, rounded downward | 0.001714346 | 0.003138127 |
| RC237 inverse response upper, rounded upward | 30.339060887 | 37.552320043 |
| RC237 signed gap lower, rounded downward | -30.250501691 | -37.455237227 |
| RC237 signed gap upper, rounded upward | 0.086844850 | 0.093944689 |

Both inverse upper bounds and both signed lower bounds improve. Neither parity proves a positive signed gap or an actual negative original direction. The full auxiliary norm below one remains uncertified.

## Verification and remaining gate

The validator checks 146 pinned input/helper blobs. Replay reverses exact summation orders and strengthens band-tail evaluation, then requires equality with the generated certificate. All published paths are additions to the RC236 head; existing repository blobs are preserved.

The canonical eight-source metric-inverse width remains 485647/1000000. It is a different operator/source response and is not an original auxiliary norm bound. Full positivity still requires the entire RC236 signed form on the 248-dimensional even and 391-dimensional odd parameter spaces, or an equivalent uniform certificate. Original positivity, Stage I, RH, F4 and Lean remain open.

Next: use the coupled action/form interface for residual-shaped richer trials or stronger complementary inverse estimates, while retaining complete signed-form coverage as the completion requirement.
