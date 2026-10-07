# RPB108: complete native 96-vector block and eleven-panel source at 49/50

Definitions: [actual native/source scope](../docs/TERMINOLOGY_RPB108_PRIME7_NATIVE_SOURCE96_098.md).
This continues the 49/50 preflight published in ecf53f64e894cb39d1aa0fa635b863beaebfcfd7. Historical 973/1000 certificates remain unchanged.

The fresh actual native restriction retains physical Legendre degrees 0..95, prime powers 2,3,4,5,7 and the pole. All 96 raw rows are complete, with hash-bound 400-digit interval arithmetic and orders 300/300. At 49/50 the exponential remainder guard is 51 and the kernel ceiling is 49/10. The maximum actual physical entry width is approximately 3.18567655e-39.

Finalization into the physical normalized basis proves all 96 pivots and all 96 shifted pivots positive at 160 digits, using exact even/odd parity. The finite physical margin is 1/8589934592000000000000000000. Repeated finalizations from the same complete raw rows are byte-identical. The independently widened 80-digit compact checks repeat byte for byte and verify all 9216 outward inclusions. An exact independent raw-to-physical audit checks all 9216 entries, their symmetry and parity, the hashes of the raw constructor dependencies and the negative control. These repeat claims concern finalization of one full raw construction; no second full raw construction is asserted.

Separate endpoint-Beta evaluation verifies all 191 prime-7 correlations consisting of the first native row and every diagonal, with independent 450-term logarithms and exact normalization/reflection checks. The constant-mode prime-7 contribution is approximately 0.01057435987, so omission is rejected. Actual fresh/resumed first-two-row checkpoints agree, covering 96 raw even entries; this recovery audit does not certify the entire block on its own.

The full fresh 96-column source retains all 1056 panels with prime powers 2,3,4,5,7. Source orders are exponential 90, Bernoulli pairs 104 and gamma 50, using 400-digit outward arithmetic and 40-digit quantization. Complete analytic, interval-radius and rounding aggregation gives eta approximately 5.254941889728036e-35 < 5.26e-35. Independent normalization and error audit checks every column and every panel; the obsolete 102-pair analytic allowance above 2.850337e-34 and an underreported map allowance are rejected. The 104 alternating decreasing kernel coefficients are checked. The new polynomial rows retain all 298 higher-degree common coefficients rather than the historical 294.

Independent 500-digit endpoint/support reconstruction verifies all eleven panels and 110 signed support tests. It checks both prime-7 edge profiles at each degree: 192 profiles and 9312 coefficient jumps, with analytic and quantization radii retained. All 192 omission controls are rejected. The exact universal endpoint-log contribution remains separate for the residual Gram. One complete source construction is asserted, not a second full source run.

Restore the complete lossless archives and reproduce the audits:

```sh
python scripts/restore_native_prime7_native_source96_098_archives.py
python scripts/finalize_native_prime7_matrix96_098.py notes/data/RPB108_PRIME7_NATIVE96_098_COMPLETE_RAW_ROWS_20261007.json.gz > native098_repeat.json
python scripts/compact_native_prime7_matrix96_098.py --input native098_repeat.json --output compact098_repeat.json
python scripts/validate_native_prime7_matrix96_098.py native098_repeat.json native098_repeat.json notes/data/RPB108_PRIME7_NATIVE96_098_COMPLETE_RAW_ROWS_20261007.json.gz notes/data/RPB108_PRIME7_MATRIX96_098_COMPACT80_20261007.json compact098_repeat.json
python scripts/validate_native_prime7_correlation96_098.py
python scripts/validate_native_matrix96_row_recovery_098.py
python scripts/validate_native_prime7_source96_098.py notes/data/RPB108_PRIME7_SOURCE96_098_CERTIFICATE_20261007.json.gz
python scripts/validate_native_prime7_source96_edges_098.py notes/data/RPB108_PRIME7_SOURCE96_098_CERTIFICATE_20261007.json.gz
```

Passing one finalization path twice is a custody check only. To repeat finalization itself, invoke the finalizer twice into distinct output files. To reproduce a full native construction, invoke `complete_native_prime7_raw96_098.py` with an absent checkpoint path. Reproduce the full source with `certify_native_prime7_source96_098.py` and compare its decoded output separately.

[Custody manifest](data/RPB108_PRIME7_NATIVE_SOURCE96_098_CUSTODY_20261007.json) binds all three compressed and decoded archives, transport parts, scripts, audits, compact native enclosure and unchanged dependencies. Restoration checks every archive digest. The complete raw rows retain their historical checkpoint type label; completed_rows=96 records completion. The row-recovery and source audit flags describe their own extraction stages and do not assert whole-domain sign.

The initial publication 17535577eed47cbf1fff80ec843bdc5e9287713b exposed a retrieval-only dependency byte mismatch: local retrieval added one final newline to otherwise exact canonical files. The [byte-normalization audit](data/RPB108_PRIME7_098_DEPENDENCY_BYTE_NORMALIZATION_20261007.json) verifies each canonical dependency against its published Git blob, with only that terminal newline removed. It independently decodes the initial transports and proves that rebinding changes only constructor-hash metadata: every native arithmetic entry and every nonbinding source field is identical. Native finalizations, 80-digit compact checks, raw/physical audits, first-row recovery and complete source/edge audits were then rerun against canonical dependency bytes. The 49/50 preflight manifest's unchanged-dependency bindings are corrected in the same custody repair. No arithmetic claim is obtained by silently changing code or numerical data.

Next: full matched eleven-panel residual Gram, all 9216 pairings with both enclosure widths, independent residual reconstruction, actual delta=eta(2M+eta), and corrected Schur sign using complement 104/125. The finite positive block and positive complement do not yet certify coupling. Whole-domain positivity remains certified through 973/1000 with its published bounds. Global endpoint, F4, full transport and Lean closure remain open; no 49/50 whole-domain positivity or RH closure is claimed. Concurrent global/F4 work is preserved.
