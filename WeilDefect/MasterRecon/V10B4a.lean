import WeilDefect.MasterRecon.V08H
import Mathlib.Analysis.Fourier.Inversion

/-! V10B4a: the Fourier product identity in Mathlib's cycle convention.
Only the multiplier and its transform need be L¹; the physical
input is L¹ but its Fourier transform need not be L¹. -/
namespace WeilDefect.MasterRecon.V10B4a

open MeasureTheory
open scoped FourierTransform

noncomputable def phase (y x : ℝ) : ℂ :=
  Complex.exp (↑(-2 * Real.pi * x * y) * Complex.I)

theorem phase_norm (y x : ℝ) : ‖phase y x‖ = 1 := by
  unfold phase
  exact Complex.norm_exp_ofReal_mul_I _

theorem phase_add (y u x : ℝ) :
    phase y x * phase u x = phase (y+u) x := by
  unfold phase
  rw [← Complex.exp_add]
  congr 1
  push_cast
  ring

theorem phase_integrable (f : ℝ → ℂ) (hf : Integrable f) (y : ℝ) :
    Integrable (fun x => phase y x * f x) := by
  apply hf.bdd_mul (c := 1)
  · unfold phase
    exact (show Continuous (fun x : ℝ =>
      Complex.exp (↑(-2 * Real.pi * x * y) * Complex.I)) by fun_prop).aestronglyMeasurable
  · exact ae_of_all _ (fun x => (phase_norm y x).le)

theorem fourier_modulated (f : ℝ → ℂ) (y u : ℝ) :
    𝓕 (fun x => phase y x * f x) u = 𝓕 f (y+u) := by
  rw [Real.fourier_real_eq_integral_exp_smul, Real.fourier_real_eq_integral_exp_smul]
  simp only [smul_eq_mul]
  apply integral_congr_ae
  filter_upwards with x
  change phase u x * (phase y x * f x) = phase (y+u) x * f x
  rw [← mul_assoc, phase_add, add_comm u y]

theorem integrable_reflected (K : ℝ → ℂ) (hK : Integrable K) :
    Integrable (fun u => K (-u)) := by
  simpa only [neg_one_mul] using hK.comp_mul_left' (R := (-1 : ℝ)) (by norm_num)

theorem integral_reflected (K : ℝ → ℂ) :
    (∫ u, K (-u)) = ∫ u, K u := by
  have h := Measure.integral_comp_mul_left K (-1 : ℝ)
  simpa using h

theorem fourier_reflected (K : ℝ → ℂ) (x : ℝ) :
    𝓕 (fun u => K (-u)) x = 𝓕⁻ K x := by
  change 𝓕 (fun u => K (-u)) x = _
  rw [Real.fourierInv_eq_fourier_comp_neg]

/-- Product-to-convolution without an L¹ hypothesis on the Fourier
transform of the input. The inverse multiplier identity is literal. -/
theorem fourier_product_of_inverse (p f K : ℝ → ℂ)
    (hf : Integrable f) (hK : Integrable K)
    (hinv : ∀ x, 𝓕⁻ K x = p x) (y : ℝ) :
    𝓕 (fun x => p x * f x) y = ∫ u, K u * 𝓕 f (y-u) := by
  let g : ℝ → ℂ := fun x => phase y x * f x
  have hg : Integrable g := phase_integrable f hf y
  have hpair := V08H.classical_fourier_pairing
    (fun u => K (-u)) g (integrable_reflected K hK) hg
  calc
    𝓕 (fun x => p x * f x) y =
        ∫ x, g x * 𝓕 (fun u => K (-u)) x := by
      rw [Real.fourier_real_eq_integral_exp_smul]
      apply integral_congr_ae
      filter_upwards with x
      rw [fourier_reflected, hinv]
      change phase y x * (p x * f x) = (phase y x * f x) * p x
      ring
    _ = ∫ u, 𝓕 g u * K (-u) := hpair.symm
    _ = ∫ u, 𝓕 f (y+u) * K (-u) := by
      apply integral_congr_ae
      filter_upwards with u
      rw [show 𝓕 g u = 𝓕 f (y+u) from fourier_modulated f y u]
    _ = ∫ u, K u * 𝓕 f (y-u) := by
      rw [← integral_reflected (fun u => K u * 𝓕 f (y-u))]
      apply integral_congr_ae
      filter_upwards with u
      simp only [sub_neg_eq_add, mul_comm]

theorem fourier_product (p f : ℝ → ℂ)
    (hp : Integrable p) (hpc : Continuous p) (hK : Integrable (𝓕 p))
    (hf : Integrable f) (y : ℝ) :
    𝓕 (fun x => p x * f x) y =
      ∫ u, 𝓕 p u * 𝓕 f (y-u) :=
  fourier_product_of_inverse p f (𝓕 p) hf hK
    (fun x => hp.fourierInv_fourier_eq hK (hpc.continuousAt (x := x))) y

end WeilDefect.MasterRecon.V10B4a

#print axioms WeilDefect.MasterRecon.V10B4a.phase_norm
#print axioms WeilDefect.MasterRecon.V10B4a.phase_add
#print axioms WeilDefect.MasterRecon.V10B4a.phase_integrable
#print axioms WeilDefect.MasterRecon.V10B4a.fourier_modulated
#print axioms WeilDefect.MasterRecon.V10B4a.integrable_reflected
#print axioms WeilDefect.MasterRecon.V10B4a.integral_reflected
#print axioms WeilDefect.MasterRecon.V10B4a.fourier_reflected
#print axioms WeilDefect.MasterRecon.V10B4a.fourier_product_of_inverse
#print axioms WeilDefect.MasterRecon.V10B4a.fourier_product
