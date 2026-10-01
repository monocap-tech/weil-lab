# RPB-108 — actual archimedean exterior function and weighted mass

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `d8a521255334bd9b09abb7ce7a3b2499b093d866`.

## Actual function constructed

The pinned [RPB-EXT-A8 Gauss representation](../docs/IMPORTED_SOURCE_PINS.md)
has positive cosine density 2 exp(-t/2)/(1-exp(-2t)), t>0.
The candidate signed off-diagonal kernel retains the negative half-density:
-exp(-|z|/2)/(1-exp(-2|z|)). Its Fourier/distribution identification is still
a separate obligation; no transform equality is introduced here.

For a positive gap δ, replace |z| by max(δ,|z|). The denominator is strictly
positive, and the resulting signed complex kernel is continuous and uniformly
bounded in norm by 1/(1-exp(-2δ)). Convolution with the actual compact rough
carrier is therefore an actual continuous function. The proof uses only the
carrier's certified global L1 integrability, not boundedness or smoothing
of the carrier.

## Genuine exterior agreement

Take δ=a-c>0. For x outside (-a,a) and y in [-c,c], the certified geometry
gives |x-y|≥δ. Thus the truncation is inactive for every displacement in the
compact integral. The actual gap function equals the explicit untruncated
Gauss integral at that x.

The compact product genuinely converges: it is an L1 carrier multiplied by
a continuous bounded kernel away from the singularity. Exterior agreement is
not obtained by totalizing a divergent integral.

The arbitrary continuation at small displacements is not the whole singular
archimedean core. No interior identification follows from exterior agreement.

## Constructed regularity and mass

The function has the explicit uniform estimate

\[
 |A_\delta h(x)|\le
 \frac{\|h\|_{L^1}}{1-e^{-2\delta}}.
\]

It is locally integrable by continuity. For each κ>0, its norm times
exp(-κ|x|) is integrable on the whole line. This weighted mass is proved from
the uniform bound and integrability of the inverse exponential weight,
rather than imported as a field of an unspecified core.

This pass uses the uniform bound to obtain weighted mass. Sharper exterior
exponential decay is not needed and is not claimed as a new theorem.

## Remaining representation residue

The exterior archimedean function and its regularity/weighted mass are
constructed. Next: attach its exterior distribution action with the exact
Fourier normalization, reconstruct the pole-restored residual using central
cancellation and the already constructed finite-prime part, and prove the
compact source weak realization. Actual source-domain/quadratic/normalized
estimate attachment remains open.

The weighted Gaussian bridge and actual pole convergence are already
constructed. Threshold bookkeeping stays closed; coercivity has not started.
Canonical Weil and WD-T40 standing remain unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,960 build jobs passed. Nine endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`38f82d8b8328a7c0ce4e07e6b1476a9a2d3c9407`, run `36933467318`,
job `110608114891`, source blob `dc3e8c0e1b72769c8cdd6970c8b1131d395c24bc`.

Validation-only workflow/cache changes are excluded from research promotion.
The original research workflow blob remains
`f194e9564577d3b79831b7abfb91b5933f3af98f`. Prior checkpoint notes remain immutable.
