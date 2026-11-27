import WeilDefect.Arithmetic.ActualZetaIV106E18K2PhysicalMoments
import WeilDefect.Arithmetic.ActualZetaIV106E7PrimeCutoff

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric InnerProductSpace
open scoped SchwartzMap

/-- A smaller rational buffer suffices for every previously eligible cell. -/
def neutralIV106E18LWidth : ℝ := 11/3325
def neutralIV106E18LBuffer : ℝ := 1/10000
def neutralIV106E18LLeft (j : ℕ) : ℝ := -(11/10)+(j:ℝ)*(11/3325)

def neutralIV106E18LEligible (j : ℕ) : Prop :=
  1 ≤ j ∧ j ≤ 663 ∧ j ≠ 35 ∧ j ≠ 36 ∧ j ≠ 76 ∧
  j ≠ 177 ∧ j ≠ 178 ∧ j ≠ 245 ∧ j ≠ 332 ∧ j ≠ 454 ∧ j ≠ 455

/-- Two-sided log bounds from the literal Mathlib atanh-series remainder. -/
theorem neutralIV106E18LLog_bounds :
    (693147180/1000000000:ℝ) ≤ Real.log 2 ∧ Real.log 2 ≤ (693147181/1000000000:ℝ) ∧
    (1098612288/1000000000:ℝ) ≤ Real.log 3 ∧ Real.log 3 ≤ (1098612289/1000000000:ℝ) ∧
    (1386294360/1000000000:ℝ) ≤ Real.log 4 ∧ Real.log 4 ≤ (1386294362/1000000000:ℝ) ∧
    (1609437912/1000000000:ℝ) ≤ Real.log 5 ∧ Real.log 5 ≤ (1609437913/1000000000:ℝ) ∧
    (1945910149/1000000000:ℝ) ≤ Real.log 7 ∧ Real.log 7 ≤ (1945910150/1000000000:ℝ) ∧
    (2079441540/1000000000:ℝ) ≤ Real.log 8 ∧ Real.log 8 ≤ (2079441543/1000000000:ℝ) ∧
    (2197224576/1000000000:ℝ) ≤ Real.log 9 ∧ Real.log 9 ≤ (2197224578/1000000000:ℝ) := by
  have l2 := Real.sum_range_le_log_div (x := (1/3:ℝ)) (by norm_num) (by norm_num) 12
  have u2 := Real.log_div_le_sum_range_add (x := (1/3:ℝ)) (by norm_num) (by norm_num) 12
  have l3 := Real.sum_range_le_log_div (x := (1/5:ℝ)) (by norm_num) (by norm_num) 12
  have u3 := Real.log_div_le_sum_range_add (x := (1/5:ℝ)) (by norm_num) (by norm_num) 12
  have l5 := Real.sum_range_le_log_div (x := (1/9:ℝ)) (by norm_num) (by norm_num) 12
  have u5 := Real.log_div_le_sum_range_add (x := (1/9:ℝ)) (by norm_num) (by norm_num) 12
  have l7 := Real.sum_range_le_log_div (x := (3/11:ℝ)) (by norm_num) (by norm_num) 12
  have u7 := Real.log_div_le_sum_range_add (x := (3/11:ℝ)) (by norm_num) (by norm_num) 12
  norm_num [Finset.sum_range_succ] at l2 u2 l3 u3 l5 u5 l7 u7
  have e3 : Real.log 3 = Real.log 2 + Real.log (3/2) := by
    rw [← Real.log_mul (by norm_num) (by norm_num)]; norm_num
  have e5 : Real.log 5 = 2*Real.log 2 + Real.log (5/4) := by
    rw [← Real.log_pow, ← Real.log_mul (by norm_num) (by norm_num)]; norm_num
  have e7 : Real.log 7 = 2*Real.log 2 + Real.log (7/4) := by
    rw [← Real.log_pow, ← Real.log_mul (by norm_num) (by norm_num)]; norm_num
  have e4 : Real.log 4 = 2*Real.log 2 := by
    rw [← Real.log_pow]; norm_num
  have e8 : Real.log 8 = 3*Real.log 2 := by
    rw [← Real.log_pow]; norm_num
  have e9 : Real.log 9 = 2*Real.log 3 := by
    rw [← Real.log_pow]; norm_num
  rw [e4,e8,e9,e3,e5,e7]
  refine ⟨?_,?_,?_,?_,?_,?_,?_,?_,?_,?_,?_,?_,?_,?_⟩ <;>
    linarith only [l2,u2,l3,u3,l5,u5,l7,u7]

/-- A point in the buffered ball has literal rational endpoint inequalities. -/
theorem neutralIV106E18LBall (j : ℕ) (y : ℝ)
    (hy : y ∈ closedBall (neutralIV106E18LLeft j+neutralIV106E18LWidth/2)
      (neutralIV106E18LWidth/2+neutralIV106E18LBuffer)) :
    neutralIV106E18LLeft j-1/10000 ≤ y ∧
      y ≤ neutralIV106E18LLeft j+11/3325+1/10000 := by
  rw [mem_closedBall,Real.dist_eq,abs_le] at hy
  unfold neutralIV106E18LWidth neutralIV106E18LBuffer at hy
  constructor <;> linarith [hy.1,hy.2]

