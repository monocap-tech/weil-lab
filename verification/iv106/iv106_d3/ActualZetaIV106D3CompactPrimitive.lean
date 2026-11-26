import Mathlib
import Mathlib.Analysis.Distribution.SchwartzSpace.Deriv

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap LineDeriv

/-- Adjacent interval means force the primitive to vanish at every endpoint. -/
theorem neutralIV106D3Endpoint (v : 𝓢(ℝ, ℂ)) (p : ℕ → ℝ) (N : ℕ)
    (hc : ∀ j < N, (∫ t in p j..p (j+1), v t) = 0) :
    ∀ j ≤ N, (∫ t in p 0..p j, v t) = 0 := by
  intro j
  induction j with
  | zero => intro hj; simp
  | succ j ih =>
    intro hj
    have he := intervalIntegral.integral_add_adjacent_intervals
      (v.continuous.intervalIntegrable (p 0) (p j))
      (v.continuous.intervalIntegrable (p j) (p (j+1)))
    rw [ih (Nat.le_trans (Nat.le_succ j) hj), hc j (Nat.lt_of_succ_le hj), zero_add] at he
    exact he.symm

/-- The globally defined oriented primitive vanishes outside the window. -/
theorem neutralIV106D3Primitive_outside (v : 𝓢(ℝ, ℂ)) (l r : ℝ)
    (hlr : l ≤ r) (hv : ∀ x ∉ Set.Icc l r, v x = 0)
    (hm : (∫ t in l..r, v t) = 0) (x : ℝ) (hx : x ∉ Set.Icc l r) :
    (∫ t in l..x, v t) = 0 := by
  by_cases hl : x < l
  · have hz : (∫ t in x..l, v t) = 0 := by
      calc
        _ = ∫ t in x..l, (0 : ℂ) := by
          apply intervalIntegral.integral_congr_Ioo_of_le hl.le
          intro t ht
          exact hv t (fun h => (not_le_of_gt ht.2) h.1)
        _ = 0 := intervalIntegral.integral_zero
    rw [intervalIntegral.integral_symm, hz, neg_zero]
  · have hr : r < x := by
      by_contra! h
      exact hx ⟨le_of_not_gt hl, h⟩
    have hz : (∫ t in r..x, v t) = 0 := by
      calc
        _ = ∫ t in r..x, (0 : ℂ) := by
          apply intervalIntegral.integral_congr_Ioo_of_le hr.le
          intro t ht
          exact hv t (fun h => (not_le_of_gt ht.1) h.2)
        _ = 0 := intervalIntegral.integral_zero
    have he := intervalIntegral.integral_add_adjacent_intervals
      (v.continuous.intervalIntegrable l r) (v.continuous.intervalIntegrable r x)
    rw [hm, hz, add_zero] at he
    exact he.symm

/-- Construct the actual compactly supported Schwartz primitive, not a witness premise. -/
theorem neutralIV106D3Schwartz_primitive (v : 𝓢(ℝ, ℂ)) (l r : ℝ)
    (hlr : l ≤ r) (hv : ∀ x ∉ Set.Icc l r, v x = 0)
    (hm : (∫ t in l..r, v t) = 0) :
    ∃ V : 𝓢(ℝ, ℂ), (∀ x, V x = ∫ t in l..x, v t) ∧
      ∂_{(1 : ℝ)} V = v ∧ (∀ x ∉ Set.Icc l r, V x = 0) := by
  let F : ℝ → ℂ := fun x => ∫ t in l..x, v t
  have hd (x : ℝ) : HasDerivAt F (v x) x :=
    (v.continuous.integral_hasStrictDerivAt l x).hasDerivAt
  have hs : ContDiff ℝ ∞ F := by
    apply contDiff_infty_iff_deriv.mpr
    refine ⟨fun x => (hd x).differentiableAt, ?_⟩
    rw [show deriv F = (v : ℝ → ℂ) from funext fun x => (hd x).deriv]
    exact v.smooth'
  have ho (x : ℝ) (hx : x ∉ Set.Icc l r) : F x = 0 :=
    neutralIV106D3Primitive_outside v l r hlr hv hm x hx
  have hc : HasCompactSupport F := by
    change IsCompact (closure (Function.support F))
    apply isCompact_Icc.of_isClosed_subset isClosed_closure
    apply closure_minimal _ isClosed_Icc
    intro x hx
    by_contra h
    exact hx (ho x h)
  let V := hc.toSchwartzMap hs
  refine ⟨V, fun x => rfl, ?_, ho⟩
  apply SchwartzMap.ext
  intro x
  rw [SchwartzMap.lineDerivOp_apply_eq_fderiv, fderiv_apply_one_eq_deriv]
  change deriv F x = v x
  exact (hd x).deriv

/-- Combine two one-sided Cauchy--Schwarz estimates without a centered kernel. -/
theorem neutralIV106D3TwoSided (s t A B z : ℝ)
    (hs : 0 ≤ s) (ht : 0 ≤ t) (hh : 0 < s+t)
    (hL : z ≤ s*A) (hR : z ≤ t*B) :
    z ≤ s*t/(s+t)*(A+B) := by
  have h1 := mul_le_mul_of_nonneg_left hL ht
  have h2 := mul_le_mul_of_nonneg_left hR hs
  rw [div_mul_eq_mul_div]
  apply (le_div_iff₀ hh).mpr
  nlinarith only [h1, h2]

#print axioms neutralIV106D3Endpoint
#print axioms neutralIV106D3Primitive_outside
#print axioms neutralIV106D3Schwartz_primitive
#print axioms neutralIV106D3TwoSided
end
end WeilDefect
