import WeilDefect.MasterRecon.V06D
import Mathlib.MeasureTheory.Group.Integral
import Mathlib.Analysis.Complex.Exponential

/-! V07A: exact Mellin translation and normalized reflected-pair algebra.
This gate uses the original integral, and one common multiplicity weight
on both members of a pair. Actual zeta indexing and bounded Hilbert direct
sum assembly remain separate obligations. -/
namespace WeilDefect.MasterRecon.V07A

open MeasureTheory

noncomputable def mellin (f : ℝ → ℂ) (w : ℂ) : ℂ :=
  ∫ x : ℝ, Complex.exp (w * (x : ℂ)) * f x

def translate (a : ℝ) (f : ℝ → ℂ) : ℝ → ℂ :=
  fun x => f (x - a)

/-- The sign of the phase is fixed by τ_a f(x) = f(x-a).
The Bochner identity itself does not require an integrability assumption;
the actual carrier's integrability is a separate attachment. -/
theorem mellin_translate (f : ℝ → ℂ) (w : ℂ) (a : ℝ) :
    mellin (translate a f) w = Complex.exp (w * (a : ℂ)) * mellin f w := by
  unfold mellin translate
  calc
    (∫ x : ℝ, Complex.exp (w * (x : ℂ)) * f (x - a)) =
        ∫ x : ℝ, (fun y : ℝ => Complex.exp (w * (a : ℂ)) *
          (Complex.exp (w * (y : ℂ)) * f y)) (x - a) := by
      apply integral_congr_ae
      filter_upwards with x
      have h : w * (x : ℂ) = w * (a : ℂ) + w * ((x - a : ℝ) : ℂ) := by
        push_cast
        ring
      rw [h, Complex.exp_add, mul_assoc]
    _ = ∫ y : ℝ, Complex.exp (w * (a : ℂ)) *
          (Complex.exp (w * (y : ℂ)) * f y) :=
      integral_sub_right_eq_self (μ := (volume : Measure ℝ))
        (fun y : ℝ => Complex.exp (w * (a : ℂ)) *
          (Complex.exp (w * (y : ℂ)) * f y)) a
    _ = Complex.exp (w * (a : ℂ)) *
          ∫ y : ℝ, Complex.exp (w * (y : ℂ)) * f y :=
      integral_const_mul _ _

noncomputable def pairPlus (u v : ℂ) : ℂ :=
  (u + v) / (Real.sqrt 2 : ℂ)

noncomputable def pairMinus (u v : ℂ) : ℂ :=
  (u - v) / (Real.sqrt 2 : ℂ)

noncomputable def evenMix (z : ℂ) : ℂ :=
  (Complex.exp z + Complex.exp (-z)) / 2

noncomputable def oddMix (z : ℂ) : ℂ :=
  (Complex.exp z - Complex.exp (-z)) / 2

theorem reflected_pair_mix (u v q z : ℂ) :
    pairPlus (q * Complex.exp z * u) (q * Complex.exp (-z) * v) =
        q * (evenMix z * pairPlus u v + oddMix z * pairMinus u v) ∧
    pairMinus (q * Complex.exp z * u) (q * Complex.exp (-z) * v) =
        q * (oddMix z * pairPlus u v + evenMix z * pairMinus u v) := by
  constructor <;> unfold pairPlus pairMinus evenMix oddMix <;> ring

/-- One common square-root multiplicity weight for the reflected pair. -/
noncomputable def weightedMellin (f : ℝ → ℂ) (m : ℕ) (w : ℂ) : ℂ :=
  (Real.sqrt (m : ℝ) : ℂ) * mellin f w

theorem weighted_mellin_translate (f : ℝ → ℂ) (m : ℕ) (w : ℂ) (a : ℝ) :
    weightedMellin (translate a f) m w =
      Complex.exp (w * (a : ℂ)) * weightedMellin f m w := by
  unfold weightedMellin
  rw [mellin_translate]
  ring

/-- Explicit split of the reflected exponents ±δ+iγ into the common
ordinate phase and opposite real displacements. -/
theorem reflected_exponential_split (δ γ a : ℝ) :
    Complex.exp (((δ : ℂ) + (γ : ℂ) * Complex.I) * (a : ℂ)) =
      Complex.exp ((γ : ℂ) * Complex.I * (a : ℂ)) *
        Complex.exp ((δ : ℂ) * (a : ℂ)) ∧
    Complex.exp (((-(δ : ℂ)) + (γ : ℂ) * Complex.I) * (a : ℂ)) =
      Complex.exp ((γ : ℂ) * Complex.I * (a : ℂ)) *
        Complex.exp (-((δ : ℂ) * (a : ℂ))) := by
  constructor
  · rw [← Complex.exp_add]
    congr 1
    ring
  · rw [← Complex.exp_add]
    congr 1
    ring

theorem reflected_mellin_translation (f : ℝ → ℂ) (m : ℕ) (δ γ a : ℝ) :
    let wp : ℂ := (δ : ℂ) + (γ : ℂ) * Complex.I
    let wm : ℂ := -(δ : ℂ) + (γ : ℂ) * Complex.I
    let q := Complex.exp ((γ : ℂ) * Complex.I * (a : ℂ))
    let z := (δ : ℂ) * (a : ℂ)
    let u := weightedMellin f m wp
    let v := weightedMellin f m wm
    pairPlus (weightedMellin (translate a f) m wp)
        (weightedMellin (translate a f) m wm) =
        q * (evenMix z * pairPlus u v + oddMix z * pairMinus u v) ∧
    pairMinus (weightedMellin (translate a f) m wp)
        (weightedMellin (translate a f) m wm) =
        q * (oddMix z * pairPlus u v + evenMix z * pairMinus u v) := by
  dsimp only
  simp only [weighted_mellin_translate, (reflected_exponential_split δ γ a).1,
    (reflected_exponential_split δ γ a).2]
  exact reflected_pair_mix _ _ _ _

end WeilDefect.MasterRecon.V07A

#print axioms WeilDefect.MasterRecon.V07A.mellin_translate
#print axioms WeilDefect.MasterRecon.V07A.reflected_pair_mix
#print axioms WeilDefect.MasterRecon.V07A.weighted_mellin_translate
#print axioms WeilDefect.MasterRecon.V07A.reflected_exponential_split
#print axioms WeilDefect.MasterRecon.V07A.reflected_mellin_translation
