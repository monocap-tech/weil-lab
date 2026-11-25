import WeilDefect.MasterRecon.V06C
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Function.LpSpace.Basic
import Mathlib.MeasureTheory.Group.Measure

/-! V06D: actual Lebesgue L² tail observations and the support contradiction.
Instead of choosing an essential supremum, propagate an initially empty
right tail leftwards in fixed steps. The continuous embedding of the
physical carrier and its real translation identity remain explicit inputs. -/
namespace WeilDefect.MasterRecon.V06D

open MeasureTheory Set Filter
open scoped ENNReal Topology

noncomputable abbrev PhysicalL2 := Lp ℂ 2 (volume : Measure ℝ)
noncomputable abbrev TailL2 (d : ℝ) := Lp ℂ 2 ((volume : Measure ℝ).restrict (Ioi d))

noncomputable def realTailRestriction (d : ℝ) : PhysicalL2 →L[ℝ] TailL2 d :=
  Lp.LpToLpOfMeasureLeSMul (c := 1) (by simp)
    (by simpa using (Measure.restrict_le_self (μ := (volume : Measure ℝ))
      (s := Ioi d)))

theorem realTailRestriction_ae (d : ℝ) (f : PhysicalL2) :
    realTailRestriction d f =ᵐ[(volume : Measure ℝ).restrict (Ioi d)] f := by
  unfold realTailRestriction
  exact Lp.coeFn_LpToLpOfMeasureLeSMul _ _ f

/-- Upgrade the library's real-linear restriction to a complex-linear
bounded observation, using its actual almost-everywhere representative. -/
noncomputable def tailRestriction (d : ℝ) : PhysicalL2 →L[ℂ] TailL2 d :=
  let R := realTailRestriction d
  ({ toFun := R
     map_add' := R.map_add
     map_smul' := fun c f => by
       apply Lp.ext
       filter_upwards [realTailRestriction_ae d (c • f),
         realTailRestriction_ae d f,
         ae_restrict_of_ae (Lp.coeFn_smul c f),
         Lp.coeFn_smul c (R f)] with x h1 h2 h3 h4
       change R (c • f) x = (c • R f) x
       rw [h1, h3, h4]
       change c * f x = c * R f x
       rw [h2] } : PhysicalL2 →ₗ[ℂ] TailL2 d).mkContinuous ‖R‖ R.le_opNorm

theorem tailRestriction_ae (d : ℝ) (f : PhysicalL2) :
    tailRestriction d f =ᵐ[(volume : Measure ℝ).restrict (Ioi d)] f :=
  realTailRestriction_ae d f

/-- A genuine right tail of a Lebesgue equivalence class, not a pointwise
support predicate imposed on a chosen representative. -/
def TailZero (f : ℝ → ℂ) (d : ℝ) : Prop :=
  ∀ᵐ x ∂(volume : Measure ℝ), d < x → f x = 0

theorem tailRestriction_zero_iff (d : ℝ) (f : PhysicalL2) :
    tailRestriction d f = 0 ↔ TailZero f d := by
  rw [Lp.eq_zero_iff_ae_eq_zero]
  have hiff : (∀ᵐ x ∂(volume : Measure ℝ).restrict (Ioi d), f x = 0) ↔
      TailZero f d :=
    ae_restrict_iff' (μ := (volume : Measure ℝ)) (s := Ioi d)
      (p := fun x : ℝ => f x = 0) measurableSet_Ioi
  constructor
  · intro h
    exact hiff.mp ((tailRestriction_ae d f).symm.trans h)
  · intro h
    exact (tailRestriction_ae d f).trans (hiff.mpr h)

/-- Lebesgue almost-everywhere statements survive translation. -/
theorem ae_translate {p : ℝ → Prop}
    (h : ∀ᵐ x ∂(volume : Measure ℝ), p x) (a : ℝ) :
    ∀ᵐ x ∂(volume : Measure ℝ), p (x + a) :=
  (measurePreserving_add_right (volume : Measure ℝ) a).quasiMeasurePreserving.tendsto_ae.eventually h

variable {H : Type*} [NormedAddCommGroup H] [NormedSpace ℂ H]

