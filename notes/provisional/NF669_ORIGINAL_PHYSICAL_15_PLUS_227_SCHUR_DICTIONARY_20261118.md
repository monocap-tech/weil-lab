# NF669 — exact original 242 = certified 15 ⊕ complementary 227 physical source dictionary

## Kernel-accepted predecessor / boundary

The corrected NF667 workflow **44455028120** completed successfully in all three jobs, including authentic original NF606 integral physical 15-source coercivity at exactly `10^-60` and standard-axiom audit. This is the original selected source set `[0,...,13,241]`, *not* a general claim about all 242 physical directions. Its full rigorous original-source certificate is independent of any floating eigenvalue test.

NF668 generic positive-definite/injective real finite Gram consequences have now passed Lean in workflow **44457538220**, generic job **135336128892**, including standard axiom audit. NF668's original physical specialization was still compiling when NF669 was prepared. The NF669 source dictionary therefore depends on the already accepted NF665 physical coercivity, not on pending NF668 generated material.

## Exact original 242 index partition

`WeilDefect/Generated/NF669/OriginalPhysicalComplementDictionary.lean` defines:

- selected block `S : Fin 15 → Fin 242`, *identically* the earlier certified `neutralNF661Source`: `S(0..13)=0..13`, `S(14)=241`;
- complementary block `J : Fin 227 → Fin 242` with `J(j)=j+14`, exactly original oscillators `14..240`;
- injectivity and disjointness of both embeddings;
- exhaustive dichotomy `∀k:Fin242, (∃i,S i=k) ∨ (∃j,J j=k)`;
- explicit bijection `(Fin 15 ⊕ Fin 227) ≃ Fin 242`, with original generator labels preserved.

This rules out accidentally using a transformed moment basis or an altered pole when formulating the remaining complementary operator. All new structural proofs are pending separate Lean acceptance.

## Actual original analytical H block definitions

For exact original `neutralNF606PhysicalH`, not its certified integer center:

```
A_ij = H_(S i),(S j),      dimensions 15×15
B_ij = H_(S i),(J j),      dimensions 15×227
C_ij = H_(J i),(J j),      dimensions 227×227
```

A is definitionally the same original integral matrix `neutralNF661PhysicalH` whose quantitative coercivity has just been kernel-certified:

`∀x, 10^-60 * Σ_i x_i² ≤ Σ_ij A_ij x_i x_j.`

The cross block `B` and cofinite block `C` are defined by the same original NF606 real integrals. Symmetry of A/C and source-actual transposition of B use the existing accepted original physical H symmetry proof. There is **no positive-coercivity assumption** for C.

## General exact Schur-completion proof candidate

`WeilDefect/Arithmetic/ActualZetaOriginalPhysicalGramSchurAlgebra.lean` establishes finite real bilinearity and symmetry, the quadratic square-expansion formula, and the exact identity

`Q_full(x,y) = Q_A(x+U y) + (Q_C(y)-Q_A(U y))`

provided the cross-block Riesz response satisfies

`∀x,y, Cross_B(x,y)=Bilinear_A(x,U y)`.

The generic lemmas then prove:
- given the already certified `Q_A≥0` and a nonnegative Schur remainder `Q_C(y)-Q_A(U y)≥0`, the combined block energy is nonnegative;
- conversely, combined block nonnegativity forces the Schur remainder to be nonnegative (test at `x=-U y`).

These source-independent algebraic claims are **Lean pending**. In particular, no NF669 proof claims that the authentic original B has an already certified Riesz response or that its actual 227-source Schur remainder has a strict margin. Those are separate mathematical/analytical obligations, not missing parentheses in the original Gram positivity proof.

**Important distinction:** because H is originally defined by products of functions under an integral, nonnegative full L2 Gram energy is qualitatively expected from integral squares under the standard integrability hypotheses. The substantive full-system problem is quantitative/nondegenerate original physical coordinate control and its connection to the corrected signed Weil form; local A coercivity alone does not prove either.

## Verification architecture

New two-job pinned workflow `.github/workflows/nf669-original-physical-complement.yml`:

1. `generic-schur-completion`: Lean builds all seven exact Schur algebra lemmas and audits standard axioms.
2. `original-physical-complement`: rehydrates same pinned original NF631/NF632/NF621/NF648 artifacts, rebuilds NF655, NF658, NF659, the NF662/663 original-real certificate chain and NF664–NF665 coercivity, then compiles the exact 15+227 original index dictionary and audits its source coercivity/transposition and all upstream terminal certificates against explicit standard axiom whitelist.

All new NF669 material is formally proposed until compiler checks pass. Draft stacked against NF668, no merge to main.

## Next

NF670 should discharge the actual source-index sum/block quadratic correspondence and then investigate Riesz response `U=A^-1B` for the 227 original oscillator directions. The authentic complementary Schur energy must be separately controlled if demanding strict full-dimensional coercivity. This does not advance global signed Weil positivity or RH without further transport.
