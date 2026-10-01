import WeilDefect.Morphology.NeutralGaussianSchwartz
import Mathlib.Analysis.Asymptotics.SpecificAsymptotics
import Mathlib.Analysis.Asymptotics.SuperpolynomialDecay
import Mathlib.Analysis.SpecialFunctions.Gaussian.PoissonSummation
import Mathlib.RingTheory.Polynomial.Hermite.Gaussian

namespace WeilDefect

noncomputable section

open Filter Set
open Asymptotics Polynomial
open scoped SchwartzMap Topology ContDiff

/-- Standard real Gaussian used to seed the project moving Gaussian kernel. -/
def standardGaussianReal (x : ℝ) : ℝ :=
  Real.exp (-(x ^ 2 / 2))

lemma standardGaussianReal_superpolynomialDecay :
    SuperpolynomialDecay (cocompact ℝ) id standardGaussianReal := by
  rw [superpolynomialDecay_iff_norm_tendsto_zero]
  intro n
  have h := tendsto_rpow_abs_mul_exp_neg_mul_sq_cocompact
    (a := (1 / 2 : ℝ)) (by norm_num) (n : ℝ)
  have h' : Tendsto (fun x : ℝ => |x| ^ (n : ℝ) * standardGaussianReal x)
      (cocompact ℝ) (𝓝 0) := by
    refine h.congr' (Eventually.of_forall fun x => ?_)
    unfold standardGaussianReal
    congr 2
    ring
  simpa [standardGaussianReal, Real.norm_eq_abs, abs_mul, abs_pow, Real.rpow_natCast,
    abs_of_pos] using h'

lemma iter_deriv_standardGaussianReal (n : ℕ) (x : ℝ) :
    deriv^[n] standardGaussianReal x =
      (-1 : ℝ) ^ n * aeval x (hermite n) * standardGaussianReal x := by
  change deriv^[n] (fun y : ℝ => Real.exp (-(y ^ 2 / 2))) x =
    (-1 : ℝ) ^ n * aeval x (hermite n) * Real.exp (-(x ^ 2 / 2))
  exact Polynomial.deriv_gaussian_eq_hermite_mul_gaussian n x

/-- The standard real Gaussian, bundled in Schwartz space. -/
def standardGaussianSchwartzReal : 𝓢(ℝ, ℝ) where
  toFun := standardGaussianReal
  smooth' := by
    unfold standardGaussianReal
    fun_prop
  decay' k n := by
    let p : ℝ[X] := X ^ k * C ((-1 : ℝ) ^ n) *
      (hermite n).map (Int.castRingHom ℝ)
    have hp_decay : SuperpolynomialDecay (cocompact ℝ) id
        (fun x : ℝ => p.eval x * standardGaussianReal x) := by
      simpa only [Function.comp_apply, id_eq] using
        standardGaussianReal_superpolynomialDecay.polynomial_mul p
    have hp_tendsto : Tendsto
        (fun x : ℝ => ‖p.eval x * standardGaussianReal x‖)
        (cocompact ℝ) (𝓝 0) := by
      exact tendsto_zero_iff_norm_tendsto_zero.mp (by simpa using hp_decay 0)
    have hp_cont : Continuous (fun x : ℝ => ‖p.eval x * standardGaussianReal x‖) := by
      unfold standardGaussianReal
      fun_prop
    have hp_bounded : Bornology.IsBounded (range fun x : ℝ =>
        ‖p.eval x * standardGaussianReal x‖) :=
      hp_cont.isBounded_range_iff_isBigO.mpr (hp_tendsto.isBigO_one ℝ)
    rw [isBounded_iff_forall_norm_le] at hp_bounded
    obtain ⟨C, hC⟩ := hp_bounded
    refine ⟨C, fun x => ?_⟩
    have hx := hC ‖p.eval x * standardGaussianReal x‖ ⟨x, rfl⟩
    rw [norm_norm] at hx
    convert hx using 1
    simp only [Real.norm_eq_abs, norm_iteratedFDeriv_eq_norm_iteratedDeriv,
      iteratedDeriv_eq_iterate, iter_deriv_standardGaussianReal]
    simp [p, eval_mul, eval_pow, eval_X, eval_map, aeval_def, abs_mul,
      standardGaussianReal, abs_of_pos]
    ring

