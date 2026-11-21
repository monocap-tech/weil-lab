# PI018 — Analytic-only exact contact anchor, full diagonal Gamma extension, and a falsifiable spectral compatibility test

**Lane:** independent PI### Potential Interface. Based on the exact original PI007 physical kernel, PI008 original finite digamma symbol and upstream Gamma frequency convention, with all later PI009–PI017 source work retained. Source base branch: \`research/pi017-source-exact-core-pr-gate-and-contact-interface\` (draft PR #835). PI registry: issue #792.

**OPERATING MODE:** ANALYTIC-FIRST / NO NEW ACTIONS. This stage contains only a mathematical memo and an exact-arithmetic script. **No new .lean theorem candidates, compiler workflows, or pull requests are created.** Existing pending Lean workflows remain pending; they are NOT declared PASS. NF### numerical certification continues independently, as do IV### and CP### analytic research. No global Weil positivity, RH/GRH, Masullo operator diagonal extension, or complete cross-projection equivalence is claimed.

## 1. Exact source-specific starting point

Reopened the literal upstream-related PI source files in the existing project branch:

- \`WeilDefect/Arithmetic/PI007FiniteGammaKernel.lean\`, Git blob \`598fe925b129fcf8eb7d5fd5b94e7849a9e82ef9\`: **exact source** \`K_N(u) = ∑_(0≤n<N) exp(-(2n+1/2)|u|)\`.
- \`WeilDefect/Arithmetic/PI008FiniteDigammaSymbol.lean\`, Git blob \`276d2b3caca7686aacceafaa19e723655b03e3a1\`: **exact source** \`Ω_N(r) = -γ-logπ+∑_(0≤n<N) (1/(n+1) - a_n/(a_n²+(r/2)²))\`, \`a_n=n+1/4\`.
- \`docs/PI008_FREQUENCY_MAJORANT_AND_FORMALIZATION_GATE.md\`, Git blob \`8054beb59e45b11847f4db17d14d341fe4ff0355\`: **classical analytic** source-frequency error \`|Ω(r)-Ω_N(r)|≤3/N+8r²/N²\` for N≥1, and the explicit \`A_N(h)\` finite archimedean pairing.
- Genuine external convention: \`Zeta23.paperFT h r = ∫h(u)e^{+iru}du\`, upstream \`Zeta23/Defs.lean\` Git blob \`8024700cbfefb54d763b487afa84c03fef58a550\`; \`gammaBracket = Re ψ(1/4+ir/2)-logπ\`, \`Zeta23/ExplicitFormula.lean\` blob \`11119489556113fd419d7b6fb45ccbaa2e493e2a\`.

Denote \`H_N=∑_(n<N)1/(n+1)\`. For \`h∈C_c^∞(ℝ;ℂ)\`, let
\[
F_h(r)=\int_{\mathbb R}h(u)e^{iru}du,\quad
A_N(h)=\frac1{2\pi}\int_{\mathbb R}F_h(r)\,\Omega_N(r)\,dr,\quad
A(h)=\frac1{2\pi}\int_{\mathbb R}F_h(r)\,\Omega(r)\,dr.
\]
The PI007–PI008 **classical** finite Fourier identity gives
\[
\boxed{A_N(h)=(H_N-\gamma-\log\pi)h(0)-\int_{\mathbb R}h(u)K_N(u)du.}
\tag{PI018-1}
\]
This is an identity of the **archimedean Gamma term**, not the full original signed Weil quadratic form or an independently certified Masullo trace theorem.

## 2. Main discovery: a unique exponential anchor cancels H_N *exactly*

For \`a>0\`, define the **auxiliary compensation function** \(\eta_a(u)=e^{-a|u|}\). It is continuous and Lipschitz but **not smooth at u=0**. It is used ONLY as a subtraction device, not presented as an admissible compactly supported smooth test for Masullo's theorem.

Because the physical finite kernel is a finite sum, ordinary absolutely convergent real integrals give
\[
\begin{aligned}
I_{a,N}
&:=\int_{\mathbb R}\eta_a(u)K_N(u)\,du
 =\sum_{n=0}^{N-1}\frac{2}{a+2n+1/2}\\
&=\boxed{\sum_{n=0}^{N-1}\frac{1}{n+a/2+1/4}.}
\end{aligned}
\tag{PI018-2}
\]

Set **a=3/2**. Every summand becomes \(1/(n+1)\), so
\[
\boxed{\int_{\mathbb R}e^{-3|u|/2}K_N(u)\,du=H_N,\qquad\forall N\ge0.}
\tag{PI018-3}
\]
This is an exact finite-level equality, not an asymptotic, approximate integral, chosen constant fit or a claim about the spectral operator.

**Uniqueness within positive exponential anchors:** if \(I_{a,N}=H_N\) for every N≥1, then at N=1,
\(2/(a+1/2)=1\), hence **a=3/2**. Conversely a=3/2 satisfies every N. There may exist other *nonexponential* normalizing functions; uniqueness is claimed only in the one-parameter family \(\eta_a=e^{-a|u|}\).

Define \(q_h(u)=h(u)-h(0)\eta_*(u)\), where \(\eta_*=\eta_{3/2}\). Substituting (PI018-3) into (PI018-1) gives
\[
\boxed{
A_N(h)=-\,(\gamma+\log\pi)\,h(0)
-\int_{\mathbb R}q_h(u)K_N(u)\,du,
\qquad\forall N\ge0.}
\tag{PI018-4}
\]
The contact coefficient **no longer diverges with truncation level**. The original source fixes it at \(-\gamma-\log\pi\) *relative to this specific anchor*. This number by itself is **not invariant under a change of compensation anchor**.

## 3. Complete classical limit for ALL smooth compact tests, including h(0) ≠ 0

The physical limit kernel for u≠0 is
\[
K(u)=\sum_{n=0}^{\infty}e^{-(2n+1/2)|u|}
=\frac{e^{-|u|/2}}{1-e^{-2|u|}},
\quad
K(u)-K_N(u)=\frac{e^{-(2N+1/2)|u|}}{1-e^{-2|u|}}.
\]
Near zero, \(K(u)\sim1/(2|u|)\); one cannot separately integrate a general h(u)K(u) when h(0)≠0. But \(q_h(0)=0\) and its **Lipschitz** behavior suffices; smoothness of the compensation anchor itself is *not* needed:

For all real u,
\[
|q_h(u)|\le
\underbrace{\left(\|h'\|_{\infty}+\tfrac32|h(0)|\right)}_{L_*(h)}
|u|.
\tag{PI018-5}
\]
Here the first inequality uses the mean value bound for smooth h and
\(|1-e^{-3|u|/2}|\le(3/2)|u|\). Since h is compactly supported and eta_* decays, q_h is integrable at infinity and q_h K is absolutely integrable near the origin and at infinity.

The elementary inequality
\[
\frac1{1-e^{-2u}}\le1+\frac1{2u}\qquad(u>0)
\]
gives for \(N\ge0\) and \(\alpha_N=2N+1/2\):
\[
\boxed{
\left|\int_{\mathbb R}q_h(u)(K(u)-K_N(u))du\right|
\le L_*(h)\left(\frac1{\alpha_N}+\frac2{\alpha_N^2}\right).
}
\tag{PI018-6}
\]
This **extends PI007's physical-tail estimate to arbitrary h(0)**, with the necessary contact compensation. It is a new analytic quantitative statement, not an appeal to a finite-dimensional Gram certificate.

On the independent frequency side, PI008 already established, for N≥1,
\[
\boxed{
|A(h)-A_N(h)|\le\frac1{2\pi}
\left(\frac{3M_0(h)}N+\frac{8M_2(h)}{N^2}\right),
\quad
M_j(h)=\int_{\mathbb R}|r|^j|F_h(r)|dr<\infty.
}
\tag{PI018-7}
\]

Combine (PI018-4), (PI018-6), (PI018-7):
\[
\left|A(h)+(\gamma+\log\pi)h(0)+
\int_{\mathbb R}q_h(u)K(u)du\right|
\le
\frac{3M_0/N+8M_2/N^2}{2\pi}
+
L_*(h)\left(\frac1{\alpha_N}+\frac2{\alpha_N^2}\right).
\tag{PI018-8}
\]
Both bounds tend to zero as N→∞. Thus the **complete classical signed-source Gamma distribution** for *every* complex smooth compact test is
\[
\boxed{\displaystyle
A(h)=-(\gamma+\log\pi)h(0)
-\int_{\mathbb R}
\Big(h(u)-h(0)e^{-3|u|/2}\Big)
\frac{e^{-|u|/2}}{1-e^{-2|u|}}du.}
\tag{PI018-MAIN}
\]
The integral is genuinely absolutely convergent; no divergent terms were discarded.

**Certification boundary:** this is a classical analytic deduction from the original PI007–PI008 definitions, Fourier identity and explicit tail. It is NOT a kernel-accepted Lean theorem nor a literal compiled IV011 original-source bridge. It also does NOT assert the existence of a Masullo operator on the diagonal domain.

## 4. General anchor covariance: what is intrinsic and what is gauge

For arbitrary a>0 define
\[
C_{a,N}:=(H_N-\gamma-\log\pi)-I_{a,N}
=-\gamma-\log\pi+
\sum_{n<N}\left[\frac1{n+1}
-\frac1{n+a/2+1/4}\right].
\]
The authentic digamma series gives the limit
\[
\boxed{C_a:=\lim_{N\to\infty}C_{a,N}
=\psi\left(\frac a2+\frac14\right)-\log\pi.}
\tag{PI018-9}
\]
Then the equivalent family of distributions is
\[
A(h)=C_a h(0)-\int_{\mathbb R}(h(u)-h(0)\eta_a(u))K(u)du.
\tag{PI018-10}
\]

Explicit anchors:
- a=1/2: \(\psi(1/2)=-\gamma-2\log2\), hence \(C_{1/2}=-\gamma-\log(4\pi)\).
- **a=3/2**: \(\psi(1)=-\gamma\), hence \(C_{3/2}=-\gamma-\log\pi\), **exactly at every finite N**.
- a=7/2: \(\psi(2)=1-\gamma\), hence \(C_{7/2}=1-\gamma-\log\pi\).

Since \(\eta_a-\eta_b=O(|u|)\) at zero, the following is an ordinary absolutely convergent integral:
\[
\boxed{C_a-C_b
=\int_{\mathbb R}(\eta_b(u)-\eta_a(u))K(u)du.}
\tag{PI018-11}
\]
Thus the complete distribution A(h) is **independent of the anchor**, whereas the displayed scalar C_a is a **gauge/coordinate-dependent contact coefficient**. It would be a category error to declare \(-\gamma-\log\pi\) an intrinsic cross-projection invariant without specifying the \(\eta_*\) gauge and the original logarithmic norm coordinate.

The exact finite anchor a=3/2 is source-selected by the original a_n=n+1/4 coefficients plus the harmonic terms. If those source normalizations, support coordinates or Fourier signs were changed, its special value would have to be rederived. This is a strong local analytical *calibration choice*, not global support capacity or a positivity proof.

## 5. Falsifiable test of the INDEPENDENT Masullo operator

Suppose (a genuine additional hypothesis!) an independently defined Masullo spectral trace or operator provides a scalar-valued **archimedean component** \(T_{\mathrm{spec}}(h)\) on some diagonal-admissible test family \(\mathcal D\), **after independently matching all arithmetic/primes and source sign conventions**. Define for h∈D with h(0)≠0:
\[
\boxed{
\mathfrak C_{\mathrm{spec}}[h]
=
\frac{T_{\mathrm{spec}}(h)+
\displaystyle\int_{\mathbb R}(h(u)-h(0)\eta_*(u))K(u)du}
{h(0)}.}
\tag{PI018-DIAGNOSTIC}
\]
**Necessary exact compatibility condition:**
\[
\mathfrak C_{\mathrm{spec}}[h]=-\gamma-\log\pi
\quad\text{for every valid diagonal test }h.
\tag{PI018-FALSIFIER}
\]

Interpretation:
- If the genuine operator is **undefined** on all h(0)≠0 tests, this diagnostic is **not yet evaluable**. This is the missing-domain hypothesis, not a successful comparison.
- If two admissible tests yield **different values** for the diagnostic, no single constant contact/mass correction can make the proposed spectral operator agree with the original Gamma distribution on both tests.
- If the values are constant but **different** from \(-\gamma-\log\pi\), the operator agrees at best up to a nonzero \(c\,h(0)\) scalar-contact correction; it does not identify the original distribution as stated.
- If the values match, this pays a necessary diagonal calibration condition on that test family; it does **not**, without further density/operator hypotheses, establish global equality, trace-class status, positivity, or RH.

For a physical Schwartz correlation \(h_{s,t}(u)=\int t(x)\overline{s(x-u)}dx\), \(h_{s,t}(0)=\langle t,s\rangle\). On a diagonal h_{s,s}, this is \(\|s\|_2^2>0\), so a false scalar contact changes the diagonal form. Orthogonal tests have h(0)=0 and cannot detect such a correction, exactly as PI006's independent information-loss result demonstrated.

**Critical admissibility caveat:** \(\eta_*\) is not itself asserted to lie in Masullo's original smooth test space, nor does Masullo's stated trace theorem cover the diagonal \(\varphi(C_\mathbb Q^1)\ne0\) regime. The diagnostic is a **falsifiable conditional conjecture**, not an evaluation already performed on Masullo's operator. The legitimate diagonal tests should come from actual admissible correlations, with eta_* appearing only as a compensator in the integral.

## 6. Independent exact regression and intentionally zero Actions fan-out

\`scripts/pi018_contact_anchor_exact_preflight.py\` carries **only** exact rational arithmetic. It symbolically integrates each physical exponential using \(\int_{\mathbb R}e^{-b|u|}du=2/b\) for b>0, rather than running floating-point quadrature. Independent equivalent execution PASS:
- **257** distinct finite N=0,…,256 harmonic cancellations for \(\eta_{3/2}\);
- **101** exact a=1/2 half-integer-harmonic identities and **101** exact a=7/2 shifted-harmonic identities;
- **28** exact finite gauge-transition equalities;
- **540** exact diagonal, including nonzero h(0), gauge-independence checks;
- finite N=1 uniqueness witness, and three distinct nonzero mass/contact offsets invisible on h(0)=0 tests.

These calculations are consistency checks, not an automatic proof of the infinite digamma identity or original spectral trace.

**No PR is opened**, because any new pull request may trigger the repository's broad generic workflows even when PI018 contains no .lean modules. The analytic branch contains **this memo and the exact-arithmetic script only**; it adds **no GitHub Actions workflow, Lean file, or automatic compiler job**. Leave the already queued actions undisturbed; preserve NF's numerical compiler priority. Registry issue #792 records PI018's mathematical status.

## 7. PI019 analytic-only handoff

1. Use the exact \(\eta_*\) contact calibration to formulate a rigorous **spectral diagonal admissibility** test against the literal statement/domain of Masullo's theorem. In particular ask whether the operator admits any independently defined extension to a dense set containing nonzero autocorrelations.
2. On such a domain, compute \(\mathfrak C_{\mathrm{spec}}[h]\) directly from the proposed spectral operator, **without importing the original Weil contact value as a definition**. Test at least two genuinely independent diagonal correlations; document any sign/normalization mismatch.
3. Compare with CP's proposed projection invariant and IV's phase-sensitive prime information, preserving the distinction between the **intrinsic** distribution A, the **anchor-dependent** C_a, and possible mass/δ corrections.
4. Prove a two-test falsification theorem: if C_spec[h_1]≠C_spec[h_2], not even a single mass-contact extension can reconcile the spectral and Gamma forms. If equal but incorrect, document a one-scalar mismatch rather than claiming equivalence.
5. Keep formalization backlog frozen on PI/IV/CP except for a genuinely decisive narrow gate with explicit budget. NF numerical certification and CI recovery continue independently.

**PI018 conclusion:** the harmonic divergence in the original finite Gamma scalar has an **exact all-N compensator**. This extends the physical-side Gamma formula to all complex smooth compact tests, with a quantitative convergence estimate. It sharpens the diagonal compatibility question into a numerical/equational **operator test** that an independent construction could actually fail. It does NOT establish such an operator or RH.
