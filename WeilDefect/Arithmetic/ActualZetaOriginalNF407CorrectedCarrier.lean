import WeilDefect.Arithmetic.ActualZetaOriginalNF407SourceBinding
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointCorrectedGraph

namespace WeilDefect
noncomputable section
open MeasureTheory Filter Set
open scoped SchwartzMap ComplexConjugate

/-! NF587: exact source family specialization of the corrected
carrier. The only analytic source inputs are the two collar bounds.
The actual reconstruction must be shown to lie in its frozen box;
a bound on the midpoint alone is not a substitute. -/

def neutralNF587SourceBounds (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) : Prop :=
  (∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
    |neutralNF587Source a b x| ≤ neutralNF578C0) ∧
  (∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
    |deriv (neutralNF587Source a b) x| ≤ (7/10^4:ℝ))

theorem neutralNF587Source_correctedGraph
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hcert : ∀ a b, neutralNF587SourceInFrozenBox a b →
      neutralNF587SourceBounds a b)
    (hbox : neutralNF587SourceInFrozenBox a b) :
    let U := neutralNF587Source a b
    let hm := neutralNF587Source_measurable a b
    let hOpen : ∀ x ∈ Ioo ((11/10:ℝ)-1/500) (11/10:ℝ),
      |U x| ≤ 2/10^7 := fun x hx => (hcert a b hbox).1 x ⟨hx.1.le,hx.2.le⟩
    let ell := neutralNF575OriginalEndpointL2 U hm hOpen
    ∃ (s : ℕ → 𝓢(ℝ,ℂ)) (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (F : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ)),
      let f := fun n => neutralNF586CorrectedTest ell (s n)
      (∀ n x, s n x = (neutralNF583Odd
        (neutralNF582HalfSequence (neutralNF575OriginalEndpointHalf U) n) x:ℂ)) ∧
      neutralNF573OriginalGraphPhysical K = ell ∧
      (∀ n, neutralNF573OriginalGraphPhysical (F n) = (f n).toLp 2 volume) ∧
      (∀ n x, conj (f n x) = f n x) ∧
      (∀ n x, f n (-x) = -f n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → f n x = 0) ∧
      (∀ n, neutralNF546OriginalSelectedMoments ((f n).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments ell) ∧
      Tendsto F atTop (nhds K) := by
  exact neutralNF586OriginalEndpoint_correctedGraph_of_C1_bounds
    (neutralNF587Source a b) (deriv (neutralNF587Source a b))
    (neutralNF587Source_measurable a b)
    (neutralNF587Source_contDiff a b).continuous.continuousOn
    (neutralNF587Source_derivative_continuous a b).continuousOn
    (fun x _ => neutralNF587Source_hasDerivAt a b x)
    (hcert a b hbox).1 (hcert a b hbox).2

end
end WeilDefect
