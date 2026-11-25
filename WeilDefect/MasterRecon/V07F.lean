import WeilDefect.MasterRecon.V07E

/-! V07F: bounded selected ordinate generator and exact forcing attachment.
The packet is a genuine finite subset of the full coefficient index.
No bound on ordinates outside that subset is required. -/
namespace WeilDefect.MasterRecon.V07F

open scoped ENNReal InnerProduct BigOperators
open V07C

variable {ι : Type*} [DecidableEq ι]

def clipped (s : Finset ι) (g : ι → ℝ) (i : ι) : ℝ :=
  if i ∈ s then g i else 0

noncomputable def packetBound (s : Finset ι) (g : ι → ℝ) : ℝ :=
  ∑ i ∈ s, |g i|

theorem packetBound_nonneg (s : Finset ι) (g : ι → ℝ) :
    0 ≤ packetBound s g := by
  unfold packetBound
  exact Finset.sum_nonneg (fun i _ => abs_nonneg (g i))

theorem clipped_bound (s : Finset ι) (g : ι → ℝ) (i : ι) :
    |clipped s g i| ≤ packetBound s g := by
  by_cases hi : i ∈ s
  · rw [clipped, if_pos hi]
    exact Finset.single_le_sum (fun j _ => abs_nonneg (g j)) hi
  · rw [clipped, if_neg hi, abs_zero]
    exact packetBound_nonneg s g

theorem scalarBlock_norm_le (q : ℂ) : ‖phaseBlock q‖ ≤ ‖q‖ := by
  apply ContinuousLinearMap.opNorm_le_bound _ (norm_nonneg q)
  intro x
  rw [phaseBlock_apply, norm_smul]

noncomputable def selectedGenerator (s : Finset ι) (g : ι → ℝ) :
    Coeff ι →L[ℂ] Coeff ι :=
  V07B.blockLift (fun i => phaseBlock (clipped s g i : ℂ))
    (packetBound s g) (packetBound_nonneg s g)
    (fun i => (scalarBlock_norm_le _).trans (by
      rw [Complex.norm_real, Real.norm_eq_abs]
      exact clipped_bound s g i))

theorem selectedGenerator_norm (s : Finset ι) (g : ι → ℝ) :
    ‖selectedGenerator s g‖ ≤ packetBound s g :=
  V07B.blockLift_norm_le _ _ _ _

theorem selectedGenerator_apply (s : Finset ι) (g : ι → ℝ)
    (x : Coeff ι) (i : ι) :
    selectedGenerator s g x i = (clipped s g i : ℂ) • x i := rfl

theorem pair_scalar_exp (w : ℂ) (x : Pair) :
    NormedSpace.exp (w • (1 : Pair →L[ℂ] Pair)) x =
      Complex.exp w • x := by
  have h := NormedSpace.algebraMap_exp_comm (𝕂 := ℂ) (𝔸 := Pair →L[ℂ] Pair) w
  rw [Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one] at h
  rw [← h, ← Complex.exp_eq_exp_ℂ]
  rfl

theorem selected_exp_coordinate (s : Finset ι) (g : ι → ℝ)
    (z : ℂ) (x : Coeff ι) (i : ι) :
    NormedSpace.exp (z • selectedGenerator s g) x i =
      Complex.exp (z * (clipped s g i : ℂ)) • x i := by
  let L : Coeff ι →L[ℂ] Pair := lp.evalCLM ℂ (fun _ : ι => Pair) 2 i
  have h : ∀ y : Coeff ι, L ((z • selectedGenerator s g) y) =
      ((z * (clipped s g i : ℂ)) • (1 : Pair →L[ℂ] Pair)) (L y) := by
    intro y
    change z • selectedGenerator s g y i = (z * (clipped s g i : ℂ)) • y i
    rw [selectedGenerator_apply, mul_smul]
  have he := V07D.exp_intertwine L _ _ h x
  change NormedSpace.exp (z • selectedGenerator s g) x i =
    NormedSpace.exp ((z * (clipped s g i : ℂ)) • (1 : Pair →L[ℂ] Pair)) (x i) at he
  rw [he, pair_scalar_exp]

