import WeilDefect.MasterRecon.V02
import WeilDefect.MasterRecon.V03
import WeilDefect.MasterRecon.V04

/-! MASTER-RECON V05A. Assemble the actual Gram strong limit and
the typed Picard compression identity. Explicit block identities remain
visible; the canonical direct-sum instantiation is a separate check. -/

namespace WeilDefect.MasterRecon.V05

open Filter
open scoped InnerProduct NNReal Topology BigOperators

variable {H X K L : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup X] [InnerProductSpace ℂ X] [CompleteSpace X]
variable [NormedAddCommGroup K] [InnerProductSpace ℂ K] [CompleteSpace K]
variable [NormedAddCommGroup L] [InnerProductSpace ℂ L] [CompleteSpace L]

/-- V04 inverse existence and V03 strong convergence on the actual Gram. -/
theorem gram_scaled_resolvent_sequence
    (S : L →L[ℂ] X) (η : ℕ → ℝ≥0)
    (hη : ∀ n, 0 < η n)
    (hη0 : Tendsto (fun n => (η n : ℝ)) atTop (𝓝 0)) :
    ∃ R : ℕ → L →L[ℂ] L,
      (∀ n x, R n (((S.adjoint) ∘L S) x + ((η n : ℝ) : ℂ) • x) = x) ∧
      (∀ n x, ((S.adjoint) ∘L S) (R n x) + ((η n : ℝ) : ℂ) • R n x = x) ∧
      (∀ x, Tendsto (fun n => ((η n : ℝ) : ℂ) • R n x)
        atTop (𝓝 (S.ker.starProjection x))) := by
  let B : L →L[ℂ] L := (S.adjoint) ∘L S
  have hp : B.IsPositive := ContinuousLinearMap.isPositive_adjoint_comp_self S
  have hex := fun n => V04.positive_shift_inverse B hp (η n) (hη n)
  choose R hR using hex
  let C : ℕ → L →L[ℂ] L := fun n => ((η n : ℝ) : ℂ) • R n
  have hl := fun n => (V03.scaled_inverse_laws B (R n) ((η n : ℝ) : ℂ) (hR n).1)
  have hc : ∀ n z, ‖C n z‖ ≤ ‖z‖ := fun n z => (hR n).2.2 z
  have hfix : ∀ n x, C n (S.ker.starProjection x) = S.ker.starProjection x := by
    intro n x
    have hm : S.ker.starProjection x ∈ B.ker := by
      change S.ker.starProjection x ∈ ((S.adjoint) ∘L S).ker
      rw [ContinuousLinearMap.ker_adjoint_comp_self]
      exact Submodule.starProjection_apply_mem S.ker x
    exact (hl n).1 _ hm
  have hres : ∀ n y, C n (B y) = ((η n : ℝ) : ℂ) • (y - C n y) :=
    fun n y => (hl n).2 y
  refine ⟨R, fun n => (hR n).1, fun n => (hR n).2.1, ?_⟩
  intro x
  exact V03.strong_limit_of_range_approx B S.ker.starProjection C
    (fun n => (η n : ℝ)) (fun n => (η n).coe_nonneg) hη0 hc hfix hres
    (V04.gram_range_approximation S) x

/-- The finite-channel Picard operator is invertible from the physical
positive inverse equation, without assuming positivity of its inverse. -/
theorem picard_operator_isUnit
    (P : H →L[ℂ] X) (M : K →L[ℂ] X)
    (R : X →L[ℂ] X) (η : ℝ≥0)
    (hR : ∀ z, (P ∘L (P.adjoint)) (R z) + ((η : ℝ) : ℂ) • R z = z) :
    IsUnit (1 + (M.adjoint) ∘L R ∘L M) := by
  apply ContinuousLinearMap.isUnit_of_forall_le_norm_inner_map _ (c := 1) (by norm_num)
  intro u
  have hp := ContinuousLinearMap.isPositive_self_comp_adjoint P
  have h := V04.shifted_energy_lower (P ∘L (P.adjoint)) hp η (R (M u))
  rw [hR (M u)] at h
  have hn : 0 ≤ (inner ℂ (M u) (R (M u))).re :=
    le_trans (by positivity) h
  have hr : 0 ≤ (inner ℂ ((M.adjoint) (R (M u))) u).re := by
    rw [M.adjoint_inner_left]
    have heq : (inner ℂ (R (M u)) (M u)).re =
        (inner ℂ (M u) (R (M u))).re :=
      inner_re_symm (𝕜 := ℂ) (R (M u)) (M u)
    rw [heq]
    exact hn
  have he : (inner ℂ ((1 + (M.adjoint) ∘L R ∘L M) u) u).re =
      ‖u‖ ^ 2 + (inner ℂ ((M.adjoint) (R (M u))) u).re := by
    change (inner ℂ (u + (M.adjoint) (R (M u))) u).re = _
    rw [inner_add_left, Complex.add_re]
    have hh : (inner ℂ u u).re = ‖u‖ ^ 2 := inner_self_eq_norm_sq (𝕜 := ℂ) u
    rw [hh]
  calc
    ‖u‖ ^ 2 * ((1 : ℝ≥0) : ℝ) ≤
        (inner ℂ ((1 + (M.adjoint) ∘L R ∘L M) u) u).re := by
      rw [he]
      simpa only [NNReal.coe_one, mul_one] using
        (le_add_of_nonneg_right (a := ‖u‖ ^ 2) hr)
    _ ≤ ‖inner ℂ ((1 + (M.adjoint) ∘L R ∘L M) u) u‖ := Complex.re_le_norm _

