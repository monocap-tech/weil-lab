import WeilDefect.Morphology.NeutralLogMetricTruncatedBounds
import WeilDefect.Morphology.NeutralLogMetricCapL2
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.MeasureTheory.Function.UniformIntegrable

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter Topology
open scoped ENNReal

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

/-- Spatial cutoff removal for measurable cap-bounded Lipschitz trials.
 The genuinely integrable full jump dominates every truncated jump. -/
theorem neutralLogMetricTruncatedTrialJump_integral_tendsto
    (B x L M : ℝ) (hB : 0 ≤ B) (hx : x ∈ Ioo (-B) B)
    (hL : 0 ≤ L) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M)
    (hmod : ∀ y ∈ Icc (-B) B, ‖v x - v y‖ ≤ L * |x - y|) :
    Tendsto (fun n : ℕ => ∫ y : ℝ,
      (v x - neutralLogMetricTrialZeroExtension B v y) *
        (neutralLogMetricTruncatedJumpDensity
          (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) (x - y) : ℂ))
      atTop (𝓝 (∫ y : ℝ, neutralLogMetricTrialJump B v x y)) := by
  have hxcap : x ∈ Icc (-B) B := ⟨hx.1.le, hx.2.le⟩
  have hxv : neutralLogMetricTrialZeroExtension B v x = v x := by
    simp [neutralLogMetricTrialZeroExtension, hxcap]
  have hfull := neutralLogMetricTrialJump_integrable B x L hB hx v hv hL hmod
  apply tendsto_integral_of_dominated_convergence
    (fun y : ℝ => ‖neutralLogMetricTrialJump B v x y‖)
  · intro n
    have hn := neutralLogMetricTruncatedJump_integrable
      (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) x M (by positivity) hM
      (neutralLogMetricTrialZeroExtension B v)
      (neutralLogMetricTrialZeroExtension_measurable B v hv)
      (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)
    simpa only [hxv] using hn.aestronglyMeasurable
  · exact hfull.norm
  · intro n
    exact Eventually.of_forall (fun y => neutralLogMetricTruncatedTrialJump_norm_le
      (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) B x y (by positivity) hxcap v)
  · exact Eventually.of_forall (fun y =>
      neutralLogMetricTruncatedTrialJump_natural_tendsto B x y hxcap v)

/-- The positive-time physical action, with concrete cutoffs removed,
 recovers the endpoint candidate for measurable cap-bounded Lipschitz trials. -/
theorem neutralLogMetricPoissonTrialAction_tendsto_endpointCandidate
    (B x L M : ℝ) (hB : 0 ≤ B) (hx : x ∈ Ioo (-B) B)
    (hL : 0 ≤ L) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M)
    (hmod : ∀ y ∈ Icc (-B) B, ‖v x - v y‖ ≤ L * |x - y|) :
    Tendsto (fun n : ℕ => v x +
      ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (v x - ∫ y : ℝ, neutralLogMetricTrialZeroExtension B v y *
            (neutralLogMetricPoissonDensity t (x - y) : ℂ)))
      atTop (𝓝 (neutralLogMetricEndpointCandidate B v x)) := by
  have hxcap : x ∈ Icc (-B) B := ⟨hx.1.le, hx.2.le⟩
  have hxv : neutralLogMetricTrialZeroExtension B v x = v x := by
    simp [neutralLogMetricTrialZeroExtension, hxcap]
  have he (n : ℕ) :
      (∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
        ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
          (v x - ∫ y : ℝ, neutralLogMetricTrialZeroExtension B v y *
            (neutralLogMetricPoissonDensity t (x - y) : ℂ))) =
      ∫ y : ℝ, (v x - neutralLogMetricTrialZeroExtension B v y) *
        (neutralLogMetricTruncatedJumpDensity
          (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) (x - y) : ℂ) := by
    simpa only [hxv] using neutralLogMetricTruncatedJump_action
      (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) x M (by positivity) hM
      (neutralLogMetricTrialZeroExtension B v)
      (neutralLogMetricTrialZeroExtension_measurable B v hv)
      (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)
  rw [neutralLogMetricEndpointCandidate_eq_trial_jump B x L hB hx v hv hL hmod]
  simp_rw [he]
  exact tendsto_const_nhds.add
    (neutralLogMetricTruncatedTrialJump_integral_tendsto
      B x L M hB hx hL hM v hv hbound hmod)

/-- A cutoff-independent spatial norm budget for every truncated trial
 action, with the genuine endpoint tails retained in the envelope. -/
