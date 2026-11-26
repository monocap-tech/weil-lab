import WeilDefect.Arithmetic.ActualZetaIV133OriginalProjectedRow
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap FourierTransform ComplexConjugate BigOperators

/-- The original arithmetic source has literal radius compatibility
on an unchanged supported Schwartz pair. The inverse correlation
formula removes the radius parameter, not the arithmetic terms. -/
theorem neutralIV138Mixed_radius (a b : ℝ) (ha : 0 ≤ a) (hab : a ≤ b)
    (u v : 𝓢(ℝ,ℂ))
    (hu : ∀ x : ℝ, x ∉ Set.Icc (-a) a → u x = 0)
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    neutralIV101Mixed a u v = neutralIV101Mixed b u v := by
  have hub : ∀ x : ℝ, x ∉ Set.Icc (-b) b → u x = 0 := by
    intro x hx
    apply hu x
    intro h
    apply hx
    exact ⟨by linarith [h.1],by linarith [h.2]⟩
  have hvb : ∀ x : ℝ, x ∉ Set.Icc (-b) b → v x = 0 := by
    intro x hx
    apply hv x
    intro h
    apply hx
    exact ⟨by linarith [h.1],by linarith [h.2]⟩
  have hc : neutralIV103Correlation a u v = neutralIV103Correlation b u v := by
    funext t
    rw [neutralIV103Correlation_inverse a ha u v hu hv t,
      neutralIV103Correlation_inverse b (ha.trans hab) u v hub hvb t]
  unfold neutralIV101Mixed
  change Zeta23.EF.literatureRHS (neutralIV103Correlation a u v) =
    Zeta23.EF.literatureRHS (neutralIV103Correlation b u v)
  rw [hc]

theorem neutralIV138Q_radius (a b : ℝ) (ha : 0 ≤ a) (hab : a ≤ b)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-a) a → v x = 0) :
    neutralIV101Q a v = neutralIV101Q b v := by
  unfold neutralIV101Q
  rw [neutralIV138Mixed_radius a b ha hab v v hv hv]

/-- A positive larger-window receiver suffices on the unchanged
radius-11/10 core. No rescaling of primes, Gamma or poles. -/
theorem neutralIV138Window_from_two
    (hpos : ∀ v : 𝓢(ℝ,ℂ),
      (∀ x : ℝ, x ∉ Set.Icc (-(2:ℝ)) 2 → v x = 0) →
      0 ≤ neutralIV101Q 2 v)
    (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    0 ≤ neutralIV101Q (11/10:ℝ) v := by
  rw [neutralIV138Q_radius _ 2 (by norm_num) (by norm_num) v hv]
  apply hpos v
  intro x hx
  apply hv x
  intro h
  apply hx
  exact ⟨by linarith [h.1],by linarith [h.2]⟩

/-- Exact signed cross-nullness eliminates the packed response energy.
There is no need to charge its global norm on this smaller tail. -/
theorem neutralIV138Schur_crossNull (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ))
    (hb : neutralIV106CrossRHS k hk v = 0) :
    neutralIV107SchurEnergy k hk v = neutralIV101Q (11/10:ℝ) v := by
  unfold neutralIV107SchurEnergy
  rw [neutralIV108Response_energy, hb]
  simp

/-- The packed cross rows are actual physical constraint representers.
Adding their k equations is different from mass orthogonality. -/
theorem neutralIV138CrossRows_iff (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0) :
    neutralIV106CrossRHS k hk v = 0 ↔
      ∀ i : Fin k, inner ℂ
        (neutralIV133PhysicalRow (11/10:ℝ) (neutralIV100Carrier k hk i))
        (v.toLp 2 volume) = 0 := by
  constructor
  · intro h i
    rw [neutralIV133PhysicalRow_pair _ (by norm_num) _ _
      (neutralIV009OriginalCollars_supported_window _ (neutralIV100Carrier_collars k hk i)) hv]
    exact congrFun h i
  · intro h
    funext i
    have hi := h i
    rw [neutralIV133PhysicalRow_pair _ (by norm_num) _ _
      (neutralIV009OriginalCollars_supported_window _ (neutralIV100Carrier_collars k hk i)) hv] at hi
    exact hi

/-- The original certified cell leakage receiver without the global
packed response budget, on the signed cross-null tail. -/
theorem neutralIV138CrossNull_tail (k : ℕ) (hk : 0 < k) (N : ℕ)
    (hN : 0 < N) (v : 𝓢(ℝ,ℂ))
    (hv : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v x = 0)
    (hb : neutralIV106CrossRHS k hk v = 0)
    (hz : neutralIV127CellNull (11/10:ℝ) N v)
    (T eta : ℝ) (hT : 0 ≤ T)
    (hm : eta ≤ (1-neutralIV127Leakage (11/10:ℝ) N T)*
      Real.log (Real.exp 1+T) -
      (neutralActualZetaNativeLogError (11/10:ℝ) +
        neutralPhysicalPoleEnergyConstant (11/10:ℝ))) :
    eta*‖v.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk v := by
  rw [neutralIV138Schur_crossNull k hk v hb]
  have hg := neutralIV109Original_garding _ (by norm_num) v hv
  have hl := neutralIV125LogLower_of_leakage _ v hv T _ hT
    (neutralIV127LowBand _ (by norm_num) N hN v hv hz T hT)
  have hp := mul_le_mul_of_nonneg_right hm (sq_nonneg ‖v.toLp 2 volume‖)
  linarith only [hg,hl,hp]

#print axioms neutralIV138Mixed_radius
#print axioms neutralIV138Q_radius
#print axioms neutralIV138Window_from_two
#print axioms neutralIV138Schur_crossNull
#print axioms neutralIV138CrossRows_iff
#print axioms neutralIV138CrossNull_tail

end
end WeilDefect
