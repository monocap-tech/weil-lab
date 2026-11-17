import WeilDefect.Arithmetic.ActualZetaOriginalEndpointSeedGeometry
import Mathlib.Analysis.Complex.ExponentialBounds

namespace WeilDefect
noncomputable section
open Set

/-! NF585: literal real twisted half-carrier amplitude and its
derivative. All numerical constants are the historical NF577
ones, paid independently of the pending Fourier split proofs. -/

def neutralNF585TwistedAmplitude (U : ℝ → ℝ) (y d : ℝ) : ℝ :=
  (U (neutralNF578B-d)/2)*Real.exp (-y*(neutralNF578B-d))

def neutralNF585TwistedDerivative (U U' : ℝ → ℝ) (y d : ℝ) : ℝ :=
  ((-U' (neutralNF578B-d)+y*U (neutralNF578B-d))/2) *
    Real.exp (-y*(neutralNF578B-d))

theorem neutralNF585Twisted_hasDerivAt (U U' : ℝ → ℝ) (y d : ℝ)
    (h : HasDerivAt U (U' (neutralNF578B-d)) (neutralNF578B-d)) :
    HasDerivAt (neutralNF585TwistedAmplitude U y)
      (neutralNF585TwistedDerivative U U' y d) d := by
  have hx : HasDerivAt (fun d : ℝ => neutralNF578B-d) (-1) d := by
    simpa only [Pi.sub_apply, id_eq, zero_sub] using
      (hasDerivAt_const d neutralNF578B).sub (hasDerivAt_id d)
  have hu := (h.comp d hx).div_const 2
  have he := (hx.const_mul (-y)).exp
  have hp := hu.mul he
  unfold neutralNF585TwistedAmplitude neutralNF585TwistedDerivative
  convert hp using 1
  · funext x
    simp only [Pi.mul_apply, Function.comp_apply]
  · simp only [Function.comp_apply]
    ring

theorem neutralNF585Twisted_continuousOn (U : ℝ → ℝ) (y : ℝ)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B)) :
    ContinuousOn (neutralNF585TwistedAmplitude U y) (Icc 0 neutralNF578Delta) := by
  have hx : Continuous (fun d : ℝ => neutralNF578B-d) := by fun_prop
  have hm : MapsTo (fun d : ℝ => neutralNF578B-d) (Icc 0 neutralNF578Delta)
      (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B) := by
    intro d hd
    exact ⟨by linarith [hd.2], by linarith [hd.1]⟩
  exact ((hU.comp hx.continuousOn hm).div_const 2).mul (by fun_prop)

theorem neutralNF585TwistedDerivative_continuousOn (U U' : ℝ → ℝ) (y : ℝ)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hU' : ContinuousOn U' (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B)) :
    ContinuousOn (neutralNF585TwistedDerivative U U' y) (Icc 0 neutralNF578Delta) := by
  have hx : Continuous (fun d : ℝ => neutralNF578B-d) := by fun_prop
  have hm : MapsTo (fun d : ℝ => neutralNF578B-d) (Icc 0 neutralNF578Delta)
      (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B) := by
    intro d hd
    exact ⟨by linarith [hd.2], by linarith [hd.1]⟩
  have hu := hU.comp hx.continuousOn hm
  have hu' := hU'.comp hx.continuousOn hm
  exact ((hu'.neg.add (continuousOn_const.mul hu)).div_const 2).mul (by fun_prop)

theorem neutralNF585Exp_half_le_two : Real.exp (neutralNF578B/2) ≤ 2 := by
  have h : neutralNF578B/2 ≤ Real.log 2 := by
    unfold neutralNF578B
    linarith [Real.log_two_gt_d9]
  simpa only [Real.exp_log (by norm_num : (0:ℝ)<2)] using Real.exp_le_exp.mpr h

theorem neutralNF585Twist_exp_le_two (y d : ℝ) (hy : |y| ≤ 1/2)
    (hd : d ∈ Icc 0 neutralNF578Delta) :
    Real.exp (-y*(neutralNF578B-d)) ≤ 2 := by
  have hx : 0 ≤ neutralNF578B-d := by
    unfold neutralNF578B neutralNF578Delta at *
    linarith [hd.2]
  have hx' : neutralNF578B-d ≤ neutralNF578B := by linarith [hd.1]
  have hn : -y ≤ 1/2 := (neg_le_abs y).trans hy
  have h : -y*(neutralNF578B-d) ≤ neutralNF578B/2 := by
    calc
      _ ≤ (1/2)*(neutralNF578B-d) := mul_le_mul_of_nonneg_right hn hx
      _ ≤ (1/2)*neutralNF578B := mul_le_mul_of_nonneg_left hx' (by norm_num)
      _ = _ := by ring
  exact (Real.exp_le_exp.mpr h).trans neutralNF585Exp_half_le_two

/-- Historical NF577 bounds on the actual U and U' pay the exact
twisted amplitude with no replacement by a Taylor polynomial. -/
theorem neutralNF585Twisted_bounds
    (U U' : ℝ → ℝ) (y d : ℝ)
    (hy : |y| ≤ 1/2) (hd : d ∈ Icc 0 neutralNF578Delta)
    (hU : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      |U x| ≤ neutralNF578C0)
    (hU' : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      |U' x| ≤ (7/10^4:ℝ)) :
    |neutralNF585TwistedAmplitude U y d| ≤ neutralNF578C0 ∧
      |neutralNF585TwistedDerivative U U' y d| ≤ neutralNF578C1 := by
  let x := neutralNF578B-d
  have hx : x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B := by
    exact ⟨by dsimp [x]; linarith [hd.2], by dsimp [x]; linarith [hd.1]⟩
  have h0 := hU x hx
  have h1 := hU' x hx
  have he := neutralNF585Twist_exp_le_two y d hy hd
  have hep : 0 ≤ Real.exp (-y*x) := (Real.exp_pos _).le
  have h0p : 0 ≤ neutralNF578C0 := by unfold neutralNF578C0; norm_num
  have h1p : 0 ≤ neutralNF578C1 := by unfold neutralNF578C1 neutralNF578C0; norm_num
  have hp : |y*U x| ≤ (1/2)*neutralNF578C0 := by
    rw [abs_mul]
    exact mul_le_mul hy h0 (abs_nonneg _) (by norm_num)
  have hsum : |-U' x+y*U x| ≤ neutralNF578C1 := by
    calc
      _ ≤ |-U' x|+|y*U x| := abs_add_le _ _
      _ ≤ (7/10^4:ℝ)+(1/2)*neutralNF578C0 := by rw [abs_neg]; exact add_le_add h1 hp
      _ = _ := by unfold neutralNF578C1; ring
  constructor
  · change |(U x/2)*Real.exp (-y*x)| ≤ _
    rw [abs_mul, abs_div, abs_of_nonneg hep, abs_of_nonneg (by norm_num : (0:ℝ)≤2)]
    calc
      _ ≤ (neutralNF578C0/2)*2 := mul_le_mul
        (div_le_div_of_nonneg_right h0 (by norm_num)) he hep (by positivity)
      _ = _ := by ring
  · change |((-U' x+y*U x)/2)*Real.exp (-y*x)| ≤ _
    rw [abs_mul, abs_div, abs_of_nonneg hep, abs_of_nonneg (by norm_num : (0:ℝ)≤2)]
    calc
      _ ≤ (neutralNF578C1/2)*2 := mul_le_mul
        (div_le_div_of_nonneg_right hsum (by norm_num)) he hep (by positivity)
      _ = _ := by ring

end
end WeilDefect
