import WeilDefect.Arithmetic.ActualZetaOriginalEndpointSeedGeometry
import Mathlib.Analysis.Calculus.BumpFunction.Normed
import Mathlib.Analysis.Calculus.ContDiff.Convolution
import Mathlib.MeasureTheory.Measure.Haar.NormedSpace

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped Convolution ContDiff

/-!
NF579: the literal original compression is followed by an actual
positive unit-mass smooth bump; no abstract mollifier existence
premise. Its full complex strip transform bound is proved directly.
The source itself remains a real integrable half-carrier argument.
-/

def neutralNF579Bump (s : ℝ) (hs : s < 1) : ContDiffBump (0 : ℝ) where
  rIn := neutralNF578Epsilon s / 2
  rOut := neutralNF578Epsilon s
  rIn_pos := by unfold neutralNF578Epsilon; linarith
  rIn_lt_rOut := by unfold neutralNF578Epsilon; linarith

def neutralNF579Mollifier (s : ℝ) (hs : s < 1) : ℝ → ℝ :=
  (neutralNF579Bump s hs).normed volume

theorem neutralNF579Mollifier_nonneg (s : ℝ) (hs : s < 1) (x : ℝ) :
    0 ≤ neutralNF579Mollifier s hs x :=
  (neutralNF579Bump s hs).nonneg_normed x

theorem neutralNF579Mollifier_integrable (s : ℝ) (hs : s < 1) :
    Integrable (neutralNF579Mollifier s hs) volume :=
  (neutralNF579Bump s hs).integrable_normed

theorem neutralNF579Mollifier_mass (s : ℝ) (hs : s < 1) :
    ∫ x, neutralNF579Mollifier s hs x ∂volume = 1 :=
  (neutralNF579Bump s hs).integral_normed

theorem neutralNF579Mollifier_even (s : ℝ) (hs : s < 1) (x : ℝ) :
    neutralNF579Mollifier s hs (-x) = neutralNF579Mollifier s hs x :=
  (neutralNF579Bump s hs).normed_neg x

theorem neutralNF579Mollifier_smooth (s : ℝ) (hs : s < 1) :
    ContDiff ℝ ∞ (neutralNF579Mollifier s hs) :=
  (neutralNF579Bump s hs).contDiff_normed

theorem neutralNF579Mollifier_compact (s : ℝ) (hs : s < 1) :
    HasCompactSupport (neutralNF579Mollifier s hs) :=
  (neutralNF579Bump s hs).hasCompactSupport_normed

theorem neutralNF579Mollifier_supported (s : ℝ) (hs : s < 1) (x : ℝ)
    (hx : neutralNF578Epsilon s < |x|) :
    neutralNF579Mollifier s hs x = 0 := by
  by_contra hn
  have hm : x ∈ Function.support (neutralNF579Mollifier s hs) := hn
  unfold neutralNF579Mollifier at hm
  rw [(neutralNF579Bump s hs).support_normed_eq] at hm
  have hball : dist x (0 : ℝ) < neutralNF578Epsilon s := hm
  rw [Real.dist_eq, sub_zero] at hball
  linarith

/-- Lebesgue integrability survives the same affine contraction,
by two measure-preserving reflections and one nonzero dilation. -/
theorem neutralNF579CompressedHalf_integrable (h : ℝ → ℝ)
    (hh : Integrable h volume) (s : ℝ) (hs : 0 < s) :
    Integrable (neutralNF578CompressedHalf h s) volume := by
  let c := neutralNF578Center
  let f : ℝ → ℝ := fun x => h (c-x)
  have hf : Integrable f volume :=
    (integrable_comp_sub_left h c).mpr hh
  have hd : Integrable (fun x => f (x/s)) volume := hf.comp_div hs.ne'
  have hr : Integrable (fun x => f ((c-x)/s)) volume :=
    (integrable_comp_sub_left (fun x => f (x/s)) c).mpr hd
  have he : neutralNF578CompressedHalf h s = fun x => f ((c-x)/s) := by
    funext x
    unfold neutralNF578CompressedHalf
    dsimp [f,c]
    congr 1
    ring
  rw [he]
  exact hr

def neutralNF579Seed (h : ℝ → ℝ) (s : ℝ) (hs : s < 1) : ℝ → ℝ :=
  neutralNF578OddSeed h (neutralNF579Mollifier s hs) s

