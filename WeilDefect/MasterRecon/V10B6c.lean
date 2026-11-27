import WeilDefect.MasterRecon.V10B6b

/-! V10B6c: contractive channel projections on the entire Hilbert
coefficient space and the signed Gram receiver. The orbit-indexed
arithmetic diagonal is attached in V10B6d, not assumed here. -/
namespace WeilDefect.MasterRecon.V10B6c

open scoped ENNReal InnerProduct BigOperators

variable {ι : Type*}

def channel (positive : Bool) (v : V07C.Pair) : ℂ :=
  if positive then (WithLp.ofLp v).1 else (WithLp.ofLp v).2

theorem channel_sq_le (positive : Bool) (v : V07C.Pair) :
    ‖channel positive v‖^2 ≤ ‖v‖^2 := by
  rw [V10B6a.pair_norm_sq]
  cases positive <;> simp only [channel, Bool.false_eq_true, if_false, if_true] <;>
    nlinarith [sq_nonneg ‖(WithLp.ofLp v).1‖, sq_nonneg ‖(WithLp.ofLp v).2‖]

theorem channel_add (positive : Bool) (v w : V07C.Pair) :
    channel positive (v+w) = channel positive v + channel positive w := by
  cases positive <;> rfl

theorem channel_smul (positive : Bool) (a : ℂ) (v : V07C.Pair) :
    channel positive (a • v) = a • channel positive v := by
  cases positive <;> rfl

theorem channel_finite_budget (positive : Bool) (x : V07C.Coeff ι)
    (S : Finset ι) :
    (∑ i ∈ S, ‖channel positive (x i)‖^2) ≤ ‖x‖^2 := by
  calc
    _ ≤ ∑ i ∈ S, ‖x i‖^2 := Finset.sum_le_sum (fun i _ => channel_sq_le positive (x i))
    _ ≤ _ := by
      simpa only [ENNReal.toReal_ofNat, Real.rpow_natCast] using
        (lp.sum_rpow_le_norm_rpow (by norm_num : 0 < (2 : ℝ≥0∞).toReal) x S)

noncomputable def channelValue (positive : Bool) (x : V07C.Coeff ι) :
    V09E.PositiveCoeff ι :=
  ⟨fun i => channel positive (x i),
    V10B6a.lp_two_mem_of_budget _ _ (channel_finite_budget positive x)⟩

theorem channelValue_apply (positive : Bool) (x : V07C.Coeff ι) (i : ι) :
    channelValue positive x i = channel positive (x i) := rfl

theorem channelValue_bound (positive : Bool) (x : V07C.Coeff ι) :
    ‖channelValue positive x‖ ≤ ‖x‖ := by
  have h := V10B6a.lp_two_norm_sq_le_of_budget (channelValue positive x)
    (‖x‖^2) (channel_finite_budget positive x)
  exact le_of_sq_le_sq h (norm_nonneg _)

noncomputable def projection (positive : Bool) :
    V07C.Coeff ι →L[ℂ] V09E.PositiveCoeff ι :=
  ({ toFun := channelValue positive
     map_add' := fun x y => by
       apply lp.ext
       funext i
       exact channel_add positive (x i) (y i)
     map_smul' := fun a x => by
       apply lp.ext
       funext i
       exact channel_smul positive a (x i) } :
       V07C.Coeff ι →ₗ[ℂ] V09E.PositiveCoeff ι).mkContinuous 1
       (fun x => by simpa only [one_mul] using channelValue_bound positive x)

theorem projection_apply (positive : Bool) (x : V07C.Coeff ι) (i : ι) :
    projection positive x i = channel positive (x i) := rfl

theorem projection_norm_le (positive : Bool) :
    ‖(projection positive : V07C.Coeff ι →L[ℂ] V09E.PositiveCoeff ι)‖ ≤ 1 := by
  apply ContinuousLinearMap.opNorm_le_bound _ zero_le_one
  intro x
  simpa only [one_mul] using channelValue_bound positive x

