import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalActivePrimeSupportGeometry
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension
import Mathlib.Analysis.Distribution.SchwartzSpace.Basic
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators Topology

/-!
IV015 — actual NONZERO original complex Schwartz support witness.

IV014 provided a finite arithmetic-active prime-power interval-gap
criterion, but neither generated a nonzero test nor proved that such a
test lies beyond the old finite Schwartz span.

The construction below uses Mathlib's genuine C-infinity compact
bump function, sends the REAL bump into the COMPLEX physical target
through Complex.ofRealCLM, and uses the true
HasCompactSupport.toSchwartzMap embedding. The value at the selected
center is EXACTLY ONE. The source outside a prescribed interval
vanishes and every old finite superposition supported in [-a,a]
vanishes at that center, giving a PROVED algebraic distinction.

Existence of a suitable PRIME-ACTIVE geometric gap and original new
diagonal/residual Schur positivity remain OPEN numerical/analytic
obligations. Source is a Lean CANDIDATE until real kernel PASS.
-/

/-- A literal, nonzero, compactly supported COMPLEX Schwartz function
in any positive-radius real interval, with exact value one at its
center. This is an actual physical object, not a conditional abstract
Gram vector or an asserted new-support existence hypothesis. -/
theorem neutralIV015ExistsComplexSchwartzBump
    (c r : ℝ) (hr : 0 < r) :
    ∃ t : 𝓢(ℝ, ℂ),
      t c = 1 ∧
      (∀ x : ℝ, x ∉ Set.Icc (c-r) (c+r) → t x = 0) := by
  have hc : c ∈ Set.Ioo (c-r) (c+r) := by
    constructor <;> linarith
  obtain ⟨f, hts, hcompact, hsmooth, _, hfc⟩ :=
    exists_contDiff_tsupport_subset (n := (⊤ : ℕ∞))
      (isOpen_Ioo.mem_nhds hc)
  let q : ℝ → ℂ := Complex.ofRealCLM ∘ f
  have hqcompact : HasCompactSupport q := hcompact.comp_left rfl
  have hqdiff : ContDiff ℝ ∞ q := Complex.ofRealCLM.contDiff.comp hsmooth
  let t : 𝓢(ℝ, ℂ) := hqcompact.toSchwartzMap hqdiff
  refine ⟨t, ?_, ?_⟩
  · change Complex.ofRealCLM (f c) = (1 : ℂ)
    simp [hfc]
  · intro x hx
    change q x = 0
    by_contra hn
    have hxmem : x ∈ Function.support q := by
      simpa only [Function.mem_support] using hn
    have hxTS : x ∈ tsupport q := subset_tsupport q hxmem
    have hqts : tsupport q ⊆ Set.Ioo (c-r) (c+r) := by
      exact (tsupport_comp_subset rfl _).trans hts
    have hxI := hqts hxTS
    exact hx ⟨le_of_lt hxI.1, le_of_lt hxI.2⟩

/-- A nonzero bump supported in a small interval inside [-b,b] has
the authentic physical large-window support condition. This does
NOT say that the entire old [-a,a] window satisfies any positivity
criterion. -/
theorem neutralIV015Bump_supported_largeWindow
    (b c r : ℝ)
    (hwin : |c| + r < b)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (c-r) (c+r) → t x = 0) :
    ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0 := by
  have hleft : -b ≤ c-r := by
    have hc := neg_abs_le c
    linarith
  have hright : c+r ≤ b := by
    have hc := le_abs_self c
    linarith
  intro x hx
  apply ht x
  intro hsmall
  exact hx ⟨hleft.trans hsmall.1, hsmall.2.trans hright⟩

/-- The center of any bump with a+r<|c| is outside the old source
interval [-a,a]. An old finite physical Schwartz sum supported there
must vanish at c, while the true new bump equals one. Thus the
constructed physical source is NOT in the old finite family span. -/
theorem neutralIV015Bump_not_oldPhysicalSpan
    {n : ℕ} (a c : ℝ)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (hcenter : a < |c|)
    (t : 𝓢(ℝ, ℂ)) (htc : t c = 1) :
    t ≠ neutralIV009PhysicalSchwartzSum s u := by
  have hc : c ∉ Set.Icc (-a) a := by
    intro hc
    have hnorm : |c| ≤ a := abs_le.mpr hc
    linarith
  have hzero :=
    neutralIV009PhysicalSchwartzSum_supported a s u hs c hc
  intro heq
  have hv := congrArg (fun f : 𝓢(ℝ, ℂ) => f c) heq
  rw [htc, hzero] at hv
  exact one_ne_zero hv

