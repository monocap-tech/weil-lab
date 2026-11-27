import WeilDefect.MasterRecon.V10A
import Mathlib.Analysis.Calculus.Deriv.Star
import Mathlib.Analysis.Analytic.Order
import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.NumberTheory.LSeries.ZetaZeros

/-! V10B6g: zeta conjugation and analytic multiplicity.
Independent of the multiplier, sampling and one-sub functional-equation
modules. Conjugation is proved by the Dirichlet series and identity
principle on the punctured complex plane, not assumed as an axiom. -/
namespace WeilDefect.MasterRecon.V10B6g

open Set Filter
open scoped Topology ComplexConjugate

noncomputable def conjugateFunction (f : ℂ → ℂ) : ℂ → ℂ :=
  conj ∘ f ∘ conj

theorem conjugate_deriv (f : ℂ → ℂ) :
    deriv (conjugateFunction f) = conjugateFunction (deriv f) := by
  exact deriv_conj_conj

theorem conjugate_iteratedDeriv (f : ℂ → ℂ) (n : ℕ) :
    iteratedDeriv n (conjugateFunction f) =
      conjugateFunction (iteratedDeriv n f) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [iteratedDeriv_succ,iteratedDeriv_succ,ih,conjugate_deriv]

theorem conjugate_differentiableAt (f : ℂ → ℂ) (z : ℂ)
    (hf : DifferentiableAt ℂ f (conj z)) :
    DifferentiableAt ℂ (conjugateFunction f) z :=
  differentiableAt_conj_conj_iff.mpr hf

def punctured : Set ℂ := ({1} : Set ℂ)ᶜ

theorem punctured_open : IsOpen punctured := isOpen_compl_singleton

theorem punctured_connected : IsConnected punctured :=
  isConnected_compl_singleton_of_one_lt_rank (by simp) 1

theorem conj_ne_one (z : ℂ) (hz : z ≠ 1) : conj z ≠ 1 := by
  intro h
  apply hz
  have he := congrArg (fun w : ℂ => conj w) h
  simpa using he

