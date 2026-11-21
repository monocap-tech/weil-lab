# PI012 — Exact complex rational Fourier closure and source-bound Lean gates

**Lane:** PI### Potential Interface, stacked on PI011 PR #823, PI010 #821, PI009 #820, PI008 #818 and prior PI branches. Independently tracked by issue #792. NF, IV and CP workstreams are unchanged.

**Stage status:** exact classical algebra and independent rational verification PASS. Two real Lean source files are committed as **uncompiled candidates**. No PI012 accepted .olean or axiom audit; no IV011 source import, Masullo operator-trace equivalence, Weil positivity, RH or GRH.

## 1. Exact source and compiler custody

Literal PI010 source: WeilDefect/Arithmetic/PI010FourierHalflineAtom.lean, defining pi010PositiveExponent, pi010NegativeExponent and genuine pinned-Mathlib half-line integral theorem candidates.

Literal PI011 source: WeilDefect/Arithmetic/PI011WholeLineFourierAtom.lean, defining pi011PhysicalFourierAtom and the PI011 whole-line candidate
\[
\int_{\mathbb R}\exp(-\alpha|u|+iru)\,du
=-\frac1{-\alpha+ir}+\frac1{\alpha+ir},\quad\alpha>0.
\]

All dedicated compiler runs PI009 #44858094682, PI010 #44858575862 and PI011 #44859118766 were **queued** on inspection. This source stack is not kernel certified merely because all proof candidates contain no sorry.

Source positive Fourier convention: Zeta23.paperFT(f)(z) = integral f(u)*exp(i*z*u)du in upstream Zeta23/Defs.lean, Git blob 8024700cbfefb54d763b487afa84c03fef58a550. PI012 uses +iru throughout and keeps the inverse 1/(2*pi) normalization as a separate future theorem.

## 2. Exact rational closure, including poles

For real \(\alpha>0\) and r, put z_minus = alpha - i*r, z_plus = alpha + i*r. Their real parts equal alpha, so both are nonzero. The real denominator \(D=\alpha^2+r^2>0\).

Then, with actual complex field algebra,
\[
-\frac1{-\alpha+ir}+\frac1{\alpha+ir}
=\frac1{\alpha-ir}+\frac1{\alpha+ir}
=\boxed{\frac{2\alpha}{\alpha^2+r^2}}.
\tag{PI012-closed}
\]

New **uncompiled Lean candidate** WeilDefect/Arithmetic/PI012ComplexRationalIdentity.lean, imported from Mathlib only, contains six isolated named targets: denominator positivity, two complex conjugate denominator nonvanishing lemmas, generic reciprocal addition, imaginary-unit-square identity and pi012FourierReciprocalClosed.

Separate **uncompiled Lean candidate** WeilDefect/Arithmetic/PI012SourceFourierAtom.lean imports the PI012 core and PI011, with pi012SourceFractionsClosed and pi012WholeLineFourierClosed: the latter composes PI011's actual integral target with the source-positive rational closure. Nothing equating the whole IV011 Gamma integral to a trace is asserted in this file.

## 3. Exact link to PI008's genuine finite digamma atom

At \(\alpha_n=2n+1/2=2(n+1/4)\),
\[
\boxed{
\frac{2\alpha_n}{\alpha_n^2+r^2}
=
\frac{n+1/4}{(n+1/4)^2+(r/2)^2}.
}
\tag{PI012-atom}
\]
The right side is exactly pi008GammaRationalAtom n r, defined in the literal PI008FiniteDigammaSymbol.lean source. This is a mathematical equality; a **new Lean proof importing PI008 and reconciling real/complex types** remains for PI013 and cannot be claimed as PI012 kernel accepted.

For finite \(N\), absolute integrability and finite integral linearity imply
\[
\int_{\mathbb R}\left(\sum_{n<N}e^{-(2n+1/2)|u|}\right)e^{iru}\,du
=\sum_{n<N}\frac{n+1/4}{(n+1/4)^2+(r/2)^2}.
\]
This is PI013's finite Fourier-transform formalization target. It does not require RH, nor does it confer the entire PI007–PI008 Gamma frequency-limit Lean proof for free.

## 4. Independent exact arithmetic preflight

Script scripts/pi012_complex_fourier_atom_preflight.py checks 286 exact rational (alpha,r) pairs, including positive-alpha denominator guards, the correct two complex reciprocal real/imaginary parts, vanishing imaginary sum, even frequency orientation, the exact PI008 atom under alpha=2n+1/2 and 24 more finite partial-sum checks. Equivalent independent fractions.Fraction calculations were executed and PASSED. These verify algebra, not actual integrability/Lean.

## 5. Dedicated audit (new PI012 proof candidates only)

Workflow .github/workflows/pi012-rational-fourier-lean.yml must build the **actual** PI012ComplexRationalIdentity and PI012SourceFourierAtom modules, which also forces PI010/PI011 transitive imports, require nonempty actual .olean objects and direct lake env lean axiom logs, and execute scripts/pi012_strict_rational_fourier_audit.py. The audit accepts exactly the named six core + two source theorems and only standard Lean axioms propext, Classical.choice and Quot.sound; evidence includes source Git blobs, checked-out SHA, object SHA256 and compiler logs. Workflows that are queued or have no verified log/receipt do not count.

## 6. PI013 handoff

Recover real PI009–PI012 compiler outcomes, repair authentic elaboration/tactic failures, prove PI012-atom against PI008 in Lean, and prove the **finite sum** Fourier identity with explicit real-complex and \(2\pi\) normalization. The limiting Gamma transform still needs direct source-bound Lean proof, and an **IV-based PI companion** is required for original neutralIV011OriginalMixedArch. The independent Masullo operator's diagonal contact normalization remains unverified (PI006 information-loss obstruction). Nothing in PI012 establishes global Weil positivity, RH or GRH.
