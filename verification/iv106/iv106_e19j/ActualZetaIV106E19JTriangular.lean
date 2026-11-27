import WeilDefect.Arithmetic.ActualZetaIV106E19IKernelBank
import WeilDefect.Arithmetic.ActualZetaIV106E19APhysicalReserve

namespace WeilDefect
noncomputable section
open MeasureTheory Set InnerProductSpace
open scoped BigOperators InnerProduct

/-- Distinct original cell representatives are orthogonal in physical
L2. This statement does not assert logarithmic or Weil orthogonality. -/
theorem neutralIV106E19JOrthogonal (i j : ℕ) (hij : i ≠ j) :
    inner ℂ (neutralIV106E18OTrial i) (neutralIV106E18OTrial j) = 0 := by
  rw [L2.inner_def]
  have hz : (fun x : ℝ => inner ℂ (neutralIV106E18OTrial i x)
      (neutralIV106E18OTrial j x)) =ᵐ[volume] (fun _ => 0) := by
    filter_upwards [(neutralIV106E18JTrial_memLp (neutralIV106E18LLeft i)
      neutralIV106E18LWidth neutralIV106E19IWidth_pos).coeFn_toLp,
      (neutralIV106E18JTrial_memLp (neutralIV106E18LLeft j)
      neutralIV106E18LWidth neutralIV106E19IWidth_pos).coeFn_toLp] with x hi hj
    change inner ℂ ((neutralIV106E18JTrial_memLp (neutralIV106E18LLeft i)
      neutralIV106E18LWidth neutralIV106E19IWidth_pos).toLp _ x)
      ((neutralIV106E18JTrial_memLp (neutralIV106E18LLeft j)
      neutralIV106E18LWidth neutralIV106E19IWidth_pos).toLp _ x) = 0
    rw [hi,hj]
    by_cases hm : x ∈ Icc (neutralIV106E18LLeft i)
        (neutralIV106E18LLeft i+neutralIV106E18LWidth)
    · rw [neutralIV106E19IDisjoint i j hij x hm,inner_zero]
    · rw [neutralIV106E18ITrial_outside _ _ neutralIV106E19IWidth_pos x hm,zero_inner]
  rw [integral_congr_ae hz]
  simp

theorem neutralIV106E19JDiagonal (i : ℕ) :
    inner ℂ (neutralIV106E18OTrial i) (neutralIV106E18OTrial i) =
      (12994320639248774641/98293908912022687500000:ℂ) := by
  rw [inner_self_eq_norm_sq_to_K]
  have h : ‖neutralIV106E18OTrial i‖^2 =
      12994320639248774641/98293908912022687500000 := by
    exact neutralIV106E19AMass_physical (neutralIV106E18LLeft i)
  rw [← Complex.ofReal_pow,h]
  push_cast
  rfl

/-- Generic triangular witness criterion: each column has a nonzero
leading observation and all columns starting later vanish there. -/
theorem neutralIV106E19JTriangular {J E : Type*} [Fintype J]
    [AddCommGroup E] [Module ℂ E]
    (s : J → ℕ) (hs : Function.Injective s)
    (v : J → E) (L : J → E →ₗ[ℂ] ℂ)
    (hd : ∀ i, L i (v i) ≠ 0)
    (hz : ∀ i j, s i < s j → L i (v j) = 0) :
    LinearIndependent ℂ v := by
  classical
  apply Fintype.linearIndependent_iff.mpr
  intro g hg i
  by_contra hi
  let P : ℕ → Prop := fun n => ∃ j : J, s j=n ∧ g j ≠ 0
  have hP : ∃ n, P n := ⟨s i,i,rfl,hi⟩
  obtain ⟨a,ha,hga⟩ := Nat.find_spec hP
  have hsmall (j : J) (hj : s j < s a) : g j = 0 := by
    by_contra hgj
    have hle := Nat.find_min' hP (show P (s j) from ⟨j,rfl,hgj⟩)
    omega
  have he := congrArg (L a) hg
  simp only [map_sum,map_smul,map_zero,smul_eq_mul] at he
  have hsum : (∑ j, g j*L a (v j)) = g a*L a (v a) := by
    apply Finset.sum_eq_single a
    · intro j hj hja
      rcases lt_or_gt_of_ne (fun h => hja (hs h)) with hlt | hgt
      · rw [hsmall j hlt,zero_mul]
      · rw [hz a j hgt,mul_zero]
    · simp
  rw [hsum] at he
  exact (mul_ne_zero hga (hd a)) he

