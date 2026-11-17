import WeilDefect.Arithmetic.ActualZetaOriginalRealOddSchwartzFullSource
import WeilDefect.Arithmetic.ActualZetaOriginalJ242OddParity
import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalGramPhysicalIntegral
import Mathlib.Topology.Algebra.Module.FiniteDimension

namespace WeilDefect
noncomputable section
open MeasureTheory Filter Module
open scoped SchwartzMap ComplexConjugate
set_option maxHeartbeats 1500000

/-!
NF573: lift the actual finite-rank correction into the original
full source graph, using the complete actual divisor, not a
Green basis or a truncated zero analysis. Only 242 individually
admissible columns are needed for a bounded graph correction.
Uncorrected seed graph convergence is a distinct hypothesis.
-/

/-- Physical L² realization of the actual full source graph. -/
def neutralNF573OriginalGraphPhysical :
    NeutralActualZetaSourceDomain (11 / 10 : ℝ) →L[ℂ] RealComplexL2 :=
  neutralLogPhysical.comp
    (((neutralLogHilbertSubmodule (11 / 10 : ℝ)).toSubmodule.subtypeL).comp
      (neutralActualZetaSourcePhysical (11 / 10 : ℝ)))

/-- The actual selected moments on the genuine complete source graph
are automatically continuous, via the continuous physical projection. -/
def neutralNF573OriginalGraphMoments :
    NeutralActualZetaSourceDomain (11 / 10 : ℝ) →L[ℂ] (Fin 242 → ℂ) :=
  neutralNF546OriginalSelectedMomentsCLM.comp neutralNF573OriginalGraphPhysical

/-- Each exact canonical column has the real, odd, smooth, supported
structure needed for full-divisor graph admission. -/
theorem neutralNF573CanonicalColumn_real (j : Fin 242) (x : ℝ) :
    conj (neutralNF548CanonicalOriginalColumns j x) =
      neutralNF548CanonicalOriginalColumns j x := by
  change conj (neutralNF547OriginalWeightedColumn
    neutralNF548ComplexEvenCollarCutoff
    neutralNF548ComplexEvenCollarCutoff_smooth
    neutralNF548ComplexEvenCollarCutoff_hasCompactSupport j x) =
    neutralNF547OriginalWeightedColumn
      neutralNF548ComplexEvenCollarCutoff
      neutralNF548ComplexEvenCollarCutoff_smooth
      neutralNF548ComplexEvenCollarCutoff_hasCompactSupport j x
  rw [neutralNF547OriginalWeightedColumn_apply]
  simp [neutralNF548ComplexEvenCollarCutoff,
    neutralNF546OriginalComplexGenerator]

/-- EXACT physical realization of each of the original 242 columns
in the complete actual-multiplicity source graph. No Gram positivity
needed for admission of the columns themselves. -/
theorem neutralNF573CanonicalColumn_fullSource (j : Fin 242) :
    ∃ v : NeutralActualZetaSourceDomain (11 / 10 : ℝ),
      neutralNF573OriginalGraphPhysical v =
        (neutralNF548CanonicalOriginalColumns j).toLp 2 volume :=
  neutralNF573OriginalRealOddSchwartz_fullSource
    (neutralNF548CanonicalOriginalColumns j)
    (fun x hx => neutralNF548CanonicalOriginalColumns_supported j x hx)
    (neutralNF573CanonicalColumn_real j)
    (neutralNF551CanonicalOriginalColumn_odd j)

