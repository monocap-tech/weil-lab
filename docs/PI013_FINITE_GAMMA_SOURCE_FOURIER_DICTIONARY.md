# PI013 — Literal PI008 atom and finite positive-Fourier Gamma sum

**Lane:** independent PI### Potential Interface, stacked on PI012 #824 → PI011 #823 → PI010 #821 → PI009 #820 → PI008 #818 → PI007 #816 and prior PI branches. Registry #792. NF### Phase III, IV### Phase IV and CP### cross-projection work remain untouched.

**Status:** exact classical finite Fourier dictionary and source audit; independent Fraction preflight PASS; two PI013 Lean proof-candidate modules with direct compiler workflow. **No PI013 .olean/axiom PASS has been verified.** Masullo operator trace, diagonal contact normalization, original IV011 Gamma transport, global Weil positivity, RH and GRH remain OPEN.

## 1. Actual source definitions

- PI007 physical kernel, file WeilDefect/Arithmetic/PI007FiniteGammaKernel.lean: pi007FiniteGammaKernel N u = sum over n<N of exp(-(2n+1/2)|u|).
- PI008 finite rational atom, file WeilDefect/Arithmetic/PI008FiniteDigammaSymbol.lean: pi008GammaRationalAtom n r = a_n/(a_n²+(r/2)²), where a_n = n+1/4.
- PI011 whole-line integrand, file WeilDefect/Arithmetic/PI011WholeLineFourierAtom.lean: pi011PhysicalFourierAtom α r u = exp(-α|u|+iru).
- PI012 Fourier integral source candidate, file WeilDefect/Arithmetic/PI012SourceFourierAtom.lean: pi012WholeLineFourierClosed α r evaluates the integral of the PI011 function at 2α/(α²+r²), α>0.
- True upstream Zeta23 paperFT f z = integral f(u)*exp(i*z*u)du in anthropics/formal-math/zeta23/Zeta23/Defs.lean, blob 8024700cbfefb54d763b487afa84c03fef58a550. It uses the **positive** Fourier exponent. It is NOT directly imported on the standalone PI branch.
- Pinned Mathlib v4.34.0, Mathlib/MeasureTheory/Integral/Bochner/Basic.lean, theorem **integral_finsetSum**: exact integral of a finite family of integrable summands equals the sum of their integrals. The actual theorem text was inspected.

All direct PI009–PI012 compiler runs checked at PI013 inception were QUEUED; no prior PI kernel acceptance receipt has been recovered.

## 2. Exact one-atom real/complex dictionary

Put a_n = n+1/4 and α_n=2a_n=2n+1/2>0. For every real angular frequency r,

\[
\boxed{\int_{\mathbb R}e^{-\alpha_n|u|+iru}\,du
=\frac{2\alpha_n}{\alpha_n^2+r^2}
=\frac{a_n}{a_n^2+(r/2)^2}
=\operatorname{pi008GammaRationalAtom}(n,r).}
\tag{PI013-atom}
\]

The **left** integral is complex-valued, with a real value represented in ℂ. This type is not silently identified with a real integral. Source-oriented normalization is unchanged; there is no factor 2π on the forward transform.

New uncompiled candidate WeilDefect/Arithmetic/PI013GammaAtomCast.lean has five named Lean proofs:
1. π013 positive damping and the exact PI007 exponent;
2. the real rational equality with literal PI008;
3. complex-of-real cast of that equality;
4. the actual PI012 **whole-line Fourier integral** equals the literal PI008 rational atom (coerced to ℂ).
All five have #print axioms declarations. Any Lean field-simp or coercion failure must be repaired from actual compiler logs, not ignored.

## 3. Finite source Gamma transform

Define the original physical finite kernel and source-positive transform,

\[
K_N(u)=\sum_{n=0}^{N-1}e^{-\alpha_n|u|},\qquad
\mathcal F_+f(r)=\int_{\mathbb R}f(u)e^{iru}\,du.
\]

Each summand is absolutely integrable because α_n>0. Hence **finite** Bochner linearity gives

