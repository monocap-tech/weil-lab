# NF649 — complete first 15-source physical Gram block target, signed-key correction

## Status and scheduling decision

NF648 #679 is the latest stacked PR at inspection. No newer kernel closure was visible. Its head 55f93a25bcb615bb48002d47a2dbe31bf965fcb8 returned 68 pull-request workflow runs, all queued, including historical unrelated trials; relevant NF641–648 and NF627 literal jobs were also queued. Opening another stacked PR would risk repeating the backlog. NF649 is therefore staged on a separate branch with no PR or automatic workflow added at this step. No cancellation or mutation of existing CI runs; connector does not expose cancellation. The existing NF648 three-group trials remain unchanged.

## Actual local source scope

Read the original NF545 source signature: indices 0..13 are exactly the fourteen degrees of f=37/64; index 241 is the genuine sinh pole. Their 15x15 principal Gram block has 120 lower-triangle entries (225 total by symmetry if independently transferred). Four signed source pairs per lower entry give 480 queries.

**Correction caught by the first route audit:** the three NF648 tables are insufficient for all mixed terms. Canonicalization negates BOTH h and f, not f alone. The original fourth key (-1/2,37/64) has 14 degrees. It uses the very same ten endpoint leaves, with the two real signs interchanged; do not identify the two numerical tables by conjugacy or assume their reference-rounded centers agree. NF648 optional --opposite-mixed includes this fourth table (default three-group mode unchanged).

| Canonical key | Distinct degrees | Queries |
|---|---:|---:|
| (1,0) | 1 | 2 |
| (0,37/32) | 27 | 210 |
| (1/2,37/64) | 14 | 28 |
| (-1/2,37/64) | 14 | 28 |
| zero | 27 | 212 |

All 480 source-derived routes passed after correction; all 56 canonical nonzero degrees plus 27 exact zero degrees consumed. Original three-table proposal omitted 28 pair queries (caught before a retained-artifact or kernel proof claim). Independent 2600-digit BigInt arithmetic reconstructed all ten endpoint values, 56 nonzero moment payments and all 120 physical entries using both NF622 external coefficient-scale and actual NF622PairRect rounded reference arithmetic. All 120 widened radii required an increase, every one-unit underpayment rejected, maximal reconstructed widening radius 1861198149186/Q. This was a separate source-derived numerical replay, not retained byte verification or Lean execution.

## Proposed local physical enclosure theorem and emitter

Generic local lookup transfer from per-table analytical enclosures, canonical sign restoration and exact zero moments. For each actual source pair, require original NF624LookupCheck; require four checked signed pair routes per H entry. Transport through NF622H_of_specs and the original NF591Ball.contains_widen inequality to the retained widened NF631 ball. No full-bank or global-coverage hypothesis. NF649 emitter checks common source shard digests and NF631 widening summary/entry hashes, selected source signature, all 120 retained radii against the actual reference-entry arithmetic, and produces a small four-table bank with 120 route and widening gates and 120 containment theorems, grouped into 15 row modules. Only degree-index hypotheses discharged by the local four-table proofs; no assumed entry truth in terminal targets.

New generic proof candidate and emitters were not executed on actual retained artifacts or in Lean in this session. Existing NF648 three local analytic trials are prerequisites for the extended proof plan. Full physical solve, global Weil positivity and RH remain open. No main merge.

## Bounded future trial runbook

On an adequately provisioned runner at this branch with the pinned Lean toolchain, obtain exactly the original retained artifacts, not regenerated replacements:

- NF632 full pi proposals: run 44359888464 artifact nf632-full-pi-proposals, extract beneath WeilDefect/Generated/NF632.
- NF635 full endpoints: run 44364429357 artifact nf635-original-complete-endpoint-proposals, extract beneath inputs/bank.
- NF621 all eight shards: run 44338849733 matching nf621-shard-* beneath inputs/shards.
- NF631 reference widened entries and summary: run 44359078922 artifact nf631-reference-widened-entries beneath inputs/widened.

```bash
python scripts/emit_nf648_ten_leaf_moments.py --root . --shards inputs/shards --bank inputs/bank --pi WeilDefect/Generated/NF632 --output WeilDefect/Generated/NF648 --opposite-mixed
python scripts/emit_nf649_local_gram_block.py --root . --shards inputs/shards --moments WeilDefect/Generated/NF648 --entries inputs/widened/nf631-widened-entries.jsonl.gz --summary inputs/widened/nf631-widening.json --output WeilDefect/Generated/NF649
lake build WeilDefect.Arithmetic.ActualZetaOriginalPhysicalLocalGramBlock
lake build WeilDefect.Generated.NF649.Complete
```

The terminal Complete import audits representative actual containment theorems and builds every lower-triangle row module. Do not characterize this principal subblock as the full 242-source physical matrix.

Next: inspect CI queue and recover accepted runs before opening additional automatic workflow trials. Prioritize correction of observed errors and actual retained-code execution rather than extending uncompiled proof architecture.
