import WeilDefect.Arithmetic.CP_C1H_OriginalPointwisePrimeCorrelation
import Mathlib.MeasureTheory.Group.Integral
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
CP-C1(H2) — original frozen Schwartz source NF600 integral transport.
Source candidate only. H1 must first pass genuine Lean v4.34 compilation.
This module imports exactly the original H1 orientation theorems, does
not duplicate them, and discharges the source correlation integral
hypotheses of CP-C1(G) using the same genuine CP001 flat bumps.
No spectral target, pole/Gamma sign, universal positivity, or RH.
-/

private def LC : Set ℝ := Ioo (-(11/10:ℝ)) (-(11/10:ℝ)+1/500)
private def RC : Set ℝ := Ioo ((11/10:ℝ)-1/500) (11/10:ℝ)

private theorem LC_mem_old (x : ℝ) (hx : x ∈ LC) :
    x ∈ neutralNF543OriginalCollars := Or.inl hx

private theorem RC_mem_old (x : ℝ) (hx : x ∈ RC) :
    x ∈ neutralNF543OriginalCollars := Or.inr hx

private theorem pair_supported
    (L R : 𝓢(ℝ, ℂ))
    (hL : ∀ x : ℝ, x ∉ LC → L x = 0)
    (hR : ∀ x : ℝ, x ∉ RC → R x = 0)
    (v : ℂ) :
    ∀ x : ℝ, x ∉ neutralNF543OriginalCollars → (L + v • R) x = 0 := by
  intro x hx
  have hLx : L x = 0 := hL x (by
    intro h
    exact hx (LC_mem_old x h))
  have hRx : R x = 0 := hR x (by
    intro h
    exact hx (RC_mem_old x h))
  simp [hLx, hRx]

/-- Actual NF600 correlation, not a generic formal bilinear surrogate. -/
theorem neutralCPC1H_positiveShift_integral
    (L R : 𝓢(ℝ, ℂ))
    (hL : ∀ x : ℝ, x ∉ LC → L x = 0)
    (hR : ∀ x : ℝ, x ∉ RC → R x = 0)
    (v : ℂ) :
    neutralWindowCorrelation (11/10:ℝ)
      ((L + v • R).toLp 2 volume) ((L + v • R).toLp 2 volume)
      (Real.log 9) =
      v * ∫ x : ℝ, R x * conj (L (x - Real.log 9)) := by
  rw [neutralNF600Correlation_eq (L + v • R) (pair_supported L R hL hR v)]
  calc
    (∫ x : ℝ, (L + v • R) x * conj ((L + v • R) (x - Real.log 9))) =
        ∫ x : ℝ, v * (R x * conj (L (x - Real.log 9))) := by
          apply integral_congr_ae
          filter_upwards [] with x
          simpa [smul_eq_mul] using
            (neutralCPC1H_positiveShift_pointwise L R hL hR v x)
    _ = v * ∫ x : ℝ, R x * conj (L (x - Real.log 9)) := by
      rw [integral_const_mul]

/-- Genuine reversed correlation, including the conjugated phase. -/
theorem neutralCPC1H_negativeShift_integral
    (L R : 𝓢(ℝ, ℂ))
    (hL : ∀ x : ℝ, x ∉ LC → L x = 0)
    (hR : ∀ x : ℝ, x ∉ RC → R x = 0)
    (v : ℂ) :
    neutralWindowCorrelation (11/10:ℝ)
      ((L + v • R).toLp 2 volume) ((L + v • R).toLp 2 volume)
      (-Real.log 9) =
      conj v * ∫ x : ℝ, L x * conj (R (x + Real.log 9)) := by
  rw [neutralNF600Correlation_eq (L + v • R) (pair_supported L R hL hR v)]
  calc
    (∫ x : ℝ, (L + v • R) x * conj ((L + v • R) (x - -Real.log 9))) =
        ∫ x : ℝ, conj v * (L x * conj (R (x + Real.log 9))) := by
          apply integral_congr_ae
          filter_upwards [] with x
          simpa [smul_eq_mul, sub_neg_eq_add] using
            (neutralCPC1H_negativeShift_pointwise L R hL hR v x)
    _ = conj v * ∫ x : ℝ, L x * conj (R (x + Real.log 9)) := by
      rw [integral_const_mul]

/-- Exact ORIGINAL outer CP001 functions, not a translated replacement. -/
def neutralCPC1HLeft : 𝓢(ℝ, ℂ) :=
  neutralCPC1EFlatSchwartz (-1099/1000) (1/2000) (by norm_num)

def neutralCPC1HRight : 𝓢(ℝ, ℂ) :=
  neutralCPC1EFlatSchwartz (1099/1000) (1/2000) (by norm_num)

