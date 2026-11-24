import WeilDefect.Arithmetic.ActualZetaIV071GammaFinitePrelude
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open Filter

/-!
IV080 — a direct, elementary linear-growth envelope for the ORIGINAL
source Zeta23.EF.gammaBracket via its existing certified NF599 series.

No alternate gamma multiplier; all inputs are authentic NF599 gains,
original gammaBracket and the IV071 pointwise sum.

The linear bound is weaker than logarithmic growth but sufficient
in principle for the ORIGINAL Weil mixed convolution tests f ⋆ g̃
when each C² compact factor provides a separate quadratic Fourier decay.

This source proves no Fourier decay, no weighted L¹, no signed Weil
positivity and no RH. Frozen original Phase IV source SHA:
165981950e193a8b6ea219f7b31e379db495befa.
-/

/-- Elementary source gain bound from (a-|r|/2)^2 ≥ 0.
Uniform in the frequency and nonzero positive resolvent scale. -/
theorem neutralIV080NF599Gain_linear
    (a r : ℝ) (ha : 0 < a) :
    neutralNF599Gain a r ≤ |r| / (2 * a ^ 2) := by
  let b : ℝ := |r| / 2
  have hb : 0 ≤ b := by dsimp [b]; positivity
  have hb2 : (r / 2) ^ 2 = b ^ 2 := by
    dsimp [b]
    nlinarith [sq_abs r]
  have hAMGM : a * b ≤ a ^ 2 + b ^ 2 := by
    nlinarith [sq_nonneg (a - b)]
  have hden : 0 < a * (a ^ 2 + b ^ 2) := by positivity
  have ha2 : 0 < a ^ 2 := by positivity
  have hcross := mul_le_mul_of_nonneg_left hAMGM
    (mul_nonneg ha.le hb)
  have hrat : b ^ 2 / (a * (a ^ 2 + b ^ 2)) ≤ b / a ^ 2 := by
    apply (div_le_div_iff₀ hden ha2).mpr
    nlinarith [hcross]
  calc
    neutralNF599Gain a r =
        b ^ 2 / (a * (a ^ 2 + b ^ 2)) := by
          unfold neutralNF599Gain
          rw [hb2]
    _ ≤ b / a ^ 2 := hrat
    _ = |r| / (2 * a ^ 2) := by dsimp [b]; ring

/-- Elementary reciprocal-square tail comparison with the exact
telescoping 2*(1/(n+1)-1/(n+2)). -/
theorem neutralIV080TailReciprocal_term (n : ℕ) :
    (1 : ℝ) / (((n : ℝ) + 1 + 1 / 4) ^ 2) ≤
      2 * (1 / ((n : ℝ) + 1) - 1 / ((n : ℝ) + 2)) := by
  have hA : 0 < (((n : ℝ) + 1 + 1 / 4) ^ 2) := by positivity
  have hB : 0 < ((n : ℝ) + 1) * ((n : ℝ) + 2) := by positivity
  have hn : 0 ≤ (n : ℝ) := by positivity
  have hpoly : ((n : ℝ) + 1) * ((n : ℝ) + 2) ≤
      2 * (((n : ℝ) + 1 + 1 / 4) ^ 2) := by
    nlinarith [sq_nonneg (n : ℝ)]
  have hle :
      (1 : ℝ) / (((n : ℝ) + 1 + 1 / 4) ^ 2) ≤
        2 / (((n : ℝ) + 1) * ((n : ℝ) + 2)) := by
    apply (div_le_div_iff₀ hA hB).mpr
    nlinarith [hpoly]
  calc
    _ ≤ 2 / (((n : ℝ) + 1) * ((n : ℝ) + 2)) := hle
    _ = 2 * (1 / ((n : ℝ) + 1) - 1 / ((n : ℝ) + 2)) := by
      have h1 : (n : ℝ) + 1 ≠ 0 := by positivity
      have h2 : (n : ℝ) + 2 ≠ 0 := by positivity
      field_simp [h1, h2]
      ring

/-- Fully finite telescoping tail bound: no infinite-sum interchange. -/
theorem neutralIV080TailReciprocal_partial (N : ℕ) :
    (∑ n ∈ Finset.range N,
        (1 : ℝ) / (((n : ℝ) + 1 + 1 / 4) ^ 2)) ≤ 2 := by
  have hpartial (M : ℕ) :
      (∑ n ∈ Finset.range M,
          (1 : ℝ) / (((n : ℝ) + 1 + 1 / 4) ^ 2)) ≤
        2 * (1 - 1 / ((M : ℝ) + 1)) := by
    induction M with
    | zero => simp
    | succ M ih =>
        rw [Finset.sum_range_succ]
        calc
          _ ≤ 2 * (1 - 1 / ((M : ℝ) + 1)) +
                2 * (1 / ((M : ℝ) + 1) -
                  1 / ((M : ℝ) + 2)) :=
            add_le_add ih (neutralIV080TailReciprocal_term M)
          _ = 2 * (1 - 1 / (((M + 1 : ℕ) : ℝ) + 1)) := by
            push_cast
            ring
  have hfrac : 0 ≤ (1 : ℝ) / ((N : ℝ) + 1) := by positivity
  nlinarith [hpartial N]

