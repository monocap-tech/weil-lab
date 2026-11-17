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
  have hsumFunctions :
      (fun x : ℝ => ∑ i : Fin 242,
        ((d i • neutralNF546OriginalSelectedPhysicalL2 i :
            RealComplexL2) : ℝ → ℂ) x) =ᵐ[volume]
      (fun x : ℝ => ∑ i : Fin 242,
        d i * neutralNF546OriginalWindowGenerator i x) := by
    have hsumRaw := (eventuallyEq_sum
      (s := (Finset.univ : Finset (Fin 242)))
      (fun i _ => hterm i))
    simpa only [Finset.sum_apply] using hsumRaw
  have hsum :
      ((∑ i : Fin 242,
        d i • neutralNF546OriginalSelectedPhysicalL2 i :
          RealComplexL2) : ℝ → ℂ) =ᵐ[volume]
      (fun x => ∑ i : Fin 242,
        d i * neutralNF546OriginalWindowGenerator i x) :=
    (Lp.coeFn_fun_finsetSum Finset.univ
      (fun i : Fin 242 =>
        d i • neutralNF546OriginalSelectedPhysicalL2 i)).trans hsumFunctions
  simpa only [neutralNF549OriginalPhysicalSynthesis,
      Module.Basis.constr_apply_fintype, Pi.basisFun_equivFun,
      LinearEquiv.refl_apply, neutralNF550OriginalWindowSourceCombination]
    using hsum

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
      linarith [hleft.2]⟩
  · exact hx ⟨by
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
    calc
      conj (neutralNF550OriginalSourceCombination d x) *
          (neutralNF548ComplexEvenCollarCutoff x *
            neutralNF550OriginalSourceCombination d x) =
        neutralNF548ComplexEvenCollarCutoff x *
          (conj (neutralNF550OriginalSourceCombination d x) *
            neutralNF550OriginalSourceCombination d x) := by ring
      _ = neutralNF548ComplexEvenCollarCutoff x *
          ((‖neutralNF550OriginalSourceCombination d x‖ ^ 2 : ℝ) : ℂ) := by
        rw [← Complex.normSq_eq_conj_mul_self,
          Complex.normSq_eq_norm_sq]
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
  simpa only [RCLike.inner_apply,
    neutralNF550OriginalSourceCombination] using
      (neutralNF550OriginalCanonicalWeightedSquare_pointwise d x)


/-- All TRUE original 242 selected functions are continuous.
Consequently their unchanged finite complex source combination is
continuous; this is used for the strict-positive real integral. -/
theorem neutralNF550OriginalSourceCombination_continuous
    (d : Fin 242 → ℂ) :
    Continuous (neutralNF550OriginalSourceCombination d) := by
  unfold neutralNF550OriginalSourceCombination
  apply continuous_finsetSum Finset.univ
  intro j hj
  exact continuous_const.mul
    (neutralNF546OriginalComplexGenerator_continuous j)

