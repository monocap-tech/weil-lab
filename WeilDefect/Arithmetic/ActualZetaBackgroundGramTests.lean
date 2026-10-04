import WeilDefect.Arithmetic.ActualZetaBackgroundFiniteTests

namespace WeilDefect
noncomputable section
open ContinuousLinearMap InnerProductSpace CarrierAudit
open scoped InnerProduct ComplexConjugate
set_option maxHeartbeats 800000
set_option backward.isDefEq.respectTransparency false

namespace CarrierAudit
variable {D E F : Type*}
variable [NormedAddCommGroup D] [InnerProductSpace ℂ D] [CompleteSpace D]
variable [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
variable [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]

/-- Mixed unshifted background Gram form on unchanged domain vectors. -/
def backgroundGram (A : D →L[ℂ] E) (B : D →L[ℂ] F) (u v : D) : ℂ :=
  inner ℂ (A u) (A v) - inner ℂ (B u) (B v)

theorem backgroundGram_diagonal (A : D →L[ℂ] E) (B : D →L[ℂ] F) (u : D) :
    (backgroundGram A B u u).re = ‖A u‖ ^ 2 - ‖B u‖ ^ 2 := by
  simp only [backgroundGram, inner_self_eq_norm_sq_to_K, map_sub,
    RCLike.re_ofReal_pow]

theorem backgroundGram_hermitian (A : D →L[ℂ] E) (B : D →L[ℂ] F) (u v : D) :
    backgroundGram A B u v = conj (backgroundGram A B v u) := by
  simp only [backgroundGram, map_sub, inner_conj_symm]

/-- Unit domination controls mixed interference, not merely each diagonal.
The proof uses the already constructed WD-T10 residual factor. -/
theorem backgroundGram_cauchy_schwarz (A : D →L[ℂ] E) (B : D →L[ℂ] F)
    (h : ∀ f, ‖B f‖ ≤ ‖A f‖) (u v : D) :
    ‖backgroundGram A B u v‖ ^ 2 ≤
      (backgroundGram A B u u).re * (backgroundGram A B v v).re := by
  obtain ⟨X, _, _, hc⟩ := domination_gives_wdt10_factor A B h
  let R := WDT10.effectivePositive ((observationMap A)†) X
  have hc' : A† ∘L A - B† ∘L B = R ∘L R† := by
    rw [← observation_covariance A]
    exact hc
  have hi (x y : D) : backgroundGram A B x y = inner ℂ (R† x) (R† y) := by
    calc
      _ = inner ℂ x ((A† ∘L A - B† ∘L B) y) := by
        simp only [backgroundGram, sub_apply, comp_apply, inner_sub_right,
          adjoint_inner_right]
      _ = inner ℂ x ((R ∘L R†) y) := by rw [hc']
      _ = _ := by simp only [comp_apply, adjoint_inner_right]
  rw [hi u v, hi u u, hi v v, inner_self_eq_norm_sq_to_K,
    inner_self_eq_norm_sq_to_K, RCLike.re_ofReal_pow, RCLike.re_ofReal_pow]
  have hn := norm_inner_le_norm (𝕜 := ℂ) (R† u) (R† v)
  have hp := mul_nonneg (sub_nonneg.mpr hn)
    (add_nonneg (norm_nonneg (inner ℂ (R† u) (R† v)))
      (mul_nonneg (norm_nonneg (R† u)) (norm_nonneg (R† v))))
  nlinarith

end CarrierAudit

/-- Actual Gram form pulled back through the same bounded Green synthesis.
Raw copies are not replaced by independent observation labels. -/
def neutralActualZetaBackgroundGram (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (u v : NeutralActualZetaGreenCoefficients) : ℂ :=
  backgroundGram
    ((neutralActualZetaHilbertPositiveAnalysis a).comp
      (neutralActualZetaGreenHilbertSourceContinuous a ha))
    ((neutralActualZetaHilbertBackgroundAnalysis a s).comp
      (neutralActualZetaGreenHilbertSourceContinuous a ha)) u v

theorem neutralActualZetaBackgroundGram_diagonal (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (v : NeutralActualZetaGreenCoefficients) :
    (neutralActualZetaBackgroundGram a ha s v v).re =
      neutralActualZetaGreenBackgroundTest a ha s v := by
  rw [neutralActualZetaBackgroundGram, backgroundGram_diagonal,
    neutralActualZetaGreenBackgroundTest_hilbert]
  rfl

/-- The Gram form is the existing actual background operator evaluated on
the same two Green graph vectors, not a replacement operator. -/
theorem neutralActualZetaBackgroundGram_operator (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (u v : NeutralActualZetaGreenCoefficients) :
    neutralActualZetaBackgroundGram a ha s u v =
      inner ℂ (neutralActualZetaGreenHilbertSourceContinuous a ha u)
        (neutralActualZetaHilbertBackgroundOperator a s
          (neutralActualZetaGreenHilbertSourceContinuous a ha v)) := by
  rw [neutralActualZetaHilbertBackgroundOperator_mixed]
  rfl

/-- Synthesis collisions give identical entire Gram rows. In particular,
repeated-ordinate packet copies cannot improve mixed observability. -/
theorem neutralActualZetaBackgroundGram_synthesis_collision (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (u v z : NeutralActualZetaGreenCoefficients)
    (h : neutralActualZetaGreenHilbertSourceContinuous a ha u =
      neutralActualZetaGreenHilbertSourceContinuous a ha v) :
    neutralActualZetaBackgroundGram a ha s u z =
      neutralActualZetaBackgroundGram a ha s v z := by
  simp only [neutralActualZetaBackgroundGram, backgroundGram, comp_apply]
  rw [h]

/-- Necessary mixed-packet bound from the exact finite positivity criterion.
A collection of positive single-copy diagonal tests alone is insufficient. -/
theorem neutralActualZetaBackgroundGram_cauchy_schwarz (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (h : ∀ (t : Finset NeutralActualZetaDivisorCoordinate)
      (c : NeutralActualZetaDivisorCoordinate → ℂ),
      0 ≤ neutralActualZetaGreenBackgroundTest a ha s
        (neutralActualZetaFiniteCoefficients t c))
    (u v : NeutralActualZetaGreenCoefficients) :
    ‖neutralActualZetaBackgroundGram a ha s u v‖ ^ 2 ≤
      neutralActualZetaGreenBackgroundTest a ha s u *
        neutralActualZetaGreenBackgroundTest a ha s v := by
  have hp := (neutralActualZetaGreenBackground_lifts_iff_finite a ha s).mpr h
  have hd : ∀ x : NeutralActualZetaGreenCoefficients,
      ‖((neutralActualZetaHilbertBackgroundAnalysis a s).comp
        (neutralActualZetaGreenHilbertSourceContinuous a ha)) x‖ ≤
      ‖((neutralActualZetaHilbertPositiveAnalysis a).comp
        (neutralActualZetaGreenHilbertSourceContinuous a ha)) x‖ := by
    intro x
    have hx := hp x
    rw [neutralActualZetaGreenBackgroundTest_hilbert] at hx
    change ‖neutralActualZetaHilbertBackgroundAnalysis a s
      (neutralActualZetaGreenHilbertSourceContinuous a ha x)‖ ≤
      ‖neutralActualZetaHilbertPositiveAnalysis a
        (neutralActualZetaGreenHilbertSourceContinuous a ha x)‖
    nlinarith [norm_nonneg (neutralActualZetaHilbertPositiveAnalysis a
      (neutralActualZetaGreenHilbertSourceContinuous a ha x)),
      norm_nonneg (neutralActualZetaHilbertBackgroundAnalysis a s
        (neutralActualZetaGreenHilbertSourceContinuous a ha x))]
  have hh := backgroundGram_cauchy_schwarz _ _ hd u v
  change ‖neutralActualZetaBackgroundGram a ha s u v‖ ^ 2 ≤
    (neutralActualZetaBackgroundGram a ha s u u).re *
      (neutralActualZetaBackgroundGram a ha s v v).re at hh
  rw [neutralActualZetaBackgroundGram_diagonal,
    neutralActualZetaBackgroundGram_diagonal] at hh
  exact hh

/-- A strict mixed Gram violation produces a finite actual negative packet,
and thereby rules out every unit background factor on the relevant completion.
This theorem does not assert that an actual violating pair has been found. -/
theorem neutralActualZetaBackgroundGram_violation_finite_negative (a : ℝ) (ha : 0 < a)
    (s : Finset NeutralActualZetaDivisorCoordinate)
    (u v : NeutralActualZetaGreenCoefficients)
    (h : neutralActualZetaGreenBackgroundTest a ha s u *
        neutralActualZetaGreenBackgroundTest a ha s v <
      ‖neutralActualZetaBackgroundGram a ha s u v‖ ^ 2) :
    ∃ (t : Finset NeutralActualZetaDivisorCoordinate)
      (c : NeutralActualZetaDivisorCoordinate → ℂ),
      neutralActualZetaGreenBackgroundTest a ha s
        (neutralActualZetaFiniteCoefficients t c) < 0 := by
  by_contra hn
  push Not at hn
  have hh := neutralActualZetaBackgroundGram_cauchy_schwarz a ha s hn u v
  linarith

end
end WeilDefect
