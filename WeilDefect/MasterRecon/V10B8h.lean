import WeilDefect.MasterRecon.V10B8g
import WeilDefect.MasterRecon.V10B6i

/-! V10B8h: assemble the three literal terms, transport equality on a
dense smooth core, and obtain the exact physical-norm defect receiver.
Density, literal explicit formula and vertical Stirling are not assumed
to be certified by this module. -/
namespace WeilDefect.MasterRecon.V10B8h

open MeasureTheory Set Complex
open scoped InnerProduct ComplexConjugate
open V08I (logCarrier physicalInclusion FullL2)
open V10B8e (residual archOperator correction)
open V10B8c (poleOperator evalRestricted)
open V10B8d (primeOperator physicalPrime)
open V10B6c (signedGram analysisChannel)

def SmoothCore (t : ℝ) : Set (logCarrier t) :=
  {g | ∃ f : ℝ → ℂ, ContDiff ℝ 2 f ∧ tsupport f ⊆ Icc (-t) t ∧
    (physicalInclusion t g : ℝ → ℂ) =ᵐ[volume] f}

noncomputable def arithmeticOperator (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C) :
    logCarrier t →L[ℂ] logCarrier t :=
  archOperator t hd C hC + poleOperator t ht - primeOperator t

theorem arithmetic_selfAdjoint (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C) :
    (arithmeticOperator t ht hd C hC).adjoint = arithmeticOperator t ht hd C hC := by
  unfold arithmeticOperator
  simp [V10B8e.arch_selfAdjoint,V10B8c.pole_selfAdjoint,V10B8d.prime_selfAdjoint]

theorem arithmetic_core_diagonal (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C)
    (T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index)
    (hT : V10B6d.LiteralCoordinates t T) (hEF : V10B8b.LiteralEF)
    (g : logCarrier t) (hg : g ∈ SmoothCore t) :
    (inner ℂ (signedGram T g) g).re =
      (inner ℂ (arithmeticOperator t ht hd C hC g) g).re := by
  obtain ⟨f,hf,hfs,hae⟩ := hg
  have hfc : HasCompactSupport f :=
    IsCompact.of_isClosed_subset isCompact_Icc (isClosed_tsupport f) hfs
  rw [V10B8b.diagonal_of_literalEF hEF t T hT g f hf hfc hae]
  unfold arithmeticOperator V10B8b.literatureRHS
  rw [ContinuousLinearMap.sub_apply,ContinuousLinearMap.add_apply,
    inner_sub_left,inner_add_left,
    V10B8c.pole_autocorr t ht g f hf.continuous hfc hae,
    V10B8d.prime_literal t g f hfs hae,
    V10B8g.arch_literal t hd C hC g f hf.continuous hfc hae]
  simp only [V10B8b.primeTerm,V10B8d.primeWeight]
  ring

theorem arithmetic_diagonal (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C)
    (T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index)
    (hT : V10B6d.LiteralCoordinates t T) (hEF : V10B8b.LiteralEF)
    (hcore : Dense (SmoothCore t)) (g : logCarrier t) :
    (inner ℂ (signedGram T g) g).re =
      (inner ℂ (arithmeticOperator t ht hd C hC g) g).re := by
  have h₁ : Continuous (fun v : logCarrier t => (inner ℂ (signedGram T v) v).re) :=
    Complex.continuous_re.comp ((signedGram T).continuous.inner continuous_id)
  have h₂ : Continuous (fun v : logCarrier t =>
      (inner ℂ (arithmeticOperator t ht hd C hC v) v).re) :=
    Complex.continuous_re.comp ((arithmeticOperator t ht hd C hC).continuous.inner continuous_id)
  have he : EqOn (fun v : logCarrier t => (inner ℂ (signedGram T v) v).re)
      (fun v => (inner ℂ (arithmeticOperator t ht hd C hC v) v).re) (SmoothCore t) :=
    fun v hv => arithmetic_core_diagonal t ht hd C hC T hT hEF v hv
  have hc := he.closure h₁ h₂
  exact hc (hcore g)

theorem selfAdjoint_diagonal_real
    (t : ℝ) (S : logCarrier t →L[ℂ] logCarrier t) (hS : S.adjoint = S)
    (g : logCarrier t) : (inner ℂ (S g) g).im = 0 := by
  have h : inner ℂ (S g) g = inner ℂ g (S g) := by
    calc
      inner ℂ (S g) g = inner ℂ (S.adjoint g) g := by rw [hS]
      _ = inner ℂ g (S g) := ContinuousLinearMap.adjoint_inner_left S g g
  have hc := inner_conj_symm (𝕜 := ℂ) (S g) g
  rw [← h] at hc
  have hi := congrArg Complex.im hc
  rw [Complex.conj_im] at hi
  linarith

theorem arithmetic_operator_identity (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C)
    (T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index)
    (hT : V10B6d.LiteralCoordinates t T) (hEF : V10B8b.LiteralEF)
    (hcore : Dense (SmoothCore t)) :
    signedGram T = arithmeticOperator t ht hd C hC := by
  have he : ∀ g : logCarrier t, inner ℂ (signedGram T g) g =
      inner ℂ (arithmeticOperator t ht hd C hC g) g := by
    intro g
    apply Complex.ext
    · exact arithmetic_diagonal t ht hd C hC T hT hEF hcore g
    · rw [selfAdjoint_diagonal_real t _ (V10B6c.signedGram_symmetric T),
        selfAdjoint_diagonal_real t _ (arithmetic_selfAdjoint t ht hd C hC)]
  have h := (ext_inner_map (signedGram T).toLinearMap
      (arithmeticOperator t ht hd C hC).toLinearMap).mp he
  ext g : 1
  exact congrArg (fun L : logCarrier t →ₗ[ℂ] logCarrier t => L g) h

