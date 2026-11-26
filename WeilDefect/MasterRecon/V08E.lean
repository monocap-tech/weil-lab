import WeilDefect.MasterRecon.V08D
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.Topology.ContinuousMap.Compact

/-! V08E: actual bounded-band Fourier integral as a compact map from
physical L¹ to continuous frequency functions. This does not yet identify
the weighted Fourier L² carrier or its Plancherel normalization. -/
namespace WeilDefect.MasterRecon.V08E

open MeasureTheory Set Filter
open scoped ENNReal Topology BigOperators

abbrev Band (R : ℝ) := Set.Icc (-R) R
local instance bandCompact (R : ℝ) : CompactSpace (Band R) :=
  compactSpace_Icc (-R) R

noncomputable abbrev PhysicalL1 (μ : Measure ℝ) := Lp ℂ 1 μ

theorem moment_integrable (μ : Measure ℝ) (t : ℝ)
    (ht : ∀ᵐ x ∂μ, |x| ≤ t) (j : ℕ) (f : PhysicalL1 μ) :
    Integrable (fun x : ℝ => (x : ℂ) ^ j * f x) μ := by
  have hf : Integrable (fun x => f x) μ :=
    memLp_one_iff_integrable.mp (Lp.memLp f)
  have hm : Continuous (fun x : ℝ => (x : ℂ) ^ j) := by fun_prop
  apply hf.bdd_mul hm.aestronglyMeasurable (c := t ^ j)
  filter_upwards [ht] with x hx
  rw [norm_pow, Complex.norm_real, Real.norm_eq_abs]
  gcongr

theorem moment_integral_bound (μ : Measure ℝ) (t : ℝ)
    (ht : ∀ᵐ x ∂μ, |x| ≤ t) (j : ℕ) (f : PhysicalL1 μ) :
    ‖∫ x, (x : ℂ) ^ j * f x ∂μ‖ ≤ t ^ j * ‖f‖ := by
  have hf : Integrable (fun x => f x) μ :=
    memLp_one_iff_integrable.mp (Lp.memLp f)
  rw [L1.norm_eq_integral_norm, ← integral_const_mul]
  apply norm_integral_le_of_norm_le (hf.norm.const_mul _)
  filter_upwards [ht] with x hx
  rw [norm_mul, norm_pow, Complex.norm_real, Real.norm_eq_abs]
  gcongr

noncomputable def moment (μ : Measure ℝ) (t : ℝ) (ht0 : 0 ≤ t)
    (ht : ∀ᵐ x ∂μ, |x| ≤ t) (j : ℕ) : PhysicalL1 μ →L[ℂ] ℂ :=
  ({
    toFun := fun f => ∫ x, (x : ℂ) ^ j * f x ∂μ
    map_add' := fun f g => by
      calc
        (∫ x, (x : ℂ) ^ j * (f + g) x ∂μ) =
            ∫ x, ((x : ℂ) ^ j * f x + (x : ℂ) ^ j * g x) ∂μ := by
          apply integral_congr_ae
          filter_upwards [Lp.coeFn_add f g] with x hx
          change (x : ℂ) ^ j * (f + g) x = _
          rw [show (f + g) x = f x + g x from hx, mul_add]
        _ = _ := integral_add (moment_integrable μ t ht j f)
          (moment_integrable μ t ht j g)
    map_smul' := fun c f => by
      change (∫ x, (x : ℂ) ^ j * (c • f) x ∂μ) =
        c * (∫ x, (x : ℂ) ^ j * f x ∂μ)
      rw [← integral_const_mul]
      apply integral_congr_ae
      filter_upwards [Lp.coeFn_smul c f] with x hx
      change (x : ℂ) ^ j * (c • f) x = c * ((x : ℂ) ^ j * f x)
      rw [show (c • f) x = c * f x from hx]
      ring
  } : PhysicalL1 μ →ₗ[ℂ] ℂ).mkContinuous (t ^ j)
    (moment_integral_bound μ t ht j)

theorem moment_apply (μ : Measure ℝ) (t : ℝ) (ht0 : 0 ≤ t)
    (ht : ∀ᵐ x ∂μ, |x| ≤ t) (j : ℕ) (f : PhysicalL1 μ) :
    moment μ t ht0 ht j f = ∫ x, (x : ℂ) ^ j * f x ∂μ := rfl

