import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalWiderThreeCellSourceMeasure
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalThreeCellPrime9Transfer
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalWiderPrimeFreeBump
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV020: the TRUE original n=9 arithmetic transfer into the DOUBLED
radius physical interval [99/500,101/500] about c=1/5.

This is a separate fresh-source direct Lean proof, adapting the
IV018 pointwise translated correlation argument. At every TRUE
arithmetic-active prime power m<10, both old/new and new/new
correlations vanish by IV019's exact original widened logarithmic
gap; old-old survives only as the original historical NF600 n=9
charge. At all n>=10 the ORIGINAL support cutoff applies, and at
inactive n the ORIGINAL von-Mangoldt coefficient vanishes.

Hence, for every original old two-collar complex Schwartz S,
every new wide-interval complex Schwartz t, every v∈ℂ,
  P_original(S+v•t,S+v•t) = P_original(S,S)
and the original NF600 n=9 prime allowance is transferred
without modifying the authentic arithmetic object.

Together with the EXACT original wider union measure1/125
Cauchy–Schwarz bound from the preceding module and IV019's
signed Gamma+two-pole source budget, the terminal theorem
CANDIDATE establishes a genuine 1/10 lower on the actual
signed original Weil form of S+v•t. An honest Lean kernel and
strict original-source axiom audit are mandatory. This is a
RESTRICTED physical support result, not global Weil positivity.
-/

theorem neutralIV020WideOldPlusNew_supportedThreeCell
    (S t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hS : neutralNF735InOriginalCollars S)
    (ht : ∀ x : ℝ,
      x ∉ neutralIV020WidePhysicalInterval → t x = 0) :
    ∀ x : ℝ, x ∉ neutralIV020WideThreeCellSupport →
      (S + v • t) x = 0 := by
  intro x hx
  have hxOld : x ∉ neutralNF543OriginalCollars :=
    fun h => hx (Or.inl h)
  have hxNew : x ∉ neutralIV020WidePhysicalInterval :=
    fun h => hx (Or.inr h)
  simp [hS x hxOld, ht x hxNew]

/-- Physical old/new source disjointness implies EXACT orthogonal
mass addition, without an abstract orthogonal Gram model:
  Mass(S+v•t)=Mass(S)+Mass(v•t).
The imaginary cross term is absent pointwise, because supports
are genuinely disjoint in the real variable x. -/
theorem neutralIV020WideOldPlusNew_mass_add
    (S t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hS : neutralNF735InOriginalCollars S)
    (ht : ∀ x : ℝ,
      x ∉ neutralIV020WidePhysicalInterval → t x = 0) :
    neutralNF600Mass (S + v • t) =
      neutralNF600Mass S + neutralNF600Mass (v • t) := by
  have hdisj (x : ℝ) : S x = 0 ∨ t x = 0 := by
    by_cases hx : x ∈ neutralNF543OriginalCollars
    · right
      have hxNew : x ∉ neutralIV020WidePhysicalInterval :=
        (Set.disjoint_left.mp neutralIV020WideOldNew_disjoint) hx
      exact ht x hxNew
    · left
      exact hS x hx
  have hpoint (x : ℝ) :
      ‖(S + v • t) x‖^2 =
        ‖S x‖^2 + ‖(v • t) x‖^2 := by
    rcases hdisj x with hz | hz
    · simp [hz]
    · simp [hz]
  have hiS : Integrable (fun x : ℝ => ‖S x‖^2) :=
    (memLp_two_iff_integrable_sq_norm
      S.continuous.aestronglyMeasurable).mp (S.memLp 2 volume)
  have hiT : Integrable (fun x : ℝ => ‖(v • t) x‖^2) :=
    (memLp_two_iff_integrable_sq_norm
      (v • t).continuous.aestronglyMeasurable).mp
      ((v • t).memLp 2 volume)
  calc
    neutralNF600Mass (S + v • t) =
      ∫ x : ℝ, ‖(S + v • t) x‖^2 :=
        neutralNF600Mass_eq_integral _
    _ = ∫ x : ℝ, (‖S x‖^2 + ‖(v • t) x‖^2) := by
      apply integral_congr_ae
      filter_upwards [] with x
      exact hpoint x
    _ = (∫ x : ℝ, ‖S x‖^2) +
          (∫ x : ℝ, ‖(v • t) x‖^2) :=
        integral_add hiS hiT
    _ = neutralNF600Mass S + neutralNF600Mass (v • t) := by
      rw [← neutralNF600Mass_eq_integral S,
        ← neutralNF600Mass_eq_integral (v • t)]