theorem neutralIV106E18LWindow (j : ℕ) (hj : neutralIV106E18LEligible j) :
    closedBall (neutralIV106E18LLeft j+neutralIV106E18LWidth/2)
      (neutralIV106E18LWidth/2+neutralIV106E18LBuffer) ⊆
      Set.Icc (-(11/10:ℝ)) (11/10) := by
  intro y hy
  obtain ⟨hyL,hyU⟩ := neutralIV106E18LBall j y hy
  have hjL : (1:ℝ) ≤ (j:ℝ) := by exact_mod_cast hj.1
  have hjU : (j:ℝ) ≤ 663 := by exact_mod_cast hj.2.1
  unfold neutralIV106E18LLeft at hyL hyU
  exact ⟨by linarith only [hjL,hyL], by linarith only [hjU,hyU]⟩

theorem neutralIV106E18LGap (j : ℕ) (hj : neutralIV106E18LEligible j)
    (x : ℝ) (hx : x ∈ Set.Icc (4393/4000:ℝ) (4399/4000))
    (y : ℝ) (hy : y ∈ closedBall (neutralIV106E18LLeft j+neutralIV106E18LWidth/2)
      (neutralIV106E18LWidth/2+neutralIV106E18LBuffer)) :
    (1/10000:ℝ) ≤ |x-y| := by
  obtain ⟨_,hyU⟩ := neutralIV106E18LBall j y hy
  have hjU : (j:ℝ) ≤ 663 := by exact_mod_cast hj.2.1
  unfold neutralIV106E18LLeft at hyU
  have hh : (1/10000:ℝ) ≤ x-y := by linarith only [hx.1,hyU,hjU]
  exact hh.trans (le_abs_self _)

