import WeilDefect.Arithmetic.ActualZetaOriginalCollar242Correction

namespace WeilDefect
noncomputable section
open Filter

/-!
NF543: topology of the exact finite-rank 242 correction in a genuine
normed full-source graph. This is a structural theorem: it applies to
the actual original all-divisor P/N source graph only after its
specific moment and correction maps are proved bounded there.
-/

/-- Finite-rank moment correction in an arbitrary normed source graph.
The same formula can be used on the TRUE physical+P/N graph when the
source-specific bounded maps are constructed. -/
def neutralNF543CorrectGraph
    {V : Type*} [NormedAddCommGroup V] [NormedSpace ℂ V]
    (M : V →L[ℂ] (Fin 242 → ℂ))
    (R : (Fin 242 → ℂ) →L[ℂ] V)
    (ell g : V) : V :=
  g + R (M ell - M g)

/-- Exact equality of all 242 original moment components, assuming
the true finite-rank graph right-inverse identity. -/
theorem neutralNF543CorrectGraph_moments
    {V : Type*} [NormedAddCommGroup V] [NormedSpace ℂ V]
    (M : V →L[ℂ] (Fin 242 → ℂ))
    (R : (Fin 242 → ℂ) →L[ℂ] V)
    (hMR : ∀ d : Fin 242 → ℂ, M (R d) = d)
    (ell g : V) :
    M (neutralNF543CorrectGraph M R ell g) = M ell := by
  unfold neutralNF543CorrectGraph
  rw [map_add, hMR]
  abel

/-- If the original uncorrected smooth approximants converge in the
COMPLETE source graph, the 242-moment corrected approximants also
converge in precisely the SAME graph. No weak/physical-only
substitution is made. The actual source-specific M and R remain
separate proof obligations. -/
theorem neutralNF543CorrectGraph_tendsto
    {V ι : Type*}
    [NormedAddCommGroup V] [NormedSpace ℂ V]
    {l : Filter ι}
    (M : V →L[ℂ] (Fin 242 → ℂ))
    (R : (Fin 242 → ℂ) →L[ℂ] V)
    (ell : V) (g : ι → V)
    (hg : Tendsto g l (nhds ell)) :
    Tendsto (fun s => neutralNF543CorrectGraph M R ell (g s))
      l (nhds ell) := by
  have hc : Continuous (fun v : V => v + R (M ell - M v)) :=
    continuous_id.add
      (R.continuous.comp (continuous_const.sub M.continuous))
  have hlim : Tendsto (fun s => g s + R (M ell - M (g s))) l
      (nhds (ell + R (M ell - M ell))) :=
    hc.continuousAt.tendsto.comp hg
  simpa [neutralNF543CorrectGraph] using hlim

end
end WeilDefect
