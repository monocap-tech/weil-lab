# RPB108: exact-null exclusion of finite critical inverse-log cusp feedback

Date: 2026-10-07 UTC. Recovered live head df6ce55bb542ef47632ede187873b4276b1ee952.
Definitions: [finite cusp class and coefficient matrix](../docs/TERMINOLOGY_RPB108_FINITE_LOG_CUSP_EXCLUSION.md).
Category: critical derivative promotion / endpoint exclusion. Conditional analytic class theorem; no general kernel classification or Lean certification.

## Result and scope

The exact full-native equation excludes every nonzero finite inverse-log cusp part with exponents q>1 in the class defined above. This includes two-sided complex coefficients, cusps at genuine interior prime-shift points and both physical endpoints, at any fixed finite aperture. It is not necessary to march apertures or to regard the actual drive as independent.

The crucial distinction is that m0(D) raises the leading cusp from log^(-q) to log^(1-q), whereas the complete finite prime operator preserves its order. At an interior center the two sides couple through an invertible matrix, so neither opposite signs nor complex phase can cancel this raised order on both sides. At an endpoint the inward coefficient is nonzero.

This excludes finite cusp propagation as an exact-null repair of the previous actual-drive controls. It does NOT establish that h in K_a intersect Xcrit has such a finite expansion. Consequently the general derivative gate and whole-kernel critical membership remain open.

## 1. Exact local archimedean coefficient, retaining both sides

Write L=log(1/v), v>0. Use the pinned actual Euler formula

    m0(D)h(x)=m0(0)h(x)+integral_0^infinity
        k(s)[2h(x)-h(x-s)-h(x+s)]ds,
    k(s)=exp(-s/2)/(1-exp(-2s))=1/(2s)+k_reg(s).

For a cusp center x_j, first take a single exponent q>1 and amplitudes a_+,a_-. The value of m0(D)h at x_j exists: the singular local inverse integrals reduce to integral^infinity L^(-q)dL, which is absolute for q>1. Denote this value by c_j; it includes every other cusp, the smooth background and the regular kernel. It is not an injective scalar observation.

On the right and left respectively, subtraction of c_j gives

    m0(D)h(x_j+v)-c_j
       =[a_+ +(a_++a_-)/(2(q-1))] L^(1-q)+O(L^(-q)),
    m0(D)h(x_j-v)-c_j
       =[a_- +(a_++a_-)/(2(q-1))] L^(1-q)+O(L^(-q)).  (1)

At an endpoint only the inward formula is used, with the outside amplitude zero.

To verify the leading term, fix a small b below every separation/cutoff radius. In v<s<b, the 2h(x) part contributes a_side L^(1-q)+O(L^(-q)). After subtraction of the center value, the missing two tails contribute

    (1/2) integral_0^v [a_++a_-] log^(-q)(1/s) ds/s
       =(a_++a_-)/(2(q-1)) L^(1-q).

Replacing the shifted profiles at s+v and s-v by their profiles at s changes the result by O(L^(-q)), sufficient here. On v<s<2v this follows by scaling and bounding each log cusp by C L^(-q). On 2v<s<sqrt(v), the mean-value derivative bound C/[s log^(q+1)(1/s)] gives O(L^(-q-1)); on sqrt(v)<s<b it gives O(sqrt(v)) with a fixed polynomial factor. The small-s second difference, 0<s<v, is O(L^(-q-1)): scale s=v y, use cancellation of the constant profile and the integrability of the logarithmic differences divided by y. The tiny region where v-s approaches zero is covered by the same integrable bound. The bounded regular kernel contributes O(L^(-q))+O(v); distant terms and the smooth background vary by O(v). These bounds prove (1), for complex amplitudes by linearity.

For finitely many larger exponents their raised terms are o(L^(1-q0)), even when not O(L^(-q0)). Thus for the leading exponent q0 the full local vector coefficient is exactly B_q0(a_+,a_-) with remainder o(L^(1-q0)). No incorrectly uniform remainder for all exponents is required.

## 2. Full actual prime feedback cannot cancel the raised order

