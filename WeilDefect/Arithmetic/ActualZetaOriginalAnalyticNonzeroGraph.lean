import WeilDefect.Arithmetic.ActualZetaOriginalRemoteNonvanishing
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointNonzero
import WeilDefect.Arithmetic.ActualZetaOriginalJ242AnalyticIdentity

namespace WeilDefect
noncomputable section
open MeasureTheory Set Filter

/-! NF603: analytic continuation turns remote nonvanishing into
nonzero physical collar energy. No endpoint sign, U400 budget, or
transcendental interval evaluator is a hypothesis. -/

theorem neutralNF603Source_analytic (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    AnalyticOnNhd ℝ (neutralNF587Source a b) univ := by
  unfold neutralNF587Source neutralNF569OriginalRealCombination
  apply AnalyticOnNhd.add
  · apply Finset.analyticOnNhd_fun_sum
    intro j _
    exact (neutralNF551OriginalRealGenerator_analytic j).const_smul (c := a j)
  · apply Finset.analyticOnNhd_fun_sum
    intro j _
    have h : AnalyticOnNhd ℝ (neutralNF587CriticalGenerator j) univ := by
      unfold neutralNF587CriticalGenerator
      apply AnalyticOnNhd.add
      · apply Finset.analyticOnNhd_fun_sum
        intro k _
        fun_prop
      · fun_prop
    exact h.const_smul (c := b j)

theorem neutralNF603L2_zero_forces_global_zero
    (U : ℝ → ℝ) (ha : AnalyticOnNhd ℝ U univ) (hU : Continuous U)
    (hLp : MemLp (neutralNF575OriginalEndpoint U) 2 volume)
    (hz : hLp.toLp (neutralNF575OriginalEndpoint U)=0) :
    ∀ x, U x=0 := by
  let E := Ioo ((11/10:ℝ)-1/500) (11/10)
  have hz' : neutralNF575OriginalEndpoint U =ᵐ[volume] (0:ℝ → ℂ) :=
    hLp.coeFn_toLp.symm.trans (Lp.eq_zero_iff_ae_eq_zero.mp hz)
  have hae : U =ᵐ[volume.restrict E] (0:ℝ → ℝ) := by
    have hr := ae_restrict_of_ae (s := E) hz'
    filter_upwards [hr,ae_restrict_mem (μ := volume) (s := E) measurableSet_Ioo] with x hzx hx
    by_contra hne
    exact neutralNF601Endpoint_ne_zero_on_right U x hx hne hzx
  have he : EqOn U (0:ℝ → ℝ) E :=
    Measure.eqOn_open_of_ae_eq hae isOpen_Ioo hU.continuousOn continuous_const.continuousOn
  have hm : (1099/1000:ℝ) ∈ E := by dsimp [E]; constructor <;> norm_num
  have hnear : U =ᶠ[nhds (1099/1000:ℝ)] (fun _ : ℝ => (0:ℝ)) := by
    filter_upwards [isOpen_Ioo.mem_nhds hm] with x hx
    exact he hx
  have hident : U = (fun _ : ℝ => (0:ℝ)) :=
    AnalyticOnNhd.eq_of_eventuallyEq ha (by fun_prop) hnear
  exact fun x => congrFun hident x

theorem neutralNF603OriginalCarrier_nonzero_of_box
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b)
    (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume) :
    hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ≠ 0 := by
  intro hz
  have h := neutralNF603L2_zero_forces_global_zero (neutralNF587Source a b)
    (neutralNF603Source_analytic a b) (neutralNF587Source_contDiff a b).continuous hLp hz
  exact (ne_of_lt (neutralNF603Source_remote_negative a b hbox)) (h 1000)

/-- Strict original support-localized graph positivity now has
only the ORIGINAL solve box and actual local coercivity premises.
Neither of the numerical checkers is required for this theorem. -/
theorem neutralNF603NF407Graph_positive_of_box (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b)
    (c : ℝ) (hc : 0<c) (hlocal : neutralNF599SmoothCollarLower c) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ∧
      0 < neutralNF598GraphWeil (11/10) K := by
  obtain ⟨hLp,K,hK,hlo⟩ := neutralNF599NF407GraphLower a b c hlocal
  have hn : neutralNF598GraphPhysical (11/10) K ≠ 0 := by
    rw [hK]
    exact neutralNF603OriginalCarrier_nonzero_of_box a b hbox hLp
  exact ⟨hLp,K,hK,neutralNF599Graph_positive_of_lower K c hc hn hlo⟩

end
end WeilDefect
