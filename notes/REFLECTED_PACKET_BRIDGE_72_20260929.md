# RPB-72 — WD-T40 carrier typeclass synthesis audit

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **TYPECLASS STATIC PASS / EVERY IMPLICIT INSTANCE REQUIRED BY THE F-1 CARRIER IS PRESENT IN PINNED MATHLIB V4.34.0 / NO LOCAL INSTANCE SHIMS REQUIRED / NO INSTANCE-DIAMOND PATCH ADDED / BUILD CERTIFICATION REMAINS INFRASTRUCTURE-BLOCKED / F-2 REMAINS CLOSED**

## 0. Objective

RPB-71 verified declaration signatures. RPB-72 audits the implicit typeclass graph required to elaborate those declarations under the exact pinned Lean/mathlib v4.34.0 corpus.

No live Lean process is available, so this is a source-level synthesis audit rather than a build certificate.

## 1. L2 exponent fact

The Lp-to-tempered-distribution coercion requires:

~~~lean
Fact (1 ≤ (2 : ℝ≥0∞))
~~~

Pinned mathlib provides the global instance:

~~~lean
fact_one_le_two_ennreal
~~~

Therefore no local Fact declaration is required.

Disposition: PASS.

## 2. Real domain inner-product geometry

The L2 Fourier transform requires the domain to be a finite-dimensional real inner-product space.

Pinned mathlib provides:

~~~lean
RCLike.toInnerProductSpaceReal : InnerProductSpace ℝ ℝ
finiteDimensional_self ℝ : FiniteDimensional ℝ ℝ
~~~

`Analysis/InnerProductSpace/Basic` explicitly checks that the concrete real inner-product instance agrees with `RCLike.toInnerProductSpaceReal`.

Disposition: PASS.

## 3. Real measurable/topological structure

Pinned mathlib provides global real-line instances:

~~~lean
Real.measurableSpace : MeasurableSpace ℝ
Real.borelSpace : BorelSpace ℝ
SecondCountableTopology ℝ
~~~

These discharge the measurable-space assumptions used by both the L2 Fourier and tempered-distribution layers.

Disposition: PASS.

## 4. Real volume and Haar structure

Pinned `MeasureTheory/Measure/Haar/OfBasis` provides for finite-dimensional real inner-product spaces:

~~~lean
measureSpaceOfInnerProductSpace
IsAddHaarMeasure (volume : Measure E)
~~~

and explicitly registers:

~~~lean
Real.measureSpace : MeasureSpace ℝ
~~~

Hence the explicit `volume` in `RealComplexL2` is the canonical real-line Lebesgue/Haar volume expected by the Fourier API.

Disposition: PASS.

## 5. Temperate growth of volume

Pinned `Analysis/Distribution/TemperateGrowth` provides:

~~~lean
IsAddHaarMeasure.instHasTemperateGrowth
~~~

under finite-dimensional real-space and Borel assumptions.

Therefore the instance chain is:

~~~text
volume IsAddHaarMeasure
    -> volume.HasTemperateGrowth
~~~

which supplies the measure-growth class required by the Lp-to-tempered-distribution coercion.

Disposition: PASS.

## 6. Local finiteness

The pinned real Lebesgue measure layer provides:

~~~lean
locallyFinite_volume : IsLocallyFiniteMeasure (volume : Measure ℝ)
~~~

This is not needed merely to form the CoeHead, but it is present for the injectivity theorem `ker_toTemperedDistributionCLM_eq_bot` and future carrier-strengthening steps.

Disposition: PASS.

## 7. Complex value-space Hilbert structure

The L2 Fourier transform on complex-valued functions requires:

~~~lean
NormedAddCommGroup ℂ
InnerProductSpace ℂ ℂ
CompleteSpace ℂ
~~~

Pinned mathlib provides the complex inner product through:

~~~lean
RCLike.innerProductSpace : InnerProductSpace 𝕜 𝕜
~~~

