import WeilDefect.Arithmetic.ActualZetaOriginalSignedGraphForm

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap

/-! NF598: graph convergence transports the literal smooth EF real
diagonal, not merely an abstract energy proxy. A strict sign or
relative margin at the authentic graph limit is sufficient for
eventual smooth witnesses. The sign of that limit remains a premise. -/

def neutralNF598SmoothWeil (s : 𝓢(ℝ,ℂ)) : ℝ :=
  (Zeta23.EF.literatureRHS (neutralWindowCorrelation (11/10:ℝ)
    (s.toLp 2 volume) (s.toLp 2 volume))).re

theorem neutralNF598SmoothWeil_tendsto
    (K : NeutralActualZetaSourceDomain (11/10:ℝ))
    (F : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ))
    (s : ℕ → 𝓢(ℝ,ℂ))
    (hp : ∀ n, neutralNF598GraphPhysical (11/10) (F n) = (s n).toLp 2 volume)
    (hs : ∀ n x, x ∉ neutralNF543OriginalCollars → s n x = 0)
    (hlim : Tendsto F atTop (nhds K)) :
    Tendsto (fun n => neutralNF598SmoothWeil (s n)) atTop
      (nhds (neutralNF598GraphWeil (11/10) K)) := by
  have he (n : ℕ) : neutralNF598GraphWeil (11/10) (F n) =
      neutralNF598SmoothWeil (s n) :=
    neutralNF598GraphWeil_eq_smooth (F n) (s n) (hs n) (hp n)
  have h := (neutralNF598GraphWeil_continuous (11/10)).continuousAt.tendsto.comp hlim
  have hf : (neutralNF598GraphWeil (11/10) ∘ F) =
      (fun n => neutralNF598SmoothWeil (s n)) := funext he
  rw [hf] at h
  exact h

theorem neutralNF598GraphMargin_continuous (a c : ℝ) :
    Continuous (fun u : NeutralActualZetaSourceDomain a =>
      neutralNF598GraphWeil a u - c*‖neutralNF598GraphPhysical a u‖^2) := by
  exact (neutralNF598GraphWeil_continuous a).sub
    (continuous_const.mul ((neutralNF598GraphPhysical_continuous a).norm.pow 2))

/-- Full graph convergence also preserves a strict relative margin,
with precisely the actual physical L² norm in the denominator. -/
theorem neutralNF598SmoothMargin_tendsto
    (K : NeutralActualZetaSourceDomain (11/10:ℝ))
    (F : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ))
    (s : ℕ → 𝓢(ℝ,ℂ)) (c : ℝ)
    (hp : ∀ n, neutralNF598GraphPhysical (11/10) (F n) = (s n).toLp 2 volume)
    (hs : ∀ n x, x ∉ neutralNF543OriginalCollars → s n x = 0)
    (hlim : Tendsto F atTop (nhds K)) :
    Tendsto (fun n => neutralNF598SmoothWeil (s n) -
      c*‖(s n).toLp 2 volume‖^2) atTop
      (nhds (neutralNF598GraphWeil (11/10) K -
        c*‖neutralNF598GraphPhysical (11/10) K‖^2)) := by
  have he (n : ℕ) : neutralNF598GraphWeil (11/10) (F n) =
      neutralNF598SmoothWeil (s n) :=
    neutralNF598GraphWeil_eq_smooth (F n) (s n) (hs n) (hp n)
  have h := (neutralNF598GraphMargin_continuous (11/10) c).continuousAt.tendsto.comp hlim
  have hf :
      ((fun u : NeutralActualZetaSourceDomain (11/10:ℝ) =>
        neutralNF598GraphWeil (11/10) u - c*‖neutralNF598GraphPhysical (11/10) u‖^2) ∘ F) =
      (fun n => neutralNF598SmoothWeil (s n) - c*‖(s n).toLp 2 volume‖^2) := by
    funext n
    change neutralNF598GraphWeil (11/10) (F n) -
      c*‖neutralNF598GraphPhysical (11/10) (F n)‖^2 = _
    rw [he n,hp n]
  rw [hf] at h
  exact h

theorem neutralNF598SmoothMargin_eventually
    (K : NeutralActualZetaSourceDomain (11/10:ℝ))
    (F : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ))
    (s : ℕ → 𝓢(ℝ,ℂ)) (c : ℝ)
    (hp : ∀ n, neutralNF598GraphPhysical (11/10) (F n) = (s n).toLp 2 volume)
    (hs : ∀ n x, x ∉ neutralNF543OriginalCollars → s n x = 0)
    (hlim : Tendsto F atTop (nhds K))
    (hmargin : c*‖neutralNF598GraphPhysical (11/10) K‖^2 <
      neutralNF598GraphWeil (11/10) K) :
    ∀ᶠ n in atTop, c*‖(s n).toLp 2 volume‖^2 < neutralNF598SmoothWeil (s n) := by
  have h := neutralNF598SmoothMargin_tendsto K F s c hp hs hlim
  have hpos : 0 < neutralNF598GraphWeil (11/10) K -
      c*‖neutralNF598GraphPhysical (11/10) K‖^2 := sub_pos.mpr hmargin
  have he := h.eventually (Ioi_mem_nhds hpos)
  filter_upwards [he] with n hn
  exact sub_pos.mp hn

theorem neutralNF598SmoothNegative_eventually
    (K : NeutralActualZetaSourceDomain (11/10:ℝ))
    (F : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ))
    (s : ℕ → 𝓢(ℝ,ℂ))
    (hp : ∀ n, neutralNF598GraphPhysical (11/10) (F n) = (s n).toLp 2 volume)
    (hs : ∀ n x, x ∉ neutralNF543OriginalCollars → s n x = 0)
    (hlim : Tendsto F atTop (nhds K))
    (hneg : neutralNF598GraphWeil (11/10) K < 0) :
    ∀ᶠ n in atTop, neutralNF598SmoothWeil (s n) < 0 :=
  (neutralNF598SmoothWeil_tendsto K F s hp hs hlim).eventually (Iio_mem_nhds hneg)

end
end WeilDefect
