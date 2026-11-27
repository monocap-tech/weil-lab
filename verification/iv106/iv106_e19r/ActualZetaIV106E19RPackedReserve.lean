import WeilDefect.Arithmetic.ActualZetaIV106E19QJointRowError
import WeilDefect.Arithmetic.ActualZetaIV106E18MPlateauMass

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap Set
open scoped BigOperators InnerProduct SchwartzMap

/-- The original choice-defined plateau is at most one, since it
integrates a nonnegative normalized bump over a subinterval. -/
theorem neutralIV106E19RPlateau_le (x : ℝ) :
    neutralIV097Plateau x ≤ 1 := by
  unfold neutralIV097Plateau
  rw [intervalIntegral.integral_of_le (by linarith),
    ← integral_Icc_eq_integral_Ioc, ← integral_indicator measurableSet_Icc]
  rw [← show (∫ t, neutralIV097Rho t) = 1 from neutralIV097Bump.integral_normed]
  have hi : Integrable neutralIV097Rho volume := neutralIV097Bump.integrable_normed
  apply integral_mono_ae (hi.indicator measurableSet_Icc) hi
  filter_upwards [] with t
  by_cases ht : t ∈ Icc (x-1099/1000-1/2000) (x-1099/1000+1/2000)
  · simp [ht]
  · simpa [ht] using (neutralIV097Rho_bounds t).1

/-- Exact L1 mass controls the actual L2 mass, without choosing a new
bump or assigning a numerical value to the original bump. -/
theorem neutralIV106E19RPacked_mass (k : ℕ) (hk : 0 < k) (i : Fin k) :
    ‖(neutralIV100Carrier k hk i).toLp 2 volume‖^2 ≤ 1/(1000*(k:ℝ)) := by
  rw [← neutralIV098Mass_integral,← neutralIV106E18MProfile_mass k hk i]
  have hi : Integrable (neutralIV106E18MProfile k i) :=
    (neutralIV097Plateau_smooth.continuous.comp
      (show Continuous (fun x : ℝ => (k:ℝ)*x+neutralIV100PackShift k i.val) by fun_prop))
      .integrable_of_hasCompactSupport (neutralIV106E18MProfile_compact k hk i)
  have hm := (memLp_two_iff_integrable_sq_norm
    (neutralIV100Carrier k hk i).continuous.aestronglyMeasurable).mp
    ((neutralIV100Carrier k hk i).memLp 2 volume)
  apply integral_mono_ae hm hi
  filter_upwards [] with x
  rw [neutralIV106E18MCarrier_real,Complex.norm_real,Real.norm_eq_abs,
    abs_of_nonneg (neutralIV106E18MProfile_nonneg k i x)]
  have h0 := neutralIV106E18MProfile_nonneg k i x
  have h1 : neutralIV106E18MProfile k i x ≤ 1 :=
    neutralIV106E19RPlateau_le _
  nlinarith [mul_nonneg h0 (sub_nonneg.mpr h1)]

/-- The full packed column synthesis has this squared norm reserve.
Distinct literal IV100 carriers, not substitute profiles, are disjoint. -/
theorem neutralIV106E19RPacked_joint (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) :
    ‖(neutralIV100Packed k hk c).toLp 2 volume‖^2 ≤
      (1/(1000*(k:ℝ))) * ∑ i, ‖c i‖^2 := by
  unfold neutralIV100Packed
  rw [neutralIV099Sector_mass _ _ _ (neutralIV100Carrier_disjoint k hk),Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  rw [mul_comm (1/(1000*(k:ℝ)))]
  exact mul_le_mul_of_nonneg_left (neutralIV106E19RPacked_mass k hk i) (sq_nonneg _)

/-- Zero approximation is a valid absolute row reserve, not an
independence or relative approximation assertion. -/
theorem neutralIV106E19RPacked_rows (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) :
    ‖∑ i, c i • neutralIV106E14Row k hk (Sum.inr (Sum.inr (Sum.inl i)))‖^2 ≤
      (1/(1000*(k:ℝ))) * ∑ i, ‖c i‖^2 := by
  let P := ContinuousLinearMap.adjoint neutralIV106E19LInclusion
  let f := (neutralIV100Packed k hk c).toLp 2 volume
  have he : P (neutralIV106E19LRawColumn f) =
      ∑ i, c i • neutralIV106E14Row k hk (Sum.inr (Sum.inr (Sum.inl i))) := by
    dsimp only [P,f]
    rw [neutralIV104Packed_toLp]
    unfold neutralIV106E19LRawColumn
    rw [map_sum,map_sum]
    simp only [map_smul,← neutralIV106E19LRawColumn,← neutralIV106E19LRow_project]
    rfl
  rw [← he]
  have hn : ‖P (neutralIV106E19LRawColumn f)‖ ≤ ‖f‖ :=
    ((P.le_opNorm _).trans (by
      simpa using mul_le_mul_of_nonneg_right neutralIV106E19LInclusion_norm
        (norm_nonneg (neutralIV106E19LRawColumn f)))).trans
      (neutralIV106E19MRaw_norm f)
  exact (pow_le_pow_left₀ (norm_nonneg _) hn 2).trans
    (neutralIV106E19RPacked_joint k hk c)

#print axioms neutralIV106E19RPlateau_le
#print axioms neutralIV106E19RPacked_mass
#print axioms neutralIV106E19RPacked_joint
#print axioms neutralIV106E19RPacked_rows
end
end WeilDefect
