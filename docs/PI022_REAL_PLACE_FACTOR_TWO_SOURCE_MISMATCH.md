# PI022 — Literal Chapter 12/13 REAL-PLACE factor-of-two mismatch on a common admissible smooth test

**Weil-Lab PI### Potential Interface — ANALYTIC-FIRST ONLY.** Stacked on \`research/pi021-analytic-halfline-laplace-spectral-rigidity\`; original NF numerical certification remains compiler-active, IV and CP independent analytic investigations. This stage adds only this source memo and one standalone exact Fraction script. **NO new Lean modules, PR, Actions workflow, or CI job.**

**Central finding:** The literal geometric/arithmetic sides of Masullo Theorems 12.5.1.1 and 13.3.1.1 are **NOT the same as printed**. In the rational-number-field case, Chapter 12 multiplies its REAL local Connes–Weil principal value by **1/2**, while Chapter 13 prints **1** times the corresponding real principal value with the same multiplicative Tamagawa measure. For source test functions supported off the identity these principal values become ordinary integrals, so a delta/contact renormalization cannot eliminate this difference. On the explicit PI019 smooth derivative-bump phase contrast in BOTH proposed theorem domains, the extra local integral is STRICTLY NONZERO.

This **invalidates PI021's "identical geometric sides" hypothesis H for the formulas as literally printed**. It does not assert either formula is actually true or false, or establish global RH/GRH or the existence of a spectral operator. A missing normalization factor/rewritten expression is a specific source-repair obligation that must be paid before any half-line spectral rigidity can be applied.

## 1. Exact primary source locations and literal coefficients

Personally re-opened the **actual 940-page primary PDF** and visually inspected these pages (not a discussion summary):

Alessandro Maria Masullo, *The Music of the Primes* (November 2026 manuscript),
https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf

