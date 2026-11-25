import WeilDefect.MasterRecon.V07A
import Mathlib.Analysis.InnerProductSpace.l2Space

/-! V07B: genuine Hilbert direct sums of uniformly bounded blocks.
No finite truncation, cardinality bound, or summability assumption on the
ordinate parameters is imposed. Concrete arithmetic blocks are separate. -/
namespace WeilDefect.MasterRecon.V07B

open scoped ENNReal InnerProduct

variable {ι : Type*} {K : ι → Type*}
variable [∀ i, NormedAddCommGroup (K i)] [∀ i, InnerProductSpace ℂ (K i)]

/-- A uniform coordinate operator bound implies square-summability. -/
theorem block_mem (B : ∀ i, K i →L[ℂ] K i) (c : ℝ) (hc : 0 ≤ c)
    (hB : ∀ i, ‖B i‖ ≤ c) (x : lp K 2) :
    Memℓp (fun i => B i (x i)) 2 := by
  have h : ∀ i, ‖B i (x i)‖ ≤ ‖(((c : ℂ) • x) : lp K 2) i‖ := by
    intro i
    calc
      ‖B i (x i)‖ ≤ ‖B i‖ * ‖x i‖ := (B i).le_opNorm _
      _ ≤ c * ‖x i‖ := mul_le_mul_of_nonneg_right (hB i) (norm_nonneg _)
      _ = ‖(((c : ℂ) • x) : lp K 2) i‖ := by
        simp [lp.coeFn_smul, Pi.smul_apply, norm_smul, Complex.norm_real,
          Real.norm_of_nonneg hc]
  exact (lp.memℓp ((c : ℂ) • x)).mono' h

/-- The bounded block diagonal operator on the entire Hilbert sum. -/
noncomputable def blockLift (B : ∀ i, K i →L[ℂ] K i) (c : ℝ) (hc : 0 ≤ c)
    (hB : ∀ i, ‖B i‖ ≤ c) : lp K 2 →L[ℂ] lp K 2 :=
  let L : lp K 2 →ₗ[ℂ] lp K 2 :=
    { toFun := fun x => ⟨fun i => B i (x i), block_mem B c hc hB x⟩
      map_add' := fun x y => by
        apply lp.ext
        funext i
        change B i (x i + y i) = B i (x i) + B i (y i)
        exact (B i).map_add _ _
      map_smul' := fun a x => by
        apply lp.ext
        funext i
        change B i (a • x i) = a • B i (x i)
        exact (B i).map_smul _ _ }
  L.mkContinuous c (fun x => by
    calc
      ‖L x‖ ≤ ‖(c : ℂ) • x‖ := by
        apply lp.norm_mono (by norm_num : (2 : ℝ≥0∞) ≠ 0)
        intro i
        change ‖B i (x i)‖ ≤ ‖(((c : ℂ) • x) : lp K 2) i‖
        calc
          ‖B i (x i)‖ ≤ ‖B i‖ * ‖x i‖ := (B i).le_opNorm _
          _ ≤ c * ‖x i‖ := mul_le_mul_of_nonneg_right (hB i) (norm_nonneg _)
          _ = _ := by
            simp [lp.coeFn_smul, Pi.smul_apply, norm_smul, Complex.norm_real,
              Real.norm_of_nonneg hc]
      _ = c * ‖x‖ := by rw [norm_smul, Complex.norm_real, Real.norm_of_nonneg hc])

theorem blockLift_apply (B : ∀ i, K i →L[ℂ] K i) (c : ℝ) (hc : 0 ≤ c)
    (hB : ∀ i, ‖B i‖ ≤ c) (x : lp K 2) (i : ι) :
    blockLift B c hc hB x i = B i (x i) := rfl

theorem blockLift_norm_le (B : ∀ i, K i →L[ℂ] K i) (c : ℝ) (hc : 0 ≤ c)
    (hB : ∀ i, ‖B i‖ ≤ c) :
    ‖blockLift B c hc hB‖ ≤ c := by
  apply ContinuousLinearMap.opNorm_le_bound _ hc
  intro x
  calc
    ‖blockLift B c hc hB x‖ ≤ ‖(c : ℂ) • x‖ := by
      apply lp.norm_mono (by norm_num : (2 : ℝ≥0∞) ≠ 0)
      intro i
      rw [blockLift_apply]
      calc
        ‖B i (x i)‖ ≤ ‖B i‖ * ‖x i‖ := (B i).le_opNorm _
        _ ≤ c * ‖x i‖ := mul_le_mul_of_nonneg_right (hB i) (norm_nonneg _)
        _ = _ := by
          simp [lp.coeFn_smul, Pi.smul_apply, norm_smul, Complex.norm_real,
            Real.norm_of_nonneg hc]
    _ = c * ‖x‖ := by rw [norm_smul, Complex.norm_real, Real.norm_of_nonneg hc]

/-- Blockwise phase cancellation gives the exact infinite-sum identity.
The local pairing identity is exposed, not derived from a finite truncation. -/
theorem block_pairing_transfer
    (B E F : ∀ i, K i →L[ℂ] K i)
    (b e f : ℝ) (hb : 0 ≤ b) (he : 0 ≤ e) (hf : 0 ≤ f)
    (hB : ∀ i, ‖B i‖ ≤ b) (hE : ∀ i, ‖E i‖ ≤ e)
    (hF : ∀ i, ‖F i‖ ≤ f)
    (h : ∀ i (x y : K i), inner ℂ (E i (B i x)) (B i y) =
      inner ℂ (F i x) y)
    (x y : lp K 2) :
    inner ℂ (blockLift E e he hE (blockLift B b hb hB x))
      (blockLift B b hb hB y) =
      inner ℂ (blockLift F f hf hF x) y := by
  rw [lp.inner_eq_tsum, lp.inner_eq_tsum]
  apply tsum_congr
  intro i
  simp only [blockLift_apply]
  exact h i (x i) (y i)

/-- Uniformly bounded, pointwise symmetric blocks retain symmetry
on the full direct sum. -/
theorem blockLift_symmetric
    (D : ∀ i, K i →L[ℂ] K i) (c : ℝ) (hc : 0 ≤ c)
    (hD : ∀ i, ‖D i‖ ≤ c)
    (hs : ∀ i (x y : K i), inner ℂ (D i x) y = inner ℂ x (D i y))
    (x y : lp K 2) :
    inner ℂ (blockLift D c hc hD x) y =
      inner ℂ x (blockLift D c hc hD y) := by
  rw [lp.inner_eq_tsum, lp.inner_eq_tsum]
  apply tsum_congr
  intro i
  simp only [blockLift_apply]
  exact hs i (x i) (y i)

end WeilDefect.MasterRecon.V07B

#print axioms WeilDefect.MasterRecon.V07B.block_mem
#print axioms WeilDefect.MasterRecon.V07B.blockLift_apply
#print axioms WeilDefect.MasterRecon.V07B.blockLift_norm_le
#print axioms WeilDefect.MasterRecon.V07B.block_pairing_transfer
#print axioms WeilDefect.MasterRecon.V07B.blockLift_symmetric
