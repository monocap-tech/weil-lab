# Weil-Lab — UOI044: disjoint-prime block orthogonality and the first ten nested support stages

**Status:** Analytic finite-stage theorem, with reproducible **exact-integer/rational arithmetic screening**, **not Lean-kernel certified**. Formalization intake belongs to master ledger #898 (F04, F10, F25, F26, F34, with F01/F08 for source/native attachment). No GitHub workflow/PR or numerical NF gate promotion.

## 0. Source and exact scope

Retain precisely the UOI040–UOI043 nested family from their saved notes, with the original literal source pin `614ba879f7389fdb620c474adaee273b00eac71c`. Let

\[
 t=\log8,\quad c_j=(j+\tfrac12)t,\quad \delta_j=(1000\,8^j)^{-1},\quad I_j=(c_j-\delta_j,c_j+\delta_j),
\]

and let \(S_m\) be the smooth compact tests supported in \(D_m=\bigcup_{j<m}I_j\), with **each collar separately** carrying the three zero moments against \(1,e^{x/2},e^{-x/2}\). These are not all Schwartz tests of the window. The original crossed pole term vanishes on each \(S_m\); UOI040's analytically derived signed Gamma inequality is

\[
 \Gamma(f)\ge G\|f\|_2^2,\qquad G=\frac{2195428693}{1996093750}>\frac{1099}{1000}.
\]

Use **all** original von Mangoldt prime powers and both signs:

\[
 C_f(s)=\int_\mathbb R f(x)\overline{f(x-s)}\,dx,\qquad
 P(f)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\left[C_f(\log n)+C_f(-\log n)\right].
\]

For these tests, the analytic literal signed expression is \(W_{\rm lit}(f)=\Gamma(f)-P(f)\). Extending the pinned Lean `neutralNF600SmoothWeil_split` from its historical original collars to arbitrary \(D_m\) remains an *independent source/form identity obligation*. No theorem in this note is claimed as Lean accepted.

## 1. New structural lemma: an \(\ell^2\) prime-power edge bound, not an \(\ell^1\) bound

For each ordered pair \(0\le j<k<m\), put

\[
 \mathcal N_{jk}=\left\{n\ge2:\Lambda(n)>0,\quad
 |\log n-(k-j)\log8|<\delta_j+\delta_k\right\},\quad
 \kappa_n=\frac{\Lambda(n)}{\sqrt n},\quad
 b_{jk}=\left(\sum_{n\in\mathcal N_{jk}}\kappa_n^2\right)^{1/2}.
\]

Then the off-diagonal prime interaction from the narrower **right** collar \(I_k\) to the left collar \(I_j\) obeys the *operator* estimate

\[
 \boxed{\left\|\mathbf1_{I_j}\sum_{n\in\mathcal N_{jk}}\kappa_n\,f_k(\,\cdot+\log n)\right\|_2
 \le b_{jk}\|f_k\|_2.}
\]

**Proof.** Every such \(n\) lies below \(2\cdot8^{k-j}\), because \(\delta_j+\delta_k<\log2\). Distinct positive integers have log-spacing at least \(1/(n_{\max}+1)\). But
\[
 2\delta_k(2\cdot8^{k-j}+1)
 =\frac{4}{1000\,8^j}+\frac{2}{1000\,8^k}<1.
\]
So distinct translates of the *same* right-collar function have disjoint supports, hence are orthogonal in physical \(L^2\). The squared norm of their sum is exactly the sum of \(\kappa_n^2\|f_k\|_2^2\). Multiplying by \(\mathbf1_{I_j}\) can only decrease that norm. This is valid **before** imposing the three local moment conditions; those conditions are used instead for the pole and Gamma estimates.

Set the real symmetric nonnegative matrix \(B_m\) to have \(b_{jk}\) off the diagonal and zero on the diagonal. There are no within-collar prime shifts: \(2\delta_j<\log2\) for every j. Writing \(a_j=\|f_j\|_2\), Cauchy–Schwarz and the complete original two-sided prime normalization yield

\[
 \boxed{P(f)\le\sum_{j,k<m}b_{jk}a_ja_k
 \le\lambda_{\max}(B_m)\|f\|_2^2.}
\]

Thus UOI043's **actual** Gamma-normalized generalized eigenvalue obeys

\[
 \boxed{\rho_m\le\frac{\lambda_{\max}(B_m)}{G}.}
\]

