import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalGramSeparationGate

namespace WeilDefect
noncomputable section
open MeasureTheory Module
open scoped SchwartzMap ComplexConjugate

/-!
NF551 — restore the ORIGINAL REAL-ODD Weil test symmetry,
rather than only their complex full-window L² shadows.

The exact NF407 selected generators are REAL and ODD: for
even monomial k the original oscillator x^k sin(2π f x)
is odd, for odd k the x^k cos(2π f x) is odd; the index-241
original pole sinh(x/2) is also odd.

The NF548 canonical χ is REAL, EVEN, compact-smooth and
strictly supported in the genuine two original terminal
collars. Therefore ALL 242 canonical correction columns χj_i
and EVERY complex-linear finite combination are ODD.

This removes a real source-structure risk from NF546–NF550:
preserving full original J242 physical moments alone does NOT
assert the corrected test retains original odd symmetry.
The parity of g itself remains a separate premise.
-/

/-- ORIGINAL NF407 selected oscillator/pole source is ODD
pointwise, for ALL 242 entries. Both source parities of the
oscillator order and the TRUE sinh pole are accounted for. -/
theorem neutralNF551OriginalSelectedRealGenerator_odd
    (i : Fin 242) (x : ℝ) :
    nf545OriginalSelectedRealGenerator i (-x) =
      -nf545OriginalSelectedRealGenerator i x := by
  by_cases hi : i.val < 241
  · simp only [nf545OriginalSelectedRealGenerator, dif_pos hi]
    let node := nf545OriginalOscillatorNodeAt ⟨i.val, hi⟩
    change
      (-x) ^ node.2 *
        (if Even node.2 then
          Real.sin (2 * Real.pi * (node.1 : ℝ) * (-x))
        else
          Real.cos (2 * Real.pi * (node.1 : ℝ) * (-x))) =
      -(x ^ node.2 *
        (if Even node.2 then
          Real.sin (2 * Real.pi * (node.1 : ℝ) * x)
        else
          Real.cos (2 * Real.pi * (node.1 : ℝ) * x)))
    by_cases he : Even node.2
    · simp only [if_pos he]
      rw [he.neg_pow]
      have harg : (2 * Real.pi * (node.1 : ℝ) * (-x)) =
          -(2 * Real.pi * (node.1 : ℝ) * x) := by ring
      rw [harg, Real.sin_neg]
      ring
    · have ho : Odd node.2 := Nat.not_even_iff_odd.mp he
      simp only [if_neg he]
      rw [ho.neg_pow]
      have harg : (2 * Real.pi * (node.1 : ℝ) * (-x)) =
          -(2 * Real.pi * (node.1 : ℝ) * x) := by ring
      rw [harg, Real.cos_neg]
      ring
  · simp only [nf545OriginalSelectedRealGenerator, dif_neg hi]
    have hx : (-x) / 2 = -(x / 2) := by ring
    rw [hx, Real.sinh_neg]

/-- The TRUE original complex physical generator is still odd,
because it is the REAL generator embedded into complex L². -/
theorem neutralNF551OriginalComplexGenerator_odd
    (i : Fin 242) (x : ℝ) :
    neutralNF546OriginalComplexGenerator i (-x) =
      -neutralNF546OriginalComplexGenerator i x := by
  simp only [neutralNF546OriginalComplexGenerator]
  norm_cast
  exact neutralNF551OriginalSelectedRealGenerator_odd i x

/-- Any finite original NF407 source combination has odd
spatial parity, even with arbitrary COMPLEX coefficients. -/
theorem neutralNF551OriginalSourceCombination_odd
    (d : Fin 242 → ℂ) (x : ℝ) :
    neutralNF550OriginalSourceCombination d (-x) =
      -neutralNF550OriginalSourceCombination d x := by
  simp only [neutralNF550OriginalSourceCombination]
  rw [← Finset.sum_neg_distrib]
  apply Finset.sum_congr rfl
  intro i hi
  rw [neutralNF551OriginalComplexGenerator_odd]
  ring

