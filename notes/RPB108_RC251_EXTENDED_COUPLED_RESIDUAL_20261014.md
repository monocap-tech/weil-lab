# RPB108 RC251: complete coupled residual through degree 256

Starting head: `2ab55d9c6efc63d45eeb697738a60f6ed1c6fdf7` (RC250).

RC251 materializes more of the same actual residual
`e=N0(Pbase-Z)-lambda D^-1 Fhat*Fhat Z`. The sources remain N0 P0 and
N0 P1. The four-trial spaces and selected RC248 trial coefficients remain
unchanged. Original N0, positive augmented N, and canonical inverse M
remain distinct; no original/augmented commutation is assumed.

RC250 supplied signed, coupled original-model numerator coefficients
through degree 256. RC251 converts those interval coefficients through
the actual canonical metric parameter interval, and computes the entire
aggregate physical band action on the same exact Z through degree 256.
Subtracting the augmentation from the original action yields a complete
retained residual center and coefficient-error enclosure on that output
block. Low-degree band centers and radii are recomputed with the stronger
interval calculation; every low model interval intersects its pinned
RC248 counterpart. No equality of the old and new centers is assumed.

The band calculation uses exact spherical-polynomial boundary controls
through 256 and 224 integration-by-parts terms, with 240 terms in replay.
Homogeneous Horner evaluation computes the same finite inverse-power
series and exact remainder using integer arithmetic. Phase and finite
series intervals are rounded outward on a 10^-120 grid; scaled static
and oscillatory moments are rounded outward on a 10^-1000 grid. All
interval containment checks are asserted, and intermediate interval
operations preserve exact rational endpoints. This avoids rounding tiny
scaled moments to a coarser absolute grid before multiplying their large
polynomial coefficients. The final band Gram intervals use a 10^-24 grid.

The independent RC248 band input-energy partition applies to the same
exact Z. It is intersected with the newly materialized input pairing.
The contraction inequality C^2<=C bounds output beyond 256 by that input
energy minus captured output energy. The original beyond-256 tail is
inherited from RC250. Their residual tail norms are combined; finite
output rounding and omitted output degrees are orthogonal. All original
global model faults and the rational/physical augmentation discrepancy
remain paid. Variational inverse and signed-gap intervals are intersected
with RC250.

| Source | RC250 inverse upper | RC251 inverse upper | Reduction | RC251 signed gap interval |
| --- | ---: | ---: | ---: | --- |
| N0 P0 | 4.281277614 | 3.999083723 | 6.59% | [-3.910524527, 0.077120767] |
| N0 P1 | 6.050710991 | 5.522428343 | 8.73% | [-5.425345527, 0.083675302] |

Decimals are approximate; all endpoints in the certificate are exact
rationals. Prior inverse lower endpoints, approximately 0.011438429
and 0.013407514, are preserved.

| Bound | Even | Odd |
| --- | ---: | ---: |
| Complete residual squared D-error | 0.001461177218 | 0.001741669544 |
| Previous squared D-error | 0.002046691141 | 0.002629598031 |
| Actual residual squared D-energy lower | 0 | 0.000001471675 |
| Actual residual squared D-energy upper | 0.005460156451 | 0.007170660938 |
| Physical band output energy beyond 256 upper | 0.000018041896 | 0.000018825979 |

The odd residual is now certified nonzero in the D-energy norm. That
does not prove a negative signed gap or exclude a successful inverse
response calculation. Both signed intervals still cross zero.

Validation covers 188 inherited Git blob pins, every intermediate
outward interval containment, independent finite-series/remainder
controls for homogeneous Horner evaluation, a tiny scaled-moment exact
interval control, parity zeros, spherical boundary derivatives, low model
interval intersections, and full input-energy partition intersection.
Replay reverses exact summation orders, uses 240 integration-by-parts
terms, and requires equality of the entire JSON certificate.

Run:
`python scripts/validate_rpb108_rc251_extended_coupled_residual.py --output certificates/rpb108_rc251_extended_coupled_residual.json`

Replay:
`python scripts/validate_rpb108_rc251_extended_coupled_residual.py --output certificates/rpb108_rc251_extended_coupled_residual.json --replay`

The full signed response matrix of rank 639 (248 even, 391 odd) is still
unevaluated. The original full auxiliary norm gate is open. The separate
canonical eight-source inverse width remains `485647/1000000`. Stage I,
RH, F4, and Lean remain open.

Next cursor RC252: refine remaining direct residual tails or strengthen
residual inverse estimates, while preserving the full signed positivity
requirement.