\[
\boxed{\mathcal F_+K_N(r)=
\int_{\mathbb R}\sum_{n<N}e^{-\alpha_n|u|+iru}\,du
=\sum_{n<N}\frac{a_n}{a_n^2+(r/2)^2}.}
\tag{PI013-finite}
\]

This preserves the genuine finite digamma symbol:

\[
\boxed{\Omega_N(r)=H_N-\gamma-\log\pi-\mathcal F_+K_N(r)},
\quad H_N=\sum_{k=1}^{N}k^{-1}.
\tag{PI013-symbol}
\]

The source prime/Gamma sign and no-2π forward normalization are exact. Inverse Fourier normalization (1/(2π)), all limiting arguments, and the original IV011 source attachment are **separate** proof obligations.

New candidate WeilDefect/Arithmetic/PI013FiniteFourierSum.lean defines pi013FiniteDampedFourier as a finite sum of the **literal PI011 physical complex exponentials**. It states three named Lean targets: whole-line integrability of a source atom from the PI011 half-line results; the empty Fourier sum; and a finite integral equality using Mathlib integral_finsetSum to produce the sum of literal PI008 rational atoms. This is a finite theorem with actual test integrands, not a postulated equality of arbitrary divergent integrals.

**Exact formal gap:** PI013 does NOT yet prove inside Lean that its finite complex sum equals (pi007FiniteGammaKernel N u : ℂ)*exp(i*r*u) pointwise, nor directly import the external Zeta23 paperFT definition. It must not claim accepted Zeta23-to-PI finite transform custody until a separate source-bound lemma is compiled. The classical equality (PI013-finite) is correct independent mathematics, but not a certified Lean theorem yet.

## 4. Independent exact Fraction checks

Script scripts/pi013_finite_gamma_atom_preflight.py:
- 1,792 exact PI012-versus-PI008 atom rational identities (n=0..255, seven rational frequencies);
- 56 exact finite sums at eight finite lengths and seven signed frequencies;
- 50 exact physical kernel K_N(log9) checkpoints:
  K_N(log9)=(27/80)(1-9^(-2N)).
Equivalent checks were independently executed and PASS. They do **not** evaluate integrals or compile Lean.

## 5. Direct compiler and axiom acceptance

Workflow .github/workflows/pi013-finite-gamma-fourier-lean.yml builds both actual PI013 modules, plus the transitive PI007, PI008, PI010, PI011, PI012 core/source objects. It requires nonempty compiled .olean files, directly compiles each PI013 source to collect #print axioms logs, and executes the fail-closed scripts/pi013_strict_finite_fourier_lean_audit.py verifier.

The verifier demands exactly **eight** PI013 named standard-axiom receipts and only propext, Classical.choice, Quot.sound, preserving source Git blob hashes, compiled object SHA256, checked-out commit, full build logs, and failure artifacts. A queued workflow is not proof. A completed PASS would certify just these eight finite declarations, not PI008 infinite digamma inversion, IV011 Gamma transport or Masullo's operator extension.

## 6. PI014 handoff and falsification criteria

1. Recover actual PI009–PI013 CI status, repair authentic errors including type coercions and finite integral sum elaboration, and secure correct standard-only axiom receipts.
2. Prove in Lean the **literal PI007 physical kernel times the Zeta23 positive Fourier character** equals the PI013 finite complex sum, using real-complex exp compatibility; then attach the true external Zeta23 paperFT in a separate source-based companion.
3. From (PI013-symbol), prove the finite archimedean pairing for compact smooth h, with exact Fourier inversion 1/(2π) and the harmonic contact term (H_N−γ−logπ)h(0).
4. Transport PI007 physical and PI008 frequency tails through genuine Lean limits; attach only then to the original neutralIV011OriginalMixedArch on a separately IV-based PI companion, without disrupting IV proof certification.
5. Independently test Masullo's operator trace diagonal-contact normalization. PI006 proved mixed/off-diagonal tests cannot determine the absolute Hermitian positivity margin; don't assume spectral operator equivalence.

A mismatch in the original sign, π-normalization, contact compensation, trace domain or zero multiplicities is a falsifier for the corresponding compatibility claim. PI013 establishes neither global RH/GRH nor full Weil positivity.