/-- Reduce the complex-Hermitian canonical Gram to an entirely
REAL nonnegative weighted squared-norm integral. The original
source coefficients and original full physical window are fixed. -/
theorem neutralNF550CanonicalOriginalGram_real_eq_real_weighted_square
    (d : Fin 242 → ℂ) :
    (∑ i : Fin 242,
      conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re =
      ∫ x : ℝ,
        neutralNF548RealEvenCollarCutoff x *
          ‖neutralNF550OriginalSourceCombination d x‖ ^ 2 ∂volume := by
  rw [neutralNF550CanonicalOriginalGram_eq_weighted_square_integral]
  have hp (x : ℝ) :
      neutralNF548ComplexEvenCollarCutoff x *
        ((‖neutralNF550OriginalSourceCombination d x‖ ^ 2 : ℝ) : ℂ) =
      ((neutralNF548RealEvenCollarCutoff x *
          ‖neutralNF550OriginalSourceCombination d x‖ ^ 2 : ℝ) : ℂ) := by
    simp only [neutralNF548ComplexEvenCollarCutoff,
      Complex.ofReal_mul]
  simp_rw [hp]
  simpa only [integral_ofReal, Complex.ofReal_re]

/-- Genuine original canonical Gram is POSITIVE SEMIDEFINITE for
every 242-source coefficient vector, without assuming 136-root
independence. Strictness is precisely the outstanding source
nonvanishing obligation. -/
theorem neutralNF550CanonicalOriginalGram_nonneg
    (d : Fin 242 → ℂ) :
    0 ≤ (∑ i : Fin 242,
      conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re := by
  rw [neutralNF550CanonicalOriginalGram_real_eq_real_weighted_square]
  apply integral_nonneg
  intro x
  exact mul_nonneg (neutralNF548RealEvenCollarCutoff_nonneg x)
    (sq_nonneg _)

/-- The authentic real weighted squared modulus is continuous. -/
theorem neutralNF550CanonicalOriginalSquare_continuous
    (d : Fin 242 → ℂ) :
    Continuous (fun x : ℝ =>
      neutralNF548RealEvenCollarCutoff x *
        ‖neutralNF550OriginalSourceCombination d x‖ ^ 2) := by
  exact neutralNF548RealEvenCollarCutoff_smooth.continuous.mul
    ((neutralNF550OriginalSourceCombination_continuous d).norm.pow 2)

/-- The genuine squared norm weighted by the canonical source
cutoff is integrable, because χ is genuinely C∞ compactly
supported inside the old strict E. -/
theorem neutralNF550CanonicalOriginalSquare_integrable
    (d : Fin 242 → ℂ) :
    Integrable (fun x : ℝ =>
      neutralNF548RealEvenCollarCutoff x *
        ‖neutralNF550OriginalSourceCombination d x‖ ^ 2) volume := by
  apply (neutralNF550CanonicalOriginalSquare_continuous d).integrable_of_hasCompactSupport
  exact neutralNF548RealEvenCollarCutoff_hasCompactSupport.mul_right

/-- EXACT bridge from one nonzero observation inside the TRUE
positive-mass original collar to strict Hermitian positivity of
the original 242-dimensional canonical Gram.

This implication is unconditional given the witness; it does
not assert that a nonzero d always yields such a witness. -/
theorem neutralNF550CanonicalOriginalGram_pos_of_nonzero_at
    (d : Fin 242 → ℂ) (x : ℝ)
    (hχ : 0 < neutralNF548RealEvenCollarCutoff x)
    (hsource : neutralNF550OriginalSourceCombination d x ≠ 0) :
    0 < (∑ i : Fin 242,
      conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re := by
  rw [neutralNF550CanonicalOriginalGram_real_eq_real_weighted_square]
  apply integral_pos_of_integrable_nonneg_nonzero
    (neutralNF550CanonicalOriginalSquare_continuous d)
    (neutralNF550CanonicalOriginalSquare_integrable d)
    (fun y => mul_nonneg (neutralNF548RealEvenCollarCutoff_nonneg y)
      (sq_nonneg _))
  exact ne_of_gt (mul_pos hχ (pow_pos (norm_pos_iff.mpr hsource) 2))

/-- A witness inside the one ACTUAL prescribed positive interval
is sufficient to certify strict positivity of the one canonical
original source Gram. -/
theorem neutralNF550CanonicalOriginalGram_pos_of_original_collar_witness
    (d : Fin 242 → ℂ) (x : ℝ)
    (hx : x ∈ Set.Ioo
      (neutralNF548CollarCenter - 1 / 2000)
      (neutralNF548CollarCenter + 1 / 2000))
    (hsource : neutralNF550OriginalSourceCombination d x ≠ 0) :
    0 < (∑ i : Fin 242,
      conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re := by
  exact neutralNF550CanonicalOriginalGram_pos_of_nonzero_at d x
    (neutralNF548RealEvenCollarCutoff_pos_interval x hx) hsource

/-- Precise last remaining ORIGINAL J242 finite-Gram gate:
if no nonzero original 242-frequency-plus-sinh combination
vanishes on the fixed positive original endpoint collar interval,
the actual canonical original Gram is strictly positive.

NF545 proves this local source independence analytically via
136 distinct exponential-polynomial characteristic roots;
that original independence is NOT YET a Lean theorem. -/
theorem neutralNF550CanonicalOriginalGram_pos_of_collar_separation
    (hsource : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      ∃ x : ℝ,
        x ∈ Set.Ioo
          (neutralNF548CollarCenter - 1 / 2000)
          (neutralNF548CollarCenter + 1 / 2000) ∧
        neutralNF550OriginalSourceCombination d x ≠ 0) :
    ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re := by
  intro d hd
  obtain ⟨x, hx, hnonzero⟩ := hsource d hd
  exact neutralNF550CanonicalOriginalGram_pos_of_original_collar_witness
    d x hx hnonzero

end
end WeilDefect
