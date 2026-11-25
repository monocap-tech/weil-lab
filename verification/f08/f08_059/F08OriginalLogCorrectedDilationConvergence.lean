import WeilDefect.Generated.F08.OriginalNativeL2StrongContinuity
import WeilDefect.Generated.F08.LogDilationFixedVectorCorrection

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped Topology

/-- Inward scales, with the actual interval topology. -/
abbrev f08_059_inwardScale := Set.Icc (1 / 2 : ℝ) 1

def f08_059_nonzeroScale (lam : f08_059_inwardScale) : f08_038_nonzeroScale :=
  ⟨lam.1, ne_of_gt (lt_of_lt_of_le (by norm_num) lam.2.1)⟩

/-- Pointwise squared error estimate for the exact logarithmic correction. -/
theorem f08_059_correctedError_sq_le
    (lam : f08_059_inwardScale) (xi : ℝ) (u k : ℂ) :
    ‖f08_025_logDilationFactor lam.1 xi • u - k‖ ^ 2 ≤
      (2 * (1 + Real.log 2)) * ‖u - k‖ ^ 2 +
      2 * ((f08_025_logDilationFactor lam.1 xi - 1) ^ 2 * ‖k‖ ^ 2) := by
  let m := f08_025_logDilationFactor lam.1 xi
  have hm : m ^ 2 ≤ 1 + Real.log 2 :=
    f08_025_logDilationFactor_sq_le lam.1 xi lam.2.1 lam.2.2
  have he : m • u - k = m • (u - k) + (m - 1) • k := by
    rw [smul_sub, sub_smul, one_smul]
    abel
  have htri := norm_add_le (m • (u - k)) ((m - 1) • k)
  have hsq : ‖m • (u - k) + (m - 1) • k‖ ^ 2 ≤
      2 * ‖m • (u - k)‖ ^ 2 + 2 * ‖(m - 1) • k‖ ^ 2 := by
    have hprod := mul_nonneg (sub_nonneg.mpr htri)
      (add_nonneg (add_nonneg (norm_nonneg _) (norm_nonneg _))
        (norm_nonneg (m • (u - k) + (m - 1) • k)))
    nlinarith [sq_nonneg (‖m • (u - k)‖ - ‖(m - 1) • k‖)]
  have hmul := mul_le_mul_of_nonneg_right hm (sq_nonneg ‖u - k‖)
  change ‖m • u - k‖ ^ 2 ≤ _
  rw [he]
  calc
    _ ≤ 2 * ‖m • (u - k)‖ ^ 2 + 2 * ‖(m - 1) • k‖ ^ 2 := hsq
    _ = 2 * (m ^ 2 * ‖u - k‖ ^ 2) + 2 * ((m - 1) ^ 2 * ‖k‖ ^ 2) := by
      simp only [norm_smul, mul_pow, Real.norm_eq_abs, sq_abs]
    _ ≤ _ := by
      change 2 * (m ^ 2 * ‖u - k‖ ^ 2) + 2 * ((m - 1) ^ 2 * ‖k‖ ^ 2) ≤
        (2 * (1 + Real.log 2)) * ‖u - k‖ ^ 2 + 2 * ((m - 1) ^ 2 * ‖k‖ ^ 2)
      linarith

/-- Actual corrected dilation error, expressed on the native representative.
No physical Fourier scaling identity is assumed. -/
def f08_059_correctedError (lam : f08_059_inwardScale)
    (k : RealComplexL2) (xi : ℝ) : ℂ :=
  f08_025_logDilationFactor lam.1 xi •
    f08_030_nativeFrequencyDilation lam.1 (f08_059_nonzeroScale lam).2 k xi - k xi

/-- Integrable error and quantitative bound in the original L² carrier. -/
theorem f08_059_correctedError_integral_bound
    (lam : f08_059_inwardScale) (k : RealComplexL2) :
    Integrable (fun xi => ‖f08_059_correctedError lam k xi‖ ^ 2) volume ∧
    (∫ xi : ℝ, ‖f08_059_correctedError lam k xi‖ ^ 2 ∂volume) ≤
      (2 * (1 + Real.log 2)) *
        ‖f08_030_nativeFrequencyDilation lam.1 (f08_059_nonzeroScale lam).2 k - k‖ ^ 2 +
      2 * (∫ xi : ℝ, (f08_025_logDilationFactor lam.1 xi - 1) ^ 2 *
        ‖k xi‖ ^ 2 ∂volume) := by
  let u := f08_030_nativeFrequencyDilation lam.1 (f08_059_nonzeroScale lam).2 k
  let d : RealComplexL2 := u - k
  let E : ℝ → ℝ := fun xi =>
    (f08_025_logDilationFactor lam.1 xi - 1) ^ 2 * ‖k xi‖ ^ 2
  let A : ℝ → ℝ := fun xi => ‖f08_059_correctedError lam k xi‖ ^ 2
  let C : ℝ := 2 * (1 + Real.log 2)
  let B : ℝ → ℝ := fun xi => C * ‖d xi‖ ^ 2 + 2 * E xi
  have hk : Integrable (fun xi : ℝ => ‖k xi‖ ^ 2) volume :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable k)).mp (Lp.memLp k)
  have hd : Integrable (fun xi : ℝ => ‖d xi‖ ^ 2) volume :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable d)).mp (Lp.memLp d)
  have hE : Integrable E volume := by
    apply (hk.const_mul (2 + Real.log 2)).mono'
    · exact (((f08_057_logDilationFactor_continuous lam.1).sub continuous_const).pow 2).aestronglyMeasurable.mul
        ((Lp.aestronglyMeasurable k).norm.pow 2)
    · filter_upwards [] with xi
      have hn : 0 ≤ E xi := by dsimp [E]; positivity
      rw [Real.norm_eq_abs, abs_of_nonneg hn]
      exact mul_le_mul_of_nonneg_right
        (f08_057_logDilationFactor_sub_one_sq_le lam.1 xi lam.2.1 lam.2.2)
        (sq_nonneg _)
  have hB : Integrable B volume := (hd.const_mul C).add (hE.const_mul 2)
  have hab : A ≤ᵐ[volume] B := by
    filter_upwards [Lp.coeFn_sub u k] with xi hxi
    change d xi = u xi - k xi at hxi
    dsimp [A, B, E, C]
    rw [hxi]
    exact f08_059_correctedError_sq_le lam xi (u xi) (k xi)
  have hA : Integrable A volume := by
    apply hB.mono'
    · exact ((((f08_057_logDilationFactor_continuous lam.1).aestronglyMeasurable.smul
        (Lp.aestronglyMeasurable u)).sub (Lp.aestronglyMeasurable k)).norm.pow 2)
    · filter_upwards [hab] with xi hxi
      have hn : 0 ≤ A xi := sq_nonneg _
      simpa only [Real.norm_eq_abs, abs_of_nonneg hn] using hxi
  refine ⟨hA, ?_⟩
  calc
    (∫ xi, A xi ∂volume) ≤ ∫ xi, B xi ∂volume := integral_mono_ae hA hB hab
    _ = C * ‖d‖ ^ 2 + 2 * (∫ xi, E xi ∂volume) := by
      dsimp only [B]
      rw [integral_add (hd.const_mul C) (hE.const_mul 2)]
      rw [integral_const_mul, integral_const_mul, ← f08_052_originalL2_norm_sq_eq_integral d]
    _ = _ := rfl

