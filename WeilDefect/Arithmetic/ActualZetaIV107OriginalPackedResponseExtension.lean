import WeilDefect.Arithmetic.ActualZetaIV106OriginalPackedGramResponse
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- The literal mixed pairing on the original all-multiplicity divisor. -/
theorem neutralIV107Mixed_eq_tsum (a : ℝ) (f g : 𝓢(ℝ,ℂ))
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-a) a → g x = 0) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      neutralIV009OriginalPairTerm a f g q) = neutralIV101Mixed a f g := by
  exact neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond
    a (f.toLp 2 volume) (g.toLp 2 volume) (fun x : ℝ => g x)
    (g.smooth 2) (neutralIV008SchwartzWindow_hasCompactSupport a g hg)
    (neutralIV006Schwartz_window_ae a g hg)

/-- First-slot conjugate linearity, derived from the actual divisor sum. -/
theorem neutralIV107Mixed_sum_left {n : ℕ} (a : ℝ)
    (s : Fin n → 𝓢(ℝ,ℂ)) (c : Fin n → ℂ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    neutralIV101Mixed a (neutralIV009PhysicalSchwartzSum s c) v =
      ∑ i : Fin n, conj (c i) * neutralIV101Mixed a (s i) v := by
  classical
  rw [← neutralIV107Mixed_eq_tsum a _ v hv]
  have hterm (i : Fin n) : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (c i) * neutralIV009OriginalPairTerm a (s i) v q) :=
    (neutralIV009OriginalPairTerm_summable a (s i) v hv).mul_left _
  calc
    _ = ∑' q : NeutralActualZetaDivisorCoordinate, ∑ i : Fin n,
        conj (c i) * neutralIV009OriginalPairTerm a (s i) v q := by
          apply tsum_congr
          intro q
          unfold neutralIV009OriginalPairTerm
          rw [neutralIV009WindowEvaluation_finiteLinear]
          simp only [map_sum, map_mul, Finset.sum_mul]
          apply Finset.sum_congr rfl
          intro i hi
          ring
    _ = ∑ i : Fin n, ∑' q : NeutralActualZetaDivisorCoordinate,
        conj (c i) * neutralIV009OriginalPairTerm a (s i) v q :=
      Summable.tsum_finsetSum (s := (Finset.univ : Finset (Fin n)))
        (f := fun i q => conj (c i) * neutralIV009OriginalPairTerm a (s i) v q)
        (by intro i _; exact hterm i)
    _ = _ := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [tsum_mul_left, neutralIV107Mixed_eq_tsum a (s i) v hv]

/-- Second-slot linearity, preserving the fixed support and exact sums. -/
theorem neutralIV107Mixed_sum_right {n : ℕ} (a : ℝ)
    (s : Fin n → 𝓢(ℝ,ℂ)) (c : Fin n → ℂ) (v : 𝓢(ℝ,ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ, x ∉ Set.Icc (-a) a → s i x = 0) :
    neutralIV101Mixed a v (neutralIV009PhysicalSchwartzSum s c) =
      ∑ i : Fin n, neutralIV101Mixed a v (s i) * c i := by
  classical
  rw [← neutralIV107Mixed_eq_tsum a v _
    (neutralIV009PhysicalSchwartzSum_supported a s c hs)]
  have hterm (i : Fin n) : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      neutralIV009OriginalPairTerm a v (s i) q * c i) :=
    (neutralIV009OriginalPairTerm_summable a v (s i) (hs i)).mul_right _
  calc
    _ = ∑' q : NeutralActualZetaDivisorCoordinate, ∑ i : Fin n,
        neutralIV009OriginalPairTerm a v (s i) q * c i := by
          apply tsum_congr
          intro q
          unfold neutralIV009OriginalPairTerm
          rw [neutralIV009WindowEvaluation_finiteLinear, Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro i hi
          ring
    _ = ∑ i : Fin n, ∑' q : NeutralActualZetaDivisorCoordinate,
        neutralIV009OriginalPairTerm a v (s i) q * c i :=
      Summable.tsum_finsetSum (s := (Finset.univ : Finset (Fin n)))
        (f := fun i q => neutralIV009OriginalPairTerm a v (s i) q * c i)
        (by intro i _; exact hterm i)
    _ = _ := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [tsum_mul_right, neutralIV107Mixed_eq_tsum a v (s i) (hs i)]

/-- Extend the exact solved Gram rows to every packed first argument. -/
theorem neutralIV107Response_mixed (k : ℕ) (hk : 0 < k)
    (c : Fin k → ℂ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c) v =
      neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c)
        (neutralIV100Packed k hk (neutralIV106Response k hk v)) := by
  let p := neutralIV100Carrier k hk
  let d := neutralIV106Response k hk v
  have hs (i : Fin k) := neutralIV009OriginalCollars_supported_window _
    (neutralIV100Carrier_collars k hk i)
  have hd := neutralIV009PhysicalSchwartzSum_supported (11/10:ℝ) p d hs
  change neutralIV101Mixed (11/10:ℝ) (neutralIV009PhysicalSchwartzSum p c) v =
    neutralIV101Mixed (11/10:ℝ) (neutralIV009PhysicalSchwartzSum p c)
      (neutralIV009PhysicalSchwartzSum p d)
  rw [neutralIV107Mixed_sum_left _ p c v hv,
    neutralIV107Mixed_sum_left _ p c _ hd]
  apply Finset.sum_congr rfl
  intro i hi
  rw [neutralIV107Mixed_sum_right _ p d (p i) hs]
  have hr := congrFun (neutralIV106Response_solves k hk v) i
  change (∑ j : Fin k, neutralIV101Mixed (11/10:ℝ) (p i) (p j) * d j) =
    neutralIV101Mixed (11/10:ℝ) (p i) v at hr
  rw [hr]

def neutralIV107SchurEnergy (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) : ℝ :=
  neutralIV101Q (11/10:ℝ) v -
    neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (neutralIV106Response k hk v))

/-- No response-existence premise remains; complementary positivity is explicit. -/
theorem neutralIV107Window_nonneg_of_schur (k : ℕ) (hk : 0 < k)
    (hschur : ∀ v : 𝓢(ℝ,ℂ), neutralIV101MassComplement k hk v →
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) →
      0 ≤ neutralIV107SchurEnergy k hk v)
    (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0) :
    0 ≤ neutralIV101Q (11/10:ℝ) s := by
  apply neutralIV105Window_nonneg_of_response k hk _ s hs
  intro v horth hv
  refine ⟨neutralIV106Response k hk v, ?_, ?_⟩
  · intro c
    exact congrArg Complex.re (neutralIV107Response_mixed k hk c v hv)
  · have h := hschur v horth hv
    unfold neutralIV107SchurEnergy at h
    linarith

#print axioms neutralIV107Mixed_eq_tsum
#print axioms neutralIV107Mixed_sum_left
#print axioms neutralIV107Mixed_sum_right
#print axioms neutralIV107Response_mixed
#print axioms neutralIV107Window_nonneg_of_schur

end
end WeilDefect
