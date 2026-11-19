# NF677 — complete original literal scalar payment kernel replay

## Purpose and historical status

NF676 run 44525811530 was still active/queued at NF677 inspection. Instead of duplicating its proof repairs or first literal analytical H/V entry trial, this stage targets a genuinely separate finite numerical workload: every original NF639 scalar payment row, using the unchanged isolated scalar core (NF653).

NF654 had already prepared an exact external arithmetic replay and proposed a full scalar build on a push/manual-only branch. Its actual push-run outcome was not accessible through the pull-request-only workflow listing, so neither a complete prior Lean PASS nor a prior numerical failure is asserted here. NF677 makes the complete execution and its kernel audit directly traceable under a focused PR-triggered workflow.

## Original source and proof obligations

- Original NF639 scalar proposal artifact 14472975687, archive SHA256 7c4e6f03364ed0290a54683c5b52688a0478a32ae00625b3e5f6f4231ad54582.
- Original NF631 widened payment artifact 14458146136, archive SHA256 8cbae72a7714dc555c0183edfbbda077096ef910b1e284d4abc91c4960d95e6e.
- Original scalar manifest SHA256 efcb46ca6eabeae80d0beb21f8627773d23b71002c26fed82f68f47e56bbf896, all 243 literal source hashes, and the exact frozen NF407 source SHA and normalized coefficient-box SHA checked by the retained NF654 preparer.

The retained literal theorem for source i is nf639RowNNNCheck. It checks three exact rational inequalities using the original retained numerators and frozen-source midpoint/radius:
1. rowFee <= 1/100;
2. residualFee <= r;
3. selectedFee <= NF625Rad(i).

There are 242 literal kernel Boolean gates, comprising 726 scalar inequalities. The source files for all 242 row theorems are kept byte-identical. The only allowed normalization of Params.lean is replacement of the historical import by the already-isolated ActualZetaOriginalPhysicalScalarPaymentCore import; both variants are accepted only after authentic original hashes have been verified.

## Execution

New workflow nf677-complete-scalar-payments.yml pins both original archive digests, uses the existing NF654 preparer to independently reconcile all 726 scalar fees with the actual original frozen source and retained receipt, and then executes the actual Lean theorem proofs in four disjoint ranges (0–60, 61–120, 121–181, 182–241) with bounded batches of eight. Each shard separately runs #print axioms on every compiled literal theorem, insists on exactly one print per expected declaration and a subset of the three standard axioms, and records the exact source SHA for each row. A final job requires successful shards, matching original source/preflight hashes, complete coverage of indices 0..241 exactly once, and standard-axiom-only output.

No actual previous NF654 proof verdict could be retrieved, and NF677's new runs are pending until GitHub Actions completes. The retained external numerical replay is not the same as kernel acceptance. Even a full NF677 success establishes all literal scalar inequalities on the proposed numerators, **not** the validity of the cached products, their mass/defect bindings to the complete original inputs, or the original analytical H/V entry enclosure checks. It does not by itself discharge the complete hpay Boolean on the actual global cache. No global signed Weil positivity, unconditional Phase III closure, or RH result is claimed.

Next: inspect the four NF676 jobs and NF677's actual kernel output. After all literal scalar gates have passed, attach the now-certified row numerators to the actual original cache via NF639/NF640 binding and exact mass/dot-product proofs.
