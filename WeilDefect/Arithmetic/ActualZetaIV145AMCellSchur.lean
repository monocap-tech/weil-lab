import Mathlib

namespace WeilDefect
noncomputable section
open scoped BigOperators

/-- Cell geometry after shifting the origin from -2 to 0.
The translated point lies in the union of two adjacent cells.
This is a scalar lemma, not the actual zero-extension attachment. -/
theorem neutralIV145TranslatedCell {x s delta : ℝ} {i j : ℤ}
    (hxlo : (i:ℝ)*delta ≤ x)
    (hxhi : x < ((i:ℝ)+1)*delta)
    (hslo : (j:ℝ)*delta ≤ s)
    (hshi : s < ((j:ℝ)+1)*delta) :
    ((i:ℝ)+(j:ℝ))*delta ≤ x+s ∧
      x+s < ((i:ℝ)+(j:ℝ)+2)*delta := by
  constructor <;> linarith [hxlo, hxhi, hslo, hshi]

/-- Sum the pointwise envelope against nonnegative translation weights. -/
theorem neutralIV145Row_cap {ι : Type*} [Fintype ι]
    (a u b c : ι → ℝ)
    (ha : ∀ s, 0 ≤ a s) (hc : ∀ s, 0 ≤ c s)
    (hbc : ∀ s, b s ≤ c s) (hau : ∀ s, a s ≤ u s) :
    (∑ s, a s * b s) ≤ ∑ s, u s * c s := by
  classical
  apply Finset.sum_le_sum
  intro s _
  calc
    a s * b s ≤ a s * c s := mul_le_mul_of_nonneg_left (hbc s) (ha s)
    _ ≤ u s * c s := mul_le_mul_of_nonneg_right (hau s) (hc s)

/-- The exact integer AM row inequality, after coercion to reals,
pays the strict pointwise ratio. The actual array is a separate input. -/
theorem neutralIV145Row_ratio {r W h : ℝ}
    (hW : 0 < W) (hh : 0 < h)
    (hr : 50*r < 399*W*h) :
    r/(W*h) < (399/50:ℝ) := by
  apply (div_lt_iff₀ (mul_pos hW hh)).2
  linarith [hr]

/-- Algebraic weighted Young inequality with denominators cleared.
This is valid even without positivity; the division step needs positive p,q. -/
theorem neutralIV145WeightedYoung_cleared (a b p q : ℝ) :
    2*a*b*p*q ≤ a^2*q^2+b^2*p^2 := by
  nlinarith [sq_nonneg (a*q-b*p)]

theorem neutralIV145WeightedYoung (a b p q : ℝ)
    (hp : 0 < p) (hq : 0 < q) :
    2*a*b ≤ a^2*q/p+b^2*p/q := by
  apply (mul_le_mul_right₀ (mul_pos hp hq)).mp
  calc
    (2*a*b)*(p*q) ≤ a^2*q^2+b^2*p^2 := by
      nlinarith [neutralIV145WeightedYoung_cleared a b p q]
    _ = (a^2*q/p+b^2*p/q)*(p*q) := by
      field_simp [ne_of_gt hp, ne_of_gt hq] <;> ring

#print axioms neutralIV145TranslatedCell
#print axioms neutralIV145Row_cap
#print axioms neutralIV145Row_ratio
#print axioms neutralIV145WeightedYoung_cleared
#print axioms neutralIV145WeightedYoung

end
end WeilDefect
