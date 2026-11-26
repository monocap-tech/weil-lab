import WeilDefect.Arithmetic.ActualZetaIV125OriginalFourierLeakage
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap FourierTransform BigOperators

def neutralIV126Phase (t : ℝ) : ℂ := Complex.exp (Complex.I * (t : ℂ))

theorem neutralIV126Phase_norm (t : ℝ) : ‖neutralIV126Phase t‖ = 1 := by
  simp [neutralIV126Phase, Complex.norm_exp, Complex.mul_re]

theorem neutralIV126Phase_sub (t s : ℝ) :
    ‖neutralIV126Phase t - neutralIV126Phase s‖ ≤ |t-s| := by
  have he : neutralIV126Phase t - neutralIV126Phase s =
      neutralIV126Phase s * (neutralIV126Phase (t-s) - 1) := by
    unfold neutralIV126Phase
    rw [mul_sub, mul_one, ← Complex.exp_add]
    congr 2
    push_cast
    ring
  rw [he, norm_mul, neutralIV126Phase_norm, one_mul]
  simpa only [neutralIV126Phase, Real.norm_eq_abs] using
    (Real.norm_exp_I_mul_ofReal_sub_one_le (x := t-s))

def neutralIV126Node (l d : ℝ) (j : ℕ) : ℝ := l + (j : ℝ)*d

theorem neutralIV126Node_step (l d : ℝ) (j : ℕ) :
    neutralIV126Node l d (j+1) = neutralIV126Node l d j+d := by
  simp only [neutralIV126Node, Nat.cast_add, Nat.cast_one]
  ring

theorem neutralIV126Equal_end (a : ℝ) (N : ℕ) (hN : 0 < N) :
    neutralIV126Node (-a) (2*a/(N:ℝ)) N = a := by
  have h : (N:ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hN)
  unfold neutralIV126Node
  field_simp
  <;> ring

/-- Exact payment for one actual physical interval, with no phase premise. -/
theorem neutralIV126Cell_payment (f : ℝ → ℂ) (hf : Continuous f)
    (l d q : ℝ) (hd : 0 ≤ d)
    (hm : (∫ x in Set.Ioc l (l+d), f x) = 0) :
    ‖∫ x in l..(l+d), neutralIV126Phase (q*x)*f x‖ ≤
      (|q|*d) * ∫ x in l..(l+d), ‖f x‖ := by
  have hl : l ≤ l+d := by linarith
  have hp : Continuous (fun x : ℝ => neutralIV126Phase (q*x)*f x) := by
    unfold neutralIV126Phase
    fun_prop
  have hi : Integrable f (volume.restrict (Set.Ioc l (l+d))) :=
    (hf.intervalIntegrable l (l+d)).1
  have hj : Integrable (fun x => neutralIV126Phase (q*x)*f x)
      (volume.restrict (Set.Ioc l (l+d))) :=
    (hp.intervalIntegrable l (l+d)).1
  have hb : ∀ᵐ x ∂volume.restrict (Set.Ioc l (l+d)),
      ‖neutralIV126Phase (q*x)-neutralIV126Phase (q*l)‖ ≤ |q|*d := by
    filter_upwards [ae_restrict_mem measurableSet_Ioc] with x hx
    have hxl : 0 ≤ x-l := by linarith [hx.1]
    have hxd : x-l ≤ d := by linarith [hx.2]
    calc
      _ ≤ |q*x-q*l| := neutralIV126Phase_sub _ _
      _ = |q|*|x-l| := by rw [← mul_sub, abs_mul]
      _ ≤ |q|*d := by
        rw [abs_of_nonneg hxl]
        exact mul_le_mul_of_nonneg_left hxd (abs_nonneg _)
  simp only [intervalIntegral.integral_of_le hl]
  exact neutralIV125Cell_bound f (fun x => neutralIV126Phase (q*x))
    _ (neutralIV126Phase (q*l)) (|q|*d) hi hj hm hb

