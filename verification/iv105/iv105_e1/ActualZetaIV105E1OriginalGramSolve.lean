import WeilDefect.Arithmetic.ActualZetaIV105DOriginalSchurReceiver
import Mathlib.LinearAlgebra.FiniteDimensional.Basic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- The actual signed packed matrix, as a finite complex linear map. -/
def neutralIV105EGram (k : ℕ) (hk : 0 < k) :
    (Fin k → ℂ) →ₗ[ℂ] (Fin k → ℂ) where
  toFun c i := ∑ j : Fin k,
    neutralIV007OriginalMixedEntry (11/10:ℝ) (neutralIV100Carrier k hk) i j * c j
  map_add' c d := by
    funext i
    simp only [Pi.add_apply, mul_add, Finset.sum_add_distrib]
  map_smul' z c := by
    funext i
    simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j hj
    ring

/-- No matrix positivity is assumed: this is the original IV009 energy. -/
theorem neutralIV105EGram_energy (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) :
    (∑ i : Fin k, conj (c i) * neutralIV105EGram k hk c i).re =
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk c) := by
  have hs (i : Fin k) := neutralIV009OriginalCollars_supported_window
    (neutralIV100Carrier k hk i) (neutralIV100Carrier_collars k hk i)
  have h := neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
    (11/10:ℝ) (neutralIV100Carrier k hk) c hs
  have he : (∑ i : Fin k, conj (c i) * neutralIV105EGram k hk c i) =
      neutralIV007OriginalMixedEnergy (11/10:ℝ) (neutralIV100Carrier k hk) c := by
    unfold neutralIV007OriginalMixedEnergy
    apply Finset.sum_congr rfl
    intro i hi
    change conj (c i) * (∑ j : Fin k,
      neutralIV007OriginalMixedEntry (11/10:ℝ) (neutralIV100Carrier k hk) i j * c j) = _
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j hj
    ring
  rw [he, h]
  rfl

theorem neutralIV105EGram_zero (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ)
    (hc : neutralIV105EGram k hk c = 0) : c = 0 := by
  have hq := neutralIV105EGram_energy k hk c
  rw [hc] at hq
  simp only [Pi.zero_apply, mul_zero, Finset.sum_const_zero, Complex.zero_re] at hq
  have hm := neutralIV101Packed_full_margin k hk c
  have hz : ‖(neutralIV100Packed k hk c).toLp 2 volume‖^2 = 0 := by
    rw [← hq] at hm
    nlinarith only [hm, sq_nonneg ‖(neutralIV100Packed k hk c).toLp 2 volume‖]
  exact funext ((neutralIV100Packed_mass_zero_iff k hk c).mp hz)

theorem neutralIV105EGram_injective (k : ℕ) (hk : 0 < k) :
    Function.Injective (neutralIV105EGram k hk) := by
  intro c d h
  have hz : neutralIV105EGram k hk (c-d) = 0 := by
    rw [map_sub, h, sub_self]
  exact sub_eq_zero.mp (neutralIV105EGram_zero k hk (c-d) hz)

theorem neutralIV105EGram_surjective (k : ℕ) (hk : 0 < k) :
    Function.Surjective (neutralIV105EGram k hk) :=
  LinearMap.surjective_of_injective (neutralIV105EGram_injective k hk)

/-- For the actual original response, the packed matrix has a unique solve. -/
theorem neutralIV105EGram_solve_unique (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) :
    ∃! d : Fin k → ℂ, neutralIV105EGram k hk d =
      fun i => neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v := by
  obtain ⟨d, hd⟩ := neutralIV105EGram_surjective k hk
    (fun i => neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v)
  exact ⟨d, hd, fun e he => neutralIV105EGram_injective k hk (he.trans hd.symm)⟩

#print axioms neutralIV105EGram_energy
#print axioms neutralIV105EGram_zero
#print axioms neutralIV105EGram_injective
#print axioms neutralIV105EGram_surjective
#print axioms neutralIV105EGram_solve_unique
end
end WeilDefect
