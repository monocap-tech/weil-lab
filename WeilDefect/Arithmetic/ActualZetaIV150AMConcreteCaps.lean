import WeilDefect.Arithmetic.ActualZetaIV147AMRealCaps
import Mathlib.Analysis.Complex.Exponential

namespace WeilDefect
noncomputable section
open scoped BigOperators
set_option maxHeartbeats 0

/-- Range reduction to [0,1] and the existing Mathlib exponential remainder. -/
def neutralIV150S (x : ℝ) : ℝ :=
  ∑ k ∈ Finset.range 16, (x/4)^k / (Nat.factorial k : ℝ)

def neutralIV150E (x : ℝ) : ℝ :=
  (x/4)^16 * (17 / (Nat.factorial 16 * 16 : ℝ))

theorem neutralIV150Exp_interval (x : ℝ) (hx : 0 ≤ x) (hx4 : x ≤ 4)
    (hl : 0 ≤ neutralIV150S x - neutralIV150E x) :
    (neutralIV150S x - neutralIV150E x)^4 ≤ Real.exp x ∧
      Real.exp x ≤ (neutralIV150S x + neutralIV150E x)^4 := by
  have hy : 0 ≤ x/4 := by linarith
  have hy1 : |x/4| ≤ 1 := by rw [abs_of_nonneg hy]; linarith
  have hb := Real.exp_bound (x := x/4) (n := 16) hy1 (by decide)
  rw [abs_of_nonneg hy] at hb
  have hb' : |Real.exp (x/4) - neutralIV150S x| ≤ neutralIV150E x := by
    simpa [neutralIV150S, neutralIV150E] using hb
  have h := abs_le.mp hb'
  have he : Real.exp x = Real.exp (x/4)^4 := by
    calc
      Real.exp x = Real.exp ((4:ℝ)*(x/4)) := by congr 1 <;> ring
      _ = _ := by simpa using Real.exp_nat_mul (x/4) 4
  rw [he]
  constructor
  · exact pow_le_pow_left₀ hl (by linarith [h.1]) 4
  · exact pow_le_pow_left₀ (Real.exp_pos _).le (by linarith [h.2]) 4

theorem neutralIV150Exp_lt (x b : ℝ) (hx : 0 ≤ x) (hx4 : x ≤ 4)
    (hl : 0 ≤ neutralIV150S x - neutralIV150E x)
    (hc : (neutralIV150S x + neutralIV150E x)^4 < b) :
    Real.exp x < b :=
  (neutralIV150Exp_interval x hx hx4 hl).2.trans_lt hc

theorem neutralIV150Lt_exp (x b : ℝ) (hx : 0 ≤ x) (hx4 : x ≤ 4)
    (hl : 0 ≤ neutralIV150S x - neutralIV150E x)
    (hc : b < (neutralIV150S x - neutralIV150E x)^4) :
    b < Real.exp x :=
  hc.trans_le (neutralIV150Exp_interval x hx hx4 hl).1