/-- Seven compressed integer interval tests replace 654 individual real proofs. -/
theorem neutralIV106E18LPlus (j : ℕ) (hj : neutralIV106E18LEligible j)
    (n : ℕ) (hn : n ∈ ({2,3,4,5,7,8,9}:Finset ℕ))
    (y : ℝ) (hy : y ∈ closedBall (neutralIV106E18LLeft j+neutralIV106E18LWidth/2)
      (neutralIV106E18LWidth/2+neutralIV106E18LBuffer)) :
    y+Real.log n < (4393/4000:ℝ) ∨ (4399/4000:ℝ) < y+Real.log n := by
  obtain ⟨hyL,hyU⟩ := neutralIV106E18LBall j y hy
  obtain ⟨h2l,h2u,h3l,h3u,h4l,h4u,h5l,h5u,h7l,h7u,h8l,h8u,h9l,h9u⟩ := neutralIV106E18LLog_bounds
  have hj1 := hj.1
  have hj2 := hj.2.1
  have he : j ≠ 35 ∧ j ≠ 36 ∧ j ≠ 76 ∧ j ≠ 177 ∧ j ≠ 178 ∧
    j ≠ 245 ∧ j ≠ 332 ∧ j ≠ 454 ∧ j ≠ 455 := hj.2.2
  obtain ⟨he35,he36,he76,he177,he178,he245,he332,he454,he455⟩ := he
  simp only [Finset.mem_insert, Finset.mem_singleton] at hn
  rcases hn with rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · have hl : (693147180/1000000000:ℝ) ≤ Real.log 2 := h2l
    have hu : Real.log 2 ≤ (693147181/1000000000:ℝ) := h2u
    have hjc : j ≤ 453 ∨ 456 ≤ j := by omega
    rcases hjc with hp | hp
    · left
      have hp' : (j:ℝ) ≤ 453 := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyU
      linarith only [hyU,hu,hp']
    · right
      have hp' : (456:ℝ) ≤ (j:ℝ) := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyL
      linarith only [hyL,hl,hp']
  · have hl : (1098612288/1000000000:ℝ) ≤ Real.log 3 := h3l
    have hu : Real.log 3 ≤ (1098612289/1000000000:ℝ) := h3u
    have hjc : j ≤ 331 ∨ 333 ≤ j := by omega
    rcases hjc with hp | hp
    · left
      have hp' : (j:ℝ) ≤ 331 := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyU
      linarith only [hyU,hu,hp']
    · right
      have hp' : (333:ℝ) ≤ (j:ℝ) := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyL
      linarith only [hyL,hl,hp']
  · have hl : (1386294360/1000000000:ℝ) ≤ Real.log 4 := h4l
    have hu : Real.log 4 ≤ (1386294362/1000000000:ℝ) := h4u
    have hjc : j ≤ 244 ∨ 246 ≤ j := by omega
    rcases hjc with hp | hp
    · left
      have hp' : (j:ℝ) ≤ 244 := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyU
      linarith only [hyU,hu,hp']
    · right
      have hp' : (246:ℝ) ≤ (j:ℝ) := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyL
      linarith only [hyL,hl,hp']
  · have hl : (1609437912/1000000000:ℝ) ≤ Real.log 5 := h5l
    have hu : Real.log 5 ≤ (1609437913/1000000000:ℝ) := h5u
    have hjc : j ≤ 176 ∨ 179 ≤ j := by omega
    rcases hjc with hp | hp
    · left
      have hp' : (j:ℝ) ≤ 176 := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyU
      linarith only [hyU,hu,hp']
    · right
      have hp' : (179:ℝ) ≤ (j:ℝ) := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyL
      linarith only [hyL,hl,hp']
  · have hl : (1945910149/1000000000:ℝ) ≤ Real.log 7 := h7l
    have hu : Real.log 7 ≤ (1945910150/1000000000:ℝ) := h7u
    have hjc : j ≤ 75 ∨ 77 ≤ j := by omega
    rcases hjc with hp | hp
    · left
      have hp' : (j:ℝ) ≤ 75 := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyU
      linarith only [hyU,hu,hp']
    · right
      have hp' : (77:ℝ) ≤ (j:ℝ) := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyL
      linarith only [hyL,hl,hp']
  · have hl : (2079441540/1000000000:ℝ) ≤ Real.log 8 := h8l
    have hu : Real.log 8 ≤ (2079441543/1000000000:ℝ) := h8u
    have hjc : j ≤ 34 ∨ 37 ≤ j := by omega
    rcases hjc with hp | hp
    · left
      have hp' : (j:ℝ) ≤ 34 := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyU
      linarith only [hyU,hu,hp']
    · right
      have hp' : (37:ℝ) ≤ (j:ℝ) := by exact_mod_cast hp
      unfold neutralIV106E18LLeft at hyL
      linarith only [hyL,hl,hp']
  · have hl : (2197224576/1000000000:ℝ) ≤ Real.log 9 := h9l
    have hu : Real.log 9 ≤ (2197224578/1000000000:ℝ) := h9u
    right
    have hjr : (1:ℝ) ≤ (j:ℝ) := by exact_mod_cast hj.1
    unfold neutralIV106E18LLeft at hyL
    linarith only [hyL,hl,hjr]

theorem neutralIV106E18LShift (j : ℕ) (hj : neutralIV106E18LEligible j)
    (n : ℕ) (hn : n ∈ rightLimitPrimePowerFinset (11/10:ℝ))
    (y : ℝ) (hy : y ∈ closedBall (neutralIV106E18LLeft j+neutralIV106E18LWidth/2)
      (neutralIV106E18LWidth/2+neutralIV106E18LBuffer)) :
    y-Real.log n ∉ Set.Icc (4393/4000:ℝ) (4399/4000) ∧
    y+Real.log n ∉ Set.Icc (4393/4000:ℝ) (4399/4000) := by
  rw [neutralIV106E7Inventory] at hn
  have hplus := neutralIV106E18LPlus j hj n hn y hy
  have hwindow := neutralIV106E18LWindow j hj hy
  have hn2 : (2:ℕ) ≤ n := by
    simp only [Finset.mem_insert,Finset.mem_singleton] at hn
    omega
  have hn2r : (2:ℝ) ≤ (n:ℝ) := by exact_mod_cast hn2
  have hlog := Real.log_le_log (by norm_num : (0:ℝ)<2) hn2r
  have hl := neutralIV106E18LLog_bounds.1
  constructor
  · intro hx
    linarith only [hwindow.2,hlog,hl,hx.1]
  · intro hx
    rcases hplus with hp | hp <;> linarith [hx.1,hx.2]

/-- Actual IV105C row on every eligible E18A polynomial, without additional
density, support, shift, or moment premises. Upstream native gates retained. -/
theorem neutralIV106E18LResponse (k : ℕ) (hk : 0 < k) (i : Fin k)
    (j : ℕ) (hj : neutralIV106E18LEligible j) :
    inner ℂ (neutralIV105CResponse k hk i)
      ((neutralIV106E18JTrial_memLp (neutralIV106E18LLeft j)
        neutralIV106E18LWidth (by norm_num [neutralIV106E18LWidth])).toLp _) =
    ∫ x, conj (neutralIV100Carrier k hk i x) *
      (∫ y, neutralIV106E18ITrial (neutralIV106E18LLeft j) neutralIV106E18LWidth y *
        ((-(Real.exp (-|x-y|/2)/(1-Real.exp (-2*|x-y|))) : ℝ) : ℂ)) := by
  exact neutralIV106E18K2Trial_response k hk i (neutralIV106E18LLeft j)
    neutralIV106E18LWidth neutralIV106E18LBuffer
    (by norm_num [neutralIV106E18LWidth]) (by norm_num [neutralIV106E18LBuffer])
    (neutralIV106E18LWindow j hj) (δ := 1/10000) (by norm_num)
    (neutralIV106E18LGap j hj) (neutralIV106E18LShift j hj)

#print axioms neutralIV106E18LLog_bounds
#print axioms neutralIV106E18LBall
#print axioms neutralIV106E18LWindow
#print axioms neutralIV106E18LGap
#print axioms neutralIV106E18LPlus
#print axioms neutralIV106E18LShift
#print axioms neutralIV106E18LResponse
end
end WeilDefect
