import WeilDefect.Arithmetic.ActualZetaOriginalSupportCoercivityTransfer
import Mathlib.MeasureTheory.Measure.OpenPos

namespace WeilDefect
noncomputable section
open MeasureTheory Set

/-! NF601: strict positivity needs a nonzero physical vector, not
a quantitative lower bound for its norm. The endpoint point itself
is excluded from the support; use continuity of U and positivity
of the logarithmic multiplier in the open right collar. -/

theorem neutralNF601Endpoint_ne_zero_on_right (U : ℝ → ℝ) (x : ℝ)
    (hx : x ∈ Ioo ((11/10:ℝ)-1/500) (11/10))
    (hU : U x ≠ 0) :
    neutralNF575OriginalEndpoint U x ≠ 0 := by
  have hn : -x ∉ Ioo ((11/10:ℝ)-1/500) (11/10) := by
    intro h
    linarith [hx.1,h.1]
  have hlog : 0 < Real.log ((11/10:ℝ)/((11/10:ℝ)-x)) := by
    apply Real.log_pos
    apply (lt_div_iff₀ (sub_pos.mpr hx.2)).mpr
    linarith [hx.1]
  simp only [neutralNF575OriginalEndpoint,neutralNF575OriginalEndpointHalf,if_pos hx,
    if_neg hn,sub_zero,Complex.ofReal_ne_zero]
  exact mul_ne_zero (div_ne_zero hU (by norm_num)) hlog.ne'

theorem neutralNF601Endpoint_L2_ne_zero (U : ℝ → ℝ)
    (hU : Continuous U) (hB : U (11/10) ≠ 0)
    (hLp : MemLp (neutralNF575OriginalEndpoint U) 2 volume) :
    hLp.toLp (neutralNF575OriginalEndpoint U) ≠ 0 := by
  intro hzero
  have hz : neutralNF575OriginalEndpoint U =ᵐ[volume] (0:ℝ → ℂ) :=
    hLp.coeFn_toLp.symm.trans (Lp.eq_zero_iff_ae_eq_zero.mp hzero)
  let E := Ioo ((11/10:ℝ)-1/500) (11/10)
  have hae : U =ᵐ[volume.restrict E] (0:ℝ → ℝ) := by
    have hr := ae_restrict_of_ae (s := E) hz
    filter_upwards [hr,ae_restrict_mem (μ := volume) (s := E) measurableSet_Ioo] with x hzx hx
    by_contra hne
    exact neutralNF601Endpoint_ne_zero_on_right U x hx hne hzx
  have he : EqOn U (0:ℝ → ℝ) E :=
    eqOn_open_of_ae_eq hae isOpen_Ioo hU.continuousOn continuous_const.continuousOn
  have hc := he.closure hU continuous_const
  have hb : (11/10:ℝ) ∈ closure E := by
    dsimp [E]
    rw [closure_Ioo (by norm_num : (11/10:ℝ)-1/500 ≠ 11/10)]
    exact ⟨by norm_num,le_rfl⟩
  exact hB (hc hb)

/-- This wrapper is independent of the unfinished gamma proof and
of the numerical checker. It consumes only local support coercivity
and a nonzero endpoint value for the same source. -/
theorem neutralNF601NF407Graph_positive
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (c : ℝ) (hc : 0<c)
    (hlocal : neutralNF599SmoothCollarLower c)
    (hB : neutralNF587Source a b (11/10) ≠ 0) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ∧
      0 < neutralNF598GraphWeil (11/10) K := by
  obtain ⟨hLp,K,hK,hlo⟩ := neutralNF599NF407GraphLower a b c hlocal
  have hn : neutralNF598GraphPhysical (11/10) K ≠ 0 := by
    rw [hK]
    exact neutralNF601Endpoint_L2_ne_zero (neutralNF587Source a b)
      (neutralNF587Source_contDiff a b).continuous hB hLp
  exact ⟨hLp,K,hK,neutralNF599Graph_positive_of_lower K c hc hn hlo⟩

end
end WeilDefect
