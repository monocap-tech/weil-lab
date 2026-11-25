import WeilDefect.Arithmetic.ActualZetaIV101OriginalPackedComplementReceiver
import WeilDefect.Arithmetic.ActualZetaLogCarrierSchwartzCompact
import WeilDefect.Arithmetic.ActualZetaNativeFormOperator
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory InnerProductSpace FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate

/-- The same physical Schwartz vector enters the canonical form domain,
without any Green-range or positivity hypothesis. -/
def neutralIV102Canonical (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    neutralCanonicalLogFormDomain a := by
  refine ⟨s.toLp 2 volume, ?_, ?_⟩
  · filter_upwards [s.coeFn_toLp 2 volume] with x hx hout
    rw [hx]
    exact hs x hout
  · exact neutralFiniteLogFourierEnergy_of_quadraticMoment _
      (neutralSchwartzPhysical_quadraticFourierMoment s)

def neutralIV102Lift (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    NeutralLogHilbertCarrier a :=
  neutralCanonicalToLogHilbert (neutralIV102Canonical a s hs)

theorem neutralIV102Lift_physical (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    neutralLogPhysical (neutralIV102Lift a s hs).val = s.toLp 2 volume := by
  exact neutralLogPhysical_weighted (neutralIV102Canonical a s hs)

theorem neutralIV102Lift_log_norm (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    ‖neutralIV102Lift a s hs‖^2 = ∫ ξ : ℝ,
      logarithmicFourierWeight ξ * ‖(𝓕 (s.toLp 2 volume) : RealComplexL2) ξ‖^2 := by
  rw [neutralLogHilbertCarrier_norm_sq, neutralIV102Lift_physical]

theorem neutralIV102Lift_mass_le_log (a : ℝ) (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) :
    ‖s.toLp 2 volume‖^2 ≤ ‖neutralIV102Lift a s hs‖^2 := by
  exact neutralActualZetaCanonical_mass_le_log a (neutralIV102Canonical a s hs)

/-- Pull back the PHYSICAL metric to the logarithmic carrier.
This is not the carrier's native weighted inner product. -/
def neutralIV102PhysicalPair (a : ℝ) (p q : NeutralLogHilbertCarrier a) : ℂ :=
  inner ℂ (neutralLogPhysical p.val) (neutralLogPhysical q.val)

theorem neutralIV102PhysicalPair_lift (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    neutralIV102PhysicalPair a (neutralIV102Lift a u hu) (neutralIV102Lift a v hv) =
      inner ℂ (u.toLp 2 volume) (v.toLp 2 volume) := by
  unfold neutralIV102PhysicalPair
  rw [neutralIV102Lift_physical, neutralIV102Lift_physical]

def neutralIV102PackedLift (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) :
    NeutralLogHilbertCarrier (11/10:ℝ) :=
  neutralIV102Lift _ (neutralIV100Packed k hk c)
    (neutralIV009OriginalCollars_supported_window _
      (neutralIV101Packed_collars k hk c))

theorem neutralIV102MassComplement_iff (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV101MassComplement k hk v ↔
      ∀ c : Fin k → ℂ, neutralIV102PhysicalPair (11/10:ℝ)
        (neutralIV102PackedLift k hk c) (neutralIV102Lift _ v hv) = 0 := by
  unfold neutralIV101MassComplement neutralIV102PackedLift
  simp only [neutralIV102PhysicalPair_lift]

/-- On an actual Green-representable pair, the native operator is
literally the original mixed signed form. No Green surjectivity assumed. -/
theorem neutralIV102Mixed_native_of_Green (a : ℝ) (ha : 0 < a)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0)
    (p q : NeutralActualZetaGreenCoefficients)
    (hp : u.toLp 2 volume = neutralActualZetaGreenSynthesis a p)
    (hq : v.toLp 2 volume = neutralActualZetaGreenSynthesis a q) :
    neutralIV101Mixed a u v = inner ℂ (neutralIV102Lift a u hu)
      (neutralActualZetaLogWeilFormOperator a (neutralIV102Lift a v hv)) := by
  have huc : neutralIV102Canonical a u hu = neutralActualZetaGreenCanonical a ha p := by
    apply Subtype.ext
    exact hp
  have hvc : neutralIV102Canonical a v hv = neutralActualZetaGreenCanonical a ha q := by
    apply Subtype.ext
    exact hq
  have hef := neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond
    a (u.toLp 2 volume) (v.toLp 2 volume) (fun x : ℝ => v x)
    (v.smooth 2) (neutralIV008SchwartzWindow_hasCompactSupport a v hv)
    (neutralIV006Schwartz_window_ae a v hv)
  unfold neutralIV101Mixed neutralIV102Lift
  rw [huc, hvc, ← neutralActualZetaGreenZeroForm_native_operator a ha p q, ← hef,
    hp, hq]
  exact neutralActualZetaGreenCorrelation_zeroForm a p q

/-- Actual Garding transfer, conditional ONLY on the literal diagonal
attachment for this vector. This does not assert that attachment. -/
theorem neutralIV102Original_garding_of_attachment (a : ℝ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0)
    (hattach : neutralIV101Mixed a v v = inner ℂ (neutralIV102Lift a v hv)
      (neutralActualZetaLogWeilFormOperator a (neutralIV102Lift a v hv))) :
    ‖neutralIV102Lift a v hv‖^2 ≤ neutralIV101Q a v +
      (neutralActualZetaNativeLogError a + neutralPhysicalPoleEnergyConstant a) *
      ‖v.toLp 2 volume‖^2 := by
  have h := neutralActualZetaLogWeilFormOperator_garding a (neutralIV102Lift a v hv)
  rw [← hattach, neutralIV102Lift_physical] at h
  exact h

#print axioms neutralIV102Lift_physical
#print axioms neutralIV102Lift_log_norm
#print axioms neutralIV102Lift_mass_le_log
#print axioms neutralIV102PhysicalPair_lift
#print axioms neutralIV102MassComplement_iff
#print axioms neutralIV102Mixed_native_of_Green
#print axioms neutralIV102Original_garding_of_attachment

end
end WeilDefect
