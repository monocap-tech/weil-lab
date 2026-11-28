import WeilDefect.MasterRecon.V10B73a
import WeilDefect.MasterRecon.V10B69a

/-! V10B74a: the actual divided trials belong to the square-log
spectral domain; construct the principal logarithmic spectrum. -/
namespace WeilDefect.MasterRecon.V10B74a
open MeasureTheory Set
open scoped ENNReal FourierTransform
open V08I (FullL2 physicalInclusion logWeight)
open V10B67a (carrierTrial trialL2 carrierTrial_physical)
open V10B69a (D dividedTrial)

noncomputable def F (j : Fin 16) : FullL2 :=
  (𝓕 (physicalInclusion (1/4) (dividedTrial j)) : FullL2)

theorem divided_spectrum (j : Fin 16) :
    F j = D⁻¹ • (𝓕 (trialL2 j) : FullL2) := by
  have h : physicalInclusion (1/4) (dividedTrial j) = D⁻¹ • trialL2 j := by
    rw [dividedTrial,map_smul,carrierTrial_physical]
  unfold F
  rw [h]
  exact (Lp.fourierTransformₗᵢ ℝ ℂ).map_smul D⁻¹ (trialL2 j)

theorem divided_spectrum_ae (j : Fin 16) :
    (F j : ℝ → ℂ) =ᵐ[volume] fun u => D⁻¹ * (𝓕 (trialL2 j) : FullL2) u := by
  rw [divided_spectrum]
  filter_upwards [Lp.coeFn_smul D⁻¹ (𝓕 (trialL2 j) : FullL2)] with u hu
  rw [hu,Pi.smul_apply,smul_eq_mul]

theorem divided_square_weighted (j : Fin 16) :
    Integrable (fun u => logWeight u ^ 2 * ‖F j u‖^2) := by
  apply ((V10B73a.trial_square_weighted j).const_mul (‖D⁻¹‖^2)).congr
  filter_upwards [divided_spectrum_ae j] with u hu
  change ‖D⁻¹‖^2 * (logWeight u ^ 2 * ‖(𝓕 (trialL2 j) : FullL2) u‖^2) =
    logWeight u ^ 2 * ‖F j u‖^2
  rw [hu,norm_mul,mul_pow]
  ring

theorem logSpectrum_mem (f : FullL2)
    (hf : Integrable (fun u => logWeight u ^ 2 * ‖f u‖^2)) :
    MemLp (fun u => (logWeight u : ℂ)*f u) 2 volume := by
  have hm : AEStronglyMeasurable (fun u => (logWeight u : ℂ)*f u) volume :=
    (Complex.continuous_ofReal.measurable.comp
      V08I.logWeight_continuous.measurable).aestronglyMeasurable.mul
        (Lp.aestronglyMeasurable f)
  apply (memLp_two_iff_integrable_sq_norm hm).2
  apply hf.congr
  filter_upwards with u
  change logWeight u ^ 2 * ‖f u‖^2 = ‖(logWeight u : ℂ)*f u‖^2
  rw [norm_mul,mul_pow,Complex.norm_real,Real.norm_eq_abs,
    abs_of_nonneg (V08I.logWeight_pos u).le]

noncomputable def principalSpectrum (j : Fin 16) : FullL2 :=
  (logSpectrum_mem (F j) (divided_square_weighted j)).toLp
    (fun u => (logWeight u : ℂ)*F j u)

theorem principalSpectrum_ae (j : Fin 16) :
    (principalSpectrum j : ℝ → ℂ) =ᵐ[volume] fun u => (logWeight u : ℂ)*F j u :=
  MemLp.coeFn_toLp (logSpectrum_mem (F j) (divided_square_weighted j))

end WeilDefect.MasterRecon.V10B74a

#print axioms WeilDefect.MasterRecon.V10B74a.divided_spectrum
#print axioms WeilDefect.MasterRecon.V10B74a.divided_spectrum_ae
#print axioms WeilDefect.MasterRecon.V10B74a.divided_square_weighted
#print axioms WeilDefect.MasterRecon.V10B74a.logSpectrum_mem
#print axioms WeilDefect.MasterRecon.V10B74a.principalSpectrum_ae
