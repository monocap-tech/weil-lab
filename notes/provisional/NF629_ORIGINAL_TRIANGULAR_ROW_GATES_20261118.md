# NF629 — physical triangular-entry and row-local closure

Status: new proof candidates and actual source-row kernel trial; not new Lean acceptance.

## Verified standing on inspection

NF628 head a8247b8d83c64b8ebc9f7b69098b54f44d9f7edf: the focused NF628 and repaired NF625 workflows were queued (44349024956, 44349026448). NF627 literal bank workflow 44346029525 queued. NF621 complete production and aggregate coverage succeeded on run 44338849733; kernel trial 134922907973 still running, full entry assembly 134946643277 queued. Historical baseline payments succeeded, not yet the moment-derived full matrix payments. No new upstream compiler diagnostic available at inspection.

## Mathematical reduction

Use the incumbent exact neutralNF606PhysicalH_symm. Only lower triangular H entries require an analytic widening comparison. Upper triangular entries must pass exact center symmetry. The proof transports the true physical enclosure across symmetry; it does NOT require the interval evaluator to produce symmetric rectangles. All mixed V entries remain individually checked.

Counts: H 58,564 -> 29,403 analytic widening comparisons; 29,161 cheap exact center-symmetry comparisons instead; all 968 V comparisons retained. Total analytic widening comparisons 30,371 rather than 59,532. A separate synthetic exact-integer experiment (100 symmetric true matrices, 7,599 transported entries) passed, and rejected 200 injected asymmetric-center / excessive-radius mutations. This independent experiment was not the Lean checker and not the historical data.

Cache dot-product and vector equalities, and scalar box payments, now expose row-local Boolean gates. The composition uses separately supplied row truths. The new final conditional theorem returns the unique intrinsic physical solution in the original frozen box and retains all previous bank, shape, source-coverage, and parameter checks.

## Actual source-row pilot

The emitter reads the audited eight genuine moment shards, selects the necessary canonical keys/degrees for H[0,0] and V[0,0..3], and reassembles all actual first-row H centers plus four V centers. It generates a partial bank, a local source-key lookup gate, and a row-zero triangular widening gate. Unused rows of the payment-data record are placeholders; it is not a full numerical solution. It deliberately adds 10^50 / 10^2600 to pilot radii; these relaxed radii are NOT the final payment radii. The workflow binds input hashes to the accepted aggregate manifest and separately compiles the generic row theorem.

The emitter and all new Lean declarations are pending CI. No full-bank kernel truth, final actual moment-derived payments, new local margin certification or global positivity/RH claim. No main merge.
