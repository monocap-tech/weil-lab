# NF668 — unconditional original 15-source physical Gram: certified coercivity and finite nondegeneracy consequences

## Verified terminal predecessor

The corrected NF667 complete-source verification workflow run **44455028120** is **SUCCESS** in all three jobs.

- Job **135327866582** generic preconditioner frame: PASS with standard axiom audit.
- Job **135327866152** source-frozen real preconditioner: PASS, including all 15 diagonal and upper-triangular entry gates, exact K surjectivity, Frobenius norm and quadratic congruence; standard axiom audit.
- Job **135327866477** complete original physical 15-generator coercivity: PASS, including reconstruction of pinned NF631/NF632/NF621/NF648 source archives, NF655 actual physical H, 120 NF658 compact source certificates, all 225 NF662 actual physical entries, all 450 NF659 integer transformed gates, NF663 10^-192 real intervals, NF664 actual transformed-real positivity, and terminal NF665 physical 10^-60 coercivity.
- The actual theorem `WeilDefect.nf665OriginalPhysical_coercivity` and all terminal dependency prints report only **[propext, Classical.choice, Quot.sound]**. No `sorryAx` appears in the terminal dependency list. This constitutes completed original 15-source local coercivity certification, not simply a numerical preflight or theorem proposal.

The exact certified theorem is:
`∀ x : Fin 15 → ℝ, ((1:ℝ)/(10^60:ℝ)) * neutralNF661SqNorm x ≤ neutralNF661Quadratic neutralNF661PhysicalH x`.
Source indices are exactly original 0..13 and 241; physical H entries are original unweighted interval integrals of authentic generators, not a numerical surrogate.

A newer NF667 workflow with an additional strict axiom whitelist may still be pending; the above full source **build and axiom audit** are independently confirmed.

## NF668: downstream finite physical Gram mathematics

NF668 does not create a new Gram approximation or enlarge the certified source space. It builds unconditional structural consequences of the accepted theorem.

### Generic finite proof module
`WeilDefect/Arithmetic/ActualZetaOriginalPhysicalGramPositiveDefinite.lean`

Defines the row action `neutralNF668GramApply H x i := ∑j H i j * x j` and proposes theorems:
1. `x ≠ 0 ⇒ ∑i x_i² > 0` in real finite dimensions.
2. A finite-sum identity `xᵀ H x = ∑i (H x)_i x_i`.
3. Any exact real coercivity (c‖x‖² ≤ xᵀH x) with (c>0) implies **strict positivity** for every nonzero x.
4. Under that coercivity, `Hx=0 ⇒ x=0`, and `Function.Injective (neutralNF668GramApply H)`.
5. At most one solution to `Hx=b` for each b; uniqueness alone is *not* an unconditional existence assertion.

These are new Lean proof candidates. Do not mark them accepted until generic CI passes.

### Authentic original source specialization
`WeilDefect/Generated/NF668/OriginalPhysicalGramNondegenerate.lean`

Provides an exact named `Matrix (Fin 15) (Fin 15) ℝ` equal to `neutralNF661PhysicalH`, whose entries remain the genuine original NF606 integrals; establishes original-source symmetry, exposes the exact NF665 coercivity lower bound as `nf668OriginalPhysical_lowerBound`, and targets strict positive definiteness, no kernel, row-action injectivity, and unique local 15-dimensional Gram solve. An explicit action-equals-original-integral sum theorem preserves source index custody.

These named source-specific declarations are new **Lean candidates**, not yet kernel accepted. Their exact imported terminal premise is a theorem already accepted by Lean with standard axioms, not an assumption.

## Verification design

New workflow `.github/workflows/nf668-original-physical-positive-definite.yml`:

1. Generic finite real coercivity, positive quadratic energy, trivial Gram kernel, injectivity, and unique-solve proof build/axiom audit.
2. Complete original pinned source artifact reconstruction, full original 15-source certified coercivity rebuild, NF668 original H matrix specialization, and strict standard-axiom whitelist checking NF668 source consequences and all 11 critical NF665/664/663 dependencies.

Do not interpret finite Gram **injectivity** as proof of existence of the original full 242-source physical solve or global signed Weil positivity. Those remain separate obligations. The local 15-generator Gram is certified; the broader 242-dimensional H and global RH remain **OPEN**.

## Next conceptual gate

After NF668, assess the exact relation of this certified 15-source subspace to the remaining 227 original physical oscillator directions. Strict positivity of the selected 15-dimensional principal submatrix does not imply positivity of a 242×242 Gram or the global signed Weil form. A certified complement/Schur analysis or other source-aware extension is required before any broader claim. All work remains stacked in draft PRs; no merge to main.
