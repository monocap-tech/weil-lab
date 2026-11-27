import WeilDefect.MasterRecon.V10B15b
import WeilDefect.MasterRecon.V10B13b

/-! The low-band polynomial and discarded high-band Fourier parts
are orthogonal in physical L². On the retained moment kernel the
low-band mass alone is factorially small. -/
namespace WeilDefect.MasterRecon.V10B16c

open MeasureTheory Set Filter
open scoped FourierTransform InnerProduct
open V08I (FullL2 logCarrier physicalInclusion)
open V10B13a (approximation bandPolynomial out input remainderBound)

theorem approximation_fourier_support (t R : ℝ) (ht : 0 ≤ t)
    (hR : 0 ≤ R) (n : ℕ) (g : logCarrier t) :
    ∀ᵐ u ∂volume, u ∉ Icc (-R) R →
      (𝓕 (approximation t R ht hR n g) : FullL2) u = 0 := by
  let U := Lp.fourierTransformₗᵢ ℝ ℂ
  let f := (bandPolynomial t R ht n g).comp (V08K.scaleBand R)
  have he : U (approximation t R ht hR n g) =
      V08G.zeroBandValue volume R hR isCompact_Icc.measure_lt_top.ne f := by
    change U (U.symm _) = _
    rw [U.apply_symm_apply]
    rfl
  rw [show (𝓕 (approximation t R ht hR n g) : FullL2) = U (approximation t R ht hR n g) from rfl,he]
  filter_upwards [V08G.zeroBandValue_ae volume R hR isCompact_Icc.measure_lt_top.ne f] with u hu
  intro h
  rw [hu,V08G.zeroBand,Set.indicator_of_notMem h]

theorem cutoff_orthogonal (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R)
    (n : ℕ) (g : logCarrier t) :
    inner ℂ (physicalInclusion t g-V08K.physicalCutoff t R ht hR g)
      (V08K.physicalCutoff t R ht hR g-approximation t R ht hR n g) = 0 := by
  let U := Lp.fourierTransformₗᵢ ℝ ℂ
  rw [← U.inner_map_map,map_sub,map_sub]
  have he : U (V08K.physicalCutoff t R ht hR g) = V08K.spectralCutoff t R ht hR g :=
    U.apply_symm_apply _
  rw [he,L2.inner_def]
  apply integral_eq_zero_of_ae
  filter_upwards [Lp.coeFn_sub (U (physicalInclusion t g)) (V08K.spectralCutoff t R ht hR g),
    Lp.coeFn_sub (V08K.spectralCutoff t R ht hR g) (U (approximation t R ht hR n g)),
    V08K.spectralCutoff_ae t R ht hR g,
    approximation_fourier_support t R ht hR n g] with u h1 h2 h3 h4
  change inner ℂ (((U (physicalInclusion t g)-V08K.spectralCutoff t R ht hR g : FullL2) : ℝ → ℂ) u)
    (((V08K.spectralCutoff t R ht hR g-U (approximation t R ht hR n g) : FullL2) : ℝ → ℂ) u) = 0
  rw [h1,h2]
  change inner ℂ (U (physicalInclusion t g) u-V08K.spectralCutoff t R ht hR g u)
    (V08K.spectralCutoff t R ht hR g u-U (approximation t R ht hR n g) u) = 0
  rw [h3]
  by_cases hu : u ∈ Icc (-R) R
  · rw [Set.indicator_of_mem hu,sub_self,inner_zero_left]
  · rw [Set.indicator_of_notMem hu,h4 hu,sub_self,inner_zero_right]

theorem low_band_bound (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R) (n : ℕ)
    (hn : (2*Real.pi*R)*t/((n:ℝ)+1) ≤ 1/2)
    (g : logCarrier t) (hg : g ∈ (V10B13b.retained t ht n)ᗮ) :
    ‖V08K.physicalCutoff t R ht hR g‖ ≤
      ‖out R hR‖*remainderBound t R n*‖input t‖*‖g‖ := by
  have hz := V10B13a.approximation_zero t R ht hR n g
    (fun j hj => V10B13b.retained_moment_zero t ht n g hg j hj)
  let v := V08E.boundedFourier (V08K.supportMeasure t) t (2*Real.pi*R) ht
    (V08K.supportMeasure_bound t) (input t g)-bandPolynomial t R ht n g
  have he : V08K.physicalCutoff t R ht hR g = out R hR v := by
    rw [map_sub]
    change _ = V08K.physicalCutoff t R ht hR g-approximation t R ht hR n g
    rw [hz,sub_zero]
  rw [he]
  have hb := V10B13a.band_error t R ht hR n hn g
  change ‖v‖ ≤ remainderBound t R n * ‖input t g‖ at hb
  calc
    _ ≤ ‖out R hR‖*‖v‖ := (out R hR).le_opNorm v
    _ ≤ ‖out R hR‖*(remainderBound t R n*‖input t g‖) :=
      mul_le_mul_of_nonneg_left hb (norm_nonneg (out R hR))
    _ ≤ _ := by
      have h := mul_le_mul_of_nonneg_left ((input t).le_opNorm g)
        (show 0 ≤ ‖out R hR‖*remainderBound t R n by unfold remainderBound; positivity)
      nlinarith only [h]

theorem low_band_mass (t R : ℝ) (ht : 0 ≤ t) (hR : 0 ≤ R)
    (g : logCarrier t) :
    ‖V08K.physicalCutoff t R ht hR g‖^2 =
      ∫ u in Icc (-R) R, ‖(𝓕 (physicalInclusion t g) : FullL2) u‖^2 := by
  let U := Lp.fourierTransformₗᵢ ℝ ℂ
  have he : U (V08K.physicalCutoff t R ht hR g) = V08K.spectralCutoff t R ht hR g :=
    U.apply_symm_apply _
  rw [← U.norm_map (V08K.physicalCutoff t R ht hR g),he,V08G.l2_norm_sq_integral,
    ← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [V08K.spectralCutoff_ae t R ht hR g] with u hu
  rw [hu]
  by_cases h : u ∈ Icc (-R) R
  · simp [Set.indicator_of_mem h]
  · simp [Set.indicator_of_notMem h]

end WeilDefect.MasterRecon.V10B16c

#print axioms WeilDefect.MasterRecon.V10B16c.approximation_fourier_support
#print axioms WeilDefect.MasterRecon.V10B16c.cutoff_orthogonal
#print axioms WeilDefect.MasterRecon.V10B16c.low_band_bound
#print axioms WeilDefect.MasterRecon.V10B16c.low_band_mass
