# DNE50 preparation checkpoint — full remaining source integration

Mathematical parent: DNE49 `bb68642b1384d50d6b9fea517db9691e924fe5a5`, on `research/rpb108-direct-null-exclusion`.

The complete audited native chart and source map are now inputs to an additive source extension. Four producers have been launched in separate processes: even/odd N360/P600 primary and N400/P620 replay. This checkpoint precedes completion and makes **no new mathematical certificate claim**. Standing remains 88 all-high retained directions, 24 uncovered, original high floor 647/1000, inherited physical guard 1e-37. Whole-aperture positivity and RH remain open.

The source producer reuses the DNE48 even 47-column block and DNE44 odd 44-column block; new source columns are X40 through X51. It reconstructs rounded source polynomials needed for mixed correlations but never integrates or replaces the old source Gram entries. The whole-source formula, helper hash, signed poles, endpoint logs, all six prime powers in both orientations, seven half-interval panels, physical norm and polynomial payments, and retained projection are unchanged. Coordinates are integrated only for the twelve new native columns and the same 56 retained modes per parity. The inherited complete high-trial action coordinates are copied unchanged.

Expected new upper-triangle correlations: even 642, odd 606, total 1248. The even source matrix is 59-by-59, and the odd matrix is 56-by-56. Both native matrices are 56-by-56. The explicit source/native map must be used in the later response comparison.

New code has compiled. The independent source auditor is prepared but has not passed yet. It authenticates old source validations, reconstructs the audited full packet, checks exact prefix identity, every projection and error payment, physical norms, matrix symmetry, primary/replay nesting and the new retained-coordinate overlaps after whole-source error payments. A PASS record is produced only after these checks execute.

Reproduce the four producers from the repository root, each in its own process:

```sh
DNE16_ORDER=360 DNE16_PRECISION=600 python scripts/certify_dne50_complete_source_Gram.py even --output /tmp/dne50_even_360.json
DNE16_ORDER=400 DNE16_PRECISION=620 python scripts/certify_dne50_complete_source_Gram.py even --output /tmp/dne50_even_400.json
DNE16_ORDER=360 DNE16_PRECISION=600 python scripts/certify_dne50_complete_source_Gram.py odd --output /tmp/dne50_odd_360.json
DNE16_ORDER=400 DNE16_PRECISION=620 python scripts/certify_dne50_complete_source_Gram.py odd --output /tmp/dne50_odd_400.json
python scripts/pack_dne50_complete_sources.py
python scripts/validate_dne50_complete_source.py notes/data/RPB108_DNE50_EVEN_COMPLETE_SOURCE_20261010.json.gz.b64 notes/data/RPB108_DNE50_EVEN_COMPLETE_SOURCE_REPLAY_20261010.json.gz.b64 --output notes/data/RPB108_DNE50_EVEN_SOURCE_VALIDATION_20261010.json
python scripts/validate_dne50_complete_source.py notes/data/RPB108_DNE50_ODD_COMPLETE_SOURCE_20261010.json.gz.b64 notes/data/RPB108_DNE50_ODD_COMPLETE_SOURCE_REPLAY_20261010.json.gz.b64 --output notes/data/RPB108_DNE50_ODD_SOURCE_VALIDATION_20261010.json
```

Panel checkpoints bind the producer hash, exact packet hash, reused source hash, order and precision. They permit resumption of completed panels; source warmup is still reconstructed before resumption. This preparation note is immutable history; a later report and custody will record actual completion or failure.
