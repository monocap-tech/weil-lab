import WeilDefect.Arithmetic.ActualZetaIV098OriginalReflectedCollarSectorGate
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap BigOperators

variable {ι : Type*}

/-- Disjointness is pointwise, not a diagonalization of the Weil form. -/
def neutralIV099Disjoint (t : Finset ι) (p : ι → ℝ → ℂ) : Prop :=
  ∀ i ∈ t, ∀ j ∈ t, i ≠ j → ∀ x, p i x = 0 ∨ p j x = 0

theorem neutralIV099Disjoint_norm_sum (t : Finset ι) (a : ι → ℂ)
    (h : ∀ i ∈ t, ∀ j ∈ t, i ≠ j → a i = 0 ∨ a j = 0) :
    ‖∑ i ∈ t, a i‖^2 = ∑ i ∈ t, ‖a i‖^2 := by
  classical
  revert h
  induction t using Finset.induction_on with
  | empty => simp
  | @insert i t hi ih =>
    intro h
    have ht : ∀ j ∈ t, ∀ k ∈ t, j ≠ k → a j = 0 ∨ a k = 0 :=
      fun j hj k hk hne => h j (Finset.mem_insert_of_mem hj) k
        (Finset.mem_insert_of_mem hk) hne
    simp only [Finset.sum_insert hi]
    by_cases hz : a i = 0
    · simpa [hz] using ih ht
    · have hj (j : ι) (hj : j ∈ t) : a j = 0 :=
        (h i (Finset.mem_insert_self i t) j (Finset.mem_insert_of_mem hj)
          (fun he => hi (he ▸ hj))).resolve_left hz
      have hs : (∑ j ∈ t, a j) = 0 := Finset.sum_eq_zero hj
      have hn : (∑ j ∈ t, ‖a j‖^2) = 0 :=
        Finset.sum_eq_zero fun j hjt => by simp [hj j hjt]
      rw [hs, hn, add_zero, add_zero]

theorem neutralIV099Weighted_norm_sum (t : Finset ι) (p : ι → ℝ → ℂ)
    (c : ι → ℂ) (h : neutralIV099Disjoint t p) (x : ℝ) :
    ‖∑ i ∈ t, c i * p i x‖^2 = ∑ i ∈ t, ‖c i‖^2 * ‖p i x‖^2 := by
  have hd : ∀ i ∈ t, ∀ j ∈ t, i ≠ j →
      c i * p i x = 0 ∨ c j * p j x = 0 := by
    intro i hi j hj hij
    rcases h i hi j hj hij x with hz | hz
    · left
      simp [hz]
    · right
      simp [hz]
  rw [neutralIV099Disjoint_norm_sum t (fun i => c i * p i x) hd]
  simp only [norm_mul, mul_pow]

theorem neutralIV099Disjoint_integral_sum (t : Finset ι) (p : ι → ℝ → ℂ)
    (c : ι → ℂ) (hp : ∀ i ∈ t, Integrable (fun x => ‖p i x‖^2))
    (h : neutralIV099Disjoint t p) :
    (∫ x : ℝ, ‖∑ i ∈ t, c i * p i x‖^2) =
      ∑ i ∈ t, ‖c i‖^2 * (∫ x : ℝ, ‖p i x‖^2) := by
  calc
    _ = ∫ x : ℝ, ∑ i ∈ t, ‖c i‖^2 * ‖p i x‖^2 := by
      apply integral_congr_ae
      exact Filter.Eventually.of_forall (neutralIV099Weighted_norm_sum t p c h)
    _ = ∑ i ∈ t, ∫ x : ℝ, ‖c i‖^2 * ‖p i x‖^2 := by
      exact integral_finsetSum t (fun i hi => (hp i hi).const_mul _)
    _ = _ := by
      apply Finset.sum_congr rfl
      intro i hi
      rw [integral_const_mul]

def neutralIV099Sector (t : Finset ι) (p : ι → 𝓢(ℝ,ℂ)) (c : ι → ℂ) :
    𝓢(ℝ,ℂ) := ∑ i ∈ t, c i • p i

theorem neutralIV099Sector_apply (t : Finset ι) (p : ι → 𝓢(ℝ,ℂ))
    (c : ι → ℂ) (x : ℝ) :
    neutralIV099Sector t p c x = ∑ i ∈ t, c i * p i x := by
  simp [neutralIV099Sector, SchwartzMap.sum_apply, smul_eq_mul]

theorem neutralIV099Sector_collars (t : Finset ι) (p : ι → 𝓢(ℝ,ℂ))
    (c : ι → ℂ) (hc : ∀ i ∈ t, neutralNF735InOriginalCollars (p i)) :
    neutralNF735InOriginalCollars (neutralIV099Sector t p c) := by
  intro x hx
  rw [neutralIV099Sector_apply]
  apply Finset.sum_eq_zero
  intro i hi
  rw [hc i hi x hx, mul_zero]

