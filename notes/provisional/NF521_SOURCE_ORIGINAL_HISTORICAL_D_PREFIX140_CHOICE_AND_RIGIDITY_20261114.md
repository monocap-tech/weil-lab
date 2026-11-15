# NF521 — Source-certified recovery of the first 140 authentic historical D-frame columns

**November 14, 2026 PT. Original NF505 source + exact 700-decimal outward physical Gram: LOCAL PASS. Entire 140×140 exact-integer historical-frame rigidity: LOCAL PASS. Independent regrouped exact integer audit: LOCAL PASS. Dedicated GitHub CI OPEN.** Stacked on NF520 draft PR #549, no main merge.

**This is a partial frame-recovery certificate, NOT a completed original full 242D physical fit, local \(e_H\), named NF404 physical exclusion, admissible Weil multiplier/source image/graph-domain certificate, W-ODD-NEG, global Weil form, or RH.**

## The historical matrix does not need to be reproduced bit-for-bit

The actual original NF401/RPB108 selected frame \(D\) was produced at 4096-bit Arb precision by a **positive-diagonal upper-triangular inverse Cholesky** of the complete original physical selected Gram \(G_I\), including the authentic 241 raw sin/cos source generators and sinh pole. Its dyadic SHA is

\`18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e\`.

The original NF505 4096-bit native source artifact (SHA256 \`ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec\`) preserves the *entire* authentic selected list, historical frame SHA, and an outward exact-rational all-row normalization error

\[
\|D^\top G_I D-I_{242}\|_\infty
<10^{-900}.
\]

The last fact is **source-custody certified even though the complete serialized 242×242 dyadic \(D\) entries were not archived**. NF519 showed that an alternative approximation to the same D with absolute entrywise error below \(10^{-14}\) suffices to transfer any local squared physical residual with \(<6\times10^{-30}\) frame-related error (including the NF518 globally fitted source coefficient uncertainty). NF521 establishes a *constructive*, rigorous route to that approximate D.

### Exact upper-triangular uniqueness lemma

For any positive definite \(n\times n\) symmetric \(N\), suppose \(\|N-I\|_\infty\le\epsilon<1/(100n)\). Its unique positive-diagonal **upper Cholesky** \(R\), satisfying \(R^\top R=N\), obeys

\[
\boxed{\|R-I\|_\infty\le2n\epsilon.}
\]

This follows by induction from the positive-diagonal Cholesky recurrences: if earlier off-diagonal entries are bounded by \(2\epsilon\), then their next cross-term sum is at most \(4n\epsilon^2\), and every new off-diagonal entry is bounded by \((\epsilon+4n\epsilon^2)/(1-2\epsilon)<2\epsilon\); positive diagonal square-root updates satisfy the same bound.

Let \(D_n\) be the authentic first \(n\) historical columns restricted to the first \(n\) source rows, and let \(G_n\) be the exact original \(n\times n\) leading principal full-carrier raw physical Gram. The original \(D\) is upper triangular, so

\[
D_n^\top G_nD_n=(D^\top G_I D)_{1:n,1:n},
\]
hence its genuine normalization error is bounded by the same archived \(\epsilon_{\rm old}<10^{-900}\).

For an **independently constructed rational upper-triangular positive-diagonal** \(C_n\), suppose an exact source interval proof gives \(\epsilon_C=\|C_n^\top G_nC_n-I\|_\infty\). Since \(X=C_n^{-1}D_n\) is upper-positive, Cholesky uniqueness gives \(R_{\rm old}=R_C X\). The lemma and exact Neumann bound imply

\[
\boxed{
\|D_n-C_n\|_\infty
\le\|C_n\|_\infty
\frac{2n(\epsilon_C+\epsilon_{\rm old})}{1-2n\epsilon_C}.
}
\]

This error transfer involves no assumption that the mpmath candidate itself has correct rounding, no unproved condition-number extrapolation, and no reconstruction of the old dyadic bytes. Only the **true original source normalization**, an independently source-bounded new normalization, and upper-positive triangular geometry matter.

## Actual original source first 140 columns

The leading 140 nodes are exactly the first 140 immutable original NF505 generators, beginning with frequency \(37/64\), orders 0–13, and continuing in original order through frequency \(6645/128\), order 2. These are genuine original 140-dimensional *leading columns of the historical 242-dimensional D*, not a new selected subspace or replacement frame.

A new original source generator reuses the NF520 exact analytic product-to-sum Gram machinery but upgrades to:

- **700-decimal-place** fixed integer outward interval scale \(10^{700}\).
- Original full physical carrier \(I=[-11/10,11/10]\).
- Rational Machin \(\pi\), 510 alternating arctan terms; source argument reduction **before** trigonometric series.
- Rigorous original sin/cos Taylor sums through 240 terms and exp through 400 terms, with explicit analytic tails, plus directed integer rounding.
- Every true original first-140 raw generator pair, monomial moments through degree 26, original immutable NF505 source order and SHA.

The complete true source raw 140×140 \(G_{140}\) entrywise interval width is \(<1.34\times10^{-683}\). Independently evaluated direct mpmath quadratures for five selected genuine raw Gram entries agree within numerical precision; they are **not** certificate inputs.

A 590-digit mpmath upper inverse-Cholesky proposes \(C_{140}\) with exact integer denominator \(10^{420}\). It is explicitly **UNTRUSTED as a source of correctness**. A separate exact arbitrary-integer matrix multiplication certifies the complete source interval congruence \(C^\top G_{140}C\) using every outward source interval box, paying the entire 140-row interval perturbation by a rigorous induced-norm bound.

Actual source-certified quantities (displayed decimal values are explanatory; acceptance uses full Fractions):

\[
\boxed{
\epsilon_C
=\|C_{140}^\top G_{140}C_{140}-I_{140}\|_\infty
<4.016\times10^{-305}
}
\]

and

\[
\boxed{\|C_{140}\|_\infty<3.931\times10^{143}.}
\]

Combining with the genuine old full D normalization error \(<10^{-900}\), the rigorous exact-rational triangular transfer gives

\[
\boxed{
\|D_{140}-C_{140}\|_\infty
<4.420\times10^{-159}
<10^{-14}.
}
\]

**All 140 authentic historical D prefix columns are now source-certified as physical functions to far better than NF519's required frame transport tolerance.** This statement is about the **upper-left 140×140 triangular prefix and its first 140 columns**, whose remaining raw rows are identically zero by upper triangularity. It does **not** certify original columns 141 through 242, which can contribute to all 242 raw physical coefficients in \(Da_*\).

### Independent local audit

A separate executable exact-integer audit re-reads the original NF505 source SHA and archived exact normalization; verifies the original prefix Gram file SHA; verifies the candidate upper-triangular positive diagonal; recomputes the entire 140×140 source congruence using the **alternative product grouping** \((C^\top G)C\); repays all source intervals and reconstructs the identical strict triangular-rigidity upper bound. **LOCAL PASS.** This does not independently reintegrate the full 140×140 original Gram from scratch. An earlier independent direct numerical spot-check of five raw Gram entries agrees, but is not a rigorous certificate.

Smaller original-prefix milestones also passed the same source-exact method: 23 columns with frame row error below \(10^{-380}\), and 100 columns with error below \(5.9\times10^{-213}\). The 140-column result is the largest *accepted* prefix in this increment.

Actual generated local source custody:

- Authenticated true NF505 source: \`ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec\`.
- 140×140 actual source G full-carrier outward interval blob SHA256: \`30322d54316ae409194bac528d6017b48208177ec89efaf322a5a0049402bd4b\`.
- 140×140 exact candidate and source-normalization/rigidity receipt SHA256: \`ed3f4dd16ada90031ab6552746564c9974ad1a8aa01ea7454cb0044a051094a7\`.
- Independent exact audit receipt SHA256: \`33ee7bba4dad901ed18035891d9fc094efde381239e3a06d7608a64e66a246ce\`.

The locally executed original source replay and all data are provided in the \`NF521_original_historical_D_prefix140_source_exact_pack.zip\` proof pack. The original 81MB NF505 native source is omitted (separately archived and SHA-locked); 140×140 generated interval Gram and 140×140 rational C candidate are included. **Do not unpickle unknown external files.**

## Mathematical standing

| Obligation | Standing |
| --- | --- |
| Original NF518 all 242 exterior Galerkin coefficients | Source-exact |
| Original NF520 full 242-dimensional Fredholm gaps on 3 named cells | Source-exact local PASS |
| NEW original first 23 historical D columns | SOURCE-EXACT LOCAL PASS |
| NEW original first 100 historical D columns | SOURCE-EXACT LOCAL PASS |
| **NEW original first 140 historical D columns** | **SOURCE-EXACT LOCAL PASS** |
| Remaining 102 authentic historical D columns | **OPEN** |
| Full actual original physical 242-vector \(\beta=Da_*\) | OPEN |
| Original true complete 242D globally fitted local \(e_{4094}, e_{4095}, e_{\cup}\) | OPEN |
| Unconditional NF404 named physical support NO-GO | OPEN |
| Weil source multiplier image/domain, W-ODD-NEG, complete signed Weil form, RH | OPEN |
| Focused GitHub CI | OPEN; no main merge |

**Next NF522:** Increase the source-certified historical D prefix from 140 through 242 (including the original sinh pole). Optimize the high-precision analytic Gram cache and exact triangular normalization so the 3,392 actual frequency-combination moments can be evaluated without dropping source correlations. Once \(C_{242}\) satisfies the *same* source-normalization/source-uniqueness test, NF519 automatically supplies \(<6\times10^{-30}\) all-cell frame transport. Contract the full accepted 242-vector \(C_{242}a_*\), form the authentic \(W-J^\top C_{242}a_*\) locally with original NF494 H/U response and source-correlation-preserving physical integrals, and test NF517's remaining \(e_H\) upper bounds. Only then can NF520's already-certified spectral gaps yield named *physical* NF404 NO-GO; even that would leave admissible Weil source image/domain and RH OPEN.
