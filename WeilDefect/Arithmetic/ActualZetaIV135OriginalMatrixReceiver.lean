import WeilDefect.Arithmetic.ActualZetaIV134OriginalConstraintRows
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- Finite right-slot synthesis of the actual corrected form. -/
theorem neutralIV135Mixed_sum_right {n : ℕ} (k : ℕ) (hk : 0 < k)
    (u : 𝓢(ℝ,ℂ)) (w : Fin n → 𝓢(ℝ,ℂ)) (c : Fin n → ℂ)
    (hw : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → w i x = 0) :
    neutralIV130Mixed k hk u (neutralIV009PhysicalSchwartzSum w c) =
      ∑ i : Fin n, neutralIV130Mixed k hk u (w i)*c i := by
  rw [neutralIV130Mixed_row k hk u _
    (neutralIV009PhysicalSchwartzSum_supported _ w c hw),
    neutralIV107Mixed_sum_right _ w c _ hw]
  apply Finset.sum_congr rfl
  intro i hi
  rw [neutralIV130Mixed_row k hk u (w i) (hw i)]

/-- Finite left-slot synthesis by corrected Hermitian symmetry. -/
theorem neutralIV135Mixed_sum_left {n : ℕ} (k : ℕ) (hk : 0 < k)
    (u : 𝓢(ℝ,ℂ)) (w : Fin n → 𝓢(ℝ,ℂ)) (c : Fin n → ℂ)
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → u x = 0)
    (hw : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → w i x = 0) :
    neutralIV130Mixed k hk (neutralIV009PhysicalSchwartzSum w c) u =
      ∑ i : Fin n, conj (c i)*neutralIV130Mixed k hk (w i) u := by
  rw [← neutralIV132Mixed_hermitian k hk u _ hu
      (neutralIV009PhysicalSchwartzSum_supported _ w c hw),
    neutralIV135Mixed_sum_right k hk u w c hw]
  change conj (∑ i : Fin n, neutralIV130Mixed k hk u (w i)*c i) = _
  rw [map_sum]
  apply Finset.sum_congr rfl
  intro i hi
  rw [map_mul]
  have hs := neutralIV132Mixed_hermitian k hk u (w i) hu (hw i)
  change conj (neutralIV130Mixed k hk u (w i)) = _ at hs
  rw [hs]
  ring

def neutralIV135TrialGram {n : ℕ} (k : ℕ) (hk : 0 < k)
    (w : Fin n → 𝓢(ℝ,ℂ)) : Matrix (Fin n) (Fin n) ℂ :=
  fun i j => neutralIV130Mixed k hk (w i) (w j)

theorem neutralIV135TrialGram_energy {n : ℕ} (k : ℕ) (hk : 0 < k)
    (w : Fin n → 𝓢(ℝ,ℂ)) (c : Fin n → ℂ)
    (hw : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → w i x = 0) :
    neutralIV107SchurEnergy k hk (neutralIV009PhysicalSchwartzSum w c) =
      (∑ i : Fin n, conj (c i)*(neutralIV135TrialGram k hk w).mulVec c i).re := by
  rw [← neutralIV130Mixed_diagonal]
  congr 1
  rw [neutralIV135Mixed_sum_left k hk _ w c
    (neutralIV009PhysicalSchwartzSum_supported _ w c hw) hw]
  apply Finset.sum_congr rfl
  intro i hi
  rw [neutralIV135Mixed_sum_right k hk (w i) w c hw]
  rfl

/-- Subtract concrete cell and packed constraint rows, separately for
each column of the trial-lifted head. -/
def neutralIV135Residual {n : ℕ} (k : ℕ) (hk : 0 < k) (N : ℕ)
    (w : Fin n → 𝓢(ℝ,ℂ)) (D : Fin n → Fin N → ℂ)
    (P : Fin n → Fin k → ℂ) (i : Fin n) : RealComplexL2 :=
  neutralIV133CorrectedRow k hk (w i) -
    neutralIV134ConstraintSynthesis k hk N (D i) (P i)

/-- The summed physical row represents the actual mixed interaction on
the whole tail; no full-space equality of row synthesis is necessary. -/
theorem neutralIV135Residual_pair {n : ℕ} (k : ℕ) (hk : 0 < k) (N : ℕ)
    (w : Fin n → 𝓢(ℝ,ℂ)) (D : Fin n → Fin N → ℂ)
    (P : Fin n → Fin k → ℂ) (c : Fin n → ℂ)
    (hw : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → w i x = 0)
    (z : neutralIV131Tail k hk N) :
    inner ℂ (∑ i : Fin n, c i • neutralIV135Residual k hk N w D P i)
      (z.val.toLp 2 volume) =
      neutralIV130Mixed k hk (neutralIV009PhysicalSchwartzSum w c) z.val := by
  rw [sum_inner, neutralIV135Mixed_sum_left k hk z.val w c
    (neutralIV132Tail_supported k hk N z) hw]
  apply Finset.sum_congr rfl
  intro i hi
  rw [inner_smul_left]
  unfold neutralIV135Residual
  rw [inner_sub_left, neutralIV133CorrectedRow_pair k hk (w i) z.val
    (hw i) (neutralIV132Tail_supported k hk N z),
    neutralIV134Synthesis_annihilates k hk N (D i) (P i) z, sub_zero]

