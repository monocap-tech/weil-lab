# DNE50: complete original source Grams and full response test

The complete original source Grams are certified. Positive subspaces of the paid comparison cover 109 retained directions with the entire high space; 3 retained directions remain uncovered.

New independent checks: **121,430 PASS** (75,093 source, 22,376 full-response test, 23,961 positive-subspace). All 1248 new source correlations have been integrated in separate primary/replay runs. RH and Lean remain open.

Mathematical parent: DNE49 `bb68642b1384d50d6b9fea517db9691e924fe5a5`. Preparation commits: `e8b30ec42d7402362224bbb80f816f01768a7392`, `fd0434979302083c01f9f20cc30fae42f62211d7`. The branch is `research/rpb108-direct-null-exclusion`; other branches were not changed.

## Complete original source certificate

The exact frozen packet is Z56=(T4*S,X[0:52]), in both parities. The DNE49 retained chart audit proves full rank 56 per parity. Neither its columns nor the original native matrix were changed. The even source order is Z44,Y0,Y1,Y2,X40,...,X51 (59 columns); odd is Z44,X40,...,X51 (56 columns). The even native-to-source map is 0:44 followed by 47:59. High trials are not additional retained directions.

| Parity | Reused source size | New native columns | New upper correlations | Source audit checks |
|---|---:|---:|---:|---:|
| even | 47 | 12 | 642 | 39282 |
| odd | 44 | 12 | 606 | 35811 |

Both parities were computed at N360/P600 and independently replayed at N400/P620. The producer preserves the DNE48 even 47-by-47 and DNE44 odd 44-by-44 source blocks literally. Source polynomials are reconstructed for new mixed integrals, but old source entries are neither integrated again nor replaced. Every new pair is evaluated analytically over all seven half-interval panels, including the archimedean endpoint logarithms, regular kernel, signed poles and all six active prime powers in both orientations. No sampled quadrature is used.

The common polynomial grid is 10^250, stored moment coefficients are outward integers on the precision grid, and output source coordinates are rounded outward to 100 decimal places. The same analytic operator error bound, polynomial/log rounding and physical L2 payments are paid separately for every source and correlation. Exactly all 56 same-parity retained source coordinates are subtracted. New coordinates are integrated only for the twelve added columns. The complete even high-trial action coordinates are copied unchanged.

The independent auditor authenticates the old source validation hashes and the full DNE49 packet, checks every old prefix entry, norm, projection, payment, symmetry and dimension, and verifies primary/replay nesting of every paid Gram entry. It checks the new retained-coordinate overlaps after whole-source error payments. The exact signed convolution implementation matches the previously checked DNE44 implementation.

## Paid full response test

The original infinite high floor remains k=647/1000. The even residual-response upper uses the three inherited exact physical high trial vectors. With f=P_F L_original Z56 and Y the high trials, define G=f*f, B=f*(L_F Y), D=(L_F Y)*(L_F Y), M=f*Y, A=Y*L_F Y, E=B-k*M, W=D-k*A. The complete paid M is supplied by DNE49, using complete original high-trial action coordinates and their physical norm payments; A is unchanged from DNE48. G, B and D are now available from the complete source matrix with the explicit source/native map.

The producer checks W>0 and freezes a rational 3-by-56 J on the 10^-25 grid. It pays every entry of C=EJ+J*E*-J*WJ and H=k*N-G+C. The completed-square residual identity gives N-f*L_F^-1*f >= H/k. Odd uses H=k*N-G. Decimal and NumPy arithmetic only propose rational witnesses; all sign conclusions come from exact outward interval congruences and positive Gershgorin margins. The actual infinite inverse is never evaluated.

| Parity | Full 56-column budget | Certified retained rank | Physical gap lower, approximate |
|---|---|---:|---:|
| even | not certified | 55 | 1.996760286473e-39 |
| odd | not certified | 54 | 2.710527760766e-35 |

For even, an exact trial of the sufficient comparison budget has strict negative upper bound: True. This tests the chosen sufficient upper only. It is not negativity of the original Weil form; the authenticated prior 44-direction result is retained.

For odd, an exact trial of the sufficient comparison budget has strict negative upper bound: True. This tests the chosen sufficient upper only. It is not negativity of the original Weil form; the authenticated prior 44-direction result is retained.

## Maximal positive comparison subspaces

The full budgets fail, but a rational completed-square chart preserves the first 44 native coordinates literally and identifies the positive portions of the remaining 12-coordinate block. Independent certificates prove positive compressed budgets, strictly negative comparison complements, and a nonsingular full bottom coordinate chart. Thus the chosen even budget has exact inertia (55,1,0), and odd has (54,2,0). These are indices of the sufficient comparison only, not indices of the original Weil form.

The new positive embeddings B contain identity columns for every old Z44 coordinate. Together with the complete high space, their original positive packets have retained ranks 55 and 54. All prior 88 retained directions are included exactly. The three unresolved directions lie inside the complete computed native packet; none lies outside it.

Physical mass and source trace are conservatively bounded by the full native packet mass and trace multiplied by the exact squared Frobenius norm of B. The independent audit checks both products and the physical gap formula. This avoids confusing native normalization with physical L2 mass.

The common physical gap lower for the 109-direction packet is approximately 1.996760286473e-39; a conservative exact guard is `1/1000000000000000000000000000000000000000`.

Actual certified all-high retained rank: 109; uncovered retained dimension: 3. The full source computation is finished, so remaining work concerns the response comparison rather than missing source integrals. The old 88-direction result and its common physical guard 1e-37 remain valid. No whole-aperture positivity claim is made.

For each certified positive subspace, the physical guard follows from its exact Schur coefficient floor sf, physical packet mass upper bound mass, projected source trace upper bound trace and k:

    gap=min(sf/(4*(mass+trace/k^2)),k/2).

The independent response auditor reconstructs every mapped G entry, every mixed E and W entry, rational credit, full paid budget, congruence, Schur floor and physical gap. It authenticates the full chart and prior 88-direction certificate. The source and response audit counts are new and exclude inherited checks.

## Reproduction and custody

Use the producer, packer and source-audit commands in the immutable preparation checkpoint. After both source audits PASS, combine their records as in the complete-source validation, then run:

```sh
python scripts/combine_dne50_source_validations.py
python scripts/certify_dne50_full_response.py --output notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64
python scripts/validate_dne50_full_response.py notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64 --output notes/data/RPB108_DNE50_FULL_RESPONSE_VALIDATION_20261010.json
python scripts/certify_dne50_positive_subspaces.py --output notes/data/RPB108_DNE50_POSITIVE_SUBSPACES_20261010.json.gz.b64
python scripts/validate_dne50_positive_subspaces.py notes/data/RPB108_DNE50_POSITIVE_SUBSPACES_20261010.json.gz.b64 --output notes/data/RPB108_DNE50_POSITIVE_SUBSPACE_VALIDATION_20261010.json
```

All producer, audit and packing scripts compile. All four producer jobs and both final audit pipelines finished successfully. There are no unfinished computational jobs. Certificate references use SHA256 of decoded JSON bytes; custody references use SHA256 of stored bytes. Historical artifacts and wording remain unchanged.
