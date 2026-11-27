import WeilDefect.Arithmetic.ActualZetaIV106E18LBufferedGeometry
import WeilDefect.Arithmetic.ActualZetaIV106E18MPlateauMass
import WeilDefect.Arithmetic.ActualZetaIV106E18NExponentialSeries

namespace WeilDefect
noncomputable section
open MeasureTheory Set InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

def neutralIV106E18OTrial (j : ℕ) : RealComplexL2 :=
  (neutralIV106E18JTrial_memLp (neutralIV106E18LLeft j)
    neutralIV106E18LWidth (by norm_num [neutralIV106E18LWidth])).toLp _

def neutralIV106E18OEntry (k : ℕ) (hk : 0 < k) (i : Fin k) (j : ℕ) : ℂ :=
  inner ℂ (neutralIV105CResponse k hk i) (neutralIV106E18OTrial (j+1))

def neutralIV106E18OX (n : ℕ) : ℝ :=
  Real.exp (neutralIV106E18NRate n*neutralIV106E18LWidth)

def neutralIV106E18OY (k n : ℕ) : ℝ :=
  Real.exp (-neutralIV106E18NRate n*(3/(2000*(k:ℝ))))

def neutralIV106E18OW (k : ℕ) (hk : 0 < k) (n : ℕ) : ℝ :=
  (∫ x, neutralIV106E18MProfile k ⟨0,hk⟩ x *
    Real.exp (-neutralIV106E18NRate n*x)) *
  (neutralIV106E18LWidth *
    Real.exp (neutralIV106E18NRate n*neutralIV106E18LLeft 1)) *
  (-(∫ t in (0:ℝ)..1, Real.exp ((neutralIV106E18NRate n*
    neutralIV106E18LWidth)*t)*neutralIV106E18K1Poly neutralIV106E18LWidth t))

/-- No need to compute a specific choice-defined bump. The row-zero
weighted integral is positive, the polynomial coefficient fixes the sign. -/
theorem neutralIV106E18OW_pos (k : ℕ) (hk : 0 < k) (n : ℕ) (hn : 0 < n) :
    0 < neutralIV106E18OW k hk n := by
  have hh : 0 < neutralIV106E18LWidth := by norm_num [neutralIV106E18LWidth]
  have hs : (1/2:ℝ) < neutralIV106E18NRate n := by
    unfold neutralIV106E18NRate
    have hn' : (0:ℝ) < (n:ℝ) := by exact_mod_cast hn
    linarith
  unfold neutralIV106E18OW
  exact mul_pos (mul_pos (neutralIV106E18MProfile_weight_pos k hk _ _)
    (mul_pos hh (Real.exp_pos _))) (neutralIV106E18NPolynomial_sign _ _ hh hs)

theorem neutralIV106E18OW_zero (k : ℕ) (hk : 0 < k) :
    neutralIV106E18OW k hk 0 = 0 := by
  unfold neutralIV106E18OW
  rw [neutralIV106E18K1Zero _ _ (Or.inr (Or.inl (by
    unfold neutralIV106E18NRate
    push_cast
    ring)))]
  ring

theorem neutralIV106E18OX_strict : StrictMono neutralIV106E18OX := by
  intro n m hnm
  unfold neutralIV106E18OX neutralIV106E18NRate
  have hn : (n:ℝ) < (m:ℝ) := by exact_mod_cast hnm
  exact Real.exp_lt_exp.mpr (mul_lt_mul_of_pos_right (by linarith)
    (by norm_num [neutralIV106E18LWidth]))

theorem neutralIV106E18OY_strict (k : ℕ) (hk : 0 < k) :
    StrictAnti (neutralIV106E18OY k) := by
  intro n m hnm
  unfold neutralIV106E18OY neutralIV106E18NRate
  have hn : (n:ℝ) < (m:ℝ) := by exact_mod_cast hnm
  have hk' : (0:ℝ) < (k:ℝ) := by exact_mod_cast hk
  exact Real.exp_lt_exp.mpr (mul_lt_mul_of_pos_right (by linarith)
    (by positivity))

