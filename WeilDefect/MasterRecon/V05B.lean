import WeilDefect.MasterRecon.V05
import Mathlib.Analysis.InnerProductSpace.ProdL2
import Mathlib.Analysis.InnerProductSpace.PiL2

/-! V05B: instantiate the typed block identities on the genuine
Hilbert L2 direct sum, and remove the finite-coordinate hypothesis. -/
namespace WeilDefect.MasterRecon.V05B

open Filter
open scoped InnerProduct NNReal Topology BigOperators

variable {H X K : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup X] [InnerProductSpace ℂ X] [CompleteSpace X]
variable [NormedAddCommGroup K] [InnerProductSpace ℂ K] [CompleteSpace K]

noncomputable def synthesis (P : H →L[ℂ] X) (M : K →L[ℂ] X) :
    WithLp 2 (H × K) →L[ℂ] X :=
  P ∘L WithLp.fstL 2 ℂ H K + M ∘L WithLp.sndL 2 ℂ H K

noncomputable def extraction : WithLp 2 (H × K) →L[ℂ] K :=
  WithLp.sndL 2 ℂ H K

theorem synthesis_apply (P : H →L[ℂ] X) (M : K →L[ℂ] X)
    (w : WithLp 2 (H × K)) :
    synthesis P M w = P w.fst + M w.snd := rfl

theorem synthesis_adjoint_apply (P : H →L[ℂ] X) (M : K →L[ℂ] X) (z : X) :
    (synthesis P M).adjoint z = WithLp.toLp 2 ((P.adjoint) z, (M.adjoint) z) := by
  apply ext_inner_right ℂ
  intro w
  rw [ContinuousLinearMap.adjoint_inner_left, synthesis_apply,
    inner_add_right, WithLp.prod_inner_apply]
  simp only [WithLp.ofLp_toLp]
  rw [P.adjoint_inner_left, M.adjoint_inner_left]

theorem extraction_adjoint_apply (u : K) :
    (extraction (H := H) (K := K)).adjoint u = WithLp.toLp 2 ((0 : H), u) := by
  apply ext_inner_right ℂ
  intro w
  rw [ContinuousLinearMap.adjoint_inner_left, WithLp.prod_inner_apply]
  simp [extraction]

theorem canonical_block_laws (P : H →L[ℂ] X) (M : K →L[ℂ] X) :
    (∀ z, synthesis P M ((synthesis P M).adjoint z) = P ((P.adjoint) z) + M ((M.adjoint) z)) ∧
    (∀ u, synthesis P M ((extraction (H := H) (K := K)).adjoint u) = M u) ∧
    (∀ z, extraction ((synthesis P M).adjoint z) = (M.adjoint) z) ∧
    (∀ u, extraction ((extraction (H := H) (K := K)).adjoint u) = u) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro z
    rw [synthesis_adjoint_apply, synthesis_apply]
    rfl
  · intro u
    rw [extraction_adjoint_apply, synthesis_apply]
    simp
  · intro z
    rw [synthesis_adjoint_apply]
    rfl
  · intro u
    rw [extraction_adjoint_apply]
    rfl

