import WeilDefect.Arithmetic.ActualZetaIV105E2OriginalSolveAttachment

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

theorem neutralIV106C1Solve_zero (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (ho : neutralIV101MassComplement k hk v)
    (hn : ∀ i : Fin k, inner ℂ (neutralIV105CResponse k hk i)
      (v.toLp 2 volume) = 0) :
    neutralIV105E2Solve k hk v = 0 := by
  apply neutralIV105EGram_zero k hk
  rw [neutralIV105E2Solve_eq]
  funext i
  change neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v = 0
  rw [neutralIV105CResponse_pair k hk i v hv ho, hn i]

theorem neutralIV106C1Penalty_zero (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (ho : neutralIV101MassComplement k hk v)
    (hn : ∀ i : Fin k, inner ℂ (neutralIV105CResponse k hk i)
      (v.toLp 2 volume) = 0) :
    neutralIV101Q (11/10:ℝ)
      (neutralIV100Packed k hk (neutralIV105E2Solve k hk v)) = 0 := by
  have hz := neutralIV106C1Solve_zero k hk v hv ho hn
  have h := neutralIV105EGram_energy k hk (neutralIV105E2Solve k hk v)
  have hc : neutralIV105EGram k hk (neutralIV105E2Solve k hk v) = 0 := by
    rw [hz, map_zero]
  rw [hc] at h
  simp only [Pi.zero_apply, mul_zero, Finset.sum_const_zero, Complex.zero_re] at h
  exact h.symm

#print axioms neutralIV106C1Solve_zero
#print axioms neutralIV106C1Penalty_zero
end
end WeilDefect
