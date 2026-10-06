# RPB-108: interruption-safe native row recovery at 23/25

The aperture is a=23/25 and the retained native restriction has 84 Legendre
vectors of physical degrees 0 through 83. A completed-row checkpoint with
count r stores the raw, unnormalized native interval entries for every pair
whose smaller degree is below r. Entries not yet computed are zero; odd
reflection-parity entries are exactly zero. These are intermediate native
entries, not a finite positivity certificate or a whole-domain certificate.

The earlier order-240 sessions were no longer active and their output files
were empty on recovery. Fresh primary and repeat runs now save an atomic
compressed checkpoint after each row. The codec stores exact integer
endpoints on the same 10^-400 grid and binds recovery to the aperture,
dimension, approximation orders, logarithm precision, constructor, native
core, exact polynomial arithmetic, kernel integrator, logarithm enclosure
and checkpoint codec hashes. A different aperture, grid, row count, interval
orientation, dimension, odd entry or populated uncomputed entry is rejected.

The codec audit preserves all 7,056 fixture endpoints and rejects eight
invalid controls; it repeated exactly. Fixtures are explicitly synthetic
and provide no native sign result. The historical quarter checksum and
constructor rejection controls remain unchanged.

Both fresh runs reached 25 completed rows. The saved primary and repeat
snapshots have the same bindings and agree exactly on all 1,800 stored
lower-triangle entries in those rows. The raw native restriction is still
incomplete. Full normalized entry widths, all finite and shifted pivots,
outward compaction, the nine-panel residual Gram and corrected sign remain
mandatory before accepting a result at 23/25.

The actual first-two-row recovery auditor independently compares a fresh
run through row two with a run stopped after row one and resumed through
row two. It passes exactly: all 84 computed even entries agree. The independent
repeat is byte identical; it makes no full matrix claim.

## Recovery

Continue each run with its own checkpoint:

```sh
python scripts/certify_native_prime5_matrix84_092.py --checkpoint native84_092_rows.json.gz
python scripts/certify_native_prime5_matrix84_092.py --checkpoint native84_092_repeat_rows.json.gz
```

For repository-only recovery, restore the respective compressed snapshot,
verify its SHA-256 from the custody report, and use its path as the checkpoint
argument. The constructor rejects stale hash bindings. A completed raw
checkpoint still reruns normalization, full and shifted finite sign checks,
reflection parity, total entry-width guard and the negative control.

Custody:

- `notes/data/RPB108_NATIVE84_092_ROW_CHECKPOINT_20261006.json.gz`
- `notes/data/RPB108_NATIVE84_092_REPEAT_ROW_CHECKPOINT_20261006.json.gz`
- `notes/data/RPB108_NATIVE84_092_ROW_CHECKPOINT_CUSTODY_20261006.json`
- `notes/data/RPB108_NATIVE_MATRIX_CHECKPOINT_VALIDATION_20261006.json`

The whole-domain positivity frontier remains 91/100. The separate global/F4
lane's entry audit and contact dichotomy are preserved. F4, full transport,
global endpoint exclusion and historical attachment remain open. Lean and
workflows are unchanged.

## Later raw recovery snapshot

A later primary snapshot has 83 completed rows and the repeat snapshot has
84. They agree on all 3,569 lower-triangle entries whose smaller degree is
below 83. The final degree-83 diagonal remains unverified by comparison;
both final constructor certificates are still pending. The later snapshots
are stored separately, preserving the earlier 25-row custody record:

- `notes/data/RPB108_NATIVE84_092_LATEST_ROW_CHECKPOINT_20261006.json.gz`
- `notes/data/RPB108_NATIVE84_092_LATEST_REPEAT_ROW_CHECKPOINT_20261006.json.gz`
- `notes/data/RPB108_NATIVE84_092_LATEST_ROW_CHECKPOINT_CUSTODY_20261006.json`

The additive definition registry is
`docs/TERMINOLOGY_RPB108_NATIVE_ROW_RECOVERY_092.md`.
