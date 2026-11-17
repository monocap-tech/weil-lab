import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped Interval

/-!
NF584: exact endpoint-log mass and the proper-interval oscillatory
integration-by-parts estimate. Neither depends on pending original
seed/Gram modules. The primitive never crosses the singular endpoint.
-/

def neutralNF584LogKernel (B d : ℝ) : ℝ := Real.log B - Real.log d

theorem neutralNF584LogKernel_intervalIntegrable (B a b : ℝ) :
    IntervalIntegrable (neutralNF584LogKernel B) volume a b := by
  unfold neutralNF584LogKernel
  exact intervalIntegrable_const.sub intervalIntegral.intervalIntegrable_log'

theorem neutralNF584LogKernel_eq_ratio (B d : ℝ) (hB : 0 < B) (hd : 0 < d) :
    neutralNF584LogKernel B d = Real.log (B/d) := by
  unfold neutralNF584LogKernel
  rw [Real.log_div hB.ne' hd.ne']

theorem neutralNF584LogKernel_nonneg (B d : ℝ) (hd : 0 < d) (h : d ≤ B) :
    0 ≤ neutralNF584LogKernel B d := by
  unfold neutralNF584LogKernel
  exact sub_nonneg.mpr (Real.log_le_log hd h)

theorem neutralNF584LogKernel_zero_mass (B a : ℝ) :
    (∫ d in (0:ℝ)..a, neutralNF584LogKernel B d) =
      a*(neutralNF584LogKernel B a+1) := by
  unfold neutralNF584LogKernel
  rw [intervalIntegral.integral_sub intervalIntegrable_const
      intervalIntegral.intervalIntegrable_log',
    intervalIntegral.integral_const, integral_log_from_zero]
  simp <;> ring

/-- The short near-singularity panel pays exactly a log mass,
not a bound on the singular integrand at zero. -/
theorem neutralNF584NearPanel (A : ℝ → ℂ) (B a C : ℝ)
    (ha : 0 < a) (haB : a ≤ B)
    (hA : ∀ d ∈ Icc (0:ℝ) a, ‖A d‖ ≤ C) (t : ℝ) :
    ‖∫ d in (0:ℝ)..a, A d * (neutralNF584LogKernel B d : ℂ) *
      Complex.exp (-(Complex.I * (t:ℂ)) * (d:ℂ))‖ ≤
      C*a*(neutralNF584LogKernel B a+1) := by
  have h := intervalIntegral.norm_integral_le_of_norm_le
    (f := fun d : ℝ => A d * (neutralNF584LogKernel B d:ℂ) *
      Complex.exp (-(Complex.I*(t:ℂ))*(d:ℂ)))
    (g := fun d : ℝ => C*neutralNF584LogKernel B d)
    ha.le (by
      filter_upwards [] with d hd
      have hl := neutralNF584LogKernel_nonneg B d hd.1 (hd.2.trans haB)
      have hp : ‖Complex.exp (-(Complex.I*(t:ℂ))*(d:ℂ))‖ = 1 := by
        rw [Complex.norm_exp]
        simp [Complex.mul_re, Complex.mul_im]
      rw [norm_mul,norm_mul,hp,mul_one,Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg hl]
      exact mul_le_mul_of_nonneg_right (hA d ⟨hd.1.le,hd.2⟩) hl)
    ((neutralNF584LogKernel_intervalIntegrable B 0 a).const_mul C)
  calc
    _ ≤ ∫ d in (0:ℝ)..a, C*neutralNF584LogKernel B d := h
    _ = _ := by
      rw [intervalIntegral.integral_const_mul, neutralNF584LogKernel_zero_mass]
      ring

def neutralNF584Phase (t d : ℝ) : ℂ :=
  Complex.exp (-(Complex.I*(t:ℂ))*(d:ℂ))