theorem neutralLogMetricTruncatedTrialJump_integral_norm_le
    (ε R B x L M : ℝ) (hε : 0 < ε) (hB : 0 ≤ B)
    (hx : x ∈ Ioo (-B) B) (hL : 0 ≤ L) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M)
    (hmod : ∀ y ∈ Icc (-B) B, ‖v x - v y‖ ≤ L * |x - y|) :
    ‖∫ y : ℝ, (v x - neutralLogMetricTrialZeroExtension B v y) *
      (neutralLogMetricTruncatedJumpDensity ε R (x - y) : ℂ)‖ ≤
      2 * B * L + M * neutralLogMetricExteriorSource B x := by
  have hxcap : x ∈ Icc (-B) B := ⟨hx.1.le, hx.2.le⟩
  have hxv : neutralLogMetricTrialZeroExtension B v x = v x := by
    simp [neutralLogMetricTrialZeroExtension, hxcap]
  have ht0 := neutralLogMetricTruncatedJump_integrable ε R x M hε hM
    (neutralLogMetricTrialZeroExtension B v)
    (neutralLogMetricTrialZeroExtension_measurable B v hv)
    (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)
  have ht : Integrable (fun y : ℝ =>
      (v x - neutralLogMetricTrialZeroExtension B v y) *
        (neutralLogMetricTruncatedJumpDensity ε R (x - y) : ℂ)) := by
    simpa only [hxv] using ht0
  calc
    _ ≤ ∫ y : ℝ, ‖(v x - neutralLogMetricTrialZeroExtension B v y) *
        (neutralLogMetricTruncatedJumpDensity ε R (x - y) : ℂ)‖ :=
      norm_integral_le_integral_norm _
    _ ≤ ∫ y : ℝ, ‖neutralLogMetricTrialJump B v x y‖ := by
      apply integral_mono_ae ht.norm
        (neutralLogMetricTrialJump_integrable B x L hB hx v hv hL hmod).norm
      exact Eventually.of_forall (fun y =>
        neutralLogMetricTruncatedTrialJump_norm_le ε R B x y hε hxcap v)
    _ ≤ _ := neutralLogMetricTrialJump_integral_norm_le
      B x L M hB hx hL v hv (hbound x hxcap) hmod

/-- Every finite positive-time trial action obeys the same endpoint-aware
 budget, independently of the lower and upper time cutoffs. -/
theorem neutralLogMetricPoissonTrialAction_norm_le
    (ε R B x L M : ℝ) (hε : 0 < ε) (hB : 0 ≤ B)
    (hx : x ∈ Ioo (-B) B) (hL : 0 ≤ L) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ y ∈ Icc (-B) B, ‖v y‖ ≤ M)
    (hmod : ∀ y ∈ Icc (-B) B, ‖v x - v y‖ ≤ L * |x - y|) :
    ‖v x + ∫ t in Icc ε R,
      ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
        (v x - ∫ y : ℝ, neutralLogMetricTrialZeroExtension B v y *
          (neutralLogMetricPoissonDensity t (x - y) : ℂ))‖ ≤
      M + 2 * B * L + M * neutralLogMetricExteriorSource B x := by
  have hxcap : x ∈ Icc (-B) B := ⟨hx.1.le, hx.2.le⟩
  have hxv : neutralLogMetricTrialZeroExtension B v x = v x := by
    simp [neutralLogMetricTrialZeroExtension, hxcap]
  have he := neutralLogMetricTruncatedJump_action ε R x M hε hM
    (neutralLogMetricTrialZeroExtension B v)
    (neutralLogMetricTrialZeroExtension_measurable B v hv)
    (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)
  simp only [hxv] at he
  rw [he]
  have hj := neutralLogMetricTruncatedTrialJump_integral_norm_le
    ε R B x L M hε hB hx hL hM v hv hbound hmod
  have hvx := hbound x hxcap
  exact (norm_add_le _ _).trans (by linarith)

/-- Parameter measurability of the truncated density, including its
 totalized values and without any cutoff positivity premise. -/
theorem neutralLogMetricTruncatedJumpDensity_measurable (ε R : ℝ) :
    Measurable (neutralLogMetricTruncatedJumpDensity ε R) := by
  have hm : Measurable (fun p : ℝ × ℝ =>
      Real.exp (-(Real.exp 1) * p.2) /
        (p.2 ^ 2 + 4 * Real.pi ^ 2 * p.1 ^ 2)) := by fun_prop
  have hi : StronglyMeasurable (fun r : ℝ => ∫ t in Icc ε R,
      Real.exp (-(Real.exp 1) * t) / (t ^ 2 + 4 * Real.pi ^ 2 * r ^ 2)) :=
    hm.stronglyMeasurable.integral_prod_right'
  exact measurable_const.mul hi.measurable

/-- The actual truncated spatial action is measurable in the observation
 variable for any measurable trial. -/
