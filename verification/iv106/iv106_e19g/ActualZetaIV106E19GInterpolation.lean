import WeilDefect.Arithmetic.ActualZetaIV106E19FReplacement

namespace WeilDefect
noncomputable section
open Finset Matrix
open scoped BigOperators

/-- Elementary symmetric sum over actual subsets of the tuple index.
Repeated node values are allowed; only the index set is finite. -/
def neutralIV106E19GElem {k : ℕ} (r : Fin k → ℝ) (m : ℕ) : ℝ :=
  ∑ s ∈ (Finset.univ : Finset (Fin k)).powersetCard m, ∏ i ∈ s, r i

theorem neutralIV106E19GElem_bound {k : ℕ} (r : Fin k → ℝ)
    (hr : ∀ i, 0 ≤ r i ∧ r i ≤ 1) (m : ℕ) :
    0 ≤ neutralIV106E19GElem r m ∧
      neutralIV106E19GElem r m ≤ (Nat.choose k m : ℝ) := by
  classical
  unfold neutralIV106E19GElem
  constructor
  · exact Finset.sum_nonneg fun s _ => Finset.prod_nonneg fun i _ => (hr i).1
  · calc
      _ ≤ ∑ s ∈ (Finset.univ : Finset (Fin k)).powersetCard m, (1:ℝ) := by
        apply Finset.sum_le_sum
        intro s hs
        simpa using (Finset.prod_le_prod (f := r) (g := fun _ => (1:ℝ))
          (s := s) (fun i _ => (hr i).1) (fun i _ => (hr i).2))
      _ = _ := by simp [Finset.card_powersetCard]

/-- Expand the finite product by grouping subsets by cardinality. -/
theorem neutralIV106E19GProduct {k : ℕ} (r : Fin k → ℝ) (x : ℝ) :
    (∏ i, (1-r i*x)) =
      ∑ m ∈ Finset.range (k+1), (-x)^m * neutralIV106E19GElem r m := by
  classical
  calc
    _ = ∑ s ∈ (Finset.univ : Finset (Fin k)).powerset, ∏ i ∈ s, (-x)*r i := by
      have h := Finset.prod_one_add (f := fun i : Fin k => (-x)*r i)
        (Finset.univ : Finset (Fin k))
      convert h using 1
      apply Finset.prod_congr rfl
      intro i hi
      ring
    _ = ∑ m ∈ Finset.range (k+1),
        ∑ s ∈ (Finset.univ : Finset (Fin k)).powersetCard m, ∏ i ∈ s, (-x)*r i := by
      rw [Finset.powerset_card_biUnion, Finset.sum_biUnion]
      · simp
      · intro a ha b hb hab
        exact Finset.disjoint_powersetCard_of_ne hab _ _
    _ = _ := by
      apply Finset.sum_congr rfl
      intro m hm
      unfold neutralIV106E19GElem
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro s hs
      rw [Finset.prod_mul_distrib,Finset.prod_const,(Finset.mem_powersetCard.mp hs).2]

def neutralIV106E19GCoeff {k : ℕ} (r : Fin k → ℝ) (j : Fin k) : ℝ :=
  (-1:ℝ)^j.val * neutralIV106E19GElem r (j.val+1)

theorem neutralIV106E19GCoeff_bound {k : ℕ} (r : Fin k → ℝ)
    (hr : ∀ i, 0 ≤ r i ∧ r i ≤ 1) (j : Fin k) :
    0 ≤ (-1:ℝ)^j.val*neutralIV106E19GCoeff r j ∧
      (-1:ℝ)^j.val*neutralIV106E19GCoeff r j ≤ (Nat.choose k (j.val+1):ℝ) := by
  unfold neutralIV106E19GCoeff
  have h : (-1:ℝ)^j.val * (-1:ℝ)^j.val = 1 := by
    rw [← mul_pow]
    norm_num
  rw [← mul_assoc,h,one_mul]
  exact neutralIV106E19GElem_bound r hr _

/-- The quotient polynomial is evaluated by its coefficients, so this
identity is valid at x=0 and even for repeated nodes. -/
theorem neutralIV106E19GPolynomial {k : ℕ} (r : Fin k → ℝ) (x : ℝ) :
    x*(∑ j : Fin k, neutralIV106E19GCoeff r j*x^j.val) =
      1-∏ i, (1-r i*x) := by
  rw [neutralIV106E19GProduct, Finset.sum_range_succ']
  have h0 : neutralIV106E19GElem r 0 = 1 := by
    simp [neutralIV106E19GElem,Finset.powersetCard_zero]
  rw [pow_zero,h0,mul_one]
  rw [Finset.mul_sum,Fin.sum_univ_eq_sum_range]
  have he : (∑ j ∈ Finset.range k,
      x*((-1:ℝ)^j*neutralIV106E19GElem r (j+1)*x^j)) =
      -(∑ j ∈ Finset.range k, (-x)^(j+1)*neutralIV106E19GElem r (j+1)) := by
    rw [Finset.sum_neg_distrib.symm]
    apply Finset.sum_congr rfl
    intro j hj
    rw [pow_succ,show -x = (-1:ℝ)*x by ring,mul_pow]
    ring
  simp only [neutralIV106E19GCoeff] at *
  rw [he]
  ring

/-- Exact reciprocal interpolation; no Vandermonde inverse and no
distinctness hypothesis. The product vanishes at its chosen factor. -/
theorem neutralIV106E19GReciprocal {k : ℕ} (X : Fin k → ℝ)
    (hX : ∀ i, X i ≠ 0) (i : Fin k) :
    (X i)⁻¹ = ∑ j : Fin k,
      neutralIV106E19GCoeff (fun l => (X l)⁻¹) j * (X i)^j.val := by
  have hp := neutralIV106E19GPolynomial (fun l => (X l)⁻¹) (X i)
  have hz : (∏ l : Fin k, (1-(X l)⁻¹*X i)) = 0 := by
    apply Finset.prod_eq_zero (Finset.mem_univ i)
    rw [inv_mul_cancel₀ (hX i),sub_self]
  rw [hz,sub_zero] at hp
  apply (mul_left_cancel₀ (hX i))
  rw [mul_inv_cancel₀ (hX i),hp]

#print axioms neutralIV106E19GElem_bound
#print axioms neutralIV106E19GProduct
#print axioms neutralIV106E19GCoeff_bound
#print axioms neutralIV106E19GPolynomial
#print axioms neutralIV106E19GReciprocal
end
end WeilDefect
