# NF737 — Complete original index-zero source schedule and 28-shard finite-cover contract

**Canonical iteration:** NF737 · **Track:** Phase III numerical custody · **Predecessor:** NF734 [PR #758](https://github.com/monocap-tech/weil-lab/pull/758) · **Global iteration registry:** [Issue #761](https://github.com/monocap-tech/weil-lab/issues/761).

## 1. Accepted originals and unsatisfied numerical facts

The immutable NF733 full source/compiled-object custody audit passed in [run 44782027897](https://github.com/monocap-tech/weil-lab/actions/runs/44782027897), accepted artifact **14652498322**. It attests the two actual original universal Lean claims:

```lean
nf732OriginalHDRowOneAll :
  ∀ i : Fin 242, nf703OriginalCache.HDGate nf702OriginalInputs (1 : Fin 242) i = true
nf732OriginalAColumnOneAll :
  ∀ i : Fin 242, nf703OriginalCache.AGate nf702OriginalInputs i (1 : Fin 242) = true
```

Both were proven with only `[propext, Classical.choice, Quot.sound]`. Separately, original row-zero HD / column-zero A positions 0–23 are Lean accepted through NF708 (0–7), NF713 (8–15), and the earlier NF715 third global matrix frontier (16–23). The source-specific original/global accepted coverage from those exact certificates is **24 + 24 index-zero**, plus **242 + 242 index-one**, totaling **532 distinct original HD/A gate instances**.

NF734 proposes eight further original HD row-zero / A column-zero coordinates 24–31. The newly proposed NF734 gates are **not counted as accepted without successful kernel and strict axiom receipts**.

## 2. NF737's new exact 242-coordinate source bank

The earlier NF704 source emitter and authentic NF681 **242 original local HD/A dot receipts** are sufficient to **propose** every original global first-row gate on the actual NF702/NF703 frozen physical data. NF737 uses the existing authenticated `scripts/nf708_global_matrix_attachment_driver.py` with **`--columns 242`**, rather than inventing a new numerical matrix.

The new `scripts/nf737_original_indexzero_complete_source_shard_schedule.py` requires the three immutable accepted original NF708/NF713/NF715 source and axiom artifacts, their original SHA-256 manifest chains, the same physical input/historical/payment/cache/frame SHA values, and the exact original full NF681 locally accepted product source bank. It checks that every file from `Common.lean` and `Col000.lean` through `Col023.lean` is byte-for-byte **identical** to the accepted third-stage bank.

The emitted original numerical-gate theorem sources have the literal Lean propositions:

```lean
nf704ColNNNHD :
  nf703OriginalCache.HDGate nf702OriginalInputs 0 (NNN : Fin 242) = true
nf704ColNNNA :
  nf703OriginalCache.AGate nf702OriginalInputs (NNN : Fin 242) 0 = true
```

for all `NNN = 0,…,241` (with correctly elaborated concrete indices). Generation gives no proof by itself; every new declaration still needs compilation on the **original** full cache and the strict standard-axiom audit.

The exact source manifest comprises **243 Lean modules**: `Common.lean` + 242 physical `ColNNN.lean` modules, and **971 distinct Lean declaration names** (three shared + four per coordinate). All 24 already-accepted coordinate modules remain unchanged.

## 3. Disjoint remaining certification shards

Each block is eight original coordinate pairs, except the terminal two-coordinate `Fin 2`:

| Original index-zero interval | Status at NF737 source preparation |
| --- | --- |
| 0–23 (24 HD + 24 A) | **LEAN CERTIFIED** in NF708/NF713/NF715 |
| 24–31 | NF734 numerical compiler pending; NF737 source proposal |
| 32–39, 40–47, …, 232–239 | NF737 exact source candidates only |
| 240–241 | NF737 exact two-coordinate terminal source candidate only |

`24,…,241` contains exactly **218 remaining indices per family**, partitioned into **28 distinct shards**. Hence **436 new original global gate assertions**, corresponding to **872 new non-shared Lean declaration candidates**. The accepted 532 earlier gate instances are never silently augmented by this source preflight.

The script emits an independently checkable source-neutral Mathlib lemma `neutralNF737RemainingIndexZeroOf28Shards`:

```lean
(P : Fin 242 → Prop) →
(∀ i, 24 ≤ i.val → i.val < 32 → P i) →
⋯ →
(∀ i, 240 ≤ i.val → i.val < 242 → P i) →
∀ i, 24 ≤ i.val → P i
```

The CI workflow compiles it **directly in Lean**, prints its axioms, and rejects `sorryAx`, foreign axioms, source drift, or missing receipts. Even a successful pure theorem says **only** that the shards cover the range; it is **not** a proof of any new numerical matrix gate.

The same 28-shard structure can later be attached to the genuine original numerical gates only after each source-specific block has independently passed Lean.

## 4. Independent genuine original numerical pilot: index-zero 32–39

NF737 also attempts **eight actual global original HD row-zero gates and eight actual global original A column-zero gates** at positions 32–39, separately from NF734's 24–31 compiler. This is not merely abstract covering logic.

The third NF737 CI job imports the full authenticated NF702/NF703/NF681 original source bank and NF707 pinned compiled original input, replays the source fingerprints, builds the genuine NF703 center cache and exactly eight original `NF704Frontier.Col032` through `Col039` modules, then independently audits **35** theorem declarations: **32 new** numerical/projection declarations and the three accepted shared projections.

The new audit driver writes `nf737-original-indexzero-032-039-kernel-audit.json` **only after the eight actual numerical modules have compiled in Lean and the complete 35-name standard-axiom audit has passed**. This is an independent, noncontiguous new shard; it does not assert NF734's positions 24–31.

If the pilot succeeds before NF734, the set of known accepted index-zero positions becomes `0–23 ∪ 32–39` (32 positions per family), **not** the contiguous prefix `0–39`. The cumulative cited original global HD/A gate count would then become **548**, provided no additional overlapping certificates are counted. If NF734 later succeeds independently, the contiguous index-zero prefix becomes `0–39` and the gate count becomes **564**.

Until an actual successful NF737 original numerical kernel job is confirmed, all of these sixteen new gate propositions remain **OPEN**.

## 5. Strict certification ledger

| Obligation | Standing |
| --- | --- |
| Frozen original NF702 scaled inputs and full NF703 cache source | ACCEPTED existing |
| NF681 local original 242+242 product receipts | ACCEPTED existing |
| Original HD row-one / A column-one | **LEAN UNIVERSAL PASS** |
| Original HD row-zero / A column-zero positions 0–23 | **LEAN PASS** |
| NF734 positions 24–31 | NEW NUMERICAL KERNEL PENDING |
| NF737 complete remaining 218-coordinate original source bank | SOURCE PREFLIGHT PENDING NF737 CI |
| NF737 28-shard Fin242 logical lemma | KERNEL PENDING NF737 CI |
| New original global index-zero HD/A positions 24–241 | **NUMERICAL LEAN OPEN** (NF737 32–39 pilot queued) |
| Any other original physical matrix row/column index | **NOT CLOSED BY THIS WORK** |
| Complete original numerical enclosure and payment/vector banks | OPEN |
| Global Weil positivity and RH | **NOT PROVED** |

The next numerical execution stage should certify additional original index-zero ranges by importing their matching original local receipts, original cache object, and original source/compiled-object manifests, never by asserting 28 generic hypotheses as axioms.

This NF737 branch is stacked on **Phase III NF734 PR #758**, not on the parallel **Phase IV NF736 PR #760**. Both branches share the repository-wide NF registry without merging unrelated work.
