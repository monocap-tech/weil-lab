import WeilDefect.Arithmetic.ActualZetaIV105E2OriginalSolveAttachment
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- Scalar residual-energy reserve using the certified packed coercivity.
No inverse matrix or approximate spectral lower bound is assumed. -/
theorem neutralIV105FResidual_budget (q m η : ℝ)
    (hcoerc : (2/5:ℝ)*m^2 ≤ q)
    (hres : q ≤ η*m) :
    q ≤ (5/2:ℝ)*η^2 := by
  nlinarith only [hcoerc, hres, sq_nonneg ((2/5:ℝ)*m-η)]

/-- Exact correction energy for a trial coefficient vector. -/
theorem neutralIV105FTrial_identity (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ)) (t : Fin k → ℂ)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (neutralIV105E2Solve k hk v)) =
      2*(neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk t) v).re -
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk t) +
      neutralIV101Q (11/10:ℝ)
        (neutralIV100Packed k hk (neutralIV105E2Solve k hk v-t)) := by
  let d := neutralIV105E2Solve k hk v
  let e := d-t
  let p := neutralIV100Packed k hk t
  let w := neutralIV100Packed k hk e
  have ht := neutralIV009OriginalCollars_supported_window p
    (neutralIV101Packed_collars k hk t)
  have he := neutralIV009OriginalCollars_supported_window w
    (neutralIV101Packed_collars k hk e)
  have hd : p+w = neutralIV100Packed k hk d := by
    change neutralIV100Packed k hk t + neutralIV100Packed k hk e = _
    rw [← neutralIV105DPacked_add]
    congr 1
    dsimp [e]
    abel
  have hp := neutralIV101Q_add (11/10:ℝ) p w ht he
  have hsolve := congrArg Complex.re (neutralIV105E2Solve_all k hk v t hv)
  change (neutralIV101Mixed (11/10:ℝ) p v).re =
    (neutralIV101Mixed (11/10:ℝ) p (neutralIV100Packed k hk d)).re at hsolve
  rw [← hd] at hsolve
  have hlin : neutralIV101Mixed (11/10:ℝ) p (p+w) =
      neutralIV101Mixed (11/10:ℝ) p p + neutralIV101Mixed (11/10:ℝ) p w := by
    have hs : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → (p+w) x = 0 := by
      intro x hx
      change p x+w x=0
      rw [ht x hx, he x hx, add_zero]
    rw [neutralIV105BAction_pair _ (by norm_num) _ _ ht hs,
      neutralIV105BAction_pair _ (by norm_num) _ _ ht ht,
      neutralIV105BAction_pair _ (by norm_num) _ _ ht he]
    change inner ℂ (neutralIV105BAction (11/10:ℝ) p)
      ((SchwartzMap.toLpCLM ℂ ℂ 2 volume) (p+w)) = _
    rw [map_add, inner_add_right]
    rfl
  rw [hlin, Complex.add_re] at hsolve
  rw [hd] at hp
  change neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk d) =
      2*(neutralIV101Mixed (11/10:ℝ) p v).re -
      neutralIV101Q (11/10:ℝ) p + neutralIV101Q (11/10:ℝ) w
  change _ = (neutralIV101Mixed (11/10:ℝ) p p).re +
    (neutralIV101Mixed (11/10:ℝ) p w).re at hsolve
  change _ = (neutralIV101Mixed (11/10:ℝ) p p).re +
    2*(neutralIV101Mixed (11/10:ℝ) p w).re +
    neutralIV101Q (11/10:ℝ) w at hp
  unfold neutralIV101Q at *
  linarith

/-- Receiver for the trial solve: an explicit residual dual-mass bound
on the error vector is sufficient, with no numerical inverse. -/
theorem neutralIV105FTrial_upper (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ)) (t : Fin k → ℂ) (η : ℝ)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (hres : neutralIV101Q (11/10:ℝ)
      (neutralIV100Packed k hk (neutralIV105E2Solve k hk v-t)) ≤
        η * ‖(neutralIV100Packed k hk (neutralIV105E2Solve k hk v-t)).toLp 2 volume‖) :
    neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (neutralIV105E2Solve k hk v)) ≤
      2*(neutralIV101Mixed (11/10:ℝ) (neutralIV100Packed k hk t) v).re -
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk t) + (5/2:ℝ)*η^2 := by
  have hm := neutralIV101Packed_full_margin k hk (neutralIV105E2Solve k hk v-t)
  have hb := neutralIV105FResidual_budget _ _ η hm hres
  rw [neutralIV105FTrial_identity k hk v t hv]
  linarith

#print axioms neutralIV105FResidual_budget
#print axioms neutralIV105FTrial_identity
#print axioms neutralIV105FTrial_upper
end
end WeilDefect
