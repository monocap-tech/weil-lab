import WeilDefect.Filtration.CriticalDichotomy
import WeilDefect.Screening.DefectIndex

namespace WeilDefect

open Filter
open scoped Topology InnerProduct

/--
P3-U1 / WD-T38 neutral-branch entry point.

This is the composite-facing form of WD-T17: along the fixed finite-sector
compactness subsequence, critical right-approach has exactly two mutually
exclusive outcomes, attained neutral or strict negative fall-through.
-/
theorem wd_t38_p3_u1_fixed_packet_critical_dichotomy
    {Kpos M : Type*}
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    [FiniteDimensional ℂ M]
    (A : ℝ → ClosedSubmodule ℂ (WeilDefect.WDT16.CoeffSpace Kpos M))
    (c : ℝ) (t : ℕ → ℝ)
    (hA : Monotone A)
    (ht : Tendsto t atTop (𝓝 c))
    (a : ℕ → Kpos) (u : ℕ → M)
    (hmem :
      ∀ n,
        WeilDefect.WDT16.coeff (a n) (u n) ∈ A (t n))
    (hnorm :
      ∀ n,
        ‖WeilDefect.WDT16.coeff (a n) (u n)‖ = 1)
    (hq :
      Tendsto
        (fun n => WeilDefect.WDT16.jValue (a n) (u n))
        atTop (𝓝 0)) :
    ∃ φ : ℕ → ℕ, StrictMono φ ∧
      ∃ aLim : Kpos, ∃ uLim : M,
        WeilDefect.WDT16.WeaklyTendsto (fun n => a (φ n)) aLim
        ∧ Tendsto (fun n => u (φ n)) atTop (𝓝 uLim)
        ∧ WeilDefect.WDT16.coeff aLim uLim ∈
            WeilDefect.WDT15.rightLimit A c
        ∧ WeilDefect.WDT16.coeff aLim uLim ≠ 0
        ∧
          (WeilDefect.WDT17.NeutralCriticalBranch
              a u φ aLim uLim
            ∨
           WeilDefect.WDT17.NegativeFallthroughBranch
              aLim uLim)
        ∧ ¬
          (WeilDefect.WDT17.NeutralCriticalBranch
              a u φ aLim uLim
            ∧
           WeilDefect.WDT17.NegativeFallthroughBranch
              aLim uLim) := by
  exact WeilDefect.WDT17.wd_t17_fixed_sector_critical_dichotomy
    A c t hA ht a u hmem hnorm hq

/--
Negative synthesis attached to a finite-exception neutral compensator:
N_c = -P_c C_c.
-/
noncomputable def neutralNegativeSynthesis
    {H Kpos M : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    (P : Kpos →L[ℂ] H)
    (C : M →L[ℂ] Kpos) :
    M →L[ℂ] H :=
  -(P ∘L C)

/-- Physical finite-exception Weil defect used in the neutral branch. -/
noncomputable def neutralWeilOperator
    {H Kpos M : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    (P : Kpos →L[ℂ] H)
    (C : M →L[ℂ] Kpos) :
    H →L[ℂ] H :=
  WeilDefect.WDT01.physicalDefect P (neutralNegativeSynthesis P C)

/--
The unit-gain plus physical-adjoint realization forces the negative adjoint
coefficient to be exactly -u.
-/
theorem wd_t38_p3_u2_negative_adjoint_identity
    {H Kpos M : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    (P : Kpos →L[ℂ] H)
    (C : M →L[ℂ] Kpos)
    (u : M) (k : H)
    (hunit : (C†) (C u) = u)
    (hreal : C u = (P†) k) :
    (neutralNegativeSynthesis P C)† k = -u := by
  simp [neutralNegativeSynthesis,
    ContinuousLinearMap.adjoint_comp, ← hreal, hunit]

/--
P3-U2 / WD-T38 physical neutral null-mode theorem.

Under the finite-exception unit-gain relation C† C u = u and the physical
adjoint realization C u = P† k, with N = -PC, the physical Weil defect
P P† - N N† annihilates the same nonzero physical vector k.
-/
theorem wd_t38_p3_u2_physical_neutral_null_mode
    {H Kpos M : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    (P : Kpos →L[ℂ] H)
    (C : M →L[ℂ] Kpos)
    (u : M) (k : H)
    (hunit : (C†) (C u) = u)
    (hreal : C u = (P†) k)
    (hk : k ≠ 0) :
    k ≠ 0 ∧ neutralWeilOperator P C k = 0 := by
  constructor
  · exact hk
  · have hneg :
        (neutralNegativeSynthesis P C)† k = -u :=
      wd_t38_p3_u2_negative_adjoint_identity
        P C u k hunit hreal
    unfold neutralWeilOperator WeilDefect.WDT01.physicalDefect
    simp only [ContinuousLinearMap.sub_apply,
      ContinuousLinearMap.comp_apply]
    rw [hneg]
    simp [neutralNegativeSynthesis, ← hreal]

end WeilDefect
