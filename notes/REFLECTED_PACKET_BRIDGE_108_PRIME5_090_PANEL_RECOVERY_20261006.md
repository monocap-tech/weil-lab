# RPB108: durable 9/10 Gram recovery

Matched-input custody: `8989e6db22b8d9d1a800000b7bc5b39abef0ff2b`.
Definitions: [complete panel checkpoints](../docs/TERMINOLOGY_RPB108_GRAM_CHECKPOINT.md).

Earlier Gram subprocesses stopped before writing complete outputs. Their partial logs are not certificates and are not counted as successful repetitions. The matched native, source, complement and reordered Hankel inputs remain in GitHub custody.

The Gram constructor now accepts an optional checkpoint path. After each whole panel it atomically saves all three cumulative interval matrices. Recovery checks exact input bindings and reconstructs lossless fixed-grid endpoints, then resumes at the next panel. Endpoint primitives are recomputed; the full projection and rigorous final sign decision remain required.

The codec validation checks exact endpoint round trips at the 300-digit grid, rejects a changed source binding and rejects an incomplete matrix. The report is `notes/data/RPB108_GRAM_CHECKPOINT_VALIDATION_20261006.json`. Two fresh Gram runs use distinct checkpoint paths and will be compared only after complete outputs exist.

The certified whole-domain frontier remains 22/25. No 9/10 sign has yet been certified. F4, global endpoint exclusion, historical packet attachment and FULL TRANSPORT CLOSED remain open. This recovery changes no Lean files, axioms, workflows or CI configuration.
