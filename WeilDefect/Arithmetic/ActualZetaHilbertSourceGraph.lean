import WeilDefect.Arithmetic.ActualZetaSelectedBackground
import Mathlib.Analysis.InnerProductSpace.ProdL2
import Mathlib.Analysis.InnerProductSpace.l2Space

namespace WeilDefect
noncomputable section
open InnerProductSpace ContinuousLinearMap
open scoped ComplexConjugate InnerProduct ENNReal
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false

/-- Hilbert product of the two full actual-divisor coefficient spaces. -/
abbrev NeutralActualZetaHilbertCoefficients :=
  WithLp 2 (NeutralActualZetaGreenCoefficients × NeutralActualZetaGreenCoefficients)

/-- The same three source coordinates equipped with the ℓ² product norm. -/
abbrev NeutralActualZetaHilbertAmbient (a : ℝ) :=
  WithLp 2 (NeutralLogHilbertCarrier a × NeutralActualZetaHilbertCoefficients)

/-- Continuous linear coordinate identification, preserving the physical
coordinate and both complete source vectors. It is not claimed isometric
for the old maximum product norm. -/
def neutralActualZetaHilbertCoordinates (a : ℝ) :
    NeutralActualZetaHilbertAmbient a ≃L[ℂ] NeutralActualZetaSourceAmbient a :=
  (WithLp.prodContinuousLinearEquiv 2 ℂ (NeutralLogHilbertCarrier a)
    NeutralActualZetaHilbertCoefficients).trans
    ((ContinuousLinearEquiv.refl ℂ (NeutralLogHilbertCarrier a)).prodCongr
      (WithLp.prodContinuousLinearEquiv 2 ℂ
        NeutralActualZetaGreenCoefficients NeutralActualZetaGreenCoefficients))

/-- The actual source graph in its Hilbert norm is closed by pullback of
the certified source graph under the concrete coordinate equivalence. -/
def neutralActualZetaHilbertSourceGraph (a : ℝ) :
    ClosedSubmodule ℂ (NeutralActualZetaHilbertAmbient a) :=
  (neutralActualZetaSourceGraph a).comap
    (neutralActualZetaHilbertCoordinates a).toContinuousLinearMap

abbrev NeutralActualZetaHilbertSourceDomain (a : ℝ) :=
  (neutralActualZetaHilbertSourceGraph a).toSubmodule

instance neutralActualZetaHilbertSourceDomain_innerProduct (a : ℝ) :
    InnerProductSpace ℂ (NeutralActualZetaHilbertSourceDomain a) :=
  Submodule.innerProductSpace (neutralActualZetaHilbertSourceGraph a).toSubmodule

instance neutralActualZetaHilbertSourceDomain_complete (a : ℝ) :
    CompleteSpace (NeutralActualZetaHilbertSourceDomain a) :=
  (neutralActualZetaHilbertSourceGraph a).isClosed.completeSpace_coe

/-- Forward coordinate map restricted to the unchanged source equations. -/
def neutralActualZetaHilbertToSource (a : ℝ) :
    NeutralActualZetaHilbertSourceDomain a →L[ℂ] NeutralActualZetaSourceDomain a :=
  ((neutralActualZetaHilbertCoordinates a).toContinuousLinearMap.comp
    (neutralActualZetaHilbertSourceGraph a).toSubmodule.subtypeL).codRestrict
      (neutralActualZetaSourceGraph a).toSubmodule (fun f => f.property)

/-- Inverse coordinate map, retaining exactly the same graph membership. -/
def neutralActualZetaSourceToHilbert (a : ℝ) :
    NeutralActualZetaSourceDomain a →L[ℂ] NeutralActualZetaHilbertSourceDomain a :=
  ((neutralActualZetaHilbertCoordinates a).symm.toContinuousLinearMap.comp
    (neutralActualZetaSourceGraph a).toSubmodule.subtypeL).codRestrict
      (neutralActualZetaHilbertSourceGraph a).toSubmodule (fun f => by
        change neutralActualZetaHilbertCoordinates a
          ((neutralActualZetaHilbertCoordinates a).symm f.val) ∈ neutralActualZetaSourceGraph a
        rw [ContinuousLinearEquiv.apply_symm_apply]
        exact f.property)

