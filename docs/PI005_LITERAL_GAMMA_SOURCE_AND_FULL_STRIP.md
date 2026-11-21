# PI005 — Literal Zeta23 Fourier/Gamma source binding and the full-width zeta zero-strip audit

**Lane:** PI### Potential Interface, stacked only on PI004 #804 → PI003 #801 → PI002 #798 → PI001 #793. Canonical registry: issue #792. Independent of NF### Phase III numerical and IV### Phase IV support-extension certification, and CP### finite-compression research.

**Status:** upstream source-exact syntactic dictionary identified, mathematical mixed-test matching consequences corrected, and Masullo theorem's precise spectral width/multiplicity reread. **NO PI Lean kernel PASS**, independently certified Masullo operator trace theorem, diagonal contact equality, operator isometry, RH or GRH.

## 1. Critical source discovery: exact names, no invented spectral multiplier

The authenticated upstream mathematical definitions are not just analogous to PI004's classical model. They are **the identical explicit expressions** under their intended source imports.

Upstream: Anthropic's public Zeta23 source, which the literal Weil-Lab IV011 expressions refer to by the names \`Zeta23.paperFT\` and \`Zeta23.EF.gammaBracket\`.

- **Zeta23/Defs.lean**, Git blob \`8024700cbfefb54d763b487afa84c03fef58a550\`, source:
  https://github.com/anthropics/formal-math/blob/main/zeta23/Zeta23/Defs.lean
  Definition:
  \[
  \operatorname{paperFT} h(z)=\int_{\mathbb R}h(u)\exp(izu)\,du.
  \]
  It uses **positive** angular-frequency exponent, whereas PI004's auxiliary nonunitary Fourier transform had negative exponent.
- **Zeta23/ExplicitFormula.lean**, Git blob \`11119489556113fd419d7b6fb45ccbaa2e493e2a\`, source:
  https://github.com/anthropics/formal-math/blob/main/zeta23/Zeta23/ExplicitFormula.lean
  Its \`EF.gammaBracket r\` is **definitionally**
  \[
  \Omega(r)=\bigl(\operatorname{digamma}(1/4+i r/2)\bigr)_{\Re}-\log\pi.
  \]
  The same source proves \`EF.paperFT_ofReal_eq_fourier\`:
  \(\operatorname{paperFT}(h)(r)=\mathcal F_{\mathrm{Mathlib}}h(-r/(2\pi))\).
  Its \`EF.literatureRHS\` is exactly \(\mathrm{Pole}-\mathrm{Prime}+\frac1{2\pi}\int\operatorname{paperFT}(h)\,\Omega\), with **both** pole evaluations at \(\pm i/2\).
- **Zeta23/WeilEF/GammaRBracket.lean**, Git blob \`48eba58762cccfc47ac06b7af5c386b68fdba20c\`, source:
  https://github.com/anthropics/formal-math/blob/main/zeta23/Zeta23/WeilEF/GammaRBracket.lean
  \`WeilEF.gammaR_bracket\` proves the exact \(\Gamma_\mathbb R\) log-derivative bracket equals \(\Omega(r)\), on the real line. This is an existing Lean source theorem, NOT a PI-specific real-place inversion theorem.
- **Actual original Weil-Lab IV011 source**, Git blob \`14d8f01ce34f764900eccc68399d7323b4f4a25c\`, PR #774:
  https://github.com/monocap-tech/weil-lab/blob/research/iv011-original-cross-support-prime-cutoff/WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean
  The definition \`neutralIV011OriginalMixedArch\` applies exactly \`paperFT\` and \`gammaBracket\` with \(1/(2\pi)\); \`neutralIV011OriginalMixedPole\` uses both \(\pm i/2\); and \`neutralIV011OriginalMixedPrime\` preserves all genuine \(\Lambda(n)/\sqrt n\) frequencies.

**Formal source custody caveat:** Git blob identity and text inspection support these exact definitions. Before asserting an in-repository Lean PASS, verify the same pinned upstream source bytes were the ones actually compiled into the Phase IV object chain and prove the needed real-place integral/distribution identity using that exact source. Neither condition follows from a text audit alone.

## 2. Fourier sign discrepancy in PI004 is harmless, but must be explicit

Let \(\widehat h_-(r)=\int h(u)e^{-iru}\,du\), the auxiliary PI004 convention, and \(\widehat h_+(r)=\operatorname{paperFT}(h)(r)=\int h(u)e^{iru}\,du\), the literal source.

Then \(\widehat h_+(r)=\widehat h_-(-r)\). Since
\[
\Omega(-r)=\Omega(r)
\]
from digamma conjugation at real \(r\), a reflection/change of variable shows
\[
\frac1{2\pi}\int\widehat h_+(r)\Omega(r)\,dr
=
\frac1{2\pi}\int\widehat h_-(r)\Omega(r)\,dr.
\]

For a complex (non-even) mixed h this is **still valid**, because the evenness belongs to \(\Omega\), not to h. The original PI004 calculation therefore transfers unchanged to the literal source symbol *at the mathematical level*.

On the compact \(C^\infty\) correlations \(h=h_{s,t}\) vanishing on a neighborhood of zero, PI004 gave:
\[
G_{\infty,\mathbb Q}(h\circ\log|\cdot|)
=\int_\mathbb R h(u)\frac{e^{-|u|/2}}{1-e^{-2|u|}}du,
\quad
\boxed{\operatorname{Arch}_{\mathrm{IV011}}(s,t)=-G_{\infty,\mathbb Q}(h)}.
\]
This is an exact classical identity once the source symbols above are used, not a guessed fit. The identity for general nonzero-diagonal h is **NOT** included: the bare real kernel singularity and the source Gamma contact term require a matched regularization.

The two source pole terms \(\operatorname{paperFT}(h)(\pm i/2)\) are exactly \(\int h(u)e^{\mp u/2}du\), and their **sum** agrees with the Masullo \(\pm1/2\) Mellin pole evaluations from PI002. Individual terms exchange labels relative to \(H_h(z)=\int h(u)e^{zu}du\); the sum is preserved.

Together with PI003's local prime identity, this establishes source-level *geometric component compatibility* of the two displayed expressions for genuinely disjoint-support mixed test pairs that vanish near zero, without asserting Masullo's full trace/operator theorem.

## 3. Essential correction: the a=1/2 trace theorem includes all nontrivial zeta zeros

Directly inspected Masullo manuscript:
https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf

- **Theorem 12.5.1.1**, printed pp.519–520 (PDF indices 518–519): preceding paragraph expressly selects the Hardy–Sobolev strip half-width \(a=1/2\). The zero side includes zeros \(c\) of relevant Hecke L-functions in **the interior** of the relative strip \(1/2+[-a,a]+i\mathbb R\), each with its actual multiplicity \(N(c)\).
- For \(F=\mathbb Q\) and the **trivial Hecke-character isotype only**, the nontrivial zeros \(\rho\) of Riemann zeta satisfy \(0<\Re\rho<1\) unconditionally, and hence
  \[
  |\Re(\rho-\tfrac12)|<\tfrac12.
  \]
  Consequently **NO nontrivial zeta zeros are omitted by this particular width choice**. The earlier PI001–PI004 blanket warning that the strip necessarily truncates the zeta divisor was TOO STRONG and is corrected here.
- This statement must NOT be extended to arbitrary smaller \(a\), boundary contributions under other Sobolev degrees, or the separate Chapter 13 \`N_{\mathrm{spec}}\` scheme without an explicit proof.
- Masullo's printed page 520 says \(N(c)\) is the **multiplicity** of zero \(c\); the complete original Weil-Lab divisor is multiplicity-preserving. Their multiplicities are *not inherently incompatible*. An actual enumeration/representation theorem and equality of spectral trace are still required; it is not enough to note that both write \(N(c)\).

The theorem remains a manuscript claim and has not been independently certified as a valid global operator trace theorem. This audit does **not** infer RH from its claimed equality.

## 4. Why no immediate whole-form positivity follows

Masullo's displayed theorem requires \(\varphi|_{C_F^1}=0\). For the norm-pullback \(\varphi(g)=h_{s,t}(\log|g|)\), this is equivalent to \(h_{s,t}(0)=\langle t,s\rangle_{L^2}=0\).

- The PI003 old-minus/old-plus test has disjoint supports, hence \(h(0)=0\), even though its \(+\log 9\) genuine prime coefficient is nonzero.
- For a nonzero diagonal test \(t=t\), \(h_{t,t}(0)=\|t\|_2^2>0\), so the theorem cannot be applied.
- Pairwise off-diagonal agreement on this restricted class does **not** identify diagonal entries nor positivity of a full Hermitian compression. A diagonal correction \(h\mapsto h-h(0)\eta\) changes the full scalar explicit formula by \(h(0)W(\eta)\) and must be paid explicitly. The primed-real-place extension requires source-specific subtraction/contact normalization.

## 5. Falsifiable PI005 conclusion and PI006 priority

On the explicitly frozen nonzero prime-active mixed pair, **the complete arithmetic/geometric side of the two source expressions has matching pole, prime, and real-place/Gamma distributions** (paper-level classical identities under the actual source definitions), for the \(\mathbb Q\) trivial character and the author's test-domain restriction. The nontrivial zero divisor also lies entirely in the stated \(a=1/2\) strip with full multiplicities.

This gives a **sharper conditional interface proposition**:
\[
\boxed{\mathrm{If\ Masullo's\ complete\ trace\ formula\ is\ valid\ on\ }\Phi_{s,t},
\ \mathrm{then\ its\ spectral\ side\ equals\ the\ original\ full\ signed\ Weil\ mixed\ value.}}
\]
This implication is conditional on the source regularity, characterization of the trivial-character sector, complete zero enumeration, and trace theorem validity; it is NOT a claim the latter has been proved.

**PI006 next:**
1. Source-specific Lean bridge between \`neutralIV011OriginalMixedArch\` and the ordinary real-place \(K(u)\) integral for compact mixed correlations vanishing near zero; supply proof with actual named sources and strict \`#print axioms\` receipt, or retain a clearly marked kernel-open lemma.
2. Verify an **actual** original Gamma source compile dependency SHA, not merely an upstream website blob.
3. Compare the complete multiplicity-preserving zero-side summand \(H_t(\rho-1/2)\overline{H_s(1/2-\bar\rho)}\) against the original IV007 divisor-coordinates indexing, including \(\mathbb Q\) trivial-character projection and convergence.
4. Attempt a compensated diagonal extension without asserting Masullo's theorem outside its domain. A proved obstruction or nonzero contact residual is a valid result, not a failed project.
5. Only after these, test the exact dictionary against CP001's normalized 3×3 compression and Alpöge's actual Lean arithmetic functional.

**Custody:** PI is a comparison laboratory. No new PI Lean kernel theorem, global Weil positivity, RH, or GRH is established.
