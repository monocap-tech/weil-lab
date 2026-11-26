import WeilDefect.Arithmetic.ActualZetaIV106E15ResidualSchur

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct ComplexConjugate BigOperators

abbrev neutralIV106E16Index (k : ℕ) := neutralIV106C3Index 665 k

def neutralIV106E16TrialVector (k : ℕ) (hk : 0 < k)
    (t : neutralIV106E16Index k → neutralIV106E12Kernel k hk)
    (j : neutralIV106E16Index k) : neutralIV106E13H :=
  neutralIV106E14Row k hk j - (t j).val

def neutralIV106E16TrialGram (k : ℕ) (hk : 0 < k)
    (t : neutralIV106E16Index k → neutralIV106E12Kernel k hk)
    (i j : neutralIV106E16Index k) : ℂ :=
  inner ℂ (neutralIV106E16TrialVector k hk t i)
    (neutralActualZetaLogWeilFormOperator (11/10) (neutralIV106E16TrialVector k hk t j))

def neutralIV106E16ResidualGram (k : ℕ) (hk : 0 < k)
    (t : neutralIV106E16Index k → neutralIV106E12Kernel k hk)
    (i j : neutralIV106E16Index k) : ℂ :=
  inner ℂ (neutralIV106E15Residual k hk (neutralIV106E14LiftedRow k hk i) (t i))
    (neutralIV106E15Residual k hk (neutralIV106E14LiftedRow k hk j) (t j))

def neutralIV106E16Quadratic {J : Type*} [Fintype J]
    (M : J → J → ℂ) (c : J → ℂ) : ℝ :=
  (∑ i, ∑ j, conj (c i)*c j*M i j).re

/-- Synthesis preserves exact kernel membership by construction. -/
theorem neutralIV106E16Trial_synthesis (k : ℕ) (hk : 0 < k)
    (t : neutralIV106E16Index k → neutralIV106E12Kernel k hk)
    (c : neutralIV106E16Index k → ℂ) :
    (∑ j, c j • neutralIV106E14LiftedRow k hk j).val -
      (∑ j, c j • t j).val =
    ∑ j, c j • neutralIV106E16TrialVector k hk t j := by
  classical
  change (neutralIV106E13Finite k hk).subtypeL (∑ j, c j • neutralIV106E14LiftedRow k hk j) -
    (neutralIV106E12Kernel k hk).subtypeL (∑ j, c j • t j) = _
  simp only [map_sum, map_smul, neutralIV106E16TrialVector, smul_sub,
    Finset.sum_sub_distrib]
  rfl

/-- The projected residual is linear on the actual row and trial families. -/
theorem neutralIV106E16Residual_synthesis (k : ℕ) (hk : 0 < k)
    (t : neutralIV106E16Index k → neutralIV106E12Kernel k hk)
    (c : neutralIV106E16Index k → ℂ) :
    neutralIV106E15Residual k hk (∑ j, c j • neutralIV106E14LiftedRow k hk j)
      (∑ j, c j • t j) =
      ∑ j, c j • neutralIV106E15Residual k hk (neutralIV106E14LiftedRow k hk j) (t j) := by
  classical
  let B := (ContinuousLinearMap.adjoint (neutralIV106E12Kernel k hk).subtypeL) ∘L
    (neutralActualZetaLogWeilFormOperator (11/10)) ∘L (neutralIV106E13Finite k hk).subtypeL
  let A := neutralIV106E12Compressed k hk
  change B (∑ j, c j • neutralIV106E14LiftedRow k hk j) -
    A (∑ j, c j • t j) =
    ∑ j, c j • (B (neutralIV106E14LiftedRow k hk j) - A (t j))
  simp only [map_sum, map_smul, smul_sub, Finset.sum_sub_distrib]

theorem neutralIV106E16Trial_energy (k : ℕ) (hk : 0 < k)
    (t : neutralIV106E16Index k → neutralIV106E12Kernel k hk)
    (c : neutralIV106E16Index k → ℂ) :
    neutralIV106E13Energy ((∑ j, c j • neutralIV106E14LiftedRow k hk j).val -
      (∑ j, c j • t j).val) =
    neutralIV106E16Quadratic (neutralIV106E16TrialGram k hk t) c := by
  rw [neutralIV106E16Trial_synthesis]
  unfold neutralIV106E13Energy neutralIV106E16Quadratic neutralIV106E16TrialGram
  rw [neutralIV106E14Gram]