theorem selected_phase (s : Finset ι) (g : ι → ℝ) (a : ℝ)
    (v : Coeff ι) (hv : ∀ i, i ∉ s → v i = 0) :
    NormedSpace.exp (((a : ℂ) * Complex.I) • selectedGenerator s g) v =
      phase g a v := by
  apply lp.ext
  funext i
  change NormedSpace.exp (((a : ℂ) * Complex.I) • selectedGenerator s g) v i =
    phase g a v i
  rw [selected_exp_coordinate, V07E.phase_apply]
  by_cases hi : i ∈ s
  · rw [clipped, if_pos hi]
    unfold ordinatePhase
    have he : (a : ℂ) * Complex.I * (g i : ℂ) =
        (g i : ℂ) * Complex.I * (a : ℂ) := by ring
    rw [he]
  · rw [hv i hi, smul_zero, smul_zero]

theorem phase_adjoint_pairing (g : ι → ℝ) (a : ℝ) (v x : Coeff ι) :
    inner ℂ (phase g a v) x = inner ℂ v (phase g (-a) x) := by
  rw [lp.inner_eq_tsum, lp.inner_eq_tsum]
  apply tsum_congr
  intro i
  rw [V07E.phase_apply, V07E.phase_apply, inner_smul_left, inner_smul_right]
  have h : (starRingEnd ℂ) (ordinatePhase (g i) a) =
      ordinatePhase (g i) (-a) := by
    unfold ordinatePhase
    rw [← Complex.exp_conj]
    congr 1
    simp [map_mul]
  rw [h]

variable {H : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

/-- The finite selected load is exactly the V06B forcing for every real
translation parameter, without analyticity of the full ordinate phase. -/
theorem selected_forcing_pairing (A : H →L[ℂ] Coeff ι)
    (s : Finset ι) (d g : ι → ℝ) (hd : ∀ i, |d i| ≤ 1 / 2)
    (v : Coeff ι) (hv : ∀ i, i ∉ s → v i = 0) (a : ℝ) (x : H) :
    inner ℂ (V06B.selectedForcing A (displacement d hd)
      (selectedGenerator s g) v (a : ℂ)) x =
      inner ℂ v (phase g (-a)
        (NormedSpace.exp ((-(a : ℂ)) • displacement d hd) (A x))) := by
  unfold V06B.selectedForcing
  rw [selected_phase s g a v hv, ContinuousLinearMap.adjoint_inner_left]
  let B := NormedSpace.exp ((-(a : ℂ)) • displacement d hd)
  change inner ℂ (B (phase g a v)) (A x) =
    inner ℂ v (phase g (-a) (B (A x)))
  have hB : B.adjoint = B := by
    unfold B
    rw [← Complex.ofReal_neg]
    exact V07E.real_exp_selfAdjoint _ (displacement_selfAdjoint d hd) (-a)
  rw [← hB, ContinuousLinearMap.adjoint_inner_left, hB]
  exact phase_adjoint_pairing g a v (B (A x))

end WeilDefect.MasterRecon.V07F

#print axioms WeilDefect.MasterRecon.V07F.packetBound_nonneg
#print axioms WeilDefect.MasterRecon.V07F.clipped_bound
#print axioms WeilDefect.MasterRecon.V07F.scalarBlock_norm_le
#print axioms WeilDefect.MasterRecon.V07F.selectedGenerator_norm
#print axioms WeilDefect.MasterRecon.V07F.selectedGenerator_apply
#print axioms WeilDefect.MasterRecon.V07F.pair_scalar_exp
#print axioms WeilDefect.MasterRecon.V07F.selected_exp_coordinate
#print axioms WeilDefect.MasterRecon.V07F.selected_phase
#print axioms WeilDefect.MasterRecon.V07F.phase_adjoint_pairing
#print axioms WeilDefect.MasterRecon.V07F.selected_forcing_pairing
