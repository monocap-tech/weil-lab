module

public import Zeta.Zeros.HardyZ
public import Zeta.EulerMaclaurin.Continuation
public import Zeta.EulerMaclaurin.ErrorBound
public import Mathlib.Topology.Order.IntermediateValue

/-!
CP026 — original Zeta-v4.35 finite-Euler–Maclaurin → signed-HardyZ
error bridge and open narrow critical-line zero transport.

Only the genuinely published original Zeta/Mathlib proof modules
are imported.  The finite original 255+6 term numerical evaluations
are NOT asserted.  The exact two original zetaRemainderBound caps and
the two finite-point strict numerical inequalities are EXPLICIT
UNPROVED hypotheses; they must be paid by genuine source-bound
rational/interval certificates, never by a 'native_decide' of JSON.

The original published source gives:
  riemannZeta_eq_approximant_add_remainder,
  norm_zetaRemainder_le,
  abs_riemannSiegelTheta_sub_approximant_two_le,
  abs_hardyZ_sub_re_le',
  continuousOn_hardyZ,
  hardyZ_eq_zero_iff_riemannZeta.
Mathlib's genuine intermediate_value_Ioo places the zero in the
OPEN narrow interval.  Neither curvature nor source ordinal #53
is assumed or concluded.

All new theorems are SOURCE PROOF CANDIDATES until an actual
frozen original Lean4.35 compilation and strict #print axioms.
No new axiom, sorry, unsafe, classical oracle, or external JSON fact.
-/

@[expose] public section

namespace CP026OriginalPointBridge

abbrev tLeft : ℝ := (15005352 : ℝ) / 100000
abbrev tRight : ℝ := (15005353 : ℝ) / 100000

noncomputable def sourcePoint (t : ℝ) : ℂ :=
  1 / 2 + Complex.I * (t : ℂ)
noncomputable def sourceA (t : ℝ) : ℂ :=
  zetaApproximant (sourcePoint t) 6 256
noncomputable def sourceThetaApprox (t : ℝ) : ℝ :=
  riemannSiegelThetaApproximant 2 0 t
noncomputable def sourceFiniteZ (t : ℝ) : ℝ :=
  (Complex.exp (Complex.I * (sourceThetaApprox t : ℂ)) * sourceA t).re
noncomputable def sourcePointError (t : ℝ) : ℝ :=
  (12 : ℝ) / t ^ 4 * ‖sourceA t‖ + 3 / (10 : ℝ) ^ 13

private theorem sourcePoint_re (t : ℝ) :
    (sourcePoint t).re = 1 / 2 := by
  simp [sourcePoint]

private theorem sourcePoint_ne_one (t : ℝ) : sourcePoint t ≠ 1 := by
  intro h
  have hr := congrArg Complex.re h
  rw [sourcePoint_re] at hr
  norm_num at hr

/-- The actual ORIGINAL published zeta Euler–Maclaurin error bound,
with its ONLY unpaid input being the explicit pointwise Borwein
inequality on the original source function.  This theorem does not
pretend that the Python 10^55 interval receipt is a Lean hypothesis
discharge. -/
theorem original_hardy_error_from_source_Borwein
    (t : ℝ) (ht : 0 < t)
    (hR : zetaRemainderBound (sourcePoint t) 6 256
      ≤ (3 : ℝ) / (10 : ℝ) ^ 13) :
    |Zeta.hardyZ t - sourceFiniteZ t| ≤ sourcePointError t := by
  have hs : -(2 * (6 : ℕ) + 1 : ℝ) < (sourcePoint t).re := by
    rw [sourcePoint_re]
    norm_num
  have hζ := riemannZeta_eq_approximant_add_remainder
    (sourcePoint t) 6 256 (by norm_num) hs (sourcePoint_ne_one t)
  have hRem := norm_zetaRemainder_le
    (sourcePoint t) 6 256 (by norm_num) hs
  have hzeta : ‖riemannZeta (sourcePoint t) - sourceA t‖
      ≤ (3 : ℝ) / (10 : ℝ) ^ 13 := by
    calc
      ‖riemannZeta (sourcePoint t) - sourceA t‖
          = ‖zetaRemainder (sourcePoint t) 6 256‖ := by
              rw [hζ]
              simp [sourceA]
      _ ≤ zetaRemainderBound (sourcePoint t) 6 256 := hRem
      _ ≤ (3 : ℝ) / (10 : ℝ) ^ 13 := hR
  have htheta := abs_riemannSiegelTheta_sub_approximant_two_le ht
  have hpublished := abs_hardyZ_sub_re_le' t
    (sourceThetaApprox t) (sourceA t)
  change |Zeta.hardyZ t - sourceFiniteZ t|
      ≤ |riemannSiegelTheta t - sourceThetaApprox t| * ‖sourceA t‖
          + ‖riemannZeta (sourcePoint t) - sourceA t‖ at hpublished
  calc
    |Zeta.hardyZ t - sourceFiniteZ t|
        ≤ |riemannSiegelTheta t - sourceThetaApprox t| * ‖sourceA t‖
          + ‖riemannZeta (sourcePoint t) - sourceA t‖ := hpublished
    _ ≤ (12 : ℝ) / t ^ 4 * ‖sourceA t‖ + (3 : ℝ) / (10 : ℝ) ^ 13 := by
          exact add_le_add
            (mul_le_mul_of_nonneg_right htheta (norm_nonneg _)) hzeta
    _ = sourcePointError t := rfl

