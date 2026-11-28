import WeilDefect.MasterRecon.V10B64a
import WeilDefect.MasterRecon.V10B67a
import WeilDefect.MasterRecon.V10B50b

/-! Physical realization of the exact complex constraint matrix.
The factor 2 compensates for dx = dz/2; the remaining row factors
are precisely the existing unitMatrix normalizations. -/
namespace WeilDefect.MasterRecon.V10B68a
open MeasureTheory Set
open scoped BigOperators InnerProduct Matrix
open V08I (logCarrier physicalInclusion)
open V08K (supportMeasure restrictPhysical)
open V10B33a (legendre)
open V10B47c (trial load unitMatrix unitMatrix_surjective)
open V10B67a (carrierTrial supportedTrial polynomialValue carrierTrial_ae)

noncomputable def test (i : Fin 16) (z : ℝ) : ℝ :=
  if i.val=15 then load z else legendre i.val z

noncomputable def factor (i : Fin 16) : ℝ :=
  if i.val=15 then 31 else 2*(i.val:ℝ)+1

theorem test_cont (i : Fin 16) : Continuous (test i) := by
  unfold test
  by_cases hi : i.val=15
  · simp only [hi,if_true]
    exact V10B47c.load_cont
  · simp only [hi,if_false]
    exact V10B47c.legendre_cont _

theorem factor_pos (i : Fin 16) : 0 < factor i := by
  unfold factor
  split_ifs <;> positivity

noncomputable def rowValue (i : Fin 16) (x : ℝ) : ℂ :=
  Complex.ofReal (test i (2*x+1/2))

theorem row_mem (i : Fin 16) : MemLp (rowValue i) 2 (supportMeasure (1/4)) := by
  have hc : Continuous (rowValue i) :=
    Complex.continuous_ofReal.comp ((test_cont i).comp (by fun_prop))
  apply (memLp_two_iff_integrable_sq_norm hc.aestronglyMeasurable).mpr
  exact (hc.norm.pow 2).integrableOn_Icc

noncomputable def rowVector (i : Fin 16) : V08F.PhysicalL2 (supportMeasure (1/4)) :=
  (row_mem i).toLp (rowValue i)

noncomputable def rowCLM (i : Fin 16) : logCarrier (1/4) →L[ℂ] ℂ :=
  ((2*factor i:ℝ):ℂ) •
    ((innerSL ℂ (rowVector i)).comp
      ((restrictPhysical (1/4)).comp (physicalInclusion (1/4))))

noncomputable def L : logCarrier (1/4) →ₗ[ℂ] (Fin 16 → ℂ) :=
  LinearMap.pi (fun i => (rowCLM i).toLinearMap)

