import WeilDefect.MasterRecon.V04
import Mathlib.Analysis.Analytic.Constructions
import Mathlib.Analysis.Normed.Algebra.Exponential

/-! V06A: norm-analytic positive-form family and analytic inversion.
No arithmetic phase-cancellation or physical translation premise is hidden
in this abstract operator gate. -/
namespace WeilDefect.MasterRecon.V06A

open Filter Set
open scoped Topology InnerProduct

variable {H K : Type*}
variable [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup K] [InnerProductSpace ℂ K] [CompleteSpace K]

noncomputable def translatedBlock (D E : K →L[ℂ] K) (z : ℂ) :
    K →L[ℂ] K :=
  NormedSpace.exp ((-z) • D) * E * NormedSpace.exp ((-z) • D)

theorem translatedBlock_analytic (D E : K →L[ℂ] K) :
    AnalyticOnNhd ℂ (translatedBlock D E) Set.univ := by
  intro z _
  have hs : AnalyticAt ℂ (fun w : ℂ => (-w) • D) z :=
    (analyticAt_id.neg.smul analyticAt_const)
  have hx : AnalyticAt ℂ (fun w : ℂ => NormedSpace.exp ((-w) • D)) z :=
    (NormedSpace.exp_analytic (𝕂 := ℂ) ((-z) • D)).comp hs
  exact (hx.mul analyticAt_const).mul hx

noncomputable def translatedForm (A : H →L[ℂ] K)
    (D E : K →L[ℂ] K) (z : ℂ) : H →L[ℂ] H :=
  A.adjoint ∘L translatedBlock D E z ∘L A

theorem translatedForm_analytic (A : H →L[ℂ] K) (D E : K →L[ℂ] K) :
    AnalyticOnNhd ℂ (translatedForm A D E) Set.univ := by
  intro z _
  have hb := translatedBlock_analytic D E z (Set.mem_univ z)
  let L : (K →L[ℂ] K) →L[ℂ] (H →L[ℂ] K) :=
    (ContinuousLinearMap.compL ℂ H K K).flip A
  let R : (H →L[ℂ] K) →L[ℂ] (H →L[ℂ] H) :=
    ContinuousLinearMap.compL ℂ H K H A.adjoint
  have h := (R.analyticAt (L (translatedBlock D E z))).comp
    ((L.analyticAt (translatedBlock D E z)).comp hb)
  exact h

theorem translatedForm_zero (A : H →L[ℂ] K) (D E : K →L[ℂ] K) :
    translatedForm A D E 0 = A.adjoint ∘L E ∘L A := by
  simp [translatedForm, translatedBlock, NormedSpace.exp_zero]

/-- Any norm-analytic operator family invertible at zero has an actual
analytic two-sided inverse on a positive-radius complex disk. -/
theorem local_analytic_inverse (P : ℂ → H →L[ℂ] H)
    (hp : AnalyticOnNhd ℂ P Set.univ) (h0 : IsUnit (P 0)) :
    ∃ r : ℝ, 0 < r ∧
      AnalyticOnNhd ℂ (fun z => Ring.inverse (P z)) (Metric.ball 0 r) ∧
      (∀ z ∈ Metric.ball 0 r, Ring.inverse (P z) * P z = 1) ∧
      (∀ z ∈ Metric.ball 0 r, P z * Ring.inverse (P z) = 1) := by
  have hc := (hp 0 (Set.mem_univ 0)).continuousAt
  have he : {z : ℂ | IsUnit (P z)} ∈ 𝓝 (0 : ℂ) :=
    hc.preimage_mem_nhds (Units.isOpen.mem_nhds h0)
  obtain ⟨r, hr, hsub⟩ := Metric.mem_nhds_iff.mp he
  have hu : ∀ z ∈ Metric.ball (0 : ℂ) r, IsUnit (P z) :=
    fun z hz => hsub hz
  refine ⟨r, hr, ?_, ?_, ?_⟩
  · intro z hz
    obtain ⟨u, hu'⟩ := hu z hz
    have hi : AnalyticAt ℂ Ring.inverse (P z) := by
      rw [← hu']
      exact analyticAt_inverse (𝕜 := ℂ) u
    exact hi.comp (hp z (Set.mem_univ z))
  · intro z hz
    exact Ring.inverse_mul_cancel (P z) (hu z hz)
  · intro z hz
    exact Ring.mul_inverse_cancel (P z) (hu z hz)

/-- Coercivity of the untranslated positive form supplies the initial
unit. The complex extension is not formed using a complex adjoint. -/
theorem coercive_translated_inverse (A : H →L[ℂ] K) (D E : K →L[ℂ] K)
    (b : ℝ≥0) (hb : 0 < b)
    (hco : ∀ x : H, ‖x‖ ^ 2 * (b : ℝ) ≤
      (inner ℂ ((A.adjoint ∘L E ∘L A) x) x).re) :
    ∃ r : ℝ, 0 < r ∧
      AnalyticOnNhd ℂ (fun z => Ring.inverse (translatedForm A D E z))
        (Metric.ball 0 r) ∧
      (∀ z ∈ Metric.ball 0 r,
        Ring.inverse (translatedForm A D E z) * translatedForm A D E z = 1) ∧
      (∀ z ∈ Metric.ball 0 r,
        translatedForm A D E z * Ring.inverse (translatedForm A D E z) = 1) := by
  apply local_analytic_inverse _ (translatedForm_analytic A D E)
  rw [translatedForm_zero]
  apply ContinuousLinearMap.isUnit_of_forall_le_norm_inner_map _ hb
  intro x
  exact (hco x).trans (Complex.re_le_norm _)

end WeilDefect.MasterRecon.V06A

#print axioms WeilDefect.MasterRecon.V06A.translatedBlock_analytic
#print axioms WeilDefect.MasterRecon.V06A.translatedForm_analytic
#print axioms WeilDefect.MasterRecon.V06A.translatedForm_zero
#print axioms WeilDefect.MasterRecon.V06A.local_analytic_inverse
#print axioms WeilDefect.MasterRecon.V06A.coercive_translated_inverse
