import WeilDefect.Arithmetic.ActualZetaOriginalNF407SourceBinding
import WeilDefect.Arithmetic.ActualZetaOriginalNormalizedCauchySeries
import WeilDefect.Arithmetic.ActualZetaOriginalU400NormalizedBudget

namespace WeilDefect
noncomputable section
open Set

/-! NF588: literal complexification of the same 242+4 source
with normalized variable w=(B-x)/delta. The primitive source,
Cauchy coefficient, and differentiated coefficient use identical
coefficient choices. -/

def neutralNF588SelectedComplex (j : Fin 242) (z : ℂ) : ℂ :=
  if hj : j.val < 241 then
    let node := nf545OriginalOscillatorNodeAt ⟨j.val,hj⟩
    z^node.2 * (if Even node.2 then
      Complex.sin (2*(Real.pi:ℂ)*(node.1:ℂ)*z)
      else Complex.cos (2*(Real.pi:ℂ)*(node.1:ℂ)*z))
  else Complex.sinh (z/2)

def neutralNF588CriticalComplex (j : Fin 4) (z : ℂ) : ℂ :=
  (∑ k : Fin 32, ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℂ) *
      Complex.sin (2*(Real.pi:ℂ)*(neutralNF587CriticalFrequencies[k.val]! : ℂ)*z)) +
    (neutralNF587CriticalPoles[j.val]! : ℂ)*Complex.sinh (z/2)