/-- A STRICT sign is transported only if a corresponding certified
finite-source complex bound and source original pointwise remainder
bound are supplied.  No numerical value is imported from CP025 JSON. -/
theorem original_negative_of_finite_certificate (t : ℝ) (ht : 0 < t)
    (hR : zetaRemainderBound (sourcePoint t) 6 256
      ≤ (3 : ℝ) / (10 : ℝ) ^ 13)
    (hfinite : sourceFiniteZ t + sourcePointError t < 0) :
    Zeta.hardyZ t < 0 := by
  have hbound := (abs_le.mp (original_hardy_error_from_source_Borwein t ht hR)).2
  linarith

/-- Positive signed original HardyZ from one STRICT
finite-source rational interval witness. -/
theorem original_positive_of_finite_certificate (t : ℝ) (ht : 0 < t)
    (hR : zetaRemainderBound (sourcePoint t) 6 256
      ≤ (3 : ℝ) / (10 : ℝ) ^ 13)
    (hfinite : 0 < sourceFiniteZ t - sourcePointError t) :
    0 < Zeta.hardyZ t := by
  have hbound := (abs_le.mp (original_hardy_error_from_source_Borwein t ht hR)).1
  linarith

/-- Genuine *original* critical-line ζ zero existence from exactly
the two source pointwise Borwein bounds and two actual finite
Euler–Maclaurin strict signs. Unlike CP017, NO whole-interval
curvature/monotonicity/uniqueness assumption is needed; unlike
CP016, NO ordinal-53 source ranking is asserted.

This theorem is conditional until those FOUR proof inputs are
genuinely discharged by the original v4.35 kernel. -/
theorem original_critical_line_zero_in_narrow_bracket
    (hRLeft : zetaRemainderBound (sourcePoint tLeft) 6 256
        ≤ (3 : ℝ) / (10 : ℝ) ^ 13)
    (hRRight : zetaRemainderBound (sourcePoint tRight) 6 256
        ≤ (3 : ℝ) / (10 : ℝ) ^ 13)
    (hFiniteLeft : sourceFiniteZ tLeft + sourcePointError tLeft < 0)
    (hFiniteRight : 0 < sourceFiniteZ tRight - sourcePointError tRight) :
    ∃ t : ℝ, tLeft < t ∧ t < tRight ∧
      riemannZeta (1 / 2 + Complex.I * (t : ℂ)) = 0 := by
  have hposLeft : (0 : ℝ) < tLeft := by norm_num [tLeft]
  have hposRight : (0 : ℝ) < tRight := by norm_num [tRight]
  have hlt : tLeft ≤ tRight := by norm_num [tLeft, tRight]
  have hleft : Zeta.hardyZ tLeft < 0 :=
    original_negative_of_finite_certificate tLeft hposLeft hRLeft hFiniteLeft
  have hright : 0 < Zeta.hardyZ tRight :=
    original_positive_of_finite_certificate tRight hposRight hRRight hFiniteRight
  have hsubset : Set.Icc tLeft tRight ⊆ Set.Ici (0 : ℝ) := by
    intro x hx
    exact hposLeft.le.trans hx.1
  have hcont : ContinuousOn Zeta.hardyZ (Set.Icc tLeft tRight) :=
    continuousOn_hardyZ.mono hsubset
  have himage : (0 : ℝ) ∈ Zeta.hardyZ '' Set.Ioo tLeft tRight :=
    (intermediate_value_Ioo hlt hcont) ⟨hleft, hright⟩
  obtain ⟨t, ht, hzero⟩ := Set.mem_image.mp himage
  have ht0 : (0 : ℝ) ≤ t := hposLeft.le.trans ht.1.le
  exact ⟨t, ht.1, ht.2, (hardyZ_eq_zero_iff_riemannZeta ht0).mp hzero⟩

end CP026OriginalPointBridge

#print axioms CP026OriginalPointBridge.original_hardy_error_from_source_Borwein
#print axioms CP026OriginalPointBridge.original_negative_of_finite_certificate
#print axioms CP026OriginalPointBridge.original_positive_of_finite_certificate
#print axioms CP026OriginalPointBridge.original_critical_line_zero_in_narrow_bracket
