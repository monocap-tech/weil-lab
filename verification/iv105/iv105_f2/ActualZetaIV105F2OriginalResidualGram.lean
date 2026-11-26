import WeilDefect.Arithmetic.ActualZetaIV105F1OriginalTrialReceiver
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- Residual in the original signed matrix coordinates; no chosen exact
solve occurs in this definition. -/
def neutralIV105F2Residual (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ)) (t : Fin k → ℂ) (i : Fin k) : ℂ :=
  neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v -
    neutralIV105EGram k hk t i

/-- Physical Riesz vector for the residual, using the actual diagonal mass. -/
def neutralIV105F2Dual (k : ℕ) (hk : 0 < k)
    (δ : Fin k → ℂ) : RealComplexL2 :=
  (neutralIV100Packed k hk (fun i => δ i / (neutralIV104Mass k hk i : ℂ))).toLp 2 volume

theorem neutralIV105F2Dual_row (k : ℕ) (hk : 0 < k)
    (δ : Fin k → ℂ) (i : Fin k) :
    inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
      (neutralIV105F2Dual k hk δ) = δ i := by
  unfold neutralIV105F2Dual
  rw [neutralIV104Packed_pair]
  have hm : 0 < neutralIV104Mass k hk i := neutralIV100Carrier_mass_pos k hk i
  exact div_mul_cancel₀ _ (Complex.ofReal_ne_zero.mpr hm.ne')

theorem neutralIV105F2Dual_pair (k : ℕ) (hk : 0 < k)
    (c δ : Fin k → ℂ) :
    inner ℂ ((neutralIV100Packed k hk c).toLp 2 volume)
      (neutralIV105F2Dual k hk δ) =
      ∑ i : Fin k, conj (c i) * δ i := by
  rw [neutralIV104Packed_toLp, sum_inner]
  apply Finset.sum_congr rfl
  intro i hi
  rw [inner_smul_left, neutralIV105F2Dual_row]

/-- Exact finite expression for squared dual mass. This expression is
the real part of the diagonal inverse Gram quadratic form. -/
theorem neutralIV105F2Dual_norm_sq (k : ℕ) (hk : 0 < k) (δ : Fin k → ℂ) :
    ‖neutralIV105F2Dual k hk δ‖^2 =
      (∑ i : Fin k, conj (δ i / (neutralIV104Mass k hk i : ℂ)) * δ i).re := by
  let z := neutralIV105F2Dual k hk δ
  have h : inner ℂ z z =
      ∑ i : Fin k, conj (δ i / (neutralIV104Mass k hk i : ℂ)) * δ i :=
    neutralIV105F2Dual_pair k hk _ δ
  rw [inner_self_eq_norm_sq_to_K] at h
  have hr := congrArg Complex.re h
  simpa only [← Complex.ofReal_pow, Complex.ofReal_re] using hr

theorem neutralIV105F2Residual_eq (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ)) (t : Fin k → ℂ) :
    neutralIV105EGram k hk (neutralIV105E2Solve k hk v-t) =
      neutralIV105F2Residual k hk v t := by
  rw [map_sub, neutralIV105E2Solve_eq]
  rfl

/-- The error energy is the exact physical residual pairing. -/
theorem neutralIV105F2Error_energy (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ)) (t : Fin k → ℂ) :
    neutralIV101Q (11/10:ℝ)
        (neutralIV100Packed k hk (neutralIV105E2Solve k hk v-t)) =
      (inner ℂ
        ((neutralIV100Packed k hk (neutralIV105E2Solve k hk v-t)).toLp 2 volume)
        (neutralIV105F2Dual k hk (neutralIV105F2Residual k hk v t))).re := by
  rw [neutralIV105F2Dual_pair, ← neutralIV105F2Residual_eq k hk v t,
    neutralIV105EGram_energy]

/-- The trial bound now has no unknown exact-error premise. -/
theorem neutralIV105F2Trial_upper (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ)) (t : Fin k → ℂ)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (neutralIV105E2Solve k hk v)) ≤
      2*(neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk t) v).re -
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk t) +
      (5/2:ℝ)*(∑ i : Fin k,
        conj (neutralIV105F2Residual k hk v t i / (neutralIV104Mass k hk i : ℂ)) *
          neutralIV105F2Residual k hk v t i).re := by
  let η := ‖neutralIV105F2Dual k hk (neutralIV105F2Residual k hk v t)‖
  have hr : neutralIV101Q (11/10:ℝ)
      (neutralIV100Packed k hk (neutralIV105E2Solve k hk v-t)) ≤
        η * ‖(neutralIV100Packed k hk (neutralIV105E2Solve k hk v-t)).toLp 2 volume‖ := by
    rw [neutralIV105F2Error_energy]
    dsimp [η]
    rw [mul_comm]
    exact re_inner_le_norm _ _
  have h := neutralIV105FTrial_upper k hk v t η hv hr
  dsimp [η] at h
  rw [neutralIV105F2Dual_norm_sq] at h
  exact h

#print axioms neutralIV105F2Dual_row
#print axioms neutralIV105F2Dual_pair
#print axioms neutralIV105F2Dual_norm_sq
#print axioms neutralIV105F2Residual_eq
#print axioms neutralIV105F2Error_energy
#print axioms neutralIV105F2Trial_upper
end
end WeilDefect
