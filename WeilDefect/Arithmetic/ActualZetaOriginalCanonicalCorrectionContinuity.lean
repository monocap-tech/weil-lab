import WeilDefect.Arithmetic.ActualZetaOriginalCanonicalCorrectionCore

namespace WeilDefect
noncomputable section
open Filter
set_option maxHeartbeats 20000000
set_option maxRecDepth 10000

/-- A single bounded graph correction preserves every convergent
seed family in the complete source topology. The convergence of
the uncorrected seeds to the original target is STILL a hypothesis. -/
theorem neutralNF573OriginalGraphCorrection_preservesConvergence
    {ι : Type*} {l : Filter ι}
    (R : (Fin 242 → ℂ) →L[ℂ] NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (ell : NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (g : ι → NeutralActualZetaSourceDomain (11 / 10 : ℝ))
    (hg : Tendsto g l (nhds ell)) :
    Tendsto (fun s => neutralNF543CorrectGraph
      neutralNF573OriginalGraphMoments R ell (g s)) l (nhds ell) := by
  have hM : Tendsto (fun i => neutralNF573OriginalGraphMoments (g i)) l
      (nhds (neutralNF573OriginalGraphMoments ell)) :=
    neutralNF573OriginalGraphMoments.continuous.continuousAt.tendsto.comp hg
  have hd : Tendsto (fun i => neutralNF573OriginalGraphMoments ell -
      neutralNF573OriginalGraphMoments (g i)) l (nhds 0) := by
    simpa only [sub_self] using tendsto_const_nhds.sub hM
  have hR : Tendsto (fun i => R (neutralNF573OriginalGraphMoments ell -
      neutralNF573OriginalGraphMoments (g i))) l (nhds 0) := by
    have hh := (R.continuous.continuousAt (x := 0)).tendsto.comp hd
    simpa only [Function.comp_apply,map_zero] using hh
  have h := hg.add hR
  simpa only [neutralNF543CorrectGraph,add_zero] using h


end
end WeilDefect
