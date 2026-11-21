# PI004 — The real-place trace kernel and the original signed Gamma/digamma distribution

**Independent PI### Potential Interface:** stacked ONLY on PI003 #801 → PI002 #798 → PI001 #793. Registry #792. This changes no NF### Phase III, IV### Phase IV, or CP### research branch. **Status: exact classical analytic dictionary on compact mixed correlations vanishing near zero, subject to explicit source Fourier-symbol convention; no Lean kernel certificate and no proof of Masullo's global trace theorem.**

## 1. Inspect the actual source, not an illustrative replacement

**Masullo manuscript** (November 2026), *The Music of the Primes*:
https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf

- **Theorem 12.5.1.1**, printed page 519 / PDF index 518, formula **(12.5.1.1)**: at each **real** place the geometric term is
\[
G_\infty(\varphi)=\frac12\int_{\mathbb R^\times}^{\prime}
  \frac{\varphi(g)|g|^{1/2}}{|1-g|}\,d\mu_\infty(g).
\]
- **Definition A.3.2.2**, printed page 560 / PDF index 559, sets the archimedean multiplicative Tamagawa measure \(d\mu_\infty(g)=dg/|g|\); its additive real Tamagawa measure is Lebesgue \(dg\) (Appendix A.3.1, Example A.3.1.5).
- The full claimed theorem is \(G_\infty+\sum_pG_p = M(\varphi)(|\cdot|^{1/2})+M(\varphi)(|\cdot|^{-1/2})-\mathrm{Zero}_I(\varphi)\), where the zero sum lies in the author's specified *relative strip* I. This is NOT a previously accepted Weil equality, nor an independently verified operator trace.

