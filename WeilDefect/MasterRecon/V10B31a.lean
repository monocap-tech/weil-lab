import WeilDefect.MasterRecon.V10B30a
import WeilDefect.MasterRecon.V10B20c
import WeilDefect.MasterRecon.V10B21a

/-! Three moment families for the literal polynomial/log Gram.
Use reflected finite sums, avoiding a second beta differentiation proof. -/
namespace WeilDefect.MasterRecon.V10B31a

open MeasureTheory Set Filter
open scoped BigOperators
open V10B30a (ell moment)
open V10B20b (H H₂)

noncomputable def rightMoment (k m : ℕ) : ℝ :=
  ∑ j ∈ Finset.range (k+1),
    ((-1:ℝ)^j*(k.choose j:ℝ))*((m.factorial:ℝ)/((j:ℝ)+1)^(m+1))

theorem left_integrable (k : ℕ) :
    IntegrableOn (fun z : ℝ => z^k*Real.log z) (Ioo 0 1) := by
  simpa only [pow_one,mul_neg,integrable_neg_iff] using V10B20b.log_moment_integrable k 1

theorem right_integrable (k : ℕ) :
    IntegrableOn (fun z : ℝ => z^k*Real.log (1-z)) (Ioo 0 1) := by
  simpa only [pow_one,mul_neg,integrable_neg_iff] using V10B21a.reflected_moment_integrable k 1

theorem mixed_integrable (k : ℕ) :
    IntegrableOn (fun z : ℝ => z^k*Real.log z*Real.log (1-z)) (Ioo 0 1) := by
  have ha : IntegrableOn (fun z : ℝ => z^k*Real.log z^2) (Ioo 0 1) := by
    simpa only [neg_sq] using V10B20b.log_moment_integrable k 2
  have hb : IntegrableOn (fun z : ℝ => z^k*Real.log (1-z)^2) (Ioo 0 1) := by
    simpa only [neg_sq] using V10B21a.reflected_moment_integrable k 2
  apply (ha.add hb).mono' (by fun_prop : Measurable (fun z : ℝ =>
    z^k*Real.log z*Real.log (1-z))).aestronglyMeasurable
  rw [ae_restrict_iff' measurableSet_Ioo]
  refine Eventually.of_forall fun z hz => ?_
  have h₁ := Real.log_nonpos hz.1.le hz.2.le
  have h₂ : Real.log (1-z) ≤ 0 := Real.log_nonpos (by linarith [hz.2]) (by linarith [hz.1])
  have hp : 0 ≤ z^k := pow_nonneg hz.1.le _
  rw [Real.norm_eq_abs,abs_of_nonneg (by
    exact mul_nonneg_of_nonpos_of_nonpos (mul_nonpos_of_nonneg_of_nonpos hp h₁) h₂)]
  have h := mul_le_mul_of_nonneg_left
    (show Real.log z*Real.log (1-z) ≤ Real.log z^2+Real.log (1-z)^2 by
      nlinarith [sq_nonneg (Real.log z-Real.log (1-z))]) hp
  nlinarith only [h]

theorem moment_integrable (s k : ℕ) (hs : s ≤ 2) :
    IntegrableOn (fun z : ℝ => z^k*(ell z)^s) (Ioo 0 1) := by
  have hcases : s=0 ∨ s=1 ∨ s=2 := by omega
  rcases hcases with rfl|rfl|rfl
  · simpa only [pow_zero,mul_one] using V10B20b.log_moment_integrable k 0
  · simp only [ell,pow_one,mul_add]
    exact (left_integrable k).add (right_integrable k)
  · have ha : IntegrableOn (fun z : ℝ => z^k*Real.log z^2) (Ioo 0 1) := by
      simpa only [neg_sq] using V10B20b.log_moment_integrable k 2
    have hb : IntegrableOn (fun z : ℝ => z^k*Real.log (1-z)^2) (Ioo 0 1) := by
      simpa only [neg_sq] using V10B21a.reflected_moment_integrable k 2
    have he : (fun z : ℝ => z^k*(ell z)^2) =
        fun z => z^k*Real.log z^2+2*(z^k*Real.log z*Real.log (1-z))+z^k*Real.log (1-z)^2 := by
      funext z
      unfold ell
      ring
    rw [he]
    exact (ha.add ((mixed_integrable k).const_mul 2)).add hb

theorem moment_zero (k : ℕ) : moment 0 k = 1/((k:ℝ)+1) := by
  simpa [moment] using V10B20b.log_moment k 0

theorem right_one (k : ℕ) :
    (∫ z in Ioo (0:ℝ) 1, z^k*Real.log (1-z)) = -rightMoment k 1 := by
  have h := V10B21a.reflected_moment k 1
  simp only [rightMoment,pow_one,mul_neg,integral_neg] at h ⊢
  linarith

theorem moment_one (k : ℕ) :
    moment 1 k = -1/((k:ℝ)+1)^2-rightMoment k 1 := by
  unfold moment ell
  simp only [pow_one,mul_add]
  rw [integral_add (left_integrable k) (right_integrable k),V10B20b.log_left,right_one]
  ring

theorem moment_two (k : ℕ) :
    moment 2 k = 2/((k:ℝ)+1)^3+rightMoment k 2+
      2*(H (k+1)/((k:ℝ)+1)^2-(Real.pi^2/6-H₂ (k+1))/((k:ℝ)+1)) := by
  have ha : IntegrableOn (fun z : ℝ => z^k*Real.log z^2) (Ioo 0 1) := by
    simpa only [neg_sq] using V10B20b.log_moment_integrable k 2
  have hb : IntegrableOn (fun z : ℝ => z^k*Real.log (1-z)^2) (Ioo 0 1) := by
    simpa only [neg_sq] using V10B21a.reflected_moment_integrable k 2
  have he : (fun z : ℝ => z^k*(ell z)^2) =
      fun z => z^k*Real.log z^2+2*(z^k*Real.log z*Real.log (1-z))+z^k*Real.log (1-z)^2 := by
    funext z
    unfold ell
    ring
  unfold moment
  rw [he,integral_add (ha.add ((mixed_integrable k).const_mul 2)) hb,
    integral_add ha ((mixed_integrable k).const_mul 2),integral_const_mul,
    V10B20b.log_left_sq,V10B20c.mixed_log_exact]
  have h := V10B21a.reflected_moment k 2
  simp only [neg_sq] at h
  rw [h]
  unfold rightMoment
  ring

end WeilDefect.MasterRecon.V10B31a

#print axioms WeilDefect.MasterRecon.V10B31a.left_integrable
#print axioms WeilDefect.MasterRecon.V10B31a.right_integrable
#print axioms WeilDefect.MasterRecon.V10B31a.mixed_integrable
#print axioms WeilDefect.MasterRecon.V10B31a.moment_integrable
#print axioms WeilDefect.MasterRecon.V10B31a.moment_zero
#print axioms WeilDefect.MasterRecon.V10B31a.right_one
#print axioms WeilDefect.MasterRecon.V10B31a.moment_one
#print axioms WeilDefect.MasterRecon.V10B31a.moment_two
