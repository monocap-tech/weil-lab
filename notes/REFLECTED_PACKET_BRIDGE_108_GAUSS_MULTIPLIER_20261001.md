# RPB-108 — moment-derived finite Gauss multiplier attachment

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `5d341dfb342fd01ff42c30899caac9f5409a3051`.

## Actual exponential moments

For every b>0 and natural n, |x|^n exp(-b|x|) is globally integrable.
On the positive half-line, polynomial growth is dominated by exp(bx/2).
The library's exponential-decay integrability theorem gives actual
integrability. Reflection supplies the negative half-line, including
the harmless finite contribution at zero.

## Moment-derived Fourier regularity

A general lemma derives temperate growth of the Fourier transform of an
a.e. measurable function from actual integrability of all polynomial norm
moments. Fourier differentiation is lawful at every order. Each derivative
is bounded by the L1 norm of its differentiated integrand; polynomial
degree zero suffices for the temperate-growth bounds.

The finite geometric Gauss kernel inherits all moments from its actual
finite Laplace sum. Its certified Fourier identity transfers that growth
to the actual finite reciprocal symbol at the fixed t=2πξ normalization.
No missing Gauss identity or new temperate-symbol premise is assumed.

## Existing distributional action attachment

The existing tempered Fourier-multiplier CLM transposes onto a Schwartz
test as Fourier(symbol * inverseFourier(test)). The proved finite-symbol
temperate growth makes that product a lawful Schwartz test. Actual
carrier L1 and the library's bilinear Fourier/Fubini identity evaluate
this transposed pairing as the exact frequency weak identity from the
prior checkpoint. It therefore equals the actual finite physical
convolution pairing on every Schwartz test.

The positive finite sum is attached. Its negative retains the subtraction
sign of the actual finite digamma tail recurrence.

## Remaining obligations

The shifted digamma tail still requires weak/operator control. The
singular infinite Gauss kernel cannot be substituted into whole-line
integrals using its off-diagonal pointwise limit alone. Whole archimedean
source attachment, central cancellation, boundary reconstruction and
actual source-domain/quadratic/polarization/normalized estimate witnesses
remain open.

Threshold bookkeeping is closed; logarithmic coercivity has not started.
Canonical Weil, main and WD-T40 mathematical standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,966 build jobs passed. Four endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`c791f2def581ef83e6ea271e27dd0c0f497a2ce5`, run `36960906345`,
job `110694146452`, source blob `fd9a0350a97f5f02ce1d3eadc242cf74a83b11b7`.
Validation-only workflow/cache changes are excluded from research promotion.
Prior checkpoint notes remain immutable.
