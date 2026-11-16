import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalGramPhysicalIntegral

namespace WeilDefect
noncomputable section
open MeasureTheory Module Filter
open scoped SchwartzMap ComplexConjugate

/-!
NF550 — The TRUE canonical original 242-source weighted Gram
quadratic form is the physical integral of its nonnegative
source squared norm.

This is a *source identity* and does not import an unproved
positive-definite Gram axiom. It uses:
  (1) original NF407 exact j_i,
  (2) actual full-window J_i ∈ L²,
  (3) NF548 canonical real-even C∞ nonnegative χ supported in E,
  (4) source weighted synthesis Bχ d from NF547,
  (5) actual continuous L² inner product from NF549.

Strict positivity for every d≠0 still needs the original
exponential-polynomial independence theorem to be proved in Lean.
-/

/-- Exactly the 242 ORIGINAL generator functions combined with
the actual complex coefficients d, without artificial controls. -/
def neutralNF550OriginalSourceCombination
    (d : Fin 242 → ℂ) (x : ℝ) : ℂ :=
  ∑ j : Fin 242,
    d j * neutralNF546OriginalComplexGenerator j x

/-- The zero-extended original physical source combination.
This is a pointwise representative of V(d) ∈ L², not an assertion
that arbitrary L² classes have canonical pointwise values. -/
def neutralNF550OriginalWindowSourceCombination
    (d : Fin 242 → ℂ) (x : ℝ) : ℂ :=
  ∑ j : Fin 242,
    d j * neutralNF546OriginalWindowGenerator j x

/-- The finite original physical L² synthesis V(d) agrees
almost everywhere with the ACTUAL full-window source combination.
The important distinction between L² classes and pointwise
representatives is preserved throughout. -/
theorem neutralNF550OriginalPhysicalSynthesis_ae
    (d : Fin 242 → ℂ) :
    (neutralNF549OriginalPhysicalSynthesis d : ℝ → ℂ) =ᵐ[volume]
      neutralNF550OriginalWindowSourceCombination d := by
  have hterm (i : Fin 242) :
      ((d i • neutralNF546OriginalSelectedPhysicalL2 i :
          RealComplexL2) : ℝ → ℂ) =ᵐ[volume]
      (fun x => d i * neutralNF546OriginalWindowGenerator i x) := by
    filter_upwards
      [Lp.coeFn_smul (d i) (neutralNF546OriginalSelectedPhysicalL2 i),
       neutralNF546OriginalSelectedPhysicalL2_ae i] with x hs hi
    simpa only [Pi.smul_apply, smul_eq_mul, hs, hi]
  have hsum :
      ((∑ i : Fin 242,
        d i • neutralNF546OriginalSelectedPhysicalL2 i :
          RealComplexL2) : ℝ → ℂ) =ᵐ[volume]
      (fun x => ∑ i : Fin 242,
        d i * neutralNF546OriginalWindowGenerator i x) :=
    (Lp.coeFn_fun_finsetSum Finset.univ
      (fun i : Fin 242 =>
        d i • neutralNF546OriginalSelectedPhysicalL2 i)).trans
      (eventuallyEq_sum fun i _ => hterm i)
  simpa only [neutralNF549OriginalPhysicalSynthesis,
      Module.Basis.constr_apply_fintype, Pi.basisFun_repr,
      neutralNF550OriginalWindowSourceCombination] using hsum

/-- The ORIGINAL canonical χ vanishes outside the original
physical aperture. No falsely shrunk physical moment window:
χ lives inside E while J_i live on the full [-B,B]. -/
theorem neutralNF550CanonicalCutoff_zero_outside_physical
    (x : ℝ) (hx : x ∉ neutralNF546OriginalFullPhysicalWindow) :
    neutralNF548ComplexEvenCollarCutoff x = 0 := by
  apply neutralNF548ComplexEvenCollarCutoff_supported x
  intro hE
  rcases hE with hleft | hright
  · exact hx ⟨hleft.1.le, by
      dsimp [neutralNF546OriginalFullPhysicalWindow]
      linarith [hleft.2]⟩
  · exact hx ⟨by
      dsimp [neutralNF546OriginalFullPhysicalWindow]
      linarith [hright.1], hright.2.le⟩

/-- On the unchanged ORIGINAL full source window, the exact
zero-extended physical combination equals the untruncated
original J242 analytic combination, pointwise. -/
theorem neutralNF550OriginalWindowSourceCombination_eq
    (d : Fin 242 → ℂ) (x : ℝ)
    (hx : x ∈ neutralNF546OriginalFullPhysicalWindow) :
    neutralNF550OriginalWindowSourceCombination d x =
      neutralNF550OriginalSourceCombination d x := by
  unfold neutralNF550OriginalWindowSourceCombination
    neutralNF550OriginalSourceCombination
  apply Finset.sum_congr rfl
  intro j hj
  simp [neutralNF546OriginalWindowGenerator,
    Set.indicator_of_mem hx]

/-- Exact pointwise original source identity:
χ * conj(window source sum) * true source sum equals χ * the
squared complex modulus of the original 242-source combination.
The outside-window case uses genuine χ support, not an
assumption that the untruncated j_i are in full-line L². -/
theorem neutralNF550OriginalCanonicalWeightedSquare_pointwise
    (d : Fin 242 → ℂ) (x : ℝ) :
    conj (neutralNF550OriginalWindowSourceCombination d x) *
      (neutralNF548ComplexEvenCollarCutoff x *
        neutralNF550OriginalSourceCombination d x) =
      neutralNF548ComplexEvenCollarCutoff x *
        ((‖neutralNF550OriginalSourceCombination d x‖ ^ 2 : ℝ) : ℂ) := by
  by_cases hx : x ∈ neutralNF546OriginalFullPhysicalWindow
  · rw [neutralNF550OriginalWindowSourceCombination_eq d x hx]
    rw [← RCLike.conj_mul (neutralNF550OriginalSourceCombination d x)]
    ring
  · have hχ := neutralNF550CanonicalCutoff_zero_outside_physical x hx
    simp [hχ]

/-- THE SOURCE-GRAM INTEGRAL BRIDGE: the true original canonical
242×242 Hermitian form is precisely the integral of the nonnegative
squared norm of the original 242-function analytic combination
multiplied by the one fixed true endpoint collar χ.

No numerical quadrature and no selected-root approximation occurs.
Strict positivity for d ≠ 0 is a SEPARATE theorem obligation.
-/
theorem neutralNF550CanonicalOriginalGram_eq_weighted_square_integral
    (d : Fin 242 → ℂ) :
    (∑ i : Fin 242,
      conj (d i) *
        (neutralNF548CanonicalOriginalWeightedGram d) i) =
      ∫ x : ℝ,
        neutralNF548ComplexEvenCollarCutoff x *
          ((‖neutralNF550OriginalSourceCombination d x‖ ^ 2 : ℝ) : ℂ)
        ∂volume := by
  rw [neutralNF549CanonicalGram_quadratic_eq_physical_pairing]
  rw [MeasureTheory.L2.inner_def]
  apply integral_congr_ae
  filter_upwards
    [neutralNF550OriginalPhysicalSynthesis_ae d,
     (neutralNF544BumpSynthesis
       neutralNF548CanonicalOriginalColumns d).coeFn_toLp 2 volume] with x hV hB
  rw [hV, hB]
  rw [neutralNF549CanonicalSynthesis_pointwise]
  exact neutralNF550OriginalCanonicalWeightedSquare_pointwise d x

end
end WeilDefect