theorem neutralNF579ConvolvedHalf_smooth (h : ℝ → ℝ)
    (hh : Integrable h volume) (s : ℝ) (hs : 0 < s) (hs' : s < 1) :
    ContDiff ℝ ∞ (neutralNF578ConvolvedHalf h (neutralNF579Mollifier s hs') s) := by
  change ContDiff ℝ ∞
    ((neutralNF579Mollifier s hs') ⋆[ContinuousLinearMap.mul ℝ ℝ, volume]
      (neutralNF578CompressedHalf h s))
  exact (neutralNF579Mollifier_compact s hs').contDiff_convolution_left
    (ContinuousLinearMap.mul ℝ ℝ) (neutralNF579Mollifier_smooth s hs')
    (neutralNF579CompressedHalf_integrable h hh s hs).locallyIntegrable

theorem neutralNF579Seed_smooth (h : ℝ → ℝ) (hh : Integrable h volume)
    (s : ℝ) (hs : 0 < s) (hs' : s < 1) :
    ContDiff ℝ ∞ (neutralNF579Seed h s hs') := by
  have hv := neutralNF579ConvolvedHalf_smooth h hh s hs hs'
  exact hv.sub (hv.comp contDiff_id.neg)

theorem neutralNF579Seed_odd (h : ℝ → ℝ) (s : ℝ) (hs : s < 1) (x : ℝ) :
    neutralNF579Seed h s hs (-x) = -neutralNF579Seed h s hs x :=
  neutralNF578OddSeed_odd h (neutralNF579Mollifier s hs) s x

theorem neutralNF579Seed_supported (h : ℝ → ℝ) (s : ℝ) (hs : 0 < s)
    (hs' : s < 1) (hh : ∀ u, u ∉ neutralNF578PositiveCollar → h u = 0)
    (x : ℝ) (hx : x ∉ neutralNF578PositiveCollar)
    (hnx : -x ∉ neutralNF578PositiveCollar) :
    neutralNF579Seed h s hs' x = 0 :=
  neutralNF578OddSeed_supported h (neutralNF579Mollifier s hs') s x hs hs'
    hh (neutralNF579Mollifier_supported s hs') hx hnx

/-- Positive-exponent entire sample convention, the same one whose
real-axis value at -2 pi ξ is the native Fourier transform. -/
def neutralNF579RawTransform (h : ℝ → ℝ) (z : ℂ) : ℂ :=
  ∫ x : ℝ, (h x : ℂ) * Complex.exp (Complex.I * (z * (x : ℂ)))

theorem neutralNF579Mollifier_strip (s : ℝ) (hs : s < 1) (z : ℂ)
    (hz : |z.im| ≤ 1/2) :
    ‖neutralNF579RawTransform (neutralNF579Mollifier s hs) z‖ ≤
      Real.exp (neutralNF578Epsilon s/2) := by
  let ρ := neutralNF579Mollifier s hs
  let C := Real.exp (neutralNF578Epsilon s/2)
  let f : ℝ → ℂ := fun x => (ρ x : ℂ) *
    Complex.exp (Complex.I * (z * (x : ℂ)))
  have hρ : Continuous ρ := (neutralNF579Mollifier_smooth s hs).continuous
  have hf : Continuous f := by
    dsimp [f]
    fun_prop
  have hb : ∀ x, ‖f x‖ ≤ C * ρ x := by
    intro x
    by_cases hx : |x| ≤ neutralNF578Epsilon s
    · have hnon : 0 ≤ ρ x := neutralNF579Mollifier_nonneg s hs x
      have he : -(z.im*x) ≤ neutralNF578Epsilon s/2 := by
        calc
          _ ≤ |z.im*x| := neg_le_abs _
          _ = |z.im|*|x| := abs_mul _ _
          _ ≤ (1/2)*neutralNF578Epsilon s :=
            mul_le_mul hz hx (abs_nonneg _) (by norm_num)
          _ = _ := by ring
      have hexp : Real.exp (-(z.im*x)) ≤ C := Real.exp_le_exp.mpr he
      change ‖(ρ x : ℂ) * Complex.exp (Complex.I * (z * (x : ℂ)))‖ ≤ C*ρ x
      rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hnon,
        Complex.norm_exp]
      have hr : (Complex.I * (z * (x : ℂ))).re = -(z.im*x) := by
        simp [Complex.mul_re, Complex.mul_im]
      rw [hr, mul_comm C]
      exact mul_le_mul_of_nonneg_left hexp hnon
    · have hzero : ρ x = 0 :=
        neutralNF579Mollifier_supported s hs x (lt_of_not_ge hx)
      simp [f, hzero]
  have hi : Integrable (fun x => C*ρ x) volume :=
    (neutralNF579Mollifier_integrable s hs).const_mul C
  have hfn : Integrable (fun x => ‖f x‖) volume :=
    hi.mono' hf.aestronglyMeasurable.norm
      (Filter.Eventually.of_forall fun x => by
        rw [Real.norm_eq_abs, abs_of_nonneg (norm_nonneg _)]
        exact hb x)
  change ‖∫ x, f x ∂volume‖ ≤ C
  calc
    _ ≤ ∫ x, ‖f x‖ ∂volume := norm_integral_le_integral_norm _
    _ ≤ ∫ x, C*ρ x ∂volume := integral_mono hfn hi hb
    _ = C := by rw [integral_const_mul, neutralNF579Mollifier_mass s hs, mul_one]

end
end WeilDefect
