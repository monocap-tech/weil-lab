module

public import Zeta.EulerMaclaurin.Continuation
public import Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas

/-!
CP021 LEAF SOURCE-GERM KERNEL RECOVERY: import only genuine frozen
external Zeta@v1-1e6 (Lean v4.35) and original Mathlib.
NO CP011–CP020 new local theorem imports whatsoever.

Original source publishes identity ζ=A_M,N+R_M,N on complex OPEN
half-plane away from the pole. Equality of germs implies equality
of iterated COMPLEX derivatives for all k by true Mathlib theorem.
This is an unconditional mathematical identity, independent of
ANY numerical Borwein bound or prior CP020 local Lean proof.
Three new source candidates can be compiled independently.
-/

@[expose] public section

open Filter Set

namespace CP021GermLeaf

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

end CP021GermLeaf

#print axioms CP021GermLeaf.original_zeta_EM_germs_equal
#print axioms CP021GermLeaf.original_zeta_EM_derivative_error_identity
#print axioms CP021GermLeaf.original_center_valid
