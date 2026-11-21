# PI017 — Runnable source-exact core Lean sentry and the two-inversion finite-contact interface

**Independent PI### Potential Interface lane**. Stacked on PI016 #833 → PI015 #832 → PI014 #830 → PI013 #828 → PI012 #824 → PI011 #823 → PI010 #821 → PI009 #820 → PI008 #818 → PI007 #816 and the prior PI chain. Canonical PI registry: issue #792. **No NF### numerical certification, IV### arithmetic extension, or CP### source/compression branch was edited.**

**Status:** actual source-path audit **9/9 Mathlib imports found** in the pinned local Mathlib v4.34.0; a narrowly scoped *PR-triggered* direct compiler sentry is committed; a new source-typed two-Fourier-inversion finite-contact Lean **proof candidate** is committed, with 1,500 exact rational/formal-coefficient cases independently checked. **No PI017 Lean .olean, compiler success, or axiom acceptance has been observed.** The original upstream import may still fail at a renamed theorem, type, instance, or API; import-path presence alone does not prove compatibility. No Masullo operator-trace extension, full Weil positivity, RH or GRH.

## 1. Concrete verification finding: the source-compatibility CI was dormant

PI016 PR #833 contains \`.github/workflows/pi016-co-resident-zeta23-source-lean.yml\` with only \`workflow_dispatch\`. The workflow has **not executed** as a genuine source-compatibility job. Its generic queued Lean job builds the historical repository target, not the PI016 source. Draft-PR-only \`workflow_dispatch\` is not a sufficient route to source compiler custody, especially if GitHub requires the workflow file to be present on the default branch before dispatch.

At PI017 inspection, actual dedicated PI009–PI013 Actions remained queued; generic PI014–PI016 Lean jobs also remained queued. **None has an accepted source- or .olean-bound Lean PASS receipt**. Repeating a generic queued job does not change this.

