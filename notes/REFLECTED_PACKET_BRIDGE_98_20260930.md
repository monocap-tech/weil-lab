# RPB-98 — WD-T40 F-4 Gaussian-admissibility weak-realization bridge

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **F-4 DOMAIN BRIDGE TYPED IN SOURCE / NO COERCIVITY YET / COMPACT-TEST EXT-4 REALIZATION RETAINED / SPECIFIC MOVING-GAUSSIAN SCHWARTZ REPRESENTATIVE + RESIDUAL/POLE INTEGRABILITY + EXTENDED WEAK IDENTITY EXPOSED AS EXPLICIT UNRESOLVED INTERFACE / BUILD CERTIFICATION PENDING**

## 0. Objective

RPB-97 restored a fully normalized and build-certified F-2/F-3 chain.

The remaining pre-coercivity obstruction was domain-theoretic:

- the F-2 EXT-4 weak realization accepted only compactly supported Schwartz
  tests;
- the F-3 moving-Gaussian filtered mode is noncompact;
- the stored pole function had only local-integrability typing.

RPB-98 types that seam explicitly and does not yet attempt logarithmic
coercivity.

## 1. New module

Added:

~~~text
WeilDefect/Morphology/NeutralGaussianAdmissibility.lean
~~~

and registered it in the project root.

## 2. New interface

The source defines:

~~~lean
RightLimitWeilGaussianAdmissibilityBridge
~~~

parameterized by:

- the certified F-1 physical carrier;
- the certified exponential-growth residual;
- the normalized strict-right symbol-temperate premise;
- the explicit pole function;
- the moving-Gaussian normalization constant;
- the moving parameter R.

It contains exactly five pieces of data.

### 2.1 Compact-test realization

~~~lean
compactWeak :
  RightLimitWeilWeakRealizationPremise ...
~~~

Thus the bridge strengthens rather than replaces the existing F-2 EXT-4
interface.

### 2.2 Schwartz realization of the actual filtered mode

~~~lean
gaussianTest : SchwartzMap ℝ ℂ

gaussianTest_apply :
  ∀ x,
    gaussianTest x =
      movingGaussianFilteredMode Ck R carrier x
~~~

This is the exact missing typing needed before the tempered multiplier core can
be evaluated on the moving Gaussian mode.

### 2.3 Genuine whole-line integrability

The bridge requires:

~~~lean
residual_pairing_integrable
pole_pairing_integrable
~~~

for the actual Gaussian test.

This prevents Lean's total Bochner integral from silently assigning a value to
a nonintegrable expression.

### 2.4 Extended weak identity

The bridge stores:

~~~lean
gaussianWeakIdentity
~~~

with the exact same normalized multiplier core and explicit pole function as
the compact-test EXT-4 realization.

No lower bound or coercivity conclusion appears in this field.

## 3. Packaging the physical F-3 pairing

The theorem

~~~lean
movingGaussianResidualPairing_eq_weakLeft
~~~

identifies the already-certified F-3 physical pairing

~~~math
∫ q(x) G_R(x) dx
~~~

with the left-hand side of the Gaussian weak identity, using only the
pointwise identification of the Schwartz test and commutativity of complex
multiplication.

The theorem

~~~lean
gaussianWeakRealization
~~~

then exposes:

1. residual-pairing integrability;
2. pole-pairing integrability; and
3. the exact weak identity

~~~math
\langle q,G_R\rangle
=
\langle \Psi_a^{ml}(D)h,G_R\rangle
+
\langle p,G_R\rangle.
~~~

This is the F-4 domain bridge only.

## 4. What remains unresolved

RPB-98 does **not** claim the bridge is discharged.

The intended internal proof route is still:

1. construct the moving filtered mode as a Schwartz function;
2. choose compactly supported smooth cutoffs converging to it in a topology
   strong enough for the tempered multiplier core;
3. use the certified exponential growth of q for dominated convergence on the
   residual side;
4. expose the actual finite-dimensional pole growth and pass the pole pairing
   to the limit.

The current Lean/mathlib corpus does not hand this entire cutoff package to the
project as one theorem, and the F-2 pole carrier does not yet expose a growth
bound.

Therefore the bridge remains an explicit theorem-facing premise rather than a
hidden assumption.

## 5. Scope discipline

The new interface contains **none** of:

- the EXT-5 logarithmic symbol lower bound;
- the main moving-frequency window;
- an off-window negative-part estimate;
- Gaussian coercivity;
- exponential Fourier decay;
- strip holomorphy.

Thus F-4 coercivity itself has not begun.

## 6. RPB-98 determination

~~~math
\boxed{
\textbf{RPB-98 — THE NONCOMPACT GAUSSIAN-TEST DOMAIN SEAM IS NOW EXPLICITLY TYPED; THE COMPACT-TEST EXT-4 IDENTITY IS NO LONGER SILENTLY APPLIED OUTSIDE ITS DOMAIN.}
}
~~~

## Next cursor

~~~text
RPB-99 / WD-T40 F-4 GAUSSIAN-ADMISSIBILITY BRIDGE BUILD CERTIFICATION
~~~

The next pass should compile only

~~~text
WeilDefect.Morphology.NeutralGaussianAdmissibility
~~~

repair genuine compiler diagnostics, and stop.

Do not begin logarithmic coercivity before that build gate closes.
