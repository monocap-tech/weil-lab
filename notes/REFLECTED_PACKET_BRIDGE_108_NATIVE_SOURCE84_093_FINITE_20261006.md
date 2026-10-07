# RPB108: matching native/source finite closure at 93/100

Definitions: [matched inputs](../docs/TERMINOLOGY_RPB108_MATCHED_093.md).
Lane: aperture. Source base: 974e20325cc7a980b827c84f44668fd2c4378ca5.

## Accepted inputs

The fresh actual native matrix on degrees 0–83 has all 84 positive shifted
pivots. Its physical finite coercivity is
1/2097152000000000000000000 and its maximum entry width is approximately
3.4399956120390572e-37, below 10^-35. Both complete raw row checkpoints
are byte identical and retain all original construction hashes.

The parity finalizer recomputes the physical normalization of every raw
entry at the original outward 400-digit grid, then widens every resulting
entry to an 80-digit grid. Exact reflection parity makes the 84-vector
matrix a direct sum of two 42-vector blocks. Positive shifted pivots in
both blocks prove the same finite margin on the entire 84-vector space.
No parity sector or off-diagonal term within a sector is discarded.
The negative diagonal control rejects. Both parity-finalized outputs and
both compact outputs repeat exactly.

The original full 400-digit native finalizations also complete and repeat
exactly. All 7,056 physical intervals and the finite coercivity margin
agree exactly with the parity finalizer. All original 84 shifted pivots
are positive. The separate agreement record preserves their output hashes.

The independent persisted-matrix audit verifies the complete raw binding,
all 7,056 raw-to-physical entries using independent rational rounding,
all compact inclusions, all 84 shifted parity-block pivots and the original
width limit. Both audits reproduce exactly. The compact certificate
retains the parity finalization's raw matrix hash; the archived complete
raw rows and finalizer reproduce that object without repeated integration.

The fresh 84-source certificate repeats exactly, with source-map error
approximately 1.513122707744907e-36, below 2e-36. All 84 physical
normalization and error-aggregation checks and all 756 coefficient-panel
checks pass; an underreported map-error control rejects. Its independent
integration audit verifies 15 smooth product and 15 endpoint-log
contractions on panels 0,3,4,5,8 by direct exact double sums and original
convolution containment. Both audits repeat exactly.

## Complete Gram staging

The fresh Gram constructor uses these exact source/native inputs,
the same actual degrees and all nine support panels. All mixed terms and
all 84 projected-away components are retained. It emits the complete
residual Gram immediately after the full native/source pairing and width
checks, before any sign decision. Its output explicitly leaves corrected
sign pending. This makes the completed contractions independently reusable
if a subsequent sign estimate fails.

Both fresh complete Gram runs have started. They use the separately
certified 93/100 two-band complement 2/3, inverse factor 3/2 and retained
logarithmic complement 9/100. No 23/25 Gram or source is substituted.
Complete residual Gram acceptance and corrected sign are still pending.

## Exact compressed custody and recovery

The complete raw native row checkpoint is stored as
`notes/data/RPB108_NATIVE84_093_COMPLETE_RAW_ROWS_20261006.json.gz`.
The source is stored losslessly as
`notes/data/RPB108_PRIME5_SOURCE84_093_CERTIFICATE_20261006.json.gz`.
Decompression restores the original certificate bytes and hash. The Gram
and independent integration/pairing audits read this compressed source
when its uncompressed JSON is absent. The source normalization validator
accepts either representation; its mixed compressed/uncompressed check
produces the identical audit report.

To reconstruct the native full physical enclosure from archived raw rows:

```
python scripts/finalize_native_prime5_matrix84_093.py notes/data/RPB108_NATIVE84_093_COMPLETE_RAW_ROWS_20261006.json.gz > native84_093_finalized.json
python scripts/compact_native_prime5_matrix84_093.py --input native84_093_finalized.json --output notes/data/RPB108_PRIME5_MATRIX84_093_COMPACT80_20261006.json
```

This regenerates the exact compact input pinned by the Gram. The original
constructor can also resume from all 84 raw rows, without integration.
The custody manifest records compressed/uncompressed hashes and all new
scripts/certificates. Historical records and the independent global lane
are preserved. Whole-domain positivity remains certified through 23/25;
no 93/100 full-form negative witness, global endpoint exclusion, historical
packet identification, F4, full transport or new Lean proof is claimed.

## Repeated panel recovery checkpoint

The two Gram runs agree byte for byte through 7 of nine panels.
The accepted lossless recovery snapshot is
`notes/data/RPB108_PRIME5_GRAM84_093_RECOVERY_PANEL_CHECKPOINT_20261006.json.gz`.
The existing codec accepts its original source/native/constructor/geometry/Hankel
bindings at the exact 300-digit grid. Its custody JSON records both hashes
and all input bindings. This is an incomplete contraction checkpoint;
complete Gram acceptance and corrected sign remain pending.

Decompress it to a plain JSON checkpoint before resuming the constructor:

```
gzip -dc notes/data/RPB108_PRIME5_GRAM84_093_RECOVERY_PANEL_CHECKPOINT_20261006.json.gz > gram84_093_checkpoint.json
python scripts/certify_native_prime5_gram84_093.py --checkpoint gram84_093_checkpoint.json > gram84_093.json
```

The compressed source fallback and committed native compact enclosure are
sufficient to resume; none of the completed support panels is recomputed.