def neutralNF588SourceComplex (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (z : ℂ) : ℂ :=
  (∑ j : Fin 242, (a j:ℂ)*neutralNF588SelectedComplex j z) +
    ∑ j : Fin 4, (b j:ℂ)*neutralNF588CriticalComplex j z

def neutralNF588NormalizedSource (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (w : ℂ) : ℂ :=
  neutralNF588SourceComplex a b ((11/10:ℂ)-w/500)

theorem neutralNF588SelectedComplex_ofReal (j : Fin 242) (x : ℝ) :
    neutralNF588SelectedComplex j (x:ℂ) =
      (nf545OriginalSelectedRealGenerator j x:ℂ) := by
  unfold neutralNF588SelectedComplex nf545OriginalSelectedRealGenerator
  by_cases hj : j.val < 241
  · simp only [dif_pos hj]
    split_ifs <;> push_cast <;> rfl
  · simp only [dif_neg hj]
    push_cast
    rfl

theorem neutralNF588CriticalComplex_ofReal (j : Fin 4) (x : ℝ) :
    neutralNF588CriticalComplex j (x:ℂ) = (neutralNF587CriticalGenerator j x:ℂ) := by
  unfold neutralNF588CriticalComplex neutralNF587CriticalGenerator
  push_cast
  rfl

theorem neutralNF588SourceComplex_ofReal (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (x : ℝ) :
    neutralNF588SourceComplex a b (x:ℂ) = (neutralNF587Source a b x:ℂ) := by
  unfold neutralNF588SourceComplex neutralNF587Source neutralNF569OriginalRealCombination
  push_cast
  simp only [neutralNF588SelectedComplex_ofReal,neutralNF588CriticalComplex_ofReal]

theorem neutralNF588NormalizedSource_ofReal (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (w : ℝ) :
    neutralNF588NormalizedSource a b (w:ℂ) =
      (neutralNF587Source a b (11/10-w/500):ℂ) := by
  unfold neutralNF588NormalizedSource
  rw [← neutralNF588SourceComplex_ofReal]
  push_cast
  rfl

theorem neutralNF588SelectedComplex_differentiable (j : Fin 242) :
    Differentiable ℂ (neutralNF588SelectedComplex j) := by
  unfold neutralNF588SelectedComplex
  by_cases hj : j.val < 241
  · simp only [dif_pos hj]
    by_cases he : Even (nf545OriginalOscillatorNodeAt ⟨j.val,hj⟩).2
    · simp only [if_pos he]
      fun_prop
    · simp only [if_neg he]
      fun_prop
  · simp only [dif_neg hj]
    fun_prop

theorem neutralNF588CriticalComplex_differentiable (j : Fin 4) :
    Differentiable ℂ (neutralNF588CriticalComplex j) := by
  unfold neutralNF588CriticalComplex
  apply Differentiable.add
  · apply Differentiable.fun_sum
    intro k hk
    fun_prop
  · fun_prop

theorem neutralNF588SourceComplex_differentiable (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    Differentiable ℂ (neutralNF588SourceComplex a b) := by
  unfold neutralNF588SourceComplex
  apply Differentiable.add
  · apply Differentiable.fun_sum
    intro j hj
    exact (neutralNF588SelectedComplex_differentiable j).const_mul (a j:ℂ)
  · apply Differentiable.fun_sum
    intro j hj
    exact (neutralNF588CriticalComplex_differentiable j).const_mul (b j:ℂ)

theorem neutralNF588NormalizedSource_differentiable (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    Differentiable ℂ (neutralNF588NormalizedSource a b) := by
  unfold neutralNF588NormalizedSource
  exact (neutralNF588SourceComplex_differentiable a b).comp (by fun_prop)

theorem neutralNF588NormalizedSource_real_derivative
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (w : ℝ) :
    (deriv (neutralNF588NormalizedSource a b) (w:ℂ)).re =
      -(deriv (neutralNF587Source a b) (11/10-w/500))/500 := by
  have hc := (((neutralNF588NormalizedSource_differentiable a b) (w:ℂ)).hasDerivAt).real_of_complex
  have he : (fun t : ℝ => (neutralNF588NormalizedSource a b (t:ℂ)).re) =
      fun t : ℝ => neutralNF587Source a b (11/10-t/500) := by
    funext t
    rw [neutralNF588NormalizedSource_ofReal]
    simp
  rw [he] at hc
  have hd : HasDerivAt (fun t : ℝ => (11/10:ℝ)-t/500) (-1/500) w := by
    simpa only [id_eq,neg_div] using ((hasDerivAt_id w).div_const 500).const_sub (11/10:ℝ)
  have hu := (neutralNF587Source_hasDerivAt a b (11/10-w/500)).comp w hd
  have h := hc.deriv.symm.trans hu.deriv
  simpa only [Function.comp_apply] using h.trans (by ring)

/-- The remaining numerical gates are explicit: the uniform complex
disc bound and the first 400 canonical Cauchy coefficient enclosures.
The latter are NOT asserted by importing a table. -/
theorem neutralNF588OriginalSource_collar_bounds
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hdisc : ∀ z : ℂ, ‖z‖ = 20 →
      ‖neutralNF588NormalizedSource a b z‖ ≤ (10:ℝ)^400)
    (hjet : ∀ n < 400,
      ‖neutralNF588NormalizedCoefficient (neutralNF588NormalizedSource a b) n‖ ≤
        neutralNF588U400Bound n) :
    (∀ x ∈ Icc (549/500:ℝ) (11/10), |neutralNF587Source a b x| ≤ 2/10^7) ∧
      (∀ x ∈ Icc (549/500:ℝ) (11/10), |deriv (neutralNF587Source a b) x| ≤ 7/10^4) := by
  let F := neutralNF588NormalizedSource a b
  have hF : Differentiable ℂ F := neutralNF588NormalizedSource_differentiable a b
  apply neutralNF588OriginalNormalizedSeries_bounds
    (neutralNF587Source a b) (deriv (neutralNF587Source a b))
    (neutralNF588NormalizedCoefficient F) neutralNF588U400Bound
  · exact neutralNF588NormalizedCoefficient_bound F hF _ hdisc
  · exact hjet
  · intro w hw
    simpa only [F,neutralNF588NormalizedSource_ofReal,Complex.ofReal_re] using
      neutralNF588NormalizedCoefficient_value F hF w
  · intro w hw
    simpa only [F,neutralNF588NormalizedSource_real_derivative] using
      neutralNF588NormalizedCoefficient_derivative F hF w
  · exact neutralNF588U400_value_budget
  · exact neutralNF588U400_derivative_budget

end
end WeilDefect
