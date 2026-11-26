import WeilDefect.MasterRecon.V08A
import Mathlib.Analysis.Normed.Operator.Compact.Basic
import Mathlib.Analysis.SpecificLimits.Basic

/-! V08B: compact-defect removal, the functional-analytic coercivity
step of 001G §3. The actual supported log carrier, compact embedding,
sample injectivity and arithmetic defect inequality remain inputs.
Use a norm-Cauchy subsequence rather than weak compactness. -/
namespace WeilDefect.MasterRecon.V08B

open Filter Set
open scoped Topology NNReal

variable {H K L : Type*}
variable [NormedAddCommGroup H] [NormedSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup K] [NormedSpace ℂ K]
variable [NormedAddCommGroup L] [NormedSpace ℂ L]

theorem compact_defect_linear
    (A : H →L[ℂ] K) (C : H →L[ℂ] L)
    (M : ℝ) (hM : 0 ≤ M)
    (hdef : ∀ x : H, ‖x‖ ^ 2 ≤ ‖A x‖ ^ 2 + M * ‖C x‖ ^ 2)
    (x : H) :
    ‖x‖ ≤ ‖A x‖ + (M + 1) * ‖C x‖ := by
  have hm : M ≤ (M + 1) ^ 2 := by nlinarith [sq_nonneg M]
  have hmul := mul_le_mul_of_nonneg_right hm (sq_nonneg ‖C x‖)
  have hcross : 0 ≤ ‖A x‖ * ((M + 1) * ‖C x‖) := by positivity
  have hsq : ‖x‖ ^ 2 ≤ (‖A x‖ + (M + 1) * ‖C x‖) ^ 2 := by
    nlinarith [hdef x, hmul, hcross]
  exact (sq_le_sq₀ (norm_nonneg _) (by positivity)).mp hsq

theorem compact_defect_unit_lower
    (A : H →L[ℂ] K) (C : H →L[ℂ] L)
    (hcompact : IsCompactOperator C)
    (hinj : ∀ x : H, A x = 0 → x = 0)
    (M : ℝ) (hM : 0 ≤ M)
    (hdef : ∀ x : H, ‖x‖ ^ 2 ≤ ‖A x‖ ^ 2 + M * ‖C x‖ ^ 2) :
    ∃ r : ℝ, 0 < r ∧ ∀ x : H, ‖x‖ = 1 → r ≤ ‖A x‖ := by
  by_contra! hn
  have hex : ∀ n : ℕ, ∃ x : H, ‖x‖ = 1 ∧
      ‖A x‖ < 1 / ((n : ℝ) + 1) := by
    intro n
    exact hn _ (by positivity)
  choose u hu hAu using hex
  have hAu0 : Tendsto (fun n => A (u n)) atTop (𝓝 0) := by
    apply Metric.tendsto_atTop.2
    intro e he
    obtain ⟨N, hN⟩ := Metric.tendsto_atTop.1
      (tendsto_one_div_add_atTop_nhds_zero_nat (𝕜 := ℝ)) e he
    refine ⟨N, fun n hn' => ?_⟩
    rw [dist_zero_right]
    have hh := hN n hn'
    rw [Real.dist_eq, sub_zero, abs_of_nonneg (by positivity)] at hh
    exact (hAu n).trans hh
  have hc' : IsCompactOperator C.toLinearMap := hcompact
  obtain ⟨S, hS, hCS⟩ := hc'.image_closedBall_subset_compact 1
  have huS : ∀ n : ℕ, C (u n) ∈ S := by
    intro n
    apply hCS
    refine ⟨u n, ?_, rfl⟩
    rw [Metric.mem_closedBall, dist_zero_right, hu]
  obtain ⟨y, _, φ, hφ, hy⟩ := hS.tendsto_subseq huS
  let w : ℕ → H := u ∘ φ
  have hAw : Tendsto (fun n => A (w n)) atTop (𝓝 0) :=
    hAu0.comp hφ.tendsto_atTop
  have hCw : Tendsto (fun n => C (w n)) atTop (𝓝 y) := hy
  have hca : CauchySeq (fun n => A (w n)) := hAw.cauchySeq
  have hcc : CauchySeq (fun n => C (w n)) := hCw.cauchySeq
  have hcw : CauchySeq w := by
    apply Metric.cauchySeq_iff.2
    intro e he
    obtain ⟨N, hN⟩ := Metric.cauchySeq_iff.1 hca (e / 2) (by positivity)
    obtain ⟨P, hP⟩ := Metric.cauchySeq_iff.1 hcc
      (e / (2 * (M + 1))) (by positivity)
    refine ⟨max N P, fun n hn' m hm' => ?_⟩
    have ha := hN n ((le_max_left N P).trans hn') m ((le_max_left N P).trans hm')
    have hc := hP n ((le_max_right N P).trans hn') m ((le_max_right N P).trans hm')
    rw [dist_eq_norm, ← A.map_sub] at ha
    rw [dist_eq_norm, ← C.map_sub] at hc
    rw [dist_eq_norm]
    have hc2 := (lt_div_iff₀ (by positivity : 0 < 2 * (M + 1))).mp hc
    have hd := compact_defect_linear A C M hM hdef (w n - w m)
    linarith
  obtain ⟨z, hz⟩ := cauchySeq_tendsto_of_complete hcw
  have haz : A z = 0 := tendsto_nhds_unique (A.continuous.continuousAt.tendsto.comp hz) hAw
  have hz0 := hinj z haz
  have hnz : Tendsto (fun n => ‖w n‖) atTop (𝓝 ‖z‖) := hz.norm
  have hconst : Tendsto (fun n => ‖w n‖) atTop (𝓝 (1 : ℝ)) := by
    have hh : (fun n => ‖w n‖) = fun _ : ℕ => (1 : ℝ) := by
      funext n
      exact hu (φ n)
    rw [hh]
    exact tendsto_const_nhds
  have heq := tendsto_nhds_unique hnz hconst
  rw [hz0, norm_zero] at heq
  norm_num at heq