**Literal original Weil-Lab source:**
- IV011 PR #774: \`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean\` defines \`neutralIV011OriginalMixedArch\` as
\[
\operatorname{Arch}_{\rm IV011}(s,t)
=\frac1{2\pi}\int_{\mathbb R}\operatorname{paperFT}(h_{s,t})(r)
\operatorname{gammaBracket}(r)\,dr;
\]
and defines the original pole pair as \(\operatorname{paperFT}(h)(i/2)+\operatorname{paperFT}(h)(-i/2)\). The literal prime component retains all genuine von Mangoldt coefficients and signs.
- The **standard centered mathematical gamma symbol** to identify with this original \`gammaBracket\` is
\[
\Omega(r):=\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{i r}{2}\right)-\log\pi,
\]
where \(\psi=\Gamma'/\Gamma\). The exact Lean definition and \`paperFT\` convention need to be bound to this formula for a **source-specific Lean theorem**. This document proves the classical Fourier identity using \(\Omega\), and marks the in-repository symbol substitution as an outstanding formal source gate, not an assumption quietly discharged.

## 2. Exact real-place reduction (for PI mixed tests)

Let \(s,t\in C_c^\infty(\mathbb R,\mathbb C)\) be the physical original Schwartz tests, and
\[
h(u)=h_{s,t}(u)=\int_{\mathbb R}t(x)\overline{s(x-u)}\,dx.
\]
For both PI's disjoint old/new pair and the especially discriminating old-minus/old-plus pair from PI002–PI003, the supports are disjoint with positive distance. Therefore \(h(u)=0\) **on some open interval containing zero**, a stronger property than \(h(0)=0\).

Define the norm-pullback \(\varphi(g)=h(\log|g|_{\mathbb Q})\). On \(\mathbb R^\times\), separate \(g=\pm v\), with \(v>0\). Since h vanishes near 0, the integrand vanishes near \(g=1\); **the primed integral is an ordinary absolutely convergent integral**, and no principal-value extension must be postulated on this restricted test class:
\[
G_\infty(h)=\frac12\int_0^\infty
h(\log v)v^{1/2}\left(\frac1{|1-v|}+\frac1{1+v}\right)\frac{dv}{v}.
\]
Set \(u=\log v\); direct simplification for \(u>0\) and \(u<0\) yields the **same even physical kernel**:
\[
\boxed{
G_\infty(h)=\int_{\mathbb R}h(u)K(u)\,du,\qquad
K(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}}\quad(u\ne0).
}
\tag{PI004-real}
\]
A complex h is allowed; the transform is complex-linear in h. There is no extra factor two or Haar volume factor: Masullo's displayed \(1/2\) exactly pays for the two real signs.

At the previously identified \(\log9\) prime-active shift:
\[
K(\log9)=\frac{(1/3)}{1-1/81}=\boxed{\frac{27}{80}}.
\]
The same kernel value holds at \(-\log9\). This is an **exact rational kernel anchor** separate from the p-adic coefficient \(\log3/3\). It does NOT replace the smooth-bump integral by a point evaluation.

## 3. Independent Fourier–digamma deduction

For \(h\in C_c^\infty(\mathbb R;\mathbb C)\), fix the **non-unitary angular Fourier transform**
\[
\widehat h(r)=\int_{\mathbb R}h(u)e^{-iru}\,du,\quad
h(u)=\frac1{2\pi}\int_{\mathbb R}\widehat h(r)e^{iru}\,dr.
\]
The evenness of \(\Omega(r)\) ensures that the opposite sign convention for the paper transform gives the same scalar archimedean integral; the \(2\pi\) factor must still be authenticated against IV011.

Use the classical digamma representation (for \(\Re z>0\))
\[
\psi(z)=-\gamma+\int_0^\infty
\frac{e^{-v}-e^{-zv}}{1-e^{-v}}\,dv.
\]
Since \(h\) vanishes in a neighborhood of zero, \(\frac1{2\pi}\int \widehat h(r)dr=h(0)=0\), so the constant \(-\gamma-\log\pi\) and \(e^{-v}h(0)\) terms disappear. Fourier inversion gives
\[
\frac1{2\pi}\int_{\mathbb R}
\widehat h(r)\cos(rv/2)\,dr=\frac{h(v/2)+h(-v/2)}2.
\]
One can justify the interchange with a positive lower cutoff on \(v\), rapid Fourier decay and then dominated convergence; the vanishing neighborhood removes the singularity at \(v=0\). Therefore
\[
\begin{aligned}
\frac1{2\pi}\int_{\mathbb R}\widehat h(r)\Omega(r)\,dr
&=-\int_0^\infty \frac{e^{-v/4}}{1-e^{-v}}
 \frac{h(v/2)+h(-v/2)}2\,dv\\
&=-\int_0^\infty
 \frac{e^{-u/2}}{1-e^{-2u}}\bigl[h(u)+h(-u)\bigr]\,du\\
&=-G_\infty(h).
\end{aligned}
\]
Hence the **exact classical distribution identity, on this vanishing-near-zero test domain**, is
\[
\boxed{\operatorname{Arch}_{\Omega}(h)=-G_\infty(h).}
\tag{PI004-arch}
\]
The equality is unconditional mathematics for the explicit functions \(\Omega\) and K and test class stated; it does **not** certify Masullo's theorem or the Lean meaning of the source \`gammaBracket\`. Matching the repo's \`Zeta23.paperFT\` and \`Zeta23.EF.gammaBracket\` to these exact expressions remains a source-binding obligation, not a free renormalization.

## 4. Pole dictionary and the diagonal/contact obstruction

PI002 showed by the \(\mathbb Q\) Tamagawa norm disintegration that, for \(\varphi=h\circ\log|\cdot|\),
\[
M(\varphi)(|\cdot|^{z})=\int_{\mathbb R}h(u)e^{zu}du.
\]
Therefore Masullo's displayed two polar evaluations at \(z=\pm1/2\) become \(\int h(u)e^{u/2}du+\int h(u)e^{-u/2}du\), matching IV011's original \`paperFT(h)(±i/2)\` **provided the original Fourier sign/argument is source-checked** (the sum is insensitive to a global sign reversal of Fourier exponent).

The sign ledger:
\[
\begin{aligned}
\text{Masullo's displayed trace:}\quad&
G_\infty+\sum_pG_p=\mathrm{Pole}-\mathrm{Zero}_I,\\
\therefore\quad&\mathrm{Zero}_I=\mathrm{Pole}-\sum_pG_p-G_\infty,\\
\text{original IV011:}\quad&
W=\mathrm{Pole}-P+\mathrm{Arch}.
\end{aligned}
\]
PI003 established \(G_p=P_p\) on norm-only h with h(0)=0. PI004 establishes \(\mathrm{Arch}_{\Omega}=-G_\infty\) on vanishing-near-zero tests. Thus **all geometric terms in the two scalar formulas have compatible signs and coefficients on the restricted mixed domain**, *once the source Fourier symbol is bound correctly*. Their zero-side totals are NOT thereby equal: Masullo restricts the relative strip I and has unverified spectral trace and multiplicity hypotheses.

**Diagonal obstruction is real and now quantitative:** \(h_{t,t}(0)=\|t\|_2^2>0\), so \(\varphi|_{C_\mathbb Q^1}\ne0\). Masullo's theorem does not admit this diagonal test. The integral kernel K has \(K(u)\sim1/(2|u|)\) near zero, so the bare \(G_\infty\) integral diverges on a generic nonzero diagonal test. The standard Gamma Fourier term instead has a *renormalized/contact contribution*. For general smooth compact h, the standard digamma representation gives the convergent formula
\[
\operatorname{Arch}_{\Omega}(h)=
(-\gamma-\log\pi)\,h(0)
+\int_0^\infty
\frac{e^{-v}h(0)-\tfrac12e^{-v/4}[h(v/2)+h(-v/2)]}{1-e^{-v}}\,dv.
\tag{PI004-contact}
\]
One must not drop the \(h(0)\) terms or assert Masullo's unspecified primed-integral extension agrees with them. Any diagonal extension needs a precisely matched regularization and compensation, or a different admissible trace operator. This is a falsifiable interface limitation, not evidence that the signed Weil quadratic form is negative.

## 5. Exact source test and next stage

**PI004 independent exact Fraction preflight** is in \`scripts/pi004_realplace_gamma_kernel_preflight.py\`. It verifies at u=±log q for q=4,9,16 that:
- the +r and -r real-place contributions combine with the actual Masullo coefficient 1/2;
- the gamma-side geometric kernel \(q^{-1/2}/(1-q^{-2})\) agrees exactly;
- at q=9 the common rational weight is \(27/80\);
- the contact pole of K at u=0 cannot be ignored.
The script tests exact normalization identities, **not** the whole Fourier/digamma theorem, Masullo trace, or Lean imports.

**PI005 next gates:**
1. Identify and prove in the **literal original Lean source** the exact \`gammaBracket\` symbol \(\Omega\) and \`paperFT\` normalization; formulate a source-bound theorem on vanishing-near-zero mixed correlations. No bogus \`#print axioms\` receipt.
2. Certify explicit smooth source support/correlation regularity and gamma/pole equality if feasible; otherwise retain paper-level proof and list missing Mathlib lemmas.
3. Compare the author's **relative strip I**, full multiplicity \(N(c)\) and chapter 13 truncated \(N_{\mathrm{spec}}\) with the complete original zero divisor. A mismatch is to be recorded explicitly.
4. Only then attempt an Alpöge arithmetic-source interface or CP001's 3x3 compression mapping.

**Proven here:** exact classical real kernel, exact Fourier–digamma formula on the restricted test domain, and the contact obstruction. **Not proven:** equality of original Lean \`gammaBracket\` with the displayed standard symbol as a source-specific kernel theorem, Masullo's spectral theorem, global cross-projection equivalence, support positivity or RH.
