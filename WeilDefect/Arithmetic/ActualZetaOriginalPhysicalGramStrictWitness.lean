import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramIntegralSquare
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

namespace WeilDefect

/-!
NF672: the precise strictly-positive interval Gram implication.

Unlike PSD, strict positivity needs one genuinely nonzero observation
of the source combination in the actual integration interval.
No eigenvalue lower bound or condition number is inferred.
-/

noncomputable section
open MeasureTheory Finset

theorem neutralNF672IntegralGram_pos_of_witness {n : ℕ}
    (g : Fin n → ℝ → ℝ) (hg : ∀ i, Continuous (g i))
    (a b : ℝ) (hab : a < b) (c : Fin n → ℝ)
    (t : ℝ) (ht : t ∈ Set.Icc a b)
    (hne : neutralNF671SourceCombination g c t ≠ 0) :
    0 < neutralNF661Quadratic (neutralNF671IntegralGram g a b) c := by
  rw [neutralNF671IntegralGram_energy_eq_square g hg a b c]
  have hcont : Continuous
      (fun s : ℝ => (neutralNF671SourceCombination g c s)^2) := by
    unfold neutralNF671SourceCombination
    fun_prop
  apply intervalIntegral.integral_pos hab hcont.continuousOn
    (fun s hs => sq_nonneg _) 
  exact ⟨t, ht, sq_pos_of_ne_zero hne⟩

/-- A source-separating observation on the actual integration
interval is sufficient for strict original-style Gram energy.
The witness must be proved from the ORIGINAL functions independently. -/
theorem neutralNF672IntegralGram_pos_of_separation {n : ℕ}
    (g : Fin n → ℝ → ℝ) (hg : ∀ i, Continuous (g i))
    (a b : ℝ) (hab : a < b)
    (hsep : ∀ c : Fin n → ℝ, c ≠ 0 →
      ∃ t : ℝ, t ∈ Set.Icc a b ∧
        neutralNF671SourceCombination g c t ≠ 0)
    (c : Fin n → ℝ) (hc : c ≠ 0) :
    0 < neutralNF661Quadratic (neutralNF671IntegralGram g a b) c := by
  obtain ⟨t, ht, hne⟩ := hsep c hc
  exact neutralNF672IntegralGram_pos_of_witness
    g hg a b hab c t ht hne

#print axioms neutralNF672IntegralGram_pos_of_witness
#print axioms neutralNF672IntegralGram_pos_of_separation

end
end WeilDefect
