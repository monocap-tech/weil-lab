# RPB-108 — actual finite-prime regularity and L1 support-gap pairing

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `200e25ba4ce3d261841176b30372579bc5cf0782`.

## Actual component constructed

`neutralFinitePrimePhysical` is the finite physical translation sum for the
actual rough carrier, with coefficient `compactWindowPrimeCoefficient n / 2`.
The certified shell is definitionally its specialization to
`frozenWeilPrimeShell a b`. No threshold convention is changed.

Each translated carrier is globally integrable, by the existing compact-L2
to L1 theorem and translation invariance. Finite sums are therefore globally
L1 and locally integrable. If all shifts obey `|log n| ≤ L`, the function
vanishes outside `[-(c+L), c+L]`. Its norm is integrable against every fixed
weight `exp(κ |x|)`, because this weight is continuous on that compact interval.
The finite set itself supplies L as the sum of its absolute shifts; the
unconditional weighted-norm theorem requires no supplied growth estimate.

These are actual regularity results for the physical prime component, rather
than fields requested of an unspecified full residual. The existing Fourier
identification of the shell remains in force.

## Growth interface audit

The current `NeutralWeilCoreFunctionRepresentation.growth_bound` and
`NeutralExponentialResidualCarrier.growth_bound` demand a pointwise bound by
a constant times a fixed exponential. A compactly supported L2 representative
does not supply this: it may be unbounded on its compact support. Finite
translation and compact support alone cannot establish those fields.

The historical RPB-65 argument states growth of a distribution/function and
uses domination in a Gaussian pairing. Its finite-prime contribution admits
the L1 route proved here. No historical proof text is rewritten, and this
pass does not claim that the stronger current interface has been instantiated.

## Pairing result

For globally L1 q that vanishes on (-a,a), and a measurable test g with
norm at most B on the exterior, `integrable_pairing_of_L1_gap` proves genuine
integrability and

\[
\left|\int \overline{g(x)}q(x)\,dx\right|
\le B\int |q(x)|\,dx.
\]

The shell specialization consumes its already certified central vanishing.
The exterior bound B may carry Gaussian decay, so this estimate needs no
pointwise boundedness of the rough prime component. The actual Gaussian bound
has already been proved in the support-gap module; this new theorem does not
construct the whole residual or its Gaussian weak identity.

## Next residue

The finite-prime part now supplies actual local regularity and integral growth.
The archimedean core representative, full weak identity, and central
cancellation remain open, as do retained source-domain/quadratic/normalized
estimate attachment. The next growth step must either establish additional
carrier regularity or extend the residual and Gaussian bridges to integral
growth; it must not infer the current pointwise field from compact L2 support.

Threshold bookkeeping is closed. Coercivity has not started. Canonical Weil
and WD-T40 standing are unchanged.

## Certification

Certification: exact module passed 8,957 jobs on Lean 4.34.0 and mathlib
`5ed2965256430c3649e86755f9576b54eca72435`. Validation head
`d83af4b35838e08050e82019018c2f81828d6cb4`, run `36923201866`,
job `110574045820`, source blob `7e6d285d64357e775816dfcedbc2486e44b5049f`.
All eight audited endpoints use only `propext`, `Classical.choice`, and
`Quot.sound`; the unfinished/project-axiom declaration gate passed.

Validation-only workflow/cache changes are excluded from research promotion.
The original research workflow blob remains
`f194e9564577d3b79831b7abfb91b5933f3af98f`. Prior checkpoint notes remain
immutable. The promoted source is identical to the certified module blob.
