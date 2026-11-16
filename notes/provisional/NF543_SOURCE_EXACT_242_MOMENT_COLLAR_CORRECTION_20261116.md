# NF543 — Source-exact 242-moment smooth collar correction and logarithmic carrier gate

**2026-11-16 PT. Stacked draft on NF542 #570. Compiler acceptance pending.** Source custody unchanged: original NF494 H400/U400 SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`; original `B=11/10`, `δ=1/500` strict two-collar geometry; original `Fin 242` selected moment directions; all actual zeta zero multiplicity copies. The present formal algebra is conditional on a right inverse from the TRUE selected-moment Gram system; no invented numerical Gram entries or alternative moments.

## 1. Real NF542 compiler verdict and syntax repair

NF540 check [#43891499088](https://github.com/monocap-tech/weil-lab/actions/runs/43891499088) completed **SUCCESS** on NF542 HEAD `75136669...`. NF541 [#43891499147](https://github.com/monocap-tech/weil-lab/actions/runs/43891499147) also completed **SUCCESS**, so both the genuine log-energy quadratic moment theorem and derivative-witness conditional bridge have accepted Lean receipts. **This does not prove NF542.** Dedicated NF542 check [#43891501533](https://github.com/monocap-tech/weil-lab/actions/runs/43891501533) completed FAILURE with two parser errors at `ActualZetaLogCarrierSchwartzCompact.lean:88:21` and `:108:21`: the incorrectly written `ContDiff ℝ ∞ ψ` was not Lean syntax. NF543 replaces it by the correct `ContDiff ℝ ⊤ ψ`; that module requires a FRESH focused compiler check to reveal any further typechecking errors. No NF542 PASS is claimed at this point.

## 2. Actual original 242-moment correction algebra

Use `E=(-B,-B+δ) ∪ (B-δ,B)`, `B=11/10, δ=1/500`, and the actual physical `RealComplexL2` source `ell`. Let `g` be a genuine Schwartz test vanishing outside E. Let `M : RealComplexL2 →ₗ[ℂ] (Fin 242 → ℂ)` be the true 242-dimensional physical moment map and `R : (Fin 242 → ℂ) →ₗ[ℂ] 𝓢(ℝ,ℂ)` be the finite-rank smooth correction map. The right-inverse hypothesis

```
∀ d : Fin 242 → ℂ, M ((R d).toLp 2 volume) = d
```

is exactly what the original NF523/NF528 positive-definite weighted 242×242 Gram construction is intended to supply, but its **actual source-specific construction is not yet Lean-certified**. Additional hypothesis: each correction vector `R d` vanishes pointwise outside the exact E. Then define

```
phi = g + R (M ell - M [g]L²).
```

Linearity gives the *exact* moment equation `M [phi]L²=M ell`, not approximate equality. Support remains within the same two collars because both summands vanish outside E, and `phi` is Schwartz since the correction map takes values in Schwartz space. The existing NF540 quadratic Fourier moment plus NF542 Schwartz/L² compatibility (once compiled) gives a TRUE `k : NeutralLogHilbertCarrier B` satisfying

```
neutralLogPhysical k.val = [phi]L²,
M [phi]L² = M ell.
```

The correction is explicitly performed on the SAME original physical L² moment map and original endpoint source; no Green span, zeta zero replacement or finite-zero approximation appears. The numerical U400 coefficients do not appear inside the generic algebra, so no source-specific moment values or analytic independence are silently asserted.

## 3. Lean artifact and verification

New `WeilDefect/Arithmetic/ActualZetaOriginalCollar242Correction.lean` contains:

- `neutralNF543OriginalCollarSchwartz_supported`: exact authentic two-collar support -> physical L² support.
- `neutralNF543Correct`: source-defect subtraction and finite 242-dimensional right-inverse correction.
- `neutralNF543Correct_moments`: exact equality for ALL 242 physical selected moments under the right-inverse premise.
- `neutralNF543Correct_supported`: strict E support is preserved if g and R are E-supported.
- `neutralNF543Correct_hasOriginalLogCarrierAnd242Moments`: simultaneous genuine source-log carrier membership and exact source moment matching.

Independent `.github/workflows/nf543-source-exact-collar-242.yml` compiles repaired NF540, NF542 and NF543 in order under pinned Mathlib/Lean, then rejects `sorry`, `admit`, `axiom` declarations.

**Lean proof state: code committed, pending actual GitHub compiler acceptance.** A clean syntax parse is not an acceptance receipt.

## 4. Critical remaining original-source obligations

1. Construct the TRUE `M` from the repository's authentic 242 selected `j_i` (including sinh-pole mode) on the original physical L² window. Prove moments are continuous in the relevant topology and do not alter the source object.
2. Construct `R` from the original positive-definite Gram `G_ij = ∫ χ j_i j_j`: certify positivity/independence for original `j_i`, invert `G`, prove `R` is Schwarz/C∞, supported inside E and preserves real odd symmetry. The **present Lean file assumes** the resulting right-inverse and support properties; they are not yet discharged.
3. Actually build original NF528 (g_s): same original `ell_U`, midpoint affine compression, inward mollification, odd reflection, and support interior to E. Promote `phi_s = g_s + R(M ell_U - M g_s)` with this authentic R.
4. Prove true complete two-source graph convergence `phi_s → ell_U` with the **actual all-multiplicity** divisor dyadic tail and original source envelope, not just physical L². This remains analytic NF524/NF528; no new Lean certificate.
5. Independently compile NF539 exact all-source true divisor identity and NF527 true gamma/n9/pole (Q≥(1/10)‖f‖²) on every strict smooth collar. Then transfer the resulting original nonzero sign. RH and global W_ODD_NEG remain OPEN.

**Disposition:** source-exact 242-moment correction and genuine log carrier entered as a clearly conditional finite-rank formal proof target. The specific original Gram inverse and actual approximant sequence are NOT yet compiled. The original singular source is not inferred H¹ or identified with a Green span.
