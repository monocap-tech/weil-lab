import WeilDefect.MasterRecon.V10B12b
import Mathlib.LinearAlgebra.Basis.Defs

/-! V10B12c: finite matrix custody for the corrected retained basis.
The residual bank contains FULL projected tail residuals, not only
their coordinates on the trial-solve subspace. -/
namespace WeilDefect.MasterRecon.V10B12c

open scoped InnerProduct BigOperators ComplexConjugate
open V10B12a (energy)

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
variable {ι : Type*} [Fintype ι]

noncomputable def synth (v : ι → H) (a : ι → ℂ) : H :=
  ∑ i, a i • v i

noncomputable def gram (G : H →L[ℂ] H) (v : ι → H) (i j : ι) : ℂ :=
  inner ℂ (G (v i)) (v j)

noncomputable def matrixForm (M : ι → ι → ℂ) (a : ι → ℂ) : ℂ :=
  ∑ i, ∑ j, conj (a i)*(a j*M i j)

theorem matrixForm_gram (G : H →L[ℂ] H) (v : ι → H) (a : ι → ℂ) :
    matrixForm (gram G v) a = inner ℂ (G (synth v a)) (synth v a) := by
  unfold matrixForm gram synth
  simp only [map_sum,map_smul,sum_inner,inner_sum,inner_smul_left,inner_smul_right,
    Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro j _
  apply Finset.sum_congr rfl
  intro i _
  ring

theorem synth_basis (S : Submodule ℂ H) (b : Module.Basis ι ℂ S) (x : S) :
    synth (fun i => (b i:H)) (fun i => b.repr x i) = (x:H) := by
  unfold synth
  change (∑ i, b.repr x i • S.subtype (b i)) = S.subtype x
  simpa only [map_sum,map_smul] using congrArg (fun y : S => S.subtype y) (b.sum_repr x)

variable (S : Submodule ℂ H) [S.HasOrthogonalProjection]

noncomputable def corrected (b : Module.Basis ι ℂ S) (Z : S →L[ℂ] Sᗮ) (i : ι) : H :=
  (b i:H)-(Z (b i):H)

noncomputable def residualBank (G : H →L[ℂ] H)
    (b : Module.Basis ι ℂ S) (Z : S →L[ℂ] Sᗮ) (i : ι) : H :=
  Sᗮ.starProjection (G (corrected S b Z i))

theorem synth_corrected (b : Module.Basis ι ℂ S) (Z : S →L[ℂ] Sᗮ) (x : S) :
    synth (corrected S b Z) (fun i => b.repr x i) = (x:H)-(Z x:H) := by
  let L : S →L[ℂ] H := S.subtypeL-Sᗮ.subtypeL.comp Z
  have he : ∀ i, corrected S b Z i = L (b i) := fun _ => rfl
  unfold synth
  simp only [he,← map_smul,← map_sum,b.sum_repr]
  rfl

theorem synth_residual (G : H →L[ℂ] H) (b : Module.Basis ι ℂ S)
    (Z : S →L[ℂ] Sᗮ) (x : S) :
    synth (residualBank S G b Z) (fun i => b.repr x i) =
      Sᗮ.starProjection (G ((x:H)-(Z x:H))) := by
  let L := Sᗮ.starProjection.comp G
  have he : ∀ i, residualBank S G b Z i = L (corrected S b Z i) := fun _ => rfl
  unfold synth
  simp only [he,← map_smul,← map_sum]
  change L (synth (corrected S b Z) (fun i => b.repr x i)) = _
  rw [synth_corrected]
  rfl

noncomputable def lowerMatrix (G : H →L[ℂ] H) (c : ℝ)
    (b : Module.Basis ι ℂ S) (Z : S →L[ℂ] Sᗮ) (i j : ι) : ℂ :=
  gram G (corrected S b Z) i j -
    (c:ℂ)⁻¹ * gram (1:H →L[ℂ] H) (residualBank S G b Z) i j

theorem matrixForm_sub_scaled (M N : ι → ι → ℂ) (q : ℂ) (a : ι → ℂ) :
    matrixForm (fun i j => M i j-q*N i j) a =
      matrixForm M a-q*matrixForm N a := by
  unfold matrixForm
  simp only [mul_sub,Finset.sum_sub_distrib,Finset.mul_sum]
  congr 1
  apply Finset.sum_congr rfl
  intro i _
  apply Finset.sum_congr rfl
  intro j _
  ring

theorem lowerMatrix_exact (G : H →L[ℂ] H) (c : ℝ) (b : Module.Basis ι ℂ S)
    (Z : S →L[ℂ] Sᗮ) (x : S) :
    (matrixForm (lowerMatrix S G c b Z) (fun i => b.repr x i)).re =
      energy G ((x:H)-(Z x:H)) -
        ‖Sᗮ.starProjection (G ((x:H)-(Z x:H)))‖^2/c := by
  unfold lowerMatrix
  rw [matrixForm_sub_scaled,matrixForm_gram,matrixForm_gram,synth_corrected,synth_residual,
    ContinuousLinearMap.one_apply,inner_self_eq_norm_sq_to_K,Complex.sub_re]
  simp only [energy,← Complex.ofReal_inv,Complex.mul_re,Complex.ofReal_re,Complex.ofReal_im,Complex.ofReal_pow,mul_zero,sub_zero]
  ring

theorem matrix_certificate (G : H →L[ℂ] H)
    (hG : ∀ x y, inner ℂ (G x) y = inner ℂ x (G y))
    (c : ℝ) (hc : 0 < c)
    (htail : ∀ y ∈ Sᗮ, c*‖y‖^2 ≤ energy G y)
    (b : Module.Basis ι ℂ S) (Z : S →L[ℂ] Sᗮ)
    (hM : ∀ a : ι → ℂ, 0 ≤ (matrixForm (lowerMatrix S G c b Z) a).re) :
    ∀ g : H, 0 ≤ energy G g := by
  apply V10B12b.trial_certificate G hG S c hc htail Z
  intro x
  have h := hM (fun i => b.repr x i)
  rw [lowerMatrix_exact] at h
  linarith

end WeilDefect.MasterRecon.V10B12c

#print axioms WeilDefect.MasterRecon.V10B12c.matrixForm_gram
#print axioms WeilDefect.MasterRecon.V10B12c.synth_basis
#print axioms WeilDefect.MasterRecon.V10B12c.synth_corrected
#print axioms WeilDefect.MasterRecon.V10B12c.synth_residual
#print axioms WeilDefect.MasterRecon.V10B12c.matrixForm_sub_scaled
#print axioms WeilDefect.MasterRecon.V10B12c.lowerMatrix_exact
#print axioms WeilDefect.MasterRecon.V10B12c.matrix_certificate
