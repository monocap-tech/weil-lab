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
    have hc : Tendsto (fun _ : ι => neutralNF573OriginalGraphMoments ell) l
        (nhds (neutralNF573OriginalGraphMoments ell)) := tendsto_const_nhds
    simpa only [sub_self] using hc.sub hM
  have hR : Tendsto (fun i => R (neutralNF573OriginalGraphMoments ell -
      neutralNF573OriginalGraphMoments (g i))) l (nhds 0) := by
    have hh := (R.continuous.continuousAt (x := 0)).tendsto.comp hd
    change Tendsto (fun i => R (neutralNF573OriginalGraphMoments ell - neutralNF573OriginalGraphMoments (g i))) l (nhds (R 0)) at hh
    rw [map_zero] at hh
    exact hh
  let S := (neutralActualZetaSourceGraph (11/10:ℝ)).toSubmodule
  let P := S.subtypeL
  have hg' := P.continuous.continuousAt.tendsto.comp hg
  have hR' := P.continuous.continuousAt.tendsto.comp hR
  have ha := hg'.add hR'
  rw [map_zero,add_zero] at ha
  apply tendsto_subtype_rng.mpr
  change Tendsto (fun i => P (neutralNF543CorrectGraph
    neutralNF573OriginalGraphMoments R ell (g i))) l (nhds (P ell))
  simpa only [neutralNF543CorrectGraph,map_add,Function.comp_apply] using ha


end
end WeilDefect
