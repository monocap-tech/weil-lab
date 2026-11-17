import WeilDefect.Arithmetic.ActualZetaOriginalEndpointC1SeedGraph
import WeilDefect.Arithmetic.ActualZetaOriginalUnconditionalGraphCorrection

namespace WeilDefect
noncomputable section
open MeasureTheory Filter Set
open scoped SchwartzMap ComplexConjugate

/-! NF586: original corrected endpoint sequence, conditional
only on the explicit original U/U' hypotheses. No separate
positivity of the Gram, graph-admission or convergence premise. -/

theorem neutralNF586OriginalEndpoint_correctedGraph_of_C1_bounds
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
  dsimp only
  let hOpen : ∀ x ∈ Ioo ((11/10:ℝ)-1/500) (11/10:ℝ),
      |U x| ≤ 2/10^7 := fun x hx => h0 x ⟨hx.1.le,hx.2.le⟩
  let ell := neutralNF575OriginalEndpointL2 U hm hOpen
  obtain ⟨s,K,G,hge,hgr,hgo,hgs,hK,hG,hlim⟩ :=
    neutralNF585OriginalEndpoint_actualSeedGraph_of_C1_bounds U U' hm hU hU'
      hder h0 h1
  have hk : neutralNF573OriginalGraphPhysical K = ell := hK
  have hg (n : ℕ) : neutralNF573OriginalGraphPhysical (G n) = (s n).toLp 2 volume := hG n
  have hr : ∀ᵐ x ∂volume, conj (ell x) = ell x :=
    (neutralNF575OriginalEndpoint_L2_properties U
      (neutralNF575OriginalEndpoint_memLp U hm (2/10^7) (by norm_num) hOpen)).2
  have hrK : ∀ᵐ x ∂volume, conj (neutralNF573OriginalGraphPhysical K x) =
      neutralNF573OriginalGraphPhysical K x := by rw [hk]; exact hr
  obtain ⟨F,hF,hreal,hodd,hsupp,hmom,hconv⟩ :=
    neutralNF586OriginalGraph_correctedSequence K s G hrK hg hgr hgo hgs hlim
  rw [hk] at hF hreal hodd hsupp hmom
  exact ⟨s,K,F,hge,hk,hF,hreal,hodd,hsupp,hmom,hconv⟩

end
end WeilDefect
