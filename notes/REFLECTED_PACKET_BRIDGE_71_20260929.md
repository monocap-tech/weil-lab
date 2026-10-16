# RPB-71 — WD-T40 carrier static elaboration audit

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **STATIC API PASS / EVERY LOAD-BEARING CARRIER DECLARATION MATCHES PINNED MATHLIB V4.34 SIGNATURES / THREE ELABORATION-HARDENING EDITS APPLIED / NO STATIC API MISMATCH FOUND / BUILD CERTIFICATION STILL INFRASTRUCTURE-BLOCKED / F-2 REMAINS CLOSED**

## 0. Objective

RPB-70 exhausted the available live build routes before Lean execution.

RPB-71 therefore performs a declaration-by-declaration static audit against the exact pinned toolchain:

~~~text
Lean 4.34.0
mathlib v4.34.0
~~~

The pass does not claim compilation. Its purpose is to eliminate API-shape errors that can be proved from the pinned source without a running elaborator.

## 1. L2 carrier type

The pinned declaration is:

~~~lean
def Lp {α} (E : Type*) ... (p : ℝ≥0∞)
    (μ : Measure α := by volume_tac) : ...
~~~

The carrier now uses the explicit measure:

~~~lean
abbrev RealComplexL2 :=
  MeasureTheory.Lp (α := ℝ) ℂ 2 volume
~~~

This removes reliance on the default volume tactic while remaining exactly the L2 type consumed by mathlib's Fourier instance.

Disposition: PASS.

## 2. MemLp.toLp bridge

Pinned mathlib defines:

~~~lean
def MemLp.toLp (f : α → E) (h_mem_ℒp : MemLp f p μ) : Lp E p μ
~~~

and proves:

~~~lean
MemLp.coeFn_toLp
~~~

The carrier fields

~~~lean
h : ℝ → ℂ
h_memLp : MemLp h 2 volume
kExt_eq_toLp : interface.kExt = h_memLp.toLp h
~~~

match the signature exactly.

Disposition: PASS.

## 3. Abstract WD-T38 adapter

NeutralNullExtensionInterface requires only a normed complex carrier plus endpoint/right observation spaces.

RealComplexL2 supplies the required normed complex structure.

The forgetful adapter

~~~lean
toNeutralNullExtensionInterface
~~~

is a direct projection and introduces no new premise.

The kExt/l2Mode equality proof was hardened from a simplifier-based proof to:

~~~lean
unfold l2Mode
exact d.kExt_eq_toLp
~~~

Disposition: PASS.

## 4. Compact-support representative

Function.support h is definitionally the set of points where h x ≠ 0.

The stored field

~~~lean
support_subset : Function.support h ⊆ Set.Icc (-c) c
~~~

therefore supports the theorem representative_eq_zero_of_not_mem without any imported analytic statement.

Disposition: PASS.

## 5. Lp to tempered-distribution coercion

Pinned mathlib defines:

~~~lean
MeasureTheory.Lp.toTemperedDistribution
~~~

and a CoeHead instance from Lp F p μ into tempered distributions whenever Fact (1 ≤ p) is available.

The carrier coercion

~~~lean
(d.l2Mode : RealComplexTempered)
~~~

has exactly that shape at p = 2 and μ = volume.

Disposition: PASS at declaration-signature level.

## 6. Fourier compatibility

Pinned mathlib v4.34 proves:

~~~lean
MeasureTheory.Lp.fourier_toTemperedDistribution_eq
  (f : Lp (α := E) F 2) :
  𝓕 (f : 𝓢'(E, F)) = (𝓕 f : Lp (α := E) F 2)
~~~

The carrier theorem was hardened to expose the coercions explicitly:

~~~lean
change
  𝓕 (d.l2Mode : RealComplexTempered) =
    ((𝓕 d.l2Mode : RealComplexL2) : RealComplexTempered)
exact MeasureTheory.Lp.fourier_toTemperedDistribution_eq d.l2Mode
~~~

This matches the pinned theorem directly.

Disposition: PASS.

## 7. Distributional residual vanishing

Pinned mathlib defines:

~~~lean
Distribution.IsVanishingOn
~~~

and the monotonicity theorem:

~~~lean
IsVanishingOn.mono
  (hs : s₂ ⊆ s₁)
  (hf : IsVanishingOn f s₁) :
  IsVanishingOn f s₂
~~~

The carrier proof was hardened by naming s₁ and s₂ explicitly rather than relying on metavariable inference.

The interval inclusion uses c < a to prove (-c,c) ⊆ (-a,a), with the negative endpoint reversed correctly by neg_lt_neg.

Disposition: PASS.

## 8. Static audit result

~~~text
Lp type signature:                         PASS
MemLp.toLp signature:                     PASS
WD-T38 adapter shape:                     PASS
support predicate shape:                  PASS
Lp -> tempered coercion declaration:      PASS
L2 Fourier instance declaration:          PASS
tempered Fourier instance declaration:    PASS
fourier_toTemperedDistribution_eq shape:  PASS
IsVanishingOn shape:                      PASS
IsVanishingOn.mono direction:             PASS
~~~

No pinned-API mismatch was found.

Four hardening edits are now present in the carrier source:

1. explicit volume in RealComplexL2;
2. explicit s₁/s₂ in IsVanishingOn.mono;
3. explicit Fourier coercion change and direct theorem application;
4. direct unfold/exact proof for the kExt/l2Mode adapter.

## 9. Remaining uncertainty

Static source inspection cannot certify instance synthesis or tactic elaboration.

The remaining likely compiler-sensitive layer is now narrowed to typeclass synthesis for:

~~~text
Fact (1 ≤ (2 : ℝ≥0∞))
volume.HasTemperateGrowth on ℝ
IsLocallyFiniteMeasure volume
InnerProductSpace ℝ ℝ
FiniteDimensional ℝ ℝ
BorelSpace ℝ
the relevant FourierTransform instances
~~~

These are expected from the pinned mathlib declarations, but RPB-71 does not label them compiler-certified.

## 10. RPB-71 determination

~~~math
\boxed{
\textbf{RPB-71 — THE F-1 CARRIER IS STATICALLY API-CONSISTENT WITH PINNED MATHLIB V4.34 AFTER ELABORATION HARDENING; NO DECLARATION-SHAPE BLOCKER REMAINS.}
}
~~~

F-1 remains source-complete and build-uncertified because no Lean process is available.

F-2 remains unopened.

## Next cursor

~~~text
RPB-72 / WD-T40 CARRIER TYPECLASS SYNTHESIS AUDIT
~~~

The next pass should inspect only the implicit instance requirements needed by the current carrier declarations and determine whether every required instance is present in pinned mathlib v4.34. Do not start F-2.