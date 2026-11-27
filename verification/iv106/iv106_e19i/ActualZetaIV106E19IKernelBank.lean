import WeilDefect.Arithmetic.ActualZetaIV106E19ICellMeans
import WeilDefect.Arithmetic.ActualZetaIV106E19HLiteralCorrection
import WeilDefect.Arithmetic.ActualZetaIV106E19CKernelCorrection
import WeilDefect.Arithmetic.ActualZetaIV106E12ComplementInverse

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric InnerProductSpace
open scoped SchwartzMap BigOperators

/-- The original packed rows annihilate the literal rough trial, not
just a separately chosen smooth approximation. -/
theorem neutralIV106E19IPacked (k : ℕ) (hk : 0 < k) (i : Fin k)
    (j : ℕ) (hj : neutralIV106E18LEligible j) :
    inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
      (neutralIV106E18OTrial j) = 0 := by
  rw [L2.inner_def]
  let l := neutralIV106E18LLeft j
  let h := neutralIV106E18LWidth
  have hh : 0 < h := neutralIV106E19IWidth_pos
  have hz : (fun x : ℝ => inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume x)
      (neutralIV106E18OTrial j x)) =ᵐ[volume] (fun _ => 0) := by
    filter_upwards [(neutralIV100Carrier k hk i).coeFn_toLp 2 volume,
      (neutralIV106E18JTrial_memLp l h hh).coeFn_toLp] with x hx hy
    change inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume x)
      ((neutralIV106E18JTrial_memLp l h hh).toLp _ x) = 0
    rw [hx,hy]
    by_cases hm : x ∈ Icc l (l+h)
    · have hb : x ∈ closedBall (l+h/2) (h/2+neutralIV106E18LBuffer) := by
        rw [mem_closedBall,Real.dist_eq,abs_le]
        have hp : 0 < neutralIV106E18LBuffer := by norm_num [neutralIV106E18LBuffer]
        constructor <;> linarith [hm.1,hm.2]
      have hd : x ∉ Icc (4393/4000:ℝ) (4399/4000) := by
        intro hc
        have hg := neutralIV106E18LGap j hj x hc x hb
        norm_num at hg
      rw [neutralIV106E18JCarrier_zero k hk i x hd,zero_inner]
    · rw [neutralIV106E18ITrial_outside l h hh x hm,inner_zero]
  rw [integral_congr_ae hz]
  simp

/-- Each admitted cell has only the response coordinates possibly nonzero. -/
theorem neutralIV106E19IBase (k : ℕ) (hk : 0 < k) (j : ℕ)
    (hj : neutralIV106E18LEligible j) (p : neutralIV106E19CH)
    (hp : neutralLogPhysical p.val = neutralIV106E18OTrial j) :
    neutralIV106C3Constraints 665 k hk p =
      neutralIV106E19CResponseOnly k (neutralIV106E19CResponse k hk p) := by
  funext a
  rcases a with i | a
  · change neutralIV106C3PhysicalRow _ (neutralIV106C3CellColumn _ 665 i) p = 0
    rw [neutralIV106C3PhysicalRow_eq,neutralIV106C3Cell_pair,hp]
    exact neutralIV106E19IMean i j
  · rcases a with u | a
    · change neutralLogMoment (11/10:ℝ) (1/2) p -
        neutralLogMoment (11/10:ℝ) (-(1/2)) p = 0
      rw [neutralLogMoment_eq,neutralLogMoment_eq,hp]
      have h1 := neutralIV106E18K2Moment_zero (11/10:ℝ)
        (neutralIV106E18LLeft j) neutralIV106E18LWidth (1/2)
        neutralIV106E19IWidth_pos (neutralIV106E19IWindow j hj) (Or.inr (Or.inl rfl))
      have h2 := neutralIV106E18K2Moment_zero (11/10:ℝ)
        (neutralIV106E18LLeft j) neutralIV106E18LWidth (-(1/2))
        neutralIV106E19IWidth_pos (neutralIV106E19IWindow j hj) (Or.inr (Or.inr rfl))
      change sourceWindowMoment _ _ (neutralIV106E18OTrial j) = 0 at h1 h2
      rw [h1,h2,sub_self]
    · rcases a with i | i
      · change neutralIV106C3PhysicalRow _ ((neutralIV100Carrier k hk i).toLp 2 volume) p = 0
        rw [neutralIV106C3PhysicalRow_eq,hp]
        exact neutralIV106E19IPacked k hk i j hj
      · rfl