theorem neutralLogMetricTruncatedTrialAction_measurable
    (ε R B : ℝ) (v : ℝ → ℂ) (hv : Measurable v) :
    Measurable (fun x : ℝ => v x + ∫ y : ℝ,
      (v x - neutralLogMetricTrialZeroExtension B v y) *
        (neutralLogMetricTruncatedJumpDensity ε R (x - y) : ℂ)) := by
  have hd : Measurable (fun p : ℝ × ℝ =>
      neutralLogMetricTruncatedJumpDensity ε R (p.1 - p.2)) :=
    (neutralLogMetricTruncatedJumpDensity_measurable ε R).comp (by fun_prop)
  have hm : Measurable (fun p : ℝ × ℝ =>
      (v p.1 - neutralLogMetricTrialZeroExtension B v p.2) *
        (neutralLogMetricTruncatedJumpDensity ε R (p.1 - p.2) : ℂ)) :=
    ((hv.comp measurable_fst).sub
      ((neutralLogMetricTrialZeroExtension_measurable B v hv).comp measurable_snd)).mul
      (Complex.continuous_ofReal.measurable.comp hd)
  exact hv.add hm.stronglyMeasurable.integral_prod_right'.measurable

/-- Every actual truncated spatial action is in physical L2 on the cap,
 with membership derived from the common endpoint-aware budget. -/
theorem neutralLogMetricTruncatedTrialAction_memLp_two
    (ε R B L M : ℝ) (hε : 0 < ε) (hB : 0 ≤ B)
    (hL : 0 ≤ L) (hM : 0 ≤ M) (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|) :
    MemLp (fun x : ℝ => v x + ∫ y : ℝ,
      (v x - neutralLogMetricTrialZeroExtension B v y) *
        (neutralLogMetricTruncatedJumpDensity ε R (x - y) : ℂ)) 2
      (volume.restrict (Ioo (-B) B)) := by
  apply (neutralLogMetricPhysicalActionBudget_memLp_two B M L hB).mono'
    (neutralLogMetricTruncatedTrialAction_measurable ε R B v hv).aestronglyMeasurable
  filter_upwards [ae_restrict_mem measurableSet_Ioo] with x hx
  have hxcap : x ∈ Icc (-B) B := ⟨hx.1.le, hx.2.le⟩
  have hj := neutralLogMetricTruncatedTrialJump_integral_norm_le
    ε R B x L M hε hB hx hL hM v hv hbound (hmod x hxcap)
  have hvx := hbound x hxcap
  exact (norm_add_le _ _).trans (by linarith)

/-- Concrete cutoff actions converge to the endpoint candidate in the
 physical cap L2 seminorm, not merely at individual interior points. -/
theorem neutralLogMetricTruncatedTrialAction_tendsto_L2
    (B L M : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|) :
    Tendsto (fun n : ℕ => eLpNorm
      (fun x : ℝ => (v x + ∫ y : ℝ,
        (v x - neutralLogMetricTrialZeroExtension B v y) *
          (neutralLogMetricTruncatedJumpDensity
            (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) (x - y) : ℂ)) -
        neutralLogMetricEndpointCandidate B v x)
      2 (volume.restrict (Ioo (-B) B))) atTop (𝓝 0) := by
  let A : ℕ → ℝ → ℂ := fun n x => v x + ∫ y : ℝ,
    (v x - neutralLogMetricTrialZeroExtension B v y) *
      (neutralLogMetricTruncatedJumpDensity
        (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) (x - y) : ℂ)
  let G : ℝ → ℝ := fun x => M + 2 * B * L + M * neutralLogMetricExteriorSource B x
  have hGpos (x : ℝ) : 0 ≤ G x := by
    have hE := neutralLogMetricExteriorSource_nonnegative B x
    dsimp only [G]
    positivity
  have hGmeas : Measurable G :=
    measurable_const.add (measurable_const.mul (neutralLogMetricExteriorSource_measurable B))
  have hGC : MemLp (fun x : ℝ => (G x : ℂ)) 2
      (volume.restrict (Ioo (-B) B)) := by
    apply (neutralLogMetricPhysicalActionBudget_memLp_two B M L hB).mono'
      (Complex.continuous_ofReal.measurable.comp hGmeas).aestronglyMeasurable
    exact Eventually.of_forall (fun x => by
      change ‖(G x : ℂ)‖ ≤ G x
      rw [Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (hGpos x)])
  have hAmeas (n : ℕ) : AEStronglyMeasurable (A n)
      (volume.restrict (Ioo (-B) B)) :=
    (neutralLogMetricTruncatedTrialAction_measurable
      (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) B v hv).aestronglyMeasurable
  have hAbound (n : ℕ) (x : ℝ) (hx : x ∈ Ioo (-B) B) : ‖A n x‖ ≤ G x := by
    have hxcap : x ∈ Icc (-B) B := ⟨hx.1.le, hx.2.le⟩
    have hj := neutralLogMetricTruncatedTrialJump_integral_norm_le
      (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) B x L M
      (by positivity) hB hx hL hM v hv hbound (hmod x hxcap)
    have hvx := hbound x hxcap
    exact (norm_add_le _ _).trans (by dsimp only [G]; linarith)
  have hui : UnifIntegrable A 2 (volume.restrict (Ioo (-B) B)) := by
    apply (unifIntegrable_const (ι := ℕ) (by norm_num : (1 : ℝ≥0∞) ≤ 2)
      (by norm_num : (2 : ℝ≥0∞) ≠ ∞) hGC).ae_mono hAmeas
    intro n
    filter_upwards [ae_restrict_mem measurableSet_Ioo] with x hx
    change ‖A n x‖ₑ ≤ ‖(G x : ℂ)‖ₑ
    simp only [← ofReal_norm, Complex.norm_real, Real.norm_eq_abs,
      abs_of_nonneg (hGpos x)]
    exact ENNReal.ofReal_le_ofReal (hAbound n x hx)
  have hpoint : ∀ᵐ x ∂(volume.restrict (Ioo (-B) B)),
      Tendsto (fun n => A n x) atTop (𝓝 (neutralLogMetricEndpointCandidate B v x)) := by
    filter_upwards [ae_restrict_mem measurableSet_Ioo] with x hx
    have hxcap : x ∈ Icc (-B) B := ⟨hx.1.le, hx.2.le⟩
    rw [neutralLogMetricEndpointCandidate_eq_trial_jump B x L hB hx v hv hL
      (hmod x hxcap)]
    exact tendsto_const_nhds.add (neutralLogMetricTruncatedTrialJump_integral_tendsto
      B x L M hB hx hL hM v hv hbound (hmod x hxcap))
  exact tendsto_Lp_finite_of_tendsto_ae (by norm_num) (by norm_num) hAmeas
    (neutralLogMetricEndpointCandidate_memLp_two B M L hB hL v hv hbound hmod)
    hui hpoint

