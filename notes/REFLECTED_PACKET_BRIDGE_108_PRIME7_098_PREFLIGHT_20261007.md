# RPB108: eleven-panel aperture 49/50 preflight

Definitions: [49/50 preflight scope](../docs/TERMINOLOGY_RPB108_PRIME7_098_PREFLIGHT.md).
This continues the published whole-domain 973/1000 certificate e8746a5cf6ed92bac69cda54a5a76ac773db66f8. Historical certificates are unchanged.

At target 49/50, exact finer-log geometry audits retain prime powers 2,3,4,5,7 and all eleven panels. All 110 signed translation tests pass. The prime-7 paired strips remain disjoint; small overlap does not justify omission of their operator term.

Two fresh depth-eight weighted Schur constructions repeat byte for byte. The independent 140-digit linear-log audit checks all 1741 refined cells and 17410 signed transitions, every translated target cut and every exact rational weighted inequality. The resulting full supported prime norm upper bound is 1.899882. Omission of an essential translated cut and a smaller majorant for the same weights are rejected. This is not an operator-norm lower estimate.

With 96 retained physical Legendre coordinates and frequency cutoffs 14, 74/5, 77/5, the three-band archimedean-minus-prime-and-pole complement is approximately 0.8327174306316002. Its downward-rounded bound is 104/125. Independent degree recurrences audit all 144 damped terms, three infinite tails, finer Machin/log enclosures and all four pointwise step regions. Invalid positive-region controls are rejected. The complete constructor also repeats byte for byte.

At this target 4a=98/25 exceeds log(50), so the previous exponential remainder constant 50 is rejected and replaced with 51, verified by 4a<log(51). Kernel remainder constant is 5a=49/10. With orders 300/300 the independently reconstructed degree-95 diagonal truncation width is approximately 3.185677e-39; orders 260/260 give approximately 1.960723e-24 and are rejected. This is only the highest diagonal preflight; all actual native entries remain pending.

For source exponential order 90, the old 102 Bernoulli pairs give analytic map allowance approximately 2.850338e-34, exceeding the chosen 2e-34 target before rounding. Increasing to 104 pairs gives approximately 5.094757e-35. The exact rational audit includes all 96 normalized column truncation budgets and decreasing alternating kernel coefficients. Interval radii and quantization are excluded here, so no complete source-map certificate is claimed.

Restore the hash-bound transport and reproduce the checks:

```sh
python scripts/restore_native_prime7_098_preflight_archive.py
python scripts/certify_native_prime7_geometry_098.py > geometry098_repeat.json
python scripts/validate_native_prime7_geometry_098.py notes/data/RPB108_PRIME7_GEOMETRY_098_CERTIFICATE_20261007.json geometry098_repeat.json
python scripts/certify_native_prime7_weighted_schur_098.py > prime098_first.json
python scripts/certify_native_prime7_weighted_schur_098.py > prime098_second.json
python scripts/validate_native_prime7_weighted_schur_098.py prime098_first.json prime098_second.json
python scripts/certify_native_prime7_96_preflight_098.py > complement098_repeat.json
python scripts/validate_native_prime7_96_preflight_098.py complement098_repeat.json
python scripts/certify_native_prime7_source_budget_098.py
```

[Custody manifest](data/RPB108_PRIME7_098_PREFLIGHT_CUSTODY_20261007.json) binds scripts, outputs, compressed/decoded prime archives and unchanged dependencies. Next: fresh native block at 49/50, source using 104 pairs with complete error aggregation, matched eleven-panel Gram, actual source-error correction and corrected Schur test with the proved complement. Whole-domain frontier remains 973/1000 with its published bounds; no 49/50 positivity, global endpoint, F4, full transport, Lean or RH closure is claimed. Concurrent global/F4 work is preserved.
