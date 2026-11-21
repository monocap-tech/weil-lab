# PI016 — Compile the unchanged upstream Zeta23 definition in the same Lean graph as the literal finite Weil kernel

**Lane:** PI### Potential Interface, stacked only on PI015 #832 → PI014 #830 → PI013 #828 → PI012 #824 → PI011 #823 → PI010 #821 → PI009 #820 → PI008 #818 → PI007 #816 and earlier PI stages. Canonical registry issue #792. **NF### Phase III numerical certification, IV### Phase IV Schwartz-support extension and CP### cross-projection source/compression work are unaffected.**

**Status:** actual, pinned original-source co-residency experiment and genuine imported-constant Lean theorem candidates committed. **No PI016 Lean source compilation, .olean, or axiom audit PASS has been observed.** All inspected dedicated PI009–PI013 Actions and generic PI014/PI015 Lean runs were still queued; absence of compiler feedback is not success. No Masullo operator trace, original IV011 archimedean source transport, full Weil positivity, RH or GRH is claimed.

## 1. Exact discovery and the previously missing compatibility experiment

PI015 proved a source-level fact: the upstream Zeta23 project pins Lean 4.33.0-rc2 / Mathlib 51e6992efd06126df61a496bebf8f49482a4e129 (Mathlib tag v4.33.0-rc2), while the local Weil-Lab PI branch uses Lean 4.34.0 / Mathlib tag v4.34.0 at 5ed2965256430c3649e86755f9576b54eca72435. They are different compiler/library revisions.

