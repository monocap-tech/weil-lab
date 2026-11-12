# RPB-86 — WD-T40 F-2 EXT-4 weak-realization constructor

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **SOURCE IMPLEMENTED / EXPLICIT EXT-4 WEAK-REALIZATION PREMISE ADDED / PREMISE TIED TO THE CERTIFIED F-1 PHYSICAL MODE, STRICT-RIGHT RADIUS, BUILD-CERTIFIED SYMBOL-TEMPERATE INTERFACE, AND CANONICAL TEMPERED MULTIPLIER CORE / PACKAGING THEOREM INTO THE CERTIFIED EXPONENTIAL-GROWTH RESIDUAL TARGET ADDED / NO F-3 ANALYTIC CONTENT INCLUDED / BUILD CERTIFICATION PENDING**

## 0. Objective

RPB-85 build-certified every internal F-2 carrier component except the actual
compact-window operator identification.

RPB-86 implements that remaining bridge only as an explicit imported EXT-4
premise and a packaging theorem.

## 1. New imported premise

The residual-carrier module now defines:

~~~lean
RightLimitWeilWeakRealizationPremise
~~~

It is parameterized by:

- the original support radius `c`;
- the concrete F-1 `NeutralPhysicalFourierCarrier`;
- the corrected `NeutralExponentialResidualCarrier`;
- the strict-right `RightLimitWeilSymbolTemperatePremise` at
  `residual.a`; and
- the physical pole/evaluation function.

The premise stores exactly:

~~~text
pole_locallyIntegrable
compact-test weakIdentity
~~~

with multiplier term:

~~~lean
rightLimitWeilMultiplierCore
  residual.a hSymbol carrier.temperedMode
~~~

Thus the imported operator identity is tied to the actual certified physical
mode rather than to an arbitrary tempered distribution.

## 2. Weak identity

For every compactly supported Schwartz test `u`, the premise states:

~~~math
\int u(x)q(x)\,dx
=
\langle
\Psi_a^{\rm right}(D)h,
u
\rangle
+
\int u(x)p(x)\,dx.
~~~

Here:

- `q` is the full exponential-growth residual;
- the middle term is the certified conditional tempered multiplier core;
- `p` is the physical pole/evaluation contribution.

No pointwise whole-line multiplier equation is asserted.

The compressed-symbol caution therefore remains intact.

## 3. Packaging theorem

RPB-86 adds:

~~~lean
rightLimitWeilWeakRealization
~~~

which consumes the explicit EXT-4 premise and returns:

~~~lean
NeutralWeilResidualWeakRealization c
~~~

by direct field packaging.

This theorem contains no hidden analysis.

## 4. Scope discipline

The EXT-4 premise does **not** contain:

- support-gap Gaussian pairing;
- exponential smallness of the residual pairing;
- logarithmic Gaussian coercivity;
- exponential Fourier decay;
- strip holomorphy;
- compact-support contradiction.

Those remain F-3 through F-5.

Thus RPB-86 does not weaken WD-T40 by importing its internal proof.

## 5. F-2 standing

~~~text
F-1 physical Fourier carrier:
    BUILD-CERTIFIED

F-2 strict-right scalar symbol:
    BUILD-CERTIFIED

F-2 symbol-temperate imported premise:
    BUILD-CERTIFIED AS INTERFACE

F-2 canonical tempered multiplier core:
    BUILD-CERTIFIED

F-2 exponential-growth residual carrier:
    BUILD-CERTIFIED

F-2 generic weak-realization target:
    BUILD-CERTIFIED AS INTERFACE

F-2 EXT-4 actual weak-realization premise:
    SOURCE IMPLEMENTED

F-2 EXT-4 packaging theorem:
    SOURCE IMPLEMENTED

F-2 source build:
    PENDING

F-3:
    CLOSED
~~~

## 6. RPB-86 determination

~~~math
\boxed{
\textbf{RPB-86 — THE LAST F-2 MATHEMATICAL BRIDGE IS NOW REPRESENTED EXPLICITLY AS EXT-4, AND LEAN SOURCE PACKAGES IT INTO THE CERTIFIED ACTUAL-RESIDUAL INTERFACE WITHOUT IMPORTING ANY F-3--F-5 CONTENT.}
}
~~~

## Next cursor

~~~text
RPB-87 / WD-T40 F-2 EXT-4 WEAK-REALIZATION BUILD CERTIFICATION
~~~

The next pass should compile only the updated
`NeutralWeilResidualCarrier` module under the pinned toolchain, repair genuine
compiler diagnostics, and stop.

Do not begin F-3 until that build gate closes.
