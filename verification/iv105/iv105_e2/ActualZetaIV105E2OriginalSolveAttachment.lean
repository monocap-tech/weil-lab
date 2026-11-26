import WeilDefect.Arithmetic.ActualZetaIV105E1OriginalGramSolve
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

theorem neutralIV105E2Hermitian (a : ℝ) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    conj (neutralIV101Mixed a u v) = neutralIV101Mixed a v u := by
  let s : Fin 2 → 𝓢(ℝ,ℂ) := ![u,v]
  have hs : ∀ i : Fin 2, ∀ x : ℝ, x ∉ Set.Icc (-a) a → s i x = 0 := by
    intro i x hx
    fin_cases i
    · simpa [s] using hu x hx
    · simpa [s] using hv x hx
  simpa [s, neutralIV007OriginalMixedEntry, neutralIV101Mixed] using
    neutralIV008OriginalMixedEntry_hermitian a s hs 0 1

/-- Exact row linearity from the certified physical action and IV104 sum. -/
theorem neutralIV105E2Packed_right (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ)) (c : Fin k → ℂ)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV101Mixed (11/10:ℝ) v (neutralIV100Packed k hk c) =
      ∑ i : Fin k, neutralIV101Mixed (11/10:ℝ) v (neutralIV100Carrier k hk i) * c i := by
  have hp := neutralIV009OriginalCollars_supported_window
    (neutralIV100Packed k hk c) (neutralIV101Packed_collars k hk c)
  rw [neutralIV105BAction_pair _ (by norm_num) _ _ hv hp,
    neutralIV104Packed_toLp, inner_sum]
  simp only [inner_smul_right]
  apply Finset.sum_congr rfl
  intro i hi
  have hpi := neutralIV009OriginalCollars_supported_window
    (neutralIV100Carrier k hk i) (neutralIV100Carrier_collars k hk i)
  rw [neutralIV105BAction_pair _ (by norm_num) _ _ hv hpi]
  ring

theorem neutralIV105E2Packed_left (k : ℕ) (hk : 0 < k)
    (c : Fin k → ℂ) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c) v =
      ∑ i : Fin k, conj (c i) * neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v := by
  have hp := neutralIV009OriginalCollars_supported_window
    (neutralIV100Packed k hk c) (neutralIV101Packed_collars k hk c)
  rw [← neutralIV105E2Hermitian _ v _ hv hp, neutralIV105E2Packed_right k hk v c hv,
    map_sum]
  apply Finset.sum_congr rfl
  intro i hi
  have hpi := neutralIV009OriginalCollars_supported_window
    (neutralIV100Carrier k hk i) (neutralIV100Carrier_collars k hk i)
  rw [map_mul, neutralIV105E2Hermitian _ v _ hv hpi]
  ring

/-- Exact finite solve obtained from the actual Gram surjectivity, not a trial inverse. -/
def neutralIV105E2Solve (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) : Fin k → ℂ :=
  (neutralIV105EGram_surjective k hk
    (fun i => neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v)).choose

theorem neutralIV105E2Solve_eq (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) :
    neutralIV105EGram k hk (neutralIV105E2Solve k hk v) =
      fun i => neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v :=
  (neutralIV105EGram_surjective k hk
    (fun i => neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v)).choose_spec

theorem neutralIV105E2Solve_rows (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ))
    (i : Fin k) :
    neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v =
      neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i)
        (neutralIV100Packed k hk (neutralIV105E2Solve k hk v)) := by
  have hi := congrFun (neutralIV105E2Solve_eq k hk v) i
  change (∑ j : Fin k, neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i)
    (neutralIV100Carrier k hk j) * neutralIV105E2Solve k hk v j) =
      neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v at hi
  have hpi := neutralIV009OriginalCollars_supported_window
    (neutralIV100Carrier k hk i) (neutralIV100Carrier_collars k hk i)
  rw [neutralIV105E2Packed_right k hk _ _ hpi]
  exact hi.symm

theorem neutralIV105E2Solve_all (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ)) (e : Fin k → ℂ)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk e) v =
      neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk e)
        (neutralIV100Packed k hk (neutralIV105E2Solve k hk v)) := by
  have hp := neutralIV009OriginalCollars_supported_window
    (neutralIV100Packed k hk (neutralIV105E2Solve k hk v))
    (neutralIV101Packed_collars k hk (neutralIV105E2Solve k hk v))
  rw [neutralIV105E2Packed_left k hk e v hv,
    neutralIV105E2Packed_left k hk e _ hp]
  apply Finset.sum_congr rfl
  intro i hi
  rw [neutralIV105E2Solve_rows k hk v i]

/-- Fixed-window Schur equivalence without an external solve hypothesis.
The remaining complementary domination condition is the right side. -/
theorem neutralIV105E2Window_nonneg_iff (k : ℕ) (hk : 0 < k) :
    (∀ s : 𝓢(ℝ,ℂ),
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0) →
      0 ≤ neutralIV101Q (11/10:ℝ) s) ↔
    (∀ v : 𝓢(ℝ,ℂ), neutralIV101MassComplement k hk v →
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) →
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (neutralIV105E2Solve k hk v)) ≤
        neutralIV101Q (11/10:ℝ) v) := by
  apply neutralIV105DWindow_nonneg_iff k hk (neutralIV105E2Solve k hk)
  intro v ho hv e
  exact congrArg Complex.re (neutralIV105E2Solve_all k hk v e hv)

#print axioms neutralIV105E2Hermitian
#print axioms neutralIV105E2Packed_right
#print axioms neutralIV105E2Packed_left
#print axioms neutralIV105E2Solve_eq
#print axioms neutralIV105E2Solve_rows
#print axioms neutralIV105E2Solve_all
#print axioms neutralIV105E2Window_nonneg_iff
end
end WeilDefect
