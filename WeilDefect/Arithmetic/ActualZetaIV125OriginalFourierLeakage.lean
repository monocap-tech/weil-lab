import WeilDefect.Arithmetic.ActualZetaIV124OriginalPhysicalTailBudget
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap FourierTransform

/-- A zero cell mean permits exact subtraction of any constant phase. -/
theorem neutralIV125Cell_cancel (f p : ℝ → ℂ) (μ : Measure ℝ) (c : ℂ)
    (hf : Integrable f μ) (hp : Integrable (fun x => p x * f x) μ)
    (hm : (∫ x, f x ∂μ) = 0) :
    (∫ x, (p x - c) * f x ∂μ) = ∫ x, p x * f x ∂μ := by
  simp_rw [sub_mul]
  rw [integral_sub hp (hf.const_mul c), integral_const_mul, hm, mul_zero, sub_zero]

/-- Single-cell leakage payment, for a separately established phase bound. -/
theorem neutralIV125Cell_bound (f p : ℝ → ℂ) (μ : Measure ℝ) (c : ℂ) (d : ℝ)
    (hf : Integrable f μ) (hp : Integrable (fun x => p x * f x) μ)
    (hm : (∫ x, f x ∂μ) = 0)
    (hd : ∀ᵐ x ∂μ, ‖p x - c‖ ≤ d) :
    ‖∫ x, p x * f x ∂μ‖ ≤ d * ∫ x, ‖f x‖ ∂μ := by
  rw [← neutralIV125Cell_cancel f p μ c hf hp hm]
  have hi : Integrable (fun x => (p x - c) * f x) μ := by
    have hfun : (fun x : ℝ => (p x - c) * f x) =
        ((fun x : ℝ => p x * f x) - (fun x : ℝ => c * f x)) := by
      funext x
      change (p x - c) * f x = p x * f x - c * f x
      ring
    rw [hfun]
    exact hp.sub (hf.const_mul c)
  refine (norm_integral_le_integral_norm (μ := μ) _).trans ?_
  rw [← integral_const_mul]
  apply integral_mono_ae hi.norm (hf.norm.const_mul d)
  filter_upwards [hd] with x hx
  rw [norm_mul]
  exact mul_le_mul_of_nonneg_right hx (norm_nonneg _)

/-- Integrate an actual pointwise Fourier squared-mass bound over the band.
Ioc is used so the polynomial integral is exactly an interval integral. -/
theorem neutralIV125LowBand_of_pointwise (v : 𝓢(ℝ,ℂ)) (T C : ℝ)
    (hT : 0 ≤ T)
    (hpoint : ∀ ξ ∈ Set.Ioc (-T) T,
      ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2 ≤ C * ξ^2) :
    (∫ ξ in Set.Ioc (-T) T,
      ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2) ≤ C * (2*T^3/3) := by
  have hf : Integrable (fun ξ : ℝ =>
      ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2) :=
    (memLp_two_iff_integrable_sq_norm
      (Lp.aestronglyMeasurable (𝓕 (v.toLp 2 volume) : RealComplexL2))).mp (Lp.memLp _)
  have hp : IntegrableOn (fun ξ : ℝ => ξ^2) (Set.Ioc (-T) T) :=
    ((continuous_id.pow 2).intervalIntegrable (-T) T).1
  have hc : (∫ ξ in Set.Ioc (-T) T, C * ξ^2) = C * (2*T^3/3) := by
    rw [← intervalIntegral.integral_of_le (by linarith : -T ≤ T),
      intervalIntegral.integral_const_mul, integral_pow]
    norm_num <;> ring_nf <;> simp
  rw [← hc]
  exact setIntegral_mono_on hf.integrableOn (hp.const_mul C) measurableSet_Ioc hpoint

