import WeilDefect.MasterRecon.V10B5e

/-! V10B6a: normalized orbit energy and the full Hilbert coefficient
membership. The finite upper bound is inherited from the two literal
arithmetic Mellin bounds, with the fixed orbit counted only once. -/
namespace WeilDefect.MasterRecon.V10B6a

open MeasureTheory
open scoped ENNReal BigOperators
open V10A (Index displacement ordinate multiplicity normalizedPair)

noncomputable def pairSample (t : ℝ) (g : V08I.logCarrier t) (i : Index) : V07C.Pair :=
  normalizedPair (V08I.physicalInclusion t g : ℝ → ℂ) i

theorem pair_norm_sq (v : V07C.Pair) :
    ‖v‖^2 = ‖(WithLp.ofLp v).1‖^2 + ‖(WithLp.ofLp v).2‖^2 := by
  rw [WithLp.prod_norm_eq_of_L2, Real.sq_sqrt (by positivity)]

theorem fixed_exponent (i : Index) (h : displacement i = 0) :
    ((i : ℂ)-1/2) = (ordinate i : ℂ)*Complex.I := by
  rw [← V10A.right_exponent i, h]
  simp

theorem normalized_pair_energy (f : ℝ → ℂ) (i : Index) :
    ‖normalizedPair f i‖^2 =
      (multiplicity i : ℝ) * ‖V07A.mellin f ((i : ℂ)-1/2)‖^2 +
        if displacement i = 0 then 0 else
          (multiplicity i : ℝ) *
            ‖V07A.mellin f (V10A.reflect (i : ℂ)-1/2)‖^2 := by
  rw [pair_norm_sq]
  by_cases hi : displacement i = 0
  · rw [V10A.normalizedPair_fixed f i hi, if_pos hi, fixed_exponent i hi]
    simp [V10A2.weighted_energy]
  · rw [V10A.normalizedPair_nonfixed f i hi, if_neg hi]
    change ‖V07A.pairPlus _ _‖^2 + ‖V07A.pairMinus _ _‖^2 = _
    rw [V10A2.pair_energy_sum, V10A.right_exponent, V10A.left_exponent,
      V10A2.weighted_energy, V10A2.weighted_energy]

theorem normalized_pair_energy_le (f : ℝ → ℂ) (i : Index) :
    ‖normalizedPair f i‖^2 ≤
      (multiplicity i : ℝ) * ‖V07A.mellin f ((i : ℂ)-1/2)‖^2 +
      (multiplicity i : ℝ) * ‖V07A.mellin f (V10A.reflect (i : ℂ)-1/2)‖^2 := by
  rw [normalized_pair_energy]
  by_cases hi : displacement i = 0
  · rw [if_pos hi]
    exact add_le_add_left (by positivity) _
  · rw [if_neg hi]

