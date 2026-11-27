import WeilDefect.Arithmetic.ActualZetaIV103OriginalSchwartzSpectralAttachment
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic
import Mathlib.Data.Nat.Factorization.PrimePow

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap FourierTransform ComplexConjugate BigOperators

/-- The exact cutoff underlying the AM/AP radius-two prime dictionary. -/
theorem neutralIV162Exp_four_bounds :
    (54:ℝ) < Real.exp 4 ∧ Real.exp 4 < 55 := by
  have he : Real.exp 4 = (Real.exp 1)^4 := by
    rw [show (4:ℝ) = 1+1+1+1 by norm_num]
    simp only [Real.exp_add]
    ring
  have hl : (2718/1000:ℝ) ≤ Real.exp 1 :=
    (by norm_num : (2718/1000:ℝ) < 2.7182818283).le.trans Real.exp_one_gt_d9.le
  have hu : Real.exp 1 ≤ (272/100:ℝ) :=
    Real.exp_one_lt_d9.le.trans (by norm_num)
  rw [he]
  constructor
  · exact (by norm_num : (54:ℝ) < (2718/1000:ℝ)^4).trans_le
      (pow_le_pow_left₀ (by norm_num) hl 4)
  · exact (pow_le_pow_left₀ (Real.exp_pos 1).le hu 4).trans_lt (by norm_num)