/-- The one TRUE NF548 smooth complex collar cutoff is REAL and
EVEN; in particular conjugation does NOT change the cutoff. -/
theorem neutralNF551CanonicalCutoff_real
    (x : ℝ) :
    conj (neutralNF548ComplexEvenCollarCutoff x) =
      neutralNF548ComplexEvenCollarCutoff x := by
  simp [neutralNF548ComplexEvenCollarCutoff]

/-- Every ORIGINAL source-specific Schwartz column b_i=χj_i is
ODD. This is the missing pointwise Weil-test parity certificate
for the actual NF547/NF548 correction functions. -/
theorem neutralNF551CanonicalOriginalColumn_odd
    (i : Fin 242) (x : ℝ) :
    neutralNF548CanonicalOriginalColumns i (-x) =
      -neutralNF548CanonicalOriginalColumns i x := by
  change
    neutralNF547OriginalWeightedColumn
      neutralNF548ComplexEvenCollarCutoff
      neutralNF548ComplexEvenCollarCutoff_smooth
      neutralNF548ComplexEvenCollarCutoff_hasCompactSupport i (-x) =
    -neutralNF547OriginalWeightedColumn
      neutralNF548ComplexEvenCollarCutoff
      neutralNF548ComplexEvenCollarCutoff_smooth
      neutralNF548ComplexEvenCollarCutoff_hasCompactSupport i x
  rw [neutralNF547OriginalWeightedColumn_apply,
    neutralNF547OriginalWeightedColumn_apply,
    neutralNF548ComplexEvenCollarCutoff_even,
    neutralNF551OriginalComplexGenerator_odd]
  ring

/-- The TRUE source-specific Schwartz synthesis Bχ(d) is ODD
for EVERY coefficient vector d. In particular no arbitrary
choice of χ or 242 correction columns may break parity. -/
theorem neutralNF551CanonicalOriginalSynthesis_odd
    (d : Fin 242 → ℂ) (x : ℝ) :
    (neutralNF544BumpSynthesis
      neutralNF548CanonicalOriginalColumns d) (-x) =
      -(neutralNF544BumpSynthesis
        neutralNF548CanonicalOriginalColumns d) x := by
  rw [neutralNF549CanonicalSynthesis_pointwise,
    neutralNF549CanonicalSynthesis_pointwise,
    neutralNF548ComplexEvenCollarCutoff_even,
    neutralNF551OriginalSourceCombination_odd]
  ring

/-- Even without proving source J242 collar separation yet, if
the canonical Gram is positive (NF550's explicit source gate),
its right inverse always lies in the ORIGINAL ODD Schwartz class.

The Gram inverse may change coefficients but not parity, since
the entire original 242-column correction span is odd. -/
theorem neutralNF551CanonicalRightInverse_odd
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) *
          (neutralNF548CanonicalOriginalWeightedGram d) i).re)
    (d : Fin 242 → ℂ) (x : ℝ) :
    (neutralNF548CanonicalRightInverse hpos d) (-x) =
      -(neutralNF548CanonicalRightInverse hpos d) x := by
  change
    (neutralNF544BumpSynthesis neutralNF548CanonicalOriginalColumns
      ((neutralNF544GramEquiv neutralNF546OriginalSelectedMoments
        neutralNF548CanonicalOriginalColumns
        (neutralNF544PhysicalGram_injective_of_pos
          neutralNF546OriginalSelectedMoments
          neutralNF548CanonicalOriginalColumns hpos)).symm d)) (-x) =
      -(neutralNF544BumpSynthesis neutralNF548CanonicalOriginalColumns
      ((neutralNF544GramEquiv neutralNF546OriginalSelectedMoments
        neutralNF548CanonicalOriginalColumns
        (neutralNF544PhysicalGram_injective_of_pos
          neutralNF546OriginalSelectedMoments
          neutralNF548CanonicalOriginalColumns hpos)).symm d)) x
  exact neutralNF551CanonicalOriginalSynthesis_odd _ x

end
end WeilDefect
