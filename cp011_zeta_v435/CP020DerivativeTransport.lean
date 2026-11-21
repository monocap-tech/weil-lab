module

public import CP020BorweinCircle
public import Zeta.EulerMaclaurin.Continuation
public import Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas

/-!
CP020: TRANSPORT the original published Euler–Maclaurin IDENTITY
  riemannZeta s = zetaApproximant s 6 256 + zetaRemainder s 6 256
to derivative order k for ALL k, by equality of holomorphic germs
in the true source domain, not by differentiation of a VALUE-ERROR
inequality.

The original Zeta equality is already published as
  riemannZeta_eq_approximant_add_remainder
on {Re s > -13} \ {1}. This domain is open. Actual original Mathlib
Filter.EventuallyEq.iteratedDeriv_eq guarantees equality of the
k-th complex iterated derivatives of equal germs.

Combining with CP020's source circle Cauchy bound gives UNIFORM
derivative errors for the genuine original zeta approximant:
‖D^k(riemannZeta-zetaApproximant) (1/2+i t)‖
 ≤ k!*(3e-13)/(1/4)^k, t in [149.5,150.05353].

All new declarations are LEAN SOURCE CANDIDATES until compiled
under the actual original Zeta 4.35 kernel. This does not yet
bound the ENTIRE Hardy-Z phase derivative / curvature, or prove
the original CP010 narrow numerical zeta zero.
-/

@[expose] public section

open Filter Set

namespace CP020DerivativeTransport

private abbrev a : ℝ := (149500 : ℝ) / 1000
private abbrev b : ℝ := (15005353 : ℝ) / 100000
private noncomputable def sourceCenter (t : ℝ) : ℂ :=
  1 / 2 + Complex.I * (t : ℂ)

/-- The correct ORIGINAL published EM equality is an equality of
germs near EVERY non-pole complex point Re s > -13.  Both sides are
source functions, not approximate numerical arrays. -/
theorem original_zeta_EM_germs_equal
    {s : ℂ} (hre : -(13 : ℝ) < s.re) (hpole : s ≠ 1) :
    (fun z : ℂ => riemannZeta z - zetaApproximant z 6 256)
      =ᶠ[nhds s]
    (fun z : ℂ => zetaRemainder z 6 256) := by
  let U : Set ℂ := {z : ℂ | -(13 : ℝ) < z.re} \ {1}
  have hU : IsOpen U :=
    (isOpen_lt continuous_const Complex.continuous_re).sdiff
      isClosed_singleton
  have hs : s ∈ U := ⟨hre, hpole⟩
  filter_upwards [hU.mem_nhds hs] with z hz
  have horiginal :=
    riemannZeta_eq_approximant_add_remainder z 6 256
      (by norm_num) hz.1 hz.2
  dsimp
  rw [horiginal]
  ring

/-- All COMPLEX derivative orders of original ζ−EM approximant equal
the corresponding ORIGINAL holomorphic remainder derivatives.
No differentiated inequality, no new approximation of ζ, and no
extra derivative regularity assumption. -/
theorem original_zeta_EM_derivative_error_identity
    (k : ℕ) {s : ℂ} (hre : -(13 : ℝ) < s.re) (hpole : s ≠ 1) :
    iteratedDeriv k
        (fun z : ℂ => riemannZeta z - zetaApproximant z 6 256) s
      =
    iteratedDeriv k
        (fun z : ℂ => zetaRemainder z 6 256) s := by
  exact Filter.EventuallyEq.iteratedDeriv_eq k
    (original_zeta_EM_germs_equal hre hpole)

/-- The actual source height centers remain away from the zeta pole,
with Re=1/2. This exact arithmetic premise is independent of a
numerical Hardy-Z source sign test. -/
theorem original_center_valid (t : ℝ) :
    -(13 : ℝ) < (sourceCenter t).re ∧
      sourceCenter t ≠ 1 := by
  have hreal : (sourceCenter t).re = (1 : ℝ) / 2 := by
    simp [sourceCenter]
  constructor
  · rw [hreal]
    norm_num
  · intro h
    have hre := congrArg Complex.re h
    rw [hreal] at hre
    norm_num at hre

/-- MAIN SOURCE-TRANSPORT theorem: for EVERY t in the frozen
interval and EVERY complex derivative order k, original actual
ζ−A_6,256 error obeys the SAME Cauchy cap as actual original
R_6,256, once CP020BorweinCircle is accepted by a genuine kernel. -/
theorem original_zeta_approximant_derivative_error_all_heights
    (t : ℝ) (ht : t ∈ Icc a b) (k : ℕ) :
    ‖iteratedDeriv k
      (fun z : ℂ => riemannZeta z - zetaApproximant z 6 256)
      (sourceCenter t)‖ ≤
      (k.factorial : ℝ) *
        ((3 : ℝ) / (10 : ℝ) ^ 13) /
        ((1 : ℝ) / 4) ^ k := by
  obtain ⟨hre, hpole⟩ := original_center_valid t
  rw [original_zeta_EM_derivative_error_identity k hre hpole]
  have h := CP020BorweinCircle.original_EM_Cauchy_all_heights t ht k
  simpa [sourceCenter] using h

/-- The source original ζ approximation therefore has an exact,
fully specified order-three error ≤1.152×10^-10 throughout the
target interval, once ALL new Lean modules actually compile. -/
theorem original_zeta_approximant_third_derivative_error_all_heights
    (t : ℝ) (ht : t ∈ Icc a b) :
    ‖iteratedDeriv 3
        (fun z : ℂ =>
          riemannZeta z - zetaApproximant z 6 256)
        (sourceCenter t)‖ ≤
      (1152 : ℝ) / (10 : ℝ) ^ 13 := by
  have h := original_zeta_approximant_derivative_error_all_heights
    t ht 3
  convert h using 1 <;> norm_num [Nat.factorial]

end CP020DerivativeTransport

#print axioms CP020DerivativeTransport.original_zeta_EM_germs_equal
#print axioms CP020DerivativeTransport.original_zeta_EM_derivative_error_identity
#print axioms CP020DerivativeTransport.original_center_valid
#print axioms CP020DerivativeTransport.original_zeta_approximant_derivative_error_all_heights
#print axioms CP020DerivativeTransport.original_zeta_approximant_third_derivative_error_all_heights
