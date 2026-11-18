# NF638 — complete reference-compatible numerical payments PASS; integer table closure

## Recovered major milestone
NF631 run 44359078922, exact-reference-payments job 134995143316 SUCCESS. The exact external reference-rounding replay changed all 29,403 H and 968 V radii without changing their centers. After those widenings, the transformed row defect <=1/100 and ALL 242 selected payments passed again. All eight shard hashes matched audited coverage. Full cache generated. Retained artifacts:
- 14459025571 nf631-reference-widened-entries, sha256:e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9.
- 14458146136 nf631-reference-widened-payments, sha256:8cbae72a7714dc555c0183edfbbda077096ef910b1e284d4abc91c4960d95e6e.
- 14457911117 nf631-reference-center-cache, sha256:bb89b0c7b9bc4017b8c855f0e30474ee8b2f0589e29f99747fff965f44f3b1a7, 210265153 bytes.

These are external exact reference-compatible numerical data, not actual Lean widening or payment gate truth. NF631 focused-metadata failed on i<metadata lexer conflict (matroid <m) and rewrite under let-bound source coverage; repair spacing and dsimp only before rewriting. New compiler acceptance pending. NF632–637 queued at first inspection.

## Integer table closure
The boundary is generated directly by two integer-rounded products of the cached positive/negative endpoints and the exact signed powers, rather than independently storing a high-precision boundary per degree. On Q=10^2600 use c=Q*b^n/10^n for b=+11,-11, paying c*10^n=Q*b^n. Point rectangles and natural scalars have generic exact rational representation lemmas. Candidate table and chunk composition transports all checked integer degree gates to the exact original NF617/NF628 gates. Rows are denoted by a single map of the integer rows, so no separately asserted row identity or per-row boundary identity is needed. Three cache rectangles per key (lambda and two endpoints) and the shared pi/reference equality are still separate attachment obligations.

Independent BigInt replay compared the reconstructed boundaries for the genuine pole, oscillator and mixed tables to an independently written rational product rounding evaluator at every degree: 42/42 exact rectangle matches, 84/84 signed power identities, 84/84 one-unit scalar mutations rejected. This was not the committed Python emitter, nor retained shard byte verification, nor Lean execution.

Emitter prepares three whole-table Boolean gates on the audited shard rows and three zero-denominator rejection tests, plus conditional chunk composition. New focused proof candidates and emitted actual tests are pending CI; no full bank gate or unconditional physical solve. No main merge, no global Weil or RH claim.

Next: prioritize literal payment/cache verification against the now available immutable NF631 artifacts and complete attachment of integer cache/endpoint identities. Avoid unnecessary changes to the successful numerical solve.
