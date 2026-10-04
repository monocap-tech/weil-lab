import WeilDefect.Arithmetic.ActualZetaNativeSourceAttachment
import Mathlib.Topology.Algebra.Module.ClosedSubmodule

namespace WeilDefect
noncomputable section
open InnerProductSpace MeasureTheory FourierTransform
open scoped FourierTransform ComplexConjugate ENNReal
set_option maxHeartbeats 800000

/-- Physical logarithmic coordinate together with both complete actual-divisor
source coefficient vectors. The product norm is the source graph norm. -/
abbrev NeutralActualZetaSourceAmbient (a : ℝ) :=
  NeutralLogHilbertCarrier a ×
    (NeutralActualZetaGreenCoefficients × NeutralActualZetaGreenCoefficients)

/-- The full actual source graph: every coordinate is the same physical
vector's positive or negative sample, including each multiplicity copy. -/
def neutralActualZetaSourceGraphSubmodule (a : ℝ) :
    Submodule ℂ (NeutralActualZetaSourceAmbient a) where
  carrier := {x | ∀ q : NeutralActualZetaDivisorCoordinate,
    x.2.1 q = inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) x.1 ∧
    x.2.2 q = inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) x.1}
  zero_mem' := by intro q; simp
  add_mem' := by
    intro x y hx hy q
    constructor
    · change x.2.1 q + y.2.1 q = inner ℂ
        (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) (x.1 + y.1)
      rw [inner_add_right, (hx q).1, (hy q).1]
    · change x.2.2 q + y.2.2 q = inner ℂ
        (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) (x.1 + y.1)
      rw [inner_add_right, (hx q).2, (hy q).2]
  smul_mem' := by
    intro c x hx q
    constructor
    · change c * x.2.1 q = inner ℂ
        (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) (c • x.1)
      exact (congrArg (fun z : ℂ => c * z) (hx q).1).trans
        (inner_smul_right (𝕜 := ℂ)
          (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) x.1 c).symm
    · change c * x.2.2 q = inner ℂ
        (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) (c • x.1)
      exact (congrArg (fun z : ℂ => c * z) (hx q).2).trans
        (inner_smul_right _ _ _).symm

/-- Closure is proved coordinatewise, using bounded Hilbert source evaluation
and continuous evaluation in ℓ². No retained-mode membership is assumed. -/
theorem neutralActualZetaSourceGraph_isClosed (a : ℝ) :
    IsClosed (neutralActualZetaSourceGraphSubmodule a :
      Set (NeutralActualZetaSourceAmbient a)) := by
  change IsClosed {x : NeutralActualZetaSourceAmbient a | ∀ q,
    x.2.1 q = inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) x.1 ∧
    x.2.2 q = inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) x.1}
  simp only [Set.ofPred_forall]
  apply isClosed_iInter
  intro q
  have hp : Continuous (fun x : NeutralActualZetaSourceAmbient a => x.2.1 q) :=
    ((lp.evalCLM ℂ (fun _ : NeutralActualZetaDivisorCoordinate => ℂ) 2 q).continuous.comp
      (continuous_fst.comp continuous_snd))
  have hn : Continuous (fun x : NeutralActualZetaSourceAmbient a => x.2.2 q) :=
      ((lp.evalCLM ℂ (fun _ : NeutralActualZetaDivisorCoordinate => ℂ) 2 q).continuous.comp
        (continuous_snd.comp continuous_snd))
  have hfst : Continuous (fun x : NeutralActualZetaSourceAmbient a => x.1) :=
    continuous_fst
  have hcp : Continuous (fun _ : NeutralActualZetaSourceAmbient a =>
      neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) := continuous_const
  have hcn : Continuous (fun _ : NeutralActualZetaSourceAmbient a =>
      neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) := continuous_const
  have hsp : Continuous (fun x : NeutralActualZetaSourceAmbient a =>
      inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) x.1) :=
    hcp.inner (𝕜 := ℂ) hfst
  have hsn : Continuous (fun x : NeutralActualZetaSourceAmbient a =>
      inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) x.1) :=
    continuous_const.inner (𝕜 := ℂ) continuous_fst
  exact (isClosed_eq hp hsp).inter (isClosed_eq hn hsn)

/-- A concrete complete source domain with the graph norm. -/
def neutralActualZetaSourceGraph (a : ℝ) :
    ClosedSubmodule ℂ (NeutralActualZetaSourceAmbient a) :=
  ⟨neutralActualZetaSourceGraphSubmodule a, neutralActualZetaSourceGraph_isClosed a⟩

abbrev NeutralActualZetaSourceDomain (a : ℝ) := neutralActualZetaSourceGraph a

def neutralActualZetaSourcePhysical (a : ℝ) :
    NeutralActualZetaSourceDomain a →L[ℂ] NeutralLogHilbertCarrier a :=
  (ContinuousLinearMap.fst ℂ _ _).comp
    (neutralActualZetaSourceGraph a).toSubmodule.subtypeL

