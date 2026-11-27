import WeilDefect.MasterRecon.V09B
import Mathlib.MeasureTheory.Group.Measure

/-! RETURN108-L: literal translation of the supported logarithmic carrier.
Uses the existing physical L2 representative and weighted-spectrum lift.
No zero-count, critical-line supply or positivity assumption. Staged
candidate; native verification must precede use as a certified supplier. -/
namespace WeilDefect.MasterReturn.CarrierTranslation

open MeasureTheory Set Filter
open scoped FourierTransform ENNReal
open WeilDefect.MasterRecon
open V08I (FullL2 logCarrier physicalInclusion logWeight)

theorem shift_preserving (s : ℝ) :
    MeasurePreserving (fun x : ℝ => x-s) volume volume :=
  measurePreserving_sub_right volume s

noncomputable def shiftPhysical (s : ℝ) (f : FullL2) : FullL2 :=
  Lp.compMeasurePreserving (fun x : ℝ => x-s) (shift_preserving s) f

theorem shiftPhysical_ae (s : ℝ) (f : FullL2) :
    (shiftPhysical s f : ℝ → ℂ) =ᵐ[volume] V07A.translate s (f : ℝ → ℂ) :=
  Lp.coeFn_compMeasurePreserving f (shift_preserving s)

theorem shiftPhysical_support (a b s : ℝ) (hab : a+|s| ≤ b)
    (g : logCarrier a) :
    ∀ᵐ x ∂volume, x ∉ Icc (-b) b →
      shiftPhysical s (physicalInclusion a g) x = 0 := by
  have hs := (shift_preserving s).quasiMeasurePreserving.ae
    (V08I.physicalInclusion_support a g)
  filter_upwards [shiftPhysical_ae s (physicalInclusion a g), hs] with x hx hxs
  intro hout
  rw [hx]
  apply hxs
  intro hin
  apply hout
  have hbound : |x| ≤ |x-s|+|s| := by
    calc
      |x| = |(x-s)+s| := by ring_nf
      _ ≤ |x-s|+|s| := abs_add_le _ _
  exact abs_le.mp (hbound.trans (by linarith [abs_le.mpr hin]))

theorem shiftPhysical_mellin (s : ℝ) (f : FullL2) (z : ℂ) :
    V07A.mellin (shiftPhysical s f : ℝ → ℂ) z =
      Complex.exp (z*(s:ℂ)) * V07A.mellin (f : ℝ → ℂ) z := by
  rw [← V07A.mellin_translate]
  unfold V07A.mellin
  apply integral_congr_ae
  filter_upwards [shiftPhysical_ae s f] with x hx
  rw [hx]

/-- Literal Plancherel representatives have identical Fourier magnitudes.
The compact support supplies integrability on both physical windows. -/
theorem shiftPhysical_fourier_norm_ae (a b s : ℝ) (hab : a+|s| ≤ b)
    (g : logCarrier a) :
    (fun u : ℝ => ‖(𝓕 (shiftPhysical s (physicalInclusion a g)) : FullL2) u‖)
      =ᵐ[volume] fun u => ‖(𝓕 (physicalInclusion a g) : FullL2) u‖ := by
  let f := physicalInclusion a g
  let h := shiftPhysical s f
  have hf := V08K.supported_integrable a f (V08I.physicalInclusion_support a g)
  have hh := V08K.supported_integrable b h (shiftPhysical_support a b s hab g)
  filter_upwards [V08H.l2_fourier_integral_ae f hf,
    V08H.l2_fourier_integral_ae h hh] with u hu hv
  change ‖(𝓕 h : FullL2) u‖ = ‖(𝓕 f : FullL2) u‖
  rw [hv, hu, ← V08H.angularFourier_scaled, ← V08H.angularFourier_scaled,
    ← V09B.mellin_imaginary_axis, ← V09B.mellin_imaginary_axis]
  change ‖V07A.mellin (shiftPhysical s f : ℝ → ℂ)
      (-( (2*Real.pi*u : ℝ) : ℂ)*Complex.I)‖ = _
  rw [shiftPhysical_mellin, norm_mul, Complex.norm_exp]
  have hre : ((-((2*Real.pi*u : ℝ):ℂ)*Complex.I)*(s:ℂ)).re = 0 := by
    simp [Complex.mul_re, Complex.mul_im]
  rw [hre, Real.exp_zero, one_mul]

