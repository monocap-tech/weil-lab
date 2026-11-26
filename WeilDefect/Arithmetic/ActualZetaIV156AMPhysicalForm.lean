import WeilDefect.Arithmetic.ActualZetaIV156AMGeneric
import WeilDefect.Arithmetic.ActualZetaIV153AMPointwiseSum
import WeilDefect.Arithmetic.ActualZetaIV154AMSupport

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped BigOperators SchwartzMap

def neutralIV156P : Finset ℕ := (neutralIV152PrimeRows.map Prod.fst).toFinset

theorem neutralIV156Nodup : (neutralIV152PrimeRows.map Prod.fst).Nodup := by decide

theorem neutralIV156Prime_pos (n : ℕ) (hn : n ∈ neutralIV156P) :
    0 < neutralIV151Weight n := by
  have hset : neutralIV156P = ({2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53} : Finset ℕ) :=
    neutralIV152Prime_bank
  rw [hset] at hn
  have hpp : IsPrimePow n := by
    simp only [Finset.mem_insert, Finset.mem_singleton] at hn
    rcases hn with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> decide
  unfold neutralIV151Weight
  exact div_pos (ArithmeticFunction.vonMangoldt_pos_iff.mpr hpp)
    (Real.sqrt_pos.2 (by exact_mod_cast hpp.pos))

/-- The explicit prime set, without multiplicities, is the signed row
sum used by the pointwise certificate. -/
theorem neutralIV156Physical_row (x : ℝ)
    (hl : -2 ≤ x) (hu : x < 2)
    (hbank : ∀ i : ℕ, i < 16384 →
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ)) :
    (∑ n ∈ neutralIV156P, neutralIV151Weight n *
      (neutralIV152PhysicalWeight (x+Real.log (n:ℝ)) +
       neutralIV152PhysicalWeight (x+(-Real.log (n:ℝ))))) ≤
      (7979648/1000000:ℝ)*neutralIV152PhysicalWeight x := by
  obtain ⟨i,hi,he⟩ := neutralIV154Window_index x hl hu
  have hh := neutralIV153Pointwise x i he (hbank i hi)
  unfold neutralIV156P
  rw [List.sum_toFinset _ neutralIV156Nodup, List.map_map]
  simpa only [Function.comp_def, neutralIV153PairTerm, sub_eq_add_neg] using hh

/-- A continuous function vanishing outside a closed window also
vanishes at its right endpoint by closure of the open right ray. -/
theorem neutralIV156Endpoint (f : ℝ → ℂ) (hf : Continuous f)
    (hs : ∀ x, x ∉ Set.Icc (-2:ℝ) 2 → f x = 0) :
    ∀ x, x ∉ Set.Ico (-2:ℝ) 2 → f x = 0 := by
  have hclosed : IsClosed (f ⁻¹' ({0} : Set ℂ)) := isClosed_singleton.preimage hf
  have hsub : Set.Ioi (2:ℝ) ⊆ f ⁻¹' ({0} : Set ℂ) := by
    intro x hx
    change f x ∈ ({0} : Set ℂ)
    simp only [Set.mem_singleton_iff]
    apply hs
    intro h
    exact (not_lt_of_ge h.2) hx
  have h2 : (2:ℝ) ∈ f ⁻¹' ({0} : Set ℂ) := by
    apply closure_minimal hsub hclosed
    rw [closure_Ioi]
    exact le_rfl
  intro x hx
  by_cases he : x = 2
  · subst x
    simpa using h2
  · apply hs
    intro h
    exact hx ⟨h.1,lt_of_le_of_ne h.2 he⟩

theorem neutralIV156Schwartz_cross (f : 𝓢(ℝ,ℂ)) (s : ℝ) :
    Integrable (fun x : ℝ => ‖f x‖*‖f (x+s)‖) := by
  have h1 : Integrable (fun x : ℝ => ‖f x‖) := f.integrable.norm
  have hm : AEStronglyMeasurable (fun x : ℝ => ‖f (x+s)‖) := by
    exact ((f.continuous.comp (continuous_id.add continuous_const)).norm).aestronglyMeasurable
  exact h1.mul_bdd hm (Filter.Eventually.of_forall (fun x => by
    rw [Real.norm_of_nonneg (norm_nonneg _)]
    exact f.norm_le_seminorm ℝ (x+s)))

/-- Conditional original arithmetic finite form on the closed-window
Schwartz core. The complete row bank remains an explicit premise. -/
theorem neutralIV156Physical_form (f : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-2:ℝ) 2 → f x = 0)
    (hbank : ∀ i : ℕ, i < 16384 →
      0 < neutralIV146Value (i:ℤ) ∧
      1000000 * neutralIV146Row i <
        7979648 * 1000000000 * neutralIV146Value (i:ℤ)) :
    ‖∑ n ∈ neutralIV156P, (neutralIV151Weight n:ℂ) *
      ((∫ x : ℝ, f x * star (f (x+Real.log (n:ℝ)))) +
       (∫ x : ℝ, f x * star (f (x-Real.log (n:ℝ)))))‖ ≤
      (7979648/1000000:ℝ)*∫ x : ℝ, ‖f x‖^2 := by
  have hs' := neutralIV156Endpoint f f.continuous hs
  have hnorm : ∀ x, x ∉ Set.Ico (-2:ℝ) 2 → ‖f x‖ = 0 :=
    fun x hx => by rw [hs' x hx, norm_zero]
  have ha := neutralIV156Prime_pos
  apply le_trans (neutralIV156Complex_form neutralIV156P neutralIV151Weight
    (fun n => Real.log (n:ℝ)) f (fun n hn => (ha n hn).le))
  apply neutralIV156Real_form neutralIV156P neutralIV151Weight
    (fun n => Real.log (n:ℝ)) neutralIV152PhysicalWeight (fun x => ‖f x‖)
    (7979648/1000000:ℝ) ha neutralIV152Physical_nonneg (by norm_num)
    neutralIV154Measurable_weight f.continuous.norm.measurable
    (neutralIV154Zero_compatible _ (fun i hi => (hbank i hi).1) hnorm)
  · simpa only [add_zero, pow_two] using neutralIV156Schwartz_cross f 0
  · intro n hn
    exact neutralIV156Schwartz_cross f _
  · intro x hx
    have hw : x ∈ Set.Ico (-2:ℝ) 2 := by
      by_contra! h
      exact hx (hnorm x h)
    exact neutralIV156Physical_row x hw.1 hw.2 (fun i hi => (hbank i hi).2)

#print axioms neutralIV156Nodup
#print axioms neutralIV156Prime_pos
#print axioms neutralIV156Physical_row
#print axioms neutralIV156Endpoint
#print axioms neutralIV156Schwartz_cross
#print axioms neutralIV156Physical_form
end
end WeilDefect
