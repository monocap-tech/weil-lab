import WeilDefect.Arithmetic.ActualZetaOriginalEndpointMollifier

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped Convolution

/-!
NF579: exact complex strip transform identities for the actual
affine compression and convolution. The convolution integrability
premise concerns the literal exponentially twisted factors, not a
hypothetical factorization of the source transform.
-/

private theorem neutralNF579AffineIntegral (f : ℝ → ℂ) (c s : ℝ)
    (hs : 0 < s) :
    (∫ x : ℝ, f (c+(x-c)/s)) = s • ∫ x : ℝ, f x := by
  let F : ℝ → ℂ := fun x => f (c-x)
  have he : (fun x : ℝ => f (c+(x-c)/s)) =
      (fun x : ℝ => F ((c-x)/s)) := by
    funext x
    dsimp [F]
    congr 1
    ring
  rw [he]
  calc
    _ = ∫ x : ℝ, F (x/s) :=
      integral_sub_left_eq_self (fun x : ℝ => F (x/s)) volume c
    _ = |s| • ∫ x : ℝ, F x := integral_comp_div F s
    _ = s • ∫ x : ℝ, f x := by
      rw [abs_of_pos hs]
      unfold F
      rw [integral_sub_left_eq_self f volume c]

/-- Exact affine compression sample identity, valid at complex z.
In particular, there is no dilation of the imaginary-width bound
outside the true strip when 0<s≤1. -/
theorem neutralNF579CompressedHalf_transform
    (h : ℝ → ℝ) (s : ℝ) (hs : 0 < s) (z : ℂ) :
    neutralNF579RawTransform (neutralNF578CompressedHalf h s) z =
      (s : ℂ) * Complex.exp
        (Complex.I * (z * (((1-s)*neutralNF578Center : ℝ) : ℂ))) *
      neutralNF579RawTransform h ((s:ℂ)*z) := by
  let c := neutralNF578Center
  let K := Complex.exp (Complex.I * (z * (((1-s)*c : ℝ) : ℂ)))
  let f : ℝ → ℂ := fun u => K * ((h u : ℂ) *
    Complex.exp (Complex.I * (((s:ℂ)*z)*(u:ℂ))))
  have he : (fun x : ℝ => (neutralNF578CompressedHalf h s x : ℂ) *
      Complex.exp (Complex.I * (z * (x:ℂ)))) =
      (fun x : ℝ => f (c+(x-c)/s)) := by
    funext x
    let u := c+(x-c)/s
    have hu : (1-s)*c+s*u = x := by
      dsimp [u]
      field_simp [hs.ne']
      ring
    have hphase : Complex.I * (z * (x:ℂ)) =
        Complex.I * (z * (((1-s)*c : ℝ):ℂ)) +
          Complex.I * (((s:ℂ)*z)*(u:ℂ)) := by
      rw [← hu]
      push_cast
      ring
    change (h u : ℂ) * Complex.exp (Complex.I * (z*(x:ℂ))) = f u
    rw [hphase, Complex.exp_add]
    dsimp [f,K]
    ring
  unfold neutralNF579RawTransform
  rw [he, neutralNF579AffineIntegral f c s hs]
  dsimp [f]
  rw [integral_const_mul]
  rw [Complex.real_smul]
  dsimp [K,c]
  ring

/-- Multiplying by a complex exponential intertwines the actual
convolution with the convolution of the two twisted factors.
Here the total-integral identity handles Fubini with both true
twisted functions integrable. -/
theorem neutralNF579ConvolvedHalf_transform
    (h ρ : ℝ → ℝ) (s : ℝ) (z : ℂ)
    (hρ : Integrable (fun x : ℝ => (ρ x : ℂ) *
      Complex.exp (Complex.I * (z*(x:ℂ)))) volume)
    (hh : Integrable (fun x : ℝ => (neutralNF578CompressedHalf h s x : ℂ) *
      Complex.exp (Complex.I * (z*(x:ℂ)))) volume) :
    neutralNF579RawTransform (neutralNF578ConvolvedHalf h ρ s) z =
      neutralNF579RawTransform ρ z *
        neutralNF579RawTransform (neutralNF578CompressedHalf h s) z := by
  let F : ℝ → ℂ := fun x => (ρ x : ℂ) * Complex.exp (Complex.I*(z*(x:ℂ)))
  let G : ℝ → ℂ := fun x => (neutralNF578CompressedHalf h s x : ℂ) *
    Complex.exp (Complex.I*(z*(x:ℂ)))
  have he : (fun x : ℝ => (neutralNF578ConvolvedHalf h ρ s x : ℂ) *
      Complex.exp (Complex.I * (z*(x:ℂ)))) =
      F ⋆[ContinuousLinearMap.mul ℂ ℂ, volume] G := by
    funext x
    unfold neutralNF578ConvolvedHalf
    rw [← integral_complex_ofReal, ← integral_mul_const]
    change (∫ y : ℝ, ((ρ y * neutralNF578CompressedHalf h s (x-y) : ℝ):ℂ) *
      Complex.exp (Complex.I*(z*(x:ℂ)))) = ∫ y, F y * G (x-y)
    apply integral_congr_ae
    filter_upwards [] with y
    have hphase : Complex.I*(z*(x:ℂ)) =
        Complex.I*(z*(y:ℂ))+Complex.I*(z*((x-y:ℝ):ℂ)) := by
      push_cast
      ring
    rw [hphase, Complex.exp_add]
    dsimp [F,G]
    push_cast
    ring
  unfold neutralNF579RawTransform
  rw [he]
  exact integral_convolution (ContinuousLinearMap.mul ℂ ℂ) hρ hh

end
end WeilDefect
