import WeilDefect.Arithmetic.ActualZetaOriginalLogDyadicGraphLimit

namespace WeilDefect
noncomputable section
open Filter InnerProductSpace
open scoped ComplexConjugate

/-!
NF574: specialize the graph limit to the exact all-strip raw
transform hypothesis of the historical endpoint-log approximation
(NF524/NF528). The bound and log-carrier convergence are
explicit analytical inputs. No RH or Gram assumption.
-/

def neutralNF574StripEnvelope (t : ℝ) : ℝ :=
  (1 + Real.log (2 + |t|)) / (1 + |t|)

/-- The source pair normalization is the authentic raw sqrt(2)
normalization, not the normalized signed covariance convention. -/
theorem neutralNF574RawPair_sq_bound
    (A B c : ℂ) (W : ℝ)
    (hA : ‖A‖^2 ≤ W) (hB : ‖B‖^2 ≤ W) :
    ‖c*(A+B)‖^2 ≤ 4*‖c‖^2*W ∧
      ‖c*(A-B)‖^2 ≤ 4*‖c‖^2*W := by
  have hplus := pow_le_pow_left₀ (norm_nonneg (A+B)) (norm_add_le A B) 2
  have hminus := pow_le_pow_left₀ (norm_nonneg (A-B)) (norm_sub_le A B) 2
  have hsplus : ‖A+B‖^2 ≤ 4*W := by
    nlinarith only [hplus, sq_nonneg (‖A‖-‖B‖), hA, hB]
  have hsminus : ‖A-B‖^2 ≤ 4*W := by
    nlinarith only [hminus, sq_nonneg (‖A‖-‖B‖), hA, hB]
  constructor
  · rw [norm_mul, mul_pow]
    calc
      _ ≤ ‖c‖^2*(4*W) :=
        mul_le_mul_of_nonneg_left hsplus (sq_nonneg _)
      _ = _ := by ring
  · rw [norm_mul, mul_pow]
    calc
      _ ≤ ‖c‖^2*(4*W) :=
        mul_le_mul_of_nonneg_left hsminus (sq_nonneg _)
      _ = _ := by ring

/-- Both complete source coordinates of a carrier vector are
dominated by the actual logarithmic dyadic weight whenever its
raw physical window samples have the NF524/NF528 strip bound. -/
theorem neutralNF574ActualSourcePair_of_stripEnvelope
    (a : ℝ) (f : NeutralLogHilbertCarrier a) (M : ℝ) (hM : 0 ≤ M)
    (hstrip : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation a z (neutralLogPhysical f.val)‖ ≤
        M * neutralNF574StripEnvelope z.re)
    (q : NeutralActualZetaDivisorCoordinate) :
    ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) f‖^2
        ≤ (16 * ‖((Real.sqrt 2)⁻¹ : ℂ)‖^2 * M^2) * neutralNF574LogDyadicWeight q ∧
    ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) f‖^2
        ≤ (16 * ‖((Real.sqrt 2)⁻¹ : ℂ)‖^2 * M^2) * neutralNF574LogDyadicWeight q := by
  let z := neutralActualZetaDivisorOrdinate q
  have hz : |z.im| ≤ 1/2 :=
    (neutralActualZetaOrdinate_strictStrip q.1).le
  have hzc : |(conj z).im| ≤ 1/2 := by
    simpa only [Complex.conj_im, abs_neg] using hz
  have hre : z.re = q.1.val.im := neutralActualZetaOrdinate_re q.1
  have hzcRe : (conj z).re = z.re := Complex.conj_re z
  have hb (w : ℂ) (hw : |w.im| ≤ 1/2) (hr : w.re = q.1.val.im) :
      ‖neutralWindowEvaluation a w (neutralLogPhysical f.val)‖^2 ≤
        4*M^2*neutralNF574LogDyadicWeight q := by
    have hh := pow_le_pow_left₀ (norm_nonneg _) (hstrip w hw) 2
    rw [mul_pow, neutralNF574StripEnvelope, hr] at hh
    calc
      _ ≤ M^2 * ((1 + Real.log (2 + |q.1.val.im|)) /
          (1 + |q.1.val.im|))^2 := hh
      _ ≤ M^2 * (4 * neutralNF574LogDyadicWeight q) :=
        mul_le_mul_of_nonneg_left (neutralNF574LogStripEnvelope_sq_le q) (sq_nonneg M)
      _ = _ := by ring
  have hpair := neutralNF574RawPair_sq_bound
    (neutralWindowEvaluation a (conj z) (neutralLogPhysical f.val))
    (neutralWindowEvaluation a z (neutralLogPhysical f.val))
    ((Real.sqrt 2)⁻¹ : ℂ) (4*M^2*neutralNF574LogDyadicWeight q)
    (hb (conj z) hzc (hzcRe.trans hre)) (hb z hz hre)
  rw [neutralLogPositivePairSource_inner, neutralLogNegativePairSource_inner]
  constructor
  · calc
      _ ≤ 4*‖((Real.sqrt 2)⁻¹ : ℂ)‖^2*
        (4*M^2*neutralNF574LogDyadicWeight q) := hpair.1
      _ = _ := by ring
  · calc
      _ ≤ 4*‖((Real.sqrt 2)⁻¹ : ℂ)‖^2*
        (4*M^2*neutralNF574LogDyadicWeight q) := hpair.2
      _ = _ := by ring

/-- The ORIGINAL B=11/10 graph limit gate. Once the historical
U400 endpoint target k and collar-compressed/mollified log-carrier
vectors g have their common all-strip estimate and LOG-norm
convergence, this theorem supplies both target and approximant
graph admission and convergence of every actual divisor sample
in ℓ² simultaneously. The same k and g are retained. -/
theorem neutralNF574OriginalFullSourceLimit_of_stripEnvelope
    {ι : Type*} {l : Filter ι}
    (k : NeutralLogHilbertCarrier (11/10 : ℝ))
    (g : ι → NeutralLogHilbertCarrier (11/10 : ℝ))
    (hg : Tendsto g l (nhds k))
    (M : ℝ) (hM : 0 ≤ M)
    (hkt : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10 : ℝ) z (neutralLogPhysical k.val)‖ ≤
        M * neutralNF574StripEnvelope z.re)
    (hgt : ∀ (i : ι) (z : ℂ), |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10 : ℝ) z (neutralLogPhysical (g i).val)‖ ≤
        M * neutralNF574StripEnvelope z.re) :
    ∃ (K : NeutralActualZetaSourceDomain (11/10 : ℝ))
      (G : ι → NeutralActualZetaSourceDomain (11/10 : ℝ)),
      neutralActualZetaSourcePhysical (11/10 : ℝ) K = k ∧
      (∀ i, neutralActualZetaSourcePhysical (11/10 : ℝ) (G i) = g i) ∧
      Tendsto G l (nhds K) := by
  apply neutralNF574ActualFullGraphLimit_of_dyadicDomination
    (11/10 : ℝ) k g hg (16 * ‖((Real.sqrt 2)⁻¹ : ℂ)‖^2 * M^2)
    (by positivity)
  · intro q
    exact (neutralNF574ActualSourcePair_of_stripEnvelope _ k M hM hkt q).1
  · intro q
    exact (neutralNF574ActualSourcePair_of_stripEnvelope _ k M hM hkt q).2
  · intro i q
    exact (neutralNF574ActualSourcePair_of_stripEnvelope _ (g i) M hM (hgt i) q).1
  · intro i q
    exact (neutralNF574ActualSourcePair_of_stripEnvelope _ (g i) M hM (hgt i) q).2

end
end WeilDefect
