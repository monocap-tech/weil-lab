import WeilDefect.MasterRecon.V08K
import WeilDefect.MasterRecon.V10B8a
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt

/-! V10B8d: finite prime-power operator. Its summation range follows
from support of the autocorrelation, not from a numerical truncation.
Translation is defined on equivalence classes by measure preservation. -/
namespace WeilDefect.MasterRecon.V10B8d

open MeasureTheory Set Complex
open scoped InnerProduct ComplexConjugate BigOperators Convolution
open V08I (FullL2 logCarrier physicalInclusion)

noncomputable def shift (a : ℝ) : FullL2 →L[ℂ] FullL2 :=
  (Lp.compMeasurePreservingₗᵢ ℂ (fun x : ℝ => x+a)
    (measurePreserving_add_right (volume : Measure ℝ) a)).toContinuousLinearMap

theorem shift_ae (a : ℝ) (f : FullL2) :
    (shift a f : ℝ → ℂ) =ᵐ[volume] fun x => f (x+a) :=
  Lp.coeFn_compMeasurePreserving f (measurePreserving_add_right volume a)

theorem shift_norm (a : ℝ) (f : FullL2) : ‖shift a f‖ = ‖f‖ :=
  Lp.norm_compMeasurePreserving f (measurePreserving_add_right volume a)

theorem shift_inverse (a : ℝ) (f : FullL2) :
    shift (-a) (shift a f) = f := by
  apply Lp.ext
  have h := V06D.ae_translate (shift_ae a f) (-a)
  filter_upwards [shift_ae (-a) (shift a f),h] with x hx hy
  change shift (-a) (shift a f) x = f x
  rw [hx,hy,show x + -a + a = x by ring]

theorem shift_adjoint (a : ℝ) : (shift a).adjoint = shift (-a) := by
  have h := (ContinuousLinearMap.norm_map_iff_adjoint_comp_self (shift a)).mp (shift_norm a)
  have hi : (shift a) ∘L (shift (-a)) = 1 := by
    ext f : 1
    simpa only [ContinuousLinearMap.comp_apply,ContinuousLinearMap.one_apply,neg_neg]
      using shift_inverse (-a) f
  calc
    (shift a).adjoint = (shift a).adjoint ∘L ((shift a) ∘L shift (-a)) := by rw [hi]; simp
    _ = ((shift a).adjoint ∘L shift a) ∘L shift (-a) := by
      ext f : 1
      rfl
    _ = shift (-a) := by rw [h]; simp

noncomputable def shiftPair (a : ℝ) : FullL2 →L[ℂ] FullL2 :=
  shift a + shift (-a)

theorem shiftPair_selfAdjoint (a : ℝ) : (shiftPair a).adjoint = shiftPair a := by
  unfold shiftPair
  simp [shift_adjoint,add_comm]

theorem shiftPair_norm (a : ℝ) (f : FullL2) : ‖shiftPair a f‖ ≤ 2*‖f‖ := by
  unfold shiftPair
  rw [ContinuousLinearMap.add_apply]
  calc
    _ ≤ ‖shift a f‖ + ‖shift (-a) f‖ := norm_add_le _ _
    _ = _ := by rw [shift_norm,shift_norm]; ring

noncomputable def primeWeight (n : ℕ) : ℝ :=
  ArithmeticFunction.vonMangoldt n / Real.sqrt n

noncomputable def primeBank (t : ℝ) : Finset ℕ :=
  Finset.Ioc 0 ⌊Real.exp (2*t)⌋₊

noncomputable def physicalPrime (t : ℝ) : FullL2 →L[ℂ] FullL2 :=
  ∑ n ∈ primeBank t, (primeWeight n:ℂ) • shiftPair (Real.log n)

noncomputable def primeOperator (t : ℝ) : logCarrier t →L[ℂ] logCarrier t :=
  (physicalInclusion t).adjoint ∘L (physicalPrime t) ∘L (physicalInclusion t)

theorem prime_compact (t : ℝ) (ht : 0 ≤ t) : IsCompactOperator (primeOperator t) :=
  (V08K.physicalInclusion_compact t ht).clm_comp
    ((physicalInclusion t).adjoint ∘L physicalPrime t)

theorem prime_selfAdjoint (t : ℝ) :
    (primeOperator t).adjoint = primeOperator t := by
  have h : (physicalPrime t).adjoint = physicalPrime t := by
    unfold physicalPrime
    classical
    induction primeBank t using Finset.induction_on with
    | empty => simp
    | @insert n S hn ih =>
      simp [Finset.sum_insert hn,ih,shiftPair_selfAdjoint,Complex.conj_ofReal]
  unfold primeOperator
  rw [ContinuousLinearMap.adjoint_comp,ContinuousLinearMap.adjoint_comp,
    ContinuousLinearMap.adjoint_adjoint,h]
  ext f : 1
  rfl