theorem neutralActualZetaHilbertToSource_sourceToHilbert (a : ℝ)
    (f : NeutralActualZetaSourceDomain a) :
    neutralActualZetaHilbertToSource a (neutralActualZetaSourceToHilbert a f) = f := by
  apply Subtype.ext
  exact (neutralActualZetaHilbertCoordinates a).apply_symm_apply f.val

theorem neutralActualZetaSourceToHilbert_hilbertToSource (a : ℝ)
    (f : NeutralActualZetaHilbertSourceDomain a) :
    neutralActualZetaSourceToHilbert a (neutralActualZetaHilbertToSource a f) = f := by
  apply Subtype.ext
  exact (neutralActualZetaHilbertCoordinates a).symm_apply_apply f.val

/-- Exact Hilbert graph norm: physical logarithmic norm squared plus the
two unnormalized full source coefficient norms squared. -/
theorem neutralActualZetaHilbertSourceDomain_norm_sq (a : ℝ)
    (f : NeutralActualZetaHilbertSourceDomain a) :
    ‖f‖ ^ 2 =
      ‖neutralActualZetaSourcePhysical a (neutralActualZetaHilbertToSource a f)‖ ^ 2 +
      ‖neutralActualZetaPositiveAnalysis a (neutralActualZetaHilbertToSource a f)‖ ^ 2 +
      ‖neutralActualZetaNegativeAnalysis a (neutralActualZetaHilbertToSource a f)‖ ^ 2 := by
  change ‖f.val‖ ^ 2 = ‖f.val.fst‖ ^ 2 + ‖f.val.snd.fst‖ ^ 2 + ‖f.val.snd.snd‖ ^ 2
  rw [WithLp.prod_norm_sq_eq_of_L2, WithLp.prod_norm_sq_eq_of_L2]
  ring

def neutralActualZetaHilbertPositiveAnalysis (a : ℝ) :
    NeutralActualZetaHilbertSourceDomain a →L[ℂ] NeutralActualZetaGreenCoefficients :=
  (neutralActualZetaNormalizedPositiveAnalysis a).comp (neutralActualZetaHilbertToSource a)

def neutralActualZetaHilbertNegativeAnalysis (a : ℝ) :
    NeutralActualZetaHilbertSourceDomain a →L[ℂ] NeutralActualZetaGreenCoefficients :=
  (neutralActualZetaNormalizedNegativeAnalysis a).comp (neutralActualZetaHilbertToSource a)