theorem shiftPhysical_log_integrable (a b s : ℝ) (hab : a+|s| ≤ b)
    (g : logCarrier a) :
    Integrable (fun u => logWeight u *
      ‖(𝓕 (shiftPhysical s (physicalInclusion a g)) : FullL2) u‖^2) := by
  apply (V08I.logCarrier_energy_integrable a g).congr
  filter_upwards [shiftPhysical_fourier_norm_ae a b s hab g] with u hu
  change ‖(𝓕 (shiftPhysical s (physicalInclusion a g)) : FullL2) u‖ =
    ‖(𝓕 (physicalInclusion a g) : FullL2) u‖ at hu
  rw [hu]

noncomputable def shiftCarrier (a b s : ℝ) (hab : a+|s| ≤ b)
    (g : logCarrier a) : logCarrier b :=
  V08J.liftPhysical b (shiftPhysical s (physicalInclusion a g))
    (shiftPhysical_support a b s hab g)
    (shiftPhysical_log_integrable a b s hab g)

theorem shiftCarrier_physical (a b s : ℝ) (hab : a+|s| ≤ b)
    (g : logCarrier a) :
    physicalInclusion b (shiftCarrier a b s hab g) =
      shiftPhysical s (physicalInclusion a g) :=
  V08J.physicalInclusion_lift _ _ _ _

theorem shiftCarrier_mellin (a b s : ℝ) (hab : a+|s| ≤ b)
    (g : logCarrier a) (z : ℂ) :
    V07A.mellin (physicalInclusion b (shiftCarrier a b s hab g) : ℝ → ℂ) z =
      Complex.exp (z*(s:ℂ)) *
        V07A.mellin (physicalInclusion a g : ℝ → ℂ) z := by
  rw [shiftCarrier_physical, shiftPhysical_mellin]

theorem shiftCarrier_norm (a b s : ℝ) (hab : a+|s| ≤ b)
    (g : logCarrier a) : ‖shiftCarrier a b s hab g‖ = ‖g‖ := by
  have he : ‖shiftCarrier a b s hab g‖^2 = ‖g‖^2 := by
    rw [V08I.logCarrier_energy, V08I.logCarrier_energy, shiftCarrier_physical]
    apply integral_congr_ae
    filter_upwards [shiftPhysical_fourier_norm_ae a b s hab g] with u hu
    change ‖(𝓕 (shiftPhysical s (physicalInclusion a g)) : FullL2) u‖ =
      ‖(𝓕 (physicalInclusion a g) : FullL2) u‖ at hu
    rw [hu]
  nlinarith [norm_nonneg (shiftCarrier a b s hab g), norm_nonneg g]

end WeilDefect.MasterReturn.CarrierTranslation

#print axioms WeilDefect.MasterReturn.CarrierTranslation.shift_preserving
#print axioms WeilDefect.MasterReturn.CarrierTranslation.shiftPhysical_ae
#print axioms WeilDefect.MasterReturn.CarrierTranslation.shiftPhysical_support
#print axioms WeilDefect.MasterReturn.CarrierTranslation.shiftPhysical_mellin
#print axioms WeilDefect.MasterReturn.CarrierTranslation.shiftPhysical_fourier_norm_ae
#print axioms WeilDefect.MasterReturn.CarrierTranslation.shiftPhysical_log_integrable
#print axioms WeilDefect.MasterReturn.CarrierTranslation.shiftCarrier_physical
#print axioms WeilDefect.MasterReturn.CarrierTranslation.shiftCarrier_mellin
#print axioms WeilDefect.MasterReturn.CarrierTranslation.shiftCarrier_norm
