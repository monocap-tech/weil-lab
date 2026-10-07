# RPB108: first prime-7 aperture and 96-moment preflight at 973/1000

Definitions: [prime-7 preflight terminology](../docs/TERMINOLOGY_RPB108_PRIME7_0973_PREFLIGHT.md). This continues the certified 97/100 whole-domain result, commit 200ba143265914d8fc6d03b81f14bc95a9232a20. Historical certificates are unchanged.

The target 973/1000 crosses the actual prime-entry threshold log(7)/2, approximately 0.9729550745276567, and remains below log(8)/2. Its supported prime-power translations are exactly 2,3,4,5,7, with Lambda(4)=log(2); 6 is not a prime power. The source support geometry now has eleven panels, with prime 7 active only on the two new edge panels. Independent 140-digit logarithm enclosures verify all twelve cut events and all 110 signed translation tests. Reusing the old nine-panel source is rejected.

The prime-7 overlap width is approximately 8.98509446866949e-5. Nevertheless its physical L2 operator norm is exactly log(7)/sqrt(7), approximately 0.7354849040109983. At this aperture the two supported edge strips are disjoint and have equal positive width. The prime-7 operator exchanges the two strip profiles with that amplitude; the exchange is an isometry and equal constant strip profiles attain the norm. Thus its norm does not tend to zero with the overlap width. This concerns the prime-7 summand at the same target aperture, not the difference between full native forms at two apertures. No small-width operator-norm perturbation or omission of the new term is justified.

The complete five-term prime operator has a rational positive weighted Schur bound 1887171/1000000 = 1.887171. A depth-eight offset partition gives 1227 positive weight cells; refinement has 1729 cells and covers all 1602 required translated-cut events. Independent linear-logarithm enclosures recheck all 17290 signed transitions and every exact weighted inequality. An omitted essential target cut and a smaller majorant for the same weights are rejected. The smallest weight is 120965909/500000000000. The floating max-row iteration only generates a candidate. The rational row inequality, together with symmetry of the actual translation kernel and weighted Cauchy-Schwarz, proves the physical L2 bound. No operator-norm lower bound is claimed for this joint operator.

With 96 retained physical Legendre coordinates, cutoffs 14,74/5,77/5 and the new joint prime bound, the complete depth-six mass calculation gives complement lower 423/500 = 0.846; the unrounded lower is approximately 0.8460751111996083. Independent recurrence and finer Machin/logarithm enclosures verify 144 omitted-degree bounds, three infinite tails and four pointwise step regions. The invalid degree-84/cutoff-14 and degree-96/cutoff-16 positive-region controls are rejected. The pole allowance is retained.

The prime threshold simultaneously invalidates the historical exp(4a)<49 guard, since log(49)=2 log(7)<4a. The new truncation budget uses the proved constants exp(4a)<50 and 4a/(1-exp(-4a))<5a=973/200, from log(5)<4a<log(50). With those constants, the degree-95 diagonal fails the 1e-35 width target at orders 260/260 and passes at 300/300. The independent audit reconstructs the standard Legendre coefficients by binomial formula, directly evaluates both correlation integration endpoints and recomputes both complete truncation budgets. This checks only that diagonal budget; all new native entry widths are still pending.

Geometry, full weighted prime certificate and complement preflight each repeat byte for byte. [Custody manifest](data/RPB108_PRIME7_0973_PREFLIGHT_CUSTODY_20261007.json) binds all scripts, transport and independent audits. Restore the weighted certificate, then repeat the checks with:

```sh
python scripts/restore_native_prime7_0973_archive.py
python scripts/certify_native_prime7_geometry_0973.py > geometry7_repeat.json
python scripts/validate_native_prime7_geometry_0973.py notes/data/RPB108_PRIME7_GEOMETRY_0973_CERTIFICATE_20261007.json geometry7_repeat.json
python scripts/certify_native_prime7_weighted_schur_0973.py > weighted7_repeat.json
python -c "import gzip,pathlib; pathlib.Path('weighted7_archived.json').write_bytes(gzip.decompress(pathlib.Path('notes/data/RPB108_PRIME7_WEIGHTED_POINTWISE_0973_CERTIFICATE_20261007.json.gz').read_bytes()))"
python scripts/validate_native_prime7_weighted_schur_0973.py weighted7_archived.json weighted7_repeat.json
python scripts/certify_native_prime7_96_preflight_0973.py > preflight7_repeat.json
python scripts/validate_native_prime7_96_preflight_0973.py preflight7_repeat.json
```

The weighted gzip is published as UTF-8 base64 with compressed and decoded hashes verified on restoration, using the tree-write route already audited at 97/100. The complement preflight includes the exact decoded weighted-input hash.

Next: construct the actual prime-7 native 96-vector block with the repaired remainder constants, followed by the eleven-panel 96-source approximation, complete residual Gram, actual source correction and corrected Schur sign. This preflight is not a sign test; neither the 84-vector obstruction nor the old 96-vector sign threshold determines the new matched result. Whole-domain positivity remains certified through 97/100 with physical lower 9e-30 and Elog lower 4e-32. No positivity at 973/1000, global endpoint exclusion, F4, full transport, Lean or RH closure is claimed. Concurrent global/F4 work is preserved.
