import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-! V10B30a: independently auditable polynomial/logarithm Gram algebra.
The three moment arrays are actual integrals, not chosen approximations.
All analytic integrability inputs are exposed. -/
namespace WeilDefect.MasterRecon.V10B30a

open MeasureTheory Set
open scoped BigOperators

noncomputable def ell (z : ℝ) : ℝ := Real.log z+Real.log (1-z)
noncomputable def poly (n : ℕ) (c : ℕ → ℝ) (z : ℝ) : ℝ :=
  ∑ j ∈ Finset.range n, c j*z^j
noncomputable def moment (s k : ℕ) : ℝ :=
  ∫ z in Ioo (0:ℝ) 1, z^k*(ell z)^s
noncomputable def block (m n s : ℕ) (a b : ℕ → ℝ) : ℝ :=
  ∑ j ∈ Finset.range m, ∑ k ∈ Finset.range n, a j*b k*moment s (j+k)

theorem block_integral (m n s : ℕ) (a b : ℕ → ℝ)
    (hi : ∀ k : ℕ, IntegrableOn (fun z : ℝ => z^k*(ell z)^s) (Ioo 0 1)) :
    (∫ z in Ioo (0:ℝ) 1, poly m a z*poly n b z*(ell z)^s) =
      block m n s a b := by
  have he : (fun z : ℝ => poly m a z*poly n b z*(ell z)^s) =
      fun z => ∑ j ∈ Finset.range m, ∑ k ∈ Finset.range n,
        (a j*b k)*(z^(j+k)*(ell z)^s) := by
    funext z
    unfold poly
    rw [Finset.sum_mul,Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro j _
    rw [Finset.mul_sum,Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro k _
    rw [pow_add]
    ring
  have hterm (j k : ℕ) : IntegrableOn
      (fun z : ℝ => (a j*b k)*(z^(j+k)*(ell z)^s)) (Ioo 0 1) :=
    (hi (j+k)).const_mul _
  rw [he,integral_finset_sum]
  · unfold block
    apply Finset.sum_congr rfl
    intro j _
    rw [integral_finset_sum]
    · apply Finset.sum_congr rfl
      intro k _
      exact integral_const_mul _ _
    · intro k _
      exact hterm j k
  · intro j _
    exact integrable_finset_sum _ (fun k _ => hterm j k)

theorem block_integrable (m n s : ℕ) (a b : ℕ → ℝ)
    (hi : ∀ k : ℕ, IntegrableOn (fun z : ℝ => z^k*(ell z)^s) (Ioo 0 1)) :
    IntegrableOn (fun z : ℝ => poly m a z*poly n b z*(ell z)^s) (Ioo 0 1) := by
  have he : (fun z : ℝ => poly m a z*poly n b z*(ell z)^s) =
      fun z => ∑ j ∈ Finset.range m, ∑ k ∈ Finset.range n,
        (a j*b k)*(z^(j+k)*(ell z)^s) := by
    funext z
    unfold poly
    rw [Finset.sum_mul,Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro j _
    rw [Finset.mul_sum,Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro k _
    rw [pow_add]
    ring
  rw [he]
  exact integrable_finset_sum _ (fun j _ =>
    integrable_finset_sum _ (fun k _ => (hi (j+k)).const_mul (a j*b k)))

noncomputable def action (m n : ℕ) (a p : ℕ → ℝ) (z : ℝ) : ℝ :=
  poly m a z-poly n p z*ell z/2

theorem residual_gram (m n : ℕ) (a b p q : ℕ → ℝ)
    (hi : ∀ s : ℕ, s ≤ 2 → ∀ k : ℕ,
      IntegrableOn (fun z : ℝ => z^k*(ell z)^s) (Ioo 0 1)) :
    (∫ z in Ioo (0:ℝ) 1, action m n a p z*action m n b q z) =
      block m m 0 a b-(block m n 1 a q+block m n 1 b p)/2+
        block n n 2 p q/4 := by
  let A := fun z => poly m a z*poly m b z*(ell z)^0
  let B := fun z => poly m a z*poly n q z*(ell z)^1
  let C := fun z => poly m b z*poly n p z*(ell z)^1
  let D := fun z => poly n p z*poly n q z*(ell z)^2
  have ha : IntegrableOn A (Ioo 0 1) := block_integrable m m 0 a b (hi 0 (by decide))
  have hb : IntegrableOn B (Ioo 0 1) := block_integrable m n 1 a q (hi 1 (by decide))
  have hc : IntegrableOn C (Ioo 0 1) := block_integrable m n 1 b p (hi 1 (by decide))
  have hd : IntegrableOn D (Ioo 0 1) := block_integrable n n 2 p q (hi 2 (by decide))
  have he : (fun z => action m n a p z*action m n b q z) =
      fun z => A z-(B z+C z)/2+D z/4 := by
    funext z
    dsimp [action,A,B,C,D]
    ring
  rw [he,integral_add (ha.sub ((hb.add hc).div_const 2)) (hd.div_const 4),
    integral_sub ha ((hb.add hc).div_const 2),integral_div,integral_add hb hc,integral_div]
  dsimp only [A,B,C,D]
  rw [block_integral m m 0 a b (hi 0 (by decide)),
    block_integral m n 1 a q (hi 1 (by decide)),
    block_integral m n 1 b p (hi 1 (by decide)),
    block_integral n n 2 p q (hi 2 (by decide))]

theorem energy_pairing (m n : ℕ) (a p q : ℕ → ℝ)
    (hi : ∀ s : ℕ, s ≤ 1 → ∀ k : ℕ,
      IntegrableOn (fun z : ℝ => z^k*(ell z)^s) (Ioo 0 1)) :
    (∫ z in Ioo (0:ℝ) 1, action m n a p z*poly n q z) =
      block m n 0 a q-block n n 1 p q/2 := by
  let A := fun z => poly m a z*poly n q z*(ell z)^0
  let B := fun z => poly n p z*poly n q z*(ell z)^1
  have ha : IntegrableOn A (Ioo 0 1) := block_integrable m n 0 a q (hi 0 (by decide))
  have hb : IntegrableOn B (Ioo 0 1) := block_integrable n n 1 p q (hi 1 (by decide))
  have he : (fun z => action m n a p z*poly n q z) = fun z => A z-B z/2 := by
    funext z
    dsimp [action,A,B]
    ring
  rw [he,integral_sub ha (hb.div_const 2),integral_div]
  dsimp only [A,B]
  rw [block_integral m n 0 a q (hi 0 (by decide)),
    block_integral n n 1 p q (hi 1 (by decide))]

end WeilDefect.MasterRecon.V10B30a

#print axioms WeilDefect.MasterRecon.V10B30a.block_integral
#print axioms WeilDefect.MasterRecon.V10B30a.block_integrable
#print axioms WeilDefect.MasterRecon.V10B30a.residual_gram
#print axioms WeilDefect.MasterRecon.V10B30a.energy_pairing