The correct next question is **not** whether one can load a Lean 4.33 \`.olean\` into Lean 4.34. One cannot treat different toolchains' compiled objects as interchangeable. Instead ask a falsifiable question:

> Does the **unaltered upstream source file** \`zeta23/Zeta23/Defs.lean\`, Git blob \`8024700cbfefb54d763b487afa84c03fef58a550\`, compile successfully **from source** in the very same Lean 4.34.0 / Mathlib v4.34.0 object graph as the literal \`WeilDefect.Arithmetic.PI007FiniteGammaKernel\` module?

The upstream file imports Mathlib modules and defines the genuine \`Zeta23.paperFT\`. The experiment is source-authentic because the actual Git source bytes, rather than a hand-retyped replacement or a new symbol named Zeta23.paperFT, are fed directly to the compiler.

Source of upstream bytes: \`anthropics/formal-math@16a5ce41304fcdaea4e0be7c132e1c361dc26da5\`, \`zeta23/Zeta23/Defs.lean\`, Git blob \`8024700cbfefb54d763b487afa84c03fef58a550\`. The original definition is
\[
\texttt{Zeta23.paperFT}\ f\ z
:=\int_{\mathbb R}f(u)\operatorname{Complex.exp}(i z u)\,du.
\]
No factor 2π appears on the forward transform, and the Fourier exponent is **positive**. This exact source is what PI016 must import.

## 2. Two-stage direct compiler test, with falsifiers at every stage

New **manual-only** workflow:
\`.github/workflows/pi016-co-resident-zeta23-source-lean.yml\`.

### Core stage: source compatibility independent of previous PI013–PI015 proof stack

1. Checkout real PI016 repository source, install pinned local Lean 4.34 and Mathlib v4.34.
2. Clone upstream original repo at the immutable source commit and verify \`git hash-object zeta23/Zeta23/Defs.lean\` equals the **exact** source blob \`8024700…\`.
3. Compile the **literal** \`PI007FiniteGammaKernel.lean\` into an actual local \`.olean\`.
4. Compile **the exact upstream original** \`pi016-upstream/zeta23/Zeta23/Defs.lean\`, not a copy modified for 4.34, with \`lake env lean -o .lake/build/lib/lean/Zeta23/Defs.olean\`, under Weil-Lab's Lean 4.34 environment. If upstream Mathlib names or APIs have changed, this fails and the compiler logs provide the concrete migration obligation.
5. Compile \`WeilDefect/Arithmetic/PI016ImportedPaperFTCore.lean\` in **the same** local Lean graph. This module imports both \`WeilDefect.Arithmetic.PI007FiniteGammaKernel\` and the genuine \`Zeta23.Defs\`, producing two exact source-typed unfold lemmas (not a substitute declaration):
\[
\boxed{
\texttt{Zeta23.paperFT}
 \left(\lambda u.\uparrow(\texttt{pi007FiniteGammaKernel}\ N\ u)\right)
 (r:\mathbb C)
 =
\int_{\mathbb R}
\uparrow K_N(u)\,
\operatorname{Complex.exp}(i r u)\,du.
}
\tag{PI016-core}
\]
A second version retains arbitrary complex frequency z.

These two lemmas are **definition unfolding** with \`rfl\`, rather than secretly assuming Fourier inversion or the trace theorem.

\`scripts/pi016_co_resident_source_lean_audit.py --stage core\` must verify: unchanged original source blob, pinned actual upstream Git commit and native toolchain declarations, resolved local Mathlib Git HEAD, real local \`Zeta23/Defs.olean\`, PI007 \`.olean\`, imported core \`.olean\`, and exactly two accepted standard-only \`#print axioms\` outputs.

**If the core fails because the original upstream source cannot compile under 4.34, the missing compatibility theorem/source port has been identified—not falsified the classical Fourier equality.** Never patch the original source silently.

### Full stage: after the actual original definition is in a common compiler graph

The subsequent \`lake build WeilDefect.Arithmetic.PI015FiniteGammaSymbolBridge\` forces the existing PI008–PI015 local stack to compile, then \`lake env lean\` compiles the new file \`PI016ImportedFiniteGamma.lean\`, which imports the **actual** PI016 source-typed core plus local PI015 finite symbol.

It states three named source-typed theorems:

1. \`pi016ImportedPaperFT_eq_localModel\`: genuine imported \`Zeta23.paperFT\` applied to the literal PI007 finite kernel equals PI014's finite local formula;
2. \`pi016ImportedPaperFT_finiteGammaSum\`: genuinely imported \`paperFT K_N\` equals \(\sum_{n<N}\texttt{pi008GammaRationalAtom}(n,r)\);
3. \`pi016FiniteGammaSymbol_eq_importedPaperFT\`: genuine imported paper Fourier data produce the exact PI008 finite symbol,
\[
\boxed{
\Omega_N(r)=H_N-\gamma-\log\pi
-\underbrace{\texttt{Zeta23.paperFT}(K_N)(r)}_{\text{original upstream symbol,
 literal PI007 kernel}}.
}
\tag{PI016-full}
\]

This is a **finite** formula only. It does **not** assert \(\mathcal A(h)\) inverse Fourier pairing, \(N\to\infty\) gamma passage, or Masullo operator trace.

The \`--stage full\` audit checks both PI016 modules' expected five theorem names and standard-only axioms, imported original \`Zeta23/Defs.olean\` SHA256, PI007–PI015 compiled object hashes and source blob provenance. If PI011 or PI013 fails, the core receipt remains an independently inspectable result, while the full stage stays OPEN.

**Important:** CI is manual-only because PI009–PI013 compiler jobs remain queued. GitHub workflow_dispatch can require default-branch presence; this file on a draft PR does not mean a run has been dispatched or is available to dispatch. All Lean source assertions remain **CANDIDATES** until an actual successful run's SHA-bound \`.olean\` and axiom receipt are recovered.

## 3. What success would prove — and what it would NOT

A **core PASS** would establish the exact upstream \`Zeta23.Defs\` source can compile unchanged under the local compiler and co-exist with the literal PI007 kernel, so there is an actual \`Zeta23.paperFT\` source constant in a common object graph. This resolves the *minimal* external Fourier source-admissibility gate. It does NOT prove any PI008 Gamma rational-atom equality.

A **full PASS** would additionally establish the finite exact dictionary (PI016-full), based on already-accepted local PI013–PI015 modules, for the source-authentic original \`paperFT\`. It still would not prove the full source \`Zeta23.EF.gammaBracket\` (which lives in \`ExplicitFormula.lean\`) is imported/compiled under 4.34, nor bind to literal \`neutralIV011OriginalMixedArch\` from the independent IV branch.

A **failure** at any stage gives a concrete elaborator/import error and SHA-bound compiler audit log. It is not valid to reinterpret such a failure as mathematical disagreement, or to claim that a textual expression proves the actual imported source.

## 4. Crucial future inverse Fourier/contact obligation

The source-complete **finite** Gamma identity would prepare
\[
\Omega_N(r)=H_N-\gamma-\log\pi-\mathcal F_+K_N(r).
\]
The harder, independent frequency pairing is, for compact smooth complex h,
\[
\boxed{
\frac1{2\pi}\int_\mathbb R
\operatorname{paperFT}(h)(r)\Omega_N(r)\,dr
=
(H_N-\gamma-\log\pi)\,h(0)
-\int_\mathbb R h(u)K_N(u)\,du.
}
\tag{PI016-still-open-in-Lean}
\]
A genuine Lean proof must justify integrability, Fubini, inverse Fourier sign and \(1/(2\pi)\), without accidentally erasing the harmonic contact term. On Masullo-admissible h with h(0)=0 it vanishes; on diagonal tests it must be retained.

The **original** archimedean symbol \(\Omega=\Re\psi(1/4+ir/2)-\log\pi\), original IV011 source identity, PI007 physical/PI008 frequency tails and source-bound limit remain separate formal obligations. Upstream \`Zeta23.ExplicitFormula\` and \`Zeta23.GammaFacts.Series\` were not imported in PI016; no kernel-certified digamma-to-original \`gammaBracket\` transfer is claimed.

Finally, Masullo's operator trace theorem excludes norm-pullback tests with h(0)≠0. Independently identifying the extended operator's contact normalization (or proving it cannot be extended) is indispensable. PI006's scalar-mass and local-potential ambiguity remains; a finite Fourier dictionary does **not** imply global Weil positivity, RH or GRH.

## 5. PI017 handoff

1. Recover real PI009–PI015 compiler conclusions and fix specific Lean errors where available. Their queued status is not a valid theorem.
2. Obtain an actual PI016 **core** source-compatibility compiler receipt; if original Zeta23.Defs fails under 4.34, record exact failed imports/lemmas and use an explicit audited source port only if mathematically and formally equivalent. Do not mutate the source in the core test.
3. Attempt PI016 **full** source-typed dictionary only after PI013–PI015 local imports compile, with strict object SHA and axiom audits.
4. Extend the same original-source test to \`Zeta23.ExplicitFormula\` and \`GammaFacts.Series\` with appropriate actual dependencies (not just external \`paperFT\`), then construct a separate IV-based PI companion for the full signed Weil Gamma integral and inverse pairing.
5. Independently test the Masullo trace operator/diagonal-contact hypothesis. No claim of RH, global positivity, complete Weil isometry or completed spectral trace realization is made.

**PI016 advance:** from two separate source/compiler screenshots to one concrete, source-authentic, falsifiable common-graph compilation experiment; no result is preemptively labeled accepted.