| Source page | Exact printed content relevant to PI022 |
|---|---|
| **p.519, equation (12.5.1.1)**, PDF index 518 | \(\sum_{v\ {\rm real}}\boxed{\tfrac12}\int'_{F_v^\times}\varphi(g)|g|_v^{1/2}/|1-g|_v\,d\mu_v(g)\) plus complex factors \(\boxed{1/(2\pi)}\) and finite place coefficient \(\log(q_v)/\mu_v(\mathcal O_v^\times)\); equals pole evaluations MINUS the full \(N(c)\) spectral sum over a specified strip, with hypothesis \(\varphi(C_F^1)=0\). |
| **p.520**, PDF index 519 | Proof cites original global kernel and fixes zero sum as \(-\sum_{c,I}N(c) M(\varphi)(c|\cdot|_F^{-1/2})\). No replacement by capped critical-line divisor is established here. |
| **p.522, equations (13.3.1.3)–(13.3.1.5)**, PDF index 521 | Claims the critical-line-only \(\min\{N(c),[F:\mathbb Q]\}\) sum equals two pole evaluations **MINUS** the real/complex local sum with **NO 1/2 or 1/(2π) written** and MINUS the finite place sum with \(\log(q_v)\) (no \(/\mu_v(\mathcal O_v^\times)\) shown). Its moment-domain restriction is (13.3.1.2). The page also leaves a "Theorem ??", "Insert statement" and "State and prove the Main Theorems" immediately following. |
| **p.560, Definitions A.3.1.2 and A.3.2.2**, PDF index 559 | For the real local field the additive Tamagawa measure is \(dx\), and the **multiplicative** Tamagawa measure is \(\boxed{d\mu_\infty(x)=dx/|x|}\). For \(\mathbb Q_p\), \(\mu_p(\mathbb Z_p^\times)=|\operatorname{disc}(\mathbb Z_p/\mathbb Z_p)|_p^{1/2}=\boxed{1}\). Thus at \(F=\mathbb Q\) the finite coefficients \(\log p/\mu_p\) and \(\log p\) DO agree; the explicit real factor 2 is not absorbed by a finite local coefficient. |
| **pp.619–620**, PDF indices 618–619 | Appendix B.4.3 identifies the \(\mathbb R^\times\) **canonical** modulated Haar measure as \(\mu_{\rm can}=\tfrac12\mu_\infty\) and \(\mathbb C^\times\) canonical Haar as \((2\pi)^{-1}\mu_v\). Appendix B.4.4 introduces Connes–Weil principal values for the same \(\mu_v\). On p.619 **footnote 16 explicitly requests rechecking factors of 2 and 2π**. This is an unambiguous source warning, not a post hoc conjecture from the Weil-Lab project. |

The Chapter 13 appendix subscript \(\alpha_{v,0}\) denotes the standard additive character used in principal-value regularization, NOT an independent multiplicative Haar factor of 1/2. For any local test which **vanishes in a neighborhood of \(g=1\)**, all these principal-value extensions agree with the ordinary absolutely convergent local integral, so the mismatch is testable without evaluating a divergent principal value.

**Do NOT generalize the rational-field finite coefficient observation to arbitrary number fields**: at ramified finite places \(\mu_v(\mathcal O_v^\times)\) can differ from 1. The complex archimedean factor discrepancy also requires independent comparison beyond the \(F=\mathbb Q\) case.

## 2. Source-exact real-place calculation: the original physical Gamma kernel appears twice

Let \(h\in C_c^\infty(\mathbb R;\mathbb C)\) with support a positive distance from 0. Use the norm-radial local test \(f_h(x)=h(\log|x|)\) on \(\mathbb R^\times\). Then \(f_h(1)=0\) and \(f_h\) actually vanishes near \(\pm1\), so the source principal value reduces to an ordinary integral. The literal **bare Tamagawa** real integral is
\[
\mathsf R_{\mu}(h)=\int_{\mathbb R^\times}
h(\log|x|)\frac{|x|^{1/2}}{|1-x|}\frac{dx}{|x|}.
\]
Put \(u=\log|x|\). The \(x=+e^u\) and \(x=-e^u\) branches combine to yield
\[
\begin{aligned}
\mathsf R_{\mu}(h)
&=\int_{\mathbb R}h(u)e^{u/2}
\left(\frac1{|1-e^u|}+\frac1{1+e^u}\right)du\\
&=\boxed{2\int_{\mathbb R}h(u)\,
\frac{e^{-|u|/2}}{1-e^{-2|u|}}\,du}.
\end{aligned}
\tag{PI022-real}
\]
The last expression involves the **literal PI007/PI018 physical Gamma kernel**
\(K(u)=e^{-|u|/2}/(1-e^{-2|u|})\) for \(u\ne0\). No analytic continuation or incomplete integral subtraction is required, because supp(h) avoids the origin.

Therefore the printed local real terms evaluate as
\[
\boxed{
\mathsf A_{12,\infty}(h)=\frac12\mathsf R_{\mu}(h)
=\int h(u)K(u)\,du,\quad
\mathsf A_{13,\infty}(h)=\mathsf R_{\mu}(h)
=2\int h(u)K(u)\,du.}
\tag{PI022-factor-2}
\]
**Exact source coefficient difference:**
\[
\boxed{
\mathsf A_{13,\infty}(h)-\mathsf A_{12,\infty}(h)
=\int hK.}
\tag{PI022-delta}
\]

This is a physical **distributed** difference, not a scalar \(c h(0)\). Both source formulas can be compared at nonzero h with \(h(0)=0\), where principal-value normalization ambiguity at the identity disappears entirely.

As an exact support point check at \(u=\log9\),
\[
K(\log9)=\frac{27}{80},\quad
\mathsf R_\mu\text{ integrand density at }\log9=\frac{27}{40}.
\]
The latter is exactly twice the original physical kernel, with no floating-point numerical fit.

## 3. Smooth test in BOTH stated domains with provably nonzero correction

Take \(a=\log9\), a nonzero nonnegative \(\rho\in C_c^\infty(\mathbb R)\) of support diameter \(d<a\), and put \(\phi=\rho'\), \(\psi(x)=\phi(x-a)\) and
\[
s_\beta=(\phi+\beta\psi)/\sqrt2,\quad
h_\beta(u)=\int s_\beta(x)\overline{s_\beta(x-u)}dx.
\]
The old PI019 calculation is exact:
\[
D_e=h_1-h_{-1}=C(u+a)+C(u-a),\quad
C(v)=\int\phi(x)\phi(x-v)dx.
\]
Because the bumps are separated and \(\int\phi=0\),
\[
\boxed{D_e(0)=0,\qquad \int_{\mathbb R}D_e(u)du=0.}
\tag{PI022-double-domain}
\]
This is a **genuine smooth, compactly supported** complex-linear *difference* of two diagonal autocorrelations. It is not itself asserted to be a positive autocorrelation. Its norm-radial lift is a natural candidate for both manuscript theorem domains, subject to the actual \(\mathcal D(C_\mathbb Q)\) lift and Haar disintegration.

For \(\lambda_n=2n+\tfrac12\), define
\[
I_a=\int C(v)K(a+v)dv
=-\sum_{n\ge0}\lambda_n^2e^{-\lambda_na}
\left(\int\rho(x)e^{-\lambda_nx}dx\right)
\left(\int\rho(y)e^{\lambda_ny}dy\right).
\tag{PI022-sign}
\]
Every summand is strictly **negative** since \(\rho\ge0\) and nonzero, and the series converges absolutely because \(a>d\). Since K is even,
\[
\boxed{\int D_e(u)K(u)du=2I_a<0.}
\tag{PI022-witness}
\]
Consequently,
\[
\boxed{
\mathsf A_{13,\infty}(D_e)
-\mathsf A_{12,\infty}(D_e)
=2I_a<0,}
\tag{PI022-actual-falsifier}
\]
even though \(D_e(0)=\int D_e=0\). Hence the geometric expressions are **not identical on the two domains' intersection as literally printed**. No correction \(c h(0)+d\int h\), no choice of PI018 compensation anchor, and no additive-character delta adjustment at \(g=1\) can make this term disappear.

The imaginary-phase difference \(D_o=i[C(u-a)-C(u+a)]\) also lies in both domains, but its real-place contribution is **zero** by K evenness. The two probes thus distinguish an actual real-place scale mismatch from phase-blind scalar contact shifts.

This **reverses the sign** of PI019's positive-phase-bump experiment: for the derivative-bump moment-zero witness we have \(I_a<0\), so the extra local term is negative. Sign is dictated by the source shape, not by support adjacency alone.

## 4. Corrected implication of the TWO printed trace identities

Let \(P(h)\) denote their common *printed* pair of Mellin pole evaluations and \(\mathsf P_{p}(h)\) the common local finite-place sum for \(F=\mathbb Q\), where \(\mu_p(\mathbb Z_p^\times)=1\). Write
\[
\mathsf Z_{12,I}(h)=\sum_{c\in\Omega(C_\mathbb Q)_I:L(c)=0}
N(c)\,M(\varphi_h)(c|\cdot|^{-1/2}),
\]
and \(\mathsf Z_{13,\rm cap}(h)\) for Chapter 13's **critical-line-only capped** sum. Their source indexing and admissibility remain extra hypotheses.

**IF** both source formulas actually hold on a given common radial test, their printed signs give
\[
\begin{array}{rcl}
\mathsf A_{12,\infty}(h)+\mathsf P_p(h)
 &=&P(h)-\mathsf Z_{12,I}(h),\\
\mathsf Z_{13,\rm cap}(h)
 &=&P(h)-\mathsf A_{13,\infty}(h)-\mathsf P_p(h).
\end{array}
\]
Hence the **actual necessary relation implied by the two printed statements**, not an assertion already proved by either source, is
\[
\boxed{
\mathsf Z_{12,I}(h)-\mathsf Z_{13,\rm cap}(h)
=\mathsf A_{13,\infty}(h)-\mathsf A_{12,\infty}(h)
=\int_{\mathbb R}h(u)K(u)du.}
\tag{PI022-corrected-spectral}
\]
In particular, **for the explicit overlap witness**,
\[
\boxed{
\mathsf Z_{12,I}(D_e)-\mathsf Z_{13,\rm cap}(D_e)=2I_a<0.}
\tag{PI022-source-test}
\]

The previous PI020–PI021 conjectural premise that both printed formulas have exactly the SAME geometric sides, and hence require **zero** spectral difference on the overlap, is therefore **REFUTED AS A LITERAL READING of this source edition**.

This does **not** prove the Chapter 13 formula independently or find an actual nontrivial zeta zero off the line. It does **not** license concluding the claimed trace formulas are inconsistent without verifying all spectral-index and cutoff conventions. It gives a **precise necessary local normalization/source-correction gate**: either explain an extra real-place factor in a nonprinted convention, explicitly change the Chapter 13 real local coefficient, or prove how a nonzero real-place residual is carried by the spectral sum. Any modification must be source-custodied as an audited change, not silently assumed in a cross-projection equality.

The spectral rigidity theorem of PI021 remains correct, but its required source hypothesis \(\mathfrak B(D_e)=\mathfrak B(D_o)=0\) does **not** follow from the two **literal** equations (12.5.1) and (13.3.1). No RH/simplicity corollary may be promoted on that basis.

**Zero-strip caution:** Chapter 12's zero sum is over an \(I=[-\alpha,\alpha]\) relative vertical strip, whereas Chapter 13's stated sum is critical-line-only without an explicitly matched strip. If Chapter 12's strip includes trivial zeros or other source terms, extra frequencies enter. The choice \(I\) and corresponding source dependence must be fixed before any strengthened infinite-divisor comparison; PI022 does not hide this issue under a "sum over all nontrivial zeros" shorthand.

## 5. What the original appendix itself warns about

Appendix B.4.3, **printed p.619, footnote 16** expressly flags the author's intention to have the proof rechecked for the **factors of 2 and \(2\pi\)** and the value-at-zero coefficients. The same page explains \(\mu_{\rm can}=\mu_v/2\) for a real place and \(\mu_{\rm can}=\mu_v/(2\pi)\) for a complex place. That is precisely the normalization seam PI022 has now made independently testable using the original physical kernel.

This is a **manuscript-level normalization discrepancy** as printed, not a result that some unrelated source has secretly established RH. The independent PI018 Gamma anchor \(\eta_*=e^{-3|u|/2}\) is a separate *contact compensation gauge* and cannot compensate for a distributed factor-two error on functions supported away from the origin.

## 6. Independent exact regressions, no Actions

\`scripts/pi022_real_place_factor_two_exact_preflight.py\` checks only exact arithmetic:
- **14** rational-square points \(u=\log q\), each in positive and negative branches: real-place bare density is exactly \(2K(|u|)\), while source Chapter 12 half equals \(K(|u|)\);
- the actual \(u=\log9\) source physical value \(K=27/80\), bare density \(27/40\);
- **100** finite source \(K_N\) values of an exact **SIGNED DISCRETE two-atom model**, not a smooth test, with nonzero strict phase normalization contrast; at N=1 the Chapter 12 signed pairing is \(-1/3\) and Chapter 13 bare pairing \(-2/3\);
- three independent scalar-contact control coefficients cannot erase the mismatch when h(0)=∫h=0.

All are \`fractions.Fraction\` checks, no numerical quadrature, genuine zeta-zero evaluation, independent trace proof, Lean, or RH. The smooth derivative-bump inequality (PI022-sign) is a separate classical analytic derivation, not proved by a finite discrete control.

**Zero new .lean, pull requests or Actions workflows**. This protects the existing compiler backlog; NF remains the sole compiler-priority lane.

## 7. PI023 — next analytic-only obligation

1. Determine whether the Chapter 13 omitted \(\tfrac12\) at the **real place** (and \(1/(2\pi)\) at complex places) is an editorial error or whether a separately defined source principal-value convention absorbs those factors. The off-identity smooth witness shows any claimed absorption must explain the **actual Haar measure**, not a delta-at-identity correction.
2. Fix the source-visible finite-field factor \(\mu_v(\mathcal O_v^\times)\), and compare its exact values and finite prime corrections for arbitrary number fields; at \(F=\mathbb Q\) it is 1, so the real mismatch persists.
3. Compare Chapter 12 full-\(N(c)\) and Chapter 13 critical/capped-\(N_{\rm spec}(c)\) sums **against the corrected nonzero local residual** (PI022-corrected-spectral), rather than setting their difference to zero.
4. Investigate whether a fully source-matched spectrum could reproduce the explicit real-place residual \(\int hK\) on the complete translated phase family; preserve possible trivial zero poles, zero-strip choice, and principal-value conventions.
5. If a revised manuscript removes the mismatch, freeze exact source revision/Git blob and redo the source comparison; never silently carry a later correction into the November edition.
6. Feed the phase-preserving source test to IV and CP analytic research without claiming their finite support graph or certified finite zero roster already implies full spectral equivalence. Continue NF numerical CI independently.

**PI022 verdict:** the assumption that Chapter 12 and Chapter 13 have an identical globally normalized geometric side is **not supported by their displayed formulas**. There is an explicit, non-contact **factor-two** archimedean discrepancy on common-domain smooth tests. This is a more immediate and falsifiable source gate than PI021's conditional infinite-rigidity argument. No proof of RH, spectral-operator equivalence, or global Weil positivity follows.