/-- Unconditional convergence of the exact corrected native dilation error
on every original L² vector, as inward scales approach one. -/
theorem f08_059_correctedError_integral_tendsto (k : RealComplexL2) :
    Tendsto (fun lam : f08_059_inwardScale =>
      ∫ xi : ℝ, ‖f08_059_correctedError lam k xi‖ ^ 2 ∂volume)
      (𝓝 (⟨1, by constructor <;> norm_num⟩ : f08_059_inwardScale)) (𝓝 (0 : ℝ)) := by
  let oneScale : f08_059_inwardScale := ⟨1, by constructor <;> norm_num⟩
  let l := 𝓝 oneScale
  have hv : Tendsto (fun lam : f08_059_inwardScale => lam.1) l (𝓝 (1 : ℝ)) :=
    continuous_subtype_val.continuousAt
  have hlift : Tendsto f08_059_nonzeroScale l
      (𝓝 (⟨1, one_ne_zero⟩ : f08_038_nonzeroScale)) :=
    tendsto_subtype_rng.mpr hv
  have hu : Tendsto (fun lam : f08_059_inwardScale =>
      f08_030_nativeFrequencyDilation lam.1 (f08_059_nonzeroScale lam).2 k) l (𝓝 k) := by
    exact (f08_055_originalNativeL2_dilation_tendsto k).comp hlift
  have hd : Tendsto (fun lam : f08_059_inwardScale =>
      ‖f08_030_nativeFrequencyDilation lam.1 (f08_059_nonzeroScale lam).2 k - k‖ ^ 2)
      l (𝓝 (0 : ℝ)) := by
    simpa using ((hu.sub_const k).norm.pow 2)
  have hvw : Tendsto (fun lam : f08_059_inwardScale => lam.1) l
      (𝓝[Set.Icc (1 / 2 : ℝ) 1] (1 : ℝ)) :=
    tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ hv
      (Filter.Eventually.of_forall fun lam => lam.2)
  have he : Tendsto (fun lam : f08_059_inwardScale =>
      ∫ xi : ℝ, (f08_025_logDilationFactor lam.1 xi - 1) ^ 2 *
        ‖k xi‖ ^ 2 ∂volume) l (𝓝 (0 : ℝ)) :=
    (f08_057_logDilationFixedVector_error_tendsto k).comp hvw
  have hupper : Tendsto (fun lam : f08_059_inwardScale =>
      (2 * (1 + Real.log 2)) *
        ‖f08_030_nativeFrequencyDilation lam.1 (f08_059_nonzeroScale lam).2 k - k‖ ^ 2 +
      2 * (∫ xi : ℝ, (f08_025_logDilationFactor lam.1 xi - 1) ^ 2 *
        ‖k xi‖ ^ 2 ∂volume)) l (𝓝 (0 : ℝ)) := by
    simpa using ((hd.const_mul (2 * (1 + Real.log 2))).add (he.const_mul 2))
  change Tendsto _ l _
  rw [Metric.tendsto_nhds]
  intro ε hε
  filter_upwards [(Metric.tendsto_nhds.mp hupper) ε hε] with lam hlam
  rw [Real.dist_eq, sub_zero] at hlam ⊢
  have hn : 0 ≤ ∫ xi : ℝ, ‖f08_059_correctedError lam k xi‖ ^ 2 ∂volume :=
    integral_nonneg (fun _ => sq_nonneg _)
  rw [abs_of_nonneg hn]
  exact lt_of_le_of_lt (f08_059_correctedError_integral_bound lam k).2
    (lt_of_le_of_lt (le_abs_self _) hlam)

#print axioms f08_059_correctedError_sq_le
#print axioms f08_059_correctedError_integral_bound
#print axioms f08_059_correctedError_integral_tendsto

end
end WeilDefect