theorem moment_norm (μ : Measure ℝ) (t : ℝ) (ht0 : 0 ≤ t)
    (ht : ∀ᵐ x ∂μ, |x| ≤ t) (j : ℕ) :
    ‖moment μ t ht0 ht j‖ ≤ t ^ j :=
  ContinuousLinearMap.opNorm_le_bound _ (by positivity)
    (moment_integral_bound μ t ht j)

noncomputable def frequencyMonomial (R : ℝ) (j : ℕ) : C(Band R, ℂ) :=
  ⟨fun u => (-Complex.I * ((u : ℝ) : ℂ)) ^ j / (j.factorial : ℂ),
    by fun_prop⟩

theorem frequencyMonomial_norm (R : ℝ) (hR : 0 ≤ R) (j : ℕ) :
    ‖frequencyMonomial R j‖ ≤ R ^ j / (j.factorial : ℝ) := by
  apply (ContinuousMap.norm_le _ (by positivity)).2
  intro u
  have hu : |(u : ℝ)| ≤ R := abs_le.mpr u.property
  change ‖(-Complex.I * ((u : ℝ) : ℂ)) ^ j / (j.factorial : ℂ)‖ ≤ _
  simp only [norm_div, norm_pow, norm_mul, norm_neg, Complex.norm_I,
    one_mul, Complex.norm_real, Real.norm_eq_abs, Complex.norm_natCast]
  gcongr

theorem moment_series_bound (μ : Measure ℝ) (t R : ℝ)
    (ht0 : 0 ≤ t) (hR : 0 ≤ R) (ht : ∀ᵐ x ∂μ, |x| ≤ t) (j : ℕ) :
    ‖moment μ t ht0 ht j‖ * ‖frequencyMonomial R j‖ ≤
      1 * ((R * t) ^ j / (j.factorial : ℝ)) := by
  calc
    _ ≤ t ^ j * (R ^ j / (j.factorial : ℝ)) :=
      mul_le_mul (moment_norm μ t ht0 ht j) (frequencyMonomial_norm R hR j)
        (norm_nonneg _) (by positivity)
    _ = _ := by rw [mul_pow]; ring

noncomputable def boundedFourier (μ : Measure ℝ) (t R : ℝ)
    (ht0 : 0 ≤ t) (ht : ∀ᵐ x ∂μ, |x| ≤ t) :
    PhysicalL1 μ →L[ℂ] C(Band R, ℂ) :=
  ∑' j : ℕ, (moment μ t ht0 ht j).smulRight (frequencyMonomial R j)

theorem boundedFourier_compact (μ : Measure ℝ) (t R : ℝ)
    (ht0 : 0 ≤ t) (hR : 0 ≤ R) (ht : ∀ᵐ x ∂μ, |x| ≤ t) :
    IsCompactOperator (boundedFourier μ t R ht0 ht) :=
  (V08D.factorial_moment_series_compact (moment μ t ht0 ht)
    (frequencyMonomial R) 1 (R * t) (by norm_num) (by positivity)
    (moment_series_bound μ t R ht0 hR ht)).2

