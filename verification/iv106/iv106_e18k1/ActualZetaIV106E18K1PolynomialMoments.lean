import Mathlib

namespace WeilDefect
noncomputable section
open MeasureTheory

def neutralIV106E18K1B (t : ℝ) : ℝ := t^5*(1-t)^5

def neutralIV106E18K1B1 (t : ℝ) : ℝ :=
  5*t^4*(1-t)^5 - 5*t^5*(1-t)^4

def neutralIV106E18K1B2 (t : ℝ) : ℝ :=
  20*t^3*(1-t)^5 - 50*t^4*(1-t)^4 + 20*t^5*(1-t)^3

def neutralIV106E18K1B3 (t : ℝ) : ℝ :=
  60*t^2*(1-t)^5 - 300*t^3*(1-t)^4 +
  300*t^4*(1-t)^3 - 60*t^5*(1-t)^2

def neutralIV106E18K1Poly (h t : ℝ) : ℝ :=
  neutralIV106E18K1B3 t - h^2/4 * neutralIV106E18K1B1 t

theorem neutralIV106E18K1Jets (t : ℝ) :
    HasDerivAt neutralIV106E18K1B (neutralIV106E18K1B1 t) t ∧
    HasDerivAt neutralIV106E18K1B1 (neutralIV106E18K1B2 t) t ∧
    HasDerivAt neutralIV106E18K1B2 (neutralIV106E18K1B3 t) t := by
  have ht : HasDerivAt (fun x : ℝ => x) 1 t := hasDerivAt_id t
  have hu : HasDerivAt (fun x : ℝ => 1-x) (-1) t := by
    simpa using (hasDerivAt_const t (1:ℝ)).sub ht
  refine ⟨?_, ?_, ?_⟩
  · unfold neutralIV106E18K1B neutralIV106E18K1B1
    convert (ht.pow 5).mul (hu.pow 5) using 1 <;> ring
  · unfold neutralIV106E18K1B1 neutralIV106E18K1B2
    convert (((ht.pow 4).mul (hu.pow 5)).const_mul 5).sub
      (((ht.pow 5).mul (hu.pow 4)).const_mul 5) using 1 <;> ring
  · unfold neutralIV106E18K1B2 neutralIV106E18K1B3
    convert ((((ht.pow 3).mul (hu.pow 5)).const_mul 20).sub
      (((ht.pow 4).mul (hu.pow 4)).const_mul 50)).add
      (((ht.pow 5).mul (hu.pow 3)).const_mul 20) using 1 <;> ring

theorem neutralIV106E18K1Endpoints :
    neutralIV106E18K1B 0 = 0 ∧ neutralIV106E18K1B 1 = 0 ∧
    neutralIV106E18K1B1 0 = 0 ∧ neutralIV106E18K1B1 1 = 0 ∧
    neutralIV106E18K1B2 0 = 0 ∧ neutralIV106E18K1B2 1 = 0 := by
  norm_num [neutralIV106E18K1B, neutralIV106E18K1B1, neutralIV106E18K1B2]

/-- A single exact derivative identity replaces three successive IBP
rewrites. The coefficient is retained for general exponential rates. -/
def neutralIV106E18K1Primitive (h q t : ℝ) : ℝ :=
  Real.exp (q*t) * (neutralIV106E18K1B2 t -
    q*neutralIV106E18K1B1 t + (q^2-h^2/4)*neutralIV106E18K1B t)

theorem neutralIV106E18K1Primitive_deriv (h q t : ℝ) :
    HasDerivAt (neutralIV106E18K1Primitive h q)
      (Real.exp (q*t) * (neutralIV106E18K1Poly h t +
        q*(q^2-h^2/4)*neutralIV106E18K1B t)) t := by
  obtain ⟨hb,hb1,hb2⟩ := neutralIV106E18K1Jets t
  have he := ((hasDerivAt_id t).const_mul q).exp
  unfold neutralIV106E18K1Primitive neutralIV106E18K1Poly
  convert he.mul ((hb2.sub (hb1.const_mul q)).add
    (hb.const_mul (q^2-h^2/4))) using 1 <;> ring

theorem neutralIV106E18K1Transform (h q : ℝ) :
    (∫ t in (0:ℝ)..1, Real.exp (q*t)*neutralIV106E18K1Poly h t) =
      (-q^3+h^2*q/4) *
        (∫ t in (0:ℝ)..1, Real.exp (q*t)*neutralIV106E18K1B t) := by
  let f : ℝ → ℝ := fun t => Real.exp (q*t)*neutralIV106E18K1Poly h t
  let g : ℝ → ℝ := fun t => Real.exp (q*t)*neutralIV106E18K1B t
  let C : ℝ := q*(q^2-h^2/4)
  have hf : Continuous f := by
    dsimp [f,neutralIV106E18K1Poly,neutralIV106E18K1B3,neutralIV106E18K1B1]
    fun_prop
  have hg : Continuous g := by dsimp [g,neutralIV106E18K1B]; fun_prop
  have hd (t : ℝ) : HasDerivAt (neutralIV106E18K1Primitive h q)
      (f t+C*g t) t := by
    convert neutralIV106E18K1Primitive_deriv h q t using 1 <;>
      dsimp [f,g,C] <;> ring
  have he := intervalIntegral.integral_eq_sub_of_hasDerivAt
    (a := (0:ℝ)) (b := 1) (fun t _ => hd t)
    ((hf.add (continuous_const.mul hg)).intervalIntegrable (μ := volume) 0 1)
  have hz : neutralIV106E18K1Primitive h q 1 -
      neutralIV106E18K1Primitive h q 0 = 0 := by
    norm_num [neutralIV106E18K1Primitive,neutralIV106E18K1B,
      neutralIV106E18K1B1,neutralIV106E18K1B2]
  rw [hz,intervalIntegral.integral_add
    (hf.intervalIntegrable (μ := volume) 0 1)
    ((continuous_const.mul hg).intervalIntegrable (μ := volume) 0 1),
    intervalIntegral.integral_const_mul] at he
  change (∫ t in (0:ℝ)..1, f t) =
    (-q^3+h^2*q/4)*(∫ t in (0:ℝ)..1, g t)
  dsimp [C] at he
  linear_combination he

theorem neutralIV106E18K1Zero (h q : ℝ)
    (hq : q = 0 ∨ q = h/2 ∨ q = -h/2) :
    (∫ t in (0:ℝ)..1, Real.exp (q*t)*neutralIV106E18K1Poly h t) = 0 := by
  rw [neutralIV106E18K1Transform]
  rcases hq with rfl | rfl | rfl <;> ring

#print axioms neutralIV106E18K1Jets
#print axioms neutralIV106E18K1Endpoints
#print axioms neutralIV106E18K1Primitive_deriv
#print axioms neutralIV106E18K1Transform
#print axioms neutralIV106E18K1Zero
end
end WeilDefect
