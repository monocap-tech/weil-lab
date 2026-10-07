# RPB108: complete eleven-panel actual source at 973/1000

Definitions: [eleven-panel source and error-map scope](../docs/TERMINOLOGY_RPB108_PRIME7_SOURCE96_0973.md). This continues the complete actual native block, commit df6ce55bb542ef47632ede187873b4276b1ee952. Historical source scripts and certificates are unchanged.

The actual source approximation on physical Legendre degrees 0..95 at aperture 973/1000 now retains all supported prime powers 2,3,4,5,7. The two prime-7 edge panels are included explicitly, with amplitude log(7)/sqrt(7), and the prime-power-4 coefficient remains log(2)/2. The exact endpoint-log contribution is kept separately for the residual Gram; it is not replaced by a polynomial or dropped.

The new target requires a repaired Bernoulli budget. An independent exact aggregation using the old 100 pairs gives an analytic column-map budget above 3.710036e-34 even before coefficient rounding, exceeding the chosen 2e-34 target. The new calculation uses 102 pairs, exponential order 90, gamma order 50, 220 logarithm terms and 400-digit outward intervals. Its analytic budget before coefficient rounding is approximately 6.441546e-35. All 102 kernel coefficient magnitudes decrease with alternating signs, proving the 9/4 polynomial-kernel ceiling used by the error calculation.

After retaining interval radii and 40-digit coefficient-rounding errors, the complete normalized source-map allowance is approximately 6.599752767135603e-35 < 2e-34. Independent audit reconstructs the analytic remainder for every row, verifies the physical normalization and complete squared-error aggregation across all 96 columns, and checks all 1056 panel encodings. It also rejects the old 100-pair budget and an underreported map error. The lossless common-tail codec retains all 294 higher-degree coefficients per row and the degree-dependent panel prefixes.

The independent support audit uses finer logarithm and square-root enclosures on a 500-digit grid. It verifies all eleven open panels and all 110 signed support tests. An independent closed binomial formula for shifted Legendre polynomials checks both new prime-7 edge-profile coefficient jumps for every degree: 192 profiles and 9312 coefficients, with the analytic/quantization radii retained. Omitting any of those 192 profiles is rejected. The core and common tail cancel in these adjacent-panel comparisons, isolating the newly entering actual term without assuming an old source is valid at the new aperture.

The source constructor ran once. Aggregation, coefficient-jump audits and archive restoration do not assert a second complete source construction. All constructor/dependency hashes are bound to the output. [Custody manifest](data/RPB108_PRIME7_SOURCE96_0973_CUSTODY_20261007.json) binds the source transport, scripts and independent audit outputs. Restore the UTF-8 base64 gzip transport and repeat the independent checks with:

```sh
python scripts/restore_native_prime7_source96_0973_archive.py
python scripts/validate_native_prime7_source96_0973.py notes/data/RPB108_PRIME7_SOURCE96_0973_CERTIFICATE_20261007.json.gz
python scripts/validate_native_prime7_source96_edges_0973.py notes/data/RPB108_PRIME7_SOURCE96_0973_CERTIFICATE_20261007.json.gz
```

For a new full construction, run `python scripts/certify_native_prime7_source96_0973.py > source7_fresh.json`; compare its decoded output separately. No fresh-repeat claim is included here.

Next: full matched eleven-panel 96-source residual Gram, all 9216 native/source pairings including both enclosure widths, actual delta=eta(2M+eta), then corrected Schur sign using complement 423/500. The already positive native block and complement do not establish that coupling sign. Whole-domain positivity remains certified through 97/100 with physical lower 9e-30 and Elog lower 4e-32. No target whole-domain positivity, global endpoint exclusion, F4, full transport, Lean or RH closure is claimed. Concurrent global/F4 work is preserved.