theorem finite_of_ennreal_budget {ι : Type*} (F : ι → ℝ) (hF : ∀ i, 0 ≤ F i)
    (B : ℝ) (hB : 0 ≤ B)
    (h : (∑' i, ENNReal.ofReal (F i)) ≤ ENNReal.ofReal B)
    (S : Finset ι) : (∑ i ∈ S, F i) ≤ B := by
  have he : ENNReal.ofReal (∑ i ∈ S, F i) ≤ ENNReal.ofReal B := by
    rw [ENNReal.ofReal_sum_of_nonneg (fun i _ => hF i)]
    exact (ENNReal.sum_le_tsum S).trans h
  have ht := ENNReal.toReal_mono ENNReal.ofReal_ne_top he
  simpa only [ENNReal.toReal_ofReal (Finset.sum_nonneg (fun i _ => hF i)),
    ENNReal.toReal_ofReal hB] using ht

theorem pair_finite_budget (t : ℝ) (ht : 0 ≤ t) (A : ℝ) (hA : 0 ≤ A)
    (hcount : ∀ n : ℤ, (V09D.count (n : ℝ) ((n : ℝ)+1) : ℝ) ≤
      A * Real.log (|(n : ℝ)|+3)) :
    ∃ B : ℝ, 0 ≤ B ∧ ∀ (g : V08I.logCarrier t) (S : Finset Index),
      (∑ i ∈ S, ‖pairSample t g i‖^2) ≤ B * ‖g‖^2 := by
  obtain ⟨C,hC,h⟩ := V10B5e.bounded_arithmetic_samples t ht A hA hcount
  refine ⟨2*C,by positivity,?_⟩
  intro g S
  let f := (V08I.physicalInclusion t g : ℝ → ℂ)
  let R : Index → ℝ := fun i =>
    (multiplicity i : ℝ)*‖V07A.mellin f ((i : ℂ)-1/2)‖^2
  let L : Index → ℝ := fun i =>
    (multiplicity i : ℝ)*‖V07A.mellin f (V10A.reflect (i : ℂ)-1/2)‖^2
  have hR := finite_of_ennreal_budget R (fun i => by dsimp [R]; positivity)
    (C*‖g‖^2) (by positivity) (h g).1 S
  have hL := finite_of_ennreal_budget L (fun i => by dsimp [L]; positivity)
    (C*‖g‖^2) (by positivity) (h g).2 S
  calc
    _ ≤ ∑ i ∈ S, (R i + L i) :=
      Finset.sum_le_sum (fun i _ => normalized_pair_energy_le f i)
    _ = (∑ i ∈ S, R i) + (∑ i ∈ S, L i) := Finset.sum_add_distrib
    _ ≤ (2*C)*‖g‖^2 := by linarith only [hR,hL]

theorem lp_two_mem_of_budget {ι : Type*} {K : Type*} [NormedAddCommGroup K]
    (F : ι → K) (B : ℝ)
    (h : ∀ S : Finset ι, (∑ i ∈ S, ‖F i‖^2) ≤ B) :
    Memℓp F 2 := by
  apply memℓp_gen' (C := B)
  intro S
  simpa only [ENNReal.toReal_ofNat, Real.rpow_natCast] using h S

theorem lp_two_norm_sq {ι : Type*} {K : Type*} [NormedAddCommGroup K]
    (x : lp (fun _ : ι => K) 2) :
    ‖x‖^2 = ∑' i, ‖x i‖^2 := by
  simpa only [ENNReal.toReal_ofNat, Real.rpow_natCast] using
    (lp.norm_rpow_eq_tsum (by norm_num : 0 < (2 : ℝ≥0∞).toReal) x)

theorem lp_two_norm_sq_le_of_budget {ι : Type*} {K : Type*} [NormedAddCommGroup K]
    (x : lp (fun _ : ι => K) 2) (B : ℝ)
    (h : ∀ S : Finset ι, (∑ i ∈ S, ‖x i‖^2) ≤ B) :
    ‖x‖^2 ≤ B := by
  have hs := (lp.memℓp x).summable (by norm_num : 0 < (2 : ℝ≥0∞).toReal)
  have hs' : Summable (fun i => ‖x i‖^2) := by
    simpa only [ENNReal.toReal_ofNat, Real.rpow_natCast] using hs
  rw [lp_two_norm_sq]
  exact le_of_tendsto hs'.hasSum (Filter.Eventually.of_forall h)

theorem pair_mem (t : ℝ) (g : V08I.logCarrier t) (B : ℝ)
    (h : ∀ S : Finset Index, (∑ i ∈ S, ‖pairSample t g i‖^2) ≤ B*‖g‖^2) :
    Memℓp (pairSample t g) 2 :=
  lp_two_mem_of_budget _ _ h

end WeilDefect.MasterRecon.V10B6a

#print axioms WeilDefect.MasterRecon.V10B6a.pair_norm_sq
#print axioms WeilDefect.MasterRecon.V10B6a.fixed_exponent
#print axioms WeilDefect.MasterRecon.V10B6a.normalized_pair_energy
#print axioms WeilDefect.MasterRecon.V10B6a.normalized_pair_energy_le
#print axioms WeilDefect.MasterRecon.V10B6a.finite_of_ennreal_budget
#print axioms WeilDefect.MasterRecon.V10B6a.pair_finite_budget
#print axioms WeilDefect.MasterRecon.V10B6a.lp_two_mem_of_budget
#print axioms WeilDefect.MasterRecon.V10B6a.lp_two_norm_sq
#print axioms WeilDefect.MasterRecon.V10B6a.lp_two_norm_sq_le_of_budget
#print axioms WeilDefect.MasterRecon.V10B6a.pair_mem
