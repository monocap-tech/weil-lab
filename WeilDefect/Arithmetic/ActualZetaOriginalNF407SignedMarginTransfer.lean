import WeilDefect.Arithmetic.ActualZetaOriginalGraphPhysicalUniqueness
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointQualitativeCorrectedGraph

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate

/-! NF598: conditional signed transfer for the ORIGINAL smooth
moment-corrected sequence. The target is an independently supplied
actual graph vector with the same physical carrier; uniqueness
identifies it with the qualitative approximation limit. No sign of
the target, solve-box custody or global positivity is asserted. -/

theorem neutralNF598NF407SmoothMargin
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
    (K : NeutralActualZetaSourceDomain (11/10:ℝ))
    (hK : neutralNF598GraphPhysical (11/10) K =
      hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)))
    (c : ℝ)
    (hmargin : c * ‖neutralNF598GraphPhysical (11/10) K‖^2 <
      neutralNF598GraphWeil (11/10) K) :
    ∃ f : ℕ → 𝓢(ℝ,ℂ),
      (∀ n x, conj (f n x) = f n x) ∧
      (∀ n x, f n (-x) = -f n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → f n x = 0) ∧
      (∀ n, neutralNF546OriginalSelectedMoments ((f n).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments (neutralNF598GraphPhysical (11/10) K)) ∧
      (∀ᶠ n in atTop, c * ‖(f n).toLp 2 volume‖^2 <
        neutralNF598SmoothWeil (f n)) := by
  obtain ⟨hLp',s,L,F,hseed,hL,hF,hreal,hodd,hsupp,hmom,hconv⟩ :=
    neutralNF596NF407CorrectedGraph a b
  let ell := hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b))
  let f := fun n => neutralNF586CorrectedTest ell (s n)
  have hL' : neutralNF598GraphPhysical (11/10) L = ell := hL
  have he : L = K := neutralNF598GraphPhysical_injective (11/10)
    (hL'.trans hK.symm)
  have hp (n : ℕ) : neutralNF598GraphPhysical (11/10) (F n) =
      (f n).toLp 2 volume := hF n
  have ht : Tendsto F atTop (nhds K) := he ▸ hconv
  refine ⟨f,hreal,hodd,hsupp,?_,?_⟩
  · intro n
    rw [hK]
    exact hmom n
  · exact neutralNF598SmoothMargin_eventually K F f c hp hsupp ht hmargin

end
end WeilDefect
