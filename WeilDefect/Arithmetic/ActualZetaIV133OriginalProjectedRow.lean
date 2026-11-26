import WeilDefect.Arithmetic.ActualZetaIV132OriginalHeadResidualPayment
import Mathlib.Analysis.Fourier.LpSpace
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap FourierTransform ComplexConjugate

/-- Literal physical L2 Riesz row: inverse Fourier of the actual signed
spectral row, plus both original pole columns. -/
def neutralIV133PhysicalRow (a : ℝ) (u : 𝓢(ℝ,ℂ)) : RealComplexL2 :=
  (Lp.fourierTransformₗᵢ ℝ ℂ).symm (neutralIV109SpectralRowL2 a u) +
    sourceWindowMoment a (-(1/2)) (u.toLp 2 volume) •
      neutralMomentColumnL2 a (1/2) +
    sourceWindowMoment a (1/2) (u.toLp 2 volume) •
      neutralMomentColumnL2 a (-(1/2))

theorem neutralIV133Spectral_physical (a : ℝ) (u v : 𝓢(ℝ,ℂ)) :
    inner ℂ ((Lp.fourierTransformₗᵢ ℝ ℂ).symm
      (neutralIV109SpectralRowL2 a u)) (v.toLp 2 volume) =
    inner ℂ (neutralIV109SpectralRowL2 a u) (𝓕 (v.toLp 2 volume) : RealComplexL2) := by
  rw [← Lp.inner_fourier_eq]
  change inner ℂ ((Lp.fourierTransformₗᵢ ℝ ℂ)
    ((Lp.fourierTransformₗᵢ ℝ ℂ).symm (neutralIV109SpectralRowL2 a u)))
    (𝓕 (v.toLp 2 volume) : RealComplexL2) = _
  rw [LinearIsometryEquiv.apply_symm_apply]

theorem neutralIV133PhysicalRow_pair (a : ℝ) (ha : 0 ≤ a) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    inner ℂ (neutralIV133PhysicalRow a u) (v.toLp 2 volume) =
      neutralIV101Mixed a u v := by
  rw [neutralIV103Mixed_native a ha u v hu hv,
    neutralActualZetaLogWeilFormOperator_mixed, neutralLogPoleOperator_mixed,
    neutralIV102Lift_physical, neutralIV102Lift_physical,
    ← neutralIV109SpectralRow_pair]
  unfold neutralIV133PhysicalRow
  rw [inner_add_left, inner_add_left, inner_smul_left, inner_smul_left,
    neutralIV133Spectral_physical, neutralMomentColumnL2_inner,
    neutralMomentColumnL2_inner]
  ring

def neutralIV133CorrectedRow (k : ℕ) (hk : 0 < k) (u : 𝓢(ℝ,ℂ)) : RealComplexL2 :=
  neutralIV133PhysicalRow (11/10:ℝ) (u-neutralIV130ResponseVector k hk u)

theorem neutralIV133CorrectedRow_pair (k : ℕ) (hk : 0 < k) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    inner ℂ (neutralIV133CorrectedRow k hk u) (v.toLp 2 volume) =
      neutralIV130Mixed k hk u v := by
  rw [neutralIV130Mixed_row k hk u v hv]
  unfold neutralIV133CorrectedRow
  apply neutralIV133PhysicalRow_pair _ (by norm_num) _ _ _ hv
  intro x hx
  change u x-neutralIV130ResponseVector k hk u x = 0
  rw [hu x hx, neutralIV130Response_supported k hk u x hx, sub_zero]

/-- Any actual constraint-annihilating physical row can be subtracted.
No exact projection or computed annihilator is presumed. -/
theorem neutralIV133Projected_bound (k : ℕ) (hk : 0 < k) (u z : 𝓢(ℝ,ℂ))
    (d : RealComplexL2)
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → u x = 0)
    (hz : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z x = 0)
    (hd : inner ℂ d (z.toLp 2 volume) = 0) :
    ‖neutralIV130Mixed k hk u z‖ ≤
      ‖neutralIV133CorrectedRow k hk u-d‖ * ‖z.toLp 2 volume‖ := by
  have h := norm_inner_le_norm (𝕜 := ℂ) (neutralIV133CorrectedRow k hk u-d)
    (z.toLp 2 volume)
  rw [inner_sub_left, neutralIV133CorrectedRow_pair k hk u z hu hz, hd, sub_zero] at h
  exact h

