import Mathlib
import Mathlib.Analysis.InnerProductSpace.Projection.Submodule

/-!
MASTER-RECON-V02: abstract Picard-to-gap algebra and half-marker lift.
Proof candidates only until the dedicated Lean workflow passes.
Inverse existence and spectral convergence are separate obligations.
-/

namespace WeilDefect.MasterRecon.V02

open scoped InnerProduct

variable {H K L : Type*}
variable [NormedAddCommGroup H] [NormedSpace ℂ H]
variable [NormedAddCommGroup K] [NormedSpace ℂ K]
variable [NormedAddCommGroup L] [NormedSpace ℂ L]

/-- Typed Woodbury identity at a vector, with explicit inverse equations.
No finite-rank, positivity, or closed-range assumption is hidden here. -/
theorem picard_woodbury_apply
    (A R T : H →L[ℂ] H) (M : K →L[ℂ] H)
    (N : H →L[ℂ] K) (C : K →L[ℂ] K)
    (hR : ∀ y, R (A y) = y)
    (hT : ∀ x, A (T (M x)) + M (N (T (M x))) = M x)
    (hC : ∀ x, C (x + N (R (M x))) = x)
    (x : K) :
    C x = x - N (T (M x)) := by
  let y : H := T (M x)
  have hy0 : A y + M (N y) = M x := hT x
  have hy : M (x - N y) = A y := by
    rw [map_sub, ← hy0]
    abel
  have hc := hC (x - N y)
  rw [hy, hR, sub_add_cancel] at hc
  exact hc

/-- The second resolvent identity, connecting the physical and coefficient
resolvents, again with all inverse equations explicit. -/
theorem coefficient_resolvent_apply
    (S : L →L[ℂ] H) (N : H →L[ℂ] L)
    (T : H →L[ℂ] H) (R : L →L[ℂ] L) (η : ℂ)
    (hT : ∀ x, S (N (T (S x))) + η • T (S x) = S x)
    (hR : ∀ x, R (N (S x) + η • x) = x)
    (x : L) :
    x - N (T (S x)) = η • R x := by
  let y : H := T (S x)
  have hy : S (N y) + η • y = S x := hT x
  have hn : N (S (N y)) + η • N y = N (S x) := by
    simpa only [map_add, map_smul] using congrArg N hy
  have hd : N (S x) - N (S (N y)) = η • N y := by
    rw [← hn]
    abel
  have hh : N (S (x - N y)) + η • (x - N y) = η • x := by
    rw [map_sub, map_sub, hd, smul_sub]
    abel
  calc
    x - N (T (S x)) = R (N (S (x - N y)) + η • (x - N y)) :=
      (hR (x - N y)).symm
    _ = R (η • x) := congrArg R hh
    _ = η • R x := map_smul R η x

section Projection

variable {E F : Type*}
variable [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E]
variable [NormedAddCommGroup F] [NormedSpace ℂ F]

/-- Half-threshold reconstruction in the gap complement.
The extraction and inclusion are kept as explicit typed maps. -/
theorem half_marker_lift_mem_orthogonal
    (G : Submodule ℂ E) [G.HasOrthogonalProjection]
    (ell : E →L[ℂ] F) (i : F →L[ℂ] E) (u : F)
    (h : ell (G.starProjection (i u)) = (1 / 2 : ℂ) • u) :
    G.starProjection (i u) -
      (2 : ℂ) • i (ell (G.starProjection (i u))) ∈ Gᗮ := by
  have hh : (2 : ℂ) • i ((1 / 2 : ℂ) • u) = i u := by
    rw [map_smul, smul_smul]
    norm_num
  rw [h, hh]
  have hp : i u - G.starProjection (i u) ∈ Gᗮ :=
    Submodule.sub_starProjection_mem_orthogonal (i u)
  simpa only [neg_sub] using Gᗮ.neg_mem hp

end Projection

end WeilDefect.MasterRecon.V02

#print axioms WeilDefect.MasterRecon.V02.picard_woodbury_apply
#print axioms WeilDefect.MasterRecon.V02.coefficient_resolvent_apply
#print axioms WeilDefect.MasterRecon.V02.half_marker_lift_mem_orthogonal
