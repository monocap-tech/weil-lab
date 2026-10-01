# RPB-108 — concrete exterior residual candidate

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `42324e13e69718c51b9b4408f3a8e8d1faaf6ee4`.

## Constructed ingredients and function

The explicit function is the archimedean gap convolution minus the actual
finite prime translations for `rightLimitPrimePowerFinset a`, plus the named
source pole. The sign and cutoff follow the existing right-limit symbol.
Outside (-a,a), the archimedean term is the genuinely convergent untruncated
Gauss integral. Inside (-a,a), the candidate is explicitly zero.

This constructs a specific function; it does not assert that the candidate
represents the source distribution. The auxiliary archimedean continuation
inside the interval is discarded by the indicator.

## Genuine analytic fields

The archimedean ingredient is continuous, the finite prime ingredient is L1,
and the pole is continuous. Their sum and its measurable exterior restriction
are locally integrable. No boundedness of the rough carrier is required.

For any κ>1/2, the pole norm times exp(-κ|x|) is dominated by its explicit
constant times exp(-(κ-1/2)|x|), whose integral converges. The other two
ingredients already have weighted mass. The norm triangle inequality proves
weighted mass of the sum, and the indicator can only decrease the norm.

At κ=1 the explicit function inhabits every analytic field of
`NeutralIntegralGrowthResidual`, including the strict gap and central AE zero.
Consequently the certified integral-growth Gaussian estimates now apply to
this concrete candidate. No Gaussian source identity follows without source
realization.

## Attachment still open

Vanishing imposed by a zero continuation is not proof that the pole-restored
source action cancels centrally. Exact Fourier/distribution identification on
the exterior and actual source cancellation inside must identify the compact
weak action of this particular candidate. Boundary distribution contributions
must also be addressed; central and exterior statements alone do not justify
a whole-line identity. Source form-domain/quadratic/shifted-estimate attachment
remains open. Threshold bookkeeping is closed; coercivity has not started.
Canonical Weil and WD-T40 standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,961 build jobs passed. Eight endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`b5b421fa5f0092fbe146229c72d599a329d8242d`, run `36936688172`,
job `110618484466`, source blob `016129d75f5368032392af46db03df752149f217`.

Validation-only workflow/cache changes are excluded from research promotion.
The original research workflow blob remains
`f194e9564577d3b79831b7abfb91b5933f3af98f`.
Prior checkpoint notes remain immutable.
