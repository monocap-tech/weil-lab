# CP-C1(D) — exact nine-scalar falsifiable original Weil compatibility

**Jurisdiction:** independent CP. **Branch source:** pinned genuine original Lean 4.34 IV008 and IV009, with pending repaired CP-C1(B) and independent CP-C1(C) candidates. **Acceptance:** all five CP-C1(D) names and the repaired B/C chain require genuine direct Lean and standard-only axiom receipts; this is currently a source candidate, not LEAN PASS.

## Original physical measurements

Fix three actual complex Schwartz tests `s : Fin 3 -> 𝓢(ℝ,ℂ)` supported in one original window. Let `q(f) = Re Zeta23.EF.literatureRHS (neutralWindowCorrelation a f f)` and `A_ij` be the literal original mixed arithmetic value. The original first-conjugate-linear convention forces

```
A_ii ∈ ℝ,  A_ii = q(s_i)
Re A_ij = [q(s_i+s_j) - q(s_i) - q(s_j)]/2
Im A_ij = -[q(s_i+i s_j) - q(s_i) - q(s_j)]/2, i<j
A_ji = conj A_ij.
```

The nine observations are exactly 3 diagonals, 3 '+' probes and 3 'i' probes. This is a **complete physical probe dictionary for the original signed arithmetic form** once B is accepted. CP-C1(C) and original IV008 also identify the same entries with the unchanged all-multiplicity **complete** original zeta-divisor pairing. These complete divisor entries must not be confused with a finite-height RH-only Gram model.

## Independently falsifiable conditional test

For any independently proposed `T : Fin 3 -> Fin 3 -> ℂ`, the new Lean theorem candidate `neutralCPC1D_original_eq_target_of_nine_phase_readings` requires (i) **T is Hermitian**, (ii) three target diagonal real parts equal the original source readings, (iii) each upper triangle real part equals the original physical +1 reconstruction, and (iv) each upper triangle imaginary part equals the original physical i reconstruction, including the **negative** sign. From those **nine independent real scalar obligations**, it concludes the entire 3×3 matrix equality `A=T`. It does **not assume** that an external arithmetic or spectral target satisfies any of these hypotheses.

A target with the same support graph and mass but a wrong off-diagonal phase must fail. A target using only zeros on the critical line without a rigorously complete divisor and normalization dictionary cannot be called compatible with the original complete zeta-divisor side merely on the strength of this theorem.

## Existing and unpaid certificates

- Genuine original IV009 Actions [44850887402](https://github.com/monocap-tech/weil-lab/actions/runs/44850887402): LEAN PASS with original IV008/IV009 standard axioms.
- New CP-C1(B) Actions [45060782018](https://github.com/monocap-tech/weil-lab/actions/runs/45060782018): LEAN FAIL. Corrected proof alias and section closure committed at `afcaae11`; not yet recompil-ed.
- CP-C1(C) Fin 3 exact complete-divisor bridge: source committed, not yet compiled.
- CP-C1(D): five new source Lean candidates with two genuine original anchor axiom requests; not yet compiled.
- Exact CP001 flat-profile bump construction, its Schwartz support and overlap, complete external zero roster, independent finite-height zero-side interval matrix, certified `G` normalization and tail decay remain unproved in this gate.

**Workflow discipline:** No PR reopening, no new heavy Actions submission while legacy unrestricted NF PR hooks remain active. Test the new branch in an isolated Lean v4.34 checkout or via a controlled manual compiler lane. Do not promote preflight to compiler success.
