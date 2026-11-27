import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Topology.Algebra.InfiniteSum.Order

/-! V10B32b: positive normalized pole-load coefficient reserve.
The literal Legendre expansion and termwise spherical series comparison
are independent inputs. This receiver accounts for normalization of
both numerator and denominator, not only the omitted outer modes. -/
namespace WeilDefect.MasterRecon.V10B32b

open scoped BigOperators

theorem ratio_bound (j : ℕ) (hj : 15 ≤ j) (a b : ℝ)
    (ha : 0 < a) (hb : 0 ≤ b) (hba : b ≤ a) :
    (1/(64*(2*(j:ℝ)+1)*(2*(j:ℝ)+3)))*(b/a) ≤ 1/65000 := by
  have h₁ : (31:ℝ) ≤ 2*(j:ℝ)+1 := by exact_mod_cast (show 31 ≤ 2*j+1 by omega)
  have h₂ : (33:ℝ) ≤ 2*(j:ℝ)+3 := by exact_mod_cast (show 33 ≤ 2*j+3 by omega)
  have hden : (65000:ℝ) ≤ 64*(2*(j:ℝ)+1)*(2*(j:ℝ)+3) := by
    have h := mul_le_mul h₁ h₂ (by norm_num) (by linarith)
    nlinarith only [h]
  have hd : 0 < 64*(2*(j:ℝ)+1)*(2*(j:ℝ)+3) := by positivity
  have hq : b/a ≤ 1 := (div_le_one ha).mpr hba
  calc
    _ ≤ 1/(64*(2*(j:ℝ)+1)*(2*(j:ℝ)+3)) :=
      mul_le_of_le_one_right (by positivity) hq
    _ ≤ _ := one_div_le_one_div_of_le (by norm_num) hden

theorem geometric_coeff (c : ℕ → ℝ) (ρ : ℝ) (hρ : 0 ≤ ρ)
    (h0 : c 0 ≤ 1) (hstep : ∀ k, c (k+1) ≤ ρ*c k) (k : ℕ) :
    c k ≤ ρ^k := by
  induction k with
  | zero => simpa using h0
  | succ k ih =>
    rw [pow_succ,mul_comm (ρ^k) ρ]
    exact (hstep k).trans (mul_le_mul_of_nonneg_left ih hρ)

theorem outer_tail (c : ℕ → ℝ) (ρ : ℝ) (hρ : 0 ≤ ρ) (hρ1 : ρ < 1)
    (hn : ∀ k, 0 ≤ c k) (h0 : c 0 ≤ 1)
    (hstep : ∀ k, c (k+1) ≤ ρ*c k) (m : ℕ) :
    (∑' k : ℕ, c (m+k)) ≤ ρ^m/(1-ρ) := by
  have hg := (hasSum_geometric_of_norm_lt_one (show ‖ρ‖<1 by
    simpa only [Real.norm_eq_abs,abs_of_nonneg hρ] using hρ1)).mul_left (ρ^m)
  have hb (k : ℕ) : c (m+k) ≤ ρ^m*ρ^k := by
    rw [← pow_add]
    exact geometric_coeff c ρ hρ h0 hstep _
  have hs : Summable (fun k : ℕ => c (m+k)) :=
    Summable.of_nonneg_of_le (fun k => hn _) hb hg.summable
  have hh := hs.tsum_le_tsum hb hg.summable
  rw [hg.tsum_eq] at hh
  simpa only [div_eq_mul_inv] using hh

theorem normalization_error (a b a' b' ε : ℝ)
    (ha : 0 ≤ a') (hb : 0 < b')
    (hε : 0 ≤ ε)
    (ha₁ : a' ≤ a) (ha₂ : a ≤ (1+ε)*a')
    (hb₁ : b' ≤ b) (hb₂ : b ≤ (1+ε)*b') :
    |a/b-a'/b'| ≤ ε*(a'/b') := by
  have hbp : 0 < b := hb.trans_le hb₁
  have hq : 0 ≤ a'/b' := div_nonneg ha hb.le
  have hlo : a'/b' - ε*(a'/b') ≤ a/b := by
    apply (le_div_iff₀ hbp).mpr
    have hcross : a'*b ≤ a'*((1+ε)*b') := mul_le_mul_of_nonneg_left hb₂ ha
    have he : 0 ≤ ε*a'*b := by positivity
    have he' := mul_le_mul_of_nonneg_left hb₁ (show 0 ≤ ε*a' by positivity)
    field_simp [hb.ne']
    nlinarith only [hcross,he',ha₁,mul_le_mul_of_nonneg_right ha₁ hb.le]
  have hhi : a/b ≤ a'/b'+ε*(a'/b') := by
    calc
      _ ≤ a/b' := div_le_div_of_nonneg_left (ha.trans ha₁) hb hb₁
      _ ≤ ((1+ε)*a')/b' := div_le_div_of_nonneg_right ha₂ hb.le
      _ = _ := by ring
  exact abs_le.mpr ⟨by linarith,by linarith⟩

theorem frozen_ratio_tail :
    (1/65000:ℝ)^10/(1-1/65000) < 1/(10:ℝ)^25 := by norm_num

end WeilDefect.MasterRecon.V10B32b

#print axioms WeilDefect.MasterRecon.V10B32b.ratio_bound
#print axioms WeilDefect.MasterRecon.V10B32b.geometric_coeff
#print axioms WeilDefect.MasterRecon.V10B32b.outer_tail
#print axioms WeilDefect.MasterRecon.V10B32b.normalization_error
#print axioms WeilDefect.MasterRecon.V10B32b.frozen_ratio_tail