Every summand of the actual T_a is a fixed translation times Lambda(n)/sqrt(n); there are finitely many at a fixed finite a. At a translated cusp point its variation from its continuous value is O(L^(-q0)); at a smooth point it is O(v). Translations hitting an endpoint use the continuous zero extension and the appropriate one-sided profile. Threshold equalities are included. Several translated cusps may coincide, but their finite sum still has no L^(1-q0) term.

The actual pole is smooth. Therefore, at any cusp center approached from either lawful physical side,

    q_h(x_j+/-v)-q_h(x_j)
       =(corresponding row of B_q0 applied to a) L^(1-q0)
          +o(L^(1-q0)).

Here q_h(x_j) denotes its continuous limit, which exists in this class, including an inward endpoint limit. Distributional full nullity forces the pointwise equation on each punctured neighborhood, where the formula is smooth. Its limit is zero, and both available raised-order coefficients must vanish.

At an interior center, B_q has eigenvalues 1 and q/(q-1), both nonzero for q>1. The antisymmetric amplitudes cancel the shared tail but leave their own a_side L^(1-q) term. At an endpoint b_q=(2q-1)/(2(q-1))>0. Hence all amplitudes at q0 vanish at every center, contradicting its definition. Removing that exponent and repeating handles all finitely many exponents. Thus every cusp coefficient vanishes. The remaining b is smooth and in H1.

The reasoning uses the full actual homogeneous equation, rather than merely a matched exterior inverse moment, Hardy budgets, necessary flux sign or a chosen prime profile. It makes no finite-selection or historical-packet substitution.

## 3. What is excluded and what remains

The preceding log-cusp control has boundary exponent 4 and interior exponent 3. Treating both sides is essential: putting another log cusp on the other side of its prime-2 point cannot restore the homogeneous equation within this finite class. The smallest exponent already produces a nonzero interior raised-order coefficient somewhere, before any boundary order-4 repair can matter. The argument also covers any finite added set of translated inverse-log cusps with exponents >1.

It does not rule out infinitely many accumulating singular centers, non-power slowly varying profiles, oscillatory tails, or nonzero remainders outside this finite class. The actual interior log^3 gain is a norm conclusion, not an asymptotic expansion theorem. Finite prime support does not imply finite propagation or a finite singular set: repeated signed translations can produce arbitrarily many locations. No finite cusp expansion is silently assigned to K_a.

Exact failed extension: finite inverse-log cusp exclusion -> general K_a intersect Xcrit derivative promotion. Missing premise: a justified classification or an estimate covering the unclassified remainder. A finite expansion alone is insufficient if its remainder is arbitrary Xcrit; the remainder's m0 image could carry the raised-order terms.

Smallest remaining theorem remains

    actual full q_h=0, h in K_a intersect Xcrit -> h' in L2.

A direct critical boundary estimate that controls all remainders could supply it; no such estimate is proved here. Whole-contact-kernel Xcrit membership is a separate gate. The accepted external |beta_rho|<=3/8 controls transverse source corrections but changes neither the local Euler coefficient nor the prime translation order, and supplies no missing classification. No new critical positive-source moment bound is obtained. This is restricted exact-null compatibility progress, not endpoint exclusion, RH, F4 or FULL TRANSPORT CLOSED.

## Custody and checks

Sources read at the recovered live head:

- CRITICAL_LOG_CUSP_20261007: blob 235d0ad7272ed5ebdc8921adc91fef2cba3bc181.
- ACTUAL_DRIVE_CUSP_20261007: blob b0fc27ece02f8f5cbdce6d86eda4c28d60d12c81.
- CRITICAL_INTERIOR_GAIN_20261007: blob 05f53463842cb5aafbb5116c7f3a4bf65207400e.
- EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007: blob c369d3760606d9e5b9ae0f4862156fd712e5be29.

Analytic checks: the exact Euler normalization, both-side tail coefficients, error splits, continuity at the center, full finite translation order, complex/antisymmetric cancellation and endpoint support. The companion rational check verifies matrix eigenvalues and endpoint coefficients and rejects the q=1 formula; it is not an analytic proof or Lean certificate. No external theorem newly invoked, aperture computation, Lean/workflow change or axiom claim. Canonical historical wording and concurrent aperture custody are preserved additively.
