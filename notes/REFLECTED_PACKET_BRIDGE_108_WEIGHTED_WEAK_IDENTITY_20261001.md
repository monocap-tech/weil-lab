# RPB-108 — weighted Hermitian source identity and actual pole convergence

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `e5653d51f559e9ecdcd249692a08902488748a27`.

## Concrete advance

The previous integral-growth pass proved the actual residual/Gaussian
support-gap pairing and a generic compact-to-Schwartz cutoff extension.
This continuation attaches the already named physical source pole and derives
the exact fixed-cutoff multiplier-plus-pole identity for that Hermitian
Gaussian test.

The radius-only pole tail and integrability proofs consume the carrier,
a strict radius, and explicit pole growth. They consume no pointwise residual
growth field. For `neutralWeilSourcePole`, the growth rate is exactly 1/2,
so the sufficient large-parameter condition is 4 ≤ R(a-c).

`neutralWeilSourcePole_dualGaussian_integrable` proves genuine convergence
of the actual pole pairing. The weighted residual pairing converges by the
previous module. Neither product integrability remains an input to
`integralGrowthWeilGaussianHermitian`.

## Compact source identity retained explicitly

`IntegralGrowthWeilWeakRealization` retains precisely the compact-test
identity for the fixed-cutoff multiplier core and named pole. It contains no
Gaussian identity. The new theorem derives the Hermitian Gaussian equation
using the already certified Schwartz cutoffs and both genuine integrability
results. It applies the multiplier to the actual conjugated Gaussian test;
it introduces no Fourier normalization factor.

The actual compact source witness remains unconstructed. Adding this
interface does not prove the source equation or construct the residual.

## Archimedean preflight and remaining residue

The pinned RPB-EXT-A8 Gauss kernel has a 1/x singularity at zero. The rough
compact carrier does not license treating it as an ordinary globally
integrable convolution kernel. Off-support construction has a positive
distance from that singularity; reconstructing the whole distribution still
requires the exact compact weak realization and central cancellation.
This pass does not formalize that off-support construction.

Next: construct the actual archimedean function and weighted mass, attach the
compact source identity and central cancellation, and retain the actual
source-domain/quadratic/normalized-estimate attachment. Pole/Gaussian
integrability and compact-to-Gaussian weak extension are now constructed in
the weighted route. The whole residual remains open.

Threshold bookkeeping is closed. Coercivity has not started. Canonical Weil
and WD-T40 standing are unchanged; historical notes remain immutable.

## Certification

Certification: exact module passed 8,959 jobs on Lean 4.34.0 and mathlib
`5ed2965256430c3649e86755f9576b54eca72435`. Validation head
`965b934fed9a7cca1c7ddad5d4c427c253fa3ed1`, run `36931697060`,
job `110602273298`, source blob `733587e649dadbc4fdbc8d2b97a2774813889753`.
All four audited endpoints use only `propext`, `Classical.choice`, and
`Quot.sound`; the unfinished/project-axiom declaration gate passed.

Validation-only workflow/cache changes are excluded from research promotion.
The original research workflow blob remains
`f194e9564577d3b79831b7abfb91b5933f3af98f`. Prior checkpoint notes remain
immutable. The promoted source is identical to the certified module blob.
