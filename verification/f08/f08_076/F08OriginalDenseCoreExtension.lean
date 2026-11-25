import WeilDefect.Generated.F08.OriginalSchwartzHilbertCore
import WeilDefect.Arithmetic.ActualZetaNativeFormOperator
import WeilDefect.Arithmetic.ActualZetaLogCarrierSchwartzCompact
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap Topology InnerProduct

def f08_076_core (a : ℝ) : Set (NeutralLogHilbertCarrier a) :=
  {q | ∃ s : 𝓢(ℝ, ℂ), tsupport (s : ℝ → ℂ) ⊆ Set.Ioo (-a) a ∧
    neutralLogPhysical q.val = s.toLp 2 volume}

def f08_076_native (a : ℝ) (p q : NeutralLogHilbertCarrier a) : ℂ :=
  inner ℂ p (neutralActualZetaLogWeilFormOperator a q)

/-- Literal original arithmetic source, not a substitute PSD pairing. -/
def f08_076_literal (a : ℝ) (s t : 𝓢(ℝ, ℂ)) : ℂ :=
  Zeta23.EF.literatureRHS
    (neutralWindowCorrelation a (s.toLp 2 volume) (t.toLp 2 volume))

/-- Explicit unpaid source-identity premise. This is not assumed globally. -/
def f08_076_attachment (a : ℝ) : Prop :=
  ∀ (p q : NeutralLogHilbertCarrier a) (s t : 𝓢(ℝ, ℂ)),
    tsupport (s : ℝ → ℂ) ⊆ Set.Ioo (-a) a →
    tsupport (t : ℝ → ℂ) ⊆ Set.Ioo (-a) a →
    neutralLogPhysical p.val = s.toLp 2 volume →
    neutralLogPhysical q.val = t.toLp 2 volume →
    f08_076_literal a s t = f08_076_native a p q

theorem f08_076_core_dense (a : ℝ) (ha : 0 < a) :
    Dense (f08_076_core a) := by
  rw [Metric.dense_iff]
  intro k ε hε
  obtain ⟨q,s,hs,_,hp,he⟩ :=
    f08_075_originalSchwartzHilbert_approx a ha k ε hε
  exact ⟨q, ⟨s,hs,hp⟩, by simpa [dist_eq_norm, norm_sub_rev] using he⟩

