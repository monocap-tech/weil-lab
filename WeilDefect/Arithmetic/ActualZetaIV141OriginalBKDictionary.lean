import WeilDefect.Arithmetic.ActualZetaIV139OriginalCompactAttachment
import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap BigOperators ComplexConjugate

/-- BK's actual radius-two restricted trigonometric dictionary.
The even zero mode has the separate normalization 1/sqrt(8).
The positive mode ID is not the row position in the recovered array. -/
def neutralIV141ModeValue (odd : Bool) (j : ℕ) (x : ℝ) : ℂ :=
  if odd = true then ((Real.sin ((j:ℝ)*Real.pi*x/8)/2 : ℝ) : ℂ)
  else if j = 0 then ((1/Real.sqrt 8 : ℝ) : ℂ)
  else ((Real.cos ((j:ℝ)*Real.pi*x/8)/2 : ℝ) : ℂ)

theorem neutralIV141Mode_continuous (odd : Bool) (j : ℕ) :
    Continuous (neutralIV141ModeValue odd j) := by
  cases odd
  · by_cases hj : j = 0 <;> simp [neutralIV141ModeValue,hj] <;> fun_prop
  · simp [neutralIV141ModeValue] <;> fun_prop

def neutralIV141Mode (odd : Bool) (j : ℕ) : ℝ → ℂ :=
  (Set.Icc (-(2:ℝ)) 2).indicator (neutralIV141ModeValue odd j)

theorem neutralIV141Mode_memLp (odd : Bool) (j : ℕ) :
    MemLp (neutralIV141Mode odd j) 2 volume := by
  have hc := neutralIV141Mode_continuous odd j
  have hm : AEStronglyMeasurable (neutralIV141Mode odd j) volume :=
    hc.aestronglyMeasurable.indicator measurableSet_Icc
  apply (memLp_two_iff_integrable_sq_norm hm).mpr
  have hi : IntegrableOn (fun x : ℝ => ‖neutralIV141ModeValue odd j x‖^2)
      (Set.Icc (-(2:ℝ)) 2) volume := (hc.norm.pow 2).integrableOn_Icc
  apply (hi.integrable_indicator measurableSet_Icc).congr
  filter_upwards [] with x
  by_cases hx : x ∈ Set.Icc (-(2:ℝ)) 2 <;>
    simp [neutralIV141Mode,hx]

def neutralIV141ModeL2 (odd : Bool) (j : ℕ) : RealComplexL2 :=
  (neutralIV141Mode_memLp odd j).toLp (neutralIV141Mode odd j)

theorem neutralIV141Mode_pair (odd : Bool) (j : ℕ) (f : RealComplexL2) :
    inner ℂ (neutralIV141ModeL2 odd j) f =
      ∫ x in Set.Icc (-(2:ℝ)) 2, conj (neutralIV141ModeValue odd j x)*f x := by
  rw [L2.inner_def, ← integral_indicator measurableSet_Icc]
  apply integral_congr_ae
  filter_upwards [(neutralIV141Mode_memLp odd j).coeFn_toLp] with x hx
  change inner ℂ ((neutralIV141Mode_memLp odd j).toLp
    (neutralIV141Mode odd j) x) (f x) = _
  rw [hx]
  by_cases hmem : x ∈ Set.Icc (-(2:ℝ)) 2 <;>
    simp [neutralIV141Mode,hmem,RCLike.inner_apply']

/-- Raw TN column, from integer data only. BK's two exact denominators
are explicit. Nonnegative deficit numerators are stored as naturals.
No particular array has yet been supplied to this definition. -/
def neutralIV141RawColumn {m n : ℕ} (odd : Bool)
    (mode deficit : Fin m → ℕ) (N : Fin m → Fin n → ℤ)
    (i : Fin n) : RealComplexL2 :=
  ∑ j : Fin m,
    (((N j i : ℤ) : ℂ) / (2^23 : ℂ) *
      (Real.sqrt ((deficit j : ℝ)/10^8) : ℂ)) •
      neutralIV141ModeL2 odd (mode j)

/-- The projected BK columns differ from the raw ones by the two
literal pole columns. On the double-pole-null space these differences
are annihilators, so the raw dictionary can be used without projection
coefficient enclosures for the purpose of tail constraints. -/
theorem neutralIV141PoleShift_pair (r f : RealComplexL2) (c d : ℂ)
    (hp : sourceWindowMoment 2 (1/2) f = 0)
    (hm : sourceWindowMoment 2 (-(1/2)) f = 0) :
    inner ℂ (r - c • neutralMomentColumnL2 2 (1/2) -
      d • neutralMomentColumnL2 2 (-(1/2))) f = inner ℂ r f := by
  rw [inner_sub_left,inner_sub_left,inner_smul_left,inner_smul_left,
    neutralMomentColumnL2_inner,neutralMomentColumnL2_inner,hp,hm]
  simp

def neutralIV141ParityPole (odd : Bool) : RealComplexL2 :=
  if odd = true then (1/2:ℂ) •
    (neutralMomentColumnL2 2 (1/2) - neutralMomentColumnL2 2 (-(1/2)))
  else (1/2:ℂ) •
    (neutralMomentColumnL2 2 (1/2) + neutralMomentColumnL2 2 (-(1/2)))

theorem neutralIV141ParityPole_pair (odd : Bool) (f : RealComplexL2)
    (hp : sourceWindowMoment 2 (1/2) f = 0)
    (hm : sourceWindowMoment 2 (-(1/2)) f = 0) :
    inner ℂ (neutralIV141ParityPole odd) f = 0 := by
  cases odd <;>
    simp [neutralIV141ParityPole,inner_smul_left,inner_add_left,inner_sub_left,
      neutralMomentColumnL2_inner,hp,hm]

/-- Exact orthogonal projection formula onto the parity pole complement.
Its pairing identity below needs no lower bound for the pole norm. -/
def neutralIV141ProjectedColumn (odd : Bool) (r : RealComplexL2) : RealComplexL2 :=
  r - (inner ℂ (neutralIV141ParityPole odd) r /
    inner ℂ (neutralIV141ParityPole odd) (neutralIV141ParityPole odd)) •
      neutralIV141ParityPole odd

theorem neutralIV141Projected_pair (odd : Bool) (r f : RealComplexL2)
    (hp : sourceWindowMoment 2 (1/2) f = 0)
    (hm : sourceWindowMoment 2 (-(1/2)) f = 0) :
    inner ℂ (neutralIV141ProjectedColumn odd r) f = inner ℂ r f := by
  unfold neutralIV141ProjectedColumn
  rw [inner_sub_left,inner_smul_left,neutralIV141ParityPole_pair odd f hp hm,mul_zero,sub_zero]

theorem neutralIV141Bank_null_iff {n : ℕ} (odd : Bool) (r : Fin n → RealComplexL2)
    (f : RealComplexL2) (hp : sourceWindowMoment 2 (1/2) f = 0)
    (hm : sourceWindowMoment 2 (-(1/2)) f = 0) :
    (∀ i, inner ℂ (neutralIV141ProjectedColumn odd (r i)) f = 0) ↔
      (∀ i, inner ℂ (r i) f = 0) := by
  simp only [neutralIV141Projected_pair odd _ f hp hm]

#print axioms neutralIV141Mode_continuous
#print axioms neutralIV141Mode_memLp
#print axioms neutralIV141Mode_pair
#print axioms neutralIV141PoleShift_pair
#print axioms neutralIV141ParityPole_pair
#print axioms neutralIV141Projected_pair
#print axioms neutralIV141Bank_null_iff

end
end WeilDefect