/-- The finite graph synthesis is continuous because its coefficient
domain is finite-dimensional. The column graph vectors must realize
the actual NF548 columns, with both complete P/N vectors. -/
def neutralNF573GraphColumnSynthesis
    (v : Fin 242 → NeutralActualZetaSourceDomain (11 / 10 : ℝ)) :
    (Fin 242 → ℂ) →L[ℂ] NeutralActualZetaSourceDomain (11 / 10 : ℝ) :=
  by
    let L := (Pi.basisFun ℂ (Fin 242)).constr ℂ v
    refine L.mkContinuous (∑ j : Fin 242, ‖v j‖) ?_
    intro d
    change ‖((Pi.basisFun ℂ (Fin 242)).constr ℂ v) d‖ ≤ _
    rw [Module.Basis.constr_apply_fintype]
    simp only [Pi.basisFun_repr]
    calc
      ‖∑ j : Fin 242, d j • v j‖ ≤ ∑ j : Fin 242, ‖d j • v j‖ := norm_sum_le _ _
      _ ≤ ∑ j : Fin 242, ‖v j‖ * ‖d‖ := by
        apply Finset.sum_le_sum
        intro j hj
        calc
          ‖d j • v j‖ ≤ ‖d j‖ * ‖v j‖ := norm_smul_le _ _
          _ ≤ ‖d‖ * ‖v j‖ := mul_le_mul_of_nonneg_right (norm_le_pi_norm d j) (norm_nonneg _)
          _ = _ := mul_comm _ _
      _ = _ := Finset.sum_mul ..

