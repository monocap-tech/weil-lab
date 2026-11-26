import WeilDefect.Arithmetic.ActualZetaIV106C1OriginalResponseNull
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate

/-- Upgrade a physical mass margin using the existing shifted form estimate. -/
theorem neutralIV106C2Scalar (L m q D : ℝ)
    (hD : 0 ≤ D) (hm : m ≤ q) (hL : L ≤ q + D*m) :
    L / (1+D) ≤ q := by
  apply (div_le_iff₀ (by linarith : 0 < 1+D)).2
  have h := mul_le_mul_of_nonneg_left hm hD
  nlinarith only [h, hL]

def neutralIV106C2Loss (a : ℝ) : ℝ :=
  neutralActualZetaNativeLogError a + neutralPhysicalPoleEnergyConstant a

theorem neutralIV106C2Loss_nonneg (a : ℝ) :
    0 ≤ neutralIV106C2Loss a :=
  add_nonneg (neutralActualZetaNativeLogError_spec a).1
    (neutralPhysicalPoleEnergyConstant_nonnegative a)

theorem neutralIV106C2Native_form_margin (a : ℝ)
    (f : NeutralLogHilbertCarrier a)
    (hm : ‖neutralLogPhysical f.val‖^2 ≤
      (inner ℂ f (neutralActualZetaLogWeilFormOperator a f)).re) :
    ‖f‖^2 / (1+neutralIV106C2Loss a) ≤
      (inner ℂ f (neutralActualZetaLogWeilFormOperator a f)).re := by
  exact neutralIV106C2Scalar _ _ _ _
    (neutralIV106C2Loss_nonneg a) hm
    (neutralActualZetaLogWeilFormOperator_garding a f)

theorem neutralIV106C2Original_form_margin (a : ℝ) (ha : 0 ≤ a)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0)
    (hm : ‖v.toLp 2 volume‖^2 ≤ neutralIV101Q a v) :
    ‖neutralIV102Lift a v hv‖^2 / (1+neutralIV106C2Loss a) ≤
      neutralIV101Q a v := by
  exact neutralIV106C2Scalar _ _ _ _
    (neutralIV106C2Loss_nonneg a) hm
    (neutralIV102Original_garding_of_attachment a v hv
      (neutralIV103Mixed_native a ha v v hv hv))

/-- Conditional tail receiver; the unit mass margin still needs attachment. -/
theorem neutralIV106C2Schur_form_margin (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (ho : neutralIV101MassComplement k hk v)
    (hn : ∀ i : Fin k, inner ℂ (neutralIV105CResponse k hk i)
      (v.toLp 2 volume) = 0)
    (hm : ‖v.toLp 2 volume‖^2 ≤ neutralIV101Q (11/10:ℝ) v) :
    ‖neutralIV102Lift (11/10:ℝ) v hv‖^2 /
        (1+neutralIV106C2Loss (11/10:ℝ)) ≤
      neutralIV101Q (11/10:ℝ) v -
        neutralIV101Q (11/10:ℝ)
          (neutralIV100Packed k hk (neutralIV105E2Solve k hk v)) := by
  rw [neutralIV106C1Penalty_zero k hk v hv ho hn, sub_zero]
  exact neutralIV106C2Original_form_margin _ (by norm_num) v hv hm

#print axioms neutralIV106C2Scalar
#print axioms neutralIV106C2Loss_nonneg
#print axioms neutralIV106C2Native_form_margin
#print axioms neutralIV106C2Original_form_margin
#print axioms neutralIV106C2Schur_form_margin
end
end WeilDefect
