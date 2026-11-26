import WeilDefect.Arithmetic.ActualZetaIV123OriginalPoleReceiver
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- Hermitian symmetry of the actual mixed arithmetic form, on supported tests. -/
theorem neutralIV130Mixed_hermitian (a : ℝ) (u v : 𝓢(ℝ,ℂ))
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

theorem neutralIV130Mixed_add_right (a : ℝ) (u v w : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0)
    (hw : ∀ x : ℝ, x ∉ Set.Icc (-a) a → w x = 0) :
    neutralIV101Mixed a u (v+w) =
      neutralIV101Mixed a u v + neutralIV101Mixed a u w := by
  let s : Fin 2 → 𝓢(ℝ,ℂ) := ![v,w]
  have hs : ∀ i : Fin 2, ∀ x : ℝ, x ∉ Set.Icc (-a) a → s i x = 0 := by
    intro i x hx
    fin_cases i
    · simpa [s] using hv x hx
    · simpa [s] using hw x hx
  have hS : neutralIV009PhysicalSchwartzSum s (fun _ => 1) = v+w := by
    simp [neutralIV009PhysicalSchwartzSum, Fin.sum_univ_two, s]
  have h := neutralIV107Mixed_sum_right a s (fun _ => 1) u hs
  rw [hS] at h
  simpa [s, Fin.sum_univ_two] using h

theorem neutralIV130Mixed_sub_left (a : ℝ) (u v w : 𝓢(ℝ,ℂ))
    (hw : ∀ x : ℝ, x ∉ Set.Icc (-a) a → w x = 0) :
    neutralIV101Mixed a (u-v) w =
      neutralIV101Mixed a u w - neutralIV101Mixed a v w := by
  let s : Fin 2 → 𝓢(ℝ,ℂ) := ![u,v]
  let c : Fin 2 → ℂ := ![1,-1]
  have hS : neutralIV009PhysicalSchwartzSum s c = u-v := by
    simp [neutralIV009PhysicalSchwartzSum, Fin.sum_univ_two, s, c, sub_eq_add_neg]
  have h := neutralIV107Mixed_sum_left a s c w hw
  rw [hS] at h
  simpa [s, c, Fin.sum_univ_two, sub_eq_add_neg] using h

/-- Linearity of the uniquely solved original packed response on supported sums. -/
theorem neutralIV130Response_add (k : ℕ) (hk : 0 < k) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV106Response k hk (u+v) =
      fun i => neutralIV106Response k hk u i + neutralIV106Response k hk v i := by
  symm
  apply neutralIV106Response_unique
  funext i
  have h1 := congrFun (neutralIV106Response_solves k hk u) i
  have h2 := congrFun (neutralIV106Response_solves k hk v) i
  change (∑ j : Fin k, neutralIV106Gram k hk i j * neutralIV106Response k hk u j) =
    neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) u at h1
  change (∑ j : Fin k, neutralIV106Gram k hk i j * neutralIV106Response k hk v j) =
    neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v at h2
  change (∑ j : Fin k, neutralIV106Gram k hk i j *
    (neutralIV106Response k hk u j + neutralIV106Response k hk v j)) =
    neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) (u+v)
  rw [neutralIV130Mixed_add_right _ _ u v hu hv]
  simp only [mul_add, Finset.sum_add_distrib, h1, h2]

