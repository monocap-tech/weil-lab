import Mathlib

namespace WeilDefect

/-! NF659: source-independent interval transport through a fixed
finite rational congruence. Unlike a numerical equality gate, these
lemmas take *arbitrary real* source entries lying within the checked
balls, and prove the transformed entries lie in the propagated balls.

No numerical truth or positivity hypothesis is introduced here. -/

theorem neutralNF659WeightedSum_bound
    {ι : Type*} [Fintype ι] (w a c r : ι → ℝ)
    (h : ∀ i, |a i - c i| ≤ r i) :
    |(∑ i, w i * a i) - (∑ i, w i * c i)| ≤
      ∑ i, |w i| * r i := by
  have ht (i : ι) :
      |w i * (a i - c i)| ≤ |w i| * r i := by
    rw [abs_mul]
    exact mul_le_mul_of_nonneg_left (h i) (abs_nonneg _)
  calc
    |(∑ i, w i * a i) - (∑ i, w i * c i)| =
        |∑ i, w i * (a i - c i)| := by
          simp only [mul_sub, Finset.sum_sub_distrib]
    _ ≤ ∑ i, |w i * (a i - c i)| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ i, |w i| * r i :=
      Finset.sum_le_sum (fun i _ => ht i)

theorem neutralNF659DoubleSum_bound
    {ι κ : Type*} [Fintype ι] [Fintype κ]
    (w a c r : ι → κ → ℝ)
    (h : ∀ i j, |a i j - c i j| ≤ r i j) :
    |(∑ i, ∑ j, w i j * a i j) -
        (∑ i, ∑ j, w i j * c i j)| ≤
      ∑ i, ∑ j, |w i j| * r i j := by
  have hi (i : ι) :
      |(∑ j, w i j * a i j) -
          (∑ j, w i j * c i j)| ≤
        ∑ j, |w i j| * r i j :=
    neutralNF659WeightedSum_bound
      (w i) (a i) (c i) (r i) (h i)
  have ho := neutralNF659WeightedSum_bound
    (fun _ : ι => (1 : ℝ))
    (fun i => ∑ j, w i j * a i j)
    (fun i => ∑ j, w i j * c i j)
    (fun i => ∑ j, |w i j| * r i j) hi
  simpa only [one_mul, abs_one] using ho

/-- This is the exact congruence interval bound used for the
NF657 rational change of basis. Its proof is uniform in the
number of coordinates and does not invoke a positivity theorem. -/
theorem neutralNF659CongruenceEntry_bound
    {n : ℕ}
    (H C E K : Fin n → Fin n → ℝ)
    (h : ∀ p q, |H p q - C p q| ≤ E p q)
    (i j : Fin n) :
    |(∑ p : Fin n, ∑ q : Fin n, K i p * K j q * H p q) -
        (∑ p : Fin n, ∑ q : Fin n, K i p * K j q * C p q)| ≤
      ∑ p : Fin n, ∑ q : Fin n,
        |K i p * K j q| * E p q := by
  exact neutralNF659DoubleSum_bound
    (fun p q => K i p * K j q) H C E h

#print axioms neutralNF659CongruenceEntry_bound

end WeilDefect