theorem row_literal (i : Fin 16) (g : logCarrier (1/4)) :
    L g i = ((2*factor i:ℝ):ℂ) *
      (∫ x, (test i (2*x+1/2):ℂ)*physicalInclusion (1/4) g x
        ∂supportMeasure (1/4)) := by
  change rowCLM i g = _
  unfold rowCLM
  rw [ContinuousLinearMap.smul_apply,smul_eq_mul,
    ContinuousLinearMap.comp_apply,ContinuousLinearMap.comp_apply,
    innerSL_apply_apply,L2.inner_def]
  congr 1
  apply integral_congr_ae
  filter_upwards [MemLp.coeFn_toLp (row_mem i),
    V08K.restrictPhysical_ae (1/4) (physicalInclusion (1/4) g)] with x hx hy
  change inner ℂ (rowVector i x)
    (restrictPhysical (1/4) (physicalInclusion (1/4) g) x) = _
  rw [show rowVector i x = rowValue i x from hx,hy,RCLike.inner_apply']
  simp only [rowValue,Complex.conj_ofReal]

theorem trial_pair (i j : Fin 16) :
    (∫ x, (test i (2*x+1/2):ℂ)*physicalInclusion (1/4) (carrierTrial j) x
      ∂supportMeasure (1/4)) =
      (1/2:ℝ) • (Complex.ofReal (∫ z in (0:ℝ)..1, test i z*trial j z)) := by
  let F : ℝ → ℂ := fun z => Complex.ofReal (test i z*trial j z)
  have ha : (physicalInclusion (1/4) (carrierTrial j) : ℝ → ℂ)
      =ᵐ[supportMeasure (1/4)] supportedTrial j :=
    ae_restrict_of_ae (carrierTrial_ae j)
  calc
    _ = ∫ x, F (2*x+1/2) ∂supportMeasure (1/4) := by
      apply integral_congr_ae
      filter_upwards [ha,ae_restrict_mem (μ := volume)
        (s := Icc (-(1/4):ℝ) (1/4)) measurableSet_Icc] with x hx hm
      have hm' : x ∈ Icc (-1/4:ℝ) (1/4) := by
        simpa only [neg_div] using hm
      rw [hx,supportedTrial,indicator_of_mem hm',polynomialValue,
        V10B66a.trialPoly_eval]
      exact (Complex.ofReal_mul _ _).symm
    _ = (1/2:ℝ) • (∫ z in (0:ℝ)..1, F z) := by
      simpa only [supportMeasure,neg_div] using V10B50b.affine_support_integral F
    _ = _ := by
      congr 1
      simp only [F,intervalIntegral.integral_of_le (by norm_num : (0:ℝ) ≤ 1),
        integral_complex_ofReal]

theorem physical_matrix (i j : Fin 16) : L (carrierTrial j) i = unitMatrix i j := by
  rw [row_literal,trial_pair]
  have h : ((2*factor i:ℝ):ℂ) *
      ((1/2:ℝ) • Complex.ofReal (∫ z in (0:ℝ)..1, test i z*trial j z)) =
      Complex.ofReal (factor i*(∫ z in (0:ℝ)..1, test i z*trial j z)) := by
    rw [Complex.real_smul]
    push_cast
    ring
  rw [h]
  unfold unitMatrix factor test
  by_cases hi : i.val=15
  · simp only [hi,if_true]
  · simp only [hi,if_false]

theorem ker_retained (g : logCarrier (1/4)) :
    g ∈ L.ker ↔ g ∈ V10B17b.retainedᗮ := by
  rw [V10B64a.retained_literal_iff]
  change L g = 0 ↔ _
  have hf (i : Fin 16) : ((2*factor i:ℝ):ℂ) ≠ 0 := by
    exact_mod_cast (mul_pos (by norm_num : (0:ℝ)<2) (factor_pos i)).ne'
  constructor
  · intro h
    have hz (i : Fin 16) :
        (∫ x, (test i (2*x+1/2):ℂ)*physicalInclusion (1/4) g x
          ∂supportMeasure (1/4))=0 := by
      have hi := congrFun h i
      change L g i = 0 at hi
      rw [row_literal] at hi
      exact (mul_eq_zero.mp hi).resolve_left (hf i)
    constructor
    · intro j hj
      let i : Fin 16 := ⟨j,by omega⟩
      have hi : i.val ≠ 15 := by dsimp [i]; omega
      simpa only [test,if_neg hi,i] using hz i
    · let i : Fin 16 := ⟨15,by omega⟩
      have hi : i.val=15 := rfl
      simpa only [test,if_pos hi] using hz i
  · rintro ⟨hl,hq⟩
    funext i
    change L g i = 0
    rw [row_literal]
    by_cases hi : i.val=15
    · simp only [test,if_pos hi,hq,mul_zero]
    · simp only [test,if_neg hi,hl i.val (by omega),mul_zero]

theorem physical_surjective : Function.Surjective L := by
  intro b
  obtain ⟨a,ha⟩ := unitMatrix_surjective b
  refine ⟨∑ j, a j • carrierTrial j,?_⟩
  rw [map_sum]
  funext i
  have hi := congrFun ha i
  simp only [Matrix.mulVec,dotProduct] at hi
  rw [← hi,Finset.sum_apply]
  apply Finset.sum_congr rfl
  intro j _
  rw [map_smul,Pi.smul_apply,smul_eq_mul,physical_matrix,mul_comm]

theorem physical_section (g : logCarrier (1/4)) :
    ∃ a : Fin 16 → ℂ, g-(∑ j, a j • carrierTrial j) ∈ V10B17b.retainedᗮ := by
  obtain ⟨a,ha⟩ := V10B33b.constraint_section L carrierTrial unitMatrix
    (fun i j => (physical_matrix i j).symm) unitMatrix_surjective g
  exact ⟨a,(ker_retained _).mp ha⟩

end WeilDefect.MasterRecon.V10B68a

#print axioms WeilDefect.MasterRecon.V10B68a.test_cont
#print axioms WeilDefect.MasterRecon.V10B68a.factor_pos
#print axioms WeilDefect.MasterRecon.V10B68a.row_mem
#print axioms WeilDefect.MasterRecon.V10B68a.row_literal
#print axioms WeilDefect.MasterRecon.V10B68a.trial_pair
#print axioms WeilDefect.MasterRecon.V10B68a.physical_matrix
#print axioms WeilDefect.MasterRecon.V10B68a.ker_retained
#print axioms WeilDefect.MasterRecon.V10B68a.physical_surjective
#print axioms WeilDefect.MasterRecon.V10B68a.physical_section
