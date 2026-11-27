import Mathlib.Analysis.Normed.Operator.Compact.Basic
import Mathlib.Analysis.Normed.Module.FiniteDimension
import Mathlib.LinearAlgebra.Vandermonde
import Mathlib.Tactic

/-! RETURN108-K: generic full-kernel and finite-observation receivers.
No zeta arithmetic, positivity, critical-line supply or Green density is
postulated. Actual translation/moment observations are a separate attachment.
This is a staging candidate pending native compilation and named axiom audit. -/
namespace WeilDefect.MasterReturn.KernelCompleteness

open Set
open scoped BigOperators

variable {H E : Type*} [NormedAddCommGroup H] [NormedSpace ℂ H]
    [NormedAddCommGroup E] [NormedSpace ℂ E]

/-- Any closed submodule fixed pointwise by a compact operator is finite
dimensional. Use compact restriction, then Riesz's compact-ball theorem. -/
theorem finiteDimensional_of_compact_fixed
    (S : Submodule ℂ H) (hS : IsClosed (S : Set H))
    (K : H →L[ℂ] H) (hK : IsCompactOperator K)
    (hfix : ∀ x ∈ S, K x = x) : FiniteDimensional ℂ S := by
  have hm : ∀ x ∈ S, K.toLinearMap x ∈ S := by
    intro x hx
    change K x ∈ S
    rw [hfix x hx]
    exact hx
  have hk : IsCompactOperator (K.toLinearMap.restrict hm) :=
    (show IsCompactOperator K.toLinearMap from hK).restrict hm hS
  have hid : K.toLinearMap.restrict hm = LinearMap.id := by
    ext x
    apply Subtype.ext
    exact hfix x.val x.property
  rw [hid] at hk
  obtain ⟨C, hC, hsub⟩ := hk.image_closedBall_subset_compact 1
  apply FiniteDimensional.of_isCompact_closedBall ℂ (by norm_num : (0 : ℝ) < 1)
  apply hC.of_isClosed_subset Metric.isClosed_closedBall
  intro x hx
  apply hsub
  exact ⟨x, hx, rfl⟩

/-- The full sampling kernel is finite when a bounded receiver factoring
through the sample map is identity plus compact. No adjoint is needed. -/
theorem fullKernel_finite_of_compactSigned
    (T : H →L[ℂ] E) (R : E →L[ℂ] H)
    (K : H →L[ℂ] H) (hK : IsCompactOperator K)
    (hfactor : R.comp T = ContinuousLinearMap.id ℂ H + K) :
    FiniteDimensional ℂ T.toLinearMap.ker := by
  apply finiteDimensional_of_compact_fixed T.toLinearMap.ker T.isClosed_ker (-K) hK.neg
  intro x hx
  have hx0 : T x = 0 := hx
  have he := congrArg (fun A : H →L[ℂ] H => A x) hfactor
  simp only [ContinuousLinearMap.comp_apply, hx0, map_zero,
    ContinuousLinearMap.add_apply, ContinuousLinearMap.id_apply] at he
  change -(K x) = x
  exact neg_eq_iff_add_eq_zero.mpr (by simpa [add_comm] using he.symm)

/-- A bank with geometric observations at n distinct nodes is independent.
Rows may carry arbitrary nonzero factors, including the original Mellin
transform at each node. This is the finite algebraic part of the
equally-spaced translation argument. -/
theorem independent_of_vandermonde_observations
    {n : ℕ} (v : Fin n → H) (L : Fin n → H →ₗ[ℂ] ℂ)
    (z c : Fin n → ℂ) (hz : Function.Injective z)
    (hc : ∀ j, c j ≠ 0)
    (hobs : ∀ j i, L j (v i) = c j * z j ^ (i : ℕ)) :
    LinearIndependent ℂ v := by
  classical
  rw [Fintype.linearIndependent_iff']
  intro a ha
  have hrows : ∀ j, (∑ i : Fin n, z j ^ (i : ℕ) * a i) = 0 := by
    intro j
    have h := congrArg (L j) ha
    simp only [map_sum, map_smul, map_zero, smul_eq_mul, hobs] at h
    have hf : (∑ i : Fin n, a i * (c j * z j ^ (i : ℕ))) =
        c j * (∑ i : Fin n, z j ^ (i : ℕ) * a i) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro i hi
      ring
    rw [hf] at h
    exact (mul_eq_zero.mp h).resolve_left (hc j)
  have hz0 : a = 0 := Matrix.eq_zero_of_forall_index_sum_pow_mul_eq_zero hz hrows
  intro i
  exact congrFun hz0 i

/-- A finite-dimensional receiving kernel cannot contain banks of arbitrary
finite size. The bank must lie in that exact kernel, not only approximate it. -/
theorem zero_of_arbitrarily_large_kernel_banks
    {X : Type*} [AddCommGroup X] (T : H →L[ℂ] E)
    (hfin : FiniteDimensional ℂ T.toLinearMap.ker)
    (x : X)
    (hbanks : x ≠ 0 → ∀ n : ℕ,
      ∃ v : Fin n → T.toLinearMap.ker, LinearIndependent ℂ v) : x = 0 := by
  classical
  by_contra hx
  letI : FiniteDimensional ℂ T.toLinearMap.ker := hfin
  obtain ⟨v, hv⟩ := hbanks hx (Module.finrank ℂ T.toLinearMap.ker + 1)
  have h := hv.fintype_card_le_finrank
  rw [Fintype.card_fin] at h
  omega

/-- Combine the two independent suppliers: identity-plus-compact factor,
and exact independent banks arising from a hypothetical nonzero vector.
In the intended application X is the smaller-window sampling kernel. -/
theorem fullSample_zero_of_enlarged_compact
    {X : Type*} [AddCommGroup X] (T : H →L[ℂ] E) (R : E →L[ℂ] H)
    (K : H →L[ℂ] H) (hK : IsCompactOperator K)
    (hfactor : R.comp T = ContinuousLinearMap.id ℂ H + K)
    (x : X)
    (hbanks : x ≠ 0 → ∀ n : ℕ,
      ∃ v : Fin n → T.toLinearMap.ker, LinearIndependent ℂ v) : x = 0 :=
  zero_of_arbitrarily_large_kernel_banks T
    (fullKernel_finite_of_compactSigned T R K hK hfactor) x hbanks

end WeilDefect.MasterReturn.KernelCompleteness

#print axioms WeilDefect.MasterReturn.KernelCompleteness.finiteDimensional_of_compact_fixed
#print axioms WeilDefect.MasterReturn.KernelCompleteness.fullKernel_finite_of_compactSigned
#print axioms WeilDefect.MasterReturn.KernelCompleteness.independent_of_vandermonde_observations
#print axioms WeilDefect.MasterReturn.KernelCompleteness.zero_of_arbitrarily_large_kernel_banks
#print axioms WeilDefect.MasterReturn.KernelCompleteness.fullSample_zero_of_enlarged_compact