theorem boundedFourier_integral (μ : Measure ℝ) (t R : ℝ)
    (ht0 : 0 ≤ t) (hR : 0 ≤ R) (ht : ∀ᵐ x ∂μ, |x| ≤ t)
    (f : PhysicalL1 μ) (u : Band R) :
    boundedFourier μ t R ht0 ht f u =
      ∫ x, V08D.fourierKernel (u : ℝ) x * f x ∂μ := by
  let F : ℕ → PhysicalL1 μ →L[ℂ] C(Band R, ℂ) :=
    fun j => (moment μ t ht0 ht j).smulRight (frequencyMonomial R j)
  have hs : Summable F :=
    (V08D.factorial_moment_series_compact (moment μ t ht0 ht)
      (frequencyMonomial R) 1 (R * t) (by norm_num) (by positivity)
      (moment_series_bound μ t R ht0 hR ht)).1
  let ev : (PhysicalL1 μ →L[ℂ] C(Band R, ℂ)) →L[ℂ] ℂ :=
    (ContinuousMap.evalCLM ℂ u).comp (ContinuousLinearMap.apply ℂ _ f)
  change ev (∑' j, F j) = _
  rw [ev.map_tsum hs]
  let q : ℕ → ℂ := fun j => frequencyMonomial R j u
  let g : ℕ → ℝ → ℂ := fun j x => q j * ((x : ℂ) ^ j * f x)
  have hi : ∀ j, Integrable (g j) μ :=
    fun j => (moment_integrable μ t ht j f).const_mul (q j)
  have hq : ∀ j, ‖q j‖ ≤ R ^ j / (j.factorial : ℝ) := fun j =>
    ((frequencyMonomial R j).norm_coe_le_norm u).trans (frequencyMonomial_norm R hR j)
  have hf : Integrable (fun x => f x) μ := memLp_one_iff_integrable.mp (Lp.memLp f)
  have hnorm : ∀ j, (∫ x, ‖g j x‖ ∂μ) ≤
      ‖f‖ * ((R * t) ^ j / (j.factorial : ℝ)) := by
    intro j
    rw [L1.norm_eq_integral_norm, mul_comm, ← integral_const_mul]
    apply integral_mono_ae (hi j).norm (hf.norm.const_mul _)
    filter_upwards [ht] with x hx
    have hp : |x| ^ j ≤ t ^ j := by gcongr
    have hh : ‖q j‖ * |x| ^ j ≤ (R * t) ^ j / (j.factorial : ℝ) := by
      calc
        _ ≤ (R ^ j / (j.factorial : ℝ)) * t ^ j :=
          mul_le_mul (hq j) hp (by positivity) (by positivity)
        _ = _ := by rw [mul_pow]; ring
    change ‖q j * ((x : ℂ) ^ j * f x)‖ ≤ _
    rw [norm_mul, norm_mul, norm_pow, Complex.norm_real, Real.norm_eq_abs, ← mul_assoc]
    exact mul_le_mul_of_nonneg_right hh (norm_nonneg _)
  have hfac : Summable (fun j : ℕ => (R * t) ^ j / (j.factorial : ℝ)) := by
    have h := NormedSpace.norm_expSeries_div_summable (R * t)
    convert h using 1
    funext j
    rw [Real.norm_of_nonneg (by positivity)]
  have hsum : Summable (fun j => ∫ x, ‖g j x‖ ∂μ) :=
    Summable.of_nonneg_of_le (fun j => integral_nonneg fun x => norm_nonneg _)
      hnorm (hfac.mul_left ‖f‖)
  calc
    (∑' j, ev (F j)) = ∑' j, ∫ x, g j x ∂μ := by
      apply tsum_congr
      intro j
      change (moment μ t ht0 ht j f) * q j = _
      rw [moment_apply]
      change _ = ∫ x, q j * ((x : ℂ) ^ j * f x) ∂μ
      rw [integral_const_mul, mul_comm]
    _ = ∫ x, (∑' j, g j x) ∂μ := integral_tsum_of_summable_integral_norm hi hsum
    _ = _ := by
      apply integral_congr_ae
      filter_upwards with x
      let z : ℂ := -Complex.I * ((u : ℝ) : ℂ) * (x : ℂ)
      have he : (∑' j : ℕ, g j x) = ∑' j : ℕ, (z ^ j / (j.factorial : ℂ)) * f x := by
        apply tsum_congr
        intro j
        change ((-Complex.I * ((u : ℝ) : ℂ)) ^ j / (j.factorial : ℂ)) *
          ((x : ℂ) ^ j * f x) = _
        unfold z
        rw [mul_pow]
        ring
      rw [he, tsum_mul_right]
      change (∑' j : ℕ, z ^ j / (j.factorial : ℂ)) * f x = Complex.exp z * f x
      rw [Complex.exp_eq_exp_ℂ, NormedSpace.exp_eq_tsum_div]

end WeilDefect.MasterRecon.V08E

#print axioms WeilDefect.MasterRecon.V08E.moment_integrable
#print axioms WeilDefect.MasterRecon.V08E.moment_integral_bound
#print axioms WeilDefect.MasterRecon.V08E.moment_apply
#print axioms WeilDefect.MasterRecon.V08E.moment_norm
#print axioms WeilDefect.MasterRecon.V08E.frequencyMonomial_norm
#print axioms WeilDefect.MasterRecon.V08E.moment_series_bound
#print axioms WeilDefect.MasterRecon.V08E.boundedFourier_compact
#print axioms WeilDefect.MasterRecon.V08E.boundedFourier_integral