theorem channel_energy_split (x : V07C.Coeff ι) :
    ‖projection true x‖^2 + ‖projection false x‖^2 = ‖x‖^2 := by
  have hp := (lp.memℓp (projection true x)).summable (by norm_num : 0 < (2 : ℝ≥0∞).toReal)
  have hm := (lp.memℓp (projection false x)).summable (by norm_num : 0 < (2 : ℝ≥0∞).toReal)
  have hp' : Summable (fun i => ‖projection true x i‖^2) := by
    simpa only [ENNReal.toReal_ofNat, Real.rpow_natCast] using hp
  have hm' : Summable (fun i => ‖projection false x i‖^2) := by
    simpa only [ENNReal.toReal_ofNat, Real.rpow_natCast] using hm
  rw [V10B6a.lp_two_norm_sq, V10B6a.lp_two_norm_sq, V10B6a.lp_two_norm_sq,
    ← hp'.tsum_add hm']
  apply tsum_congr
  intro i
  rw [projection_apply, projection_apply, V10B6a.pair_norm_sq]
  rfl

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]

noncomputable def analysisChannel (positive : Bool) (T : H →L[ℂ] V07C.Coeff ι) :
    H →L[ℂ] V09E.PositiveCoeff ι :=
  (projection positive).comp T

theorem analysisChannel_apply (positive : Bool) (T : H →L[ℂ] V07C.Coeff ι)
    (g : H) (i : ι) :
    analysisChannel positive T g i = channel positive (T g i) := rfl

theorem analysisChannel_norm_le (positive : Bool) (T : H →L[ℂ] V07C.Coeff ι) :
    ‖analysisChannel positive T‖ ≤ ‖T‖ := by
  apply ContinuousLinearMap.opNorm_le_bound _ (norm_nonneg T)
  intro g
  exact (channelValue_bound positive (T g)).trans (T.le_opNorm g)

noncomputable def signedGram (T : H →L[ℂ] V07C.Coeff ι) : H →L[ℂ] H :=
  (analysisChannel true T).adjoint ∘L (analysisChannel true T) -
    (analysisChannel false T).adjoint ∘L (analysisChannel false T)

theorem signedGram_pairing (T : H →L[ℂ] V07C.Coeff ι) (g h : H) :
    inner ℂ (signedGram T g) h =
      inner ℂ (analysisChannel true T g) (analysisChannel true T h) -
      inner ℂ (analysisChannel false T g) (analysisChannel false T h) := by
  unfold signedGram
  simp only [ContinuousLinearMap.sub_apply, ContinuousLinearMap.comp_apply,
    inner_sub_left, ContinuousLinearMap.adjoint_inner_left]

theorem signedGram_diagonal (T : H →L[ℂ] V07C.Coeff ι) (g : H) :
    (inner ℂ (signedGram T g) g).re =
      ‖analysisChannel true T g‖^2 - ‖analysisChannel false T g‖^2 := by
  rw [signedGram_pairing, inner_self_eq_norm_sq_to_K, inner_self_eq_norm_sq_to_K]
  simp

theorem signedGram_symmetric (T : H →L[ℂ] V07C.Coeff ι) :
    (signedGram T).adjoint = signedGram T := by
  unfold signedGram
  simp [ContinuousLinearMap.adjoint_comp]

end WeilDefect.MasterRecon.V10B6c

#print axioms WeilDefect.MasterRecon.V10B6c.channel_sq_le
#print axioms WeilDefect.MasterRecon.V10B6c.channel_add
#print axioms WeilDefect.MasterRecon.V10B6c.channel_smul
#print axioms WeilDefect.MasterRecon.V10B6c.channel_finite_budget
#print axioms WeilDefect.MasterRecon.V10B6c.channelValue_apply
#print axioms WeilDefect.MasterRecon.V10B6c.channelValue_bound
#print axioms WeilDefect.MasterRecon.V10B6c.projection_apply
#print axioms WeilDefect.MasterRecon.V10B6c.projection_norm_le
#print axioms WeilDefect.MasterRecon.V10B6c.channel_energy_split
#print axioms WeilDefect.MasterRecon.V10B6c.analysisChannel_apply
#print axioms WeilDefect.MasterRecon.V10B6c.analysisChannel_norm_le
#print axioms WeilDefect.MasterRecon.V10B6c.signedGram_pairing
#print axioms WeilDefect.MasterRecon.V10B6c.signedGram_diagonal
#print axioms WeilDefect.MasterRecon.V10B6c.signedGram_symmetric
