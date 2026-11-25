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
    (synthesis P M)† z = WithLp.toLp 2 (P† z, M† z) := by
  apply ext_inner_right ℂ
  intro w
  rw [ContinuousLinearMap.adjoint_inner_left, synthesis_apply,
    inner_add_right, WithLp.prod_inner_apply]
  simp only [WithLp.ofLp_toLp]
  rw [P.adjoint_inner_left, M.adjoint_inner_left]

theorem extraction_adjoint_apply (u : K) :
    (extraction (H := H) (K := K))† u = WithLp.toLp 2 ((0 : H), u) := by
  apply ext_inner_right ℂ
  intro w
  rw [ContinuousLinearMap.adjoint_inner_left, WithLp.prod_inner_apply]
  simp [extraction]

theorem canonical_block_laws (P : H →L[ℂ] X) (M : K →L[ℂ] X) :
    (∀ z, synthesis P M ((synthesis P M)† z) = P (P† z) + M (M† z)) ∧
    (∀ u, synthesis P M ((extraction (H := H) (K := K))† u) = M u) ∧
    (∀ z, extraction ((synthesis P M)† z) = M† z) ∧
    (∀ u, extraction ((extraction (H := H) (K := K))† u) = u) := by
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
  refine ⟨fun i => ⟪e i, x⟫_ℂ, (e.sum_repr' x).symm, ?_⟩
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
      (∀ n x, R n (((synthesis P M)† ∘L synthesis P M) x +
        ((η n : ℝ) : ℂ) • x) = x) ∧
      (∀ n x, ((synthesis P M)† ∘L synthesis P M) (R n x) +
        ((η n : ℝ) : ℂ) • R n x = x) ∧
      Tendsto (fun n => ‖extraction ∘L (((η n : ℝ) : ℂ) • R n) ∘L
          (extraction (H := H) (K := K))† -
        extraction ∘L (synthesis P M).ker.starProjection ∘L
          (extraction (H := H) (K := K))†‖) atTop (𝓝 0) := by
  obtain ⟨R, hl, hr, ht⟩ := V05.gram_scaled_resolvent_sequence
    (synthesis P M) η hη hη0
  refine ⟨R, hl, hr, ?_⟩
  apply finite_dimensional_selected_norm_limit
  intro u
  have hc := extraction.continuous.continuousAt.tendsto.comp
    (ht ((extraction (H := H) (K := K))† u))
  have hd := hc.sub (tendsto_const_nhds (x :=
    extraction ((synthesis P M).ker.starProjection
      ((extraction (H := H) (K := K))† u))))
  simpa using hd

end WeilDefect.MasterRecon.V05B

#print axioms WeilDefect.MasterRecon.V05B.synthesis_apply
#print axioms WeilDefect.MasterRecon.V05B.synthesis_adjoint_apply
#print axioms WeilDefect.MasterRecon.V05B.extraction_adjoint_apply
#print axioms WeilDefect.MasterRecon.V05B.canonical_block_laws
#print axioms WeilDefect.MasterRecon.V05B.orthonormal_coordinates
#print axioms WeilDefect.MasterRecon.V05B.finite_dimensional_selected_norm_limit
#print axioms WeilDefect.MasterRecon.V05B.canonical_gram_compression_limit
