import WeilDefect.Arithmetic.ActualZetaOriginalSignedGraphLimit
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointQualitativeC1Graph

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap

/-! NF599: support-localized positivity is independent of the
canonical moment correction. Use the now-certified qualitative
uncorrected seed graph and the literal smooth Weil identity.
The analytic two-collar inequality is a separate premise; it is
not deduced from Gram positivity or endpoint negativity. -/

def neutralNF599SmoothCollarLower (c : ℝ) : Prop :=
  ∀ s : 𝓢(ℝ,ℂ), (∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) →
    c * ‖s.toLp 2 volume‖^2 ≤ neutralNF598SmoothWeil s

theorem neutralNF599GraphLower_closed (c : ℝ) :
    IsClosed {u : NeutralActualZetaSourceDomain (11/10:ℝ) |
      c * ‖neutralNF598GraphPhysical (11/10) u‖^2 ≤
        neutralNF598GraphWeil (11/10) u} := by
  exact isClosed_le
    (continuous_const.mul ((neutralNF598GraphPhysical_continuous (11/10)).norm.pow 2))
    (neutralNF598GraphWeil_continuous (11/10))

theorem neutralNF599GraphLower_of_sequence
    (c : ℝ) (hlocal : neutralNF599SmoothCollarLower c)
    (K : NeutralActualZetaSourceDomain (11/10:ℝ))
    (F : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ))
    (s : ℕ → 𝓢(ℝ,ℂ))
    (hp : ∀ n, neutralNF598GraphPhysical (11/10) (F n) = (s n).toLp 2 volume)
    (hs : ∀ n x, x ∉ neutralNF543OriginalCollars → s n x = 0)
    (hlim : Tendsto F atTop (nhds K)) :
    c * ‖neutralNF598GraphPhysical (11/10) K‖^2 ≤
      neutralNF598GraphWeil (11/10) K := by
  apply (neutralNF599GraphLower_closed c).mem_of_tendsto hlim
  apply Filter.Eventually.of_forall
  intro n
  change c * ‖neutralNF598GraphPhysical (11/10) (F n)‖^2 ≤
    neutralNF598GraphWeil (11/10) (F n)
  rw [neutralNF598GraphWeil_eq_smooth (F n) (s n) (hs n) (hp n),hp n]
  exact hlocal (s n) (hs n)

theorem neutralNF599NF407GraphLower (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (c : ℝ) (hlocal : neutralNF599SmoothCollarLower c) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ∧
      c * ‖neutralNF598GraphPhysical (11/10) K‖^2 ≤
        neutralNF598GraphWeil (11/10) K := by
  obtain ⟨hLp,s,K,G,hseed,hreal,hodd,hsupp,hK,hG,hconv⟩ :=
    neutralNF596NF407SeedGraph a b
  exact ⟨hLp,K,hK,neutralNF599GraphLower_of_sequence c hlocal K G s hG hsupp hconv⟩

theorem neutralNF599Graph_positive_of_lower
    (K : NeutralActualZetaSourceDomain (11/10:ℝ)) (c : ℝ)
    (hc : 0 < c)
    (hne : neutralNF598GraphPhysical (11/10) K ≠ 0)
    (h : c * ‖neutralNF598GraphPhysical (11/10) K‖^2 ≤
      neutralNF598GraphWeil (11/10) K) :
    0 < neutralNF598GraphWeil (11/10) K :=
  (mul_pos hc (sq_pos_of_pos (norm_pos_iff.mpr hne))).trans_le h

end
end WeilDefect