theorem neutralIV099Sector_derivative (t : Finset ι) (p : ι → 𝓢(ℝ,ℂ))
    (c : ι → ℂ) (x : ℝ) :
    deriv (neutralIV099Sector t p c : ℝ → ℂ) x =
      ∑ i ∈ t, c i * deriv (p i : ℝ → ℂ) x := by
  have he : (neutralIV099Sector t p c : ℝ → ℂ) =
      fun y => ∑ i ∈ t, c i * p i y :=
    funext (neutralIV099Sector_apply t p c)
  rw [he]
  have h : HasDerivAt (fun y : ℝ => ∑ i ∈ t, c i * p i y)
      (∑ i ∈ t, c i * deriv (p i : ℝ → ℂ) x) x :=
    HasDerivAt.fun_sum fun i hi => ((p i).differentiable x).hasDerivAt.const_mul (c i)
  exact h.deriv

theorem neutralIV099Sector_mass (t : Finset ι) (p : ι → 𝓢(ℝ,ℂ))
    (c : ι → ℂ) (h : neutralIV099Disjoint t (fun i => (p i : ℝ → ℂ))) :
    ‖(neutralIV099Sector t p c).toLp 2 volume‖^2 =
      ∑ i ∈ t, ‖c i‖^2 * ‖(p i).toLp 2 volume‖^2 := by
  have hp (i : ι) (hi : i ∈ t) : Integrable (fun x : ℝ => ‖p i x‖^2) :=
    (memLp_two_iff_integrable_sq_norm (p i).continuous.aestronglyMeasurable).mp
      ((p i).memLp 2 volume)
  rw [← neutralIV098Mass_integral (neutralIV099Sector t p c)]
  simp_rw [neutralIV099Sector_apply]
  rw [neutralIV099Disjoint_integral_sum t (fun i => (p i : ℝ → ℂ)) c hp h]
  simp_rw [neutralIV098Mass_integral]

theorem neutralIV099Sector_energy (t : Finset ι) (p : ι → 𝓢(ℝ,ℂ))
    (c : ι → ℂ)
    (h : neutralIV099Disjoint t (fun i => deriv (p i : ℝ → ℂ))) :
    neutralIV096DerivativeEnergy (neutralIV099Sector t p c) =
      ∑ i ∈ t, ‖c i‖^2 * neutralIV096DerivativeEnergy (p i) := by
  have hp (i : ι) (hi : i ∈ t) :
      Integrable (fun x : ℝ => ‖deriv (p i : ℝ → ℂ) x‖^2) := by
    let d := SchwartzMap.derivCLM ℂ ℂ (p i)
    exact (memLp_two_iff_integrable_sq_norm d.continuous.aestronglyMeasurable).mp
      (d.memLp 2 volume)
  unfold neutralIV096DerivativeEnergy
  simp_rw [neutralIV099Sector_derivative]
  exact neutralIV099Disjoint_integral_sum t (fun i => deriv (p i : ℝ → ℂ)) c hp h