theorem arithmetic_compact_perturbation (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C) :
    ∃ K : logCarrier t →L[ℂ] logCarrier t, IsCompactOperator K ∧
      arithmeticOperator t ht hd C hC = 1+K := by
  refine ⟨correction t hd C hC + poleOperator t ht - primeOperator t, ?_, ?_⟩
  · exact ((V10B8e.correction_compact t ht hd C hC).add
      (V10B8c.pole_compact t ht)).sub (V10B8d.prime_compact t ht)
  · unfold arithmeticOperator archOperator
    abel

theorem pole_physical_bound (t : ℝ) (ht : 0 ≤ t) (g : logCarrier t) :
    ‖inner ℂ (poleOperator t ht g) g‖ ≤
      (2*‖evalRestricted t (1/2) ht‖*‖evalRestricted t (-1/2) ht‖)*
        ‖physicalInclusion t g‖^2 := by
  let p := physicalInclusion t g
  let E := evalRestricted t (1/2) ht
  let F := evalRestricted t (-1/2) ht
  rw [V10B8c.pole_pairing]
  change ‖conj (F p)*E p+conj (E p)*F p‖ ≤ _
  have he := E.le_opNorm p
  have hf := F.le_opNorm p
  calc
    _ ≤ ‖conj (F p)*E p‖+‖conj (E p)*F p‖ := norm_add_le _ _
    _ = 2*(‖E p‖*‖F p‖) := by simp only [norm_mul,Complex.norm_conj]; ring
    _ ≤ 2*((‖E‖*‖p‖)*(‖F‖*‖p‖)) :=
      mul_le_mul_of_nonneg_left (mul_le_mul he hf (norm_nonneg _) (by positivity)) (by norm_num)
    _ = _ := by dsimp [E,F,p]; ring

theorem prime_physical_bound (t : ℝ) (g : logCarrier t) :
    ‖inner ℂ (primeOperator t g) g‖ ≤ ‖physicalPrime t‖*‖physicalInclusion t g‖^2 := by
  unfold primeOperator
  simp only [ContinuousLinearMap.comp_apply,ContinuousLinearMap.adjoint_inner_left]
  calc
    _ ≤ ‖physicalPrime t (physicalInclusion t g)‖*‖physicalInclusion t g‖ :=
      norm_inner_le_norm _ _
    _ ≤ (‖physicalPrime t‖*‖physicalInclusion t g‖)*‖physicalInclusion t g‖ :=
      mul_le_mul_of_nonneg_right ((physicalPrime t).le_opNorm _) (norm_nonneg _)
    _ = _ := by ring

theorem signed_defect (t : ℝ) (ht : 0 ≤ t)
    (hd : Measurable residual) (C : ℝ) (hC : ∀ u, |residual u| ≤ C) (hC0 : 0 ≤ C)
    (T : logCarrier t →L[ℂ] V07C.Coeff V10A.Index)
    (hT : V10B6d.LiteralCoordinates t T) (hEF : V10B8b.LiteralEF)
    (hcore : Dense (SmoothCore t)) :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ g : logCarrier t,
      ‖g‖^2 ≤ ‖analysisChannel true T g‖^2+M*‖physicalInclusion t g‖^2 := by
  let P := 2*‖evalRestricted t (1/2) ht‖*‖evalRestricted t (-1/2) ht‖
  let D := ‖physicalPrime t‖
  refine ⟨C+P+D,by dsimp [P,D]; positivity,?_⟩
  intro g
  have ha := V10B8e.arch_lower t hd C hC g
  have hp := pole_physical_bound t ht g
  have hd' := prime_physical_bound t g
  have hp' := Complex.abs_re_le_norm (inner ℂ (poleOperator t ht g) g)
  have hd'' := Complex.abs_re_le_norm (inner ℂ (primeOperator t g) g)
  have h := arithmetic_diagonal t ht hd C hC T hT hEF hcore g
  rw [V10B6c.signedGram_diagonal] at h
  unfold arithmeticOperator at h
  rw [ContinuousLinearMap.sub_apply,ContinuousLinearMap.add_apply,
    inner_sub_left,inner_add_left,Complex.sub_re,Complex.add_re] at h
  have hpneg := neg_abs_le (inner ℂ (poleOperator t ht g) g).re
  have hdpos := le_abs_self (inner ℂ (primeOperator t g) g).re
  change ‖g‖^2 ≤ ‖analysisChannel true T g‖^2+(C+P+D)*‖physicalInclusion t g‖^2
  dsimp [P,D]
  nlinarith only [ha,hp,hp',hd',hd'',hpneg,hdpos,h,sq_nonneg ‖analysisChannel false T g‖]

end WeilDefect.MasterRecon.V10B8h

#print axioms WeilDefect.MasterRecon.V10B8h.arithmetic_selfAdjoint
#print axioms WeilDefect.MasterRecon.V10B8h.arithmetic_core_diagonal
#print axioms WeilDefect.MasterRecon.V10B8h.arithmetic_diagonal
#print axioms WeilDefect.MasterRecon.V10B8h.selfAdjoint_diagonal_real
#print axioms WeilDefect.MasterRecon.V10B8h.arithmetic_operator_identity
#print axioms WeilDefect.MasterRecon.V10B8h.arithmetic_compact_perturbation
#print axioms WeilDefect.MasterRecon.V10B8h.pole_physical_bound
#print axioms WeilDefect.MasterRecon.V10B8h.prime_physical_bound
#print axioms WeilDefect.MasterRecon.V10B8h.signed_defect
