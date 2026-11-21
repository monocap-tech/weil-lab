# PI008 — Explicit frequency-side digamma error, source-compatible limit and first Lean finite-symbol gate

**Lane:** PI### Potential Interface. Stacked only on PI007 #816 → PI006 #812 → PI005 #809 → PI004 #804 → PI003 #801 → PI002 #798 → PI001 #793; PI registry #792. NF###, IV###, CP### are separate and unchanged.

**Status:** closed **classical analytic** frequency-limit argument with an explicit uniform tail bound; independent exact-Fraction regression; small standalone Lean finite-symbol proof candidates, **not yet compiler-accepted**. The actual IV011 archimedean source bridge and Masullo operator trace remain OPEN. No proof of global Weil positivity, RH or GRH.

## 1. Authenticate source, conventions, and previous gap

Actual original signed IV011 source: PR #774, \`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean\`, where
\[
A(h)=\frac{1}{2\pi}\int_{\mathbb R} \operatorname{paperFT}(h)(r)\,
\operatorname{gammaBracket}(r)\,dr .
\]
Actual upstream \`Zeta23.paperFT h r = \int h(u)e^{iru}\,du\` (blob \`8024700cbfefb54d763b487afa84c03fef58a550\`, \`Zeta23/Defs.lean\`) and \`Zeta23.EF.gammaBracket r = \Re\psi(1/4+ir/2)-\log\pi\` (blob \`11119489556113fd419d7b6fb45ccbaa2e493e2a\`, \`Zeta23/ExplicitFormula.lean\`). The upstream Lean \`Zeta23.DigammaSeries.hasSum_digamma_series\` (blob \`2c6cf90050c2e6d5cbef0745d0445e3a8d02394a\`) provides an exact partial-fraction series.

PI007 prepared the correct finite symbols and established the *physical-side* tail, but explicitly left unproved the interchange between the pointwise digamma series and the **frequency integral**. PI008 resolves that classical-analytic convergence obligation; it does NOT yet supply a Lean proof.

## 2. Source-exact finite symbol and frequency tail

For \(N\in\mathbb N\), \(a_n=n+1/4\), \(t=r/2\), define
\[
\Omega_N(r)=-\gamma-\log\pi+\sum_{n=0}^{N-1}
\left(\frac1{n+1}-\frac{a_n}{a_n^2+t^2}\right).
\]
The authentic upstream digamma partial-fraction theorem and elementary index telescope imply \(\Omega_N(r)\to\Omega(r)=\Re\psi(1/4+ir/2)-\log\pi\) for each real r.

The nth summand has exact decomposition
\[
d_n(r):=\frac1{n+1}-\frac{a_n}{a_n^2+t^2}
=-\frac{3/4}{(n+1)a_n}+\frac{t^2}{a_n(a_n^2+t^2)}.
\]
Since \(a_n=n+1/4\ge (n+1)/4>0\), we get the **explicit termwise majorant**
\[
\boxed{|d_n(r)|\le \frac{3}{(n+1)^2}+\frac{16r^2}{(n+1)^3}.}\tag{PI008-atom}
\]
This bound is uniform in N, not a numerical fit.

For the *full frequency-side truncation error*, use the integral comparisons (N≥1)
\[
\sum_{k=N+1}^\infty k^{-2}\le \int_N^\infty x^{-2}dx=\frac1N,\qquad
\sum_{k=N+1}^\infty k^{-3}\le \int_N^\infty x^{-3}dx=\frac1{2N^2}.
\]
Therefore
\[
\boxed{
|\Omega(r)-\Omega_N(r)|\le \frac3N+\frac{8r^2}{N^2}\quad(N\ge1).
}\tag{PI008-frequency-tail}
\]
Additionally \(\sum_{k\ge1}k^{-2}\le2\) and \(\sum_{k\ge1}k^{-3}\le3/2\) give
\[
\boxed{|\Omega_N(r)|\le |\gamma+\log\pi|+6+24r^2\quad(N\ge0).}\tag{PI008-majorant}
\]
The same growth bound applies to the pointwise limit \(\Omega\). No unproved uniform convergence in r is invoked.

## 3. Complete the frequency integral passage with an explicit error

For \(h\in C_c^\infty(\mathbb R;\mathbb C)\), let \(F_h(r)=\operatorname{paperFT}(h)(r)\). Standard fourfold integration by parts, compact support and smoothness imply
\[
M_0(h)=\int_\mathbb R |F_h(r)|dr<\infty,\qquad
M_2(h)=\int_\mathbb R r^2 |F_h(r)|dr<\infty.
\]
Define the authentic archimedean scalar and its finite proxy:
\[
A(h)=\frac1{2\pi}\int_\mathbb R F_h(r)\Omega(r)dr,\quad
A_N(h)=\frac1{2\pi}\int_\mathbb R F_h(r)\Omega_N(r)dr.
\]
The bound (PI008-frequency-tail), a genuinely integrable majorant, and the triangle inequality give for N≥1:
\[
\boxed{
|A(h)-A_N(h)|
\le \frac{1}{2\pi}
\left(\frac{3M_0(h)}{N}+\frac{8M_2(h)}{N^2}\right).
}\tag{PI008-arch-tail}
\]
This is stronger than qualitative dominated convergence: it gives an **explicit per-test frequency error certificate**. The right side tends to zero, hence the source-sign Gamma integral is the limit of genuine finite partial fractions. In particular the step PI007 left open is closed **as classical mathematics**.

The PI007 finite Fourier-atom identity (a separate classical step) states
\[
A_N(h)=(H_N-\gamma-\log\pi)h(0)-\int_\mathbb R h(u)K_N(u)du,
\quad K_N(u)=\sum_{n=0}^{N-1}e^{-(2n+1/2)|u|}.
\]
For the Masullo-admissible **norm-only** test domain h(0)=0, the harmonic contact term is exactly zero. PI007's physical estimate, with \(\alpha_N=2N+1/2\) and \(L=\|h'\|_\infty\), is
\[
\left|\int h(K-K_N)\right|
\le L\left(\frac1{\alpha_N}+\frac2{\alpha_N^2}\right).
\]
Taking the limit on both independently controlled sides gives the full classical real-place bridge
\[
\boxed{A(h)=-\int_\mathbb R h(u)\frac{e^{-|u|/2}}{1-e^{-2|u|}}\,du,\quad h(0)=0.}
\tag{PI008-realplace}
\]
On smooth compact tests h, no assumptions that h is even, real, or zero on a whole neighborhood of 0 are needed. The only remaining obstacles to calling this **Lean-certified for IV011** are the genuine formal source attachment, frequency and physical estimates, Fourier atom, kernel build and axiom audits.

## 4. Diagonal-contact law follows by a *paid* limit, not by omitting a divergent term

For h with \(h(0)\ne0\), the finite formula includes \((H_N-\gamma-\log\pi)h(0)\), which must be retained as \(\int hK_N\) grows near zero. Since (PI008-arch-tail) holds for **any** smooth compact h, \(A_N(h)\to A(h)\) after full cancellation.

Choose \(\eta\in C_c^\infty\) with \(\eta(0)=1\), and write g=h−h(0)η. Then g(0)=0 and the source-specific identity becomes
\[
\boxed{A(h)=h(0)A(\eta)-\int_{\mathbb R}g(u)K(u)du.}
\]
The result is independent of η and agrees with PI006's compensated distribution. **This constructs only the normalization selected by the original Weil Gamma source**. It does not justify a Masullo **operator trace** at tests excluded by Masullo's theorem. Without independent contact normalization, the ambiguity proved in PI006 remains.

## 5. Formal ledger and fail-closed acceptance

New standalone candidate \`WeilDefect/Arithmetic/PI008FiniteDigammaSymbol.lean\` (Mathlib-only, on PI stack) introduces the correctly oriented finite rational Gamma symbol and elementary finite-stage recursion / evenness results. These are small pilot proofs with \`#print axioms\` targets. **They have not been kernel compiled at commit time.** They deliberately do not import \`neutralIV011OriginalMixedArch\` from a branch where the definition does not exist.

\`scripts/pi008_frequency_majorant_preflight.py\` verifies the exact rational pointwise decomposition and majorant, uniform N-tail sample checkpoints, and the exact \(n=9\) physical-kernel anchor using Fractions. This sanity check is not a formal proof of an infinite sum or the integral bound.

The existing PI007 head \`64939b1b382e92d9a8b7e140de08b21a5bad1a24\` had a generic GitHub Actions run \`44856739800\` in **queued** status when inspected; no PI007 compiler pass was established. The PI008 stage shall not call a source candidate \`LEAN PASS\` without:
1. exact source SHA, genuine compiled \`.olean\`,
2. build status and logs, with no errors,
3. \`#print axioms\` accepting only \`propext\`, \`Classical.choice\`, \`Quot.sound\`,
4. verified dependencies and a separate **actual** IV-based source companion for \`neutralIV011OriginalMixedArch\`.
No \`sorry\`, opaque theorem substitute, or assumption that Masullo's unverified global trace theorem is accepted.

## 6. PI009 next gate

PI009 should recover real compiler results and repair PI007/PI008 finite Lean pilots, then formalize the source-specific \(|d_n(r)|\) and \(|\Omega-\Omega_N|\) estimates, the Fourier atom integral, and the two controlled limit passages in an **explicit IV-based companion** (while leaving the original IV lane unchanged). If the Mathlib Fourier atom requires a missing analytic lemma, record the precise theorem signature and build it in PI as a genuine formal obligation.

Later interface tests must independently check Masullo's operator/diagonal contact normalization and Alpöge's actual arithmetic test map. Neither is implied by the now source-compatible **classical** gamma formula.