theorem neutralIV106E16Residual_energy (k : ℕ) (hk : 0 < k)
    (t : neutralIV106E16Index k → neutralIV106E12Kernel k hk)
    (c : neutralIV106E16Index k → ℂ) :
    ‖neutralIV106E15Residual k hk (∑ j, c j • neutralIV106E14LiftedRow k hk j)
      (∑ j, c j • t j)‖^2 =
    neutralIV106E16Quadratic (neutralIV106E16ResidualGram k hk t) c := by
  rw [neutralIV106E16Residual_synthesis]
  let r j := neutralIV106E15Residual k hk (neutralIV106E14LiftedRow k hk j) (t j)
  have h := neutralIV106E14Gram (ContinuousLinearMap.id ℂ (neutralIV106E12Kernel k hk)) r c
  have he := congrArg Complex.re h
  simp only [ContinuousLinearMap.id_apply] at he
  unfold neutralIV106E16Quadratic neutralIV106E16ResidualGram
  change ‖∑ j, c j • r j‖^2 = _
  rw [← he]
  rw [inner_self_eq_norm_sq_to_K, Complex.ofReal_re]

/-- Any redundant row representation is sufficient. No linear trial map
on the quotient of the row coordinates is assumed or needed. -/
theorem neutralIV106E16Matrix_receiver (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk)
    (t : neutralIV106E16Index k → neutralIV106E12Kernel k hk)
    (h : ∀ c : neutralIV106E16Index k → ℂ,
      neutralIV106E11Alpha⁻¹ * neutralIV106E16Quadratic
        (neutralIV106E16ResidualGram k hk t) c ≤
        neutralIV106E16Quadratic (neutralIV106E16TrialGram k hk t) c) :
    ∀ q : neutralIV106E13H, 0 ≤ neutralIV106E13Energy q := by
  apply (neutralIV106E13Nonnegative_iff k hk e he).mpr
  intro y
  obtain ⟨c,hc⟩ := neutralIV106E14Synthesis k hk y
  let z := ∑ j, c j • t j
  have hb := (neutralIV106E15Enclosure k hk e he
    (∑ j, c j • neutralIV106E14LiftedRow k hk j) z).1
  dsimp only [z] at hb
  rw [neutralIV106E16Trial_energy, neutralIV106E16Residual_energy, hc] at hb
  exact (sub_nonneg.mpr (h c)).trans hb

/-- Ordered enclosures may be supplied as separate trial and residual
quadratic bounds; the actual inverse need never be evaluated numerically. -/
theorem neutralIV106E16Interval_receiver (k : ℕ) (hk : 0 < k)
    (e : neutralIV106E12Kernel k hk ≃L[ℂ] neutralIV106E12Kernel k hk)
    (he : e.toContinuousLinearMap = neutralIV106E12Compressed k hk)
    (t : neutralIV106E16Index k → neutralIV106E12Kernel k hk)
    (L R : neutralIV106E16Index k → neutralIV106E16Index k → ℂ)
    (β : ℝ) (hβ : neutralIV106E11Alpha⁻¹ ≤ β)
    (hL : ∀ c, neutralIV106E16Quadratic L c ≤
      neutralIV106E16Quadratic (neutralIV106E16TrialGram k hk t) c)
    (hR : ∀ c, neutralIV106E16Quadratic
      (neutralIV106E16ResidualGram k hk t) c ≤ neutralIV106E16Quadratic R c)
    (hcert : ∀ c, β*neutralIV106E16Quadratic R c ≤ neutralIV106E16Quadratic L c) :
    ∀ q : neutralIV106E13H, 0 ≤ neutralIV106E13Energy q := by
  apply neutralIV106E16Matrix_receiver k hk e he t
  intro c
  have hr : 0 ≤ neutralIV106E16Quadratic (neutralIV106E16ResidualGram k hk t) c := by
    rw [← neutralIV106E16Residual_energy]
    positivity
  have hβ0 : 0 ≤ β := (inv_nonneg.mpr neutralIV106E11Alpha_pos.le).trans hβ
  calc
    _ ≤ β*neutralIV106E16Quadratic (neutralIV106E16ResidualGram k hk t) c :=
      mul_le_mul_of_nonneg_right hβ hr
    _ ≤ β*neutralIV106E16Quadratic R c := mul_le_mul_of_nonneg_left (hR c) hβ0
    _ ≤ neutralIV106E16Quadratic L c := hcert c
    _ ≤ _ := hL c

#print axioms neutralIV106E16Trial_synthesis
#print axioms neutralIV106E16Residual_synthesis
#print axioms neutralIV106E16Trial_energy
#print axioms neutralIV106E16Residual_energy
#print axioms neutralIV106E16Matrix_receiver
#print axioms neutralIV106E16Interval_receiver
end
end WeilDefect
