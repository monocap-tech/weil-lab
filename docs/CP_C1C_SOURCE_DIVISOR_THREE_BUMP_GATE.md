# Weil-Lab — CP-C1(C): direct original Fin 3 arithmetic–divisor source bridge

**Independent cross-projection source proposal, November 22, 2026.**

## 1. Kernel-predecessor evidence

The genuine original IV009 Lean 4.34 Actions run **44850887402** finished successfully. Its log shows a **9,242-job successful build**, strict standard-only axiom audit, and both of the following accepted declarations:

- `WeilDefect.neutralIV008OriginalMixedEntry_eq_divisor`, identifying the literal original mixed zeta arithmetic explicit formula with the actual **all-multiplicity** original zeta-divisor entry on a supported Schwartz family;
- `WeilDefect.neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal`, identifying the full mixed finite-energy matrix with the diagonal of the actual physical complex Schwartz sum.

This is a valuable **internal original-source arithmetic ↔ complete-divisor** identification. It is **not** automatically an independently rederived pole–prime–Gamma matrix or a separate operator/spectral model. No finite enumeration, truncation estimate, RH or universal positivity is involved.

## 2. Proposed exact Fin 3 theorem

Let `s : Fin 3 → 𝓢(ℝ,ℂ)` be arbitrary genuine complex Schwartz tests each vanishing outside the same physical interval `[-a,a]`, and let `u : Fin 3 → ℂ`. Define

- `A(i,j) = neutralIV007OriginalMixedEntry a s i j` (literal original signed arithmetic EF),
- `Z∞(i,j) = neutralIV007OriginalDivisorEntry a s i j` (complete actual all-copy zeta divisor),
- `S = neutralIV009PhysicalSchwartzSum s u`.

The existing IV008 and IV009 theorems mathematically imply

\[
A(i,j) = Z_\infty(i,j)\quad (i,j\in\{0,1,2\}),
\]

\[
\operatorname{EF}_{\mathrm{original}}(S,S)
=\sum_{i,j=0}^{2}\overline{u_i} Z_\infty(i,j)u_j.
\]

Moreover `Z∞` is Hermitian. There is **no PSD assertion**, because off-critical zeros have reflected sesquilinear factors rather than plain squared norms.

The attached `CP_C1C_original_complete_divisor_finite3.lean` specializes the existing original-source lemmas to `Fin 3` and requests five real axiom reports (two predecessors, three new declarations). It deliberately imports neither IV010 nor CP-C1(B), so it can be compiled independently after the usual source pin checks. **These three new names have NOT been compiled or kernel accepted.**

## 3. The genuinely unpaid physical and independent gates

**Frozen actual CP001 bump family.** The CP001 normalized even flat real profile is explicitly

\[
\phi(u)=\begin{cases}e^{1-1/(1-u^2)},&|u|<1\\0,&|u|\ge1.\end{cases}
\]

with physical `b_(c,h)(x)=φ((x-c)/h)` at `c=±1099/1000`, `h=1/2000`, and at `c=1/5`, `h=r ∈ {1/1000,1/500}`. To instantiate the *frozen* CP001 source, prove this exact flat function is `C∞`, real, even, compactly supported, and hence a complex Schwartz test, with literal support in `[-11/10,11/10]`. Do not substitute the generic Mathlib bump supplied by IV015; that is a different test and does not inherit CP003's fixed bump-mass/overlap intervals, nor CP004's particular Fourier shape `Φ`.

**Independent arithmetic explicit-formula matrix E.** CP-C1(A) separately requires independently computed original poles, genuine von Mangoldt terms (including `n=9` and both orientations) and Gamma terms, with exactly the same Fourier and conjugation conventions. The source identity `A=Z∞` does not itself establish independently computed `A=E`.

**Finite spectral truncation Z(T).** The untruncated source equality `A=Z∞` is not a certificate for a numerically enclosed finite-height zero matrix: it needs a count-complete ordinal roster, exact Fourier-profile enclosures, and a quantitatively justified all-zero tail. The target `||G^-1/2 (A-Z(T))G^-1/2||op≤ε` is still open.

**Independent spectral model.** Mapping to a genuinely distinct Hilbert/spectral realization requires an admissibility-preserving map and actual pairing preservation. It does not follow from indexing the same original divisor two ways.

## 4. Custody and next action

No new GitHub branch, PR event, or CI job is needed to record this source-only derivation. In view of the repository's old NF pull_request/push trigger fan-out, keep this file local until there is a controlled compiler opening. CP-C1(B) job **45060782018** is the active genuine compiler gate as of this memo; it must not be called accepted until its own `.olean` and eight axiom receipts pass. The exact `Fin 3` source candidate may then be compiled as a smaller alternative attachment, independently of CP-C1(B)'s six-phase-lemma gate.

**Promotion rule:** no more than “mathematically follows from earlier accepted IV008/IV009, provided the statements specialize as written; source candidate not compiled” until the new declaration passes a real Lean kernel and a strict source-bound axiom receipt.

## 5. CP-C1(B) genuine compiler diagnostic and recovery

Original CP-C1(B) Actions run [45060782018](https://github.com/monocap-tech/weil-lab/actions/runs/45060782018) **FAILED in the actual Lean 4.34 source compilation step** after its strict Python preflight and pinned Lake bootstrap passed. The first compiler error was a failed `rw [hdiag]` at line 133: the goal's diagonal alias had reduced to the genuine mixed entry while the hypothesis had not. The recovery changes to `dsimp only [neutralCPC1BOriginalDiagonal] at hdiag ⊢` prior to rewriting. The second compiler error was an unmatched unnamed `noncomputable section` before `end WeilDefect`, fixed by an additional `end`. This is a **source repair candidate**, not yet a recompilation pass. In the failed compiler run, the first three new CP-C1(B) theorems had standard-only axiom reports, while the phase response and the two derived probe theorems inherited `sorryAx` due to the unfinished proof; they are not accepted. The new independent CP-C1(C) Fin 3 candidate likewise closes its unnamed section. No original finite 3-bump instantiation, spectral tail enclosure or independent spectral isometry is claimed.