/-- The true source-defined NF599 finite Gamma truncation grows
no faster than 9|r| above its authentic gammaBracket 0. -/
theorem neutralIV080GammaFinite_linear
    (N : ℕ) (r : ℝ) :
    neutralIV071GammaFinite N r ≤
      Zeta23.EF.gammaBracket 0 + 9 * |r| := by
  have hquarter : neutralNF599Gain (1 / 4) r ≤ 8 * |r| := by
    have h := neutralIV080NF599Gain_linear (1 / 4) r (by norm_num)
    norm_num at h ⊢
    linarith
  have htail : (∑ n ∈ Finset.range N,
      neutralNF599Gain ((n : ℝ) + 1 + 1 / 4) r) ≤ |r| := by
    have hterm (n : ℕ) :
        neutralNF599Gain ((n : ℝ) + 1 + 1 / 4) r ≤
          (|r| / 2) *
            (1 / (((n : ℝ) + 1 + 1 / 4) ^ 2)) := by
      calc
        _ ≤ |r| / (2 * (((n : ℝ) + 1 + 1 / 4) ^ 2)) :=
          neutralIV080NF599Gain_linear _ r (by positivity)
        _ = (|r| / 2) *
            (1 / (((n : ℝ) + 1 + 1 / 4) ^ 2)) := by ring
    have hsum := Finset.sum_le_sum
      (s := Finset.range N) (fun n _ => hterm n)
    have hpartial := neutralIV080TailReciprocal_partial N
    have hcoef : 0 ≤ |r| / 2 := by positivity
    calc
      (∑ n ∈ Finset.range N,
          neutralNF599Gain ((n : ℝ) + 1 + 1 / 4) r) ≤
        ∑ n ∈ Finset.range N,
          (|r| / 2) *
            (1 / (((n : ℝ) + 1 + 1 / 4) ^ 2)) := hsum
      _ = (|r| / 2) * (∑ n ∈ Finset.range N,
            (1 : ℝ) / (((n : ℝ) + 1 + 1 / 4) ^ 2)) := by
              rw [Finset.mul_sum]
      _ ≤ (|r| / 2) * 2 :=
        mul_le_mul_of_nonneg_left hpartial hcoef
      _ = |r| := by ring
  unfold neutralIV071GammaFinite
  linarith

/-- Original source gammaBracket growth bound, transferred from the
true IV071 pointwise finite approximations (not a fresh digamma axiom). -/
theorem neutralIV080Gamma_linear (r : ℝ) :
    Zeta23.EF.gammaBracket r ≤
      Zeta23.EF.gammaBracket 0 + 9 * |r| := by
  exact le_of_tendsto (neutralIV071GammaFinite_tendsto r)
    (Filter.Eventually.of_forall (fun N =>
      neutralIV080GammaFinite_linear N r))

/-- Global original source Gamma absolute bound. In contrast to the
DCT envelope previously assumed, this is a prospective *proved*
source growth estimate and reduces the target to first Fourier moment. -/
theorem neutralIV080Gamma_abs_linear (r : ℝ) :
    |Zeta23.EF.gammaBracket r| ≤
      |Zeta23.EF.gammaBracket 0| + 9 * |r| := by
  have hlow : Zeta23.EF.gammaBracket 0 ≤
      Zeta23.EF.gammaBracket r := by
    have h := neutralNF599GammaLower_partial r 0
    simp only [Finset.range_zero, Finset.sum_empty, add_zero] at h
    have hn := neutralNF599Gain_nonneg (1 / 4) r (by norm_num)
    linarith
  have hhigh := neutralIV080Gamma_linear r
  apply abs_le.mpr
  constructor
  · have h := neg_abs_le (Zeta23.EF.gammaBracket 0)
    have hs : 0 ≤ 9 * |r| := by positivity
    linarith
  · have h := le_abs_self (Zeta23.EF.gammaBracket 0)
    linarith

#print axioms neutralIV080NF599Gain_linear
#print axioms neutralIV080TailReciprocal_term
#print axioms neutralIV080TailReciprocal_partial
#print axioms neutralIV080GammaFinite_linear
#print axioms neutralIV080Gamma_linear
#print axioms neutralIV080Gamma_abs_linear

end
end WeilDefect
