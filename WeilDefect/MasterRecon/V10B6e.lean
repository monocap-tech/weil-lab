import WeilDefect.MasterRecon.V10A
import Mathlib.Analysis.SpecialFunctions.Gamma.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.Analytic.Order

/-! V10B6e: native functional-equation transport of analytic order.
Conjugation of zeta values and analytic orders are separate explicit
inputs to the final same-height reflection receiver. -/
namespace WeilDefect.MasterRecon.V10B6e

open Set Filter
open scoped Topology ComplexConjugate

def strip : Set ℂ := {z | 0 < z.re ∧ z.re < 1}

theorem strip_open : IsOpen strip := by
  exact (isOpen_lt continuous_const Complex.continuous_re).inter
    (isOpen_lt Complex.continuous_re continuous_const)

theorem strip_ne_one {z : ℂ} (hz : z ∈ strip) : z ≠ 1 := by
  intro h
  have h' := hz.2
  rw [h, Complex.one_re] at h'
  exact (lt_irrefl _ h')

theorem strip_ne_neg_nat {z : ℂ} (hz : z ∈ strip) (n : ℕ) : z ≠ -(n : ℂ) := by
  intro h
  have hp := hz.1
  rw [h, Complex.neg_re, Complex.natCast_re] at hp
  exact (not_lt_of_ge (neg_nonpos.mpr (Nat.cast_nonneg n))) hp

theorem one_sub_strip {z : ℂ} (hz : z ∈ strip) : 1-z ∈ strip := by
  change 0 < (1-z).re ∧ (1-z).re < 1
  rw [Complex.sub_re, Complex.one_re]
  exact ⟨by linarith [hz.2],by linarith [hz.1]⟩

theorem conj_strip {z : ℂ} (hz : z ∈ strip) : conj z ∈ strip := by
  change 0 < (conj z).re ∧ (conj z).re < 1
  simpa only [Complex.conj_re, strip, mem_setOf_eq] using hz

noncomputable def functionalFactor (z : ℂ) : ℂ :=
  2 * (2 * (Real.pi : ℂ)) ^ (-z) * Complex.Gamma z * Complex.cos (Real.pi*z/2)

theorem factor_analytic {z : ℂ} (hz : z ∈ strip) :
    AnalyticAt ℂ functionalFactor z := by
  have hc : (2 * (Real.pi : ℂ)) ≠ 0 := by
    exact mul_ne_zero (by norm_num) (by exact_mod_cast Real.pi_ne_zero)
  have hd : DifferentiableOn ℂ functionalFactor strip := by
    intro w hw
    have hp : DifferentiableAt ℂ (fun v : ℂ => (2*(Real.pi : ℂ))^(-v)) w :=
      (differentiableAt_id.neg).const_cpow (Or.inl hc)
    have hg := Complex.differentiableAt_Gamma w (strip_ne_neg_nat hw)
    have hcos : DifferentiableAt ℂ (fun v : ℂ => Complex.cos (Real.pi*v/2)) w := by fun_prop
    exact (((differentiableAt_const _).mul hp).mul hg |>.mul hcos).differentiableWithinAt
  exact hd.analyticOnNhd strip_open z hz

theorem zeta_analytic {z : ℂ} (hz : z ∈ strip) : AnalyticAt ℂ riemannZeta z :=
  analyticOn_riemannZeta z (by simpa using strip_ne_one hz)

theorem one_sub_order_ge {z : ℂ} (hz : z ∈ strip) :
    analyticOrderAt riemannZeta z ≤ analyticOrderAt riemannZeta (1-z) := by
  let a : ℂ → ℂ := fun w => 1-w
  have ha : AnalyticAt ℂ a z := by dsimp [a]; fun_prop
  have hd : deriv a z ≠ 0 := by
    have h : HasDerivAt a (-1) z := by
      simpa [a] using (hasDerivAt_id z).const_sub (1 : ℂ)
    rw [h.deriv]
    norm_num
  have hcomp := analyticOrderAt_comp_of_deriv_ne_zero (f := riemannZeta) ha hd
  have he : (riemannZeta ∘ a) =ᶠ[𝓝 z] (fun w => functionalFactor w * riemannZeta w) := by
    filter_upwards [strip_open.mem_nhds hz] with w hw
    exact riemannZeta_one_sub (strip_ne_neg_nat hw) (strip_ne_one hw)
  have hmul : analyticOrderAt (fun w => functionalFactor w * riemannZeta w) z =
      analyticOrderAt functionalFactor z + analyticOrderAt riemannZeta z :=
    analyticOrderAt_mul (factor_analytic hz) (zeta_analytic hz)
  have h := (analyticOrderAt_congr he).trans hmul
  rw [hcomp] at h
  change analyticOrderAt riemannZeta (1-z) =
    analyticOrderAt functionalFactor z + analyticOrderAt riemannZeta z at h
  rw [h]
  exact le_add_left (le_refl _)

theorem one_sub_order {z : ℂ} (hz : z ∈ strip) :
    analyticOrderAt riemannZeta (1-z) = analyticOrderAt riemannZeta z := by
  apply le_antisymm
  · have h := one_sub_order_ge (one_sub_strip hz)
    simpa only [sub_sub_cancel] using h
  · exact one_sub_order_ge hz

theorem one_sub_zero {z : ℂ} (hz : V09D.stripZero z) :
    V09D.stripZero (1-z) := by
  have hs : z ∈ strip := hz.2
  refine ⟨?_, one_sub_strip hs⟩
  rw [riemannZeta_one_sub (strip_ne_neg_nat hs) (strip_ne_one hs), hz.1, mul_zero]

theorem reflection_zero_of_conj
    (hc : ∀ z ∈ strip, riemannZeta (conj z) = conj (riemannZeta z))
    (z : ℂ) (hz : V09D.stripZero z) : V09D.stripZero (V10A.reflect z) := by
  have hs : z ∈ strip := hz.2
  have h : V09D.stripZero (conj z) := by
    refine ⟨?_, conj_strip hs⟩
    rw [hc z hs, hz.1]
    simp
  exact one_sub_zero h

theorem reflection_mult_of_conj_order
    (hc : ∀ z ∈ strip,
      analyticOrderAt riemannZeta (conj z) = analyticOrderAt riemannZeta z)
    (z : ℂ) (hz : V09D.stripZero z) :
    V09D.mult (V10A.reflect z) = V09D.mult z := by
  unfold V09D.mult V10A.reflect
  rw [one_sub_order (conj_strip hz.2), hc z hz.2]

end WeilDefect.MasterRecon.V10B6e

#print axioms WeilDefect.MasterRecon.V10B6e.strip_open
#print axioms WeilDefect.MasterRecon.V10B6e.strip_ne_one
#print axioms WeilDefect.MasterRecon.V10B6e.strip_ne_neg_nat
#print axioms WeilDefect.MasterRecon.V10B6e.one_sub_strip
#print axioms WeilDefect.MasterRecon.V10B6e.conj_strip
#print axioms WeilDefect.MasterRecon.V10B6e.factor_analytic
#print axioms WeilDefect.MasterRecon.V10B6e.zeta_analytic
#print axioms WeilDefect.MasterRecon.V10B6e.one_sub_order_ge
#print axioms WeilDefect.MasterRecon.V10B6e.one_sub_order
#print axioms WeilDefect.MasterRecon.V10B6e.one_sub_zero
#print axioms WeilDefect.MasterRecon.V10B6e.reflection_zero_of_conj
#print axioms WeilDefect.MasterRecon.V10B6e.reflection_mult_of_conj_order
