import WeilDefect.MasterRecon.V10B6a

/-! V10B6b: construct the literal complex-linear arithmetic analysis
map. The physical inclusion is an L² equivalence class; linearity is
proved via almost-everywhere integral congruence. -/
namespace WeilDefect.MasterRecon.V10B6b

open MeasureTheory
open scoped ENNReal BigOperators
open V10A (Index displacement ordinate multiplicity normalizedPair)

noncomputable def carrierMellin (t : ℝ) (g : V08I.logCarrier t) (z : ℂ) : ℂ :=
  V07A.mellin (V08I.physicalInclusion t g : ℝ → ℂ) z

theorem carrier_integrand_integrable (t : ℝ) (ht : 0 ≤ t)
    (g : V08I.logCarrier t) (z : ℂ) :
    Integrable (fun x : ℝ => Complex.exp (z*(x : ℂ)) *
      V08I.physicalInclusion t g x) :=
  V09B.mellin_integrand_integrable t ht _
    (V08K.supported_integrable t _ (V08I.physicalInclusion_support t g))
    (V08I.physicalInclusion_support t g) z

theorem carrierMellin_add (t : ℝ) (ht : 0 ≤ t)
    (g h : V08I.logCarrier t) (z : ℂ) :
    carrierMellin t (g+h) z = carrierMellin t g z + carrierMellin t h z := by
  unfold carrierMellin V07A.mellin
  rw [← integral_add (carrier_integrand_integrable t ht g z)
    (carrier_integrand_integrable t ht h z)]
  apply integral_congr_ae
  rw [map_add]
  filter_upwards [Lp.coeFn_add (V08I.physicalInclusion t g)
    (V08I.physicalInclusion t h)] with x hx
  change (V08I.physicalInclusion t g + V08I.physicalInclusion t h) x =
    V08I.physicalInclusion t g x + V08I.physicalInclusion t h x at hx
  rw [hx, mul_add]

theorem carrierMellin_smul (t : ℝ) (a : ℂ)
    (g : V08I.logCarrier t) (z : ℂ) :
    carrierMellin t (a • g) z = a * carrierMellin t g z := by
  unfold carrierMellin V07A.mellin
  rw [← integral_const_mul]
  apply integral_congr_ae
  rw [map_smul]
  filter_upwards [Lp.coeFn_smul a (V08I.physicalInclusion t g)] with x hx
  change (a • V08I.physicalInclusion t g) x =
    a * V08I.physicalInclusion t g x at hx
  rw [hx]
  ring

theorem pairSample_add (t : ℝ) (ht : 0 ≤ t)
    (g h : V08I.logCarrier t) (i : Index) :
    V10B6a.pairSample t (g+h) i =
      V10B6a.pairSample t g i + V10B6a.pairSample t h i := by
  have hm (z : ℂ) := carrierMellin_add t ht g h z
  unfold carrierMellin at hm
  apply WithLp.ofLp_injective
  by_cases hi : displacement i = 0
  · simp only [V10B6a.pairSample, normalizedPair, if_pos hi]
    apply Prod.ext
    · change V07A.weightedMellin _ _ _ = V07A.weightedMellin _ _ _ +
        V07A.weightedMellin _ _ _
      simp only [V07A.weightedMellin, hm, mul_add]
    · change (0 : ℂ) = 0 + 0
      simp
  · simp only [V10B6a.pairSample, normalizedPair, if_neg hi, V07E.samplePair]
    apply Prod.ext
    · change V07A.pairPlus _ _ = V07A.pairPlus _ _ + V07A.pairPlus _ _
      simp only [V07A.pairPlus, V07A.weightedMellin, hm]
      ring
    · change V07A.pairMinus _ _ = V07A.pairMinus _ _ + V07A.pairMinus _ _
      simp only [V07A.pairMinus, V07A.weightedMellin, hm]
      ring

theorem pairSample_smul (t : ℝ) (a : ℂ)
    (g : V08I.logCarrier t) (i : Index) :
    V10B6a.pairSample t (a • g) i = a • V10B6a.pairSample t g i := by
  have hm (z : ℂ) := carrierMellin_smul t a g z
  unfold carrierMellin at hm
  apply WithLp.ofLp_injective
  by_cases hi : displacement i = 0
  · simp only [V10B6a.pairSample, normalizedPair, if_pos hi]
    apply Prod.ext
    · change V07A.weightedMellin _ _ _ = a * V07A.weightedMellin _ _ _
      simp only [V07A.weightedMellin, hm]
      ring
    · change (0 : ℂ) = a * 0
      simp
  · simp only [V10B6a.pairSample, normalizedPair, if_neg hi, V07E.samplePair]
    apply Prod.ext
    · change V07A.pairPlus _ _ = a * V07A.pairPlus _ _
      simp only [V07A.pairPlus, V07A.weightedMellin, hm]
      ring
    · change V07A.pairMinus _ _ = a * V07A.pairMinus _ _
      simp only [V07A.pairMinus, V07A.weightedMellin, hm]
      ring

noncomputable def analysisValue (t B : ℝ)
    (hB : ∀ (g : V08I.logCarrier t) (S : Finset Index),
      (∑ i ∈ S, ‖V10B6a.pairSample t g i‖^2) ≤ B*‖g‖^2)
    (g : V08I.logCarrier t) : V07C.Coeff Index :=
  ⟨V10B6a.pairSample t g, V10B6a.pair_mem t g B (hB g)⟩