/-- Plancherel mass outside the actual band gives a logarithmic energy floor. -/
theorem neutralIV125LogLower_of_leakage (a : ℝ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0)
    (T eps : ℝ) (hT : 0 ≤ T)
    (hLeak : (∫ ξ in Set.Ioc (-T) T,
      ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2) ≤
        eps * ‖v.toLp 2 volume‖^2) :
    ((1-eps)*Real.log (Real.exp 1+T))*‖v.toLp 2 volume‖^2 ≤
      ‖neutralIV102Lift a v hv‖^2 := by
  let F : ℝ → ℝ := fun ξ => ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2
  let w : ℝ → ℝ := logarithmicFourierWeight
  let I : Set ℝ := Set.Ioc (-T) T
  let L : ℝ := Real.log (Real.exp 1 + T)
  have hf : Integrable F :=
    (memLp_two_iff_integrable_sq_norm
      (Lp.aestronglyMeasurable (𝓕 (v.toLp 2 volume) : RealComplexL2))).mp (Lp.memLp _)
  have hw : Integrable (fun ξ => w ξ * F ξ) :=
    (neutralIV102Canonical a v hv).property.2
  have hmass : (∫ ξ, F ξ) = ‖v.toLp 2 volume‖^2 := by
    dsimp [F]
    rw [← neutralPhysicalL2_norm_sq, Lp.norm_fourier_eq]
  have hI : MeasurableSet I := measurableSet_Ioc
  have hsplit := integral_add_compl hI hf
  have hsplitw := integral_add_compl hI hw
  have hL : 0 ≤ L := by
    apply Real.log_nonneg
    have he := Real.add_one_le_exp (1:ℝ)
    linarith
  have hband : 0 ≤ ∫ ξ in I, w ξ * F ξ := by
    apply integral_nonneg
    intro ξ
    exact mul_nonneg (le_trans (by norm_num) (one_le_logarithmicFourierWeight ξ))
      (sq_nonneg _)
  have hout : (∫ ξ in Iᶜ, L * F ξ) ≤ ∫ ξ in Iᶜ, w ξ * F ξ := by
    apply setIntegral_mono_on (hf.const_mul L).integrableOn hw.integrableOn hI.compl
    intro ξ hx
    have hξ : T ≤ |ξ| := by
      by_contra hn
      have hab := abs_lt.mp (lt_of_not_ge hn)
      exact hx ⟨hab.1, hab.2.le⟩
    apply mul_le_mul_of_nonneg_right _ (sq_nonneg _)
    dsimp [L, w, logarithmicFourierWeight]
    exact Real.log_le_log (by positivity) (add_le_add_right hξ _)
  rw [integral_const_mul] at hout
  change (∫ ξ in I, F ξ) ≤ eps * ‖v.toLp 2 volume‖^2 at hLeak
  have htail : (1-eps)*‖v.toLp 2 volume‖^2 ≤ ∫ ξ in Iᶜ, F ξ := by
    rw [hmass] at hsplit
    linarith only [hLeak, hsplit]
  have hpay := mul_le_mul_of_nonneg_left htail hL
  rw [neutralIV102Lift_log_norm]
  change ((1-eps)*L)*‖v.toLp 2 volume‖^2 ≤ ∫ ξ, w ξ * F ξ
  linarith only [hpay, hout, hband, hsplitw]

/-- Close the actual IV124 Schur tail receiver from a certified band payment. -/
theorem neutralIV125Schur_of_leakage (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (T eps eta : ℝ) (hT : 0 ≤ T)
    (hLeak : (∫ ξ in Set.Ioc (-T) T,
      ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2) ≤
        eps * ‖v.toLp 2 volume‖^2)
    (hmargin : eta ≤ (1-eps)*Real.log (Real.exp 1+T) -
      (neutralActualZetaNativeLogError (11/10:ℝ) +
       neutralPhysicalPoleEnergyConstant (11/10:ℝ) +
       neutralIV124PhysicalBudget k hk)) :
    eta * ‖v.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk v :=
  neutralIV124Schur_tail_of_log_lower k hk v hv _ eta
    (neutralIV125LogLower_of_leakage _ v hv T eps hT hLeak) hmargin

#print axioms neutralIV125Cell_cancel
#print axioms neutralIV125Cell_bound
#print axioms neutralIV125LowBand_of_pointwise
#print axioms neutralIV125LogLower_of_leakage
#print axioms neutralIV125Schur_of_leakage

end
end WeilDefect
