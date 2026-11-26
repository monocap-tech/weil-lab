import WeilDefect.Arithmetic.ActualZetaIV102OriginalSchwartzMetricTransport
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- The original physical Gram is diagonal by the pointwise disjointness
of the actual IV100 carriers, not a change to a weighted metric. -/
theorem neutralIV104Carrier_orthogonal (k : ℕ) (hk : 0 < k)
    (i j : Fin k) (hij : i ≠ j) :
    inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
      ((neutralIV100Carrier k hk j).toLp 2 volume) = 0 := by
  rw [MeasureTheory.L2.inner_def]
  calc
    _ = ∫ x : ℝ, (0 : ℂ) := by
      apply integral_congr_ae
      filter_upwards [(neutralIV100Carrier k hk i).coeFn_toLp 2 volume,
        (neutralIV100Carrier k hk j).coeFn_toLp 2 volume] with x hi hj
      rw [hi, hj]
      rcases neutralIV100Carrier_disjoint k hk i (Finset.mem_univ i)
        j (Finset.mem_univ j) hij x with h | h
      · simp [h]
      · simp [h]
    _ = 0 := by simp

def neutralIV104Mass (k : ℕ) (hk : 0 < k) (i : Fin k) : ℝ :=
  ‖(neutralIV100Carrier k hk i).toLp 2 volume‖^2

def neutralIV104Coefficient (k : ℕ) (hk : 0 < k)
    (s : 𝓢(ℝ,ℂ)) (i : Fin k) : ℂ :=
  inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume) (s.toLp 2 volume) /
    (neutralIV104Mass k hk i : ℂ)

