# NF656 — first original 15-source physical Gram interval positivity

**New exact external result:** the NF631 original retained widened physical (H) entry intervals for indices (I=\{0,1,\ldots,13,241\}) admit a strictly positive interval (LDL^T) factorization. All 15 outward-rounded diagonal pivots have strictly positive lower bounds, with original entry radii included. This proves by exact interval arithmetic that **every real symmetric matrix whose 120 lower-triangle entries lie within these retained enclosures is positive definite**, conditional on the standard interval arithmetic and Sylvester/LDL argument. It does **not** establish that the actual analytic physical (H) lies in the enclosures; that is NF655's still-running Lean task. Nor does this finite principal block establish global Weil positivity or RH.

## Original-source custody and arithmetic

Source GitHub NF631 run 44359078922: artifact 14459025571, ZIP SHA256 `e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9`. Inner retained `nf631-widened-entries.jsonl.gz` SHA256 `9e76e2dea4f46ed5fc3ff8875f804c186cd0cacb86c47295f0cd93d189b9f7e6`, cross-checked against original `nf631-widening.json` schema `NF631-reference-widening-v1`; original entry digest `43e81193739d18b699481384bf9c91f5d546a4398005f4c2925426985618bcde`. Used exactly 120 H balls (midpoint, nonnegative radius), with (Q=10^{2600}). No synthetic source or reconstructed matrix substituted.

Enclose each rational interval ([(m-r)/Q,(m+r)/Q]) by floor/ceil into scaled integer endpoints ([\lfloor S(m-r)/Q\rfloor,\lceil S(m+r)/Q\rceil]), (S=10^{160}). For each (k=0,\ldots,14), compute an outward enclosure of the exact symmetric (LDL^T) decomposition recursively:
[
D_k=A_{kk}-\sum_{j<k}L_{kj}^2D_j,\qquad
L_{ik}=\frac{A_{ik}-\sum_{j<k}L_{ij}L_{kj}D_j}{D_k}.
]
Use **integer floor for every lower product/division bound and integer ceiling for every upper**, with the numerator and denominator corner extrema; positive-denominator check is mandatory. This is interval arithmetic, not float or post hoc point eigenvalue estimation.

| Pivot (k) | Outward lower bound (approximation for display) |
|---|---:|
| 0 | (9.63650589\times10^{-1}) |
| 1 | (5.96151371\times10^{-1}) |
| 2 | (7.44118973\times10^{-2}) |
| 3 | (1.99434435\times10^{-3}) |
| 4 | (3.06564580\times10^{-5}) |
| 5 | (3.11309368\times10^{-7}) |
| 6 | (2.24877807\times10^{-9}) |
| 7 | (1.21577076\times10^{-11}) |
| 8 | (5.10634518\times10^{-14}) |
| 9 | (1.71460684\times10^{-16}) |
| 10 | (4.70856248\times10^{-19}) |
| 11 | (1.07724890\times10^{-21}) |
| 12 | (2.08505684\times10^{-24}) |
| 13 | (3.45877687\times10^{-27}) |
| 14 | **(4.94206527\times10^{-46})** |

Each lower pivot is **strictly greater than zero as an exact integer**. At (S=10^{160}), the final pivot enclosure width is approximately (1.681\times10^{-148}), 102–103 orders of magnitude smaller than its lower bound. Independent replays using (S=10^{100},10^{120},10^{140}) all retained positive lower pivots. A separate 110-digit high-precision real-symmetric point eigensolver gave 15 positive center eigenvalues, smallest approximately (2.84551707\times10^{-47}); this is only an independent numerical cross-check, **not** the enclosure proof.

## Formal obligations

1. NF655 Lean: all 120 *physical* H entries belong to the exact widened input intervals; CI run 44420223350, base 106 and cross 14 pending at last inspection. NF648 first 42 moment rows and 73 source prefix modules already accepted; 14 opposite-sign moment rows unverified.
2. Formalize physical block symmetry (or cite an accepted theorem), all-entries interval inclusion, and interval arithmetic soundness/positive LDL transfer to infer (H_I\succ0) in Lean.
3. Strictly distinguish finite principal-block positive definiteness from the already certified canonical Gram positivity and from global signed Weil positivity. No full (242\times242) physical (H) proof, no solve custody, no RH.

New code: `scripts/verify_nf656_original_physical_gram_interval_ldl.py`, syntax: `python scripts/verify_nf656_original_physical_gram_interval_ldl.py --entries nf631-widened-entries.jsonl.gz --summary nf631-widening.json --output nf656-ldl.json`. The script emits exact scaled pivot bounds and cross-checks original SHA digests. It has not been run via a repository CI workflow or imported by Lean; this independent exact trial was executed locally using the same interval recurrence. **No new CI fan-out or main merge.**
