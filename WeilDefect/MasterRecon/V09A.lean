import WeilDefect.MasterRecon.V08K
import Mathlib.Analysis.Complex.JensenFormula

/-! V09A: Jensen receiver for uniqueness under superlinear distinct
zero density. The density of actual critical-line zeta zeros is NOT
assumed proved here. -/
namespace WeilDefect.MasterRecon.V09A

open Set Metric MeromorphicOn
open scoped BigOperators

theorem divisor_one_le_at_zero (F : ℂ → ℂ)
    (hF : ∀ z, AnalyticAt ℂ F z) (c z : ℂ) (hc : F c ≠ 0)
    (r : ℝ) (hz : z ∈ closedBall c r) (hz0 : F z = 0) :
    1 ≤ divisor F (closedBall c r) z := by
  have ha : AnalyticOnNhd ℂ F (closedBall c r) := fun x _ => hF x
  have ht : analyticOrderAt F z ≠ ⊤ := by
    intro h
    have he := (analyticOrderAt_eq_top_iff_eq_zero z hF).mp h
    exact hc (by rw [he]; rfl)
  obtain ⟨n, hn⟩ := ENat.ne_top_iff_exists.mp ht
  have hn0 : n ≠ 0 := by
    intro h
    have horder : analyticOrderAt F z = 0 := by rw [← hn, h]; simp
    exact ((hF z).analyticOrderAt_eq_zero.mp horder) hz0
  rw [ha.divisor_apply hz, ← hn]
  have hp : 1 ≤ n := Nat.one_le_iff_ne_zero.mpr hn0
  simpa using (show (1 : ℤ) ≤ (n : ℤ) by exact_mod_cast hp)

theorem distinct_zeros_le_divisor_sum (F : ℂ → ℂ)
    (hF : ∀ z, AnalyticAt ℂ F z) (c : ℂ) (hc : F c ≠ 0)
    (r : ℝ) (S : Finset ℂ)
    (hs : ∀ z ∈ S, z ∈ closedBall c r ∧ F z = 0) :
    (S.card : ℤ) ≤ ∑ᶠ u, divisor F (closedBall c r) u := by
  classical
  let D := divisor F (closedBall c r)
  have hD : (Function.support D).Finite := D.finiteSupport (isCompact_closedBall c r)
  have hnon : ∀ z, 0 ≤ D z :=
    (show AnalyticOnNhd ℂ F (closedBall c r) from fun x _ => hF x).divisor_nonneg
  have hle : ∀ z ∈ S, 1 ≤ D z := fun z hz =>
    divisor_one_le_at_zero F hF c z hc r (hs z hz).1 (hs z hz).2
  have hsub : S ⊆ hD.toFinset := by
    intro z hz
    apply Set.Finite.mem_toFinset.mpr
    exact ne_of_gt (lt_of_lt_of_le (by norm_num) (hle z hz))
  change (S.card : ℤ) ≤ ∑ᶠ u, D u
  rw [finsum_eq_sum_of_support_subset D (s := hD.toFinset) (by simp)]
  calc
    (S.card : ℤ) = ∑ z ∈ S, (1 : ℤ) := by simp
    _ ≤ ∑ z ∈ S, D z := Finset.sum_le_sum hle
    _ ≤ ∑ z ∈ hD.toFinset, D z :=
      Finset.sum_le_sum_of_subset_of_nonneg hsub (fun z _ _ => hnon z)

