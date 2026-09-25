import WeilDefect.Filtration.CriticalDichotomy
import WeilDefect.Screening.DefectIndex
import WeilDefect.Arithmetic.PrimeSupport
import WeilDefect.Arithmetic.NoSobolevBootstrap

namespace WeilDefect

open Filter MeasureTheory
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


/-- Prime powers present in the strict right-limit compact-window operator. -/
def rightLimitPrimePowers (c : ℝ) : Set ℕ :=
  {n | IsPrimePow n ∧ Real.log (n : ℝ) ≤ 2 * c}

/--
The right-limit prime set is exactly the endpoint strict-active set plus the
equality-threshold correction.
-/
theorem wd_t38_p3_u3_right_limit_prime_decomposition
    (c : ℝ) :
    rightLimitPrimePowers c =
      activePrimePowers c ∪ primePowerThreshold c := by
  ext n
  simp only [rightLimitPrimePowers, activePrimePowers,
    primePowerThreshold, Set.mem_setOf_eq, Set.mem_union]
  constructor
  · rintro ⟨hn, hle⟩
    rcases lt_or_eq_of_le hle with hlt | heq
    · exact Or.inl ⟨hn, hlt⟩
    · exact Or.inr ⟨hn, heq⟩
  · rintro (hactive | hthreshold)
    · exact ⟨hactive.1, le_of_lt hactive.2⟩
    · exact ⟨hthreshold.1, le_of_eq hthreshold.2⟩

/--
P3-U3 threshold-aware finiteness: the strict right-limit arithmetic support
is finite.  Relative to the endpoint strict-< support, the only additional
indices lie in the equality-threshold set, which contains at most one natural
prime power.
-/
theorem wd_t38_p3_u3_right_limit_prime_support_finite
    (c : ℝ) :
    (rightLimitPrimePowers c).Finite
      ∧ (primePowerThreshold c).Subsingleton := by
  constructor
  · rw [wd_t38_p3_u3_right_limit_prime_decomposition]
    exact
      (wd_t34_active_prime_powers_finite c).union
        (primePowerThreshold_subsingleton c).finite
  · exact primePowerThreshold_subsingleton c



/--
P3-U4 / WD-T38: once the physical neutral carrier is identified with the
compact-window Weil form, its shifted quadratic form has logarithmic Fourier
order.  The imported compact-window formula/symbol comparison remain explicit
premises exactly as in WD-T35.
-/
theorem wd_t38_p3_u4_logarithmic_order_neutral_carrier
    (Q : ℝ)
    (symbol density : ℝ → ℝ)
    (shift pole a b K : ℝ)
    (hdensity : ∀ t, 0 ≤ density t)
    (ha : 0 ≤ a)
    (hK : 0 ≤ K)
    (hlower :
      ∀ t,
        a * logarithmicFourierWeight t
          ≤ symbol t + shift)
    (hupper :
      ∀ t,
        symbol t + shift
          ≤ b * logarithmicFourierWeight t)
    (hpole0 : 0 ≤ pole)
    (hpole :
      pole ≤ K * spectralMass density)
    (hdensity_int : Integrable density volume)
    (hlog_int :
      Integrable
        (fun t : ℝ =>
          logarithmicFourierWeight t * density t) volume)
    (hsymbol_int :
      Integrable
        (fun t : ℝ =>
          (symbol t + shift) * density t) volume)
    (hQ :
      Q + shift * spectralMass density
        =
      shiftedCompactWeilForm symbol density shift pole) :
    a * logarithmicFourierEnergy density
      ≤ Q + shift * spectralMass density
      ∧
    Q + shift * spectralMass density
      ≤ (b + K) * logarithmicFourierEnergy density := by
  exact wd_t35_compact_weil_logarithmic_form_order
    Q symbol density shift pole a b K
    hdensity ha hK hlower hupper hpole0 hpole
    hdensity_int hlog_int hsymbol_int hQ

/--
P3-U6 scope guard in its purely logical form: vanishing of a total
cancellation does not imply vanishing of the individual summands.

This theorem intentionally says nothing stronger about the prime, pole, or
archimedean pieces of a particular Weil-form realization.
-/
theorem wd_t38_p3_u6_global_cancellation_not_termwise :
    ¬ (∀ x y : ℝ, x + y = 0 → x = 0 ∧ y = 0) := by
  intro h
  have hbad := h 1 (-1) (by norm_num)
  norm_num at hbad

/--
P3-U5 / WD-T38: logarithmic form control alone does not uniformly dominate
any positive-Sobolev frequency weight.
-/
theorem wd_t38_p3_u5_no_free_positive_sobolev_control
    {eps : ℝ} (heps : 0 < eps) :
    ¬ (fun x : ℝ => positiveSobolevFrequencyWeight eps x)
        =O[atTop] logarithmicFourierWeight :=
  wd_t36_no_positive_sobolev_bootstrap heps

/--
P3-U5 with the fixed finite prime correction retained: finite arithmetic
translations do not repair the positive-order mismatch.
-/
theorem wd_t38_p3_u5_finite_prime_translations_no_smoothing
    {eps : ℝ} (heps : 0 < eps)
    (c : ℝ) (coeff : ℕ → ℝ) :
    ¬ (fun x : ℝ => positiveSobolevFrequencyWeight eps x)
        =O[atTop]
      (fun t : ℝ =>
        logarithmicFourierWeight t
          + finitePrimeTrigCorrection c coeff t) :=
  wd_t36_finite_prime_translations_add_no_smoothing
    heps c coeff

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