/-- Assemble the two certified algebraic identities with typed block maps.
All inverse equations and block relations are explicit. -/
theorem picard_compression_apply
    (P : H →L[ℂ] X) (M : K →L[ℂ] X) (S : L →L[ℂ] X)
    (i : K →L[ℂ] L) (ell : L →L[ℂ] K)
    (A R T : X →L[ℂ] X) (C : K →L[ℂ] K) (B : L →L[ℂ] L)
    (η : ℂ)
    (hA : ∀ z, A z = P ((P.adjoint) z) + η • z)
    (hR : ∀ z, R (A z) = z)
    (hSS : ∀ z, S ((S.adjoint) z) = P ((P.adjoint) z) + M ((M.adjoint) z))
    (hT : ∀ z, S ((S.adjoint) (T z)) + η • T z = z)
    (hB : ∀ z, B ((S.adjoint) (S z) + η • z) = z)
    (hC : ∀ u, C (u + (M.adjoint) (R (M u))) = u)
    (hi : ∀ u, S (i u) = M u)
    (hell : ∀ z, ell ((S.adjoint) z) = (M.adjoint) z)
    (hei : ∀ u, ell (i u) = u)
    (u : K) :
    C u = ell (η • B (i u)) := by
  have htw : ∀ x, A (T (M x)) + M ((M.adjoint) (T (M x))) = M x := by
    intro x
    calc
      A (T (M x)) + M ((M.adjoint) (T (M x))) =
          S ((S.adjoint) (T (M x))) + η • T (M x) := by
        rw [hA, hSS]
        abel
      _ = M x := hT (M x)
  have hw := V02.picard_woodbury_apply A R T M (M.adjoint) C hR htw hC u
  have hcoef := V02.coefficient_resolvent_apply S (S.adjoint) T B η
    (fun x => hT (S x)) hB (i u)
  calc
    C u = u - (M.adjoint) (T (M u)) := hw
    _ = ell (i u - (S.adjoint) (T (S (i u)))) := by
      rw [map_sub, hei, hell, hi]
    _ = ell (η • B (i u)) := congrArg ell hcoef


section FiniteCompression

variable {ι : Type*} [Fintype ι]

/-- Pointwise convergence on a finite selected domain implies norm
convergence. The coordinate expansion is explicitly in the physical metric. -/
theorem finite_selected_norm_limit
    (D : ℕ → K →L[ℂ] K) (e : ι → K)
    (hexp : ∀ x : K, ∃ a : ι → ℂ,
      x = ∑ i, a i • e i ∧ ∀ i, ‖a i‖ ≤ ‖x‖)
    (hpoint : ∀ x, Tendsto (fun n => D n x) atTop (𝓝 0)) :
    Tendsto (fun n => ‖D n‖) atTop (𝓝 0) := by
  classical
  have hcol : ∀ i : ι, Tendsto (fun n => ‖D n (e i)‖) atTop (𝓝 0) := by
    intro i
    simpa using (hpoint (e i)).norm
  have hs : ∀ s : Finset ι,
      Tendsto (fun n => ∑ i ∈ s, ‖D n (e i)‖) atTop (𝓝 0) := by
    intro s
    induction s using Finset.induction_on with
    | empty => simp
    | @insert i s hi ih =>
      simp only [Finset.sum_insert hi]
      simpa using (hcol i).add ih
  apply Metric.tendsto_nhds.mpr
  intro ε hε
  have hev := (Metric.tendsto_nhds.mp (hs Finset.univ)) ε hε
  filter_upwards [hev] with n hn
  rw [Real.dist_eq, sub_zero, abs_of_nonneg (norm_nonneg _)]
  rw [Real.dist_eq, sub_zero,
    abs_of_nonneg (Finset.sum_nonneg fun _ _ => norm_nonneg _)] at hn
  exact lt_of_le_of_lt (V03.finite_coordinate_opNorm_bound (D n) e hexp) hn

end FiniteCompression

end WeilDefect.MasterRecon.V05

#print axioms WeilDefect.MasterRecon.V05.gram_scaled_resolvent_sequence
#print axioms WeilDefect.MasterRecon.V05.picard_operator_isUnit
#print axioms WeilDefect.MasterRecon.V05.picard_compression_apply

#print axioms WeilDefect.MasterRecon.V05.finite_selected_norm_limit