def neutralIV104Project (k : ℕ) (hk : 0 < k) (s : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  neutralIV100Packed k hk (neutralIV104Coefficient k hk s)

def neutralIV104Residual (k : ℕ) (hk : 0 < k) (s : 𝓢(ℝ,ℂ)) : 𝓢(ℝ,ℂ) :=
  s - neutralIV104Project k hk s

theorem neutralIV104Packed_toLp (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) :
    (neutralIV100Packed k hk c).toLp 2 volume =
      ∑ i : Fin k, c i • (neutralIV100Carrier k hk i).toLp 2 volume := by
  change (SchwartzMap.toLpCLM ℂ ℂ 2 volume)
    (∑ i : Fin k, c i • neutralIV100Carrier k hk i) =
      ∑ i : Fin k, c i •
        (SchwartzMap.toLpCLM ℂ ℂ 2 volume) (neutralIV100Carrier k hk i)
  simp only [map_sum, map_smul]

theorem neutralIV104Packed_pair (k : ℕ) (hk : 0 < k)
    (c : Fin k → ℂ) (i : Fin k) :
    inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
      ((neutralIV100Packed k hk c).toLp 2 volume) =
      c i * (neutralIV104Mass k hk i : ℂ) := by
  classical
  rw [neutralIV104Packed_toLp]
  simp only [inner_sum, inner_smul_right]
  rw [Finset.sum_eq_single i]
  · rw [inner_self_eq_norm_sq_to_K]
    simp only [neutralIV104Mass, Complex.ofReal_pow]
    <;> first
      | rfl
      | congr 1
        <;> first | rfl | norm_cast | push_cast <;> rfl
      | change c i * ((‖(neutralIV100Carrier k hk i).toLp 2 volume‖ : ℝ) : ℂ)^2 =
          c i * ((‖(neutralIV100Carrier k hk i).toLp 2 volume‖ : ℝ) : ℂ)^2
        rfl
  · intro j hj hji
    rw [neutralIV104Carrier_orthogonal k hk i j (Ne.symm hji), mul_zero]
  · simp

theorem neutralIV104Project_pair (k : ℕ) (hk : 0 < k)
    (s : 𝓢(ℝ,ℂ)) (i : Fin k) :
    inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
      ((neutralIV104Project k hk s).toLp 2 volume) =
      inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
        (s.toLp 2 volume) := by
  unfold neutralIV104Project
  rw [neutralIV104Packed_pair]
  unfold neutralIV104Coefficient
  have hm : 0 < neutralIV104Mass k hk i := neutralIV100Carrier_mass_pos k hk i
  exact div_mul_cancel₀ _ (Complex.ofReal_ne_zero.mpr hm.ne')

theorem neutralIV104Residual_toLp (k : ℕ) (hk : 0 < k) (s : 𝓢(ℝ,ℂ)) :
    (neutralIV104Residual k hk s).toLp 2 volume =
      s.toLp 2 volume - (neutralIV104Project k hk s).toLp 2 volume := by
  change (SchwartzMap.toLpCLM ℂ ℂ 2 volume) (s - neutralIV104Project k hk s) =
    (SchwartzMap.toLpCLM ℂ ℂ 2 volume) s -
      (SchwartzMap.toLpCLM ℂ ℂ 2 volume) (neutralIV104Project k hk s)
  exact map_sub _ _ _

theorem neutralIV104Residual_orthogonal (k : ℕ) (hk : 0 < k)
    (s : 𝓢(ℝ,ℂ)) : neutralIV101MassComplement k hk (neutralIV104Residual k hk s) := by
  intro c
  rw [neutralIV104Packed_toLp, sum_inner]
  apply Finset.sum_eq_zero
  intro i hi
  rw [inner_smul_left, neutralIV104Residual_toLp, inner_sub_right,
    neutralIV104Project_pair, sub_self, mul_zero]

theorem neutralIV104Residual_supported (k : ℕ) (hk : 0 < k)
    (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0) :
    ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
      neutralIV104Residual k hk s x = 0 := by
  intro x hx
  have hp := neutralIV009OriginalCollars_supported_window
    (neutralIV104Project k hk s)
    (neutralIV101Packed_collars k hk (neutralIV104Coefficient k hk s))
    x hx
  change s x - neutralIV104Project k hk s x = 0
  rw [hs x hx, hp, sub_zero]

theorem neutralIV104Decomposition (k : ℕ) (hk : 0 < k) (s : 𝓢(ℝ,ℂ)) :
    neutralIV104Project k hk s + neutralIV104Residual k hk s = s := by
  unfold neutralIV104Residual
  abel

/-- Every smooth test in the original window has a decomposition of the
precise type required by IV101. The two analytic inequalities are still
explicitly required, not inferred from physical orthogonality. -/
theorem neutralIV104Window_nonneg_of_complement (k : ℕ) (hk : 0 < k) (K : ℝ)
    (hmix : ∀ (c : Fin k → ℂ) (v : 𝓢(ℝ,ℂ)),
      neutralIV101MassComplement k hk v →
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) →
      |(neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk c) v).re| ≤
        K * ‖(neutralIV100Packed k hk c).toLp 2 volume‖ * ‖v.toLp 2 volume‖)
    (hcomp : ∀ v : 𝓢(ℝ,ℂ), neutralIV101MassComplement k hk v →
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) →
      (5/2:ℝ)*K^2*‖v.toLp 2 volume‖^2 ≤ neutralIV101Q (11/10:ℝ) v)
    (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → s x = 0) :
    0 ≤ neutralIV101Q (11/10:ℝ) s := by
  have h := neutralIV101Packed_complement_nonneg k hk K hmix hcomp
    (neutralIV104Coefficient k hk s) (neutralIV104Residual k hk s)
    (neutralIV104Residual_orthogonal k hk s)
    (neutralIV104Residual_supported k hk s hs)
  change 0 ≤ neutralIV101Q (11/10:ℝ)
    (neutralIV104Project k hk s + neutralIV104Residual k hk s) at h
  simpa only [neutralIV104Decomposition] using h

#print axioms neutralIV104Carrier_orthogonal
#print axioms neutralIV104Packed_toLp
#print axioms neutralIV104Packed_pair
#print axioms neutralIV104Project_pair
#print axioms neutralIV104Residual_toLp
#print axioms neutralIV104Residual_orthogonal
#print axioms neutralIV104Residual_supported
#print axioms neutralIV104Decomposition
#print axioms neutralIV104Window_nonneg_of_complement

end
end WeilDefect
