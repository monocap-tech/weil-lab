import WeilDefect.MasterRecon.V07C
import Mathlib.Analysis.SpecialFunctions.Exponential

/-! V07D: exponential covariance on the full Hilbert direct sum.
Continuous evaluation commutes with the convergent operator exponential
series. The two scalar eigenchannels recover the original hyperbolic mix. -/
namespace WeilDefect.MasterRecon.V07D

open scoped ENNReal InnerProduct Nat
open V07C

section Intertwine
variable {H K : Type*}
variable [NormedAddCommGroup H] [NormedSpace ℂ H] [CompleteSpace H]
variable [NormedAddCommGroup K] [NormedSpace ℂ K] [CompleteSpace K]

theorem power_intertwine (L : H →L[ℂ] K) (D : H →L[ℂ] H)
    (B : K →L[ℂ] K) (h : ∀ x, L (D x) = B (L x))
    (n : ℕ) (x : H) :
    L ((D ^ n) x) = (B ^ n) (L x) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ', pow_succ']
    change L (D ((D ^ n) x)) = B ((B ^ n) (L x))
    rw [h, ih]

theorem exp_intertwine (L : H →L[ℂ] K) (D : H →L[ℂ] H)
    (B : K →L[ℂ] K) (h : ∀ x, L (D x) = B (L x)) (x : H) :
    L (NormedSpace.exp D x) = NormedSpace.exp B (L x) := by
  let F : (H →L[ℂ] H) →L[ℂ] K := L.comp (ContinuousLinearMap.apply ℂ H x)
  let G : (K →L[ℂ] K) →L[ℂ] K := ContinuousLinearMap.apply ℂ K (L x)
  change F (NormedSpace.exp D) = G (NormedSpace.exp B)
  simp only [NormedSpace.exp_eq_tsum ℂ]
  rw [F.map_tsum (NormedSpace.expSeries_summable' (𝕂 := ℂ) D),
    G.map_tsum (NormedSpace.expSeries_summable' (𝕂 := ℂ) B)]
  apply tsum_congr
  intro n
  rw [F.map_smul, G.map_smul]
  change (n !⁻¹ : ℂ) • L ((D ^ n) x) = (n !⁻¹ : ℂ) • (B ^ n) (L x)
  rw [power_intertwine L D B h]

end Intertwine

theorem global_exp_coordinate {ι : Type*} (d : ι → ℝ)
    (hd : ∀ i, |d i| ≤ 1 / 2) (z : ℂ) (x : Coeff ι) (i : ι) :
    NormedSpace.exp (z • displacement d hd) x i =
      NormedSpace.exp (z • displacementBlock (d i)) (x i) := by
  let L : Coeff ι →L[ℂ] Pair := lp.evalCLM ℂ (fun _ : ι => Pair) 2 i
  have h : ∀ y : Coeff ι, L ((z • displacement d hd) y) =
      (z • displacementBlock (d i)) (L y) := by
    intro y
    change z • displacement d hd y i = z • displacementBlock (d i) (y i)
    rw [displacement_apply]
  exact exp_intertwine L _ _ h x

noncomputable def sumChannel : Pair →L[ℂ] ℂ :=
  WithLp.fstL 2 ℂ ℂ ℂ + WithLp.sndL 2 ℂ ℂ ℂ

noncomputable def diffChannel : Pair →L[ℂ] ℂ :=
  WithLp.fstL 2 ℂ ℂ ℂ - WithLp.sndL 2 ℂ ℂ ℂ

theorem scalar_exp_apply (w u : ℂ) :
    NormedSpace.exp (w • (1 : ℂ →L[ℂ] ℂ)) u = Complex.exp w * u := by
  have h := NormedSpace.algebraMap_exp_comm (𝕂 := ℂ) (𝔸 := ℂ →L[ℂ] ℂ) w
  rw [Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one] at h
  rw [← h, ← Complex.exp_eq_exp_ℂ]
  rfl

theorem local_exp_sum (d : ℝ) (z : ℂ) (x : Pair) :
    sumChannel (NormedSpace.exp (z • displacementBlock d) x) =
      Complex.exp (z * (d : ℂ)) * sumChannel x := by
  have h : ∀ y : Pair, sumChannel ((z • displacementBlock d) y) =
      ((z * (d : ℂ)) • (1 : ℂ →L[ℂ] ℂ)) (sumChannel y) := by
    intro y
    change z * ((d : ℂ) * (WithLp.ofLp y).2) +
      z * ((d : ℂ) * (WithLp.ofLp y).1) =
        (z * (d : ℂ)) * ((WithLp.ofLp y).1 + (WithLp.ofLp y).2)
    ring
  rw [exp_intertwine sumChannel _ _ h, scalar_exp_apply]

theorem local_exp_diff (d : ℝ) (z : ℂ) (x : Pair) :
    diffChannel (NormedSpace.exp (z • displacementBlock d) x) =
      Complex.exp (-(z * (d : ℂ))) * diffChannel x := by
  have h : ∀ y : Pair, diffChannel ((z • displacementBlock d) y) =
      (-(z * (d : ℂ)) • (1 : ℂ →L[ℂ] ℂ)) (diffChannel y) := by
    intro y
    change z * ((d : ℂ) * (WithLp.ofLp y).2) -
      z * ((d : ℂ) * (WithLp.ofLp y).1) =
        (-(z * (d : ℂ))) * ((WithLp.ofLp y).1 - (WithLp.ofLp y).2)
    ring
  rw [exp_intertwine diffChannel _ _ h, scalar_exp_apply]

theorem local_exp_mix (d : ℝ) (z : ℂ) (x : Pair) :
    NormedSpace.exp (z • displacementBlock d) x =
      WithLp.toLp 2
        (V07A.evenMix (z * (d : ℂ)) * (WithLp.ofLp x).1 +
           V07A.oddMix (z * (d : ℂ)) * (WithLp.ofLp x).2,
         V07A.oddMix (z * (d : ℂ)) * (WithLp.ofLp x).1 +
           V07A.evenMix (z * (d : ℂ)) * (WithLp.ofLp x).2) := by
  let y := NormedSpace.exp (z • displacementBlock d) x
  have hp := local_exp_sum d z x
  have hm := local_exp_diff d z x
  change (WithLp.ofLp y).1 + (WithLp.ofLp y).2 =
    Complex.exp (z * (d : ℂ)) * ((WithLp.ofLp x).1 + (WithLp.ofLp x).2) at hp
  change (WithLp.ofLp y).1 - (WithLp.ofLp y).2 =
    Complex.exp (-(z * (d : ℂ))) * ((WithLp.ofLp x).1 - (WithLp.ofLp x).2) at hm
  apply WithLp.ofLp_injective
  apply Prod.ext
  · change (WithLp.ofLp y).1 = _
    unfold V07A.evenMix V07A.oddMix
    linear_combination (hp + hm) / 2
  · change (WithLp.ofLp y).2 = _
    unfold V07A.evenMix V07A.oddMix
    linear_combination (hp - hm) / 2

theorem global_exp_mix {ι : Type*} (d : ι → ℝ)
    (hd : ∀ i, |d i| ≤ 1 / 2) (z : ℂ) (x : Coeff ι) (i : ι) :
    NormedSpace.exp (z • displacement d hd) x i =
      WithLp.toLp 2
        (V07A.evenMix (z * (d i : ℂ)) * (WithLp.ofLp (x i)).1 +
           V07A.oddMix (z * (d i : ℂ)) * (WithLp.ofLp (x i)).2,
         V07A.oddMix (z * (d i : ℂ)) * (WithLp.ofLp (x i)).1 +
           V07A.evenMix (z * (d i : ℂ)) * (WithLp.ofLp (x i)).2) := by
  rw [global_exp_coordinate, local_exp_mix]

end WeilDefect.MasterRecon.V07D

#print axioms WeilDefect.MasterRecon.V07D.power_intertwine
#print axioms WeilDefect.MasterRecon.V07D.exp_intertwine
#print axioms WeilDefect.MasterRecon.V07D.global_exp_coordinate
#print axioms WeilDefect.MasterRecon.V07D.scalar_exp_apply
#print axioms WeilDefect.MasterRecon.V07D.local_exp_sum
#print axioms WeilDefect.MasterRecon.V07D.local_exp_diff
#print axioms WeilDefect.MasterRecon.V07D.local_exp_mix
#print axioms WeilDefect.MasterRecon.V07D.global_exp_mix