/-- The entire integral of the clipped trial equals its finite cell integral. -/
theorem neutralIV106E18OTrial_weight (l h s : ℝ) (hh : 0 < h) :
    neutralIV106E18NWeight (neutralIV106E18ITrial l h) s =
      ((h*Real.exp (s*l)) *
        (∫ t in (0:ℝ)..1, Real.exp ((s*h)*t)*neutralIV106E18K1Poly h t) : ℝ) := by
  unfold neutralIV106E18NWeight
  rw [← setIntegral_eq_integral_of_forall_compl_eq_zero
    (s := Set.Icc l (l+h))
    (f := fun x => neutralIV106E18ITrial l h x*(Real.exp (s*x):ℂ))
    (fun x hx => by simp [neutralIV106E18ITrial_outside l h hh x hx]),
    integral_Icc_eq_integral_Ioc, ← intervalIntegral.integral_of_le (by linarith : l ≤ l+h)]
  rw [neutralIV106E18K2Affine l h s hh]
  push_cast
  rfl

theorem neutralIV106E18ORow_weight (k : ℕ) (hk : 0 < k) (i : Fin k) (s : ℝ) :
    neutralIV106E18NWeight (neutralIV100Carrier k hk i) s =
      (Real.exp (s*((i.val:ℝ)*(3/(2000*(k:ℝ))))) *
        (∫ x, neutralIV106E18MProfile k ⟨0,hk⟩ x*Real.exp (s*x)) : ℝ) := by
  unfold neutralIV106E18NWeight
  simp_rw [neutralIV106E18MCarrier_real k hk i,← Complex.ofReal_mul]
  rw [integral_complex_ofReal,neutralIV106E18MProfile_weight_translate k hk i s]

theorem neutralIV106E18OLeft_step (j : ℕ) :
    neutralIV106E18LLeft (j+1) = neutralIV106E18LLeft 1 +
      (j:ℝ)*neutralIV106E18LWidth := by
  unfold neutralIV106E18LLeft neutralIV106E18LWidth
  push_cast
  ring

/-- Literal coefficient identity, including the complex coercion. -/
theorem neutralIV106E18OTerm (k : ℕ) (hk : 0 < k) (i : Fin k) (j n : ℕ) :
    neutralIV106E18NTerm (neutralIV100Carrier k hk i)
      (neutralIV106E18ITrial (neutralIV106E18LLeft (j+1)) neutralIV106E18LWidth) n =
    (neutralIV106E18OW k hk n *
      neutralIV106E18OY k n ^ i.val * neutralIV106E18OX n ^ j : ℝ) := by
  unfold neutralIV106E18NTerm
  rw [neutralIV106E18ORow_weight k hk i,neutralIV106E18OTrial_weight _ _ _
    (by norm_num [neutralIV106E18LWidth]),neutralIV106E18OLeft_step]
  unfold neutralIV106E18OW neutralIV106E18OX neutralIV106E18OY
  rw [← Real.exp_nat_mul,← Real.exp_nat_mul]
  have he : neutralIV106E18NRate n *
      (neutralIV106E18LLeft 1+(j:ℝ)*neutralIV106E18LWidth) =
      neutralIV106E18NRate n*neutralIV106E18LLeft 1 +
      (j:ℝ)*(neutralIV106E18NRate n*neutralIV106E18LWidth) := by ring
  rw [he,Real.exp_add]
  have hr : -neutralIV106E18NRate n*((i.val:ℝ)*(3/(2000*(k:ℝ)))) =
    (i.val:ℝ)*(-neutralIV106E18NRate n*(3/(2000*(k:ℝ)))) := by ring
  rw [hr]
  push_cast
  ring

