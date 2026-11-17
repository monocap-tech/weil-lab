import WeilDefect.Arithmetic.ActualZetaOriginalCollar242GraphCorrection

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap

/-! NF597: the last physical correction identity is naturality of
a linear map, entirely independent of the original Gram implementation.
Prove it before specializing to the enormous actual graph type. -/

theorem neutralNF597CorrectGraph_physical
    {V : Type*} [NormedAddCommGroup V] [NormedSpace ℂ V]
    (P : V →L[ℂ] RealComplexL2)
    (M : NeutralNF543Moments) (R : NeutralNF543RightInverse)
    (MG : V →L[ℂ] (Fin 242 → ℂ))
    (RG : (Fin 242 → ℂ) →L[ℂ] V)
    (hM : ∀ v, MG v = M (P v))
    (hR : ∀ d, P (RG d) = (R d).toLp 2 volume)
    (ell g : V) (s : 𝓢(ℝ,ℂ)) (hs : P g = s.toLp 2 volume) :
    P (neutralNF543CorrectGraph MG RG ell g) =
      (neutralNF543Correct M R (P ell) s).toLp 2 volume := by
  let d := M (P ell) - M (s.toLp 2 volume)
  have hd : MG ell - MG g = d := by rw [hM ell,hM g,hs]
  calc
    P (neutralNF543CorrectGraph MG RG ell g) =
        P g + P (RG (MG ell - MG g)) := by
          unfold neutralNF543CorrectGraph
          exact map_add P _ _
    _ = s.toLp 2 volume + (R d).toLp 2 volume := by rw [hs,hd,hR]
    _ = (s + R d).toLp 2 volume :=
      (map_add (SchwartzMap.toLpCLM ℂ ℂ 2 volume) s (R d)).symm
    _ = (neutralNF543Correct M R (P ell) s).toLp 2 volume := rfl

end
end WeilDefect