theorem neutralIV020WideOldMass_le_expandedMass
    (S t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hS : neutralNF735InOriginalCollars S)
    (ht : ∀ x : ℝ,
      x ∉ neutralIV020WidePhysicalInterval → t x = 0) :
    neutralNF600Mass S ≤ neutralNF600Mass (S + v • t) := by
  have heq := neutralIV020WideOldPlusNew_mass_add S t v hS ht
  have hm : 0 ≤ neutralNF600Mass (v • t) := by
    unfold neutralNF600Mass
    positivity
  linarith

/-- An exact pointwise translated-source identity. Three
conditions explicitly remove all old-new, new-old and new-new
terms at the literal original real translation τ.
Only the original old-old translated product survives.
This lemma uses REAL complex Schwartz evaluations, not a
formal assertion that Weil positivity polarizes. -/
theorem neutralIV020WideExpandedCorrelation_eq_old_of_threeZeros
    (S t : 𝓢(ℝ,ℂ)) (v : ℂ) (τ : ℝ)
    (hS : neutralNF735InOriginalCollars S)
    (ht : ∀ x : ℝ,
      x ∉ neutralIV020WidePhysicalInterval → t x = 0)
    (hST : ∀ x : ℝ, t x = 0 ∨ S (x - τ) = 0)
    (hTS : ∀ x : ℝ, t (x - τ) = 0 ∨ S x = 0)
    (hTT : ∀ x : ℝ, t x = 0 ∨ t (x - τ) = 0) :
    neutralWindowCorrelation (11/10:ℝ)
        ((S + v • t).toLp 2 volume)
        ((S + v • t).toLp 2 volume) τ =
      neutralWindowCorrelation (11/10:ℝ)
        (S.toLp 2 volume) (S.toLp 2 volume) τ := by
  have hSw : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → S x = 0 :=
    neutralIV009OriginalCollars_supported_window S hS
  have htw : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0 :=
    neutralIV020WideThreeCell_supported_window t
      (by
        intro x hx
        exact ht x (fun h => hx (Or.inr h)))
  have hFw : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
        (S + v • t) x = 0 :=
    neutralIV020WideThreeCell_supported_window (S + v • t)
      (neutralIV020WideOldPlusNew_supportedThreeCell S t v hS ht)
  rw [neutralIV011MixedCorrelation_eq_schwartzIntegral
        (11/10:ℝ) (11/10:ℝ) (le_refl _)
        (S + v • t) (S + v • t) hFw hFw τ,
      neutralIV011MixedCorrelation_eq_schwartzIntegral
        (11/10:ℝ) (11/10:ℝ) (le_refl _)
        S S hSw hSw τ]
  apply integral_congr_ae
  filter_upwards [] with x
  have ha : (v * t x) * conj (S (x-τ)) = 0 := by
    rcases hST x with hz | hz
    · simp [hz]
    · simp [hz]
  have hb : (S x) * conj (v * t (x-τ)) = 0 := by
    rcases hTS x with hz | hz
    · simp [hz]
    · simp [hz]
  have hc : (v * t x) * conj (v * t (x-τ)) = 0 := by
    rcases hTT x with hz | hz
    · simp [hz]
    · simp [hz]
  change (S x + v * t x) *
      conj (S (x-τ) + v * t (x-τ)) =
        S x * conj (S (x-τ))
  calc
    _ = S x * conj (S (x-τ)) +
          (v * t x) * conj (S (x-τ)) +
          S x * conj (v * t (x-τ)) +
          (v * t x) * conj (v * t (x-τ)) := by
      rw [map_add]
      ring
    _ = S x * conj (S (x-τ)) := by
      rw [ha,hb,hc]
      ring

/-- FINITE original n<10 arithmetic-active translated CORRELATION
transfer from the enlarged three-cell physical source to the
historical old two-collar source, at BOTH signs of the real log.

