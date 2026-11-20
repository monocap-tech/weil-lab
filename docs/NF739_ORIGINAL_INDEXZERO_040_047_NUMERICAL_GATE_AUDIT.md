# NF739 — Original physical HD row zero and A column zero: 040–047

**Canonical iteration:** NF739, following independent Phase III NF737 (#762) and Phase IV NF738 (#763); the canonical numbered ledger is [issue #761](https://github.com/monocap-tech/weil-lab/issues/761).

**Branch:** `research/nf739-original-indexzero-gates-040-047`, stacked **only** on Phase III `research/nf737-remaining-original-indexzero-242-source-schedule`. The Phase IV IV003–IV005 analysis is a separate branch of mathematics and has no dependency here.

## Frozen numerical data and accepted baseline

The work concerns the *actual* original inputs `nf702OriginalInputs : NF626ScaledInputs` and actual complete original center cache `nf703OriginalCache : NF626CenterCache`. The original exact local NF681 242-term products are accepted; new original global proof theorems must attach these products **to those exact complete objects**, not to a surrogate.

Accepted numerical source-specific **index-zero** global matrix gate instances at the verifiable baseline are:
- NF708 first original 0..7: 8 HD and 8 A, run 44640227758, job 135969102426, immutable artifact 14589570565.
- NF713 second 8..15: 8 HD and 8 A, run 44649041852, job 135998999534, immutable artifact 14594190839.
- NF715 third 16..23: 8 HD and 8 A, run 44669131044, job 136065595864, immutable artifact 14599683589.

In addition, NF732/NF733 already certified *universally* all 242 genuine original HD **index-one row** and all 242 genuine original A **index-one column** entries; the accepted custody run 44782027897, job 136446941618, artifact 14652498322, is source/Lean/standard-axiom pinned.

This yields an **independently evidenced baseline of 532 distinct original global HD/A gates**. NF734 indexzero 24–31 and NF737 indexzero 32–39 have separate pending jobs and are **not** prerequisites; no source-only generated gates are counted as accepted.

## New precise source-to-kernel target

`scripts/nf739_original_indexzero_040_047_global_kernel.py` operates only on the authenticated complete `NF704Frontier` source bank produced by the unchanged NF737 emitter, and verifies all source and historical receipt hashes before proposing:

```lean
-- For every integer i with 40 ≤ i < 48:
theorem nf704Col{i}HD :
  nf703OriginalCache.HDGate nf702OriginalInputs 0 (i : Fin 242) = true
theorem nf704Col{i}A :
  nf703OriginalCache.AGate nf702OriginalInputs (i : Fin 242) 0 = true
```

Actual declaration names are `nf704Col040HD`…`nf704Col047HD` and `nf704Col040A`…`nf704Col047A`. Each `ColNNN.lean` contains also the necessary `DGate` and `DProjection` proof declarations: **32 new candidate theorems and three shared original projections audited = 35 declarations**.

The source is an **unchanged original source-generation formula**. NF739 creates no independent fake matrix or trivial Boolean oracle, and does not alter the historical frozen numerical inputs.

## Independent audit architecture

The new CI workflow:
1. Independently replays NF737's full 242-index original source authentication against all *three* accepted original source/axiom archives, original NF702/NF703/NF681 source manifests and the authenticated NF733 index-one universal certificate.
2. Saves the complete unchanged source bank and exact 242-source schedule as a verifiable artifact. Source emission is explicitly **not** a numerical theorem.
3. Restores exactly the accepted NF707 compiled original inputs with matching compiler fingerprint; compiles genuine original NF702 inputs and full NF703 center cache.
4. Directly compiles source modules `Col040` through `Col047` against those real original objects.
5. Runs `#print axioms` for exactly 35 names and requires all names, only standard `[propext, Classical.choice, Quot.sound]` axioms, no `sorryAx`, exact source hashes, and no Lean errors before producing `nf739-original-indexzero-040-047-kernel-audit.json`.

The source pilot does **not** require either NF734 24–31 or NF737 32–39 to pass; successful NF739 would yield another **16 distinct accepted matrix-product identities**, independently bringing the proven distinct total to **at least 548**. It would **not** establish a contiguous prefix from 0 to 47 unless the other pilots separately pass, nor close universal indexzero.

The NF739 job may incur the cost of reconstructing the original center-cache compiled objects and is deliberately limited to eight coordinate modules. It retains source-compilation isolation; no Phase IV IV003–IV005 runner dependency is introduced.

## Verification at creation

**New NF739 original source verification, Lean kernel and axiom audits are PENDING.** No acceptance of the 16 new numerical gate candidates is claimed yet. The NF737 full-bank source job was queued at creation; the NF739 workflow reconstructs the immutable source independently rather than assuming that job's output was successful. Full physical H/V entries, all vector/parameter/payment gates, the entire global HD/A matrix cache, unconditional original Phase III theorem and global Weil positivity / RH remain open.

**Next numerical target:** after restoring current compiler receipts, complete/aggregate original indexzero row/column; then scale the authenticated full-row method to new matrix indices without assuming one row's certificate proves another.