def neutralCPC1HPhase (v : ℂ) : 𝓢(ℝ, ℂ) :=
  neutralCPC1HLeft + v • neutralCPC1HRight

/-- Frozen flat bump interval [-1099/1000-1/2000,-1099/1000+1/2000]
really lies STRICTLY inside the historical open left collar. -/
theorem neutralCPC1HLeft_supportedLC :
    ∀ x : ℝ, x ∉ LC → neutralCPC1HLeft x = 0 := by
  intro x hx
  apply neutralCPC1EFlatSchwartz_zero_outside
    (-1099/1000) (1/2000) (by norm_num) x
  intro h
  apply hx
  change x ∈ Ioo (-11/10) (-11/10 + 1/500)
  exact ⟨by linarith [h.1], by linarith [h.2]⟩

theorem neutralCPC1HRight_supportedRC :
    ∀ x : ℝ, x ∉ RC → neutralCPC1HRight x = 0 := by
  intro x hx
  apply neutralCPC1EFlatSchwartz_zero_outside
    (1099/1000) (1/2000) (by norm_num) x
  intro h
  apply hx
  change x ∈ Ioo (11/10 - 1/500) (11/10)
  exact ⟨by linarith [h.1], by linarith [h.2]⟩

/-- The actual CP001 flat Schwartz values are real, not complex phases.
No reflection-symmetry or log approximation is used. -/
theorem neutralCPC1HLeft_real (x : ℝ) :
    conj (neutralCPC1HLeft x) = neutralCPC1HLeft x := by
  change conj ((neutralCPC1EFlatReal (-1099/1000) (1/2000) x : ℂ)) =
    (neutralCPC1EFlatReal (-1099/1000) (1/2000) x : ℂ)
  simp

theorem neutralCPC1HRight_real (x : ℝ) :
    conj (neutralCPC1HRight x) = neutralCPC1HRight x := by
  change conj ((neutralCPC1EFlatReal (1099/1000) (1/2000) x : ℂ)) =
    (neutralCPC1EFlatReal (1099/1000) (1/2000) x : ℂ)
  simp

/-- TRUE real CP001 n=9 overlap, not a postulated scalar. -/
def neutralCPC1HOverlapReal : ℝ :=
  ∫ x : ℝ,
    neutralCPC1EFlatReal (-1099/1000) (1/2000) x *
      neutralCPC1EFlatReal (1099/1000) (1/2000) (x + Real.log 9)

/-- Lebesgue translation invariance: the physically right-to-left
correlation equals the left-to-right overlap after x ↦ x+log9. -/
theorem neutralCPC1H_overlap_shift :
    (∫ x : ℝ, neutralCPC1HRight x *
        conj (neutralCPC1HLeft (x - Real.log 9))) =
      ∫ x : ℝ, neutralCPC1HLeft x *
        conj (neutralCPC1HRight (x + Real.log 9)) := by
  calc
    (∫ x : ℝ, neutralCPC1HRight x *
      conj (neutralCPC1HLeft (x - Real.log 9))) =
      ∫ x : ℝ, neutralCPC1HRight (x + Real.log 9) *
        conj (neutralCPC1HLeft x) := by
          simpa only [sub_add_cancel] using
            (integral_sub_right_eq_self
              (f := fun y : ℝ => neutralCPC1HRight (y + Real.log 9) *
                conj (neutralCPC1HLeft y)))
    _ = ∫ x : ℝ, neutralCPC1HLeft x *
        conj (neutralCPC1HRight (x + Real.log 9)) := by
          apply integral_congr_ae
          filter_upwards [] with x
          rw [neutralCPC1HLeft_real x,
            neutralCPC1HRight_real (x + Real.log 9)]
          exact mul_comm _ _

/-- Exact conversion of the complex physical overlap to the frozen
real integral; relies on standard Mathlib `integral_ofReal`. -/
theorem neutralCPC1H_overlap_as_real :
    (∫ x : ℝ, neutralCPC1HLeft x *
        conj (neutralCPC1HRight (x + Real.log 9))) =
      (neutralCPC1HOverlapReal : ℂ) := by
  calc
    (∫ x : ℝ, neutralCPC1HLeft x *
      conj (neutralCPC1HRight (x + Real.log 9))) =
      ∫ x : ℝ, ((neutralCPC1EFlatReal (-1099/1000) (1/2000) x *
        neutralCPC1EFlatReal (1099/1000) (1/2000)
          (x + Real.log 9) : ℝ) : ℂ) := by
          apply integral_congr_ae
          filter_upwards [] with x
          simp [neutralCPC1HLeft, neutralCPC1HRight,
            neutralCPC1EFlatSchwartz_apply, neutralCPC1EFlatComplex,
            Complex.ofReal_mul, Complex.conj_ofReal]
    _ = (neutralCPC1HOverlapReal : ℂ) := by
      simpa only [neutralCPC1HOverlapReal] using
        (integral_ofReal (f := fun x : ℝ =>
          neutralCPC1EFlatReal (-1099/1000) (1/2000) x *
          neutralCPC1EFlatReal (1099/1000) (1/2000)
            (x + Real.log 9)))