theorem neutralIV133Penalty_projected_le (k : ℕ) (hk : 0 < k)
    (Z : Submodule ℂ (𝓢(ℝ,ℂ))) (h : 𝓢(ℝ,ℂ)) (d : RealComplexL2)
    (hh : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → h x = 0)
    (hz : ∀ z : Z, ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z.val x = 0)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : Z, eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val)
    (hd : ∀ z : Z, inner ℂ d (z.val.toLp 2 volume) = 0) :
    neutralIV131Penalty k hk Z h ≤ ‖neutralIV133CorrectedRow k hk h-d‖^2/eta := by
  unfold neutralIV131Penalty
  apply csSup_le
  · exact ⟨neutralIV131Loss k hk h (0 : Z).val, ⟨0,rfl⟩⟩
  · rintro r ⟨z,rfl⟩
    have hr := neutralIV133Projected_bound k hk h z.val d hh (hz z) (hd z)
    have hb := (neg_le_abs (neutralIV130Mixed k hk h z.val).re).trans
      ((Complex.abs_re_le_norm _).trans hr)
    exact neutralIV131Scalar_payment eta _ _ _ _ he hb (hc z)

/-- Exact trial shift with the constraint-aware physical residual norm. -/
theorem neutralIV133Penalty_trial_projected_le (k : ℕ) (hk : 0 < k)
    (Z : Submodule ℂ (𝓢(ℝ,ℂ))) (h : 𝓢(ℝ,ℂ)) (y : Z) (d : RealComplexL2)
    (hh : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → h x = 0)
    (hz : ∀ z : Z, ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → z.val x = 0)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : Z, eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val)
    (hd : ∀ z : Z, inner ℂ d (z.val.toLp 2 volume) = 0) :
    neutralIV131Penalty k hk Z h ≤ neutralIV131Loss k hk h y.val +
      ‖neutralIV133CorrectedRow k hk (h+y.val)-d‖^2/eta := by
  have hs : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → (h+y.val) x = 0 := by
    intro x hx
    change h x+y.val x = 0
    rw [hh x hx,hz y x hx,add_zero]
  unfold neutralIV131Penalty
  apply csSup_le
  · exact ⟨neutralIV131Loss k hk h (0 : Z).val, ⟨0,rfl⟩⟩
  · rintro r ⟨z,rfl⟩
    let w : Z := z-y
    have hw : z.val = y.val+w.val := by
      change z.val = y.val+(z.val-y.val)
      abel
    change neutralIV131Loss k hk h z.val ≤ _
    rw [hw, neutralIV132Loss_shift k hk h y.val w.val hh (hz y) (hz w)]
    have hr := neutralIV133Projected_bound k hk (h+y.val) w.val d hs (hz w) (hd w)
    have hb := (neg_le_abs (neutralIV130Mixed k hk (h+y.val) w.val).re).trans
      ((Complex.abs_re_le_norm _).trans hr)
    have hp : neutralIV131Loss k hk (h+y.val) w.val ≤
        ‖neutralIV133CorrectedRow k hk (h+y.val)-d‖^2/eta :=
      neutralIV131Scalar_payment eta _ _ _ _ he hb (hc w)
    linarith only [hp]

#print axioms neutralIV133Spectral_physical
#print axioms neutralIV133PhysicalRow_pair
#print axioms neutralIV133CorrectedRow_pair
#print axioms neutralIV133Projected_bound
#print axioms neutralIV133Penalty_projected_le
#print axioms neutralIV133Penalty_trial_projected_le

end
end WeilDefect
