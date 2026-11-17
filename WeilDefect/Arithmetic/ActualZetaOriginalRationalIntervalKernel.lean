import Mathlib

namespace WeilDefect
noncomputable section

/-! NF591: an exact rational enclosure kernel. Soundness is
independent of the fixed precision chosen by the external replay.
No floating point, no Arb primitive, no axiom of interval custody. -/

structure NF591Ball where
  mid : ℚ
  rad : ℚ
  deriving Repr

def NF591Ball.Contains (b : NF591Ball) (x : ℝ) : Prop :=
  |x-(b.mid:ℝ)| ≤ (b.rad:ℝ)

def NF591Ball.add (a b : NF591Ball) : NF591Ball :=
  ⟨a.mid+b.mid,a.rad+b.rad⟩

def NF591Ball.neg (a : NF591Ball) : NF591Ball :=
  ⟨-a.mid,a.rad⟩

def NF591Ball.mul (a b : NF591Ball) : NF591Ball :=
  ⟨a.mid*b.mid,|a.mid| * b.rad+|b.mid| * a.rad+a.rad*b.rad⟩

def NF591Ball.divPos (a : NF591Ball) (d : ℚ) : NF591Ball :=
  ⟨a.mid/d,a.rad/d⟩

theorem NF591Ball.contains_add {a b : NF591Ball} {x y : ℝ}
    (hx : a.Contains x) (hy : b.Contains y) : (a.add b).Contains (x+y) := by
  unfold Contains at *
  simp only [add,Rat.cast_add]
  calc
    |x+y-((a.mid:ℝ)+(b.mid:ℝ))| =
        |(x-(a.mid:ℝ))+(y-(b.mid:ℝ))| := by congr 1 <;> ring
    _ ≤ |x-(a.mid:ℝ)|+|y-(b.mid:ℝ)| := abs_add_le _ _
    _ ≤ _ := add_le_add hx hy

theorem NF591Ball.contains_neg {a : NF591Ball} {x : ℝ} (hx : a.Contains x) :
    a.neg.Contains (-x) := by
  unfold Contains at *
  simp only [neg,Rat.cast_neg]
  rw [show -x-(-(a.mid:ℝ))=-(x-(a.mid:ℝ)) by ring,abs_neg]
  exact hx

theorem NF591Ball.contains_mul {a b : NF591Ball} {x y : ℝ}
    (hx : a.Contains x) (hy : b.Contains y) : (a.mul b).Contains (x*y) := by
  unfold Contains at *
  simp only [mul,Rat.cast_add,Rat.cast_mul,Rat.cast_abs]
  let u := x-(a.mid:ℝ)
  let v := y-(b.mid:ℝ)
  have ha : 0 ≤ (a.rad:ℝ) := (abs_nonneg _).trans hx
  have hb : 0 ≤ (b.rad:ℝ) := (abs_nonneg _).trans hy
  have hu : |u| ≤ (a.rad:ℝ) := hx
  have hv : |v| ≤ (b.rad:ℝ) := hy
  calc
    |x*y-(a.mid:ℝ)*(b.mid:ℝ)| =
        |(a.mid:ℝ)*v+(b.mid:ℝ)*u+u*v| := by congr 1 <;> dsimp [u,v] <;> ring
    _ ≤ |(a.mid:ℝ)*v+(b.mid:ℝ)*u|+|u*v| := abs_add_le _ _
    _ ≤ (|(a.mid:ℝ)*v|+|(b.mid:ℝ)*u|)+|u*v| :=
      add_le_add (abs_add_le _ _) le_rfl
    _ ≤ _ := by
      simp only [abs_mul]
      exact add_le_add
        (add_le_add (mul_le_mul_of_nonneg_left hv (abs_nonneg _))
          (mul_le_mul_of_nonneg_left hu (abs_nonneg _)))
        (mul_le_mul hu hv (abs_nonneg _) ha)

theorem NF591Ball.contains_divPos {a : NF591Ball} {x : ℝ} {d : ℚ}
    (hx : a.Contains x) (hd : 0 < d) : (a.divPos d).Contains (x/(d:ℝ)) := by
  unfold Contains at *
  simp only [divPos,Rat.cast_div]
  rw [← sub_div,abs_div,abs_of_pos (show (0:ℝ)<(d:ℝ) by exact_mod_cast hd)]
  exact div_le_div_of_nonneg_right hx (by exact_mod_cast hd.le)