def neutralIV130ResponseVector (k : ℕ) (hk : 0 < k) (u : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  neutralIV100Packed k hk (neutralIV106Response k hk u)

def neutralIV130Mixed (k : ℕ) (hk : 0 < k) (u v : 𝓢(ℝ,ℂ)) : ℂ :=
  neutralIV101Mixed (11/10:ℝ) u v -
    neutralIV101Mixed (11/10:ℝ) (neutralIV130ResponseVector k hk u)
      (neutralIV130ResponseVector k hk v)

theorem neutralIV130Response_supported (k : ℕ) (hk : 0 < k) (u : 𝓢(ℝ,ℂ)) :
    ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
      neutralIV130ResponseVector k hk u x = 0 :=
  neutralIV009OriginalCollars_supported_window _
    (neutralIV101Packed_collars k hk (neutralIV106Response k hk u))

theorem neutralIV130Mixed_diagonal (k : ℕ) (hk : 0 < k) (u : 𝓢(ℝ,ℂ)) :
    (neutralIV130Mixed k hk u u).re = neutralIV107SchurEnergy k hk u := by
  simp only [neutralIV130Mixed, Complex.sub_re, neutralIV130ResponseVector,
    neutralIV107SchurEnergy, neutralIV101Q]

/-- The corrected mixed form is a single actual physical row, with the
first argument corrected by the exact packed response. -/
theorem neutralIV130Mixed_row (k : ℕ) (hk : 0 < k) (u v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV130Mixed k hk u v =
      neutralIV101Mixed (11/10:ℝ) (u-neutralIV130ResponseVector k hk u) v := by
  rw [neutralIV130Mixed_sub_left _ _ _ _ hv]
  unfold neutralIV130Mixed neutralIV130ResponseVector
  rw [neutralIV107Response_mixed k hk (neutralIV106Response k hk u) v hv]

theorem neutralIV130Mixed_physical_bound (k : ℕ) (hk : 0 < k) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    ‖neutralIV130Mixed k hk u v‖ ≤
      neutralIV109RowConstant (11/10:ℝ) (u-neutralIV130ResponseVector k hk u) *
        ‖v.toLp 2 volume‖ := by
  rw [neutralIV130Mixed_row k hk u v hv]
  apply neutralIV109Mixed_physical_bound _ (by norm_num) _ _ _ hv
  intro x hx
  change u x - neutralIV130ResponseVector k hk u x = 0
  rw [hu x hx, neutralIV130Response_supported k hk u x hx, sub_zero]

/-- Exact polarization of the response-corrected diagonal. -/
theorem neutralIV130Schur_add (k : ℕ) (hk : 0 < k) (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV107SchurEnergy k hk (u+v) =
      neutralIV107SchurEnergy k hk u + 2*(neutralIV130Mixed k hk u v).re +
        neutralIV107SchurEnergy k hk v := by
  have hR : neutralIV130ResponseVector k hk (u+v) =
      neutralIV130ResponseVector k hk u + neutralIV130ResponseVector k hk v := by
    unfold neutralIV130ResponseVector
    rw [neutralIV130Response_add k hk u v hu hv, ← neutralIV105Packed_add]
  change neutralIV101Q (11/10:ℝ) (u+v) -
    neutralIV101Q (11/10:ℝ) (neutralIV130ResponseVector k hk (u+v)) = _
  rw [hR, neutralIV101Q_add _ u v hu hv,
    neutralIV101Q_add _ _ _ (neutralIV130Response_supported k hk u)
      (neutralIV130Response_supported k hk v)]
  change _ = (neutralIV101Q (11/10:ℝ) u -
    neutralIV101Q (11/10:ℝ) (neutralIV130ResponseVector k hk u)) +
    2*(neutralIV101Mixed (11/10:ℝ) u v -
      neutralIV101Mixed (11/10:ℝ) (neutralIV130ResponseVector k hk u)
        (neutralIV130ResponseVector k hk v)).re +
    (neutralIV101Q (11/10:ℝ) v -
      neutralIV101Q (11/10:ℝ) (neutralIV130ResponseVector k hk v))
  simp only [Complex.sub_re]
  ring

#print axioms neutralIV130Mixed_hermitian
#print axioms neutralIV130Mixed_add_right
#print axioms neutralIV130Mixed_sub_left
#print axioms neutralIV130Response_add
#print axioms neutralIV130Response_supported
#print axioms neutralIV130Mixed_diagonal
#print axioms neutralIV130Mixed_row
#print axioms neutralIV130Mixed_physical_bound
#print axioms neutralIV130Schur_add

end
end WeilDefect