/-- No real-log comparisons are hidden in the finite prime-power census. -/
theorem neutralIV162Prime_range :
    rightLimitPrimePowerFinset 2 = (Finset.range 55).filter IsPrimePow := by
  ext n
  rw [mem_rightLimitPrimePowerFinset,Finset.mem_filter,Finset.mem_range]
  have ⟨hl,hu⟩ := neutralIV162Exp_four_bounds
  constructor
  · rintro ⟨hp,hlog⟩
    have hn : (0:ℝ) < (n:ℝ) := by exact_mod_cast hp.pos
    have h : (n:ℝ) ≤ Real.exp 4 :=
      (Real.log_le_iff_le_exp hn).mp (by simpa only [show (2:ℝ)*2=4 by norm_num] using hlog)
    exact ⟨by exact_mod_cast h.trans_lt hu,hp⟩
  · rintro ⟨hn,hp⟩
    have hn' : (0:ℝ) < (n:ℝ) := by exact_mod_cast hp.pos
    have h : (n:ℝ) ≤ 54 := by exact_mod_cast (show n ≤ 54 by omega)
    exact ⟨hp,by
      have hh := (Real.log_le_iff_le_exp hn').mpr (h.trans hl.le)
      rw [show (2:ℝ)*2=4 by norm_num]
      exact hh⟩

def neutralIV162PrimeBank : Finset ℕ :=
  {2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53}

/-- Explicit prime-power witnesses and distinct prime-divisor exclusions.
Avoid reducing the opaque minFac decision procedure. -/
set_option maxHeartbeats 4000000 in
theorem neutralIV162Census (n : ℕ) (hn : n < 55) :
    IsPrimePow n ↔ n ∈ neutralIV162PrimeBank := by
  interval_cases n
  · simp [neutralIV162PrimeBank, not_isPrimePow_zero]
  · simp [neutralIV162PrimeBank, not_isPrimePow_one]
  · have hp : IsPrimePow (2:ℕ) := (isPrimePow_nat_iff _).2 ⟨2,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (3:ℕ) := (isPrimePow_nat_iff _).2 ⟨3,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (4:ℕ) := (isPrimePow_nat_iff _).2 ⟨2,2,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (5:ℕ) := (isPrimePow_nat_iff _).2 ⟨5,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (6:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 3 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (7:ℕ) := (isPrimePow_nat_iff _).2 ⟨7,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (8:ℕ) := (isPrimePow_nat_iff _).2 ⟨2,3,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (9:ℕ) := (isPrimePow_nat_iff _).2 ⟨3,2,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (10:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 5 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (11:ℕ) := (isPrimePow_nat_iff _).2 ⟨11,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (12:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 3 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (13:ℕ) := (isPrimePow_nat_iff _).2 ⟨13,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (14:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 7 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (15:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 3 ⟨by decide, by decide⟩
      have hb := hu 5 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (16:ℕ) := (isPrimePow_nat_iff _).2 ⟨2,4,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (17:ℕ) := (isPrimePow_nat_iff _).2 ⟨17,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (18:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 3 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (19:ℕ) := (isPrimePow_nat_iff _).2 ⟨19,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (20:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 5 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (21:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 3 ⟨by decide, by decide⟩
      have hb := hu 7 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (22:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 11 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (23:ℕ) := (isPrimePow_nat_iff _).2 ⟨23,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (24:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 3 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (25:ℕ) := (isPrimePow_nat_iff _).2 ⟨5,2,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (26:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 13 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (27:ℕ) := (isPrimePow_nat_iff _).2 ⟨3,3,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (28:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 7 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (29:ℕ) := (isPrimePow_nat_iff _).2 ⟨29,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (30:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 3 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (31:ℕ) := (isPrimePow_nat_iff _).2 ⟨31,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (32:ℕ) := (isPrimePow_nat_iff _).2 ⟨2,5,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (33:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 3 ⟨by decide, by decide⟩
      have hb := hu 11 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (34:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 17 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (35:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 5 ⟨by decide, by decide⟩
      have hb := hu 7 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (36:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 3 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (37:ℕ) := (isPrimePow_nat_iff _).2 ⟨37,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (38:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 19 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (39:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 3 ⟨by decide, by decide⟩
      have hb := hu 13 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (40:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 5 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (41:ℕ) := (isPrimePow_nat_iff _).2 ⟨41,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (42:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 3 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (43:ℕ) := (isPrimePow_nat_iff _).2 ⟨43,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (44:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 11 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (45:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 3 ⟨by decide, by decide⟩
      have hb := hu 5 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (46:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 23 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (47:ℕ) := (isPrimePow_nat_iff _).2 ⟨47,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (48:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 3 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (49:ℕ) := (isPrimePow_nat_iff _).2 ⟨7,2,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (50:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 5 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (51:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 3 ⟨by decide, by decide⟩
      have hb := hu 17 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (52:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 13 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]
  · have hp : IsPrimePow (53:ℕ) := (isPrimePow_nat_iff _).2 ⟨53,1,by decide,by decide,by decide⟩
    simp [neutralIV162PrimeBank, hp]
  · have hp : ¬ IsPrimePow (54:ℕ) := by
      intro h
      obtain ⟨q, hq, hu⟩ := isPrimePow_iff_unique_prime_dvd.mp h
      have ha := hu 2 ⟨by decide, by decide⟩
      have hb := hu 3 ⟨by decide, by decide⟩
      omega
    simp [neutralIV162PrimeBank, hp]

theorem neutralIV162Prime_bank :
    rightLimitPrimePowerFinset 2 = neutralIV162PrimeBank := by
  rw [neutralIV162Prime_range]
  ext n
  rw [Finset.mem_filter, Finset.mem_range]
  constructor
  · rintro ⟨hn,hp⟩
    exact (neutralIV162Census n hn).1 hp
  · intro hn
    have hb : n < 55 := by
      simp only [neutralIV162PrimeBank, Finset.mem_insert, Finset.mem_singleton] at hn
      rcases hn with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> decide
    exact ⟨hb,(neutralIV162Census n hb).2 hn⟩

theorem neutralIV162Prime_count :
    (rightLimitPrimePowerFinset 2).card = 24 := by
  rw [neutralIV162Prime_bank]
  unfold neutralIV162PrimeBank
  decide

/-- AM's physical prime energy uses exactly the original two signed
translations, with the original von Mangoldt coefficient. -/
def neutralIV162PrimeMixed (u v : 𝓢(ℝ,ℂ)) : ℂ :=
  ∑ n ∈ neutralIV162PrimeBank,
    ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
      ((∫ x : ℝ, v x * conj (u (x-Real.log n))) +
       (∫ x : ℝ, v x * conj (u (x+Real.log n))))

/-- Same-window specialization of the original mixed correlation
identity, proved directly from the IV006 representative dictionary.
No cross-support Schur extension is needed for this equality. -/
theorem neutralIV191Correlation (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0)
    (τ : ℝ) :
    neutralWindowCorrelation a (u.toLp 2 volume) (v.toLp 2 volume) τ =
      ∫ x : ℝ, v x * conj (u (x - τ)) := by
  have huae := neutralIV006Schwartz_window_ae a u hu
  have hvae := neutralIV006Schwartz_window_ae a v hv
  have hshift :=
    (measurePreserving_sub_right volume τ).quasiMeasurePreserving.ae_eq_comp huae
  unfold neutralWindowCorrelation
  apply integral_congr_ae
  filter_upwards [hvae, hshift] with x hvx hux
  change neutralWindowRepresentative a (u.toLp 2 volume) (x - τ) =
    u (x - τ) at hux
  rw [hvx, hux]

theorem neutralIV162Prime_literal (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-(2:ℝ)) 2 → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(2:ℝ)) 2 → v x = 0) :
    (∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation 2 u v) n) =
      neutralIV162PrimeMixed u v := by
  rw [neutralIV103Prime_finite,neutralIV162Prime_bank]
  unfold neutralIV162PrimeMixed
  apply Finset.sum_congr rfl
  intro n hn
  unfold neutralIV085PrimeSummand neutralIV103Correlation
  rw [neutralIV191Correlation 2 u v hu hv (Real.log n),
    neutralIV191Correlation 2 u v hu hv (-Real.log n)]
  simp only [sub_neg_eq_add]

#print axioms neutralIV162Exp_four_bounds
#print axioms neutralIV162Prime_range
#print axioms neutralIV162Census
#print axioms neutralIV162Prime_bank
#print axioms neutralIV162Prime_count
#print axioms neutralIV191Correlation
#print axioms neutralIV162Prime_literal
end
end WeilDefect