/-- Adjacent equal physical cells recombine exactly; no disjointness
or finite-sum integral identity is left as a premise. -/
theorem neutralIV126Partition_payment (f : ℝ → ℂ) (hf : Continuous f)
    (l d q : ℝ) (N : ℕ) (hd : 0 ≤ d)
    (hm : ∀ j < N, (∫ x in Set.Ioc (neutralIV126Node l d j)
      (neutralIV126Node l d (j+1)), f x) = 0) :
    ‖∫ x in l..(neutralIV126Node l d N), neutralIV126Phase (q*x)*f x‖ ≤
      (|q|*d) * ∫ x in l..(neutralIV126Node l d N), ‖f x‖ := by
  let b := neutralIV126Node l d
  have hb0 : b 0 = l := by simp [b, neutralIV126Node]
  have hp : Continuous (fun x : ℝ => neutralIV126Phase (q*x)*f x) := by
    unfold neutralIV126Phase
    fun_prop
  have hs : (∑ j ∈ Finset.range N, ∫ x in b j..b (j+1),
      neutralIV126Phase (q*x)*f x) =
      ∫ x in l..b N, neutralIV126Phase (q*x)*f x := by
    rw [intervalIntegral.sum_integral_adjacent_intervals
      (fun j _ => hp.intervalIntegrable (b j) (b (j+1))), hb0]
  have hn : (∑ j ∈ Finset.range N, ∫ x in b j..b (j+1), ‖f x‖) =
      ∫ x in l..b N, ‖f x‖ := by
    rw [intervalIntegral.sum_integral_adjacent_intervals
      (fun j _ => hf.norm.intervalIntegrable (b j) (b (j+1))), hb0]
  change ‖∫ x in l..b N, neutralIV126Phase (q*x)*f x‖ ≤ _
  rw [← hs, ← hn, Finset.mul_sum]
  refine (norm_sum_le _ _).trans (Finset.sum_le_sum ?_)
  intro j hj
  have hstep : b (j+1) = b j+d := neutralIV126Node_step l d j
  rw [hstep]
  have hmean := hm j (Finset.mem_range.mp hj)
  change (∫ x in Set.Ioc (b j) (b (j+1)), f x) = 0 at hmean
  rw [hstep] at hmean
  exact neutralIV126Cell_payment f hf (b j) d q hd hmean

/-- Actual equal-cell estimate on the complete original physical window. -/
theorem neutralIV126Window_payment (v : 𝓢(ℝ,ℂ)) (a q : ℝ)
    (N : ℕ) (ha : 0 ≤ a) (hN : 0 < N)
    (hm : ∀ j < N, (∫ x in Set.Ioc
      (neutralIV126Node (-a) (2*a/(N:ℝ)) j)
      (neutralIV126Node (-a) (2*a/(N:ℝ)) (j+1)), v x) = 0) :
    ‖∫ x in (-a)..a, neutralIV126Phase (q*x)*v x‖ ≤
      (|q|*(2*a/(N:ℝ))) * ∫ x in (-a)..a, ‖v x‖ := by
  have h := neutralIV126Partition_payment (fun x => v x) v.continuous
    (-a) (2*a/(N:ℝ)) q N (by positivity) hm
  rw [neutralIV126Equal_end a N hN] at h
  exact h

/-- Schwartz to physical L2 Fourier transport is genuinely a.e.,
not pointwise for an arbitrary representative. -/
theorem neutralIV126Fourier_ae_bound (v : 𝓢(ℝ,ℂ)) (C : ℝ)
    (h : ∀ ξ : ℝ, ‖(𝓕 v : 𝓢(ℝ,ℂ)) ξ‖^2 ≤ C*ξ^2) :
    ∀ᵐ ξ ∂volume, ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2 ≤ C*ξ^2 := by
  rw [SchwartzMap.toLp_fourier_eq v]
  filter_upwards [((𝓕 v : 𝓢(ℝ,ℂ)).coeFn_toLp 2 volume)] with ξ hξ
  rw [hξ]
  exact h ξ

/-- A.e. low-band receiver, avoiding the stronger IV125 pointwise premise. -/
theorem neutralIV126LowBand_ae (v : 𝓢(ℝ,ℂ)) (T C : ℝ) (hT : 0 ≤ T)
    (hpoint : ∀ᵐ ξ ∂volume,
      ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2 ≤ C*ξ^2) :
    (∫ ξ in Set.Ioc (-T) T,
      ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2) ≤ C*(2*T^3/3) := by
  have hf : Integrable (fun ξ : ℝ =>
      ‖(𝓕 (v.toLp 2 volume) : RealComplexL2) ξ‖^2) :=
    (memLp_two_iff_integrable_sq_norm
      (Lp.aestronglyMeasurable (𝓕 (v.toLp 2 volume) : RealComplexL2))).mp (Lp.memLp _)
  have hp : IntegrableOn (fun ξ : ℝ => ξ^2) (Set.Ioc (-T) T) :=
    ((continuous_id.pow 2).intervalIntegrable (-T) T).1
  have hc : (∫ ξ in Set.Ioc (-T) T, C*ξ^2) = C*(2*T^3/3) := by
    rw [← intervalIntegral.integral_of_le (by linarith : -T ≤ T),
      intervalIntegral.integral_const_mul, integral_pow]
    norm_num <;> ring
  rw [← hc]
  apply setIntegral_mono_on_ae hf.integrableOn (hp.const_mul C) measurableSet_Ioc
  filter_upwards [hpoint] with ξ hξ _
  exact hξ

#print axioms neutralIV126Phase_norm
#print axioms neutralIV126Phase_sub
#print axioms neutralIV126Node_step
#print axioms neutralIV126Equal_end
#print axioms neutralIV126Cell_payment
#print axioms neutralIV126Partition_payment
#print axioms neutralIV126Window_payment
#print axioms neutralIV126Fourier_ae_bound
#print axioms neutralIV126LowBand_ae

end
end WeilDefect