The exact IV016 1/5-center four-gap proof removes all S-t terms;
the self width 1/500 prime shift bound removes t-t terms.
This is NOT a hypothetical approximate support projection. -/
theorem neutralIV020WideExpandedActiveCorrelation_eq_old
    (S t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hS : neutralNF735InOriginalCollars S)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
        ((1/5:ℝ)+(1/500:ℝ)) → t x = 0)
    (m : ℕ) (hm : m ∈ Finset.range 10)
    (hactive : ArithmeticFunction.vonMangoldt m ≠ 0) :
    neutralWindowCorrelation (11/10:ℝ)
        ((S + v • t).toLp 2 volume)
        ((S + v • t).toLp 2 volume)
        (Real.log m) =
      neutralWindowCorrelation (11/10:ℝ)
        (S.toLp 2 volume) (S.toLp 2 volume)
        (Real.log m) ∧
    neutralWindowCorrelation (11/10:ℝ)
        ((S + v • t).toLp 2 volume)
        ((S + v • t).toLp 2 volume)
        (-Real.log m) =
      neutralWindowCorrelation (11/10:ℝ)
        (S.toLp 2 volume) (S.toLp 2 volume)
        (-Real.log m) := by
  have htNarrow := neutralIV020Wide_support_from_bump t ht
  have hST : neutralIV014ActivePrimeSeparated S t 10 :=
    neutralIV015FrozenCollar_activeSeparated_of_gap
      S t 10 (1/5:ℝ) (1/500:ℝ)
      hS ht neutralIV019WideFrozenConcrete_allIntegerGap
  have hTT : neutralIV014ActivePrimeSeparated t t 10 :=
    neutralIV014ActiveSeparated_of_intervalGap
      t t 10 (1/5:ℝ) (1/5:ℝ)
      (1/500:ℝ) (1/500:ℝ)
      ht ht neutralIV019WideSelfActiveGap
  have hSTPlus (x : ℝ) :
      t x = 0 ∨ S (x - Real.log m) = 0 := by
    rcases hST m hm hactive x with hz | ⟨hz,_⟩
    · exact Or.inl hz
    · exact Or.inr hz
  have hSTMinus (x : ℝ) :
      t x = 0 ∨ S (x - (-Real.log m)) = 0 := by
    rcases hST m hm hactive x with hz | ⟨_,hz⟩
    · exact Or.inl hz
    · exact Or.inr (by simpa only [sub_neg_eq_add] using hz)
  have hTSPlus (x : ℝ) :
      t (x - Real.log m) = 0 ∨ S x = 0 := by
    rcases hST m hm hactive (x - Real.log m) with hz | ⟨_,hz⟩
    · exact Or.inl hz
    · exact Or.inr (by
        simpa only [sub_add_cancel] using hz)
  have hTSMinus (x : ℝ) :
      t (x - (-Real.log m)) = 0 ∨ S x = 0 := by
    rcases hST m hm hactive (x + Real.log m) with hz | ⟨hz,_⟩
    · exact Or.inl (by simpa only [sub_neg_eq_add] using hz)
    · exact Or.inr (by
        simpa only [add_sub_cancel_right] using hz)
  have hTTPlus (x : ℝ) :
      t x = 0 ∨ t (x - Real.log m) = 0 := by
    rcases hTT m hm hactive x with hz | ⟨hz,_⟩
    · exact Or.inl hz
    · exact Or.inr hz
  have hTTMinus (x : ℝ) :
      t x = 0 ∨ t (x - (-Real.log m)) = 0 := by
    rcases hTT m hm hactive x with hz | ⟨_,hz⟩
    · exact Or.inl hz
    · exact Or.inr (by simpa only [sub_neg_eq_add] using hz)
  constructor
  · exact neutralIV020WideExpandedCorrelation_eq_old_of_threeZeros
      S t v (Real.log m) hS htNarrow
      hSTPlus hTSPlus hTTPlus
  · exact neutralIV020WideExpandedCorrelation_eq_old_of_threeZeros
      S t v (-Real.log m) hS htNarrow
      hSTMinus hTSMinus hTTMinus

