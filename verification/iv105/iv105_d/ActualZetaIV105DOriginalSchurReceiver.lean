import WeilDefect.Arithmetic.ActualZetaIV105COriginalProjectedPhysicalResponse
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

theorem neutralIV105DPacked_add (k : ℕ) (hk : 0 < k) (c d : Fin k → ℂ) :
    neutralIV100Packed k hk (c+d) =
      neutralIV100Packed k hk c + neutralIV100Packed k hk d := by
  simp only [neutralIV100Packed, neutralIV099Sector, Pi.add_apply,
    add_smul, Finset.sum_add_distrib]

theorem neutralIV105DPacked_neg (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) :
    neutralIV100Packed k hk (-c) = -neutralIV100Packed k hk c := by
  simp only [neutralIV100Packed, neutralIV099Sector, Pi.neg_apply,
    neg_smul, Finset.sum_neg_distrib]

theorem neutralIV105DQ_zero (a : ℝ) : neutralIV101Q a 0 = 0 := by
  have h := neutralIV101Q_add a 0 0 (by simp) (by simp)
  simp only [zero_add] at h
  change neutralIV101Q a 0 = neutralIV101Q a 0 + 2 * neutralIV101Q a 0 +
    neutralIV101Q a 0 at h
  linarith

/-- Exact completion with a solved packed response; no assumed inverse norm.
The solve equation is explicitly required on the entire packed sector. -/
theorem neutralIV105DComplete_square (k : ℕ) (hk : 0 < k)
    (c d : Fin k → ℂ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (hsolve : ∀ e : Fin k → ℂ,
      (neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk e) v).re =
      (neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk e)
        (neutralIV100Packed k hk d)).re) :
    neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk c + v) =
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (c+d)) +
        neutralIV101Q (11/10:ℝ) v -
        neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk d) := by
  have hc := neutralIV009OriginalCollars_supported_window
    (neutralIV100Packed k hk c) (neutralIV101Packed_collars k hk c)
  have hd := neutralIV009OriginalCollars_supported_window
    (neutralIV100Packed k hk d) (neutralIV101Packed_collars k hk d)
  rw [neutralIV105DPacked_add, neutralIV101Q_add _ _ v hc hv,
    neutralIV101Q_add _ _ _ hc hd, hsolve c]
  ring

/-- Equivalence on the original supported smooth core conditional only
on the exact packed solve supplied by d. Positivity of the packed
block is inherited from IV101, not postulated here. -/
theorem neutralIV105DWindow_nonneg_iff (k : ℕ) (hk : 0 < k)
    (d : 𝓢(ℝ,ℂ) → Fin k → ℂ)
    (hsolve : ∀ (v : 𝓢(ℝ,ℂ)),
      neutralIV101MassComplement k hk v →
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) →
      ∀ e : Fin k → ℂ,
        (neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk e) v).re =
        (neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk e)
          (neutralIV100Packed k hk (d v))).re) :
    (∀ s : 𝓢(ℝ,ℂ),
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0) →
      0 ≤ neutralIV101Q (11/10:ℝ) s) ↔
    (∀ v : 𝓢(ℝ,ℂ), neutralIV101MassComplement k hk v →
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) →
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (d v)) ≤
        neutralIV101Q (11/10:ℝ) v) := by
  constructor
  · intro h v ho hv
    have hwin := neutralIV009OriginalCollars_supported_window
      (neutralIV100Packed k hk (-d v)) (neutralIV101Packed_collars k hk (-d v))
    have hp : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
        (neutralIV100Packed k hk (-d v) + v) x = 0 := by
      intro x hx
      change neutralIV100Packed k hk (-d v) x + v x = 0
      rw [hwin x hx, hv x hx, add_zero]
    have hn := h _ hp
    rw [neutralIV105DComplete_square k hk (-d v) (d v) v hv (hsolve v ho hv),
      neg_add_cancel] at hn
    have hz : neutralIV100Packed k hk (0 : Fin k → ℂ) = 0 := by
      simp [neutralIV100Packed, neutralIV099Sector]
    rw [hz, neutralIV105DQ_zero, zero_add] at hn
    exact sub_nonneg.mp hn
  · intro h s hs
    let v := neutralIV104Residual k hk s
    have hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0 :=
      neutralIV104Residual_supported k hk s hs
    have ho : neutralIV101MassComplement k hk v :=
      neutralIV104Residual_orthogonal k hk s
    let c := neutralIV104Coefficient k hk s
    have hd : neutralIV100Packed k hk c + v = s :=
      neutralIV104Decomposition k hk s
    rw [← hd, neutralIV105DComplete_square k hk c (d v) v hv (hsolve v ho hv)]
    have hm := neutralIV101Packed_full_margin k hk (c+d v)
    have hp : 0 ≤ neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (c+d v)) :=
      le_trans (by positivity) hm
    linarith [h v ho hv]

#print axioms neutralIV105DPacked_add
#print axioms neutralIV105DPacked_neg
#print axioms neutralIV105DQ_zero
#print axioms neutralIV105DComplete_square
#print axioms neutralIV105DWindow_nonneg_iff
end
end WeilDefect
