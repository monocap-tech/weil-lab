import WeilDefect.Arithmetic.ActualZetaOriginalEndpointLiteralStrip
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointActualSeedGraph

namespace WeilDefect
noncomputable section
open MeasureTheory Filter Set
open scoped SchwartzMap ComplexConjugate

/-! NF585: all independently formulated Fourier and L1 inputs
of the literal endpoint graph theorem are now consequences of
closed-collar regularity and the original U/U' estimates.
Authentic binding of U remains separate. -/

theorem neutralNF585OriginalEndpoint_actualSeedGraph_of_C1_bounds
    (U U' : ℝ → ℝ) (hm : Measurable U)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hU' : ContinuousOn U' (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hder : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      HasDerivAt U (U' x) x)
    (h0 : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      |U x| ≤ neutralNF578C0)
    (h1 : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      |U' x| ≤ (7/10^4:ℝ)) :
    let hOpen : ∀ x ∈ Ioo ((11/10:ℝ)-1/500) (11/10:ℝ),
      |U x| ≤ 2/10^7 := fun x hx => h0 x ⟨hx.1.le,hx.2.le⟩
    ∃ (g : ℕ → 𝓢(ℝ,ℂ))
      (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (G : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ)),
      (∀ n x, g n x = (neutralNF583Odd
        (neutralNF582HalfSequence (neutralNF575OriginalEndpointHalf U) n) x:ℂ)) ∧
      (∀ n x, conj (g n x) = g n x) ∧
      (∀ n x, g n (-x) = -g n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → g n x = 0) ∧
      neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) K).val =
        neutralNF575OriginalEndpointL2 U hm hOpen ∧
      (∀ n, neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) (G n)).val =
        (g n).toLp 2 volume) ∧ Tendsto G atTop (nhds K) := by
  dsimp only
  exact neutralNF583OriginalEndpoint_actualSeedGraph U hm _
    (neutralNF585LiteralHalf_integrable U hU) (1/40000) (by norm_num)
    (neutralNF585LiteralHalf_strip U U' hU hU' hder h0 h1)

end
end WeilDefect