theorem shift_autocorr (a : ℝ) (u : FullL2) (f : ℝ → ℂ)
    (hae : (u : ℝ → ℂ) =ᵐ[volume] f) :
    inner ℂ (shift a u) u = V10B8a.weilTest f f (-a) := by
  rw [L2.inner_def]
  unfold V10B8a.weilTest V10B8a.tilde
  rw [convolution_def]
  apply integral_congr_ae
  filter_upwards [shift_ae a u,hae,V06D.ae_translate hae a] with x hx hy hz
  change conj (shift a u x)*u x = f x*conj (f (-(-a-x)))
  rw [hx,hy,hz]
  rw [show -(-a-x) = x+a by ring,mul_comm]

theorem prime_pairing (t : ℝ) (g : logCarrier t) (f : ℝ → ℂ)
    (hae : (physicalInclusion t g : ℝ → ℂ) =ᵐ[volume] f) :
    inner ℂ (primeOperator t g) g =
      ∑ n ∈ primeBank t, (primeWeight n:ℂ) *
        (V10B8a.weilTest f f (Real.log n)+V10B8a.weilTest f f (-Real.log n)) := by
  unfold primeOperator
  simp only [ContinuousLinearMap.comp_apply,ContinuousLinearMap.adjoint_inner_left]
  unfold physicalPrime
  rw [ContinuousLinearMap.sum_apply,sum_inner]
  apply Finset.sum_congr rfl
  intro n hn
  simp only [ContinuousLinearMap.smul_apply,inner_smul_left,Complex.conj_ofReal,
    shiftPair,ContinuousLinearMap.add_apply,inner_add_left]
  rw [shift_autocorr _ _ f hae,shift_autocorr _ _ f hae,neg_neg,add_comm]

theorem prime_outside (t : ℝ) (f : ℝ → ℂ) (hfs : tsupport f ⊆ Icc (-t) t)
    (n : ℕ) (hn : n ∉ primeBank t) :
    (primeWeight n:ℂ) *
        (V10B8a.weilTest f f (Real.log n)+V10B8a.weilTest f f (-Real.log n)) = 0 := by
  rcases Nat.eq_zero_or_pos n with rfl | hp
  · simp [primeWeight]
  · have hN : ⌊Real.exp (2*t)⌋₊ < n := by
      by_contra h
      apply hn
      exact Finset.mem_Ioc.mpr ⟨hp,le_of_not_gt h⟩
    have hex : Real.exp (2*t) < (n:ℝ) := (Nat.floor_lt (Real.exp_pos _).le).mp hN
    have hlog : 2*t < Real.log n := by
      rw [← Real.log_exp (2*t)]
      exact Real.log_lt_log (Real.exp_pos _) hex
    have hs := V10B8a.autocorr_support hfs
    have h₁ : V10B8a.weilTest f f (Real.log n) = 0 := by
      apply image_eq_zero_of_notMem_tsupport
      intro h
      exact (not_le_of_gt hlog) (hs h).2
    have h₂ : V10B8a.weilTest f f (-Real.log n) = 0 := by
      apply image_eq_zero_of_notMem_tsupport
      intro h
      have hh := (hs h).1
      linarith
    rw [h₁,h₂,add_zero,mul_zero]

theorem prime_literal (t : ℝ) (g : logCarrier t) (f : ℝ → ℂ)
    (hfs : tsupport f ⊆ Icc (-t) t)
    (hae : (physicalInclusion t g : ℝ → ℂ) =ᵐ[volume] f) :
    inner ℂ (primeOperator t g) g =
      ∑' n : ℕ, (primeWeight n:ℂ) *
        (V10B8a.weilTest f f (Real.log n)+V10B8a.weilTest f f (-Real.log n)) := by
  rw [tsum_eq_sum (s := primeBank t) (fun n hn => prime_outside t f hfs n hn)]
  exact prime_pairing t g f hae

end WeilDefect.MasterRecon.V10B8d

#print axioms WeilDefect.MasterRecon.V10B8d.shift_ae
#print axioms WeilDefect.MasterRecon.V10B8d.shift_norm
#print axioms WeilDefect.MasterRecon.V10B8d.shift_inverse
#print axioms WeilDefect.MasterRecon.V10B8d.shift_adjoint
#print axioms WeilDefect.MasterRecon.V10B8d.shiftPair_selfAdjoint
#print axioms WeilDefect.MasterRecon.V10B8d.shiftPair_norm
#print axioms WeilDefect.MasterRecon.V10B8d.prime_compact
#print axioms WeilDefect.MasterRecon.V10B8d.prime_selfAdjoint
#print axioms WeilDefect.MasterRecon.V10B8d.shift_autocorr
#print axioms WeilDefect.MasterRecon.V10B8d.prime_pairing
#print axioms WeilDefect.MasterRecon.V10B8d.prime_outside
#print axioms WeilDefect.MasterRecon.V10B8d.prime_literal