theorem compact_defect_coercivity
    (A : H →L[ℂ] K) (C : H →L[ℂ] L)
    (hcompact : IsCompactOperator C)
    (hinj : ∀ x : H, A x = 0 → x = 0)
    (M : ℝ) (hM : 0 ≤ M)
    (hdef : ∀ x : H, ‖x‖ ^ 2 ≤ ‖A x‖ ^ 2 + M * ‖C x‖ ^ 2) :
    ∃ b : ℝ≥0, 0 < b ∧ ∀ x : H, ‖x‖ ^ 2 * (b : ℝ) ≤ ‖A x‖ ^ 2 := by
  obtain ⟨r, hr, hunit⟩ := compact_defect_unit_lower A C hcompact hinj M hM hdef
  refine ⟨⟨r ^ 2, sq_nonneg r⟩, ?_, ?_⟩
  · exact_mod_cast (show 0 < r ^ 2 by positivity)
  intro x
  by_cases hx : x = 0
  · simp [hx]
  have hp : 0 < ‖x‖ := norm_pos_iff.mpr hx
  let q : ℂ := ((‖x‖)⁻¹ : ℝ)
  have hq : ‖q‖ = ‖x‖⁻¹ := by
    unfold q
    rw [Complex.norm_real, Real.norm_of_nonneg (by positivity)]
  have hnorm : ‖q • x‖ = 1 := by
    rw [norm_smul, hq, inv_mul_cancel₀ hp.ne']
  have ha := hunit (q • x) hnorm
  rw [A.map_smul, norm_smul, hq, ← div_eq_inv_mul] at ha
  have hl := (le_div_iff₀ hp).mp ha
  have hs := (sq_le_sq₀ (by positivity : 0 ≤ r * ‖x‖) (norm_nonneg (A x))).2 hl
  change ‖x‖ ^ 2 * r ^ 2 ≤ ‖A x‖ ^ 2
  nlinarith

end WeilDefect.MasterRecon.V08B

#print axioms WeilDefect.MasterRecon.V08B.compact_defect_linear
#print axioms WeilDefect.MasterRecon.V08B.compact_defect_unit_lower
#print axioms WeilDefect.MasterRecon.V08B.compact_defect_coercivity