/-- The concrete Poisson time actions converge in the physical cap L2
 seminorm, by their exact interior equality with the spatial actions. -/
theorem neutralLogMetricPoissonTrialAction_tendsto_L2
    (B L M : ℝ) (hB : 0 ≤ B) (hL : 0 ≤ L) (hM : 0 ≤ M)
    (v : ℝ → ℂ) (hv : Measurable v)
    (hbound : ∀ x ∈ Icc (-B) B, ‖v x‖ ≤ M)
    (hmod : ∀ x ∈ Icc (-B) B, ∀ y ∈ Icc (-B) B,
      ‖v x - v y‖ ≤ L * |x - y|) :
    Tendsto (fun n : ℕ => eLpNorm
      (fun x : ℝ => (v x +
        ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (v x - ∫ y : ℝ, neutralLogMetricTrialZeroExtension B v y *
              (neutralLogMetricPoissonDensity t (x - y) : ℂ))) -
        neutralLogMetricEndpointCandidate B v x)
      2 (volume.restrict (Ioo (-B) B))) atTop (𝓝 0) := by
  have he (n : ℕ) :
      eLpNorm (fun x : ℝ => (v x +
        ∫ t in Icc (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1),
          ((Real.exp (-(Real.exp 1) * t) / t : ℝ) : ℂ) *
            (v x - ∫ y : ℝ, neutralLogMetricTrialZeroExtension B v y *
              (neutralLogMetricPoissonDensity t (x - y) : ℂ))) -
        neutralLogMetricEndpointCandidate B v x)
        2 (volume.restrict (Ioo (-B) B)) =
      eLpNorm (fun x : ℝ => (v x + ∫ y : ℝ,
        (v x - neutralLogMetricTrialZeroExtension B v y) *
          (neutralLogMetricTruncatedJumpDensity
            (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) (x - y) : ℂ)) -
        neutralLogMetricEndpointCandidate B v x)
        2 (volume.restrict (Ioo (-B) B)) := by
    apply eLpNorm_congr_ae
    filter_upwards [ae_restrict_mem measurableSet_Ioo] with x hx
    have hxcap : x ∈ Icc (-B) B := ⟨hx.1.le, hx.2.le⟩
    have hxv : neutralLogMetricTrialZeroExtension B v x = v x := by
      simp [neutralLogMetricTrialZeroExtension, hxcap]
    have ha := neutralLogMetricTruncatedJump_action
      (1 / ((n : ℝ) + 1)) ((n : ℝ) + 1) x M (by positivity) hM
      (neutralLogMetricTrialZeroExtension B v)
      (neutralLogMetricTrialZeroExtension_measurable B v hv)
      (neutralLogMetricTrialZeroExtension_norm_le B M hM v hbound)
    simp only [hxv] at ha
    dsimp only
    rw [ha]
  simp_rw [he]
  exact neutralLogMetricTruncatedTrialAction_tendsto_L2 B L M hB hL hM v hv hbound hmod

end
end WeilDefect
