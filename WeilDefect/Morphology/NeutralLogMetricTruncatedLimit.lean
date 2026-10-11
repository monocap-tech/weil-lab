import WeilDefect.Morphology.NeutralLogMetricTruncatedBounds
import Mathlib.MeasureTheory.Integral.Bochner.Set

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter Topology

/-- Any increasing sequence of finite time intervals exhausting positive
 time recovers the genuinely convergent full jump density off the diagonal. -/
theorem neutralLogMetricTruncatedJumpDensity_tendsto
    (ε R : ℕ → ℝ)
    (hmono : Monotone (fun n => Icc (ε n) (R n)))
    (hcover : (⋃ n, Icc (ε n) (R n)) = Ioi (0 : ℝ))
    (r : ℝ) (hr : 0 < r) :
    Tendsto (fun n => neutralLogMetricTruncatedJumpDensity (ε n) (R n) r)
      atTop (𝓝 (neutralLogMetricJumpDensity r)) := by
  have hi : IntegrableOn (fun t : ℝ =>
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2))
      (⋃ n, Icc (ε n) (R n)) := by
    rw [hcover]
    exact neutralLogMetricJumpDensity_integrable r hr
  have ht := tendsto_setIntegral_of_monotone
    (fun n => measurableSet_Icc (a := ε n) (b := R n)) hmono hi
  have htwo : Tendsto (fun _ : ℕ => (2 : ℝ)) atTop (𝓝 (2 : ℝ)) :=
    tendsto_const_nhds
  simpa only [neutralLogMetricTruncatedJumpDensity,
    neutralLogMetricJumpDensity, hcover] using htwo.mul ht

/-- Signed spatial displacements have the same off-diagonal limit;
 the full density is evaluated at absolute distance. -/
theorem neutralLogMetricTruncatedJumpDensity_tendsto_abs
    (ε R : ℕ → ℝ)
    (hmono : Monotone (fun n => Icc (ε n) (R n)))
    (hcover : (⋃ n, Icc (ε n) (R n)) = Ioi (0 : ℝ))
    (r : ℝ) (hr : r ≠ 0) :
    Tendsto (fun n => neutralLogMetricTruncatedJumpDensity (ε n) (R n) r)
      atTop (𝓝 (neutralLogMetricJumpDensity |r|)) := by
  simpa only [neutralLogMetricTruncatedJumpDensity_abs] using
    neutralLogMetricTruncatedJumpDensity_tendsto ε R hmono hcover |r|
      (abs_pos.mpr hr)

/-- The reciprocal/natural cutoff intervals increase with the index. -/
theorem neutralLogMetricTimeCutoff_monotone :
    Monotone (fun n : ℕ => Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1)) := by
  intro i j hij
  have hij' : (i : ℝ) + 1 ≤ (j : ℝ) + 1 := by
    exact_mod_cast Nat.add_le_add_right hij 1
  exact Icc_subset_Icc (one_div_le_one_div_of_le (by positivity) hij') hij'

/-- The concrete cutoffs cover all positive time and include no nonpositive time. -/
theorem neutralLogMetricTimeCutoff_iUnion :
    (⋃ n : ℕ, Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1)) = Ioi (0 : ℝ) := by
  ext t
  simp only [mem_iUnion, mem_Icc, mem_Ioi]
  constructor
  · rintro ⟨n, hn⟩
    exact lt_of_lt_of_le (by positivity : 0 < 1 / ((n : ℝ) + 1)) hn.1
  · intro ht
    obtain ⟨n, hn⟩ := exists_nat_gt (max t (1 / t))
    have hrec : 1 / t ≤ (n : ℝ) + 1 := by
      have hm := le_max_right t (1 / t)
      linarith
    refine ⟨n, ?_, ?_⟩
    · apply (div_le_iff₀ (by positivity : 0 < (n : ℝ) + 1)).mpr
      have hm := (div_le_iff₀ ht).mp hrec
      nlinarith
    · have hm := le_max_left t (1 / t)
      linarith

/-- The actual reciprocal/natural cutoffs recover the full density at
 every nonzero signed spatial displacement without exhaustion premises. -/
theorem neutralLogMetricTruncatedJumpDensity_natural_tendsto
    (r : ℝ) (hr : r ≠ 0) :
    Tendsto (fun n : ℕ => neutralLogMetricTruncatedJumpDensity
      (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) r)
      atTop (𝓝 (neutralLogMetricJumpDensity |r|)) := by
  exact neutralLogMetricTruncatedJumpDensity_tendsto_abs
    (fun n => 1 / ((n : ℝ) + 1)) (fun n => (n : ℝ) + 1)
    neutralLogMetricTimeCutoff_monotone neutralLogMetricTimeCutoff_iUnion r hr

/-- Cancellation extends the cutoff limit through the spatial diagonal
 at cap points, without asserting density convergence at zero radius. -/
theorem neutralLogMetricTruncatedTrialJump_tendsto
    (ε R : ℕ → ℝ)
    (hmono : Monotone (fun n => Icc (ε n) (R n)))
    (hcover : (⋃ n, Icc (ε n) (R n)) = Ioi (0 : ℝ))
    (B x y : ℝ) (hx : x ∈ Icc (-B) B) (v : ℝ → ℂ) :
    Tendsto (fun n => (v x - neutralLogMetricTrialZeroExtension B v y) *
      (neutralLogMetricTruncatedJumpDensity (ε n) (R n) (x - y) : ℂ))
      atTop (𝓝 (neutralLogMetricTrialJump B v x y)) := by
  by_cases hxy : x = y
  · subst y
    simpa [neutralLogMetricTrialJump, neutralLogMetricTrialZeroExtension, hx] using
      (tendsto_const_nhds : Tendsto (fun _ : ℕ => (0 : ℂ)) atTop (𝓝 (0 : ℂ)))
  · have hd := neutralLogMetricTruncatedJumpDensity_tendsto_abs
      ε R hmono hcover (x - y) (sub_ne_zero.mpr hxy)
    have hc : Tendsto (fun n =>
        (neutralLogMetricTruncatedJumpDensity (ε n) (R n) (x - y) : ℂ))
        atTop (𝓝 (neutralLogMetricJumpDensity |x - y| : ℂ)) :=
      (Complex.continuous_ofReal.tendsto (neutralLogMetricJumpDensity |x - y|)).comp hd
    have hvx : Tendsto (fun _ : ℕ => v x - neutralLogMetricTrialZeroExtension B v y)
        atTop (𝓝 (v x - neutralLogMetricTrialZeroExtension B v y)) :=
      tendsto_const_nhds
    simpa only [neutralLogMetricTrialJump] using hvx.mul hc

/-- Pointwise convergence of the actual cancelled jump for the concrete
 time exhaustion, at every spatial point including the diagonal. -/
theorem neutralLogMetricTruncatedTrialJump_natural_tendsto
    (B x y : ℝ) (hx : x ∈ Icc (-B) B) (v : ℝ → ℂ) :
    Tendsto (fun n : ℕ => (v x - neutralLogMetricTrialZeroExtension B v y) *
      (neutralLogMetricTruncatedJumpDensity
        (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) (x - y) : ℂ))
      atTop (𝓝 (neutralLogMetricTrialJump B v x y)) := by
  exact neutralLogMetricTruncatedTrialJump_tendsto
    (fun n => 1 / ((n : ℝ) + 1)) (fun n => (n : ℝ) + 1)
    neutralLogMetricTimeCutoff_monotone neutralLogMetricTimeCutoff_iUnion B x y hx v

end
end WeilDefect
