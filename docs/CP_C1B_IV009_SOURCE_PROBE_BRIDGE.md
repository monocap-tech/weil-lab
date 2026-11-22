# Weil-Lab — CP-C1(B): source-identified original Weil nine-probe gate

**Cross-projection next step | 2026-11-22 | Lean candidates; NOT NEW LEAN PASS.** This is a SOURCE-CO-RESIDENT companion branch based on the **kernel-passed IV009 head** `3033a762c936019e662503f718ec8017b7482297` (Actions run `44850887402`), deliberately separate from the CP034/CP-C1(A) research branch and the protected NF/IV/PI ongoing work. It is not a modification to IV009 itself. IV010's separate compiler run `44850903052` failed; this bridge intentionally depends only on the IV009 verified proof and its IV008/IV007 ancestors, not IV010, and does not rely on a v4.35 zero-roster library.

## 1. Exact source-identified mathematical target

For arbitrary physical complex Schwartz `f,g : 𝓢(ℝ,ℂ)` that vanish off the **same real window** `[-a,a]`, define the true original arithmetic Weil mixed value

`M_a(f,g) = Zeta23.EF.literatureRHS (neutralWindowCorrelation a (f.toLp 2 volume) (g.toLp 2 volume))`,

and `D_a(f)=M_a(f,f)`, both still complex before taking real parts. The source correlation has conjugate-linear **first** and linear **second** slots. The previously verified IV009 theorem states an exact complex equality between the genuine physical Schwartz-sum original diagonal and the full finite-family original mixed Weil energy. It retains the complete pole/prime/Gamma source through `literatureRHS`.

The present NEW Lean *candidates*, if they compile, would specialize that theorem to a two-test family and prove directly

\[
D_a(f+v g)=M_a(f,f)+M_a(f,g)v+\overline v M_a(g,f)+\overline v M_a(g,g)v,
\]
\[
\Re D_a(f+v g)=\Re D_a(f)+2\Re(M_a(f,g)v)+\Re D_a(g)|v|^2.
\]

Consequently both components of the authentic original arithmetic mixed value would be recovered by real physical diagonal probes:

\[
\boxed{\Re M_a(f,g)=\frac{\Re D_a(f+g)-\Re D_a(f)-\Re D_a(g)}{2}},
\]
\[
\boxed{\Im M_a(f,g)=-\frac{\Re D_a(f+ig)-\Re D_a(f)-\Re D_a(g)}{2}}.
\]

For each of CP001's three genuine bump tests, these formulas apply once the bumps are constructed as original Schwartz objects with verified window support. The three basis diagonals and three pairs of real/imaginary probes then determine the whole 3x3 original arithmetic matrix by pure algebra. This is the missing original SOURCE bridge behind CP-C1(A)'s nine-probe criterion; it does not identify an independent explicit-formula matrix or spectral zero-side matrix.

## 2. Trust boundaries and actual predecessor checks

- **IV009 actual Actions kernel run `44850887402`: SUCCESS**, including direct full original module build and strict standard-only axiom stage. Its original source Git blob is `fa794132d438d095436879c4f78d9340ea29be02`.
- **IV008 original mixed Hermitian source Git blob:** `0a7b6cc16670160c6f4b338a36c6d51ae730dde7`. IV009's run imported the original ancestor.
- **IV010 original one-new-support gate run `44850903052`: FAILURE**. This new source **does not import IV010**, thus does not inherit its unverified assertions or compiler obstruction.
- **CP034 zero-side source-leaf run `44918784472`: SUCCESS**, but in a different Lean **v4.35** environment; never directly import its `.olean` into this **v4.34** original Weil source tree.

The new candidate file imports only the source-verified `ActualZetaPhaseIVOriginalSchwartzPolarization` and Mathlib. Six new original-source theorem proofs and two original anchor `#print axioms` requests are present. New proof text contains no `sorry` / `admit` / new axioms, but this fact is only a source inspection, not kernel acceptance.

## 3. Reproducible cheap preflight and negative control

`cpc1b_original_source_gate.py` checks the exact six theorem declaration inventory, eight requested original axiom reports, source-code conventions, no explicit proof holes, and optional **actual Git-blob matches** for IV008 and IV009 on the branch checkout. It separately checks with exact Python `Fraction` arithmetic that the imaginary probe necessarily carries a **minus sign**, rejecting its wrong-sign control. The local source-only preflight ran and passed against the new candidate.

No new GitHub Actions workflow, PR event or heavy compiler was triggered by this draft creation. The new source is a candidate until the exact pinned v4.34 Lane returns a successful `.olean` and **all eight actual `#print axioms` reports** with only `propext`, `Classical.choice`, `Quot.sound` (or none), supported by a log and source-bound receipt. Any compiler error must be repaired as the first real source diagnostic; never hide it behind a synthetic gate or an assumed source theorem.

## 4. Next concrete source acceptance and the still missing equivalence

1. In the authentic Lean v4.34 checkout, first run the cheap source gate with `--upstream`. If the original IV009/IV008 byte hashes drift, STOP and review rather than silently re-pin.
2. After source dependency + runner audit, compile this isolated new file with its actual imported library environment. Record first genuine Lean diagnostic or a complete kernel / strict axiom receipt. Do not launch an unrelated IV/NF workflow fan-out.
3. Formalize actual CP001 bump Schwartz instances and their common `[-11/10,11/10]` support, then instantiate the pair theorem on the three pairs. Merely naming bump functions in a markdown document does not discharge their Schwartz/support proofs.
4. Separately source-identify the **independent** arithmetic explicit-formula target and its nine probe diagonals with the same Fourier normalization, two poles, complete von Mangoldt `n=9` terms, Gamma term, and complex phase convention. CP-C1(A) would then become an exact original-versus-independent-matrix equality theorem.
5. CP-C1(B) **does not** close CP-C1(B spectral truncation), because full zero-roster completeness, reflected off-line terms, interval quadrature, and normalized operator tail remain separate gates. No support-independent Weil positivity or RH follows.

**Acceptance boundary:** SOURCE CANDIDATE ONLY. Genuine IV009 predecessor certified, new pair/recovery theorems not yet compiled; no original three-bump/spectral equivalence or whole-support positivity certified.