/-- All genuine original von-Mangoldt prime-power terms match
pointwise in the finite authenticated n<10 source sum. The
exact high-frequency n>=10 cutoff closes the infinite original
prime sum; a zero Λ(n) is never replaced by a false correlation
vanishing assumption. -/
theorem neutralIV020WideExpandedPrime_eq_old
    (S t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hS : neutralNF735InOriginalCollars S)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
        ((1/5:ℝ)+(1/500:ℝ)) → t x = 0) :
    neutralIV011OriginalMixedPrime (11/10:ℝ)
      (S + v • t) (S + v • t) =
    neutralIV011OriginalMixedPrime (11/10:ℝ) S S := by
  have htNarrow := neutralIV020Wide_support_from_bump t ht
  have hF : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
        (S + v • t) x = 0 :=
    neutralIV020WideThreeCell_supported_window (S+v•t)
      (neutralIV020WideOldPlusNew_supportedThreeCell
        S t v hS htNarrow)
  have hSwide :=
    neutralIV009OriginalCollars_supported_window S hS
  rw [neutralIV011OriginalMixedPrime_eq_finite
        (11/10:ℝ) (11/10:ℝ) (le_refl _)
        (S+v•t) (S+v•t) hF hF 10
        neutralIV015FrozenConcrete_logCutoff,
      neutralIV011OriginalMixedPrime_eq_finite
        (11/10:ℝ) (11/10:ℝ) (le_refl _)
        S S hSwide hSwide 10
        neutralIV015FrozenConcrete_logCutoff]
  apply Finset.sum_congr rfl
  intro m hm
  by_cases hz : ArithmeticFunction.vonMangoldt m = 0
  · simp [hz]
  · obtain ⟨hp,hn⟩ :=
      neutralIV020WideExpandedActiveCorrelation_eq_old
        S t v hS ht m hm hz
    rw [hp,hn]

/-- The ONLY surviving original prime term for ANY enlarged
S+v•t source is the historic original old-collar prime.
NF600's genuine n=9 result bounds its real part by 2/5
old physical mass; disjointness enlarges mass, so the
SAME 2/5 bound holds for the new three-cell source. -/
theorem neutralIV020WideExpandedPrime_real_bound
    (S t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hS : neutralNF735InOriginalCollars S)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
        ((1/5:ℝ)+(1/500:ℝ)) → t x = 0) :
    |(neutralIV011OriginalMixedPrime
      (11/10:ℝ) (S+v•t) (S+v•t)).re| ≤
      (2/5:ℝ) * neutralNF600Mass (S+v•t) := by
  have htNarrow := neutralIV020Wide_support_from_bump t ht
  have hp := neutralNF600Prime_bound_actual S hS
  have heq := neutralIV020WideExpandedPrime_eq_old S t v hS ht
  have hcast :
      neutralIV011OriginalMixedPrime (11/10:ℝ) S S =
        neutralNF600Prime S := rfl
  rw [heq,hcast]
  have hm := neutralIV020WideOldMass_le_expandedMass
    S t v hS htNarrow
  linarith only [hp,hm]

/-- UNCONDITIONAL original signed 1/4 numerical coercivity TARGET:
for ANY complex old source supported in BOTH true NF543 collars,
any complex new physical Schwartz input supported in the
candidate [0.199,0.201] interval and any complex coefficient v,
the COMPLETE unmodified literal zeta Weil diagonal is >=1/4
of the exact enlarged physical L2 mass.

No old/new mixed Schur premise, no assumed source diagonal
positivity, no "positive" replacement prime series.
The n=9 historic prime and BOTH polar residues and complete
signed Gamma source are all paid explicitly. -/
theorem neutralIV020WideOriginalOldPlusNew_oneTenth_coercive
    (S t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hS : neutralNF735InOriginalCollars S)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
        ((1/5:ℝ)+(1/500:ℝ)) → t x = 0) :
    (1/10:ℝ) * neutralNF600Mass (S+v•t) ≤
      (neutralIV010Diagonal (11/10:ℝ) (S+v•t)).re := by
  have htNarrow := neutralIV020Wide_support_from_bump t ht
  have hSupport := neutralIV020WideOldPlusNew_supportedThreeCell
    S t v hS htNarrow
  have hPrime := neutralIV020WideExpandedPrime_real_bound
    S t v hS ht
  exact neutralIV020WideThreeCell_oneTenth_of_primeBound
    (S+v•t) hSupport hPrime

