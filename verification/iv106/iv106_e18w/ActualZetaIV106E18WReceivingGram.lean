import WeilDefect.Arithmetic.ActualZetaIV106E18WNativePerturbation

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- Original supported smooth arithmetic pairing, compared to the
actual native rough carrier pairing with no new source assumption. -/
theorem neutralIV106E18WOriginal_error (a : ℝ) (ha : 0 ≤ a)
    (s t : 𝓢(ℝ,ℂ))
    (hs : ∀ x ∉ Set.Icc (-a) a, s x = 0)
    (ht : ∀ x ∉ Set.Icc (-a) a, t x = 0)
    (p q : NeutralLogHilbertCarrier a) (K M δ : ℝ)
    (hK : ‖neutralActualZetaLogWeilFormOperator a‖ ≤ K)
    (hM : 0 ≤ M) (hδ : 0 ≤ δ)
    (hp : ‖p‖ ≤ M) (hq : ‖q‖ ≤ M)
    (hsp : ‖neutralIV102Lift a s hs-p‖ ≤ δ)
    (htq : ‖neutralIV102Lift a t ht-q‖ ≤ δ) :
    ‖neutralIV101Mixed a s t -
      inner ℂ p (neutralActualZetaLogWeilFormOperator a q)‖ ≤
      K*(2*M*δ+δ^2) := by
  rw [neutralIV103Mixed_native a ha s t hs ht]
  exact neutralIV106E18WUniform a p q _ _ K M δ hK hM hδ hp hq hsp htq

/-- Exact observation matching and native log norm approximation of one
literal rough polynomial, on its unchanged buffered cell. -/
theorem neutralIV106E18WCell (k : ℕ) (hk : 0 < k)
    (l h b : ℝ) (hh : 0 < h) (hb : 0 < b)
    (hw : Set.Icc (l-b) (l+h+b) ⊆ Set.Icc (-(11/10:ℝ)) (11/10))
    (p : NeutralLogHilbertCarrier (11/10:ℝ))
    (hp : neutralLogPhysical p.val = (neutralIV106E18JTrial_memLp l h hh).toLp _)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ s : 𝓢(ℝ,ℂ),
      (∀ x ∉ Set.Icc (l-b) (l+h+b), s x = 0) ∧
      neutralIV106E18RObserve k hk (s.toLp 2 volume) =
        neutralIV106E18RObserve k hk (neutralLogPhysical p.val) ∧
      ∃ hs : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), s x = 0,
        ‖neutralIV102Lift (11/10:ℝ) s hs-p‖ ≤ neutralIV106E18WConstant*ε := by
  obtain ⟨s,hs,ho,_,_,he⟩ := neutralIV106E18VLiteral_match k hk l h b hh hb ε hε
  have hs' : ∀ x ∉ Set.Icc (-(11/10:ℝ)) (11/10), s x = 0 :=
    fun x hx => hs x (fun hi => hx (hw hi))
  refine ⟨s,hs,?_,hs',?_⟩
  · rw [hp]
    exact ho
  · exact neutralIV106E18WLift_error _ p s hs' _ hp ε hε.le he

/-- Finite Hermitian matrix reserve, stated in coefficient L1 mass.
This does not assume that the coordinate family is independent. -/
theorem neutralIV106E18WMatrix_error {J : Type*} [Fintype J]
    (G H : J → J → ℂ) (c : J → ℂ) (r : ℝ)
    (hr : 0 ≤ r) (h : ∀ i j, ‖G i j-H i j‖ ≤ r) :
    ‖(∑ i, ∑ j, conj (c i)*c j*G i j) -
      (∑ i, ∑ j, conj (c i)*c j*H i j)‖ ≤
      r*(∑ i, ‖c i‖)^2 := by
  classical
  have he : (∑ i, ∑ j, conj (c i)*c j*G i j) -
      (∑ i, ∑ j, conj (c i)*c j*H i j) =
      ∑ i, ∑ j, conj (c i)*c j*(G i j-H i j) := by
    simp only [mul_sub, Finset.sum_sub_distrib]
  rw [he]
  calc
    _ ≤ ∑ i, ‖∑ j, conj (c i)*c j*(G i j-H i j)‖ :=
      norm_sum_le _ _
    _ ≤ ∑ i, ∑ j, ‖conj (c i)*c j*(G i j-H i j)‖ :=
      Finset.sum_le_sum (fun i _ => norm_sum_le _ _)
    _ ≤ ∑ i, ∑ j, ‖c i‖*‖c j‖*r := by
      apply Finset.sum_le_sum
      intro i hi
      apply Finset.sum_le_sum
      intro j hj
      rw [norm_mul,norm_mul,Complex.norm_conj]
      exact mul_le_mul_of_nonneg_left (h i j) (mul_nonneg (norm_nonneg _) (norm_nonneg _))
    _ = r*(∑ i, ‖c i‖)^2 := by
      simp only [← Finset.sum_mul, ← Finset.mul_sum]
      ring

/-- Lower reserve transports to the new Gram quadratic. A norm bound
on entry differences alone is not a positivity certificate. -/
theorem neutralIV106E18WMatrix_lower {J : Type*} [Fintype J]
    (G H : J → J → ℂ) (c : J → ℂ) (r : ℝ)
    (hr : 0 ≤ r) (h : ∀ i j, ‖G i j-H i j‖ ≤ r) :
    (∑ i, ∑ j, conj (c i)*c j*H i j).re-r*(∑ i, ‖c i‖)^2 ≤
      (∑ i, ∑ j, conj (c i)*c j*G i j).re := by
  have hn := neutralIV106E18WMatrix_error G H c r hr h
  have ha := (Complex.abs_re_le_norm _).trans hn
  rw [Complex.sub_re] at ha
  have hl := (abs_le.mp ha).1
  linarith

#print axioms neutralIV106E18WOriginal_error
#print axioms neutralIV106E18WCell
#print axioms neutralIV106E18WMatrix_error
#print axioms neutralIV106E18WMatrix_lower
end
end WeilDefect