/-- UNIFORM genuine physical bump existence conditional ONLY on
FINITE center/radius prime-log geometric inequalities, not on a
postulated nonzero Schwartz vector. The same bump works for EVERY
old complex Schwartz input supported in [-a,a]. -/
theorem neutralIV015ExistsUniformActivePrimeSeparatedBump
    (a b c r : ℝ) (N : ℕ)
    (hr : 0 < r)
    (hwin : |c| + r < b)
    (hgap : ∀ m : ℕ, m ∈ Finset.range N →
      ArithmeticFunction.vonMangoldt m ≠ 0 →
      a+r < |c - Real.log m| ∧
      a+r < |c + Real.log m|) :
    ∃ t : 𝓢(ℝ, ℂ),
      t c = 1 ∧
      (∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0) ∧
      (∀ s : 𝓢(ℝ, ℂ),
        (∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0) →
          neutralIV014ActivePrimeSeparated s t N) := by
  obtain ⟨t, htc, htlocal⟩ :=
    neutralIV015ExistsComplexSchwartzBump c r hr
  have htwide :=
    neutralIV015Bump_supported_largeWindow b c r hwin t htlocal
  refine ⟨t, htc, htwide, ?_⟩
  intro s hs
  have hS :
      ∀ x : ℝ, x ∉ Set.Icc (0-a) (0+a) → s x = 0 := by
    simpa only [zero_sub, zero_add] using hs
  have hcenterGaps :
      ∀ m : ℕ, m ∈ Finset.range N →
        ArithmeticFunction.vonMangoldt m ≠ 0 →
        a+r < |c - 0 - Real.log m| ∧
        a+r < |c - 0 + Real.log m| := by
    intro m hm hactive
    simpa only [sub_zero] using hgap m hm hactive
  exact neutralIV014ActiveSeparated_of_intervalGap
    s t N 0 c a r hS htlocal hcenterGaps

/-- Original arithmetic physical witness, genuinely outside the
previous old finite [-a,a] Schwartz span, with ZERO original mixed
Λ-weighted prime term and UNCHANGED original two-pole-plus-Gamma EF.
The only remaining premises are exact finite arithmetic interval
gaps and a genuine logarithmic cutoff. It does NOT sign the residual
or the new diagonal, and gives no global Weil positivity. -/
theorem neutralIV015ExistsOriginalPrimeFreeNewPhysicalDirection
    {n : ℕ} (a b c r : ℝ) (N : ℕ)
    (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (hr : 0 < r)
    (hwin : |c| + r < b)
    (hnew : a+r < |c|)
    (hcut : ∀ m : ℕ, N ≤ m → a+b < Real.log m)
    (hgap : ∀ m : ℕ, m ∈ Finset.range N →
      ArithmeticFunction.vonMangoldt m ≠ 0 →
      a+r < |c - Real.log m| ∧
      a+r < |c + Real.log m|) :
    ∃ t : 𝓢(ℝ, ℂ),
      t c = 1 ∧
      (∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0) ∧
      t ≠ neutralIV009PhysicalSchwartzSum s u ∧
      neutralIV011OriginalMixedPrime b
        (neutralIV009PhysicalSchwartzSum s u) t = 0 ∧
      neutralIV010Mixed b
        (neutralIV009PhysicalSchwartzSum s u) t =
        neutralIV013OriginalMixedAnalyticRemainder b
          (neutralIV009PhysicalSchwartzSum s u) t := by
  obtain ⟨t, htc, htwide, hsepAll⟩ :=
    neutralIV015ExistsUniformActivePrimeSeparatedBump
      a b c r N hr hwin hgap
  let S := neutralIV009PhysicalSchwartzSum s u
  have hS : ∀ x : ℝ, x ∉ Set.Icc (-a) a → S x = 0 :=
    neutralIV009PhysicalSchwartzSum_supported a s u hs
  have hsep : neutralIV014ActivePrimeSeparated S t N :=
    hsepAll S hS
  have hprime := neutralIV014ActiveMixedPrime_zero
    a b hab S t hS htwide N hcut hsep
  have hEF := neutralIV014ActiveMixed_eq_analytic
    a b hab S t hS htwide N hcut hsep
  refine ⟨t, htc, htwide, ?_, hprime, hEF⟩
  exact neutralIV015Bump_not_oldPhysicalSpan a c s u hs
    (by linarith) t htc

#print axioms neutralIV014ActiveSeparated_of_intervalGap
#print axioms neutralIV014ActiveMixedPrime_zero
#print axioms neutralIV014ActiveMixed_eq_analytic
#print axioms neutralIV009PhysicalSchwartzSum_supported
#print axioms neutralIV015ExistsComplexSchwartzBump
#print axioms neutralIV015Bump_supported_largeWindow
#print axioms neutralIV015Bump_not_oldPhysicalSpan
#print axioms neutralIV015ExistsUniformActivePrimeSeparatedBump
#print axioms neutralIV015ExistsOriginalPrimeFreeNewPhysicalDirection

end
end WeilDefect
