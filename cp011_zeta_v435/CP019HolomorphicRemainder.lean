module

public import Zeta.EulerMaclaurin.Continuation
public import Zeta.EulerMaclaurin.ErrorBound
public import Mathlib.Analysis.Calculus.DiffContOnCl

/-!
CP019 genuine original Euler–Maclaurin REMAINDER holomorphy on all
moving complex Cauchy disks around 1/2+i t with radius 1/4.

The original published source ALREADY proves:
 * the t_{M+1} term is entire (finite Pochhammer polynomial and cpow),
 * Complex.differentiableOn_eulerMaclaurinRemainderIoi_cpow for
   original improper remainder, on Re s > 1-p.

Consequently the COMPLETE original zetaRemainder(s,6,256) is holomorphic
on the half-plane Re(s)>-13. Its complex balls with real center 1/2
and radius 1/4 lie entirely inside Re(s)>=1/4.

This source proof candidate removes the separate holomorphy
hypothesis from CP019 Cauchy derivative source transfer.
The only outstanding numerical hypothesis there becomes the
uniform exact Borwein envelope on the complex Cauchy circle.

Real original external Lean v4.35 kernel acceptance PENDING.
-/

@[expose] public section

open Metric

namespace CP019HolomorphicRemainder

noncomputable def sourceCenter (t : ℝ) : ℂ :=
  1 / 2 + Complex.I * (t : ℂ)

private abbrev radius : ℝ := 1 / 4

/-- Genuine original Euler–Maclaurin remainder is holomorphic over
the source half-plane Re(s)>-13. This reuses the original public
improper-remainder differentiability theorem without adding a new
analytic regularity hypothesis. -/
theorem original_remainder_differentiableOn :
    DifferentiableOn ℂ (fun z : ℂ => zetaRemainder z 6 256)
      {z : ℂ | -(13 : ℝ) < z.re} := by
  have hN : (256 : ℂ) ≠ 0 := by norm_num
  have hterm : Differentiable ℂ
      (fun z : ℂ =>
        ((bernoulli 14 : ℝ) / ((14 : ℕ).factorial : ℝ) : ℂ)
          * (ascPochhammer ℂ 13).eval z
          * ((256 : ℂ) ^ (-z - (13 : ℂ)))) :=
    ((differentiable_const _).mul
      (ascPochhammer ℂ 13).differentiable).mul
      ((differentiable_id.neg.sub_const _).const_cpow (Or.inl hN))
  have hrem : DifferentiableOn ℂ
      (fun z : ℂ =>
        Complex.eulerMaclaurinRemainderIoi 14
          (fun y : ℝ => (y : ℂ) ^ (-z)) (256 : ℝ))
      {z : ℂ | -(13 : ℝ) < z.re} := by
    simpa using
      (Complex.differentiableOn_eulerMaclaurinRemainderIoi_cpow 14 256
        (by norm_num))
  have hsum := hterm.differentiableOn.add hrem
  simpa [zetaRemainder] using hsum

/-- Every source radius-1/4 CLOSED disk lies in Re s >= 1/4,
irrespective of the real ordinate, so its closure is safely inside
the genuine original remainder holomorphy half-plane Re s > -13. -/
theorem closed_disk_real_part_ge_quarter (t : ℝ) (z : ℂ)
    (hz : z ∈ closedBall (sourceCenter t) radius) :
    (1 : ℝ) / 4 ≤ z.re := by
  have hd : ‖z - sourceCenter t‖ ≤ radius :=
    mem_closedBall_iff_norm.mp hz
  have hr := Complex.abs_re_le_norm (z - sourceCenter t)
  have hlow := (abs_le.mp (hr.trans hd)).1
  have hc : (sourceCenter t).re = (1 : ℝ) / 2 := by
    simp [sourceCenter]
  have heq : z.re = (z - sourceCenter t).re + (1 : ℝ) / 2 := by
    rw [Complex.sub_re, hc]
    ring
  rw [heq]
  dsimp [radius] at hlow
  linarith

/-- Actual source holomorphy on the disk with boundary continuity:
the real Cauchy integral preconditions from Mathlib are formally
discharged rather than assumed at each t. -/
theorem original_zeta_remainder_diffContOnCl_ball (t : ℝ) :
    DiffContOnCl ℂ (fun z : ℂ => zetaRemainder z 6 256)
      (ball (sourceCenter t) radius) := by
  apply original_remainder_differentiableOn.diffContOnCl_ball
  intro z hz
  have hbound := closed_disk_real_part_ge_quarter t z hz
  change -(13 : ℝ) < z.re
  linarith

end CP019HolomorphicRemainder

#print axioms CP019HolomorphicRemainder.original_remainder_differentiableOn
#print axioms CP019HolomorphicRemainder.closed_disk_real_part_ge_quarter
#print axioms CP019HolomorphicRemainder.original_zeta_remainder_diffContOnCl_ball