theorem distinct_zeros_jensen (F : ℂ → ℂ)
    (hF : ∀ z, AnalyticAt ℂ F z) (c : ℂ) (hc : F c ≠ 0)
    (r M : ℝ) (hr : 0 < r) (hM : 1 ≤ M)
    (hb : ∀ z ∈ sphere c (2 * r), ‖F z‖ ≤ M)
    (S : Finset ℂ) (hs : ∀ z ∈ S, z ∈ closedBall c r ∧ F z = 0) :
    (S.card : ℝ) ≤ Real.log (M / ‖F c‖) / Real.log 2 := by
  have hd := distinct_zeros_le_divisor_sum F hF c hc r S hs
  have hj := AnalyticOnNhd.sum_divisor_le (f := F) (c := c) (r := r) (R := 2 * r)
    (M := M) (by simpa [abs_of_pos hr] using hr)
    (by rw [abs_of_pos hr, abs_of_pos (by positivity : 0 < 2 * r)]; linarith)
    hM (fun z _ => hF z) hc (by simpa [abs_of_pos (by positivity : 0 < 2 * r)] using hb)
  rw [abs_of_pos hr, show 2 * r / r = 2 by field_simp [hr.ne']] at hj
  exact (show (S.card : ℝ) ≤ ((∑ᶠ u, divisor F (closedBall c r) u : ℤ) : ℝ) by
    exact_mod_cast hd).trans hj

/-- Entire functions of exponential type have a linear upper bound
on the number of DISTINCT zeros in each disk centered at a nonzero value. -/
theorem exponential_type_linear_count (F : ℂ → ℂ)
    (hF : ∀ z, AnalyticAt ℂ F z) (A B : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B)
    (hg : ∀ z, ‖F z‖ ≤ Real.exp (A + B * ‖z‖))
    (c : ℂ) (hc : F c ≠ 0) (r : ℝ) (hr : 0 < r)
    (S : Finset ℂ) (hs : ∀ z ∈ S, z ∈ closedBall c r ∧ F z = 0) :
    (S.card : ℝ) ≤
      (A + B * ‖c‖ - Real.log ‖F c‖) / Real.log 2 +
        (2 * B / Real.log 2) * r := by
  let M := Real.exp (A + B * (‖c‖ + 2 * r))
  have hM : 1 ≤ M := Real.one_le_exp (by positivity)
  have hb : ∀ z ∈ sphere c (2 * r), ‖F z‖ ≤ M := by
    intro z hz
    have hd : ‖z - c‖ = 2 * r := by simpa [dist_eq_norm] using hz
    have hn : ‖z‖ ≤ ‖c‖ + 2 * r := by
      calc
        ‖z‖ = ‖z - c + c‖ := by rw [sub_add_cancel]
        _ ≤ ‖z - c‖ + ‖c‖ := norm_add_le _ _
        _ = _ := by rw [hd]; ring
    exact (hg z).trans (Real.exp_le_exp.mpr (by gcongr))
  have hj := distinct_zeros_jensen F hF c hc r M hr hM hb S hs
  have hc' : 0 < ‖F c‖ := norm_pos_iff.mpr hc
  rw [Real.log_div (Real.exp_pos _).ne' hc'.ne'] at hj
  dsimp [M] at hj
  rw [Real.log_exp] at hj
  convert hj using 1 <;> ring

/-- A superlinear distinct-zero supply contradicts any nonzero entire
function of exponential type. The supply is explicit and must be
proved for the arithmetic sampling set in a subsequent attachment. -/
theorem exponential_type_unique_of_superlinear_zeros
    (F : ℂ → ℂ) (hF : ∀ z, AnalyticAt ℂ F z)
    (A B : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B)
    (hg : ∀ z, ‖F z‖ ≤ Real.exp (A + B * ‖z‖))
    (hd : ∀ (c : ℂ) (a b : ℝ), ∃ (r : ℝ) (S : Finset ℂ),
      0 < r ∧ (∀ z ∈ S, z ∈ closedBall c r ∧ F z = 0) ∧
      a + b * r < (S.card : ℝ)) :
    F = 0 := by
  funext c
  by_contra hc
  change F c ≠ 0 at hc
  obtain ⟨r, S, hr, hs, hlarge⟩ := hd c
    ((A + B * ‖c‖ - Real.log ‖F c‖) / Real.log 2)
    (2 * B / Real.log 2)
  exact (not_lt_of_ge (exponential_type_linear_count F hF A B hA hB hg c hc r hr S hs)) hlarge

end WeilDefect.MasterRecon.V09A

#print axioms WeilDefect.MasterRecon.V09A.divisor_one_le_at_zero
#print axioms WeilDefect.MasterRecon.V09A.distinct_zeros_le_divisor_sum
#print axioms WeilDefect.MasterRecon.V09A.distinct_zeros_jensen
#print axioms WeilDefect.MasterRecon.V09A.exponential_type_linear_count
#print axioms WeilDefect.MasterRecon.V09A.exponential_type_unique_of_superlinear_zeros
