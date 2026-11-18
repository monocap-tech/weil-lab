# NF630 — original literal scaled payment data

Status: new proof candidates, emitter, and bounded actual pilot; not new Lean acceptance.

## Recovered CI
- NF621 run 44338849733: all eight moment shards and aggregate coverage accepted; numerical historical baseline payments accepted (artifact 14443609129), original frame artifact 14443252637. The high-precision kernel trial job 134922907973 compiled the cached evaluator successfully (8974 jobs), then the runner received a shutdown signal. The actual literal kernel check did not return a success or a mathematical failure.
- The full moment-derived entry assembly job 134946643277 was queued; the entry artifact was not listed at inspection.
- NF625 shard composition job 134936804056 failed through the old NF625 row cast and NF624 source-spec errors; repairs were already committed in NF628 and NF626, respectively. New NF627–629 jobs queued.

## Separate selected-box row interface
For one actual coefficient index i, let d be the exact scaled historical frame row, y the common-scale candidate, and r a proposed residual bound. Check both integer numerators dy = sum_j d_j y_j and mass = sum_j |d_j|. Together with scale positivity, r >= 0 and a scalar rational comparison, these certify the selected-box payment at i. This does NOT establish r as a bound on the physical residual; the transformed row and residual gates remain independent.

The pilot reads the exact historical artifact and the accepted historical baseline payment receipt; validates frozen-source/frame hashes, entry hash and all-pass metadata; independently recomputes the payments for literal rows 0 and 241 and requires equality to the archived receipt. It emits only those rows and the genuine y and r. The first and last row choice is for bounded kernel feasibility, not a claim of exhaustive coverage.

Independent synthetic integer model experiment: 100 rows of 242 entries, 300 injected bad dot/mass/payment-cap mutations all rejected. This is not execution of the committed Python emitter or Lean code.

## Full literal mode
Requires the moment-derived NF622 entry artifact (not Arb centers), matching NF626 cache receipt and NF623 payment receipt. Exact historical frame/candidate, critical vector, scales and uniform radii, row dimensions, hashes and cache input consistency are checked before emitting. Large literal data are split in groups of four rows, then assembled into the actual NF626ScaledInputs and NF626CenterCache. The emitter writes a bounded first-row cache/payment trial; full workflow_dispatch mode emits proposals and does not compile all of them. No new numerical computation or full emitter test was completed locally.

No new physical enclosure truth, final local margin custody, global Weil positivity, RH, or main merge. New CI pending.