@[simp]
theorem standardGaussianSchwartzReal_apply (x : ℝ) :
    standardGaussianSchwartzReal x = Real.exp (-(x ^ 2 / 2)) :=
  rfl

/-- The centered real Gaussian with the project physical width exp(-R x^2 / 4). -/
def projectCenteredGaussianSchwartzReal (R : ℝ) (hR : 0 < R) : 𝓢(ℝ, ℝ) := by
  let c : ℝ := Real.sqrt (R / 2)
  have hc : c ≠ 0 := by
    exact ne_of_gt (Real.sqrt_pos.2 (div_pos hR two_pos))
  exact SchwartzMap.compCLMOfContinuousLinearEquiv ℝ
    (ContinuousLinearEquiv.smulLeft (Units.mk0 c hc)) standardGaussianSchwartzReal

@[simp]
theorem projectCenteredGaussianSchwartzReal_apply
    (R : ℝ) (hR : 0 < R) (x : ℝ) :
    projectCenteredGaussianSchwartzReal R hR x =
      Real.exp (-R * x ^ 2 / 4) := by
  change standardGaussianReal (Real.sqrt (R / 2) * x) =
    Real.exp (-R * x ^ 2 / 4)
  unfold standardGaussianReal
  have hsqrt : Real.sqrt (R / 2) ^ 2 = R / 2 := by
    rw [Real.sq_sqrt (div_nonneg hR.le (by norm_num))]
  congr 1
  rw [mul_pow, hsqrt]
  ring

/-- Complexification of the project centered Gaussian. -/
def projectCenteredGaussianSchwartz
    (R : ℝ) (hR : 0 < R) : 𝓢(ℝ, ℂ) :=
  (projectCenteredGaussianSchwartzReal R hR).postcompCLM Complex.ofRealCLM

@[simp]
theorem projectCenteredGaussianSchwartz_apply
    (R : ℝ) (hR : 0 < R) (x : ℝ) :
    projectCenteredGaussianSchwartz R hR x =
      (Real.exp (-R * x ^ 2 / 4) : ℂ) := by
  rw [projectCenteredGaussianSchwartz, SchwartzMap.postcompCLM_apply,
    projectCenteredGaussianSchwartzReal_apply]
  simp only [Complex.ofRealCLM_apply]

/-- The oscillatory phase in the project moving Gaussian kernel is temperate. -/
theorem movingGaussianPhase_hasTemperateGrowth (R : ℝ) :
    Function.HasTemperateGrowth
      (fun z : ℝ =>
        Complex.exp (((R * z : ℝ) : ℂ) * Complex.I)) := by
  have hlin : Function.HasTemperateGrowth (fun z : ℝ => R * z) := by
    fun_prop
  simpa only [Function.comp_def] using
    Complex.hasTemperateGrowth_exp_mul_I.comp hlin

/-- The exact physical moving Gaussian kernel, bundled as a Schwartz map. -/
def movingGaussianPhysicalKernelSchwartz
    (Ck : ℂ) (R : ℝ) (hR : 0 < R) : 𝓢(ℝ, ℂ) :=
  (Ck * (Real.sqrt R : ℂ)) •
    SchwartzMap.smulLeftCLM ℂ
      (fun z : ℝ =>
        Complex.exp (((R * z : ℝ) : ℂ) * Complex.I))
      (projectCenteredGaussianSchwartz R hR)

@[simp]
theorem movingGaussianPhysicalKernelSchwartz_apply
    (Ck : ℂ) (R : ℝ) (hR : 0 < R) (z : ℝ) :
    movingGaussianPhysicalKernelSchwartz Ck R hR z =
      movingGaussianPhysicalKernel Ck R z := by
  rw [movingGaussianPhysicalKernelSchwartz, smul_apply]
  rw [SchwartzMap.smulLeftCLM_apply_apply
    (movingGaussianPhase_hasTemperateGrowth R)]
  rw [projectCenteredGaussianSchwartz_apply]
  unfold movingGaussianPhysicalKernel
  simp only [smul_eq_mul]
  have hz : |z| ^ 2 = z ^ 2 := sq_abs z
  rw [hz]
  ring

end

end WeilDefect
