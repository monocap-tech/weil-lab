import WeilDefect.MasterRecon.V06A

/-! V06B: analytic bounded-generator forcing and solution orbit.
The selected ordinate generator is a bounded input; its actual finite
packet construction and real translation covariance are later attachments. -/
namespace WeilDefect.MasterRecon.V06B

open Set
open scoped Topology InnerProduct NNReal

variable {H K : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup K] [InnerProductSpace ℂ K] [CompleteSpace K]

/-- Analytic evaluation of a varying bounded operator on a varying vector. -/
theorem analytic_apply {F G : Type*} [NormedAddCommGroup F] [NormedSpace ℂ F]
    [NormedAddCommGroup G] [NormedSpace ℂ G]
    (B : ℂ → F →L[ℂ] G) (v : ℂ → F) (s : Set ℂ)
    (hB : AnalyticOnNhd ℂ B s) (hv : AnalyticOnNhd ℂ v s) :
    AnalyticOnNhd ℂ (fun z => B z (v z)) s := by
  intro z hz
  let ev : (F →L[ℂ] G) →L[ℂ] F →L[ℂ] G :=
    (ContinuousLinearMap.apply ℂ G : F →L[ℂ] (F →L[ℂ] G) →L[ℂ] G).flip
  exact AnalyticAt.comp₂ (ev.analyticAt_bilinear (B z, v z)) (hB z hz) (hv z hz)

/-- The imaginary ordinate factor uses only the bounded selected generator,
not the unbounded full ordinate generator. The vector v is the selected load. -/
noncomputable def selectedForcing (A : H →L[ℂ] K)
    (D G : K →L[ℂ] K) (v : K) (z : ℂ) : H :=
  A.adjoint (NormedSpace.exp ((-z) • D)
    (NormedSpace.exp ((z * Complex.I) • G) v))

theorem selectedForcing_analytic (A : H →L[ℂ] K)
    (D G : K →L[ℂ] K) (v : K) :
    AnalyticOnNhd ℂ (selectedForcing A D G v) Set.univ := by
  have hd : AnalyticOnNhd ℂ (fun z : ℂ => NormedSpace.exp ((-z) • D)) Set.univ := by
    intro z _
    have hs : AnalyticAt ℂ (fun w : ℂ => (-w) • D) z :=
      analyticAt_id.neg.smul analyticAt_const
    exact AnalyticAt.comp (f := fun w : ℂ => (-w) • D)
      (NormedSpace.exp_analytic (𝕂 := ℂ) ((-z) • D)) hs
  have hg : AnalyticOnNhd ℂ (fun z : ℂ => NormedSpace.exp ((z * Complex.I) • G)) Set.univ := by
    intro z _
    have hm : AnalyticAt ℂ (fun w : ℂ => w * Complex.I) z :=
      analyticAt_id.mul analyticAt_const
    have hs : AnalyticAt ℂ (fun w : ℂ => (w * Complex.I) • G) z :=
      hm.smul analyticAt_const
    exact AnalyticAt.comp (f := fun w : ℂ => (w * Complex.I) • G)
      (NormedSpace.exp_analytic (𝕂 := ℂ) ((z * Complex.I) • G)) hs
  have hgv := analytic_apply _ (fun _ : ℂ => v) Set.univ hg analyticOnNhd_const
  have hdgv := analytic_apply _ _ Set.univ hd hgv
  exact A.adjoint.comp_analyticOnNhd hdgv

theorem selectedForcing_zero (A : H →L[ℂ] K)
    (D G : K →L[ℂ] K) (v : K) :
    selectedForcing A D G v 0 = A.adjoint v := by
  simp [selectedForcing, NormedSpace.exp_zero]

/-- The solution of the analytic equation is analytic and agrees with
every proposed solution of the same equation on the invertible disk.
No physical translation existence or regularity is assumed here. -/
theorem analytic_solution_orbit (P : ℂ → H →L[ℂ] H) (f : ℂ → H)
    (hP : AnalyticOnNhd ℂ P Set.univ) (hf : AnalyticOnNhd ℂ f Set.univ)
    (h0 : IsUnit (P 0)) :
    ∃ r : ℝ, 0 < r ∧ ∃ U : ℂ → H,
      AnalyticOnNhd ℂ U (Metric.ball 0 r) ∧
      (∀ z ∈ Metric.ball 0 r, P z (U z) = f z) ∧
      (∀ z ∈ Metric.ball 0 r, ∀ x : H, P z x = f z → U z = x) := by
  obtain ⟨r, hr, hR, hl, hrr⟩ := V06A.local_analytic_inverse P hP h0
  let U : ℂ → H := fun z => Ring.inverse (P z) (f z)
  have hfa : AnalyticOnNhd ℂ f (Metric.ball 0 r) :=
    fun z _ => hf z (Set.mem_univ z)
  refine ⟨r, hr, U, analytic_apply _ _ _ hR hfa, ?_, ?_⟩
  · intro z hz
    have h := congrArg (fun T : H →L[ℂ] H => T (f z)) (hrr z hz)
    change P z (Ring.inverse (P z) (f z)) = f z at h
    exact h
  · intro z hz x hx
    have h := congrArg (fun T : H →L[ℂ] H => T x) (hl z hz)
    change Ring.inverse (P z) (P z x) = x at h
    rw [hx] at h
    exact h

/-- Coercive translated form and bounded selected forcing assemble into
an analytic orbit, with exact agreement whenever the real equation holds. -/
theorem coercive_selected_orbit (A : H →L[ℂ] K)
    (D E G : K →L[ℂ] K) (v : K) (b : ℝ≥0) (hb : 0 < b)
    (hco : ∀ x : H, ‖x‖ ^ 2 * (b : ℝ) ≤
      (inner ℂ ((A.adjoint ∘L E ∘L A) x) x).re) :
    ∃ r : ℝ, 0 < r ∧ ∃ U : ℂ → H,
      AnalyticOnNhd ℂ U (Metric.ball 0 r) ∧
      (∀ z ∈ Metric.ball 0 r,
        V06A.translatedForm A D E z (U z) = selectedForcing A D G v z) ∧
      (∀ z ∈ Metric.ball 0 r, ∀ x : H,
        V06A.translatedForm A D E z x = selectedForcing A D G v z → U z = x) := by
  apply analytic_solution_orbit _ _ (V06A.translatedForm_analytic A D E)
    (selectedForcing_analytic A D G v)
  rw [V06A.translatedForm_zero]
  apply ContinuousLinearMap.isUnit_of_forall_le_norm_inner_map _ hb
  intro x
  exact (hco x).trans (Complex.re_le_norm _)

end WeilDefect.MasterRecon.V06B

#print axioms WeilDefect.MasterRecon.V06B.analytic_apply
#print axioms WeilDefect.MasterRecon.V06B.selectedForcing_analytic
#print axioms WeilDefect.MasterRecon.V06B.selectedForcing_zero
#print axioms WeilDefect.MasterRecon.V06B.analytic_solution_orbit
#print axioms WeilDefect.MasterRecon.V06B.coercive_selected_orbit
