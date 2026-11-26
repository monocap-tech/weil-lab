import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped BigOperators Matrix

/-- Real autocorrelation is symmetric in the two samples. -/
theorem neutralIV106E6Pair_symm (u v : ℂ) :
    (star u*v).re = (star v*u).re := by
  simp only [Complex.star_def, Complex.mul_re, Complex.conj_re, Complex.conj_im]
  ring

def neutralIV106E6LagMatrix2 (c1 : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![0,c1; c1,0]

/-- Both matrix off-diagonals give exactly twice the positive lag contribution. -/
theorem neutralIV106E6Lag2 (c1 : ℝ) (z : Fin 2 → ℂ) :
    (∑ i, ∑ j, neutralIV106E6LagMatrix2 c1 i j*(star (z i)*z j).re) =
      2*(c1*((star (z 0)*z 1).re)) := by
  simp [Fin.sum_univ_succ, neutralIV106E6LagMatrix2, Complex.star_def,
    Complex.mul_re, Complex.conj_re, Complex.conj_im]
  <;> ring

def neutralIV106E6LagMatrix3 (c1 c2 : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![0,c1,c2; c1,0,c1; c2,c1,0]

/-- Both matrix off-diagonals give exactly twice the positive lag contribution. -/
theorem neutralIV106E6Lag3 (c1 c2 : ℝ) (z : Fin 3 → ℂ) :
    (∑ i, ∑ j, neutralIV106E6LagMatrix3 c1 c2 i j*(star (z i)*z j).re) =
      2*(c1*((star (z 0)*z 1).re+(star (z 1)*z 2).re)+
      c2*((star (z 0)*z 2).re)) := by
  simp [Fin.sum_univ_succ, neutralIV106E6LagMatrix3, Complex.star_def,
    Complex.mul_re, Complex.conj_re, Complex.conj_im]
  <;> ring

def neutralIV106E6LagMatrix4 (c1 c2 c3 : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![0,c1,c2,c3; c1,0,c1,c2; c2,c1,0,c1; c3,c2,c1,0]

/-- Both matrix off-diagonals give exactly twice the positive lag contribution. -/
theorem neutralIV106E6Lag4 (c1 c2 c3 : ℝ) (z : Fin 4 → ℂ) :
    (∑ i, ∑ j, neutralIV106E6LagMatrix4 c1 c2 c3 i j*(star (z i)*z j).re) =
      2*(c1*((star (z 0)*z 1).re+(star (z 1)*z 2).re+(star (z 2)*z 3).re)+
      c2*((star (z 0)*z 2).re+(star (z 1)*z 3).re)+
      c3*((star (z 0)*z 3).re)) := by
  simp [Fin.sum_univ_succ, neutralIV106E6LagMatrix4, Complex.star_def,
    Complex.mul_re, Complex.conj_re, Complex.conj_im]
  <;> ring

/-- Integrate a pointwise chain bound, preserving the actual mass identity. -/
theorem neutralIV106E6Integral_receiver (F M : ℝ → ℝ) (s L P mass : ℝ)
    (hs : 0 ≤ s) (hF : Continuous F) (hM : Continuous M)
    (hbound : ∀ t ∈ Set.Icc 0 s, F t ≤ L*M t)
    (hP : (∫ t in (0:ℝ)..s, F t) = P)
    (hm : (∫ t in (0:ℝ)..s, M t) = mass) :
    P ≤ L*mass := by
  have hLM : Continuous (fun t => L*M t) := continuous_const.mul hM
  have hi := intervalIntegral.integral_mono_on hs
    (hF.intervalIntegrable (μ := volume) 0 s)
    (hLM.intervalIntegrable (μ := volume) 0 s) hbound
  rw [intervalIntegral.integral_const_mul, hP, hm] at hi
  exact hi

/-- Sum the four physical prime groups with the exact E1 loss constant. -/
theorem neutralIV106E6Total_receiver (M P2 P3 P5 P7 : ℝ)
    (h2 : P2 ≤ (1214/1000:ℝ)*M)
    (h3 : P3 ≤ (1099/1000:ℝ)*M)
    (h5 : P5 ≤ (719763/1000000:ℝ)*M)
    (h7 : P7 ≤ (735485/1000000:ℝ)*M) :
    P2+P3+P5+P7 ≤ (471031/125000:ℝ)*M := by
  linarith only [h2,h3,h5,h7]

#print axioms neutralIV106E6Pair_symm
#print axioms neutralIV106E6Lag2
#print axioms neutralIV106E6Lag3
#print axioms neutralIV106E6Lag4
#print axioms neutralIV106E6Integral_receiver
#print axioms neutralIV106E6Total_receiver
end
end WeilDefect