def neutralActualZetaHilbertBackgroundAnalysis (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    NeutralActualZetaHilbertSourceDomain a →L[ℂ] NeutralActualZetaGreenCoefficients :=
  (neutralActualZetaBackgroundNegativeAnalysis a s).comp (neutralActualZetaHilbertToSource a)

/-- Actual bounded signed source covariance on the Hilbert graph.
This is a graph-domain operator, not an asserted physical Weil operator. -/
def neutralActualZetaHilbertSourceOperator (a : ℝ) :
    NeutralActualZetaHilbertSourceDomain a →L[ℂ] NeutralActualZetaHilbertSourceDomain a :=
  (neutralActualZetaHilbertPositiveAnalysis a)† ∘L neutralActualZetaHilbertPositiveAnalysis a -
    (neutralActualZetaHilbertNegativeAnalysis a)† ∘L neutralActualZetaHilbertNegativeAnalysis a

/-- The corresponding signed effective-background covariance. Positivity and
a WD-T10-compatible factorization remain separate obligations. -/
def neutralActualZetaHilbertBackgroundOperator (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate) :
    NeutralActualZetaHilbertSourceDomain a →L[ℂ] NeutralActualZetaHilbertSourceDomain a :=
  (neutralActualZetaHilbertPositiveAnalysis a)† ∘L neutralActualZetaHilbertPositiveAnalysis a -
    (neutralActualZetaHilbertBackgroundAnalysis a s)† ∘L
      neutralActualZetaHilbertBackgroundAnalysis a s

theorem neutralActualZetaHilbertSourceOperator_mixed (a : ℝ)
    (f g : NeutralActualZetaHilbertSourceDomain a) :
    inner ℂ f (neutralActualZetaHilbertSourceOperator a g) =
      inner ℂ (neutralActualZetaHilbertPositiveAnalysis a f)
        (neutralActualZetaHilbertPositiveAnalysis a g) -
      inner ℂ (neutralActualZetaHilbertNegativeAnalysis a f)
        (neutralActualZetaHilbertNegativeAnalysis a g) := by
  simp only [neutralActualZetaHilbertSourceOperator, sub_apply, comp_apply,
    inner_sub_right, adjoint_inner_right]

theorem neutralActualZetaHilbertBackgroundOperator_mixed (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (f g : NeutralActualZetaHilbertSourceDomain a) :
    inner ℂ f (neutralActualZetaHilbertBackgroundOperator a s g) =
      inner ℂ (neutralActualZetaHilbertPositiveAnalysis a f)
        (neutralActualZetaHilbertPositiveAnalysis a g) -
      inner ℂ (neutralActualZetaHilbertBackgroundAnalysis a s f)
        (neutralActualZetaHilbertBackgroundAnalysis a s g) := by
  simp only [neutralActualZetaHilbertBackgroundOperator, sub_apply, comp_apply,
    inner_sub_right, adjoint_inner_right]

theorem neutralActualZetaHilbertSourceOperator_diagonal (a : ℝ)
    (f : NeutralActualZetaHilbertSourceDomain a) :
    inner ℂ f (neutralActualZetaHilbertSourceOperator a f) =
      (neutralActualZetaSourceQuadratic a (neutralActualZetaHilbertToSource a f) : ℂ) := by
  rw [neutralActualZetaHilbertSourceOperator_mixed]
  simp only [inner_self_eq_norm_sq_to_K, neutralActualZetaSourceQuadratic,
    neutralActualZetaHilbertPositiveAnalysis, neutralActualZetaHilbertNegativeAnalysis,
    comp_apply, Complex.ofReal_sub]

theorem neutralActualZetaHilbertBackgroundOperator_diagonal (a : ℝ)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (f : NeutralActualZetaHilbertSourceDomain a) :
    inner ℂ f (neutralActualZetaHilbertBackgroundOperator a s f) =
      (neutralActualZetaEffectiveBackgroundQuadratic a s
        (neutralActualZetaHilbertToSource a f) : ℂ) := by
  rw [neutralActualZetaHilbertBackgroundOperator_mixed]
  simp only [inner_self_eq_norm_sq_to_K, neutralActualZetaEffectiveBackgroundQuadratic,
    neutralActualZetaHilbertPositiveAnalysis, neutralActualZetaHilbertBackgroundAnalysis,
    comp_apply, Complex.ofReal_sub]

/-- Every certified Green source lift enters the equivalent Hilbert graph
without changing any source or physical coordinate. -/
def neutralActualZetaGreenHilbertSourceLift (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) : NeutralActualZetaHilbertSourceDomain a :=
  neutralActualZetaSourceToHilbert a (neutralActualZetaGreenSourceLift a ha v)

theorem neutralActualZetaGreenHilbertSourceLift_custody (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaHilbertToSource a (neutralActualZetaGreenHilbertSourceLift a ha v) =
      neutralActualZetaGreenSourceLift a ha v :=
  neutralActualZetaHilbertToSource_sourceToHilbert a _

theorem neutralActualZetaGreenHilbertSourceOperator_diagonal (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    inner ℂ (neutralActualZetaGreenHilbertSourceLift a ha v)
      (neutralActualZetaHilbertSourceOperator a (neutralActualZetaGreenHilbertSourceLift a ha v)) =
      ((neutralActualZetaGreenZeroForm a v v).re : ℂ) := by
  rw [neutralActualZetaHilbertSourceOperator_diagonal,
    neutralActualZetaGreenHilbertSourceLift_custody,
    neutralActualZetaGreenSourceQuadratic_eq_zeroForm a ha v]

theorem neutralActualZetaGreenHilbertBackgroundOperator_diagonal (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate) (v : NeutralActualZetaGreenCoefficients) :
    inner ℂ (neutralActualZetaGreenHilbertSourceLift a ha v)
      (neutralActualZetaHilbertBackgroundOperator a s (neutralActualZetaGreenHilbertSourceLift a ha v)) =
      (((neutralActualZetaGreenZeroForm a v v).re +
        ‖neutralActualZetaSelectedNegativeAnalysis a s
          (neutralActualZetaGreenSourceLift a ha v)‖ ^ 2 : ℝ) : ℂ) := by
  rw [neutralActualZetaHilbertBackgroundOperator_diagonal,
    neutralActualZetaGreenHilbertSourceLift_custody,
    neutralActualZetaEffectiveBackgroundQuadratic_add_selected,
    neutralActualZetaGreenSourceQuadratic_eq_zeroForm a ha v]

end
end WeilDefect
