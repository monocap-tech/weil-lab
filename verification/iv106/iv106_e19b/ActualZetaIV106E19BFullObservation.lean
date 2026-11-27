import WeilDefect.Arithmetic.ActualZetaIV106C3ActualConstraints
import WeilDefect.Arithmetic.ActualZetaIV106E18VLiteralMatch

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped SchwartzMap FourierTransform ComplexConjugate

/-- The physical map containing the exact C3C constraints, before
composition with the original logarithmic carrier inclusion. -/
def neutralIV106E19BPhysical (N k : ℕ) (hk : 0 < k) :
    RealComplexL2 →L[ℂ] (neutralIV106C3Index N k → ℂ) :=
  ContinuousLinearMap.pi fun j =>
    match j with
    | .inl i => InnerProductSpace.toDual ℂ RealComplexL2
        (neutralIV106C3CellColumn (11/10:ℝ) N i)
    | .inr (.inl _) => neutralSourceWindowMomentCLM (11/10:ℝ) (1/2) -
        neutralSourceWindowMomentCLM (11/10:ℝ) (-(1/2))
    | .inr (.inr (.inl i)) => InnerProductSpace.toDual ℂ RealComplexL2
        ((neutralIV100Carrier k hk i).toLp 2 volume)
    | .inr (.inr (.inr i)) => InnerProductSpace.toDual ℂ RealComplexL2
        (neutralIV105CResponse k hk i)

/-- Factorization through the original physical inclusion, with the
actual C3C index and no omitted cell coordinates. -/
theorem neutralIV106E19BPhysical_eq (N k : ℕ) (hk : 0 < k)
    (p : NeutralLogHilbertCarrier (11/10:ℝ)) :
    neutralIV106E19BPhysical N k hk (neutralLogPhysical p.val) =
      neutralIV106C3Constraints N k hk p := by
  funext j
  rcases j with i | j
  · rfl
  · rcases j with u | j
    · rfl
    · rcases j with i | i <;> rfl

/-- Retain the original E18 observation as well: in particular the two
individual pole moments, not merely their difference. -/
def neutralIV106E19BObserve (N k : ℕ) (hk : 0 < k) :=
  (neutralIV106E19BPhysical N k hk).prod (neutralIV106E18RObserve k hk)

/-- Full finite observation matching in the derivative graph. No rank
or independence premise on the 666+2k original coordinates. -/
theorem neutralIV106E19BFull_match (N k : ℕ) (hk : 0 < k)
    (l h b : ℝ) (hh : 0 < h) (hb : 0 < b) (ε : ℝ) (hε : 0 < ε) :
    let f := (neutralIV106E18JTrial_memLp l h hh).toLp _
    let d := (neutralIV106E18SDTrial_memLp l h hh).toLp _
    ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Set.Icc (l-b) (l+h+b), s x = 0) ∧
      neutralIV106E19BPhysical N k hk (s.toLp 2 volume) =
        neutralIV106E19BPhysical N k hk f ∧
      neutralIV106E18RObserve k hk (s.toLp 2 volume) =
        neutralIV106E18RObserve k hk f ∧
      dist (s.toLp 2 volume) f < ε ∧
      dist ((SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume) d < ε ∧
      (∫ ξ, logarithmicFourierWeight ξ *
        ‖(𝓕 (s.toLp 2 volume-f) : RealComplexL2) ξ‖^2) ≤
        (Real.exp 1+1+‖neutralIV106E18VScale‖^2)*ε^2 := by
  dsimp only
  obtain ⟨s,hs,ho,hf,hd,he⟩ := neutralIV106E18VMatch (l-b) (l+h+b)
    (neutralIV106E19BObserve N k hk)
    ((neutralIV106E18JTrial_memLp l h hh).toLp _)
    ((neutralIV106E18SDTrial_memLp l h hh).toLp _)
    (neutralIV106E18VTrial_graph l h b hh hb) ε hε
  exact ⟨s,hs,congrArg Prod.fst ho,congrArg Prod.snd ho,hf,hd,he⟩

/-- Exact equality of all C3C coordinates for supported smooth and
rough carrier representatives with equal physical observations. -/
theorem neutralIV106E19BConstraints_match (N k : ℕ) (hk : 0 < k)
    (p q : NeutralLogHilbertCarrier (11/10:ℝ))
    (h : neutralIV106E19BPhysical N k hk (neutralLogPhysical p.val) =
      neutralIV106E19BPhysical N k hk (neutralLogPhysical q.val)) :
    neutralIV106C3Constraints N k hk p =
      neutralIV106C3Constraints N k hk q := by
  simpa only [neutralIV106E19BPhysical_eq] using h

#print axioms neutralIV106E19BPhysical_eq
#print axioms neutralIV106E19BFull_match
#print axioms neutralIV106E19BConstraints_match
end
end WeilDefect