theorem analysisValue_apply (t B : ℝ)
    (hB : ∀ (g : V08I.logCarrier t) (S : Finset Index),
      (∑ i ∈ S, ‖V10B6a.pairSample t g i‖^2) ≤ B*‖g‖^2)
    (g : V08I.logCarrier t) (i : Index) :
    analysisValue t B hB g i = V10B6a.pairSample t g i := rfl

theorem analysisValue_bound (t B : ℝ) (hB0 : 0 ≤ B)
    (hB : ∀ (g : V08I.logCarrier t) (S : Finset Index),
      (∑ i ∈ S, ‖V10B6a.pairSample t g i‖^2) ≤ B*‖g‖^2)
    (g : V08I.logCarrier t) :
    ‖analysisValue t B hB g‖ ≤ Real.sqrt B * ‖g‖ := by
  have hs := V10B6a.lp_two_norm_sq_le_of_budget (analysisValue t B hB g)
    (B*‖g‖^2) (hB g)
  have he : (Real.sqrt B * ‖g‖)^2 = B*‖g‖^2 := by
    rw [mul_pow, Real.sq_sqrt hB0]
  rw [← he] at hs
  exact le_of_sq_le_sq hs (by positivity)

noncomputable def arithmeticAnalysis (t : ℝ) (ht : 0 ≤ t) (B : ℝ) (hB0 : 0 ≤ B)
    (hB : ∀ (g : V08I.logCarrier t) (S : Finset Index),
      (∑ i ∈ S, ‖V10B6a.pairSample t g i‖^2) ≤ B*‖g‖^2) :
    V08I.logCarrier t →L[ℂ] V07C.Coeff Index :=
  ({ toFun := analysisValue t B hB
     map_add' := fun g h => by
       apply lp.ext
       funext i
       change V10B6a.pairSample t (g+h) i =
         V10B6a.pairSample t g i + V10B6a.pairSample t h i
       exact pairSample_add t ht g h i
     map_smul' := fun a g => by
       apply lp.ext
       funext i
       change V10B6a.pairSample t (a • g) i = a • V10B6a.pairSample t g i
       exact pairSample_smul t a g i } :
       V08I.logCarrier t →ₗ[ℂ] V07C.Coeff Index).mkContinuous
        (Real.sqrt B) (analysisValue_bound t B hB0 hB)

theorem arithmeticAnalysis_apply (t : ℝ) (ht : 0 ≤ t) (B : ℝ) (hB0 : 0 ≤ B)
    (hB : ∀ (g : V08I.logCarrier t) (S : Finset Index),
      (∑ i ∈ S, ‖V10B6a.pairSample t g i‖^2) ≤ B*‖g‖^2)
    (g : V08I.logCarrier t) (i : Index) :
    arithmeticAnalysis t ht B hB0 hB g i = V10B6a.pairSample t g i := rfl

theorem arithmeticAnalysis_norm_le (t : ℝ) (ht : 0 ≤ t) (B : ℝ) (hB0 : 0 ≤ B)
    (hB : ∀ (g : V08I.logCarrier t) (S : Finset Index),
      (∑ i ∈ S, ‖V10B6a.pairSample t g i‖^2) ≤ B*‖g‖^2) :
    ‖arithmeticAnalysis t ht B hB0 hB‖ ≤ Real.sqrt B := by
  apply ContinuousLinearMap.opNorm_le_bound _ (Real.sqrt_nonneg B)
  exact analysisValue_bound t B hB0 hB

theorem bounded_arithmetic_analysis (t : ℝ) (ht : 0 ≤ t) (A : ℝ) (hA : 0 ≤ A)
    (hcount : ∀ n : ℤ, (V09D.count (n : ℝ) ((n : ℝ)+1) : ℝ) ≤
      A * Real.log (|(n : ℝ)|+3)) :
    ∃ T : V08I.logCarrier t →L[ℂ] V07C.Coeff Index,
      ∀ (g : V08I.logCarrier t) (i : Index),
        T g i = normalizedPair (V08I.physicalInclusion t g : ℝ → ℂ) i := by
  obtain ⟨B,hB0,hB⟩ := V10B6a.pair_finite_budget t ht A hA hcount
  exact ⟨arithmeticAnalysis t ht B hB0 hB,
    arithmeticAnalysis_apply t ht B hB0 hB⟩

end WeilDefect.MasterRecon.V10B6b

#print axioms WeilDefect.MasterRecon.V10B6b.carrier_integrand_integrable
#print axioms WeilDefect.MasterRecon.V10B6b.carrierMellin_add
#print axioms WeilDefect.MasterRecon.V10B6b.carrierMellin_smul
#print axioms WeilDefect.MasterRecon.V10B6b.pairSample_add
#print axioms WeilDefect.MasterRecon.V10B6b.pairSample_smul
#print axioms WeilDefect.MasterRecon.V10B6b.analysisValue_apply
#print axioms WeilDefect.MasterRecon.V10B6b.analysisValue_bound
#print axioms WeilDefect.MasterRecon.V10B6b.arithmeticAnalysis_apply
#print axioms WeilDefect.MasterRecon.V10B6b.arithmeticAnalysis_norm_le
#print axioms WeilDefect.MasterRecon.V10B6b.bounded_arithmetic_analysis