/-- BOTH formerly assumed CP-C1(G) physical cross-correlation readings,
now directly identified with the literal frozen real overlap. -/
theorem neutralCPC1H_plus_correlation (v : ℂ) :
    neutralWindowCorrelation (11/10:ℝ)
      ((neutralCPC1HPhase v).toLp 2 volume)
      ((neutralCPC1HPhase v).toLp 2 volume) (Real.log 9) =
        v * (neutralCPC1HOverlapReal : ℂ) := by
  change neutralWindowCorrelation (11/10:ℝ)
    ((neutralCPC1HLeft + v • neutralCPC1HRight).toLp 2 volume)
    ((neutralCPC1HLeft + v • neutralCPC1HRight).toLp 2 volume) (Real.log 9) = _
  rw [neutralCPC1H_positiveShift_integral _ _
    neutralCPC1HLeft_supportedLC neutralCPC1HRight_supportedRC v,
    neutralCPC1H_overlap_shift, neutralCPC1H_overlap_as_real]

/-- The negative-shift reading carries conj(v), not v. -/
theorem neutralCPC1H_minus_correlation (v : ℂ) :
    neutralWindowCorrelation (11/10:ℝ)
      ((neutralCPC1HPhase v).toLp 2 volume)
      ((neutralCPC1HPhase v).toLp 2 volume) (-Real.log 9) =
        conj v * (neutralCPC1HOverlapReal : ℂ) := by
  change neutralWindowCorrelation (11/10:ℝ)
    ((neutralCPC1HLeft + v • neutralCPC1HRight).toLp 2 volume)
    ((neutralCPC1HLeft + v • neutralCPC1HRight).toLp 2 volume) (-Real.log 9) = _
  rw [neutralCPC1H_negativeShift_integral _ _
    neutralCPC1HLeft_supportedLC neutralCPC1HRight_supportedRC v,
    neutralCPC1H_overlap_as_real]

/-- The complete original NF600 prime sum becomes a genuine physical
phase law without any `hplus` or `hminus` PREMISES. Source candidate. -/
theorem neutralCPC1H_prime_phase_unconditional (v : ℂ) :
    (neutralNF600Prime (neutralCPC1HPhase v)).re =
      2 * (ArithmeticFunction.vonMangoldt 9 / Real.sqrt 9) *
        neutralCPC1HOverlapReal * v.re := by
  have hs := pair_supported neutralCPC1HLeft neutralCPC1HRight
    neutralCPC1HLeft_supportedLC neutralCPC1HRight_supportedRC v
  rw [neutralNF600Prime_single (neutralCPC1HPhase v) hs,
    neutralCPC1H_plus_correlation v,
    neutralCPC1H_minus_correlation v]
  simp only [Complex.add_re, Complex.mul_re,
    Complex.ofReal_re, Complex.ofReal_im,
    Complex.conj_re, Complex.conj_im,
    mul_zero, sub_zero]
  ring

/-- The SIGNED PRIME SECTOR is the negative of the original NF600
positive von Mangoldt series. Gamma and poles are still part of full W. -/
theorem neutralCPC1H_signed_prime_phase_unconditional (v : ℂ) :
    (-neutralNF600Prime (neutralCPC1HPhase v)).re =
      -2 * (ArithmeticFunction.vonMangoldt 9 / Real.sqrt 9) *
        neutralCPC1HOverlapReal * v.re := by
  rw [Complex.neg_re, neutralCPC1H_prime_phase_unconditional]
  ring


#print axioms neutralNF600Correlation_eq
#print axioms neutralNF600Prime_single
#print axioms neutralCPC1H_positiveShift_pointwise
#print axioms neutralCPC1H_negativeShift_pointwise
#print axioms neutralCPC1H_positiveShift_integral
#print axioms neutralCPC1H_negativeShift_integral
#print axioms neutralCPC1HLeft_supportedLC
#print axioms neutralCPC1HRight_supportedRC
#print axioms neutralCPC1HLeft_real
#print axioms neutralCPC1HRight_real
#print axioms neutralCPC1H_overlap_shift
#print axioms neutralCPC1H_overlap_as_real
#print axioms neutralCPC1H_plus_correlation
#print axioms neutralCPC1H_minus_correlation
#print axioms neutralCPC1H_prime_phase_unconditional
#print axioms neutralCPC1H_signed_prime_phase_unconditional

end
end WeilDefect