/-- All original eligible cells lie strictly to the left of the packed collar.
This uses the literal trial support, not a Schwartz replacement. -/
theorem neutralIV106E18OEntry_series (k : ℕ) (hk : 0 < k) (i : Fin k)
    (j : ℕ) (hj : neutralIV106E18LEligible (j+1)) :
    HasSum (fun n : ℕ => (neutralIV106E18OW k hk n *
      neutralIV106E18OY k n ^ i.val * neutralIV106E18OX n ^ j : ℂ))
      (neutralIV106E18OEntry k hk i j) := by
  let u := neutralIV100Carrier k hk i
  let f := neutralIV106E18ITrial (neutralIV106E18LLeft (j+1)) neutralIV106E18LWidth
  have hh : 0 < neutralIV106E18LWidth := by norm_num [neutralIV106E18LWidth]
  have huc : HasCompactSupport (u : ℝ → ℂ) := by
    apply HasCompactSupport.intro (K := Icc (4393/4000:ℝ) (4399/4000)) isCompact_Icc
    exact neutralIV106E18JCarrier_zero k hk i
  have hf : Continuous f := neutralIV106E18ITrial_continuous _ _
  have hfc : HasCompactSupport f := neutralIV106E18ITrial_compact _ _ hh
  have hleft : ∀ y, f y ≠ 0 → y ≤ (1097/1000:ℝ) := by
    intro y hy
    have hm : y ∈ Icc (neutralIV106E18LLeft (j+1))
        (neutralIV106E18LLeft (j+1)+neutralIV106E18LWidth) := by
      by_contra hn
      exact hy (neutralIV106E18ITrial_outside _ _ hh _ hn)
    have hJ : ((j+1:ℕ):ℝ) ≤ 663 := by exact_mod_cast hj.2.1
    have he := hm.2
    unfold neutralIV106E18LLeft neutralIV106E18LWidth at he
    linarith only [he,hJ]
  have hright : ∀ x, u x ≠ 0 → (4393/4000:ℝ) ≤ x := by
    intro x hx
    have hm : x ∈ Icc (4393/4000:ℝ) (4399/4000) := by
      by_contra hn
      exact hx (neutralIV106E18JCarrier_zero k hk i x hn)
    exact hm.1
  have hs := neutralIV106E18NSeries u f huc hf hfc
    (1097/1000) (4393/4000) (by norm_num) hleft hright
  have he : neutralIV106E18OEntry k hk i j =
      ∫ x, u x*(∫ y, f y*
        ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ):ℂ)) := by
    unfold neutralIV106E18OEntry neutralIV106E18OTrial
    rw [neutralIV106E18LResponse k hk i (j+1) hj]
    apply integral_congr_ae
    filter_upwards [] with x
    change conj (u x)*_ = u x*_
    rw [show conj (u x) = u x by
      change conj (neutralIV100Carrier k hk i x) = _
      rw [neutralIV106E18MCarrier_real k hk i x,Complex.conj_ofReal]]
  rw [he]
  have ht : neutralIV106E18NTerm u f =
      fun n : ℕ => ((neutralIV106E18OW k hk n *
        neutralIV106E18OY k n ^ i.val * neutralIV106E18OX n ^ j : ℝ):ℂ) :=
    funext (neutralIV106E18OTerm k hk i j)
  rw [ht] at hs
  simpa only [Complex.ofReal_mul,Complex.ofReal_pow] using hs

/-- The first 34 consecutive interior cells avoid all excluded indices. -/
theorem neutralIV106E18OConsecutive (k : ℕ) (hk : k ≤ 34) (j : Fin k) :
    neutralIV106E18LEligible (j.val+1) := by
  have hj := j.isLt
  unfold neutralIV106E18LEligible
  omega

/-- Real response matrix with a positive-factor series on consecutive cells. -/
def neutralIV106E18OMatrix (k : ℕ) (hk : 0 < k) : Matrix (Fin k) (Fin k) ℝ :=
  fun i j => (neutralIV106E18OEntry k hk i j.val).re

theorem neutralIV106E18OMatrix_series (k : ℕ) (hk : 0 < k) (hk34 : k ≤ 34)
    (i j : Fin k) :
    HasSum (fun n : ℕ => neutralIV106E18OW k hk n *
      neutralIV106E18OY k n ^ i.val * neutralIV106E18OX n ^ j.val)
      (neutralIV106E18OMatrix k hk i j) := by
  have hs := Complex.hasSum_re (neutralIV106E18OEntry_series k hk i j.val
    (neutralIV106E18OConsecutive k hk34 j))
  simpa [neutralIV106E18OMatrix] using hs

theorem neutralIV106E18OMatrix_literal (k : ℕ) (hk : 0 < k) (hk34 : k ≤ 34)
    (i j : Fin k) :
    neutralIV106E18OEntry k hk i j.val =
      (neutralIV106E18OMatrix k hk i j : ℂ) := by
  have hs := neutralIV106E18OEntry_series k hk i j.val
    (neutralIV106E18OConsecutive k hk34 j)
  have hr := (Complex.hasSum_ofReal).mpr (neutralIV106E18OMatrix_series k hk hk34 i j)
  apply hs.unique
  simpa only [Complex.ofReal_mul,Complex.ofReal_pow] using hr

#print axioms neutralIV106E18OW_pos
#print axioms neutralIV106E18OW_zero
#print axioms neutralIV106E18OX_strict
#print axioms neutralIV106E18OY_strict
#print axioms neutralIV106E18OTrial_weight
#print axioms neutralIV106E18ORow_weight
#print axioms neutralIV106E18OLeft_step
#print axioms neutralIV106E18OTerm
#print axioms neutralIV106E18OEntry_series
#print axioms neutralIV106E18OConsecutive
#print axioms neutralIV106E18OMatrix_series
#print axioms neutralIV106E18OMatrix_literal
end
end WeilDefect
