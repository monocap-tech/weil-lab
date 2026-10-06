# RPB-108: recovered full Gram and stronger corrected Schur margin

Date: 2026-10-06 UTC. Parent: `a341961fff6aa898dd532f9f72a9041e57e45666`.
Branch: `research/rpb108-larger-aperture-complement`.
Definitions: [recovered corrected-margin registry](../docs/TERMINOLOGY_RPB108_RECOVERED_CORRECTED_MARGIN.md).

## Result

At a=81/100 the complete actual corrected Schur form certifies
tau=10^(-18), improving the previously recorded 10^(-29) margin by 10^11.
This is a fresh positive sign check against the complete recovered Gram,
including its actual source error; it does not substitute the raw finite
margin for the corrected one.

The full supported native form satisfies

```
Q(h) >= mu ||h||_2^2,
mu = 51/4557360000000000000100 > 10^(-20).

Q(h) >= kappa Elog(h),
kappa = 51/1048192800000000000023510 > 4*10^(-23).
```

The exact full-domain coefficients are more than 10^11 times the parent
turn's coefficients. The numerical aperture frontier remains 81/100.

## Exact recovery and source custody

The connector could not retrieve the 8.89 MB archived Gram. Instead the
unchanged original constructor was run from recovered, hash-checked source
inputs. The resulting 8,894,630-byte file matches both archive identifiers:

- SHA256: `32f664f3e4a686dd220755c18f8aa38b790955b9c6b1a08e99fb8c5ac3a1615c`.
- Git blob: `d2f4cd3ada4d9520dfbd13186e055e7e9942845f`.

The recovered source input is 5,312,488 bytes, Git blob
`cbdd89a810bf400bf39988a56319ac8c217eb1b7`; the native input is 6,075,959
bytes, Git blob `513b970b3d7d521c6d9f8b8f6551d550c99584d7`.
Their SHA256 values are checked against the reconstructed Gram and recorded
in the new corrected certificate.

The restored constructor and its endpoint-log, exact Hankel, exact logarithm,
basis normalization, larger-aperture complement and prime-5 complement
helpers match their archived Git blob identities. Its reconstruction
rechecks all 7,056 native/source pairings, the nine translation panels,
the source-error correction and the original sign/lift checks.
The equality of the entire canonical file includes all original interval
endpoints, sign bounds and metadata. The analytic interval-construction
proof is inherited from the archived framework; this is not a new Lean proof.

## Smaller complete transport enclosure

The exporter requires the exact original SHA256 before using any entries.
For every lower-triangle interval [lo,hi], it computes

```
[floor(10^80 lo)/10^80, ceil(10^80 hi)/10^80].
```

All 3,570 inclusions and exact original symmetry are checked. Reflection of
the lower triangle reconstructs the full symmetric matrix, retaining every
mixed parity entry. The compact file is 479,912 bytes and has SHA256
`d7c50dd7e784300ddedb2d2d020d21f427ebd2254ca841b7b35888cb532dec96`.

This is deliberate outward rounding, not a lossless re-encoding. The original
600-digit certificate remains unchanged. The compact record marks its new
interval grid and width, retains the original grid/width for provenance,
and labels inherited original sign fields explicitly. The separate new
corrected certificate contains the fresh sign result.

The original source-map error eta and surrogate norm bound M still give
delta=eta(2M+eta), independently of transport rounding. The checker verifies
M^2 against the original surrogate trace supplied by the hash-checked export.
It uses the widened trace for the new conservative lift estimate.
The native matrix is separately rounded outward on the same 80-digit grid.

## Fresh corrected sign and full-domain conversion

Every sign test uses the complete 84x84 matrix

```
Q84-(100/51)Rhat84-((100/51)delta+tau)I.
```

No mixed term is discarded and no parity splitting is used. At tau=10^(-18),
all 84 interval pivot lower endpoints are strictly positive. The first
tested shift succeeds; this pass does not test a still larger corrected
shift or claim an optimal value. The earlier failed raw-matrix shifts
10^(-17) and 10^(-16) remain merely uncertified raw attempts.

The matching complement is c=51/100. The widened Gram trace verifies
L^2>(100/51)^2(trace_upper+delta) for L=47/5, improving the previous
integer lift ceiling 10. The already proved
[Schur norm conversion](REFLECTED_PACKET_BRIDGE_108_SCHUR_NORM_CONVERSION_20261006.md)
then gives mu=tau*c/[tau+c(1+L^2)] on the entire supported form domain.

The inherited actual global Garding bound
Q>=(1/10)Elog-23||h||_2^2 gives kappa=mu/[10(mu+23)].
The displayed simple bounds are rounded down from these exact coefficients.
Existing physical support inclusion extends them to smaller windows.
No numerical rightward aperture increment or continuity modulus is computed.

## Validation and reproduction

The compact export reproduces byte for byte. Two corrected-margin runs
produce byte-identical certificates, including every shifted pivot bound.
A forced negative diagonal is rejected, and modifying the compact input's
bytes is rejected by its pinned hash. The checker verifies native/source
hashes, matched dimensions, the actual correction, all 7,056 residual
enclosure inclusions and the lift bound.

From a checkout:

```sh
python scripts/certify_native_prime5_corrected_margin_081.py --output /tmp/corrected-margin.json
cmp /tmp/corrected-margin.json notes/data/RPB108_PRIME5_CORRECTED_MARGIN_081_20261006.json
```

To reconstruct the original and reproduce the compact export:

```sh
python scripts/certify_native_prime5_gram84_081.py > /tmp/full-gram.json
python scripts/export_native_prime5_gram80_081.py --input /tmp/full-gram.json --output /tmp/compact-gram.json
cmp /tmp/compact-gram.json notes/data/RPB108_PRIME5_GRAM84_081_COMPACT80_20261006.json
```

Reconstruction is expensive. Ordinary new sign checks use the already saved
compact enclosure.

## Standing

The source-recovery blockage for this fixed Gram is resolved. The corrected
margin and full-domain coefficients are stronger at the same aperture.
Historical notes and original certificates keep their original constants.

Global endpoint exclusion, actual fixed historical packet attachment,
F4 and FULL TRANSPORT CLOSED remain open. No actual selected off-line packet
is supplied by this numerical basis certificate. No Lean or workflow edits;
no CI run requested.

Next: use the stronger complete certificate for any further numerical
aperture test; a new aperture still requires matched native/source and
complement certification. The current result does not advance that frontier.
