import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

/-! V10B39b: finite projection reproduction and stability for a continuous
orthogonal family. No infinite series or density hypotheses. -/
namespace WeilDefect.MasterRecon.V10B39b
open MeasureTheory Set
open scoped BigOperators

noncomputable def project (p : ℕ → ℝ → ℝ) (d : ℕ → ℝ)
    (n : ℕ) (f : ℝ → ℝ) (x : ℝ) : ℝ :=
  ∑ j ∈ Finset.range n, d j*(∫ t in (0:ℝ)..1, f t*p j t)*p j x

theorem finite_pair (p : ℕ → ℝ → ℝ) (d : ℕ → ℝ)
    (hp : ∀ j, Continuous (p j)) (hd : ∀ j, d j ≠ 0)
    (ho : ∀ i j, (∫ t in (0:ℝ)..1, p i t*p j t)=
      if i=j then (d j)⁻¹ else 0)
    (n j : ℕ) (hj : j ∈ Finset.range n) (a : ℕ → ℝ) :
    (∫ t in (0:ℝ)..1, (∑ i ∈ Finset.range n, a i*p i t)*p j t) =
      a j*(d j)⁻¹ := by
  have he : (fun t : ℝ => (∑ i ∈ Finset.range n, a i*p i t)*p j t) =
      fun t => ∑ i ∈ Finset.range n, a i*(p i t*p j t) := by
    funext t
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro i _
    ring
  rw [he,intervalIntegral.integral_finsetSum]
  · simp only [intervalIntegral.integral_const_mul,ho]
    rw [Finset.sum_eq_single j]
    · simp
    · intro i _ hi
      simp [hi]
    · exact fun h => False.elim (h hj)
  · intro i _
    exact (continuous_const.mul ((hp i).mul (hp j))).intervalIntegrable 0 1

theorem project_reproduces (p : ℕ → ℝ → ℝ) (d : ℕ → ℝ)
    (hp : ∀ j, Continuous (p j)) (hd : ∀ j, d j ≠ 0)
    (ho : ∀ i j, (∫ t in (0:ℝ)..1, p i t*p j t)=
      if i=j then (d j)⁻¹ else 0)
    (n : ℕ) (a : ℕ → ℝ) (x : ℝ) :
    project p d n (fun t => ∑ i ∈ Finset.range n, a i*p i t) x =
      ∑ i ∈ Finset.range n, a i*p i x := by
  unfold project
  apply Finset.sum_congr rfl
  intro j hj
  rw [finite_pair p d hp hd ho n j hj a]
  field_simp [hd j]

theorem project_sub (p : ℕ → ℝ → ℝ) (d : ℕ → ℝ)
    (hp : ∀ j, Continuous (p j)) (n : ℕ)
    (f g : ℝ → ℝ) (hf : Continuous f) (hg : Continuous g) (x : ℝ) :
    project p d n f x-project p d n g x =
      project p d n (fun t => f t-g t) x := by
  unfold project
  rw [← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro j _
  have he : (fun t => (f t-g t)*p j t) = fun t => f t*p j t-g t*p j t := by
    funext t
    ring
  have hi := intervalIntegral.integral_sub (μ := volume) ((hf.mul (hp j)).intervalIntegrable 0 1)
    ((hg.mul (hp j)).intervalIntegrable 0 1)
  change (∫ t in (0:ℝ)..1, f t*p j t-g t*p j t) =
    (∫ t in (0:ℝ)..1, f t*p j t) - (∫ t in (0:ℝ)..1, g t*p j t) at hi
  rw [he,hi]
  ring

theorem project_bound (p : ℕ → ℝ → ℝ) (d b : ℕ → ℝ)
    (hp : ∀ j, Continuous (p j)) (hd : ∀ j, 0 ≤ d j)
    (hb : ∀ j, 0 ≤ b j)
    (hpb : ∀ j x, x ∈ Icc (0:ℝ) 1 → |p j x| ≤ b j)
    (n : ℕ) (f : ℝ → ℝ) (hf : Continuous f) (ε : ℝ)
    (hε : 0 ≤ ε) (hfb : ∀ x ∈ Icc (0:ℝ) 1, |f x| ≤ ε)
    (x : ℝ) (hx : x ∈ Icc (0:ℝ) 1) :
    |project p d n f x| ≤ ε*(∑ j ∈ Finset.range n, d j*(b j)^2) := by
  have hi (j : ℕ) : |∫ t in (0:ℝ)..1, f t*p j t| ≤ ε*b j := by
    calc
      _ ≤ ∫ t in (0:ℝ)..1, |f t*p j t| :=
        intervalIntegral.abs_integral_le_integral_abs (by norm_num)
      _ ≤ ∫ _ in (0:ℝ)..1, ε*b j := by
        apply intervalIntegral.integral_mono_on (by norm_num)
          ((hf.mul (hp j)).abs.intervalIntegrable 0 1)
          (continuous_const.intervalIntegrable 0 1)
        intro t ht
        change |f t*p j t| ≤ ε*b j
        rw [abs_mul]
        exact mul_le_mul (hfb t ht) (hpb j t ht) (abs_nonneg _) hε
      _ = _ := by simp
  unfold project
  calc
    _ ≤ ∑ j ∈ Finset.range n, |d j*(∫ t in (0:ℝ)..1, f t*p j t)*p j x| := by
      simpa only [Real.norm_eq_abs] using
        norm_sum_le (Finset.range n)
          (fun j => d j*(∫ t in (0:ℝ)..1, f t*p j t)*p j x)
    _ ≤ ∑ j ∈ Finset.range n, ε*(d j*(b j)^2) := by
      apply Finset.sum_le_sum
      intro j _
      rw [abs_mul,abs_mul,abs_of_nonneg (hd j)]
      calc
        _ ≤ (d j*(ε*b j))*b j :=
          mul_le_mul (mul_le_mul_of_nonneg_left (hi j) (hd j))
            (hpb j x hx) (abs_nonneg _) (mul_nonneg (hd j) (mul_nonneg hε (hb j)))
        _ = _ := by ring
    _ = _ := by rw [Finset.mul_sum]

end WeilDefect.MasterRecon.V10B39b

#print axioms WeilDefect.MasterRecon.V10B39b.finite_pair
#print axioms WeilDefect.MasterRecon.V10B39b.project_reproduces
#print axioms WeilDefect.MasterRecon.V10B39b.project_sub
#print axioms WeilDefect.MasterRecon.V10B39b.project_bound
