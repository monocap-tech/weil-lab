# RPB-108: stronger native finite margin at 81/100

Date: 2026-10-06. Parent: `4735640c067af8f2c2da42568423d1dcc1b19ae3`.
Branch: `research/rpb108-larger-aperture-complement`.

Definitions: [finite margin terminology](../docs/TERMINOLOGY_RPB108_NATIVE_FINITE_MARGIN.md).

## Result and exact scope

On the actual stored native 84-vector restriction at aperture a=81/100,
the physical orthonormal Legendre basis is
`sqrt((2n+1)/(2a)) P_n(x/a)`, n=0,...,83, with zero extension.
The native form includes the archived prime terms 2,3,4,5.
Its stored interval matrix now certifies

```
Q_84 - 10^(-18) I > 0.
Q(h) >= 10^(-18) ||h||_L2^2 for every h in this 84-dimensional span.
```

This improves the recorded finite bound 10^(-28) by a factor 10^10.
It does not assert an optimal bound. It does not improve the whole-domain
coercivity constant or extend the aperture frontier.

## Source custody and method

The unchanged input is
`notes/data/RPB108_PRIME5_MATRIX84_081_CERTIFICATE_20261005.json`,
Git blob `513b970b3d7d521c6d9f8b8f6551d550c99584d7`, 6,075,959 bytes.
The new verifier checks the exact Git blob hash before parsing, records its
SHA256, and checks aperture, degrees, prime terms and the previous bound.
Its conclusion inherits the original analytic interval construction; it
does not reconstruct that construction from first principles.

All 7,056 matrix intervals are checked for ordered endpoints, exact symmetry,
and inclusion in their outward-rounded 60-decimal-grid replacements.
Opposite reflection parities have exactly zero entries. The two 42-dimensional
parity blocks are shifted by 10^(-18) and checked using outward rational
interval elimination. Every shifted pivot has a strictly positive lower
endpoint. This proves positive definiteness for every real symmetric matrix
in the enclosure, hence also for the actual native matrix; the Hermitian
complex restriction follows from the real symmetric form.

The verifier uses the existing rational interval implementation in
`scripts/certify_native_legendre_small_window.py`. It records all 84 shifted
pivot lower bounds, its own SHA256, and the source SHA256 in the new JSON.
Two independent runs produced byte-identical output. An indefinite
comparison matrix is rejected. Shifts 10^(-16) and 10^(-17) were not certified
by this interval procedure; those failures prove neither negativity nor
optimality.

The older constructor initialized the shift at 10^(-28) and only decreased
it until certification succeeded. That value was a successful bound, not an
optimization result. This pass tests a larger shift against the same matrix.

## Reproduce

From a checkout of this branch:

```sh
python scripts/certify_native_prime5_finite_margin_081.py --output /tmp/native-finite-margin.json
cmp /tmp/native-finite-margin.json notes/data/RPB108_NATIVE_FINITE_MARGIN_081_20261006.json
```

The script also accepts `--input` to check a recovered copy of the exact
archived source blob. Any changed source bytes are rejected.

## What remains

The previously certified full-domain physical bound remains
1/(202*10^29), with logarithmic bound 1/(10+46460*10^29), at a=81/100.
A larger finite restriction bound cannot be substituted into the corrected
Schur certificate without rechecking the full source Gram and corrected
matrix. The archived 8.89 MB Gram could not be recovered in this pass:
connector retrieval failed and direct retrieval returned HTTP 403.
The whole-domain bound therefore remains unchanged.

The inspected actual-zeta source modules encode critical-line negative rows
as zero and parameterize finite selections; they do not supply a numerical
off-line packet in those inspected definitions. This is not an exhaustive
new repository audit and is not a claim that off-line zeros do not exist.
No selected-source residual enclosure has been numerically instantiated.

No endpoint exclusion, historical fixed packet attachment, F4 closure,
FULL TRANSPORT CLOSED, Lean formalization, or RH closure follows.
No Lean or workflow files were changed and no CI run was requested.

Next forward: recover the exact full Gram, test larger shifts of the corrected
Schur matrix, and recompute the full-domain constants only if that check passes.
