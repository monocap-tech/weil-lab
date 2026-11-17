import WeilDefect.Arithmetic.ActualZetaOriginalEndpointQualitativeC1Graph
import WeilDefect.Arithmetic.ActualZetaOriginalUnconditionalGraphCorrection

namespace WeilDefect
noncomputable section
open MeasureTheory Filter Set
open scoped SchwartzMap ComplexConjugate

/-! NF596: separate qualitative approximation of the authentic
endpoint family from quantitative signed-certificate work. This
still depends on the canonical graph correction being accepted. -/

theorem neutralNF596NF407CorrectedGraph (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
      (s : ℕ → 𝓢(ℝ,ℂ)) (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (F : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ)),
      let ell := hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b))
      let f := fun n => neutralNF586CorrectedTest ell (s n)
      (∀ n x, s n x = (neutralNF583Odd
        (neutralNF582HalfSequence (neutralNF575OriginalEndpointHalf (neutralNF587Source a b)) n) x:ℂ)) ∧
      neutralNF573OriginalGraphPhysical K = ell ∧
      (∀ n, neutralNF573OriginalGraphPhysical (F n) = (f n).toLp 2 volume) ∧
      (∀ n x, conj (f n x) = f n x) ∧
      (∀ n x, f n (-x) = -f n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → f n x = 0) ∧
      (∀ n, neutralNF546OriginalSelectedMoments ((f n).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments ell) ∧ Tendsto F atTop (nhds K) := by
  obtain ⟨hLp,s,K,G,hge,hgr,hgo,hgs,hK,hG,hlim⟩ := neutralNF596NF407SeedGraph a b
  let ell := hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b))
  have hk : neutralNF573OriginalGraphPhysical K = ell := hK
  have hg (n : ℕ) : neutralNF573OriginalGraphPhysical (G n) = (s n).toLp 2 volume := hG n
  have hr : ∀ᵐ x ∂volume, conj (ell x) = ell x :=
    (neutralNF575OriginalEndpoint_L2_properties (neutralNF587Source a b) hLp).2
  have hrK : ∀ᵐ x ∂volume, conj (neutralNF573OriginalGraphPhysical K x) =
      neutralNF573OriginalGraphPhysical K x := by rw [hk]; exact hr
  obtain ⟨F,hF,hreal,hodd,hsupp,hmom,hconv⟩ :=
    neutralNF586OriginalGraph_correctedSequence K s G hrK hg hgr hgo hgs hlim
  rw [hk] at hF hreal hodd hsupp hmom
  exact ⟨hLp,s,K,F,hge,hk,hF,hreal,hodd,hsupp,hmom,hconv⟩

end
end WeilDefect
