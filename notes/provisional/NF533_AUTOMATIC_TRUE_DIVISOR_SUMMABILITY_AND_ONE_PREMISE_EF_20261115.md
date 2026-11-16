# NF533 — Genuine all-multiplicity explicit formula, removing a redundant series hypothesis

**November 15, 2026 PT. Status: LEAN COMPILATION PENDING.** Stacked on NF532 PR #560. **NF532 focused GitHub Actions #43804723365 passed both existing graph-closure and genuine physical-window correlation EF targets.** This stage adds the next minimal module, not another simulated arithmetic source, and does not replay original NF494 U400. SHA256 unchanged: `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`.

## Mathematical advance

The previous compiled `neutralActualZetaWindowCorrelation_literature` assumed both:
1. `ContDiff ℝ 2 (neutralWindowCorrelation a f g)`;
2. absolute summability of the complete authentic divisor-copy series.

The second assumption is **already a consequence of the imported unconditional true-zeta explicit formula**. For any compactly supported C² test `k`, `Zeta23.WeilEF.EF_lit_zeta` proves:

```text
Summable (fun ρ : (zetaZeros zetaSeam).carrier =>
  (zetaZeros zetaSeam).mult ρ * paperFT k (gammaOf ρ))
```

The authentic Weil-Lab divisor is literally `Σ ρ : NeutralActualZetaZeroPoint, Fin (neutralActualZetaMultiplicity ρ)`. The same imported zeta-zero point type and multiplicity are already identified in `ActualZetaLiteralFormula.lean`. Hence finite-copy expansion of the nonnegative norms gives the **exact identity**

```text
Σ_(q:actual divisor copies) ||rawFT(k, ordinate(q))||
 = Σ_(ρ:actual points) mult(ρ) ||rawFT(k, ordinate(ρ))||
 = Σ_(ρ:actual points) ||mult(ρ)*rawFT(k, ordinate(ρ))||.
```

The last series is absolutely summable by the imported EF theorem. The first is therefore summable as well. In Lean, the new proof is structured through `summable_sigma_of_nonneg`, finite-fiber `tsum_fintype`, and `Summable.of_norm_bounded`. This counts **all** genuine copies, does not assume simplicity, critical-line placement, Green-packet density or any enumeration.

The new theorem `neutralActualZetaDivisor_rawTransform_summable_of_contDiff` formalizes that transfer from the imported zeta EF to literal divisor-copy summability. The new `neutralActualZetaWindowCorrelation_literature_of_contDiff` combines it with the **already compiled** correlation transform and literature formula, and uses the existing generic `neutralWindowCorrelation_hasCompactSupport`. It thus needs *only* C² regularity of the genuine physical-window correlation.

**Both theorems are written with no sorry/axiom/admit. This module is not yet marked compiled until the dedicated NF533 check succeeds.**

## Consequences and strict limits

If accepted, the generic physical test identity becomes a single-regularity-premise theorem:

`ContDiff ℝ 2 (neutralWindowCorrelation a f g) ⟹ Σ_actual-divisor conj(F_f(conj z)) F_g(z)=literatureRHS(correlation)`.

For genuinely strict collar-supported smooth physical f and g, the remaining formal admissibility job is to prove that the L² window representatives agree with those compactly supported smooth functions and that their correlation is C² (e.g. from the existing Mathlib compact-supported convolution differentiability theorems). This is a **representation theorem**, not a need for new number-theoretic zero estimates.

The NF527 universal two-collar gamma/true n=9/pole lower bound, NF528 original U400-specific collar-preserving graph convergence, the original exact 242-moment optional provenance theorem, and complete original source positivity remain **analytic, uncompiled**. NF533 does not establish Green density, full odd-sector positivity, W_ODD_NEG or RH.

## GitHub custody

- Earlier NF532 focused PASS: `https://github.com/monocap-tech/weil-lab/actions/runs/43804723365`.
- New proof module: `WeilDefect/Arithmetic/ActualZetaSmoothLiteralFormulaAutomatic.lean`.
- Targeted Lake CI extended to `lake build WeilDefect.Arithmetic.ActualZetaSmoothLiteralFormulaAutomatic`.
- NF533 focused CI: `https://github.com/monocap-tech/weil-lab/actions/runs/43807244612`. **PENDING at drafting.**

**NF534 acceptance priority:** inspect NF533 compiler output and fix any exact elaboration errors. Then formalize C² regularity of the correlation of a genuinely compact smooth physical-window representative and compose it with this automatically summable, complete zeta EF. Keep original-source and two-collar coercivity certification separate.
