import WeilDefect.Arithmetic.ActualZetaOriginalCollarCoercivity
import WeilDefect.Arithmetic.ActualZetaOriginalResidualSignedMargin

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate

/-- Use the already accepted 2/5 local inequality without depending
on the sharpened coefficient or any physical solve receipt. -/
theorem neutralNF614OriginalMargin_of_box (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (f : ℕ → 𝓢(ℝ,ℂ)),
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ∧
      0 < (1/5:ℝ)*‖neutralNF598GraphPhysical (11/10) K‖^2 ∧
      (1/5:ℝ)*‖neutralNF598GraphPhysical (11/10) K‖^2 <
        neutralNF598GraphWeil (11/10) K ∧
      (∀ n x, conj (f n x) = f n x) ∧
      (∀ n x, f n (-x) = -f n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → f n x = 0) ∧
      (∀ n, neutralNF546OriginalSelectedMoments ((f n).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments (neutralNF598GraphPhysical (11/10) K)) ∧
      (∀ᶠ n in atTop, (1/5:ℝ)*‖(f n).toLp 2 volume‖^2 < neutralNF598SmoothWeil (f n)) :=
  neutralNF608OriginalCorrectedMargin_of_box a b hbox (2/5) (1/5)
    (by norm_num) (by norm_num) neutralNF600SmoothCollarLower

end
end WeilDefect
