import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramStrictWitness
import WeilDefect.Arithmetic.ActualZetaOriginalJ242CanonicalGramPositivity
import WeilDefect.Generated.NF671.OriginalPhysicalFullGramPSD

namespace WeilDefect

/-!
NF672: STRICT but nonquantitative positivity of the genuine ORIGINAL
242-source physical integral Gram on [-11/10,11/10].

Input facts are the full integral-square identity (NF671) and already
accepted global independence/collar separation for exactly the original
241 oscillator sources and genuine sinh pole (NF569/NF551).

No numerical 242-dimensional smallest eigenvalue, solver enclosure,
signed Weil positivity, or RH conclusion is inferred.
-/

noncomputable section
open MeasureTheory Finset

/-- Complexification of a genuine REAL original source sum is the
identical original complex combination used by the accepted collar
separation theorem. No surrogate generators are introduced. -/
theorem nf672OriginalCombination_cast (z : Fin 242 → ℝ) (t : ℝ) :
    neutralNF550OriginalSourceCombination
        (fun i : Fin 242 => (z i : ℂ)) t =
      (neutralNF671SourceCombination
        nf545OriginalSelectedRealGenerator z t : ℂ) := by
  change
    (∑ i : Fin 242, (z i : ℂ) *
      (nf545OriginalSelectedRealGenerator i t : ℂ)) =
    ((∑ i : Fin 242,
      z i * nf545OriginalSelectedRealGenerator i t : ℝ) : ℂ)
  norm_cast

/-- A nonzero REAL original 242-vector has a nonzero observation
inside the actual full physical window. The witness comes from
the previously Lean-accepted analytic source separation theorem
on the smaller fixed collar, not from numerical Gram inversion. -/
theorem nf672OriginalPhysical_intervalWitness
    (z : Fin 242 → ℝ) (hz : z ≠ 0) :
    ∃ t : ℝ, t ∈ Set.Icc (-(11 / 10 : ℝ)) (11 / 10 : ℝ) ∧
      neutralNF671SourceCombination
        nf545OriginalSelectedRealGenerator z t ≠ 0 := by
  have hd : (fun i : Fin 242 => (z i : ℂ)) ≠ 0 := by
    intro hd0
    apply hz
    funext i
    have hi : (z i : ℂ) = 0 := congrFun hd0 i
    exact_mod_cast hi
  obtain ⟨t, ht, hne⟩ :=
    neutralNF569OriginalCollarSeparatesJ242
      (fun i : Fin 242 => (z i : ℂ)) hd
  refine ⟨t, ?_, ?_⟩
  · change (-(11 / 10 : ℝ)) ≤ t ∧ t ≤ (11 / 10 : ℝ)
    dsimp [neutralNF548CollarCenter] at ht
    constructor <;> linarith [ht.1, ht.2]
  · intro hz0
    apply hne
    rw [nf672OriginalCombination_cast z t]
    simp [hz0]

/-- FULL original physical H is strictly positive definite in all
242 unmodified original generator directions. Strictness follows from
the already accepted analytic independence and an actual integration
window; the resulting constant is not quantified uniformly. -/
theorem nf672OriginalFullPhysicalGram_strict
    (z : Fin 242 → ℝ) (hz : z ≠ 0) :
    0 < neutralNF661Quadratic neutralNF606PhysicalH z := by
  rw [nf671OriginalPhysicalH_eq_integralGram]
  exact neutralNF672IntegralGram_pos_of_separation
    nf545OriginalSelectedRealGenerator
    nf671OriginalRealSource_continuous
    (-(11 / 10 : ℝ)) (11 / 10 : ℝ)
    (by norm_num)
    nf672OriginalPhysical_intervalWitness z hz

/-- An assembled original 242-vector with nonzero complement
coordinates is nonzero. The exact NF669 source partition is used,
so no extra coordinate independence assumption occurs. -/
theorem nf672OriginalAssemble_nonzero_of_complement
    (y : Fin 227 → ℝ) (hy : y ≠ 0) :
    nf670AssembleOriginal
      (fun i => -(nf670ActualRieszResponse y i)) y ≠ 0 := by
  intro hzero
  apply hy
  funext j
  have hsource := nf670AssembleOriginal_source
    (fun i => -(nf670ActualRieszResponse y i)) y (Sum.inr j)
  have hj := congrFun hzero (nf669ComplementSource j)
  exact hsource.symm.trans hj

/-- Strict positivity of the authentic 227-direction PHYSICAL Schur
remainder. This is qualitative: no explicit c*||y||² lower bound
and no assertion about the SIGNED Weil form. -/
theorem nf672ActualPhysicalSchur_strict
    (y : Fin 227 → ℝ) (hy : y ≠ 0) :
    0 < nf670ActualSchurEnergy y := by
  have h := nf672OriginalFullPhysicalGram_strict
    (nf670AssembleOriginal
      (fun i => -(nf670ActualRieszResponse y i)) y)
    (nf672OriginalAssemble_nonzero_of_complement y hy)
  rw [nf671OriginalPhysicalH_energy_eq_square] at h
  rw [nf671ActualPhysicalSchur_eq_integral_square]
  exact h

#print axioms nf672OriginalCombination_cast
#print axioms nf672OriginalPhysical_intervalWitness
#print axioms nf672OriginalFullPhysicalGram_strict
#print axioms nf672OriginalAssemble_nonzero_of_complement
#print axioms nf672ActualPhysicalSchur_strict

end
end WeilDefect