specialized to `𝕜 = ℂ`.

`Analysis/Complex/Basic` explicitly provides:

~~~lean
instance : CompleteSpace ℂ
~~~

Disposition: PASS.

## 8. L2 Fourier instance

`Mathlib.Analysis.Fourier.LpSpace` defines the L2 Fourier instance under:

~~~text
NormedAddCommGroup E
MeasurableSpace E
BorelSpace E
InnerProductSpace ℝ E
FiniteDimensional ℝ E
NormedAddCommGroup F
InnerProductSpace ℂ F
CompleteSpace F
~~~

Every one of these instances has been pinned above for `E = ℝ`, `F = ℂ`.

Therefore `𝓕 d.l2Mode` has a complete static typeclass path.

Disposition: PASS.

## 9. Tempered-distribution Fourier instance

`TemperedDistribution.instFourierTransform` requires the finite-dimensional real inner-product structure on the domain and the ordinary complex topological-module structure on the codomain.

Those are global for `ℝ` and `ℂ` under the imported corpus.

Therefore `𝓕 (d.l2Mode : RealComplexTempered)` has a complete static typeclass path.

Disposition: PASS.

## 10. Import reachability

`Mathlib.Analysis.Fourier.LpSpace` publicly imports `Mathlib.Analysis.Distribution.TemperedDistribution`, which publicly imports the Schwartz/Fourier and temperate-growth chain used above.

The same file proves `MeasureTheory.Lp.fourier_toTemperedDistribution_eq` under the generic finite-dimensional assumptions, so the required coercion and Fourier instances are part of its public elaboration surface.

No extra project import is statically required.

Disposition: PASS.

## 11. Why no local instance patch was added

Every needed class is already globally registered.

Adding local `haveI` declarations for `Fact (1 ≤ 2)`, `volume.HasTemperateGrowth`, or the real/complex inner-product structures would add noise and could create avoidable instance diamonds.

RPB-72 therefore makes no carrier-source change.

## 12. Audit matrix

~~~text
Fact (1 <= (2 : ENNReal)):             PASS
InnerProductSpace R R:                  PASS
FiniteDimensional R R:                  PASS
MeasurableSpace R:                      PASS
BorelSpace R:                           PASS
SecondCountableTopology R:              PASS
MeasureSpace R / volume:                PASS
IsAddHaarMeasure volume:                PASS
volume.HasTemperateGrowth:               PASS
IsLocallyFiniteMeasure volume:          PASS
InnerProductSpace C C:                  PASS
CompleteSpace C:                        PASS
L2 FourierTransform instance:           PASS
TemperedDistribution Fourier instance:  PASS
~~~

No missing implicit instance was found.

## 13. Remaining uncertainty

After RPB-71 and RPB-72, the unverified surface is narrowed to ordinary proof-term elaboration and parser/tactic behavior in the project file.

The typeclass graph itself no longer presents an identified blocker.

Build certification remains unavailable because the execution infrastructure still cannot run Lean.

## 14. RPB-72 determination

~~~math
\boxed{
\textbf{RPB-72 — EVERY IMPLICIT INSTANCE REQUIRED BY THE F-1 CARRIER IS PRESENT IN PINNED MATHLIB V4.34.0; NO TYPECLASS-SYNTHESIS BLOCKER IS VISIBLE STATICALLY.}
}
~~~

Current state:

~~~text
F-1  SOURCE IMPLEMENTED
     STATIC API PASS
     TYPECLASS STATIC PASS
     BUILD CERTIFICATION INFRASTRUCTURE-BLOCKED

F-2  NOT STARTED
~~~

WD-T40 remains LEAN-BLOCKED.

## Next cursor

~~~text
RPB-73 / WD-T40 CARRIER PROOF-TERM ELABORATION AUDIT
~~~

The next pass should inspect the remaining proof bodies and parser/elaboration-sensitive syntax line-by-line against pinned Lean/mathlib idioms, without starting F-2.