theorem zeta_conjugate_analytic :
    AnalyticOnNhd ℂ (conjugateFunction riemannZeta) punctured := by
  apply DifferentiableOn.analyticOnNhd _ punctured_open
  intro z hz
  have hz' : z ≠ 1 := by simpa [punctured] using hz
  exact (conjugate_differentiableAt _ z
    (differentiableAt_riemannZeta (conj_ne_one z hz'))).differentiableWithinAt

theorem zeta_conjugate_dirichlet (z : ℂ) (hz : 1 < z.re) :
    riemannZeta (conj z) = conj (riemannZeta z) := by
  have hz' : 1 < (conj z).re := by simpa only [Complex.conj_re] using hz
  rw [zeta_eq_tsum_one_div_nat_cpow hz', zeta_eq_tsum_one_div_nat_cpow hz,
    Complex.conj_tsum]
  apply tsum_congr
  intro n
  have ha : (n : ℂ).arg ≠ Real.pi := by
    rw [Complex.natCast_arg]
    exact Real.pi_ne_zero.symm
  rw [Complex.cpow_conj _ _ ha]
  simp

theorem zeta_conjugateFunction_eqOn :
    EqOn (conjugateFunction riemannZeta) riemannZeta punctured := by
  have hnear : ∀ᶠ z : ℂ in 𝓝 (2:ℂ), 1 < z.re :=
    (isOpen_lt continuous_const Complex.continuous_re).mem_nhds (by norm_num)
  have hEq : ∀ᶠ z : ℂ in 𝓝 (2:ℂ),
      conjugateFunction riemannZeta z = riemannZeta z := by
    filter_upwards [hnear] with z hz
    change conj (riemannZeta (conj z)) = riemannZeta z
    rw [zeta_conjugate_dirichlet z hz,conj_conj]
  have hfreq : ∃ᶠ z : ℂ in 𝓝[≠] (2:ℂ),
      conjugateFunction riemannZeta z = riemannZeta z :=
    (hEq.filter_mono nhdsWithin_le_nhds).frequently
  exact zeta_conjugate_analytic.eqOn_of_preconnected_of_frequently_eq
    analyticOn_riemannZeta punctured_connected.isPreconnected
    (by norm_num [punctured] : (2:ℂ) ∈ punctured) hfreq

theorem zeta_conjugate_value (z : ℂ) (hz : z ≠ 1) :
    riemannZeta (conj z) = conj (riemannZeta z) := by
  have h := zeta_conjugateFunction_eqOn (show z ∈ punctured by simpa [punctured] using hz)
  have he := congrArg (fun w : ℂ => conj w) h
  simpa [conjugateFunction,Function.comp_def] using he

theorem conjugate_order (f : ℂ → ℂ) (z : ℂ)
    (hf : AnalyticAt ℂ f (conj z)) :
    analyticOrderAt (conjugateFunction f) z = analyticOrderAt f (conj z) := by
  have hfc : AnalyticAt ℂ (conjugateFunction f) z :=
    (conjugate_differentiableAt f z hf.differentiableAt).analyticAt
  apply ENat.eq_of_forall_natCast_le_iff
  intro n
  rw [natCast_le_analyticOrderAt_iff_iteratedDeriv_eq_zero hfc,
    natCast_le_analyticOrderAt_iff_iteratedDeriv_eq_zero hf]
  simp only [conjugate_iteratedDeriv,conjugateFunction,Function.comp_apply,map_eq_zero]

theorem zeta_conjugate_order (z : ℂ) (hz : z ≠ 1) :
    analyticOrderAt riemannZeta (conj z) = analyticOrderAt riemannZeta z := by
  have hconj := conjugate_order riemannZeta z
    (analyticOn_riemannZeta (conj z) (by simpa using conj_ne_one z hz))
  have he : conjugateFunction riemannZeta =ᶠ[𝓝 z] riemannZeta := by
    filter_upwards [punctured_open.mem_nhds (show z ∈ punctured by simpa [punctured] using hz)] with w hw
    exact zeta_conjugateFunction_eqOn hw
  exact hconj.symm.trans (analyticOrderAt_congr he)

theorem zeta_order_finite (z : ℂ) (hz : z ≠ 1) :
    analyticOrderAt riemannZeta z ≠ ⊤ := by
  have h2 : riemannZeta (2:ℂ) ≠ 0 :=
    riemannZeta_ne_zero_of_one_le_re (by norm_num)
  have ho2 : analyticOrderAt riemannZeta (2:ℂ) = 0 :=
    analyticOrderAt_eq_zero.mpr (Or.inr h2)
  apply analyticOn_riemannZeta.analyticOrderAt_ne_top_of_isPreconnected
    punctured_connected.isPreconnected (x := (2:ℂ))
    (by norm_num) (by simpa using hz)
  rw [ho2]
  simp

theorem strip_mult_positive (z : ℂ) (hz : V09D.stripZero z) :
    0 < V09D.mult z := by
  have h1 : z ≠ 1 := by
    intro h
    have hh := hz.2.2
    rw [h,Complex.one_re] at hh
    exact lt_irrefl _ hh
  have ha := analyticOn_riemannZeta z (by simpa using h1)
  have hn : analyticOrderAt riemannZeta z ≠ 0 :=
    analyticOrderAt_ne_zero.mpr ⟨ha,hz.1⟩
  exact ENat.toNat_pos hn (zeta_order_finite z h1)

end WeilDefect.MasterRecon.V10B6g

#print axioms WeilDefect.MasterRecon.V10B6g.conjugate_deriv
#print axioms WeilDefect.MasterRecon.V10B6g.conjugate_iteratedDeriv
#print axioms WeilDefect.MasterRecon.V10B6g.conjugate_differentiableAt
#print axioms WeilDefect.MasterRecon.V10B6g.punctured_open
#print axioms WeilDefect.MasterRecon.V10B6g.punctured_connected
#print axioms WeilDefect.MasterRecon.V10B6g.conj_ne_one
#print axioms WeilDefect.MasterRecon.V10B6g.zeta_conjugate_analytic
#print axioms WeilDefect.MasterRecon.V10B6g.zeta_conjugate_dirichlet
#print axioms WeilDefect.MasterRecon.V10B6g.zeta_conjugateFunction_eqOn
#print axioms WeilDefect.MasterRecon.V10B6g.zeta_conjugate_value
#print axioms WeilDefect.MasterRecon.V10B6g.conjugate_order
#print axioms WeilDefect.MasterRecon.V10B6g.zeta_conjugate_order
#print axioms WeilDefect.MasterRecon.V10B6g.zeta_order_finite
#print axioms WeilDefect.MasterRecon.V10B6g.strip_mult_positive
