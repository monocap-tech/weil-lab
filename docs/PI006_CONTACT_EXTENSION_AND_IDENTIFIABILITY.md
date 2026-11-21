# PI006 — Contact normalization, off-diagonal non-identifiability, and the precise missing Lean transport gate

**PI### Potential Interface:** continuation of PI005 PR #809, PI004 #804, PI003 #801, PI002 #798, PI001 #793, registry #792. Independent of all NF### numerical custody, IV### support-extension certification, and CP### compression work. This stage does not modify any of those branches.

**Status:** exact classical distribution identities and algebraic identifiability/obstruction theorems, with a separate exact rational countermodel. **NO PI Lean compiler PASS, independently validated Masullo nuclear trace theorem, operator isometry, global Weil positivity, RH or GRH**.

## 1. Reopened source and fixed normalizations

Weil-Lab literal IV011 original signed source: https://github.com/monocap-tech/weil-lab/pull/774
- \`neutralIV011OriginalMixedArch(b,s,t)\` is the original \((2\pi)^{-1}\int \operatorname{paperFT}(h)(r)\operatorname{gammaBracket}(r)\,dr\).
- \`neutralIV011OriginalMixedPrime\` retains genuine coefficients \(\Lambda(n)/\sqrt n\).
- \`neutralIV011OriginalMixedPole\` retains both evaluations at \(\pm i/2\).

Upstream frozen definitions:
- \`Zeta23.paperFT h r = \int_\mathbb R h(u)e^{iru}\,du\` in https://github.com/anthropics/formal-math/blob/main/zeta23/Zeta23/Defs.lean (Git blob 8024700cbfefb54d763b487afa84c03fef58a550).
- \`Zeta23.EF.gammaBracket r = Re digamma(1/4+ir/2)-log(pi)\` in https://github.com/anthropics/formal-math/blob/main/zeta23/Zeta23/ExplicitFormula.lean (Git blob 11119489556113fd419d7b6fb45ccbaa2e493e2a).
- Existing upstream \`EF.paperFT_ofReal_eq_fourier\` and \`WeilEF.gammaR_bracket\` prove the Fourier convention and the gamma-factor digamma bracket, **not** the inverse Fourier transform against the adelic real-place distribution.

Masullo, *The Music of the Primes*, PDF pp.519–520 (indices 518–519), Theorem 12.5.1.1:
https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf
requires a smooth compact \(\varphi\in\mathcal D(C_F)\) with \(\varphi(C_F^1)=0\); the real geometric term at F=Q is an integral over \(\mathbb R^\times\) with factor \(1/2\) and Haar \(dg/|g|\). The theorem is a manuscript claim, not a separately certified operator proof. At its fixed a=1/2 the nontrivial zeta zeros lie within the selected strip with full multiplicity in the displayed statement.

## 2. Stronger restricted real-place lemma: h(0)=0 is sufficient

PI004 proved the real-place identity on \(C_c^\infty\) tests vanishing **near** zero. For Masullo's stated test restriction the natural condition is just \(h(0)=0\), which is enough for the *ordinary* local integral to be absolutely convergent, even if h is nonzero arbitrarily close to zero.

For \(h\in C_c^\infty(\mathbb R;\mathbb C)\), define
\[
K(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}}\quad(u\neq 0),\qquad
\Omega(r)=\Re\psi\!\left(\tfrac14+\tfrac{ir}{2}\right)-\log\pi.
\]
Near zero, \(K(u)=\frac1{2|u|}+O(1)\). If \(h(0)=0\), then \(|h(u)|\le M|u|\) near zero, so \(hK\in L^1\). The local trace-test requirement is now sufficient for absolute convergence; no arbitrary new principal value is needed.

A fixed \(\epsilon>0\) cutoff in the digamma integral and ordinary Fourier inversion, followed by \(\epsilon\downarrow0\), gives
\[
\boxed{ \mathcal A(h):=\frac1{2\pi}\int_\mathbb R
\operatorname{paperFT}(h)(r)\Omega(r)\,dr
=-\int_{\mathbb R}h(u)K(u)\,du,\quad h(0)=0. }\tag{PI006-R}
\]
This is valid for complex, non-even h. In the intermediary symmetric expression \(h(u)+h(-u)\), the first derivatives cancel, so for a smooth h with h(0)=0 the numerator is \(O(u^2)\); dominated convergence is available. The paper Fourier exponent is positive, but \(\Omega\) is even and the whole-r integral is orientation-invariant.

Thus PI004's classical real-place/Gamma dictionary extends to *all* smooth compact norm-pullback tests obeying Masullo's actual vanishing condition, not merely the physically separated examples. This is a stronger analytical interface, **not** a Lean theorem yet.

## 3. Explicit compensated diagonal extension from the ORIGINAL Gamma source

For a general compact smooth h, the bare \(\int hK\) need not exist because \(h(0)\ne0\). Choose any \(\eta\in C_c^\infty(\mathbb R;\mathbb C)\) with \(\eta(0)=1\); take eta real/even if a Hermitian normalization is desired. Define
\[
h_0:=h(0),\quad g_\eta=h-h_0\eta,\quad
R_\eta(h):=\int_{\mathbb R}g_\eta(u)K(u)\,du.
\]
Because \(g_\eta(0)=0\), the last integral is absolutely convergent even when \(h_0\ne0\).

**Exact source-selected extension identity:**
\[
\boxed{\mathcal A(h)=h_0\,\mathcal A(\eta)-R_\eta(h).}\tag{PI006-C}
\]
This is simply linearity of the literal original Gamma distribution plus (PI006-R) on \(g_\eta\). It does **not** use or presume Masullo's claimed trace theorem.

Therefore define a candidate *extended geometric distribution selected by the Weil source*:
\[
\widetilde G^{\rm Weil}_\infty(h)
:=R_\eta(h)-h_0\mathcal A(\eta)
=-\mathcal A(h).
\]
It **does not depend on eta**: for eta/xi with eta(0)=xi(0)=1, \(\mathcal A(\eta-\xi)=-\int(\eta-\xi)K\), since their difference vanishes at zero. This proves exact cancellation of the auxiliary selector.

On the Masullo-permitted domain \(h(0)=0\), \(\widetilde G^{\rm Weil}_\infty(h)=\int hK=G_\infty(h)\). For nonzero diagonal h, this is a mathematically well-defined *particular extension of the geometric functional* using Weil-Lab's own Gamma source; **it is not an independently constructed extension of Masullo's nuclear trace operator**. A genuine operator/trace equivalence must prove its new contact normalization is the same. Merely defining it to match the Weil form would be circular.

If \(\eta\) is fixed, the entire unobserved normalization is the single complex scalar \(\mathcal A(\eta)\) at the level of this translation-invariant scalar Gamma distribution. It does not yet resolve the **full** Weil quadratic form, the prime side, or trace-domain topology.

## 4. Inverse-problem obstruction: off-diagonal observations do not determine diagonals

### 4a. The larger orthogonal-pair observation class

Let H be a complex inner-product space and \(B_1,B_2\) Hermitian sesquilinear forms on H. If
\[
B_1(s,t)=B_2(s,t)\quad\text{for **every** pair with }\langle t,s\rangle_H=0,
\]
then their difference is \(c\langle t,s\rangle_H\) for a **single real scalar** c, provided the forms are defined everywhere on H. Proof: put D=B1−B2. For each nonzero s, decompose t into its component along s and an orthogonal remainder. D(s,t)=a(s)\langle t,s\rangle. Hermitian symmetry implies a(s)=a(t) whenever \(\langle t,s\rangle\ne0\); for orthogonal nonzero s,t, use s+t to connect them. Therefore a is constant and real. No boundedness assumption is needed for this algebraic statement.

Hence even a *complete* Masullo extension to **all** h(s,t) with h(0)=0 would determine the Hermitian pairing only modulo \(c\langle\cdot,\cdot\rangle\) unless an independent contact/mass normalization fixes c.

### 4b. The narrower physically disjoint test class actually used in PI001–PI005

The current frozen source bump pairs satisfy the stronger condition \(\operatorname{supp}s\cap\operatorname{supp}t=\emptyset\). On only **these** pairs the ambiguity is much larger: for any real bounded local potential V define
\[
D_V(s,t):=\int_{\mathbb R}V(x)t(x)\overline{s(x)}\,dx.
\]
For physically disjoint support, \(D_V(s,t)=0\) for every V, whereas \(D_V(t,t)=\int V|t|^2\) can be positive or negative. Thus infinitely many diagonal completions are consistent with every such off-support comparison. One cannot infer an optimal Rayleigh margin or Hermitian inertia from the observed pairs alone.

**A sharp stop condition:** any claim that agreement only on these off-support mixed tests implies full positive-form isometry is false without a locality/contact-control hypothesis. This is a rigorous information-loss obstruction, not a counterexample to the *actual* Weil positivity conjecture.

### 4c. Exact finite-dimensional counterexample

On the two-cell real space with standard mass \(G=I_2\), compare \(B_0=\mathrm{diag}(1,1)\), \(B_{\rm scalar}=\mathrm{diag}(-2,-2)\), and \(B_{\rm local}=\mathrm{diag}(-2,1)\). On the disjoint-cell ordered basis pair \((e_1,e_2)\), all cross entries are zero, but their signs/inertias differ. On **every orthogonal pair** the first two still agree, because their difference is a scalar multiple of G; the third differs on orthogonal superpositions. This distinguishes the two levels of ambiguity exactly.

\`scripts/pi006_contact_ambiguity_preflight.py\` verifies these identities by exact Fractions. This is a countermodel to an *invalid inference from partial mixed data*, not a model of the authentic signed Weil form.

## 5. The actual Lean-source boundary

There is no hidden \`#print axioms\` certificate for PI006. The original IV011 module is **not present on PI's independent main-based branch**; it is only on the separate stacked IV### source branch. Therefore a source-bound Lean proof for \`neutralIV011OriginalMixedArch\` must be built as an independently named **PI companion based on the relevant IV branch**, not by importing unavailable IV011 theorem names from the PI-only branch and pretending it compiles.

A meaningful future source-bound theorem requires:
1. The exact imported \`Zeta23.paperFT\`, \`Zeta23.EF.gammaBracket\` and original \`neutralIV011OriginalMixedArch\`, with pinned compiled source SHAs.
2. A Lean definition of the real \(K\) distribution under integrability \(h(0)=0\), and a proof of the complex Fourier/digamma inverse-transform identity (PI006-R). Upstream \`gammaR_bracket\` alone does **not** prove this.
3. The compensated exact source identity (PI006-C), with integrable subtracted kernel, including an explicit cutoff/selector.
4. Standard-axiom \`#print axioms\`, actual object compilation, and independent workflow audit before any \`LEAN PASS\` designation.
5. The \(\mathbb Q\) norm-pullback map and Masullo test-domain inclusion are still classical analytic deductions, not Mathlib-modeled operator-trace definitions.

The repo's numerical/Lean CI queue is currently under backpressure (independent NF755 and IV024 custody work); PI should not assert kernel acceptance from an unchecked candidate.

## 6. PI007 immediate falsifiable next test

PI007 should attempt the **source-bound Lean companion** proving PI006-R and PI006-C if analytic/Mathlib primitives permit, then separately test whether any independently defined Masullo principal-value/operator extension has the **same** contact normalization as \(\widetilde G^{\rm Weil}_\infty\). If the required definition is absent, explicitly classify the interface as a restricted-test identity plus an unidentifiable diagonal contact, not an operator equivalence.

A later PI### stage must separately extract Alpöge's weighted von Mangoldt test functional and match it to the PI003 \(n=9\) source term; matching an algebraic coefficient alone is not the claimed theta-lift bridge.

**Conclusion:** PI's arithmetic and archimedean dictionary is source-consistent on admissible mixed tests, and now has an exact mathematical extension construction for the Gamma **distribution**. Whether the Masullo **operator trace** supplies this same extension remains the indispensable missing hypothesis.