theorem neutralIV099Sector_energy_ratio (t : Finset ι) (p : ι → 𝓢(ℝ,ℂ))
    (c : ι → ℂ) (C : ℝ)
    (hm : neutralIV099Disjoint t (fun i => (p i : ℝ → ℂ)))
    (hd : neutralIV099Disjoint t (fun i => deriv (p i : ℝ → ℂ)))
    (hb : ∀ i ∈ t, neutralIV096DerivativeEnergy (p i) ≤ C * ‖(p i).toLp 2 volume‖^2) :
    neutralIV096DerivativeEnergy (neutralIV099Sector t p c) ≤
      C * ‖(neutralIV099Sector t p c).toLp 2 volume‖^2 := by
  rw [neutralIV099Sector_energy t p c hd, neutralIV099Sector_mass t p c hm,
    Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  calc
    _ ≤ ‖c i‖^2 * (C * ‖(p i).toLp 2 volume‖^2) :=
      mul_le_mul_of_nonneg_left (hb i hi) (sq_nonneg _)
    _ = _ := by ring

theorem neutralIV099Sector_mass_zero_iff (t : Finset ι) (p : ι → 𝓢(ℝ,ℂ))
    (c : ι → ℂ)
    (hm : neutralIV099Disjoint t (fun i => (p i : ℝ → ℂ)))
    (hp : ∀ i ∈ t, 0 < ‖(p i).toLp 2 volume‖^2) :
    ‖(neutralIV099Sector t p c).toLp 2 volume‖^2 = 0 ↔ ∀ i ∈ t, c i = 0 := by
  classical
  rw [neutralIV099Sector_mass t p c hm]
  constructor
  · intro h i hi
    have hle : ‖c i‖^2 * ‖(p i).toLp 2 volume‖^2 ≤
        ∑ j ∈ t, ‖c j‖^2 * ‖(p j).toLp 2 volume‖^2 :=
      Finset.single_le_sum (fun j hj => mul_nonneg (sq_nonneg _) (sq_nonneg _)) hi
    rw [h] at hle
    have hz : ‖c i‖^2 * ‖(p i).toLp 2 volume‖^2 = 0 :=
      le_antisymm hle (mul_nonneg (sq_nonneg _) (sq_nonneg _))
    have hc : ‖c i‖^2 = 0 := (mul_eq_zero.mp hz).resolve_right (hp i hi).ne'
    exact norm_eq_zero.mp (mul_self_eq_zero.mp (by simpa only [pow_two] using hc))
  · intro h
    apply Finset.sum_eq_zero
    intro i hi
    simp [h i hi]

/-- Arbitrary-size finite receiver, with the complete original signed diagonal.
The disjointness and derivative budgets are explicitly retained premises. -/
theorem neutralIV099Sector_margin (t : Finset ι) (p : ι → 𝓢(ℝ,ℂ))
    (c : ι → ℂ) (C : ℝ) (M N : ℕ)
    (hc : ∀ i ∈ t, neutralNF735InOriginalCollars (p i))
    (hm : neutralIV099Disjoint t (fun i => (p i : ℝ → ℂ)))
    (hd : neutralIV099Disjoint t (fun i => deriv (p i : ℝ → ℂ)))
    (hb : ∀ i ∈ t, neutralIV096DerivativeEnergy (p i) ≤ C * ‖(p i).toLp 2 volume‖^2)
    (hM : Real.exp (2*(11/10:ℝ)) < (M : ℝ)) :
    ((2/5:ℝ) - C / ((N:ℝ)+1)^2) * ‖(neutralIV099Sector t p c).toLp 2 volume‖^2 ≤
      neutralIV095FiniteDiagonal M N (neutralIV099Sector t p c) := by
  let s := neutralIV099Sector t p c
  have hs := neutralIV099Sector_collars t p c hc
  have hf := neutralNF600SmoothCollarLower s hs
  have ht := neutralIV096CollarTail_derivative_bound M N s hs hM
  have he := neutralIV099Sector_energy_ratio t p c C hm hd hb
  have hpos : 0 < ((N:ℝ)+1)^2 := by positivity
  have htail : neutralIV096DerivativeEnergy s / ((N:ℝ)+1)^2 ≤
      (C / ((N:ℝ)+1)^2) * ‖s.toLp 2 volume‖^2 := by
    calc
      _ ≤ (C * ‖s.toLp 2 volume‖^2) / ((N:ℝ)+1)^2 :=
        div_le_div_of_nonneg_right he hpos.le
      _ = _ := by ring
  change neutralNF598SmoothWeil s - neutralIV095FiniteDiagonal M N s ≤ _ at ht
  change ((2/5:ℝ) - C / ((N:ℝ)+1)^2) * ‖s.toLp 2 volume‖^2 ≤
    neutralIV095FiniteDiagonal M N s
  rw [sub_mul]
  linarith

theorem neutralIV099Sector_cutoff (t : Finset ι) (p : ι → 𝓢(ℝ,ℂ))
    (c : ι → ℂ) (C : ℝ) (M N : ℕ)
    (hc : ∀ i ∈ t, neutralNF735InOriginalCollars (p i))
    (hm : neutralIV099Disjoint t (fun i => (p i : ℝ → ℂ)))
    (hd : neutralIV099Disjoint t (fun i => deriv (p i : ℝ → ℂ)))
    (hb : ∀ i ∈ t, neutralIV096DerivativeEnergy (p i) ≤ C * ‖(p i).toLp 2 volume‖^2)
    (hM : Real.exp (2*(11/10:ℝ)) < (M : ℝ))
    (hN : C ≤ ((N:ℝ)+1)^2 / 5) :
    (1/5:ℝ) * ‖(neutralIV099Sector t p c).toLp 2 volume‖^2 ≤
      neutralIV095FiniteDiagonal M N (neutralIV099Sector t p c) := by
  have hpos : 0 < ((N:ℝ)+1)^2 := by positivity
  have h : C / ((N:ℝ)+1)^2 ≤ 1/5 := by
    apply (div_le_iff₀ hpos).mpr
    linarith
  exact (mul_le_mul_of_nonneg_right
    (show (1/5:ℝ) ≤ 2/5 - C / ((N:ℝ)+1)^2 by linarith) (sq_nonneg _)).trans
    (neutralIV099Sector_margin t p c C M N hc hm hd hb hM)

#print axioms neutralIV099Disjoint_norm_sum
#print axioms neutralIV099Weighted_norm_sum
#print axioms neutralIV099Disjoint_integral_sum
#print axioms neutralIV099Sector_apply
#print axioms neutralIV099Sector_collars
#print axioms neutralIV099Sector_derivative
#print axioms neutralIV099Sector_mass
#print axioms neutralIV099Sector_energy
#print axioms neutralIV099Sector_energy_ratio
#print axioms neutralIV099Sector_mass_zero_iff
#print axioms neutralIV099Sector_margin
#print axioms neutralIV099Sector_cutoff

end
end WeilDefect
