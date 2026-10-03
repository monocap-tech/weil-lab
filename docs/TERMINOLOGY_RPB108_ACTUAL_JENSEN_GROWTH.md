# RPB-108 — actual zeta Jensen growth terminology (2026-10-03)

These definitions accompany their first load-bearing source use. Historical
wording in other records remains unchanged.

## Actual pole-cleared entire zeta

`neutralActualZetaEntire z` is
`z * (z - 1) * completedRiemannZeta₀ z + 1`.
It is entire and has value 1 at zero. Away from 0 and 1 it equals
`z * (z - 1) * completedRiemannZeta z`, twice the conventional xi function.
At every actual open-strip zeta point its analytic order equals the existing
actual zeta analytic multiplicity. This is an actual analytic function, not a
packet realization or a WD-T38 coefficient identification.

## Actual Jensen mass

`neutralActualZetaJensenMass r` is the finite-support integer sum of the
analytic divisor of the actual entire function on the closed disk centered
at zero of radius |r|. It is nonnegative. It counts all analytic zeros in
that disk with their orders; it is an upper bound, rather than a declared
equality, for the actual open-strip height-window divisor count.

## Actual enclosing-circle envelope

`neutralActualZetaCircleEnvelope T` is the maximum of 1 and the supremum of
the norm of the actual entire function on the circle centered at zero of
radius 2(|T|+2). Compactness gives a finite upper bound; its normalization
gives a value at least 1. It is a canonically defined actual growth quantity,
not an independently supplied shell-count field.

## Count-to-growth bridge

The exact actual multiplicity-copy count at height T is at most
log(`neutralActualZetaCircleEnvelope T`)/log(2). The theorem has no supplied
count premise. It does not give a growth rate for the envelope, a local
logarithmic shell-count bound, infinite-divisor sampling, or the full Weil
form/source identity on the canonical logarithmic domain.

WD-T38 physical source-null attachment and central cancellation remain open.
Full spectral L2 remains unproved from WD-T38 and unassumed.
