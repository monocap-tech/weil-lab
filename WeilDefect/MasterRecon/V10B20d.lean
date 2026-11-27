import WeilDefect.MasterRecon.V10B20c
import Mathlib.Analysis.SpecialFunctions.Gamma.Beta
import Mathlib.Analysis.Calculus.Deriv.Inv

/-! Right endpoint moments: finite rational beta product jets.
Differentiation under the beta integral is explicitly left to the
subsequent attachment; the product algebra is independent. -/
namespace WeilDefect.MasterRecon.V10B20d

open MeasureTheory
open scoped BigOperators
open V10B20b (H H₂)

noncomputable def P (n : ℕ) (s : ℝ) : ℝ :=
  ∏ j ∈ Finset.range n, ((j:ℝ)+1)/((j:ℝ)+1+s)

noncomputable def U (n : ℕ) (s : ℝ) : ℝ :=
  ∑ j ∈ Finset.range n, 1/((j:ℝ)+1+s)

noncomputable def W (n : ℕ) (s : ℝ) : ℝ :=
  ∑ j ∈ Finset.range n, 1/((j:ℝ)+1+s)^2

noncomputable def D (n : ℕ) (s : ℝ) : ℝ := -P n s*U n s

theorem denom_pos (j : ℕ) (s : ℝ) (hs : -1 < s) :
    0 < (j:ℝ)+1+s := by linarith [Nat.cast_nonneg (α := ℝ) j]

theorem P_zero (n : ℕ) : P n 0 = 1 := by
  unfold P
  simp only [add_zero]
  apply Finset.prod_eq_one
  intro j _
  exact div_self (by positivity)

theorem factor_deriv (j : ℕ) (s : ℝ) (hs : -1 < s) :
    HasDerivAt (fun x : ℝ => ((j:ℝ)+1)/((j:ℝ)+1+x))
      (-((j:ℝ)+1)/((j:ℝ)+1+s)^2) s := by
  have h := (hasDerivAt_const s ((j:ℝ)+1)).div
    ((hasDerivAt_const s ((j:ℝ)+1)).add (hasDerivAt_id s)) (denom_pos j s hs).ne'
  convert h using 1
  ring

theorem P_deriv (n : ℕ) (s : ℝ) (hs : -1 < s) :
    HasDerivAt (P n) (D n s) s := by
  induction n with
  | zero => simpa [P,D,U] using hasDerivAt_const s (1:ℝ)
  | succ j ih =>
    have h := ih.mul (factor_deriv j s hs)
    have he : P (j+1) = fun x => P j x * (((j:ℝ)+1)/((j:ℝ)+1+x)) := by
      funext x
      exact Finset.prod_range_succ _ _
    rw [he]
    convert h using 1
    unfold D U
    rw [he,Finset.sum_range_succ]
    field_simp [(denom_pos j s hs).ne']
    <;> ring

theorem U_deriv (n : ℕ) (s : ℝ) (hs : -1 < s) :
    HasDerivAt (U n) (-W n s) s := by
  induction n with
  | zero => simpa [U,W] using hasDerivAt_const s (0:ℝ)
  | succ j ih =>
    have h := (hasDerivAt_const s (1:ℝ)).div
      ((hasDerivAt_const s ((j:ℝ)+1)).add (hasDerivAt_id s)) (denom_pos j s hs).ne'
    have he : U (j+1) = fun x => U j x+1/((j:ℝ)+1+x) := by
      funext x
      exact Finset.sum_range_succ _ _
    rw [he]
    convert ih.add h using 1
    unfold W
    rw [Finset.sum_range_succ]
    ring

theorem D_deriv (n : ℕ) (s : ℝ) (hs : -1 < s) :
    HasDerivAt (D n) (P n s*((U n s)^2+W n s)) s := by
  have h := (P_deriv n s hs).neg.mul (U_deriv n s hs)
  convert h using 1
  unfold D
  ring

theorem beta_product_jets (n : ℕ) :
    HasDerivAt (P n) (-H n) 0 ∧
    HasDerivAt (D n) ((H n)^2+H₂ n) 0 := by
  have hu : U n 0 = H n := by simp [U,H]
  have hw : W n 0 = H₂ n := by simp [W,H₂]
  constructor
  · have h := P_deriv n 0 (by norm_num)
    simpa only [D,P_zero,hu,neg_one_mul] using h
  · have h := D_deriv n 0 (by norm_num)
    simpa only [P_zero,hu,hw,one_mul] using h

theorem beta_product_scaled (k : ℕ) (s : ℝ) (hs : -1 < s) :
    Complex.betaIntegral (1+(s:ℂ)) ((k:ℂ)+1) =
      ((P (k+1) s/((k:ℝ)+1):ℝ):ℂ) := by
  have hpos : 0 < (1+(s:ℂ)).re := by simp; linarith
  rw [Complex.betaIntegral_eval_nat_add_one_right hpos k]
  push_cast
  unfold P
  rw [Finset.prod_div_distrib]
  have he : (∏ j ∈ Finset.range (k+1), ((j:ℂ)+1)) =
      ((k+1).factorial:ℂ) := by
    rw [Nat.factorial_eq_prod_range_add_one]
    push_cast
    rfl
  rw [he,Nat.factorial_succ]
  push_cast
  have hk : (k:ℂ)+1 ≠ 0 := by exact_mod_cast (show (k:ℝ)+1 ≠ 0 by positivity)
  have hd : (∏ j ∈ Finset.range (k+1), ((j:ℂ)+1+(s:ℂ))) ≠ 0 := by
    apply Finset.prod_ne_zero_iff.mpr
    intro j _
    exact_mod_cast (denom_pos j s hs).ne'
  have hden : (∏ j ∈ Finset.range (k+1), (1+(s:ℂ)+j)) =
      ∏ j ∈ Finset.range (k+1), ((j:ℂ)+1+(s:ℂ)) := by
    apply Finset.prod_congr rfl
    intro j _
    ring
  rw [hden]
  field_simp [hk,hd]
  <;> ring

end WeilDefect.MasterRecon.V10B20d

#print axioms WeilDefect.MasterRecon.V10B20d.denom_pos
#print axioms WeilDefect.MasterRecon.V10B20d.P_zero
#print axioms WeilDefect.MasterRecon.V10B20d.factor_deriv
#print axioms WeilDefect.MasterRecon.V10B20d.P_deriv
#print axioms WeilDefect.MasterRecon.V10B20d.U_deriv
#print axioms WeilDefect.MasterRecon.V10B20d.D_deriv
#print axioms WeilDefect.MasterRecon.V10B20d.beta_product_jets
#print axioms WeilDefect.MasterRecon.V10B20d.beta_product_scaled
