import WeilDefect.Arithmetic.ActualZetaIV106C3ActualConstraints
import WeilDefect.Arithmetic.ActualZetaIV106D2ReciprocalFourier
import WeilDefect.Arithmetic.ActualZetaIV106D3CompactPrimitive
import WeilDefect.Arithmetic.ActualZetaIV106D5PartitionEnergy

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped SchwartzMap LineDeriv FourierTransform

def neutralIV106D6Endpoint (j : ℕ) : ℝ :=
  -(11/10:ℝ) + (j:ℝ)*(11/3325:ℝ)

theorem neutralIV106D6Endpoint_zero : neutralIV106D6Endpoint 0 = -(11/10:ℝ) := by
  norm_num [neutralIV106D6Endpoint]

theorem neutralIV106D6Endpoint_last : neutralIV106D6Endpoint 665 = (11/10:ℝ) := by
  norm_num [neutralIV106D6Endpoint]

theorem neutralIV106D6Endpoint_width (j : ℕ) :
    neutralIV106D6Endpoint (j+1) - neutralIV106D6Endpoint j = (11/3325:ℝ) := by
  simp only [neutralIV106D6Endpoint, Nat.cast_add, Nat.cast_one]
  ring

/-- Transfer the actual C3C cell row to the Schwartz representative. -/
theorem neutralIV106D6Actual_means (k : ℕ) (hk : 0 < k)
    (q : NeutralLogHilbertCarrier (11/10:ℝ)) (v : 𝓢(ℝ,ℂ))
    (hv : neutralLogPhysical q.val = v.toLp 2 volume)
    (hq : neutralIV106C3Constraints 665 k hk q = 0) :
    ∀ j < 665, (∫ t in neutralIV106D6Endpoint j..neutralIV106D6Endpoint (j+1), v t) = 0 := by
  intro j hj
  let i : Fin 665 := ⟨j,hj⟩
  have hm := ((neutralIV106C3Constraints_zero_iff 665 k hk q).mp hq).1 i
  rw [hv] at hm
  have he : (∫ t in neutralIV106C3Cell (11/10:ℝ) 665 i, (v.toLp 2 volume) t) =
      ∫ t in neutralIV106C3Cell (11/10:ℝ) 665 i, v t := by
    apply setIntegral_congr_ae (show MeasurableSet (neutralIV106C3Cell (11/10:ℝ) 665 i)
      from measurableSet_Icc)
    filter_upwards [v.coeFn_toLp 2 volume] with t ht _
    exact ht
  rw [he] at hm
  have hc : neutralIV106C3Cell (11/10:ℝ) 665 i =
      Set.Icc (neutralIV106D6Endpoint j) (neutralIV106D6Endpoint (j+1)) := by
    unfold neutralIV106C3Cell neutralIV106D6Endpoint
    dsimp [i]
    push_cast
    norm_num
  rw [hc] at hm
  apply neutralIV106D5Closed_cell _ _ _ _ hm
  exact sub_nonneg.mp (by rw [neutralIV106D6Endpoint_width]; norm_num)

/-- Convert supported Schwartz mass on a closed window into its actual L2 norm. -/
theorem neutralIV106D6Window_mass (v : 𝓢(ℝ,ℂ)) (l r : ℝ)
    (hlr : l ≤ r) (hv : ∀ x ∉ Set.Icc l r, v x = 0) :
    (∫ x in l..r, ‖v x‖^2) = ‖v.toLp 2 volume‖^2 := by
  calc
    _ = ∫ x in Set.Icc l r, ‖v x‖^2 := by
      rw [intervalIntegral.integral_of_le hlr, integral_Icc_eq_integral_Ioc]
    _ = ∫ x : ℝ, ‖v x‖^2 := by
      rw [← integral_indicator measurableSet_Icc]
      apply integral_congr_ae
      filter_upwards [] with x
      by_cases hx : x ∈ Set.Icc l r
      · simp [hx]
      · simp [hx, hv x hx]
    _ = ∫ x : ℝ, ‖(v.toLp 2 volume) x‖^2 := by
      apply integral_congr_ae
      filter_upwards [v.coeFn_toLp 2 volume] with x hx
      rw [hx]
    _ = _ := by rw [← neutralPhysicalL2_norm_sq]