/-- Literal corrected kernel families inherit triangular witnesses from
the physical L2 rows. No numerical singular-value test is used. -/
theorem neutralIV106E19JBank_independent {J : Type*} [Fintype J]
    (k : ℕ) (hk : 0 < k) (s : J → ℕ) (hs : Function.Injective s)
    (z : J → neutralIV106E12Kernel k hk)
    (hphys : ∀ a, neutralLogPhysical (z a).val.val =
      neutralIV106E18OTrial (s a) -
        ∑ j, (neutralIV106E19HCoeff k hk (s a) j:ℂ) •
          neutralIV106E18OTrial (s a+j.val+1)) :
    LinearIndependent ℂ z := by
  classical
  let P := (neutralLogPhysicalInclusion (11/10:ℝ)).comp
    (neutralIV106E12Kernel k hk).subtypeL
  let L : J → (neutralIV106E12Kernel k hk →ₗ[ℂ] ℂ) :=
    fun a => ((InnerProductSpace.toDual ℂ RealComplexL2
      (neutralIV106E18OTrial (s a))).comp P).toLinearMap
  have hobs (a b : J) : L a (z b) =
      inner ℂ (neutralIV106E18OTrial (s a)) (neutralLogPhysical (z b).val.val) := rfl
  apply neutralIV106E19JTriangular s hs z L
  · intro a
    rw [hobs,hphys,inner_sub_right,inner_sum]
    simp only [inner_smul_right]
    have hzero : (∑ j : Fin k, (neutralIV106E19HCoeff k hk (s a) j:ℂ) *
        inner ℂ (neutralIV106E18OTrial (s a))
          (neutralIV106E18OTrial (s a+j.val+1))) = 0 := by
      apply Finset.sum_eq_zero
      intro j hj
      rw [neutralIV106E19JOrthogonal _ _ (by omega),mul_zero]
    rw [hzero,sub_zero,neutralIV106E19JDiagonal]
    norm_num
  · intro a b hab
    rw [hobs,hphys,inner_sub_right,inner_sum,
      neutralIV106E19JOrthogonal _ _ (ne_of_lt hab)]
    simp only [inner_smul_right]
    have hzero : (∑ j : Fin k, (neutralIV106E19HCoeff k hk (s b) j:ℂ) *
        inner ℂ (neutralIV106E18OTrial (s a))
          (neutralIV106E18OTrial (s b+j.val+1))) = 0 := by
      apply Finset.sum_eq_zero
      intro j hj
      rw [neutralIV106E19JOrthogonal _ _ (by omega),mul_zero]
    rw [hzero,sub_zero]

/-- Synthesize a family from actual eligible consecutive blocks and
preserve its rank via the triangular witnesses. -/
theorem neutralIV106E19JBank_exists {J : Type*} [Fintype J]
    (k : ℕ) (hk : 0 < k) (s : J → ℕ) (hs : Function.Injective s)
    (hel : ∀ a, neutralIV106E18LEligible (s a))
    (hnext : ∀ a (j : Fin k), neutralIV106E18LEligible (s a+j.val+1)) :
    ∃ z : J → neutralIV106E12Kernel k hk,
      LinearIndependent ℂ z ∧
        ∀ a, neutralLogPhysical (z a).val.val =
          neutralIV106E18OTrial (s a) -
          ∑ j, (neutralIV106E19HCoeff k hk (s a) j:ℂ) •
            neutralIV106E18OTrial (s a+j.val+1) := by
  classical
  choose z hz using fun a => neutralIV106E19IExists k hk (s a) (hel a) (hnext a)
  exact ⟨z,neutralIV106E19JBank_independent k hk s hs z hz,hz⟩

#print axioms neutralIV106E19JOrthogonal
#print axioms neutralIV106E19JDiagonal
#print axioms neutralIV106E19JTriangular
#print axioms neutralIV106E19JBank_independent
#print axioms neutralIV106E19JBank_exists
end
end WeilDefect
