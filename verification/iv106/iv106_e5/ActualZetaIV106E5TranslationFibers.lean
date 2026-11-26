import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped BigOperators

/-- Exact folding of an interval into equal translation cells.
No divisibility or periodicity assumption is used. -/
theorem neutralIV106E5Fold (f : ℝ → ℝ) (hf : Continuous f)
    (l s : ℝ) (m : ℕ) :
    (∫ x in (0:ℝ)..s, ∑ j ∈ Finset.range m, f (x+(l+(j:ℝ)*s))) =
      ∫ x in l..(l+(m:ℝ)*s), f x := by
  rw [intervalIntegral.integral_finsetSum]
  · simp_rw [intervalIntegral.integral_comp_add_right, zero_add]
    have h := intervalIntegral.sum_integral_adjacent_intervals
      (a := fun j : ℕ => l+(j:ℝ)*s) (n := m)
      (f := f) (μ := volume)
      (fun j _ => hf.intervalIntegrable (μ := volume) _ _)
    simp only [Nat.cast_zero, zero_mul, add_zero] at h
    convert h using 1
    apply Finset.sum_congr rfl
    intro j hj
    congr 1
    push_cast
    ring
  · intro j hj
    exact (hf.comp (continuous_id.add continuous_const)).intervalIntegrable
      (μ := volume) _ _

/-- A function vanishing outside a closed window has its full integral
on that window, including when it is padded to a larger interval. -/
theorem neutralIV106E5Padded_integral (f : ℝ → ℝ) (l b r : ℝ)
    (hlb : l ≤ b) (hbr : b ≤ r)
    (hf : ∀ x ∉ Set.Icc l b, f x = 0) :
    (∫ x in l..r, f x) = ∫ x : ℝ, f x := by
  rw [intervalIntegral.integral_of_le (hlb.trans hbr),
    ← integral_Icc_eq_integral_Ioc, ← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [] with x
  by_cases hx : x ∈ Set.Icc l r
  · simp [hx]
  · have hy : x ∉ Set.Icc l b := fun h => hx ⟨h.1,h.2.trans hbr⟩
    simp [hx,hf x hy]

/-- Full physical mass is the integral of the squared sample-vector mass. -/
theorem neutralIV106E5Mass (v : ℝ → ℂ) (hv : Continuous v)
    (l b s : ℝ) (m : ℕ) (hlb : l ≤ b) (hb : b ≤ l+(m:ℝ)*s)
    (hout : ∀ x ∉ Set.Icc l b, v x = 0) :
    (∫ t in (0:ℝ)..s, ∑ j ∈ Finset.range m,
      ‖v (t+(l+(j:ℝ)*s))‖^2) = ∫ x : ℝ, ‖v x‖^2 := by
  rw [neutralIV106E5Fold (fun x : ℝ => ‖v x‖^2) (by fun_prop) l s m]
  apply neutralIV106E5Padded_integral _ l b _ hlb hb
  intro x hx
  simp [hout x hx]

/-- Physical positive-lag correlation folds into the same sample coordinates. -/
theorem neutralIV106E5Shift (v : ℝ → ℂ) (hv : Continuous v)
    (l b s : ℝ) (m r : ℕ) (hlb : l ≤ b) (hb : b ≤ l+(m:ℝ)*s)
    (hout : ∀ x ∉ Set.Icc l b, v x = 0) :
    (∫ t in (0:ℝ)..s, ∑ j ∈ Finset.range m,
      (star (v (t+(l+(j:ℝ)*s)))*v (t+(l+((j+r:ℕ):ℝ)*s))).re) =
      ∫ x : ℝ, (star (v x)*v (x+(r:ℝ)*s)).re := by
  let f : ℝ → ℝ := fun x => (star (v x)*v (x+(r:ℝ)*s)).re
  have hf : Continuous f := by
    dsimp [f]
    exact Complex.continuous_re.comp
      (hv.star.mul (hv.comp (continuous_id.add continuous_const)))
  calc
    _ = ∫ t in (0:ℝ)..s, ∑ j ∈ Finset.range m, f (t+(l+(j:ℝ)*s)) := by
      apply intervalIntegral.integral_congr
      intro t ht
      apply Finset.sum_congr rfl
      intro j hj
      dsimp [f]
      congr 2
      push_cast
      ring
    _ = ∫ x in l..(l+(m:ℝ)*s), f x := neutralIV106E5Fold f hf l s m
    _ = _ := by
      apply neutralIV106E5Padded_integral f l b _ hlb hb
      intro x hx
      simp [f,hout x hx]

/-- Samples beyond the end of a padded chain vanish on the open fiber.
The open fiber avoids imposing an unnecessary boundary point condition. -/
theorem neutralIV106E5Outside (v : ℝ → ℂ) (l b s t : ℝ)
    (m j : ℕ) (hs : 0 < s) (ht : 0 < t)
    (hb : b ≤ l+(m:ℝ)*s) (hj : m ≤ j)
    (hout : ∀ x ∉ Set.Icc l b, v x = 0) :
    v (t+(l+(j:ℝ)*s)) = 0 := by
  apply hout
  intro hx
  have hj' : (m:ℝ) ≤ j := by exact_mod_cast hj
  have hmul := mul_le_mul_of_nonneg_right hj' hs.le
  linarith [hx.2]

/-- Drop out-of-range lag entries without changing the integrated correlation. -/
theorem neutralIV106E5Truncate (v : ℝ → ℂ) (l b s : ℝ) (m r : ℕ)
    (hs : 0 < s) (hb : b ≤ l+(m:ℝ)*s)
    (hout : ∀ x ∉ Set.Icc l b, v x = 0) :
    (∫ t in (0:ℝ)..s, ∑ j ∈ Finset.range m,
      (star (v (t+(l+(j:ℝ)*s)))*v (t+(l+((j+r:ℕ):ℝ)*s))).re) =
    ∫ t in (0:ℝ)..s, ∑ j ∈ Finset.range m,
      if j+r < m then
        (star (v (t+(l+(j:ℝ)*s)))*v (t+(l+((j+r:ℕ):ℝ)*s))).re
      else 0 := by
  apply intervalIntegral.integral_congr_Ioo_of_le hs.le
  intro t ht
  apply Finset.sum_congr rfl
  intro j hj
  by_cases h : j+r < m
  · simp [h]
  · rw [if_neg h, neutralIV106E5Outside v l b s t m (j+r)
      hs ht.1 hb (Nat.le_of_not_lt h) hout]
    simp

#print axioms neutralIV106E5Fold
#print axioms neutralIV106E5Padded_integral
#print axioms neutralIV106E5Mass
#print axioms neutralIV106E5Shift
#print axioms neutralIV106E5Outside
#print axioms neutralIV106E5Truncate
end
end WeilDefect