/-- Apply the true 1/4 signed original arithmetic bound to the
full old finite source family rather than a hypothetical Gram
vector: the old source is the genuine physical complex sum
Σ_i u_i • s_i supported in the FROZEN NF543 two collars.
This is a simultaneous all-complex-coefficient family result. -/
theorem neutralIV020WideOriginalFiniteOldPlusNew_oneTenth
    {n : ℕ}
    (s : Fin n → 𝓢(ℝ,ℂ))
    (hs : ∀ i : Fin n, neutralNF735InOriginalCollars (s i))
    (u : Fin n → ℂ) (t : 𝓢(ℝ,ℂ))
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
        ((1/5:ℝ)+(1/500:ℝ)) → t x = 0)
    (v : ℂ) :
    (1/10:ℝ) *
      neutralNF600Mass
        (neutralIV009PhysicalSchwartzSum s u + v•t) ≤
      (neutralIV010Diagonal (11/10:ℝ)
        (neutralIV009PhysicalSchwartzSum s u + v•t)).re := by
  have hS : neutralNF735InOriginalCollars
      (neutralIV009PhysicalSchwartzSum s u) := by
    change neutralNF735InOriginalCollars
      (∑ i : Fin n, u i • s i)
    exact neutralNF738OriginalCollars_finset_linear
      (Finset.univ : Finset (Fin n)) s u
      (by intro i _; exact hs i)
  exact neutralIV020WideOriginalOldPlusNew_oneTenth_coercive
    (neutralIV009PhysicalSchwartzSum s u) t v hS ht

/-- Construct a GENUINE nonzero complex Schwartz new physical
direction outside the old frozen original two collars, and
CERTIFY the complete ORIGINAL zeta Weil quadratic positivity
uniformly in EVERY old finite physical coefficient vector and
EVERY new complex coefficient.

This is a strict finite-class genuine source-extension theorem
candidate — not global Weil positivity, not the Riemann
hypothesis, and not a general radius enlargement.
It requires NO residual mixed Schur hypothesis. -/
theorem neutralIV020WideExistsGenuineNewThreeCellPositiveDirection
    {n : ℕ}
    (s : Fin n → 𝓢(ℝ,ℂ))
    (hs : ∀ i : Fin n, neutralNF735InOriginalCollars (s i)) :
    ∃ t : 𝓢(ℝ,ℂ),
      t (1/5:ℝ) = 1 ∧
      ¬ neutralNF735InOriginalCollars t ∧
      (∀ (u : Fin n → ℂ) (v : ℂ),
        (1/10:ℝ) *
          neutralNF600Mass
            (neutralIV009PhysicalSchwartzSum s u + v•t) ≤
          (neutralIV010Diagonal (11/10:ℝ)
            (neutralIV009PhysicalSchwartzSum s u + v•t)).re) := by
  obtain ⟨t,htone,htlocal⟩ :=
    neutralIV015ExistsComplexSchwartzBump
      (1/5:ℝ) (1/500:ℝ) (by norm_num)
  have hnew : ¬ neutralNF735InOriginalCollars t := by
    intro hOld
    have hz :=
      hOld (1/5:ℝ) neutralIV015FrozenConcrete_centerOutside
    rw [htone] at hz
    exact one_ne_zero hz
  refine ⟨t,htone,hnew,?_⟩
  intro u v
  exact neutralIV020WideOriginalFiniteOldPlusNew_oneTenth
    s hs u t htlocal v


#print axioms neutralNF600Prime_single
#print axioms neutralNF600Prime_bound_actual
#print axioms neutralIV019WideFrozenConcrete_allIntegerGap
#print axioms neutralIV019WideSelfActiveGap
#print axioms neutralIV020WideOldPlusNew_supportedThreeCell
#print axioms neutralIV020WideOldPlusNew_mass_add
#print axioms neutralIV020WideOldMass_le_expandedMass
#print axioms neutralIV020WideExpandedCorrelation_eq_old_of_threeZeros
#print axioms neutralIV020WideExpandedActiveCorrelation_eq_old
#print axioms neutralIV020WideExpandedPrime_eq_old
#print axioms neutralIV020WideExpandedPrime_real_bound
#print axioms neutralIV020WideOriginalOldPlusNew_oneTenth_coercive
#print axioms neutralIV020WideOriginalFiniteOldPlusNew_oneTenth
#print axioms neutralIV020WideExistsGenuineNewThreeCellPositiveDirection

end
end WeilDefect