/-- A checked rational widening can include rounding of both center
and radius. This is the only permission to discard exact digits. -/
def NF591Ball.Widens (a b : NF591Ball) : Prop :=
  |a.mid-b.mid|+a.rad ≤ b.rad

theorem NF591Ball.contains_widen {a b : NF591Ball} {x : ℝ}
    (hx : a.Contains x) (h : a.Widens b) : b.Contains x := by
  unfold Contains at *
  have hc : |(a.mid:ℝ)-(b.mid:ℝ)|+(a.rad:ℝ) ≤ (b.rad:ℝ) := by
    exact_mod_cast h
  calc
    |x-(b.mid:ℝ)| = |(x-(a.mid:ℝ))+((a.mid:ℝ)-(b.mid:ℝ))| := by congr 1 <;> ring
    _ ≤ |x-(a.mid:ℝ)|+|(a.mid:ℝ)-(b.mid:ℝ)| := abs_add_le _ _
    _ ≤ _ := by linarith

theorem NF591Ball.contains_abs_bound {a : NF591Ball} {x : ℝ} (hx : a.Contains x) :
    |x| ≤ (|a.mid|+a.rad:ℚ) := by
  unfold Contains at hx
  push_cast
  calc
    |x| = |(x-(a.mid:ℝ))+(a.mid:ℝ)| := by rw [sub_add_cancel]
    _ ≤ |x-(a.mid:ℝ)|+|(a.mid:ℝ)| := abs_add_le _ _
    _ ≤ _ := by linarith

structure NF591Rect where
  re : NF591Ball
  im : NF591Ball

def NF591Rect.Contains (a : NF591Rect) (z : ℂ) : Prop :=
  a.re.Contains z.re ∧ a.im.Contains z.im

def NF591Rect.add (a b : NF591Rect) : NF591Rect :=
  ⟨a.re.add b.re,a.im.add b.im⟩

def NF591Rect.neg (a : NF591Rect) : NF591Rect :=
  ⟨a.re.neg,a.im.neg⟩

def NF591Rect.mul (a b : NF591Rect) : NF591Rect :=
  ⟨(a.re.mul b.re).add (a.im.mul b.im).neg,
    (a.re.mul b.im).add (a.im.mul b.re)⟩

def NF591Rect.divPos (a : NF591Rect) (d : ℚ) : NF591Rect :=
  ⟨a.re.divPos d,a.im.divPos d⟩

theorem NF591Rect.contains_add {a b : NF591Rect} {z w : ℂ}
    (hz : a.Contains z) (hw : b.Contains w) : (a.add b).Contains (z+w) := by
  exact ⟨by simpa only [add,Complex.add_re] using NF591Ball.contains_add hz.1 hw.1,
    by simpa only [add,Complex.add_im] using NF591Ball.contains_add hz.2 hw.2⟩

theorem NF591Rect.contains_neg {a : NF591Rect} {z : ℂ}
    (hz : a.Contains z) : a.neg.Contains (-z) := by
  exact ⟨by simpa only [neg,Complex.neg_re] using NF591Ball.contains_neg hz.1,
    by simpa only [neg,Complex.neg_im] using NF591Ball.contains_neg hz.2⟩

theorem NF591Rect.contains_mul {a b : NF591Rect} {z w : ℂ}
    (hz : a.Contains z) (hw : b.Contains w) : (a.mul b).Contains (z*w) := by
  constructor
  · simpa only [mul,Complex.mul_re,sub_eq_add_neg] using
      NF591Ball.contains_add (NF591Ball.contains_mul hz.1 hw.1)
        (NF591Ball.contains_neg (NF591Ball.contains_mul hz.2 hw.2))
  · simpa only [mul,Complex.mul_im,add_comm] using
      NF591Ball.contains_add (NF591Ball.contains_mul hz.1 hw.2)
        (NF591Ball.contains_mul hz.2 hw.1)

def NF591Rect.Widens (a b : NF591Rect) : Prop :=
  a.re.Widens b.re ∧ a.im.Widens b.im

theorem NF591Rect.contains_widen {a b : NF591Rect} {z : ℂ}
    (hz : a.Contains z) (h : a.Widens b) : b.Contains z :=
  ⟨NF591Ball.contains_widen hz.1 h.1,NF591Ball.contains_widen hz.2 h.2⟩

end
end WeilDefect