PI017 corrects the *runability* obstacle: \`.github/workflows/pi017-core-source-compatibility.yml\` has a \`pull_request\` trigger on the actual sentry/workflow source changes. It is a **single narrow job**, not PI016's whole dependency-heavy proof chain. It can be scheduled by PR CI without requiring a manual-only dispatch. Its job being queued is still **not** Lean acceptance.

## 2. Independent exact source-path audit

Reopened the **actual pinned** upstream \`anthropics/formal-math\` source, \`zeta23/Zeta23/Defs.lean\` Git blob \`8024700cbfefb54d763b487afa84c03fef58a550\`, with root repository commit \`16a5ce41304fcdaea4e0be7c132e1c361dc26da5\`.

The unchanged upstream source has nine **direct** Mathlib module imports. Each one exists as a \`.lean\` file under Mathlib tag \`v4.34.0\`, local resolved commit \`5ed2965256430c3649e86755f9576b54eca72435\`:

1. \`Mathlib.Analysis.CStarAlgebra.Classes\`
2. \`Mathlib.Analysis.SpecialFunctions.Gamma.Digamma\`
3. \`Mathlib.Analysis.SpecialFunctions.Pow.Complex\`
4. \`Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt\`
5. \`Mathlib.MeasureTheory.Integral.Bochner.Basic\`
6. \`Mathlib.MeasureTheory.Measure.Lebesgue.Basic\`
7. \`Mathlib.Algebra.BigOperators.Finprod\`
8. \`Mathlib.Data.Set.Card\`
9. \`Mathlib.Data.Matrix.Basic\`

**Result:** 9/9 existing module paths under the exact chosen Mathlib tag. This rules out the simplest immediate *missing direct imported file* failure. It does **not** certify elaboration, theorem availability, transitive source compatibility, a successful local Lean compiler, or a reusable v4.33 \`.olean\`. Nor does it show the full upstream \`Zeta23.ExplicitFormula\` or \`GammaFacts.Series\` can compile at v4.34.

New deterministic \`scripts/pi017_source_import_preflight.py\` takes actual source checkouts and **fails closed** on wrong root commit, wrong source Git blob, wrong resolved local Mathlib SHA, changed literal positive-exponent \`Zeta23.paperFT\` definition, changed set of nine imports, or a missing direct imported Mathlib source path. The script's source-path logic corresponds to the source-level 9/9 audit. Its execution inside CI requires an actual queued runner and is not misrepresented as a run already completed.

## 3. PI017 real PR-triggered narrow compiler custody

The new \`pull_request\` workflow \`.github/workflows/pi017-core-source-compatibility.yml\` does the following sequentially:

- clone the **authentic original** upstream repo at \`16a5ce41304fcdaea4e0be7c132e1c361dc26da5\`, verifying \`Zeta23/Defs.lean\` Git blob \`8024700...\`;
- install the actual local Lean v4.34.0 and resolved Mathlib Git SHA \`5ed2965...\`, then run the nine-import static source gate;
- build the **literal local \`PI007FiniteGammaKernel\`** into its actual nonempty \`.olean\`;
- feed the **unaltered original upstream** \`pi016-upstream/zeta23/Zeta23/Defs.lean\` to local \`lake env lean\`, explicitly emitting \`Zeta23/Defs.olean\` in the **same** Lean v4.34 environment;
- compile \`PI016ImportedPaperFTCore.lean\` importing both original \`Zeta23.Defs\` and literal \`PI007FiniteGammaKernel\`, and require its actual nonempty \`.olean\`;
- invoke PI016's existing source/CI auditor with \`--stage core\`, demanding exactly **two** \`#print axioms\` records and only \`propext\`, \`Classical.choice\`, \`Quot.sound\`, checking real source Git blob, actual compiled object hashes and the exact checked-out source revisions;
- upload compiler logs and objects even if source compilation or axiom checks fail.

The workflow does **not** build PI008–PI016 full stack, invoke any unproven Gamma formula, import original IV011, or run numerical NF/IV/CP workflows. This is deliberately narrow to obtain an actionable source-compatibility compiler result rather than another large undiagnosable queued job.

A **PASS** would certify **only** that the byte-exact upstream \`Zeta23.Defs\` source successfully co-compiles under local Lean v4.34 with actual PI007, and that the two definition-unfold lemmas were accepted under standard axioms. It would not certify a finite atom sum or finite/infinite Gamma transform.

A **FAIL** would identify a concrete Lean/API compatibility problem. It would not invalidate the underlying classical Fourier formula.

## 4. New minimal finite Gamma contact theorem, with exactly two unpaid analytic premises

PI016's full source-typed finite formula, **if independently accepted**, is
\[
\boxed{
\Omega_N(r)
= c_N-\mathcal F_+K_N(r),\qquad
c_N=H_N-\gamma-\log\pi.
}
\tag{PI017-symbol}
\]
No constant is dropped or moved into the prime term.

For a complex test \(h\) with sufficient integrability, define a **finite** source Gamma spectral pairing
\[
A_N(h)=\frac1{2\pi}\int_\mathbb R
\operatorname{Zeta23.paperFT}(h)(r)\Omega_N(r)\,dr.
\]

The truly missing inversion obligations can be cleanly separated:

**(I) Fourier inversion at the origin**
\[
\frac1{2\pi}\int_\mathbb R
\operatorname{Zeta23.paperFT}(h)(r)\,dr=h(0).
\tag{PI017-I}
\]

**(II) Fourier pairing of the even finite kernel**
\[
\frac1{2\pi}\int_\mathbb R
\operatorname{Zeta23.paperFT}(h)(r)\,
\operatorname{Zeta23.paperFT}(K_N)(r)\,dr
=\int_\mathbb R h(u)K_N(u)\,du.
\tag{PI017-II}
\]

The **evenness of K_N** is essential: with the paper's positive Fourier sign, the general pairing gives K_N(-u), and equality with K_N(u) depends on symmetry. Actual integrability and complex Bochner integral interchange must be proved; unproved assumptions cannot be silently inferred from the symbolic identity.

Using the existing finite multiplier, linearity gives the precise conditional conclusion:
\[
\boxed{
A_N(h)=\underbrace{(H_N-\gamma-\log\pi)h(0)}_{\text{contact}}
-\int_\mathbb R h(u)K_N(u)\,du.
}
\tag{PI017-contact}
\]

New \`WeilDefect/Arithmetic/PI017FiniteContactObligations.lean\` gives a **source-typed no-sorry Lean proof candidate for this implication**, importing the genuinely named \`Zeta23.paperFT\` from PI016 and literal PI007/PI008/PI015 finite data. It states the two specific inverse Fourier identities and the required source-frequency integrability as hypotheses. It does **NOT** postulate the entire final pairing as an assumption, and it does **NOT** claim the two hypotheses already hold. Its compiler acceptance is **OPEN**, separate from the minimal PI017 core CI.

This distinction is mathematical, not merely bureaucratic: even if all PI007–PI016 source candidates pass, full Gamma transport still needs the two analytic Fourier inversion theorems, proper \(1/(2\pi)\), the original \`Zeta23.EF.gammaBracket\` source and limit. And Masullo's independent diagonal operator trace extension is an additional hypothesis.

## 5. Exact conditional-contact arithmetic check

New \`scripts/pi017_contact_two_inversions_preflight.py\` verifies **1,500** exact \`Fraction\` contact algebra cases for N=0..24, five signed rational frequencies, four h(0) values and three independent physical-pairing values. Euler's constant and log π are retained in separate formal basis coordinates; at N=0 the symbol still has \(-\gamma-\log\pi\), and for any h(0)≠0 both constants remain in the contact coefficient.

Equivalent independent rational calculation was executed **PASS**. This checks **only symbolic algebra assuming the two inversion identities**, not the identities themselves, the authenticity of an upstream trace, a Lean compiler run or original IV011.

## 6. PI018 handoff and strict status

**PI018 should recover actual PI017 PR-triggered core job logs and match its Git SHA to the precise source.** If the imported original Zeta23 source fails under v4.34, record the first compiler error and correct via an explicit equivalence-audited port. If it succeeds, attempt the **full** PI016 imported finite Gamma dictionary with the true PI013–PI015 compilation stack and strict axiom audit.

In parallel, formalize **(I)** and **(II)** above for actual compact smooth tests using the pinned Fourier inversion/Bochner integral library. Do not treat a conditional Lean implication as payment of its hypotheses. Only after that should a separately **IV-based PI companion** bind to original \`neutralIV011OriginalMixedArch\`, preserving original sign, \(1/(2\pi)\), \(\varphi(C_\mathbb Q^1)=0\) test-domain restriction and source SHA. The physical/Archimedean tails must also have true Lean limit receipts.

**Independent spectral stop line:** Masullo's operator diagonal contact normalization remains unproved; PI006 showed orthogonal/off-support mixed data do not identify the diagonal form. None of the above produces whole Weil positivity or RH/GRH.
