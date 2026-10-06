# RPB-108: all nine actual support panels complete at 23/25

The aperture is a=23/25. A complete panel checkpoint stores the CS, smooth
and cross contraction matrices after every actual support panel has been
integrated. CS is the retained Legendre/source pairing matrix; smooth is
the polynomial source Gram; cross is the endpoint-log/source pairing matrix.
All mixed terms remain available for the residual Gram construction. The
stage definitions are recorded in
`docs/TERMINOLOGY_RPB108_GRAM_STAGE_092.md`.

Both fresh computations completed all nine panels. Their complete checkpoint
files are byte identical, with SHA-256
`41bd7028d9952a1113fc9e75c5067faa72467ef277b0d4f1129727e6281e3a1e`.
The deterministic gzip archive is 3,181,266 bytes, with SHA-256
`18d6bcede9659dba6ca5dc4057bbff14b7e0f43e55d10f0478e04d3e4d080a3f`.
The custody report records the exact source, native compact certificate,
constructor, support geometry, Hankel arithmetic and checkpoint codec
bindings. A different aperture's checkpoint is rejected.

The original runs reached residual assembly and logged maximum residual
entry width approximately 3.041949685829048e-114. They stopped during the
subsequent sign stage and emitted no final certificate. The unchanged
complete checkpoint permits recovery without repeating any support panel.

The independent pairing auditor recomputes the endpoint-log projection
moments through exact rational integer Hankel arithmetic. It verifies all
7,056 native/source pairing enclosures, accounts for both interval widths,
and checks that each interval gap is below its actual source approximation
allowance. All 7,056 deliberately displaced pairs are rejected. No original
source-only pairing gate fails at this aperture. The actual source-map
approximation bound is unchanged. This auditor and both complete panel
checkpoints repeat byte for byte.

A separate export stage now runs the unchanged constructor on each complete
checkpoint and observes its result immediately before the first positive
pivot call. It verifies that the call comes from the original compute
function and receives that function's G matrix, captures the fully assembled
residual Gram and approximation error fields, and stops before sign work.
It changes no numerical operation before that boundary and leaves the
original constructor file and its checkpoint binding unchanged. The export
runs are still pending at this checkpoint.

This closes all nine panel contractions and their independent pairing
custody. The exported complete residual Gram certificate, its repeat and
corrected Schur sign remain pending. The matching native finite restriction,
source certificate and depth-six complete complement are already in custody.
No whole-domain positivity at 23/25 is claimed. The whole-domain frontier is
91/100; F4, full transport, global endpoint exclusion and historical
attachment remain open. The separate global-lane work, Lean and workflows
are unchanged.

## Custody and recovery

- `notes/data/RPB108_PRIME5_GRAM84_092_COMPLETE_PANEL_CHECKPOINT_20261006.json.gz`
- `notes/data/RPB108_PRIME5_GRAM84_092_COMPLETE_PANEL_CUSTODY_20261006.json`
- `notes/data/RPB108_PRIME5_PAIRING_ENCLOSURES_092_VALIDATION_20261006.json`
- `scripts/extract_native_prime5_gram84_092.py`
- `scripts/validate_native_prime5_pairing_enclosures_092.py`

Decompress the checkpoint, verify its hash, then run:

```sh
python scripts/extract_native_prime5_gram84_092.py complete_checkpoint.json
```

This command exports a complete residual Gram with corrected sign explicitly
pending. It does not supply a whole-domain positivity certificate.
