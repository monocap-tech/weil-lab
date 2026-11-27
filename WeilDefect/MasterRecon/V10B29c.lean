import WeilDefect.MasterRecon.V10B29b

/-! V10B29c: transport the monomial singular and beta-convolution
identities through arbitrary finite coefficient banks. -/
namespace WeilDefect.MasterRecon.V10B29c

open MeasureTheory Set Complex
open scoped BigOperators
open V10B29b (poly)

noncomputable def singularCoeff (n : ℕ) (c : ℕ → ℂ) (x : ℝ) : ℂ :=
  ∑ j ∈ Finset.range n, c j*(V10B24a.harmonic j:ℂ)*(x:ℂ)^j/2

theorem singular_poly (n : ℕ) (c : ℕ → ℂ) (x : ℝ) (hx : 0 < x) :
    V10B28a.singular (poly n c) x = singularCoeff n c x := by
  unfold V10B28a.singular singularCoeff
  have he : (fun r : ℝ => ((1/(2*r):ℝ):ℂ)*(poly n c x-poly n c (x-r))) =
      fun r => ∑ j ∈ Finset.range n, c j*
        (((1/(2*r):ℝ):ℂ)*((x:ℂ)^j-((x-r:ℝ):ℂ)^j)) := by
    funext r
    unfold poly
    rw [← Finset.sum_sub_distrib,Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    ring
  rw [he,integral_finset_sum]
  · apply Finset.sum_congr rfl
    intro j _
    rw [integral_const_mul]
    change c j*V10B28a.singular (fun y : ℝ => (y:ℂ)^j) x = _
    rw [V10B29b.singular_monomial j x hx]
    ring
  · intro j _
    have hcont : Continuous (fun r : ℝ => c j*((V10B24a.dd j x r:ℝ):ℂ)/2) := by
      unfold V10B24a.dd
      fun_prop
    have hi := (intervalIntegrable_iff_integrableOn_Ioc_of_le hx.le).mp (hcont.intervalIntegrable volume 0 x)
    apply hi.congr
    rw [ae_restrict_iff' measurableSet_Ioc]
    refine Eventually.of_forall fun r hr => ?_
    rw [V10B24a.dd_eq j x r hr.1.ne']
    push_cast
    field_simp [show (r:ℂ) ≠ 0 by exact_mod_cast hr.1.ne']
    <;> ring

noncomputable def convolutionCoeff (m n : ℕ) (a c : ℕ → ℂ) (x : ℝ) : ℂ :=
  ∑ j ∈ Finset.range m, ∑ k ∈ Finset.range n,
    a j*c k*(x:ℂ)^(j+k+1)*(j.factorial:ℂ)*(k.factorial:ℂ)/((j+k+1).factorial:ℂ)

theorem convolution_poly (m n : ℕ) (a c : ℕ → ℂ) (x : ℝ) (hx : 0 < x) :
    (∫ r in Ioc (0:ℝ) x, poly m a r*poly n c (x-r)) =
      convolutionCoeff m n a c x := by
  have he : (fun r : ℝ => poly m a r*poly n c (x-r)) =
      fun r => ∑ j ∈ Finset.range m, ∑ k ∈ Finset.range n,
        (a j*c k)*((r:ℂ)^j*((x-r:ℝ):ℂ)^k) := by
    funext r
    unfold poly
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro j _
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro k _
    ring
  rw [he,integral_finset_sum]
  · unfold convolutionCoeff
    apply Finset.sum_congr rfl
    intro j _
    rw [integral_finset_sum]
    · apply Finset.sum_congr rfl
      intro k _
      rw [integral_const_mul,← intervalIntegral.integral_of_le hx.le]
      push_cast
      rw [V10B24a.convolution_monomial j k x hx]
      ring
    · intro k _
      exact (intervalIntegrable_iff_integrableOn_Ioc_of_le hx.le).mp
        ((by fun_prop : Continuous (fun r : ℝ => (a j*c k)*((r:ℂ)^j*((x-r:ℝ):ℂ)^k))).intervalIntegrable volume 0 x)
  · intro j _
    exact (intervalIntegrable_iff_integrableOn_Ioc_of_le hx.le).mp
      ((by fun_prop : Continuous (fun r : ℝ => ∑ k ∈ Finset.range n,
        (a j*c k)*((r:ℂ)^j*((x-r:ℝ):ℂ)^k))).intervalIntegrable volume 0 x)

end WeilDefect.MasterRecon.V10B29c

#print axioms WeilDefect.MasterRecon.V10B29c.singular_poly
#print axioms WeilDefect.MasterRecon.V10B29c.convolution_poly
