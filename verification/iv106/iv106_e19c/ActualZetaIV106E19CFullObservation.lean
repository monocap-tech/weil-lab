import WeilDefect.Arithmetic.ActualZetaIV106C3ActualConstraints
import WeilDefect.Arithmetic.ActualZetaIV106E18WNativePerturbation

namespace WeilDefect
noncomputable section
open MeasureTheory Set InnerProductSpace ContinuousLinearMap FourierTransform
open scoped SchwartzMap FourierTransform

/-- Include every actual terminal cell and packed mass row, in addition to
the existing moment and response observation. No global-mean substitution. -/
def neutralIV106E19CObserve (k : ℕ) (hk : 0 < k) :
    RealComplexL2 →L[ℂ]
      (((ℂ × ℂ) × (ℂ × (Fin k → ℂ))) × ((Fin 665 → ℂ) × (Fin k → ℂ))) :=
  (neutralIV106E18RObserve k hk).prod
    ((ContinuousLinearMap.pi fun i =>
      InnerProductSpace.toDual ℂ RealComplexL2
        (neutralIV106C3CellColumn (11/10:ℝ) 665 i)).prod
    (ContinuousLinearMap.pi fun i =>
      InnerProductSpace.toDual ℂ RealComplexL2
        ((neutralIV100Carrier k hk i).toLp 2 volume)))

/-- Exact preservation of the ENTIRE native constraint map follows from
the full physical observation and literal original carrier representatives. -/
theorem neutralIV106E19CConstraints_match (k : ℕ) (hk : 0 < k)
    (p q : NeutralLogHilbertCarrier (11/10:ℝ))
    (h : neutralIV106E19CObserve k hk (neutralLogPhysical p.val) =
      neutralIV106E19CObserve k hk (neutralLogPhysical q.val)) :
    neutralIV106C3Constraints 665 k hk p = neutralIV106C3Constraints 665 k hk q := by
  have ho := congrArg Prod.fst h
  change neutralIV106E18RObserve k hk (neutralLogPhysical p.val) =
    neutralIV106E18RObserve k hk (neutralLogPhysical q.val) at ho
  have hm := (neutralIV106E18RObserve_moments k hk _ _ ho).1
  funext j
  rcases j with i | j
  · change inner ℂ (neutralIV106C3CellColumn (11/10:ℝ) 665 i)
      (neutralLogPhysical p.val) = inner ℂ (neutralIV106C3CellColumn (11/10:ℝ) 665 i)
      (neutralLogPhysical q.val)
    simpa [neutralIV106E19CObserve,InnerProductSpace.toDual_apply_apply] using
      congrArg (fun z => z.2.1 i) h
  · rcases j with u | j
    · change neutralLogMoment (11/10:ℝ) (1/2) p -
        neutralLogMoment (11/10:ℝ) (-(1/2)) p =
        neutralLogMoment (11/10:ℝ) (1/2) q -
        neutralLogMoment (11/10:ℝ) (-(1/2)) q
      rw [neutralLogMoment_eq,neutralLogMoment_eq,neutralLogMoment_eq,neutralLogMoment_eq]
      have hminus := congrArg Prod.fst hm
      have hplus := congrArg Prod.snd hm
      change sourceWindowMoment (11/10:ℝ) (-(1/2)) (neutralLogPhysical p.val) =
        sourceWindowMoment (11/10:ℝ) (-(1/2)) (neutralLogPhysical q.val) at hminus
      change sourceWindowMoment (11/10:ℝ) (1/2) (neutralLogPhysical p.val) =
        sourceWindowMoment (11/10:ℝ) (1/2) (neutralLogPhysical q.val) at hplus
      rw [hminus,hplus]
    · rcases j with i | i
      · change inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
          (neutralLogPhysical p.val) = inner ℂ ((neutralIV100Carrier k hk i).toLp 2 volume)
          (neutralLogPhysical q.val)
        simpa [neutralIV106E19CObserve,InnerProductSpace.toDual_apply_apply] using
          congrArg (fun z => z.2.2 i) h
      · exact neutralIV106E18RObserve_row k hk _ _ ho i

/-- Upgrade the joint-graph approximation to preserve every terminal row,
including the cell means on the neighboring cells touched by smoothing. -/
theorem neutralIV106E19CMatch (k : ℕ) (hk : 0 < k)
    (A B : ℝ) (f d : RealComplexL2)
    (h : (f,d) ∈ neutralIV106E18UGraphSpace A B)
    (hw : Icc A B ⊆ Icc (-(11/10:ℝ)) (11/10))
    (p : NeutralLogHilbertCarrier (11/10:ℝ))
    (hp : neutralLogPhysical p.val = f)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Icc A B, s x = 0) ∧
      ∃ hs : ∀ x ∉ Icc (-(11/10:ℝ)) (11/10), s x = 0,
        neutralIV106C3Constraints 665 k hk (neutralIV102Lift _ s hs) =
          neutralIV106C3Constraints 665 k hk p ∧
        ‖neutralIV102Lift (11/10:ℝ) s hs-p‖ ≤ neutralIV106E18WConstant*ε := by
  obtain ⟨s,hs,ho,_,_,he⟩ := neutralIV106E18VMatch A B
    (neutralIV106E19CObserve k hk) f d h ε hε
  have hs' : ∀ x ∉ Icc (-(11/10:ℝ)) (11/10), s x = 0 :=
    fun x hx => hs x (fun hi => hx (hw hi))
  refine ⟨s,hs,hs',?_,?_⟩
  · apply neutralIV106E19CConstraints_match k hk
    rw [neutralIV102Lift_physical,hp]
    exact ho
  · rw [neutralIV106E18VScale_sq] at he
    exact neutralIV106E18WLift_error _ p s hs' f hp ε hε.le he

#print axioms neutralIV106E19CConstraints_match
#print axioms neutralIV106E19CMatch
end
end WeilDefect