/-- Construct the actual constrained primitive and discharge the D2 mass premise. -/
theorem neutralIV106D6Actual_primitive (k : ℕ) (hk : 0 < k)
    (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106C3Constraints 665 k hk q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    ∃ v V : 𝓢(ℝ,ℂ), neutralLogPhysical q.val = v.toLp 2 volume ∧
      ∂_{(1:ℝ)} V = v ∧
      ‖V.toLp 2 volume‖^2 ≤ (11/3325:ℝ)^2/6 * ‖v.toLp 2 volume‖^2 := by
  rcases hd with ⟨v,hv,hphys⟩
  have hm := neutralIV106D6Actual_means k hk q v hphys hq
  have hends := neutralIV106D3Endpoint v neutralIV106D6Endpoint 665 hm
  have htotal := hends 665 (by omega)
  rw [neutralIV106D6Endpoint_zero, neutralIV106D6Endpoint_last] at htotal
  obtain ⟨V,hV,hder,hout⟩ := neutralIV106D3Schwartz_primitive v
    (-(11/10:ℝ)) (11/10:ℝ) (by norm_num) hv htotal
  have hlocal (j : ℕ) (hj : j < 665) (x : ℝ)
      (_ : x ∈ Set.Icc (neutralIV106D6Endpoint j) (neutralIV106D6Endpoint (j+1))) :
      V x = ∫ t in neutralIV106D6Endpoint j..x, v t := by
    have he := intervalIntegral.integral_add_adjacent_intervals
      (v.continuous.intervalIntegrable (μ := volume) (neutralIV106D6Endpoint 0) (neutralIV106D6Endpoint j))
      (v.continuous.intervalIntegrable (μ := volume) (neutralIV106D6Endpoint j) x)
    rw [hends j (Nat.le_of_lt hj), zero_add, neutralIV106D6Endpoint_zero] at he
    rw [hV x, he]
  have hmass := neutralIV106D5Partition_energy v V v.continuous V.continuous
    neutralIV106D6Endpoint 665 (11/3325:ℝ) (by norm_num)
    (fun j _ => neutralIV106D6Endpoint_width j) hm hlocal
  rw [neutralIV106D6Endpoint_zero, neutralIV106D6Endpoint_last,
    neutralIV106D6Window_mass V _ _ (by norm_num) hout,
    neutralIV106D6Window_mass v _ _ (by norm_num) hv] at hmass
  exact ⟨v,V,hphys,hder,hmass⟩

/-- The reciprocal density is genuinely integrable, not merely a totalized integral. -/
theorem neutralIV106D6Reciprocal_integrable (V v : 𝓢(ℝ,ℂ))
    (hd : ∂_{(1:ℝ)} V = v) :
    Integrable (fun ξ : ℝ => ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2 / ξ^2) := by
  have hm := (memLp_two_iff_integrable_sq_norm
    (Lp.aestronglyMeasurable (𝓕 (V.toLp 2 volume) : RealComplexL2))).mp
    (Lp.memLp (𝓕 (V.toLp 2 volume) : RealComplexL2))
  exact (hm.const_mul ((2*Real.pi)^2)).congr
    (neutralIV106D2Reciprocal_ae V v hd).symm

/-- Attach the certified Fourier moment to the actual C3C constrained core. -/
theorem neutralIV106D6Actual_reciprocal (k : ℕ) (hk : 0 < k)
    (q : NeutralLogHilbertCarrier (11/10:ℝ))
    (hq : neutralIV106C3Constraints 665 k hk q = 0)
    (hd : q ∈ neutralIV106C3Core (11/10:ℝ)) :
    Integrable (fun ξ : ℝ => ‖(𝓕 (neutralLogPhysical q.val) : RealComplexL2) ξ‖^2 / ξ^2) ∧
    (∫ ξ : ℝ, ‖(𝓕 (neutralLogPhysical q.val) : RealComplexL2) ξ‖^2 / ξ^2) ≤
      (2*Real.pi^2/3)*(11/3325:ℝ)^2*‖neutralLogPhysical q.val‖^2 := by
  obtain ⟨v,V,hphys,hder,hmass⟩ := neutralIV106D6Actual_primitive k hk q hq hd
  rw [hphys]
  exact ⟨neutralIV106D6Reciprocal_integrable V v hder,
    neutralIV106D2Reciprocal_bound V v (11/3325:ℝ) hder hmass⟩

#print axioms neutralIV106D6Endpoint_zero
#print axioms neutralIV106D6Endpoint_last
#print axioms neutralIV106D6Endpoint_width
#print axioms neutralIV106D6Actual_means
#print axioms neutralIV106D6Window_mass
#print axioms neutralIV106D6Actual_primitive
#print axioms neutralIV106D6Reciprocal_integrable
#print axioms neutralIV106D6Actual_reciprocal
end
end WeilDefect