theorem f08_076_mixed_difference_bound (a : ℝ)
    (p q p' q' : NeutralLogHilbertCarrier a) :
    ‖f08_076_native a p q - f08_076_native a p' q'‖ ≤
      ‖neutralActualZetaLogWeilFormOperator a‖ *
        (‖p-p'‖ * ‖q‖ + ‖p'‖ * ‖q-q'‖) := by
  have he : f08_076_native a p q - f08_076_native a p' q' =
      f08_076_native a (p-p') q + f08_076_native a p' (q-q') := by
    simp only [f08_076_native, inner_sub_left, map_sub, inner_sub_right]
    ring
  rw [he]
  calc
    _ ≤ ‖f08_076_native a (p-p') q‖ + ‖f08_076_native a p' (q-q')‖ :=
      norm_add_le _ _
    _ ≤ ‖neutralActualZetaLogWeilFormOperator a‖ * ‖p-p'‖ * ‖q‖ +
        ‖neutralActualZetaLogWeilFormOperator a‖ * ‖p'‖ * ‖q-q'‖ :=
      add_le_add (neutralActualZetaLogWeilFormOperator_mixed_bound a (p-p') q)
        (neutralActualZetaLogWeilFormOperator_mixed_bound a p' (q-q'))
    _ = _ := by ring

theorem f08_076_native_continuous (a : ℝ) :
    Continuous (fun z : NeutralLogHilbertCarrier a × NeutralLogHilbertCarrier a =>
      f08_076_native a z.1 z.2) := by
  unfold f08_076_native
  exact continuous_fst.inner
    ((neutralActualZetaLogWeilFormOperator a).continuous.comp continuous_snd)

/-- Unique even among separately continuous extensions. -/
theorem f08_076_extension_unique (a : ℝ) (ha : 0 < a)
    (hattach : f08_076_attachment a)
    (C : NeutralLogHilbertCarrier a → NeutralLogHilbertCarrier a → ℂ)
    (hleft : ∀ q, Continuous (fun p => C p q))
    (hright : ∀ p, Continuous (C p))
    (hcore : ∀ (p q : NeutralLogHilbertCarrier a) (s t : 𝓢(ℝ, ℂ)),
      tsupport (s : ℝ → ℂ) ⊆ Set.Ioo (-a) a →
      tsupport (t : ℝ → ℂ) ⊆ Set.Ioo (-a) a →
      neutralLogPhysical p.val = s.toLp 2 volume →
      neutralLogPhysical q.val = t.toLp 2 volume →
      C p q = f08_076_literal a s t) :
    ∀ p q, C p q = f08_076_native a p q := by
  have hd := f08_076_core_dense a ha
  have hbase : ∀ p ∈ f08_076_core a, ∀ q ∈ f08_076_core a,
      C p q = f08_076_native a p q := by
    rintro p ⟨s,hs,hp⟩ q ⟨t,ht,hq⟩
    exact (hcore p q s t hs ht hp hq).trans (hattach p q s t hs ht hp hq)
  have hrow : ∀ p ∈ f08_076_core a, ∀ q, C p q = f08_076_native a p q := by
    intro p hp q
    have hc : Continuous (f08_076_native a p) := by
      unfold f08_076_native
      exact continuous_const.inner (neutralActualZetaLogWeilFormOperator a).continuous
    have hclosed : IsClosed {q | C p q = f08_076_native a p q} :=
      isClosed_eq (hright p) hc
    have hsub : f08_076_core a ⊆ {q | C p q = f08_076_native a p q} :=
      fun q hq => hbase p hp q hq
    exact closure_minimal hsub hclosed (hd q)
  intro p q
  have hc : Continuous (fun p => f08_076_native a p q) := by
    unfold f08_076_native
    exact continuous_id.inner continuous_const
  have hclosed : IsClosed {p | C p q = f08_076_native a p q} :=
    isClosed_eq (hleft q) hc
  have hsub : f08_076_core a ⊆ {p | C p q = f08_076_native a p q} :=
    fun p hp => hrow p hp q
  exact closure_minimal hsub hclosed (hd p)

/-- Conditional equivalence; no positivity is asserted by this theorem. -/
theorem f08_076_core_positivity_iff (a : ℝ) (ha : 0 < a)
    (hattach : f08_076_attachment a) :
    (∀ s : 𝓢(ℝ, ℂ), tsupport (s : ℝ → ℂ) ⊆ Set.Ioo (-a) a →
      0 ≤ (f08_076_literal a s s).re) ↔
    (∀ k : NeutralLogHilbertCarrier a, 0 ≤ (f08_076_native a k k).re) := by
  constructor
  · intro hs k
    have hc : Continuous (fun k : NeutralLogHilbertCarrier a =>
        (f08_076_native a k k).re) :=
      Complex.continuous_re.comp ((f08_076_native_continuous a).comp
        (continuous_id.prodMk continuous_id))
    have hclosed : IsClosed {k : NeutralLogHilbertCarrier a |
        0 ≤ (f08_076_native a k k).re} := isClosed_le continuous_const hc
    have hsub : f08_076_core a ⊆ {k : NeutralLogHilbertCarrier a |
        0 ≤ (f08_076_native a k k).re} := by
      rintro q ⟨s,hsupp,hp⟩
      exact (hattach q q s s hsupp hsupp hp hp) ▸ hs s hsupp
    exact closure_minimal hsub hclosed (f08_076_core_dense a ha k)
  · intro hn s hs
    have hsupport : ∀ᵐ x ∂volume,
        x ∉ Set.Icc (-a) a → (s.toLp 2 volume) x = 0 := by
      filter_upwards [s.coeFn_toLp 2 volume] with x hx hout
      rw [hx]
      by_contra hne
      have hm : x ∈ Function.support (s : ℝ → ℂ) := hne
      have hi := hs (subset_closure hm)
      exact hout ⟨hi.1.le,hi.2.le⟩
    obtain ⟨k,hk⟩ :=
      neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_quadraticMoment
        a (s.toLp 2 volume) hsupport
        (neutralSchwartzPhysical_quadraticFourierMoment s)
    rw [hattach k k s s hs hs hk hk]
    exact hn k

theorem f08_076_negative_witness (a : ℝ) (ha : 0 < a)
    (hattach : f08_076_attachment a) (k : NeutralLogHilbertCarrier a)
    (hk : (f08_076_native a k k).re < 0) :
    ∃ s : 𝓢(ℝ, ℂ), tsupport (s : ℝ → ℂ) ⊆ Set.Ioo (-a) a ∧
      (f08_076_literal a s s).re < 0 := by
  by_contra h
  have hp : ∀ s : 𝓢(ℝ, ℂ), tsupport (s : ℝ → ℂ) ⊆ Set.Ioo (-a) a →
      0 ≤ (f08_076_literal a s s).re := by
    intro s hs
    exact le_of_not_gt (fun hneg => h ⟨s,hs,hneg⟩)
  exact (not_lt_of_ge ((f08_076_core_positivity_iff a ha hattach).mp hp k)) hk

#print axioms f08_076_core_dense
#print axioms f08_076_mixed_difference_bound
#print axioms f08_076_native_continuous
#print axioms f08_076_extension_unique
#print axioms f08_076_core_positivity_iff
#print axioms f08_076_negative_witness

end
end WeilDefect
