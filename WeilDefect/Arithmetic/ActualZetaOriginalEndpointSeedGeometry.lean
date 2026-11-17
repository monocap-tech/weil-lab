import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory

/-!
NF578: independently check the exact NF577 scalar constants and
the literal affine-compressed convolution support. The two analytic
integral estimates and the strong L2 limit are still separate.
No dependency on the pending original log graph chain.
-/

def neutralNF578B : ℝ := 11/10
def neutralNF578Delta : ℝ := 1/500
def neutralNF578Center : ℝ := 1099/1000
def neutralNF578Epsilon (s : ℝ) : ℝ := (1-s)/2000
def neutralNF578PositiveCollar : Set ℝ := Set.Ioo (549/500 : ℝ) (11/10)
def neutralNF578C0 : ℝ := 2/10^7
def neutralNF578C1 : ℝ := 7/10^4 + neutralNF578C0/2

/-- Exact arithmetic closure of the high-frequency integration-by-parts
bound, after its log(BT) <= 1+L and log(550)<7 estimates. -/
theorem neutralNF578HighBand_scalar (T L : ℝ)
    (hT : 500 ≤ T) (hL : 0 ≤ L) :
    (neutralNF578C0*(3*(1+L)+1)+
      neutralNF578C1*(1/500)*8)/T ≤
      (1/40000)*(1+L)/(1+T) := by
  have ht : 0 < T := by linarith
  have ht' : 0 < 1+T := by linarith
  have hn : neutralNF578C0*(3*(1+L)+1)+
      neutralNF578C1*(1/500)*8 ≤ (1/50000)*(1+L) := by
    unfold neutralNF578C1 neutralNF578C0
    linarith
  have hd : 1+T ≤ (501/500:ℝ)*T := by linarith
  have hc : (0:ℝ) ≤ (1/50000)*(1+L) := by positivity
  have hc' : (1/50000:ℝ)*(1+L)*(501/500) ≤ (1/40000)*(1+L) := by
    linarith
  calc
    _ ≤ ((1/50000)*(1+L))/T := div_le_div_of_nonneg_right hn ht.le
    _ ≤ _ := by
      apply (div_le_div_iff₀ ht ht').mpr
      calc
        _ ≤ ((1/50000)*(1+L))*((501/500)*T) :=
          mul_le_mul_of_nonneg_left hd hc
        _ = ((1/50000)*(1+L)*(501/500))*T := by ring
        _ ≤ _ := mul_le_mul_of_nonneg_right hc' ht.le

/-- Exact low-band arithmetic, after the direct L1 log-integral bound. -/
theorem neutralNF578LowBand_scalar (T L : ℝ)
    (hT0 : 0 ≤ T) (hT : T ≤ 500) (hL : 0 ≤ L) :
    neutralNF578C0*(1/500)*8 ≤
      (1/40000)*(1+L)/(1+T) := by
  apply (le_div_iff₀ (by linarith : 0 < 1+T)).mpr
  unfold neutralNF578C0
  linarith

/-- The actual NF528/NF577 affine contraction of a real half-carrier. -/
def neutralNF578CompressedHalf (h : ℝ → ℝ) (s x : ℝ) : ℝ :=
  h (neutralNF578Center+(x-neutralNF578Center)/s)

/-- The actual convolution of the compressed half with a real kernel.
No smoothness or integrability is smuggled in by its definition. -/
def neutralNF578ConvolvedHalf (h ρ : ℝ → ℝ) (s x : ℝ) : ℝ :=
  ∫ y : ℝ, ρ y * neutralNF578CompressedHalf h s (x-y)

/-- If the source argument and kernel displacement are both in their
proper supports then the output point is strictly in the SAME collar. -/
theorem neutralNF578Convolution_geometry (s x y : ℝ)
    (hs : 0 < s) (hs' : s < 1)
    (hy : |y| ≤ neutralNF578Epsilon s)
    (hx : neutralNF578Center+(x-y-neutralNF578Center)/s ∈
      neutralNF578PositiveCollar) :
    x ∈ neutralNF578PositiveCollar := by
  change (549/500:ℝ) < neutralNF578Center+(x-y-neutralNF578Center)/s ∧
    neutralNF578Center+(x-y-neutralNF578Center)/s < (11/10:ℝ) at hx
  change (549/500:ℝ) < x ∧ x < (11/10:ℝ)
  unfold neutralNF578Center at hx
  unfold neutralNF578Epsilon at hy
  have hy' := abs_le.mp hy
  have hl : -(1/1000:ℝ) < (x-y-1099/1000)/s := by linarith [hx.1]
  have hu : (x-y-1099/1000)/s < (1/1000:ℝ) := by linarith [hx.2]
  have hleft := (lt_div_iff₀ hs).mp hl
  have hright := (div_lt_iff₀ hs).mp hu
  constructor <;> linarith [hy'.1,hy'.2,hleft,hright]

/-- Pointwise support of the actual affine convolution. This is not a
statement about an abstract family of seed transforms. -/
theorem neutralNF578ConvolvedHalf_supported
    (h ρ : ℝ → ℝ) (s x : ℝ) (hs : 0 < s) (hs' : s < 1)
    (hh : ∀ u, u ∉ neutralNF578PositiveCollar → h u = 0)
    (hρ : ∀ y, neutralNF578Epsilon s < |y| → ρ y = 0)
    (hx : x ∉ neutralNF578PositiveCollar) :
    neutralNF578ConvolvedHalf h ρ s x = 0 := by
  unfold neutralNF578ConvolvedHalf
  have hz : (fun y : ℝ => ρ y * neutralNF578CompressedHalf h s (x-y)) =
      (fun _ : ℝ => (0:ℝ)) := by
    funext y
    by_cases hy : |y| ≤ neutralNF578Epsilon s
    · have ha : neutralNF578Center+(x-y-neutralNF578Center)/s ∉
          neutralNF578PositiveCollar := by
        intro ha
        exact hx (neutralNF578Convolution_geometry s x y hs hs' hy ha)
      simp only [neutralNF578CompressedHalf, hh _ ha, mul_zero]
    · rw [hρ y (lt_of_not_ge hy), zero_mul]
  rw [hz]
  simp

/-- Restore exact odd parity by reflection, with a real-valued seed. -/
def neutralNF578OddSeed (h ρ : ℝ → ℝ) (s x : ℝ) : ℝ :=
  neutralNF578ConvolvedHalf h ρ s x - neutralNF578ConvolvedHalf h ρ s (-x)

theorem neutralNF578OddSeed_odd (h ρ : ℝ → ℝ) (s x : ℝ) :
    neutralNF578OddSeed h ρ s (-x) = -neutralNF578OddSeed h ρ s x := by
  simp only [neutralNF578OddSeed, neg_neg]
  ring

theorem neutralNF578OddSeed_supported
    (h ρ : ℝ → ℝ) (s x : ℝ) (hs : 0 < s) (hs' : s < 1)
    (hh : ∀ u, u ∉ neutralNF578PositiveCollar → h u = 0)
    (hρ : ∀ y, neutralNF578Epsilon s < |y| → ρ y = 0)
    (hx : x ∉ neutralNF578PositiveCollar)
    (hnx : -x ∉ neutralNF578PositiveCollar) :
    neutralNF578OddSeed h ρ s x = 0 := by
  rw [neutralNF578OddSeed,
    neutralNF578ConvolvedHalf_supported h ρ s x hs hs' hh hρ hx,
    neutralNF578ConvolvedHalf_supported h ρ s (-x) hs hs' hh hρ hnx, sub_self]

end
end WeilDefect
