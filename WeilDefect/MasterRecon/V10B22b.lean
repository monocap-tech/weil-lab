import WeilDefect.MasterRecon.V10B22a
import WeilDefect.MasterRecon.V08H
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap

/-! V10B22b: literal Fourier translation phase and Bochner commutation.
No evaluation functional on L² is used. -/
namespace WeilDefect.MasterRecon.V10B22b

open MeasureTheory Set Filter Complex
open scoped FourierTransform InnerProduct
open V08I (FullL2)
open V10B8d (shift)
open V10B21c (actionTerm numerator denominator)

noncomputable def U : FullL2 →L[ℂ] FullL2 :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).toContinuousLinearMap

noncomputable def phase (r u : ℝ) : ℂ :=
  Complex.exp (((2*Real.pi*r*u:ℝ):ℂ)*I)

theorem phase_norm (r u : ℝ) : ‖phase r u‖ = 1 := by
  unfold phase
  rw [Complex.norm_exp]
  simp [Complex.mul_re,Complex.mul_im]

theorem classical_shift (f : ℝ → ℂ) (r u : ℝ) :
    𝓕 (fun x => f (x+r)) u = phase r u * 𝓕 f u := by
  have h := congrFun (VectorFourier.fourierIntegral_comp_add_right
    Real.fourierChar (volume : Measure ℝ) (innerₗ ℝ) f r) u
  change 𝓕 (fun x => f (x+r)) u = _ at h
  rw [h]
  simp only [phase,Circle.smul_def,Real.fourierChar_apply,smul_eq_mul,
    real_inner_comm,Real.inner_apply]
  congr 2
  push_cast
  ring

theorem shift_integrable (f : FullL2) (hf : Integrable (fun x : ℝ => f x)) (r : ℝ) :
    Integrable (fun x : ℝ => shift r f x) := by
  have h := (measurePreserving_add_right (volume : Measure ℝ) r).integrable_comp
    (MeasurableEquiv.addRight r).measurableEmbedding
  exact (h.mpr hf).congr (V10B8d.shift_ae r f).symm

theorem fourier_shift_ae (f : FullL2) (hf : Integrable (fun x : ℝ => f x)) (r : ℝ) :
    (U (shift r f) : ℝ → ℂ) =ᵐ[volume] fun u => phase r u * (U f) u := by
  filter_upwards [V08H.l2_fourier_integral_ae f hf,
    V08H.l2_fourier_integral_ae (shift r f) (shift_integrable f hf r)] with u h₁ h₂
  change (𝓕 (shift r f) : FullL2) u = phase r u * (𝓕 f : FullL2) u
  rw [h₁,h₂,Real.fourier_congr_ae (V10B8d.shift_ae r f) u,classical_shift]

noncomputable def symbol (r u : ℝ) : ℂ :=
  ((denominator r)⁻¹:ℝ) •
    (((2*Real.exp (-2*r):ℝ):ℂ)-
      (Real.exp (-r/2):ℂ)*(phase r u+phase (-r) u))

theorem symbol_fourier_ae (f : FullL2) (hf : Integrable (fun x : ℝ => f x)) (r : ℝ) :
    (U (actionTerm f r) : ℝ → ℂ) =ᵐ[volume] fun u => symbol r u * (U f) u := by
  let a : ℝ := (denominator r)⁻¹
  let b : ℝ := 2*Real.exp (-2*r)
  let c : ℝ := Real.exp (-r/2)
  let x := U f
  let y := U (shift r f)
  let z := U (shift (-r) f)
  have he : U (actionTerm f r) = a • (b • x-c • (y+z)) := by
    unfold actionTerm numerator a b c x y z
    simp only [map_smul_of_tower,map_sub,map_add]
  rw [he]
  filter_upwards [Lp.coeFn_smul a (b • x-c • (y+z)),
    Lp.coeFn_sub (b • x) (c • (y+z)), Lp.coeFn_smul b x,
    Lp.coeFn_smul c (y+z), Lp.coeFn_add y z,
    fourier_shift_ae f hf r, fourier_shift_ae f hf (-r)] with u h₁ h₂ h₃ h₄ h₅ h₆ h₇
  rw [h₁,h₂,h₃,h₄,h₅]
  change y u = phase r u * x u at h₆
  change z u = phase (-r) u * x u at h₇
  rw [h₆,h₇]
  unfold symbol
  simp only [Complex.real_smul]
  dsimp [a,b,c,x]
  ring

noncomputable def integratedAction (f : FullL2) : FullL2 :=
  ∫ r in Ioi (0:ℝ), actionTerm f r

theorem fourier_integral_comm (f : FullL2)
    (hf : IntegrableOn (actionTerm f) (Ioi 0)) :
    U (integratedAction f) = ∫ r in Ioi (0:ℝ), U (actionTerm f r) :=
  (U.integral_comp_comm hf).symm

theorem fourier_pairing_comm (f k : FullL2)
    (hf : IntegrableOn (actionTerm f) (Ioi 0)) :
    inner ℂ k (U (integratedAction f)) =
      ∫ r in Ioi (0:ℝ), inner ℂ k (U (actionTerm f r)) := by
  change ((innerSL ℂ k).comp U) (integratedAction f) = _
  exact (((innerSL ℂ k).comp U).integral_comp_comm hf).symm

end WeilDefect.MasterRecon.V10B22b

#print axioms WeilDefect.MasterRecon.V10B22b.phase_norm
#print axioms WeilDefect.MasterRecon.V10B22b.classical_shift
#print axioms WeilDefect.MasterRecon.V10B22b.shift_integrable
#print axioms WeilDefect.MasterRecon.V10B22b.fourier_shift_ae
#print axioms WeilDefect.MasterRecon.V10B22b.symbol_fourier_ae
#print axioms WeilDefect.MasterRecon.V10B22b.fourier_integral_comm
#print axioms WeilDefect.MasterRecon.V10B22b.fourier_pairing_comm
