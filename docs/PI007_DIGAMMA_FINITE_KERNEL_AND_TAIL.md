# PI007 — Finite digamma/Gamma inverse kernel with explicit analytic tails

**PI### Potential Interface**, independent continuation of PI006 PR #812. Stacked PI006 → PI005 #809 → PI004 #804 → PI003 #801 → PI002 #798 → PI001 #793. Canonical PI registry #792. No existing Phase III NF###, Phase IV IV###, or CP### research source, branch or certification status is changed.

**Certification status:** exact classical derivation and independent exact-Fraction finite-kernel sanity audit; **a small, separately labeled Lean proof candidate is committed but has not passed a compiler or axiom audit**. The difficult source-specific Fourier/digamma inverse transform remains **OPEN**. Nothing here proves Masullo's global operator trace, diagonal extension, Weil positivity, RH or GRH.

## 1. Source-exact starting points

No generic unnamed gamma distribution is substituted:

1. Authentic original mixed arithmetic source: IV011 PR #774, file \`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean\`. \`neutralIV011OriginalMixedArch\` literally uses \`Zeta23.paperFT h r\` and \`Zeta23.EF.gammaBracket r\` with coefficient \`1/(2*pi)\`.
2. \`Zeta23.paperFT h r = ∫ h(u) exp(i*r*u) du\`, upstream \`zeta23/Zeta23/Defs.lean\` (Git blob \`8024700cbfefb54d763b487afa84c03fef58a550\`). Inverse Fourier uses \`exp(-i*r*u)\`.
3. \`Zeta23.EF.gammaBracket r = Re digamma(1/4+i*r/2)-log pi\`, upstream \`zeta23/Zeta23/ExplicitFormula.lean\` (blob \`11119489556113fd419d7b6fb45ccbaa2e493e2a\`).
4. **Existing Lean theorem:** \`Zeta23.DigammaSeries.hasSum_digamma_series\` in \`zeta23/Zeta23/GammaFacts/Series.lean\` (blob \`2c6cf90050c2e6d5cbef0745d0445e3a8d02394a\`), proves
\[
\sum_{n\ge0}\Big(\frac1{n+1}-\frac1{n+1+z}\Big)
=\psi(z)+\gamma+\frac1z
\]
for z away from nonpositive integer poles. This is the source-level series to transport, **not** an integral-representation theorem that does not exist in the pinned Mathlib digamma module.
5. Mathlib \`v4.34.0\` \`Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean\` has a TODO for Gauss's integral formula. PI007 deliberately avoids treating that TODO as an available lemma.

These source identities are distinct from source-sha compilation custody; none of these observed blobs proves the present PI Lean target passed.

## 2. Derive the *correct finite partial-fraction stage* before taking limits

For \(\Re z>0\), rearrange the source's already proved series, using the telescope
\[
\sum_{n=0}^{N-1}\frac1{n+z}
=\frac1z+\sum_{n=0}^{N-1}\frac1{n+1+z}-\frac1{N+z}.
\]
As \(N\to\infty\), the last term tends to zero. Therefore
\[
\boxed{\psi(z)=-\gamma+\sum_{n\ge0}
\left(\frac1{n+1}-\frac1{n+z}\right).}
\tag{PI007-digamma}
\]

Set \(z=\tfrac14+\tfrac{ir}{2}\), \(a_n=n+\tfrac14\). Since
\[
\Re\frac1{a_n+ir/2}=\frac{a_n}{a_n^2+(r/2)^2},
\]
the actual original Gamma symbol is
\[
\Omega(r)=\Re\psi(\tfrac14+\tfrac{ir}{2})-\log\pi
=\lim_{N\to\infty}\Omega_N(r),
\]
with **fully specified finite symbol**
\[
\boxed{
\Omega_N(r)=-\gamma-\log\pi+\sum_{n=0}^{N-1}
\left[\frac1{n+1}-\frac{a_n}{a_n^2+(r/2)^2}\right].
}
\tag{PI007-finite-symbol}
\]

This is a pointwise convergent partial-fraction sequence; *not* a uniform convergence statement in \(r\). Passing its limit through the full frequency integral remains a distinct analytical/Lean obligation. Do not silently replace that step with rfl or tsum rewriting.

## 3. Exact Fourier inverse of each finite summand

For \(a>0\), the classical Fourier transform of the integrable physical kernel \(e^{-2a|u|}\) under the **positive** source exponent is
\[
\int_{\mathbb R}e^{-2a|u|}e^{iru}\,du
=\frac{4a}{(2a)^2+r^2}
=\frac{a}{a^2+(r/2)^2}.
\]
This is a directly formalizable real/complex Bochner-integral identity; a suitable named theorem must be located or proved from the two elementary half-line exponential integrals.

For \(h\in C_c^\infty(\mathbb R;\mathbb C)\), inversion yields
\[
\frac1{2\pi}\int_{\mathbb R}\operatorname{paperFT}(h)(r)
\frac{a}{a^2+(r/2)^2}\,dr
=\int_{\mathbb R}h(u)e^{-2a|u|}\,du.
\tag{PI007-atom}
\]

Let \(\mathcal A_N(h)=\frac1{2\pi}\int \operatorname{paperFT}(h)(r)\Omega_N(r)\,dr\), \(H_N=\sum_{n=1}^N1/n\). Since \(\frac1{2\pi}\int\operatorname{paperFT}(h)(r)dr=h(0)\), **for each finite N**
\[
\boxed{
\mathcal A_N(h)=\big(H_N-\gamma-\log\pi\big)h(0)
-\int_{\mathbb R}h(u)K_N(u)\,du,
}
\tag{PI007-finite-arch}
\]
where
\[
\boxed{K_N(u)=\sum_{n=0}^{N-1}e^{-(2n+1/2)|u|}.}
\]

**Important:** the contact term \((H_N-\gamma-\log\pi)h(0)\) is necessary for general h. Setting it to zero on diagonal tests is mathematically wrong. For the *Masullo-admissible norm-pullback tests* \(h(0)=0\), it disappears exactly.

## 4. Rigorous tail law, not a numerical assumption

For \(u\ne0\), a positive geometric series gives
\[
K(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}},\quad
K(u)-K_N(u)=\frac{e^{-(2N+1/2)|u|}}{1-e^{-2|u|}}.
\]
Write \(\alpha_N=2N+\tfrac12\).

If \(h(0)=0\) and \(h\) is complex C¹ with \(\|h'\|_\infty\le L\), the mean-value/FTC estimate \(|h(u)|\le L|u|\) and
\[
\frac{u}{1-e^{-2u}}\le u+\tfrac12 \quad(u>0)
\]
yield
\[
\begin{aligned}
\left|\int h(u)(K-K_N)(u)\,du\right|
&\le 2L\int_0^\infty e^{-\alpha_Nu}(u+\tfrac12)\,du\\
&=\boxed{L\left(\frac1{\alpha_N}+\frac2{\alpha_N^2}\right).}
\end{aligned}
\tag{PI007-tail}
\]
This is an explicit **uniform per-test error certificate** with a controlled derivative norm; it tends to zero as \(N\to\infty\). It does not by itself prove \(\mathcal A_N(h)\to\mathcal A(h)\) in frequency, whose summation/integration passage must be justified separately.

For any h supported away from zero, \(|u|\ge\delta>0\), the strictly stronger estimate is
\[
\boxed{
\left|\int h(K-K_N)\right|
\le \|h\|_1\,\frac{e^{-\alpha_N\delta}}{1-e^{-2\delta}}.
}
\tag{PI007-gap-tail}
\]
The PI003 physically disjoint old/old pair is in this stronger class.

At the prime-active \(u=\pm\log9\), an exact symbolic checkpoint is
\[
K_N(\log9)=\frac{27}{80}(1-9^{-2N}),\quad
K(\log9)-K_N(\log9)=\frac{27}{80}\,9^{-2N}.
\]
For N=1, the kernel is \(1/3\) and the remaining tail is \(1/240\); the exact full value is \(27/80\). These are **values of the archimedean physical kernel**, not the independent prime coefficient \((\log3)/3\).

## 5. What is actually formalized and what is not

The independent file \`WeilDefect/Arithmetic/PI007FiniteGammaKernel.lean\` is a **Lean proof candidate** on the PI-only branch. It defines the literal finite exponential kernel and proposes elementary step, nonnegativity and evenness theorems. It does not import the unavailable main-based original IV011 module and it does not contain any \`sorry\` or speculative theorem equating this finite kernel with \`neutralIV011OriginalMixedArch\`. **Its compiler status is not an accepted PASS.**

**Exact independent script:** \`scripts/pi007_digamma_finite_kernel_preflight.py\` uses only rational arithmetic for the full rational-point finite geometric identity and tail, and checks the explicit FTC-tail algebra for rational \(\alpha\). Its PASS is not a proof of the Fourier inverse, digamma theorem, or Lean source import.

### Remaining formal steps — deliver as a source-bound IV-based companion, not by altering IV

1. Prove the finite partial-fraction telescope in the actual source and derive \`gammaBracket\` as a limit of \`Omega_N\`, starting from the named \`Zeta23.DigammaSeries.hasSum_digamma_series\` theorem.
2. Prove each Fourier atom (PI007-atom), with precise positive source exponent, frequency integral and factor \(2\pi\).
3. Prove convergence of the **frequency** pairing \(\mathcal A_N(h)\to \mathcal A(h)\) using a valid uniform/tail estimate and then combine with (PI007-tail); never infer from pointwise \(\Omega_N\to\Omega\) alone.
4. Bind the resulting complex result to the authentic \`neutralIV011OriginalMixedArch\` with the actual Schwartz-window correlation. Use strict \`#print axioms\`, real compiled olean and SHA-bound source dependency audit.
5. Independently establish (or rule out) a *Masullo operator trace contact extension* matching the original Gamma-selected contact, not just a function defined to agree with the source.

**Stop boundary:** finite kernel and certified tail prepare the real-place bridge, but neither proves whole Masullo trace/Weil equivalence nor the diagonal positivity necessary for RH. The earlier PI006 scalar-mass and local-potential information-loss obstructions remain in force.

## 6. PI008 handoff

PI008 should attach the genuine source-bound Lean finite-kernel proof and attempt the first **compiler-audited** atom/finite-stage theorem, separating four receipts: source SHA, actual build, axiom audit, and mathematical limit theorem. If the compiler/Mathlib cannot establish the inverse-transform step, record that as an open formal dependency instead of inventing a certified result.

Proceed with CP/IV/NF independently; PI must not consume their authority or put unaccepted conjectures in their established ledgers.