Here \(B_m\) is an **upper-envelope** matrix in the physical collar-norm coordinates. Its Perron vector is **not** being identified with any eigenvector of the original Gamma-normalized operator \(A_m=J_m^*T_mJ_m\): the Gamma metric has nonlocal cross terms, and block norm bounds may be strict.

## 2. Fully elementary fifth-stage positive margin, including the 4093/4099 resonance

For \(m=5\) all ten cross-collar candidate sets can be enumerated with elementary logarithm/exponential comparisons. Each pair \((j,k)\ne(0,4)\) has exactly the single candidate prime power \(8^{k-j}\). The \((0,4)\) pair has exactly the three prime powers

\[
 \mathcal N_{0,4}=\{4093,4096,4099\}.
\]

This explicitly retains both extra ordinary primes; neither is swept under a ladder approximation. Elementary bounds on the actual coefficients suffice:

\[
 \kappa_8<\tfrac14,\quad\kappa_{64}<\tfrac9{100},\quad
 \kappa_{512}<\tfrac7{200},\quad\kappa_{4096}<\tfrac{11}{1000},\quad
 \kappa_{4093},\kappa_{4099}<\tfrac17.
\]

For example \(\log2<7/10\); \(\log4100<9\) and \(\sqrt{4093}>63\). By the simpler \(\ell^1\) upper on the exceptional block, every scalar adjacency row sum is **strictly below** \(17/25\); the potentially largest middle row is bounded by \(2(1/4)+2(9/100)=17/25\). Therefore

\[
 \boxed{W_{\rm lit}(f)>
 \left(G-\frac{17}{25}\right)\|f\|_2^2
 >\frac25\|f\|_2^2,\qquad 0\ne f\in S_5.}
\]

This is already a genuine **nested** five-stage restricted-support result with the *complete* prime term, not merely the powers-of-eight submodel. It is not uniform over unrestricted Schwartz tests.

## 3. A stronger exact-rational ten-stage spectral screen

For \(m=10\), the scalar \(\ell^1\) matrix is much too pessimistic: the maximum row sum exceeds 36. But the disjoint-translation \(\ell^2\) matrix remains tractable. The companion **pure-standard-library** program `rigorous_uoi044.py` performs the following finite verification:

1. For each \(j<k<10\), enclose \(e^{\delta_j+\delta_k}\) between exact rational Taylor lower/upper sums, so the integer interval \(\{n:|\log(n/8^{k-j})|<\delta_j+\delta_k\}\) is determined **without floating-point cutoffs**.
2. Enumerate **all** integers in that interval, classifying \(\Lambda(n)>0\) by exhaustive trial division (prime powers only). The widest edge \((0,9)\) contributes **14,387** prime powers in this exact search.
3. Bound \(\log p\) rationally by writing \(p=2^kr\) with \(1\le r<2\): \(\log2<7/10\) and \(\log r\le(r-r^{-1})/2\). Bound \(\sqrt n\) from below by the integer square root of \(10^{12}n\) divided by \(10^6\).
4. Round each coefficient upward to the nearest micro-unit, then each scalar block \(b_{jk}\) upward to a micro-unit, producing an **entrywise upper** integer matrix \(\widetilde B_{10}\) with denominator \(10^6\). This is an exact rational bound, **not** a sampled eigenvalue assertion.
5. Verify the ten **exact integer** inequalities \(\widetilde B_{10}v<(949/1000)v\) for

\[
 \boxed{v=(451,298,239,233,313,319,344,342,315,250)^\top>0.}
\]

By the weighted Schur/Collatz–Wielandt inequality for a symmetric nonnegative matrix, this implies

\[
 \boxed{\lambda_{\max}(B_{10})\le\lambda_{\max}(\widetilde B_{10})
 \le\max_j\frac{(\widetilde B_{10}v)_j}{v_j}
 =\frac{13369883}{14093750}
 <\frac{949}{1000}.}
\]

The compact 10×10 integer matrix and every exact prime-power interval appear in `UOI044_stage10_exact_arithmetic_receipt.json` and can be regenerated from the checker. The maximum ratio occurs at row 0. The 10-stage arithmetic bound is materially sharper than the naive prime-sum bound and is **source-faithful to all present finite-stage prime powers**.

Combining this with the positive Gamma lower bound and exact zero poles yields the main restricted result:

\[
 \boxed{\forall f\in S_{10}\setminus\{0\},\qquad
 W_{\rm lit}(f)
 >\left(G-\frac{949}{1000}\right)\|f\|_2^2
 >\frac3{20}\|f\|_2^2.}
\]

Since \(S_m\subset S_{10}\) for every \(m\le10\), the same strict margin holds at **all first ten genuinely nested support stages**. Equivalent generalized-eigenvalue screening gives
\[
 \rho_m\le\rho_{10}<\frac{949}{1000G}<1,\quad m\le10.
\]

These are *analytic* claims with a reproducible exact finite arithmetic component. They still require a separate independent mathematical/source audit and proper original Lean compilation before any formalization promotion.

## 4. What this says — and does not say — about principal eigenvectors

A positive-prime principal eigenvector of \(A_m\) (in UOI043's Gamma-form completion) cannot be supported on just one collar: the prime form is zero there, whereas \(\rho_m>0\). Thus at least two collars must participate. The multi-collar upper envelope bounds how much prime energy any such eigenvector can extract, but **does not determine its phases, support shares or frequency profile**. The positive vector \(v\) above is an *algebraic super-solution* used to bound the eigenvalue, not a recovered original eigenvector.

The \(\ell^2\) edge bound explains why UOI041's near-prime packets cost \(\sqrt{\sum \kappa_p^2}\), not \(\sum\kappa_p\): distinct translations are orthogonal when one collar is sufficiently narrow. This is a genuine source-preserving operator estimate, not a phase cancellation heuristic.

However, PNT gives \(b_{0,d}^2\sim 2\delta_0 d\log8\) as \(d\to\infty\) (with the precise fixed-relative-width interval in place). Thus \(b_{0,d}\) and the scalar envelope \(\|B_m\|\) eventually grow; a uniform infinite-stage positivity theorem cannot follow from this **Gamma-blind physical \(L^2\) bound** alone. This does **not** mean \(\rho_m\) is unbounded: the Gamma cost is stronger for very narrow remote collars, as UOI042 demonstrated for selected packets. The next real question is how to incorporate that frequency cost into a cross-collar relative-form operator estimate.

## 5. Formalization and cross-projection handoff

Allocate into existing master ledger [#898](https://github.com/monocap-tech/weil-lab/issues/898), without opening another queue:

- **F04/F25:** exact all-prime shifted-support geometry, disjointness of distinct prime-power translates, all original \(\pm\log n\) signs and weights, nested support inclusions;
- **F10:** source-typed uniform signed Gamma lower bound on the three-local-moment kernel, including exact normalization;
- **F26:** finite block-norm-to-Rayleigh theorem, weighted Schur upper certificate and first ten stages, with a genuinely compiled source-bound Lean record if pursued;
- **F34:** compare the **intrinsic** full Gamma/prime generalized spectrum under a form-preserving map. The collar graph, the powers-of-eight choice and the scalar upper-envelope matrices are support-coordinate-dependent and not preserved by arbitrary changes of basis;
- **F01/F08:** separately prove the unrestricted-source literal Schwartz identification with the original native form; no silent transfer from a specialized historic collar theorem.

**Open:** no \(\rho_m<1\) certification for all \(m\), no complete global source/core operator bridge, no all-supported Schwartz positivity and no RH. The independent NF numerical gate program is unaffected.

## 6. Reproducibility

- `rigorous_uoi044.py` — self-contained standard-library exhaustive **integer** prime-power classification, exact rational exp/log/sqrt upper bounds and 10-stage Schur inequalities; no Lean; no floating-point arithmetic in the final certificate.
- `UOI044_stage10_exact_arithmetic_receipt.json` — generated integer 10×10 upper matrix, weighted row ratios, all prime-power edge counts and exact fractions.
- `check_uoi044.py` — separate floating-point *exploratory* matrix plots/values; **not** used in the exact arithmetic proof. (Optional; keep distinct if shared.)

**Original source inputs:** saved UOI040 and UOI043 mathematical reports (explicit Γ/prime/pole conventions and nested local moment constraints); pinned original `Def_Zeta23_ExplicitFormula`, `ActualZetaOriginalCollarPrimeBound`, `ActualZetaPhaseIVOriginalNarrowSignedGamma`, and `NeutralWeilSourceMixedForm` definitions. Analytic G is imported from UOI040 as a proven-on-paper premise, not re-established in this script. No new GitHub submissions or Lean kernel evidence were created.