theorem orthonormal_coordinates {ι : Type*} [Fintype ι]
    (e : OrthonormalBasis ι ℂ K) (x : K) :
    ∃ a : ι → ℂ, x = ∑ i, a i • e i ∧ ∀ i, ‖a i‖ ≤ ‖x‖ := by
  refine ⟨fun i => inner ℂ (e i) x, (e.sum_repr' x).symm, ?_⟩
  intro i
  simpa using (norm_inner_le_norm (𝕜 := ℂ) (e i) x)

theorem finite_dimensional_selected_norm_limit [FiniteDimensional ℂ K]
    (D : ℕ → K →L[ℂ] K)
    (hpoint : ∀ x, Tendsto (fun n => D n x) atTop (𝓝 0)) :
    Tendsto (fun n => ‖D n‖) atTop (𝓝 0) := by
  let e := stdOrthonormalBasis ℂ K
  exact V05.finite_selected_norm_limit D e (orthonormal_coordinates e) hpoint

/-- Sequential norm convergence of the actual selected compression,
without any finite-dimensional assumption on the coefficient background. -/
theorem canonical_gram_compression_limit [FiniteDimensional ℂ K]
    (P : H →L[ℂ] X) (M : K →L[ℂ] X) (η : ℕ → ℝ≥0)
    (hη : ∀ n, 0 < η n)
    (hη0 : Tendsto (fun n => (η n : ℝ)) atTop (𝓝 0)) :
    ∃ R : ℕ → WithLp 2 (H × K) →L[ℂ] WithLp 2 (H × K),
      (∀ n x, R n (((synthesis P M).adjoint ∘L synthesis P M) x +
        ((η n : ℝ) : ℂ) • x) = x) ∧
      (∀ n x, ((synthesis P M).adjoint ∘L synthesis P M) (R n x) +
        ((η n : ℝ) : ℂ) • R n x = x) ∧
      Tendsto (fun n => ‖extraction ∘L (((η n : ℝ) : ℂ) • R n) ∘L
          (extraction (H := H) (K := K)).adjoint -
        extraction ∘L (synthesis P M).ker.starProjection ∘L
          (extraction (H := H) (K := K)).adjoint‖) atTop (𝓝 0) := by
  obtain ⟨R, hl, hr, ht⟩ := V05.gram_scaled_resolvent_sequence
    (synthesis P M) η hη hη0
  refine ⟨R, hl, hr, ?_⟩
  apply finite_dimensional_selected_norm_limit
  intro u
  have hc := (extraction (H := H) (K := K)).continuous.continuousAt.tendsto.comp
    (ht ((extraction (H := H) (K := K)).adjoint u))
  have hd := hc.sub (tendsto_const_nhds (x :=
    extraction ((synthesis P M).ker.starProjection
      ((extraction (H := H) (K := K)).adjoint u))))
  simpa using hd


/-- Actual Picard inverse sequence on the canonical Hilbert sum.
Both inverses are specified by their two-sided equations. The limiting
gap is the kernel projection of the actual joint synthesis. -/
theorem canonical_picard_norm_limit [FiniteDimensional ℂ K]
    (P : H →L[ℂ] X) (M : K →L[ℂ] X) (η : ℕ → ℝ≥0)
    (hη : ∀ n, 0 < η n)
    (hη0 : Tendsto (fun n => (η n : ℝ)) atTop (𝓝 0)) :
    ∃ R : ℕ → X →L[ℂ] X, ∃ C : ℕ → K →L[ℂ] K,
      (∀ n z, R n (P ((P.adjoint) z) + ((η n : ℝ) : ℂ) • z) = z) ∧
      (∀ n z, P ((P.adjoint) (R n z)) + ((η n : ℝ) : ℂ) • R n z = z) ∧
      (∀ n u, C n (u + (M.adjoint) (R n (M u))) = u) ∧
      (∀ n u, C n u + (M.adjoint) (R n (M (C n u))) = u) ∧
      Tendsto (fun n => ‖C n -
        extraction ∘L (synthesis P M).ker.starProjection ∘L
          (extraction (H := H) (K := K)).adjoint‖) atTop (𝓝 0) := by
  let S := synthesis P M
  let ell : WithLp 2 (H × K) →L[ℂ] K := extraction
  obtain ⟨hSS, hi, he, hei⟩ := canonical_block_laws P M
  obtain ⟨B, hBl, hBr, hlim⟩ := canonical_gram_compression_limit P M η hη hη0
  have hRex := fun n => V04.positive_shift_inverse (P ∘L (P.adjoint))
    (ContinuousLinearMap.isPositive_self_comp_adjoint P) (η n) (hη n)
  choose R hR using hRex
  have hTex := fun n => V04.positive_shift_inverse (S ∘L (S.adjoint))
    (ContinuousLinearMap.isPositive_self_comp_adjoint S) (η n) (hη n)
  choose T hT using hTex
  have hU : ∀ n, IsUnit (1 + (M.adjoint) ∘L R n ∘L M) :=
    fun n => V05.picard_operator_isUnit P M (R n) (η n) (hR n).2.1
  choose U hUeq using hU
  let C : ℕ → K →L[ℂ] K := fun n => ↑((U n)⁻¹)
  have hCl : ∀ n u, C n (u + (M.adjoint) (R n (M u))) = u := by
    intro n u
    have hh := congrArg (fun f : K →L[ℂ] K => f u) (U n).inv_mul
    change C n ((↑(U n) : K →L[ℂ] K) u) = u at hh
    rw [hUeq n] at hh
    simpa using hh
  have hCr : ∀ n u, C n u + (M.adjoint) (R n (M (C n u))) = u := by
    intro n u
    have hh := congrArg (fun f : K →L[ℂ] K => f u) (U n).mul_inv
    change (↑(U n) : K →L[ℂ] K) (C n u) = u at hh
    rw [hUeq n] at hh
    simpa using hh
  have hEq : ∀ n, C n = ell ∘L (((η n : ℝ) : ℂ) • B n) ∘L (ell.adjoint) := by
    intro n
    ext u
    exact V05.picard_compression_apply P M S (ell.adjoint) ell
      (P ∘L (P.adjoint) + ((η n : ℝ) : ℂ) • 1) (R n) (T n) (C n) (B n)
      ((η n : ℝ) : ℂ) (fun _ => rfl) (hR n).1 hSS (hT n).2.1
      (hBl n) (hCl n) hi he hei u
  refine ⟨R, C, fun n => (hR n).1, fun n => (hR n).2.1, hCl, hCr, ?_⟩
  have hfun : (fun n => ‖C n - ell ∘L S.ker.starProjection ∘L (ell.adjoint)‖) =
      (fun n => ‖ell ∘L (((η n : ℝ) : ℂ) • B n) ∘L (ell.adjoint) -
        ell ∘L S.ker.starProjection ∘L (ell.adjoint)‖) := by
    funext n
    rw [hEq n]
  change Tendsto (fun n => ‖C n - ell ∘L S.ker.starProjection ∘L (ell.adjoint)‖)
    atTop (𝓝 0)
  rw [hfun]
  exact hlim

end WeilDefect.MasterRecon.V05B

#print axioms WeilDefect.MasterRecon.V05B.synthesis_apply
#print axioms WeilDefect.MasterRecon.V05B.synthesis_adjoint_apply
#print axioms WeilDefect.MasterRecon.V05B.extraction_adjoint_apply
#print axioms WeilDefect.MasterRecon.V05B.canonical_block_laws
#print axioms WeilDefect.MasterRecon.V05B.orthonormal_coordinates
#print axioms WeilDefect.MasterRecon.V05B.finite_dimensional_selected_norm_limit
#print axioms WeilDefect.MasterRecon.V05B.canonical_gram_compression_limit

#print axioms WeilDefect.MasterRecon.V05B.canonical_picard_norm_limit