/-- An analytic orbit that agrees with the real translations of k in
the physical L² embedding propagates every empty right tail leftward. -/
theorem analytic_tail_step (C : H →L[ℂ] PhysicalL2) (U : ℂ → H)
    (k : PhysicalL2) (r : ℝ) (hr : 0 < r)
    (hU : AnalyticOnNhd ℂ U (Metric.ball 0 r))
    (htrans : ∀ a : ℝ, |a| < r →
      (C (U (a : ℂ)) : PhysicalL2) =ᵐ[volume] fun x => k (x - a))
    (d s : ℝ) (hs : 0 < s) (hsr : s < r)
    (hd : TailZero k d) : TailZero k (d - s) := by
  let J : H →L[ℂ] TailL2 d := (tailRestriction d).comp C
  have hneg : ∀ a : ℝ, -r < a → a < 0 → J (U (a : ℂ)) = 0 := by
    intro a har ha
    change tailRestriction d (C (U (a : ℂ))) = 0
    apply (tailRestriction_zero_iff d _).2
    have habs : |a| < r := by rw [abs_of_neg ha]; linarith
    have hshift := ae_translate hd (-a)
    filter_upwards [hshift, htrans a habs] with x hx htx
    intro hdx
    rw [htx]
    apply hx
    linarith
  have hp := V06C.positive_radius_observation U J r hr hU hneg s hs hsr
  change tailRestriction d (C (U (s : ℂ))) = 0 at hp
  have ht := (tailRestriction_zero_iff d _).1 hp
  have habs : |s| < r := by rwa [abs_of_pos hs]
  have hh : ∀ᵐ x ∂(volume : Measure ℝ), d < x → k (x - s) = 0 := by
    filter_upwards [ht, htrans s habs] with x hx htx
    intro hdx
    rw [← htx]
    exact hx hdx
  have he := ae_translate hh s
  filter_upwards [he] with x hx
  intro hdx
  have h := hx (by linarith : d < x + s)
  simpa using h

/-- No nonzero L² vector with an initially empty right tail can have an
analytic orbit agreeing with real translations on a neighborhood of zero. -/
theorem analytic_translation_right_tail_rigidity
    (C : H →L[ℂ] PhysicalL2) (U : ℂ → H)
    (k : PhysicalL2) (r : ℝ) (hr : 0 < r)
    (hU : AnalyticOnNhd ℂ U (Metric.ball 0 r))
    (htrans : ∀ a : ℝ, |a| < r →
      (C (U (a : ℂ)) : PhysicalL2) =ᵐ[volume] fun x => k (x - a))
    (d : ℝ) (hd : TailZero k d) : k = 0 := by
  let s : ℝ := r / 2
  have hs : 0 < s := by dsimp [s]; linarith
  have hsr : s < r := by dsimp [s]; linarith
  have hn : ∀ n : ℕ, TailZero k (d - (n : ℝ) * s) := by
    intro n
    induction n with
    | zero => simpa using hd
    | succ n ih =>
      have h := analytic_tail_step C U k r hr hU htrans (d - (n : ℝ) * s) s hs hsr ih
      convert h using 1
      push_cast
      ring
  have hall : ∀ᵐ x ∂(volume : Measure ℝ), ∀ n : ℕ, d - (n : ℝ) * s < x → k x = 0 :=
    ae_all_iff.2 hn
  apply Lp.eq_zero_iff_ae_eq_zero.mpr
  filter_upwards [hall] with x hx
  obtain ⟨n, hn'⟩ := exists_nat_gt ((d - x) / s)
  have hmul := (div_lt_iff₀ hs).mp hn'
  exact hx n (by linarith)

end WeilDefect.MasterRecon.V06D

#print axioms WeilDefect.MasterRecon.V06D.realTailRestriction_ae
#print axioms WeilDefect.MasterRecon.V06D.tailRestriction_ae
#print axioms WeilDefect.MasterRecon.V06D.tailRestriction_zero_iff
#print axioms WeilDefect.MasterRecon.V06D.ae_translate
#print axioms WeilDefect.MasterRecon.V06D.analytic_tail_step
#print axioms WeilDefect.MasterRecon.V06D.analytic_translation_right_tail_rigidity