/-- Exact physical custody of the graph synthesis, conditional only
on the individual column physical equalities. -/
theorem neutralNF573GraphColumnSynthesis_physical
    (v : Fin 242 → NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (hv : ∀ j, neutralNF573OriginalGraphPhysical (v j) =
      (neutralNF548CanonicalOriginalColumns j).toLp 2 volume)
    (d : Fin 242 → ℂ) :
    neutralNF573OriginalGraphPhysical (neutralNF573GraphColumnSynthesis v d) =
      (neutralNF544BumpSynthesis neutralNF548CanonicalOriginalColumns d).toLp 2 volume := by
  change neutralNF573OriginalGraphPhysical
      (((Pi.basisFun ℂ (Fin 242)).constr ℂ v) d) =
    SchwartzMap.toLpCLM ℂ ℂ 2 volume
      (neutralNF544BumpSynthesis neutralNF548CanonicalOriginalColumns d)
  simp only [neutralNF544BumpSynthesis, Module.Basis.constr_apply_fintype,
    Pi.basisFun_repr, map_sum, map_smul, hv]
  rfl

/-- The SAME actual NF544 inverse Gram, followed by finite synthesis
into the complete source graph. Positivity remains an explicit premise. -/
def neutralNF573GraphRightInverse
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (v : Fin 242 → NeutralActualZetaSourceDomain (11 / 10 : ℝ)) :
    (Fin 242 → ℂ) →L[ℂ] NeutralActualZetaSourceDomain (11 / 10 : ℝ) :=
  (neutralNF573GraphColumnSynthesis v).comp
    (LinearMap.toContinuousLinearMap
      (neutralNF544GramEquiv neutralNF546OriginalSelectedMoments
        neutralNF548CanonicalOriginalColumns
        (neutralNF544PhysicalGram_injective_of_pos
          neutralNF546OriginalSelectedMoments
          neutralNF548CanonicalOriginalColumns hpos)).symm.toLinearMap)

/-- This graph right inverse has precisely the actual NF548
physical correction; no graph-space fit replaces the finite inverse. -/
theorem neutralNF573GraphRightInverse_physical
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (v : Fin 242 → NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (hv : ∀ j, neutralNF573OriginalGraphPhysical (v j) =
      (neutralNF548CanonicalOriginalColumns j).toLp 2 volume)
    (d : Fin 242 → ℂ) :
    neutralNF573OriginalGraphPhysical (neutralNF573GraphRightInverse hpos v d) =
      (neutralNF548CanonicalRightInverse hpos d).toLp 2 volume := by
  change neutralNF573OriginalGraphPhysical
    (neutralNF573GraphColumnSynthesis v
      ((neutralNF544GramEquiv neutralNF546OriginalSelectedMoments
        neutralNF548CanonicalOriginalColumns
        (neutralNF544PhysicalGram_injective_of_pos
          neutralNF546OriginalSelectedMoments
          neutralNF548CanonicalOriginalColumns hpos)).symm d)) = _
  exact neutralNF573GraphColumnSynthesis_physical v hv _

/-- A bounded right inverse in the FULL original source graph,
with its exact physical identification and all 242 same-source moments.
Its existence uses individual graph admission, not any uniform bound
on arbitrary smooth tests or on the raw sample operator in physical L². -/
theorem neutralNF573OriginalGraphRightInverse_exists
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re) :
    ∃ R : (Fin 242 → ℂ) →L[ℂ] NeutralActualZetaSourceDomain (11 / 10 : ℝ),
      (∀ d, neutralNF573OriginalGraphPhysical (R d) =
        (neutralNF548CanonicalRightInverse hpos d).toLp 2 volume) ∧
      (∀ d, neutralNF573OriginalGraphMoments (R d) = d) := by
  classical
  choose v hv using neutralNF573CanonicalColumn_fullSource
  refine ⟨neutralNF573GraphRightInverse hpos v, ?_, ?_⟩
  · exact neutralNF573GraphRightInverse_physical hpos v hv
  · intro d
    change neutralNF546OriginalSelectedMoments
      (neutralNF573OriginalGraphPhysical
        (neutralNF573GraphRightInverse hpos v d)) = d
    rw [neutralNF573GraphRightInverse_physical hpos v hv]
    exact neutralNF548CanonicalRightInverse_correct hpos d

/-- A single bounded graph correction preserves every convergent
seed family in the complete source topology. The convergence of
the uncorrected seeds to the original target is STILL a hypothesis. -/
theorem neutralNF573OriginalGraphCorrection_preservesConvergence
    {ι : Type*} {l : Filter ι}
    (R : (Fin 242 → ℂ) →L[ℂ] NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (ell : NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (g : ι → NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (hg : Tendsto g l (nhds ell)) :
    Tendsto (fun s => neutralNF543CorrectGraph
      neutralNF573OriginalGraphMoments R ell (g s)) l (nhds ell) :=
  neutralNF543CorrectGraph_tendsto neutralNF573OriginalGraphMoments R ell g hg

/-- The graph-level corrected seed is exactly the original physical
Schwartz correction, provided the seed realizes that same Schwartz
test. This prevents treating an unrelated graph sequence as a
certificate for the canonical physical correction. -/
theorem neutralNF573OriginalGraphCorrectedSeed_physical
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (R : (Fin 242 → ℂ) →L[ℂ] NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (hR : ∀ d, neutralNF573OriginalGraphPhysical (R d) =
      (neutralNF548CanonicalRightInverse hpos d).toLp 2 volume)
    (ell g : NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (s : 𝓢(ℝ, ℂ))
    (hs : neutralNF573OriginalGraphPhysical g = s.toLp 2 volume) :
    neutralNF573OriginalGraphPhysical
      (neutralNF543CorrectGraph neutralNF573OriginalGraphMoments R ell g) =
      (neutralNF543Correct neutralNF546OriginalSelectedMoments
        (neutralNF548CanonicalRightInverse hpos)
        (neutralNF573OriginalGraphPhysical ell) s).toLp 2 volume := by
  unfold neutralNF543CorrectGraph
  rw [map_add, hR, hs]
  have hm (u : NeutralActualZetaSourceDomain (11 / 10 : ℝ)) :
      neutralNF573OriginalGraphMoments u =
      neutralNF546OriginalSelectedMoments
        (neutralNF573OriginalGraphPhysical u) := rfl
  rw [hm ell, hm g, hs]
  change s.toLp 2 volume +
    (neutralNF548CanonicalRightInverse hpos
      (neutralNF546OriginalSelectedMoments (neutralNF573OriginalGraphPhysical ell) -
        neutralNF546OriginalSelectedMoments (s.toLp 2 volume))).toLp 2 volume =
    SchwartzMap.toLpCLM ℂ ℂ 2 volume
      (s + neutralNF548CanonicalRightInverse hpos
        (neutralNF546OriginalSelectedMoments (neutralNF573OriginalGraphPhysical ell) -
          neutralNF546OriginalSelectedMoments (s.toLp 2 volume)))
  rw [map_add]
  rfl

end
end WeilDefect
