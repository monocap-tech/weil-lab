# RPB108: fresh 19/20 finite/source custody and Gram continuation

Recovered branch head: b7f42bb504ca41032f8215f3f5ea966ede44cf12.
Definitions: docs/TERMINOLOGY_RPB108_MATCHED_095.md.
Custody: notes/data/RPB108_MATCHED_095_CUSTODY_20261007.json.

This is a fresh calculation at a=19/20. No matrix, source, mass or residual
panel from a=47/50 is substituted. Historical certificates remain immutable.

## Completed finite and source stage

The complete 84-row raw native checkpoints agree byte for byte across two
fresh runs. Complete physical matrices and outward 80-digit compact matrices
also repeat exactly. All 84 shifted parity-block pivots are positive for
tau=1/67108864000000000000000000, about 1.4901161193847656e-26.
An independent rational endpoint/isqrt audit checks all 7056 raw-to-physical
entries and all 7056 compact inclusions. Maximum native width is
1.0843106287936872e-36<1e-35. The highest-degree truncation diagnostic rejects
240 Bernoulli pairs and passes 250 before the full run.

The complete 84-source output repeats exactly, SHA256
bf4cb64eb0328add621d22a85f76c9d32bcf852d44a2d3b351ed238f9584b76e.
All 84 normalization/error contributions and all 756 coefficient panels
are checked. The map error is 3.303093893001768e-36<5e-36. An underreported
error control is rejected. Exact Hankel convolution and endpoint-log controls
are checked on the fresh source data. Direct versus resumed native row
recovery repeats; the historical quarter-window golden is unchanged and
six invalid native/source constructor requests are rejected.

## Fresh complement and prime powers

The baseline complement gives 17/50 physically and 9/100 logarithmically.
The two-band comparison at cutoffs 13 and 141/10 gives
0.6593030884750124...>3/5. The old cutoff 71/5 exceeds the proved Bessel
region at a=19/20. All 48 retained degree bounds and complete infinite tails
are independently checked for both fresh masses. The negative outer
single-band intermediate is explicitly not claimed as positive coercivity.

Fresh sixth-power construction covers 165 panels and gives ||T||<=937/500.
Independent exhaustive six-step words verify each panel and prefix.
Fresh tenth-power construction covers 441 panels and gives ||T||<=919/500.
Independent multinomial reachable-state/count checks, integer forward
transfer and 441 sixth-power cross-checks verify every tenth-power row mass.
Both constructor outputs repeat exactly. The audit aggregates all 8^10
oriented words per panel, retaining 45,803,334 across the panels. Smaller
row-mass ceilings are rejected without claiming a lower bound for ||T||.

Replacing the separated prime loss in the same fresh two-band comparison
gives 0.7982182322149314...>399/500. Input hashes are pinned. The independent
direct endpoint sum repeats the inherited complete mass and path audits.
This is complement-only; a matching corrected sign remains pending.

## Resume cursor and limits

Two complete panels (indices 0 and 1) of the fresh residual Gram are saved.
The lossless checkpoint holds all three 84x84 cumulative matrices on grid
10^-300, bound to the fresh source/native inputs and Gram constructor.
Its uncompressed SHA256 is
32984d2119b964dc5314626526d3e85d6877c01a920b83cc68feade19c1d8f0b.
Independent decoding checks 21168 interval entries and rejects a mismatched
source binding. Seven panels, all 7056 final source/native pairings, source
delta, corrected pivots and physical/logarithmic conversion remain pending.

To resume, decompress the archived partial checkpoint into
gram84_095_checkpoint.json, then run:

```sh
python scripts/certify_native_prime5_gram84_095.py --checkpoint gram84_095_checkpoint.json > gram84_095.json
```

The source and tenth-power consumers support their archived gzip inputs.
The finite full matrix can be recovered with the checked finalizer from the
complete raw native archive. The corrected sign must consume the complete
fresh Gram and freshly pinned complement; no promotion follows from the
finite or complement stages alone.

The certified whole-domain frontier stays 47/50, with Q>=3e-29 physical
mass and Q>=1.6e-31 Elog. Global/F4 work on the shared branch is preserved.
F4, global endpoint exclusion and final Lean assembly remain open. Lean is
unchanged. There is no new actual negative native witness or RH claim.