def neutralActualZetaPositiveAnalysis (a : ℝ) :
    NeutralActualZetaSourceDomain a →L[ℂ] NeutralActualZetaGreenCoefficients :=
  (ContinuousLinearMap.fst ℂ _ _).comp
    ((ContinuousLinearMap.snd ℂ _ _).comp
      (neutralActualZetaSourceGraph a).toSubmodule.subtypeL)

def neutralActualZetaNegativeAnalysis (a : ℝ) :
    NeutralActualZetaSourceDomain a →L[ℂ] NeutralActualZetaGreenCoefficients :=
  (ContinuousLinearMap.snd ℂ _ _).comp
    ((ContinuousLinearMap.snd ℂ _ _).comp
      (neutralActualZetaSourceGraph a).toSubmodule.subtypeL)

theorem neutralActualZetaSourceDomain_complete (a : ℝ) :
    CompleteSpace (NeutralActualZetaSourceDomain a) := inferInstance

theorem neutralActualZetaSourceAnalysis_sampling (a : ℝ)
    (f : NeutralActualZetaSourceDomain a) (q : NeutralActualZetaDivisorCoordinate) :
    neutralActualZetaPositiveAnalysis a f q =
      inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q))
        (neutralActualZetaSourcePhysical a f) ∧
    neutralActualZetaNegativeAnalysis a f q =
      inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q))
        (neutralActualZetaSourcePhysical a f) :=
  f.property q

theorem neutralActualZetaSourceAnalysis_norm_le (a : ℝ)
    (f : NeutralActualZetaSourceDomain a) :
    ‖neutralActualZetaPositiveAnalysis a f‖ ≤ ‖f‖ ∧
    ‖neutralActualZetaNegativeAnalysis a f‖ ≤ ‖f‖ := by
  change ‖f.val.2.1‖ ≤ ‖f.val‖ ∧ ‖f.val.2.2‖ ≤ ‖f.val‖
  constructor
  · exact (norm_fst_le f.val.2).trans (norm_snd_le f.val)
  · exact (norm_snd_le f.val.2).trans (norm_snd_le f.val)

/-- The established same-vector summability supplies both ℓ² coordinates,
so every constructed Green vector has an actual source-domain lift. -/
def neutralActualZetaGreenSourceLift (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) : NeutralActualZetaSourceDomain a := by
  let f := neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v)
  let p : NeutralActualZetaGreenCoefficients := ⟨
    fun q => inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) f,
    memℓp_gen (by simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using
      neutralActualZetaGreenCanonical_positiveSource_sq_summable a ha v)⟩
  let n : NeutralActualZetaGreenCoefficients := ⟨
    fun q => inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) f,
    memℓp_gen (by simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using
      neutralActualZetaGreenCanonical_negativeSource_sq_summable a ha v)⟩
  exact ⟨(f, p, n), fun _ => ⟨rfl, rfl⟩⟩

theorem neutralActualZetaGreenSourceLift_physical (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaSourcePhysical a (neutralActualZetaGreenSourceLift a ha v) =
      neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v) := rfl

/-- Exact coefficient norm normalization: the full multiplicity-preserving
source graph counts each two-point partner orbit twice. -/
theorem neutralActualZetaGreenSourceLift_energy (a : ℝ) (ha : 0 < a)
    (v : NeutralActualZetaGreenCoefficients) :
    ‖neutralActualZetaPositiveAnalysis a (neutralActualZetaGreenSourceLift a ha v)‖ ^ 2 -
      ‖neutralActualZetaNegativeAnalysis a (neutralActualZetaGreenSourceLift a ha v)‖ ^ 2 =
    2 * ((∫ ξ : ℝ, rightLimitCompactWeilSymbolMathlib a ξ *
      ‖(𝓕 (neutralActualZetaGreenSynthesis a v) : RealComplexL2) ξ‖ ^ 2) +
      2 * (conj (sourceWindowMoment a (-(1/2)) (neutralActualZetaGreenSynthesis a v)) *
        sourceWindowMoment a (1/2) (neutralActualZetaGreenSynthesis a v)).re) := by
  have hp := (lp.hasSum_norm (by norm_num : 0 < (2 : ℝ≥0∞).toReal)
    (neutralActualZetaPositiveAnalysis a (neutralActualZetaGreenSourceLift a ha v))).tsum_eq
  have hn := (lp.hasSum_norm (by norm_num : 0 < (2 : ℝ≥0∞).toReal)
    (neutralActualZetaNegativeAnalysis a (neutralActualZetaGreenSourceLift a ha v))).tsum_eq
  simp only [ENNReal.toReal_ofNat, Real.rpow_two] at hp hn
  rw [← hp, ← hn]
  exact neutralActualZetaGreenSourceEnergy_native_quadratic a ha v

end
end WeilDefect