theorem neutralNF584Phase_norm (t d : ℝ) : ‖neutralNF584Phase t d‖ = 1 := by
  unfold neutralNF584Phase
  rw [Complex.norm_exp]
  simp [Complex.mul_re,Complex.mul_im]

theorem neutralNF584Phase_deriv (t d : ℝ) :
    HasDerivAt (neutralNF584Phase t)
      (neutralNF584Phase t d * (-(Complex.I*(t:ℂ)))) d := by
  unfold neutralNF584Phase
  have h : HasDerivAt (fun x : ℝ => -(Complex.I*(t:ℂ))*(x:ℂ))
      (-(Complex.I*(t:ℂ))) d := by
    have hc : HasDerivAt (fun x : ℝ => (x:ℂ)) (1:ℂ) d :=
      Complex.ofRealCLM.hasDerivAt
    simpa only [mul_one] using hc.const_mul (-(Complex.I*(t:ℂ)))
  exact h.cexp

/-- Proper interval estimate with the exact complex plane wave.
This generic integration-by-parts lemma keeps the endpoint traces
and derivative L1 norm separate; the singular panel is not in its
domain. -/
theorem neutralNF584OscillatoryPanel
    (b b' : ℝ → ℂ) (a δ t : ℝ) (ha : a ≤ δ)
    (hb : ∀ d ∈ uIcc a δ, HasDerivAt b (b' d) d)
    (hi : IntervalIntegrable b' volume a δ) :
    |t| * ‖∫ d in a..δ, b d * neutralNF584Phase t d‖ ≤
      ‖b δ‖ + ‖b a‖ + ∫ d in a..δ, ‖b' d‖ := by
  let k : ℂ := -(Complex.I*(t:ℂ))
  let P := neutralNF584Phase t
  have hc : Continuous P := by
    unfold P neutralNF584Phase
    fun_prop
  have hd : ∀ d ∈ uIcc a δ, HasDerivAt P (P d*k) d :=
    fun d _ => neutralNF584Phase_deriv t d
  have hdc : Continuous (fun d => P d*k) := hc.mul continuous_const
  have h := intervalIntegral.integral_mul_deriv_eq_deriv_mul hb hd hi
    hdc.continuousOn.intervalIntegrable
  have he : (∫ d in a..δ, b d*P d)*k =
      b δ*P δ-b a*P a-(∫ d in a..δ, b' d*P d) := by
    rw [← intervalIntegral.integral_mul_const]
    simpa only [mul_assoc] using h
  have hk : ‖k‖ = |t| := by
    simp [k,norm_mul,Complex.norm_real,Real.norm_eq_abs]
  have hn : ‖∫ d in a..δ, b' d*P d‖ ≤ ∫ d in a..δ, ‖b' d‖ := by
    calc
      _ ≤ ∫ d in a..δ, ‖b' d*P d‖ :=
        intervalIntegral.norm_integral_le_integral_norm ha
      _ = _ := by
        apply intervalIntegral.integral_congr
        intro d _
        change ‖b' d * P d‖ = ‖b' d‖
        rw [norm_mul,show ‖P d‖ = 1 from neutralNF584Phase_norm t d,mul_one]
  calc
    _ = ‖(∫ d in a..δ, b d*P d)*k‖ := by
      rw [norm_mul,hk,mul_comm]
    _ = ‖b δ*P δ-b a*P a-(∫ d in a..δ, b' d*P d)‖ := by rw [he]
    _ ≤ ‖b δ*P δ-b a*P a‖+‖∫ d in a..δ, b' d*P d‖ := norm_sub_le _ _
    _ ≤ (‖b δ*P δ‖+‖b a*P a‖)+(∫ d in a..δ, ‖b' d‖) :=
      add_le_add (norm_sub_le _ _) hn
    _ = _ := by simp only [norm_mul,show ∀ d, ‖P d‖ = 1 from neutralNF584Phase_norm t,mul_one]

end
end WeilDefect