theorem neutralIV150Prime_2 :
    (Int.floor (Real.log 2 * 4096) = 2839 ∧
      Int.floor (-Real.log 2 * 4096) = -2840) ∧
    Real.log 2 / Real.sqrt 2 < (490129072/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 2) (j := 2839) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (141421356237309504880/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_3 :
    (Int.floor (Real.log 3 * 4096) = 4499 ∧
      Int.floor (-Real.log 3 * 4096) = -4500) ∧
    Real.log 3 / Real.sqrt 3 < (634284101/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 3) (j := 4499) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (173205080756887729352/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_4 :
    (Int.floor (Real.log 4 * 4096) = 5678 ∧
      Int.floor (-Real.log 4 * 4096) = -5679) ∧
    Real.log 2 / Real.sqrt 4 < (346573591/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 4) (j := 5678) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (200000000000000000000/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_5 :
    (Int.floor (Real.log 5 * 4096) = 6592 ∧
      Int.floor (-Real.log 5 * 4096) = -6593) ∧
    Real.log 5 / Real.sqrt 5 < (719762516/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 5) (j := 6592) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (223606797749978969640/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_7 :
    (Int.floor (Real.log 7 * 4096) = 7970 ∧
      Int.floor (-Real.log 7 * 4096) = -7971) ∧
    Real.log 7 / Real.sqrt 7 < (735484905/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 7) (j := 7970) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (264575131106459059050/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_8 :
    (Int.floor (Real.log 8 * 4096) = 8517 ∧
      Int.floor (-Real.log 8 * 4096) = -8518) ∧
    Real.log 2 / Real.sqrt 8 < (245064536/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 8) (j := 8517) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (282842712474619009760/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_9 :
    (Int.floor (Real.log 9 * 4096) = 8999 ∧
      Int.floor (-Real.log 9 * 4096) = -9000) ∧
    Real.log 3 / Real.sqrt 9 < (366204097/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 9) (j := 8999) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (300000000000000000000/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_11 :
    (Int.floor (Real.log 11 * 4096) = 9821 ∧
      Int.floor (-Real.log 11 * 4096) = -9822) ∧
    Real.log 11 / Real.sqrt 11 < (722992628/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 11) (j := 9821) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (331662479035539984911/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_13 :
    (Int.floor (Real.log 13 * 4096) = 10506 ∧
      Int.floor (-Real.log 13 * 4096) = -10507) ∧
    Real.log 13 / Real.sqrt 13 < (711388956/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 13) (j := 10506) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (360555127546398929311/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_16 :
    (Int.floor (Real.log 16 * 4096) = 11356 ∧
      Int.floor (-Real.log 16 * 4096) = -11357) ∧
    Real.log 2 / Real.sqrt 16 < (173286796/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 16) (j := 11356) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (400000000000000000000/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_17 :
    (Int.floor (Real.log 17 * 4096) = 11604 ∧
      Int.floor (-Real.log 17 * 4096) = -11605) ∧
    Real.log 17 / Real.sqrt 17 < (687155170/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 17) (j := 11604) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (412310562561766054982/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_19 :
    (Int.floor (Real.log 19 * 4096) = 12060 ∧
      Int.floor (-Real.log 19 * 4096) = -12061) ∧
    Real.log 19 / Real.sqrt 19 < (675500630/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 19) (j := 12060) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (435889894354067355223/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_23 :
    (Int.floor (Real.log 23 * 4096) = 12842 ∧
      Int.floor (-Real.log 23 * 4096) = -12843) ∧
    Real.log 23 / Real.sqrt 23 < (653795740/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 23) (j := 12842) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (479583152331271954159/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_25 :
    (Int.floor (Real.log 25 * 4096) = 13184 ∧
      Int.floor (-Real.log 25 * 4096) = -13185) ∧
    Real.log 5 / Real.sqrt 25 < (321887583/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 25) (j := 13184) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (500000000000000000000/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_27 :
    (Int.floor (Real.log 27 * 4096) = 13499 ∧
      Int.floor (-Real.log 27 * 4096) = -13500) ∧
    Real.log 3 / Real.sqrt 27 < (211428034/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 27) (j := 13499) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (519615242270663188058/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_29 :
    (Int.floor (Real.log 29 * 4096) = 13792 ∧
      Int.floor (-Real.log 29 * 4096) = -13793) ∧
    Real.log 29 / Real.sqrt 29 < (625291138/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 29) (j := 13792) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (538516480713450403125/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_31 :
    (Int.floor (Real.log 31 * 4096) = 14065 ∧
      Int.floor (-Real.log 31 * 4096) = -14066) ∧
    Real.log 31 / Real.sqrt 31 < (616762310/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 31) (j := 14065) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (556776436283002192211/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_32 :
    (Int.floor (Real.log 32 * 4096) = 14195 ∧
      Int.floor (-Real.log 32 * 4096) = -14196) ∧
    Real.log 2 / Real.sqrt 32 < (122532268/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 32) (j := 14195) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (565685424949238019520/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_37 :
    (Int.floor (Real.log 37 * 4096) = 14790 ∧
      Int.floor (-Real.log 37 * 4096) = -14791) ∧
    Real.log 37 / Real.sqrt 37 < (593631249/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 37) (j := 14790) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (608276253029821968899/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_41 :
    (Int.floor (Real.log 41 * 4096) = 15210 ∧
      Int.floor (-Real.log 41 * 4096) = -15211) ∧
    Real.log 41 / Real.sqrt 41 < (579962520/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 41) (j := 15210) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (640312423743284868648/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_43 :
    (Int.floor (Real.log 43 * 4096) = 15405 ∧
      Int.floor (-Real.log 43 * 4096) = -15406) ∧
    Real.log 43 / Real.sqrt 43 < (573577641/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 43) (j := 15405) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (655743852430200065234/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_47 :
    (Int.floor (Real.log 47 * 4096) = 15770 ∧
      Int.floor (-Real.log 47 * 4096) = -15771) ∧
    Real.log 47 / Real.sqrt 47 < (561601748/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 47) (j := 15770) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (685565460040104412493/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_49 :
    (Int.floor (Real.log 49 * 4096) = 15940 ∧
      Int.floor (-Real.log 49 * 4096) = -15941) ∧
    Real.log 7 / Real.sqrt 49 < (277987165/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 49) (j := 15940) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (700000000000000000000/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

theorem neutralIV150Prime_53 :
    (Int.floor (Real.log 53 * 4096) = 16262 ∧
      Int.floor (-Real.log 53 * 4096) = -16263) ∧
    Real.log 53 / Real.sqrt 53 < (545361537/1000000000:ℝ) := by
  constructor
  · apply neutralIV147Signed_floor (n := 53) (j := 16262) (by norm_num)
    · apply neutralIV150Exp_lt <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]
  · apply neutralIV147Weight_cap (r := (728010988928051827109/100000000000000000000:ℝ))
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · norm_num
    · apply neutralIV150Lt_exp <;>
        norm_num [neutralIV150S, neutralIV150E, Finset.sum_range_succ, Nat.factorial]

#print axioms neutralIV150Exp_interval
#print axioms neutralIV150Exp_lt
#print axioms neutralIV150Lt_exp
#print axioms neutralIV150Prime_2
#print axioms neutralIV150Prime_3
#print axioms neutralIV150Prime_4
#print axioms neutralIV150Prime_5
#print axioms neutralIV150Prime_7
#print axioms neutralIV150Prime_8
#print axioms neutralIV150Prime_9
#print axioms neutralIV150Prime_11
#print axioms neutralIV150Prime_13
#print axioms neutralIV150Prime_16
#print axioms neutralIV150Prime_17
#print axioms neutralIV150Prime_19
#print axioms neutralIV150Prime_23
#print axioms neutralIV150Prime_25
#print axioms neutralIV150Prime_27
#print axioms neutralIV150Prime_29
#print axioms neutralIV150Prime_31
#print axioms neutralIV150Prime_32
#print axioms neutralIV150Prime_37
#print axioms neutralIV150Prime_41
#print axioms neutralIV150Prime_43
#print axioms neutralIV150Prime_47
#print axioms neutralIV150Prime_49
#print axioms neutralIV150Prime_53

end
end WeilDefect