/-- Sufficient terminal matrix test for every fibre of the trial-lifted
finite head. The matrices are literal signed energy and residual Gram. -/
theorem neutralIV135Matrix_fibre {n : ℕ} (k : ℕ) (hk : 0 < k) (N : ℕ)
    (w : Fin n → 𝓢(ℝ,ℂ)) (D : Fin n → Fin N → ℂ)
    (P : Fin n → Fin k → ℂ)
    (hw : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → w i x = 0)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : neutralIV131Tail k hk N,
      eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val)
    (hm : ∀ c : Fin n → ℂ,
      (∑ i : Fin n, conj (c i)*
        (neutralIV134ResidualGram (neutralIV135Residual k hk N w D P)).mulVec c i).re/eta ≤
      (∑ i : Fin n, conj (c i)*(neutralIV135TrialGram k hk w).mulVec c i).re)
    (c : Fin n → ℂ) (z : neutralIV131Tail k hk N) :
    0 ≤ neutralIV107SchurEnergy k hk (neutralIV009PhysicalSchwartzSum w c+z.val) := by
  let h := neutralIV009PhysicalSchwartzSum w c
  let r : RealComplexL2 := ∑ i : Fin n, c i • neutralIV135Residual k hk N w D P i
  have hp := hm c
  rw [neutralIV134ResidualGram_energy, ← neutralIV135TrialGram_energy k hk w c hw] at hp
  change ‖r‖^2/eta ≤ neutralIV107SchurEnergy k hk h at hp
  have hb := norm_inner_le_norm (𝕜 := ℂ) r (z.val.toLp 2 volume)
  rw [show inner ℂ r (z.val.toLp 2 volume) = neutralIV130Mixed k hk h z.val
    from neutralIV135Residual_pair k hk N w D P c hw z] at hb
  have hb' := (neg_le_abs (neutralIV130Mixed k hk h z.val).re).trans
    ((Complex.abs_re_le_norm _).trans hb)
  have hl := neutralIV131Scalar_payment eta ‖r‖ ‖z.val.toLp 2 volume‖
    (neutralIV130Mixed k hk h z.val).re (neutralIV107SchurEnergy k hk z.val)
    he hb' (hc z)
  rw [neutralIV130Schur_add k hk _ _
    (neutralIV009PhysicalSchwartzSum_supported _ w c hw)
    (neutralIV132Tail_supported k hk N z)]
  linarith only [hp,hl]

/-- Original-window receiver, with explicit coverage of the actual
packed complement modulo its actual coercive tail. -/
theorem neutralIV135Window_of_matrix {n : ℕ} (k : ℕ) (hk : 0 < k) (N : ℕ)
    (w : Fin n → 𝓢(ℝ,ℂ)) (D : Fin n → Fin N → ℂ)
    (P : Fin n → Fin k → ℂ)
    (hw : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → w i x = 0)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : neutralIV131Tail k hk N,
      eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val)
    (hcover : ∀ v : neutralIV129Complement k hk,
      ∃ c : Fin n → ℂ, ∃ z : neutralIV131Tail k hk N,
        v.val = neutralIV009PhysicalSchwartzSum w c+z.val)
    (hm : ∀ c : Fin n → ℂ,
      (∑ i : Fin n, conj (c i)*
        (neutralIV134ResidualGram (neutralIV135Residual k hk N w D P)).mulVec c i).re/eta ≤
      (∑ i : Fin n, conj (c i)*(neutralIV135TrialGram k hk w).mulVec c i).re)
    (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0) :
    0 ≤ neutralIV101Q (11/10:ℝ) s := by
  apply neutralIV107Window_nonneg_of_schur k hk _ s hs
  intro v horth hv
  obtain ⟨c,z,hv'⟩ := hcover ⟨v,hv,horth⟩
  change v = _ at hv'
  rw [hv']
  exact neutralIV135Matrix_fibre k hk N w D P hw eta he hc hm c z

#print axioms neutralIV135Mixed_sum_right
#print axioms neutralIV135Mixed_sum_left
#print axioms neutralIV135TrialGram_energy
#print axioms neutralIV135Residual_pair
#print axioms neutralIV135Matrix_fibre
#print axioms neutralIV135Window_of_matrix

end
end WeilDefect
