# NF631 — full physical entry production and reference-compatible payments

Status: major upstream numerical and Lean milestones verified; new reference-compatible payment replay pending.

## Confirmed changed standings

- NF621 run 44338849733, entry assembly job 134946643277 PASS: all 29,403 lower triangular H and 968 V entries, radii H < 10^-2587 and V < 10^-2583. Artifact 14448816424, zip SHA256 36fbc40be4f7f8524367bd27cc1230035d351599c3a4d4c11645c7e21b4d5ea9. External arithmetic only; moment-derived transformed-payment job 134968354605 still queued at inspection.
- NF628 run 44349024956, chunk-composition job 134959216496 LEAN PASS, including repaired literal source-spec and moment-bank dependencies. Rational payment job 134959217364 LEAN PASS. Full chunked closure still running.
- NF627 emitter job 134948528621 PASS. Generic metadata theorem job 134948527957 failed because the binder 'meta' is reserved Lean syntax. Rename it in metadata, chunked closure and row closure modules. No mathematical theorem changes.
- NF628 concrete two-key pilot job 134959216100 built both actual literal key chunks and the chunk-composition proof, then runner shutdown/exit 143 during kernel truth compilation. No actual gate truth certified. NF621 earlier trial had also been interrupted. NF629 and NF630 focused tests not yet available.

## Reference widening rather than untested radius slack

NF622 external assembly scales moments by an exact product coefficient, whereas NF622PairRect in Lean uses two sequential rounded rectangular products. Even if both enclose the same analytical entry, the old numerical interval need not contain the entire reference interval. The exact formal gate requires that latter property.

For original external center m and radius r, and the reference rectangle's real center n and radius s (all integer units on Q=10^2600), set
  R = max(r, |n-m|+s).
This preserves each historical center and its old enclosure while paying the exact reference-widening obligation. No arbitrary decimal safety pad is used. The new external evaluator mirrors NF591Ball.exactQ and NF591Rect.mulQ using the existing fixed-point integer arithmetic. All 30,371 independent entries from the accepted artifact will be checked against the audited eight moment shards. The resulting widened entries are passed through the original exact uniform transformed payment and cache producer, so any enlarged radius must pay all 242 original coefficient gates again.

New workflow runs automatically on the draft PR using already available immutable-run artifacts. Exact external reference arithmetic is not itself the Lean gate truth. Independent synthetic integer test (100 cases) checked the minimal widening calculation and rejected every one-unit insufficient radius; the committed script's own 100 rational reference tests and complete actual replay await CI.

No main merge, no new actual reference-widening acceptance, no full literal kernel truth, no unconditional intrinsic physical solve or global Weil/RH promotion.