/-- Use arbitrary actual carrier representatives of the admitted physical
cells. The Cramer coefficients cancel the entire literal constraint map. -/
theorem neutralIV106E19IKernel (k : ℕ) (hk : 0 < k) (s : ℕ)
    (hs : neutralIV106E18LEligible s)
    (hel : ∀ j : Fin k, neutralIV106E18LEligible (s+j.val+1))
    (p : neutralIV106E19CH) (q : Fin k → neutralIV106E19CH)
    (hp : neutralLogPhysical p.val = neutralIV106E18OTrial s)
    (hq : ∀ j, neutralLogPhysical (q j).val = neutralIV106E18OTrial (s+j.val+1)) :
    neutralIV106C3Constraints 665 k hk
      (p-∑ j, (neutralIV106E19HCoeff k hk s j:ℂ) • q j) = 0 := by
  classical
  rw [map_sub,map_sum]
  simp only [map_smul]
  rw [neutralIV106E19IBase k hk s hs p hp]
  have hb (j : Fin k) := neutralIV106E19IBase k hk (s+j.val+1) (hel j) (q j) (hq j)
  simp_rw [hb]
  funext a
  simp only [Pi.sub_apply,Finset.sum_apply,Pi.smul_apply,Pi.zero_apply,smul_eq_mul]
  rcases a with i | a
  · simp [neutralIV106E19CResponseOnly]
  · rcases a with u | a
    · simp [neutralIV106E19CResponseOnly]
    · rcases a with i | i
      · simp [neutralIV106E19CResponseOnly]
      · simp only [neutralIV106E19CResponseOnly]
        change inner ℂ (neutralIV105CResponse k hk i) (neutralLogPhysical p.val) -
          (∑ j, (neutralIV106E19HCoeff k hk s j:ℂ) *
            inner ℂ (neutralIV105CResponse k hk i) (neutralLogPhysical (q j).val)) = 0
        rw [hp]
        simp_rw [hq]
        have hs' : s-1+1=s := by have hh := hs.1; omega
        have he := neutralIV106E19HLiteral_response k hk s hs hel i
        unfold neutralIV106E18OEntry at he
        rw [hs'] at he
        exact sub_eq_zero.mpr he

/-- Each eligible consecutive block supplies an actual E12 kernel element,
with its original physical representative specified exactly. -/
theorem neutralIV106E19IExists (k : ℕ) (hk : 0 < k) (s : ℕ)
    (hs : neutralIV106E18LEligible s)
    (hel : ∀ j : Fin k, neutralIV106E18LEligible (s+j.val+1)) :
    ∃ z : neutralIV106E12Kernel k hk,
      neutralLogPhysical z.val.val =
        neutralIV106E18OTrial s -
          ∑ j, (neutralIV106E19HCoeff k hk s j:ℂ) •
            neutralIV106E18OTrial (s+j.val+1) := by
  classical
  obtain ⟨p,hp⟩ := neutralIV106E19IAdmission s hs
  choose q hq using fun j : Fin k => neutralIV106E19IAdmission (s+j.val+1) (hel j)
  let z := p-∑ j, (neutralIV106E19HCoeff k hk s j:ℂ) • q j
  have hz : z ∈ neutralIV106E12Kernel k hk :=
    neutralIV106E19IKernel k hk s hs hel p q hp hq
  refine ⟨⟨z,hz⟩,?_⟩
  change neutralLogPhysicalInclusion (11/10:ℝ) z = _
  rw [show z = p-∑ j, (neutralIV106E19HCoeff k hk s j:ℂ) • q j by rfl,
    map_sub,map_sum]
  simp only [map_smul]
  change neutralLogPhysical p.val -
    (∑ j, (neutralIV106E19HCoeff k hk s j:ℂ) • neutralLogPhysical (q j).val) = _
  simp_rw [hp,hq]

#print axioms neutralIV106E19IPacked
#print axioms neutralIV106E19IBase
#print axioms neutralIV106E19IKernel
#print axioms neutralIV106E19IExists
end
end WeilDefect
