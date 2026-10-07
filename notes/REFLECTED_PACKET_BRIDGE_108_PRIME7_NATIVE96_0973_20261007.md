# RPB108: actual prime-7 native 96-vector block at 973/1000

Definitions: [prime-7 native restriction and finite-sign scope](../docs/TERMINOLOGY_RPB108_PRIME7_NATIVE96_0973.md). This continues the eleven-panel/96-moment preflight published in commit 50c9f97e17ecb9f90d6c348d2f9778afe165f054. All historical aperture scripts, certificates and terminology are unchanged.

The complete actual native restriction on physical Legendre degrees 0..95 at aperture 973/1000 is now constructed with prime powers 2,3,4,5,7 retained. The archimedean multiplier and pole are unchanged. The new engine accepts only this aperture, degree 95 and matrix-return route. Its bounds explicitly use log(7)<2a<log(8), log(5)<4a<log(50), exponential remainder constant 50 and kernel constant 973/200; the historical constant 49 is not reused. Orders are 300 exponential, 300 Bernoulli pairs, gamma order 20 and 220 logarithm terms, on a 400-digit outward rational grid.

All 96 raw rows were constructed from zero and persisted in the complete hash-bound checkpoint, with 4656 lower-triangle entries. The finite sign is finalized separately on the exact even/odd parity decomposition at 160 digits. All 96 pivots and all 96 shifted pivots are positive, giving finite physical margin 1/2147483648000000000000000000, approximately 4.656612873077393e-28. The largest physical native entry width is approximately 4.211669136437853e-41, below 1e-35. A separate outward compact enclosure on the 80-digit grid passes both shifted parity blocks with the same margin.

Native finalization and compact outputs each repeat byte for byte from the completed raw checkpoint. This is one full raw native construction, not two. An actual independent fresh-versus-resumed first-two-row test agrees exactly, including the newly added prime term. The raw-to-physical audit independently recomputes all 9216 signed normalized entries and all 9216 compact inclusions, verifies constructor and finalization bindings and checks all stored positive shifted pivots. Negative sign controls are rejected. No overlap with a previous aperture's matrix is asserted, since the aperture and operator have changed.

The newly entering prime-7 term is independently checked using endpoint Legendre expansions and exact Beta moments on its small support strip. This route avoids the constructor's correlation antiderivative/Horner algorithm. At 450 logarithm terms it verifies 191 correlations covering the complete first row and all 96 diagonal entries, including normalization and exact reflection zeros. The constant-mode prime-7 contribution is approximately 6.791779386247823e-5 and strictly exceeds 6e-5; the omitted-prime control is rejected. The historical prime-4 coefficient remains log(2), not log(4).

[Custody manifest](data/RPB108_PRIME7_NATIVE96_0973_CUSTODY_20261007.json) binds the scripts, complete raw rows, physical certificate, compact enclosure and all audits. Native archives use the established UTF-8 base64 gzip transport; restoration verifies compressed and decoded hashes and restores the decoded physical JSON for audit tools. Repeat the archived checks with:

```sh
python scripts/restore_native_prime7_96_0973_archives.py
python scripts/finalize_native_prime7_matrix96_0973.py notes/data/RPB108_PRIME7_NATIVE96_0973_COMPLETE_RAW_ROWS_20261007.json.gz > native7_repeat.json
python scripts/compact_native_prime7_matrix96_0973.py --input native7_repeat.json --output compact7_repeat.json
python scripts/validate_native_prime7_matrix96_0973.py notes/data/RPB108_PRIME7_NATIVE96_0973_CERTIFICATE_20261007.json native7_repeat.json notes/data/RPB108_PRIME7_NATIVE96_0973_COMPLETE_RAW_ROWS_20261007.json.gz notes/data/RPB108_PRIME7_MATRIX96_0973_COMPACT80_20261007.json compact7_repeat.json
python scripts/validate_native_prime7_correlation96_0973.py
python scripts/validate_native_matrix96_row_recovery_0973.py
```

The already proved complement lower 423/500 is separate. Finite positivity and positive complement do not certify their cross coupling. Next: fresh actual eleven-panel 96-source approximation and complete error aggregation, then matched residual Gram, all source/native pairings, actual delta=eta(2M+eta) and corrected Schur sign. The old nine-panel source and its error allowance cannot certify the new target.

Whole-domain positivity remains certified through 97/100 with physical lower 9e-30 and Elog lower 4e-32. This pass certifies the finite restriction only at 973/1000. No target whole-domain positivity, global endpoint exclusion, F4, full transport, Lean or RH closure is claimed. Concurrent global/F4 work is preserved.
