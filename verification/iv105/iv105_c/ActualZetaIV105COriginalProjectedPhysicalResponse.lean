import WeilDefect.Arithmetic.ActualZetaIV105BOriginalPhysicalAction
import WeilDefect.Arithmetic.ActualZetaIV104OriginalPackedMassProjection
import Mathlib.MeasureTheory.Function.LpSeminorm.Indicator

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate

/-- Restrict only the physical action, not the original arithmetic form. -/
def neutralIV105CWindow (a : ℝ) (f : RealComplexL2) : RealComplexL2 :=
  (MemLp.indicator measurableSet_Icc (Lp.memLp f)).toLp
    ((Set.Icc (-a) a).indicator (fun x : ℝ => f x))

theorem neutralIV105CWindow_ae (a : ℝ) (f : RealComplexL2) :
    (neutralIV105CWindow a f : ℝ → ℂ) =ᵐ[volume]
      (Set.Icc (-a) a).indicator (fun x : ℝ => f x) :=
  (MemLp.indicator measurableSet_Icc (Lp.memLp f)).coeFn_toLp

theorem neutralIV105CWindow_supported (a : ℝ) (f : RealComplexL2) :
    ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → neutralIV105CWindow a f x = 0 := by
  filter_upwards [neutralIV105CWindow_ae a f] with x hx hout
  rw [hx, Set.indicator_of_notMem hout]

/-- Removing exterior action is exact against any supported physical test. -/
theorem neutralIV105CWindow_pair (a : ℝ) (f g : RealComplexL2)
    (hg : ∀ᵐ x ∂volume, x ∉ Set.Icc (-a) a → g x = 0) :
    inner ℂ (neutralIV105CWindow a f) g = inner ℂ f g := by
  simp only [MeasureTheory.L2.inner_def]
  apply integral_congr_ae
  filter_upwards [neutralIV105CWindow_ae a f, hg] with x hx hxg
  by_cases h : x ∈ Set.Icc (-a) a
  · rw [hx, Set.indicator_of_mem h]
  · rw [hx, Set.indicator_of_notMem h, hxg h]
    simp

def neutralIV105CProject (k : ℕ) (hk : 0 < k) (f : RealComplexL2) :
    RealComplexL2 :=
  (neutralIV100Packed k hk (fun i =>
    inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume) f /
      (neutralIV104Mass k hk i : ℂ))).toLp 2 volume

theorem neutralIV105CProject_pair (k : ℕ) (hk : 0 < k)
    (f : RealComplexL2) (i : Fin k) :
    inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
      (neutralIV105CProject k hk f) =
    inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume) f := by
  unfold neutralIV105CProject
  rw [neutralIV104Packed_pair]
  have hm : 0 < neutralIV104Mass k hk i := neutralIV100Carrier_mass_pos k hk i
  exact div_mul_cancel₀ _ (Complex.ofReal_ne_zero.mpr hm.ne')

def neutralIV105CResidual (k : ℕ) (hk : 0 < k) (f : RealComplexL2) :
    RealComplexL2 :=
  f - neutralIV105CProject k hk f

theorem neutralIV105CResidual_pair (k : ℕ) (hk : 0 < k)
    (f : RealComplexL2) (v : 𝓢(ℝ,ℂ))
    (hv : neutralIV101MassComplement k hk v) :
    inner ℂ (neutralIV105CResidual k hk f) (v.toLp 2 volume) =
    inner ℂ f (v.toLp 2 volume) := by
  rw [neutralIV105CResidual, inner_sub_left]
  unfold neutralIV105CProject
  rw [hv, sub_zero]

/-- Exact residual physical response for each packed generator, without
charging the exterior or the physical packed component. -/
def neutralIV105CResponse (k : ℕ) (hk : 0 < k) (i : Fin k) : RealComplexL2 :=
  neutralIV105CResidual k hk
    (neutralIV105CWindow (11/10:ℝ)
      (neutralIV105BAction (11/10:ℝ) (neutralIV100Carrier k hk i)))

theorem neutralIV105CResponse_pair (k : ℕ) (hk : 0 < k)
    (i : Fin k) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (horth : neutralIV101MassComplement k hk v) :
    neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v =
      inner ℂ (neutralIV105CResponse k hk i) (v.toLp 2 volume) := by
  have hu := neutralIV009OriginalCollars_supported_window
    (neutralIV100Carrier k hk i) (neutralIV100Carrier_collars k hk i)
  have hvs : ∀ᵐ x ∂volume, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
      (v.toLp 2 volume) x = 0 := by
    filter_upwards [v.coeFn_toLp 2 volume] with x hx hout
    rw [hx]
    exact hv x hout
  rw [neutralIV105CResponse, neutralIV105CResidual_pair k hk _ v horth,
    neutralIV105CWindow_pair _ _ _ hvs]
  exact neutralIV105BAction_pair _ (by norm_num) _ _ hu hv

#print axioms neutralIV105CWindow_ae
#print axioms neutralIV105CWindow_supported
#print axioms neutralIV105CWindow_pair
#print axioms neutralIV105CProject_pair
#print axioms neutralIV105CResidual_pair
#print axioms neutralIV105CResponse_pair
end
end WeilDefect
