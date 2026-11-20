# NF733 — Original physical matrix index-one Lean kernel custody

## Accepted result

At **NF732**, the original frozen physical data achieved the first **complete
source-specific original index-one universal matrix-product-gate closure**.

The following two declarations passed Lean's kernel and an independent
per-declaration standard-axiom audit:

```lean
theorem nf732OriginalHDRowOneAll :
    ∀ i : Fin 242,
      nf703OriginalCache.HDGate nf702OriginalInputs (1 : Fin 242) i = true

theorem nf732OriginalAColumnOneAll :
    ∀ i : Fin 242,
      nf703OriginalCache.AGate nf702OriginalInputs i (1 : Fin 242) = true
```

The accepted axioms for **each** theorem were exactly:

```text
[propext, Classical.choice, Quot.sound]
```

This certifies **242 genuine HD entries of original row index 1** and
**242 genuine A entries of original column index 1**, not just 484 independently
listed entry proofs. No extra parameter, numerical oracle, generic positivity
assumption, placeholder, or unproved endpoint is added.

## Accepted external provenance and proof replay

- **Source repository:** `monocap-tech/weil-lab`
- **Committed NF732 source/driver branch:** `research/nf732-pinned-original-quad-kernel-transfer`
- **NF732 original certificate workflow:** https://github.com/monocap-tech/weil-lab/actions/runs/44774641598
- **Successful actual original universal Lean job:** `136435817033`
- **Full original numerical theorem kernel audit artifact:** [14652985322](https://github.com/monocap-tech/weil-lab/actions/runs/44774641598/artifacts/14652985322)
- **Original numerical theorem source artifact:** `14650533188`
- **Accepted pure Fin242 direct eight-range theorem artifact:** `14651825109`
- **Eight original HD/A numerical quad proof jobs:** [NF729 run 44767040253](https://github.com/monocap-tech/weil-lab/actions/runs/44767040253)
- **Previous accepted individual-entry sources:** NF715–NF720, authenticated by NF721/NF723/NF727.

The actual original NF732 final job imported all eight independently accepted
source-bound numerical proof-object bundles, verified their original source
fingerprints and exact compiled Lean object identities, and then compiled
the two unconditional original universal declarations. Their printed axiom
audit passed and the complete job concluded **success**.

The eight original ranges were:

| Original quad | Index positions | Genuine original HD and A numerical proof |
| --- | --- | --- |
| 000 | 0–31 | NF729 kernel pass |
| 004 | 32–63 | NF729 kernel pass |
| 008 | 64–95 | NF729 kernel pass |
| 012 | 96–127 | NF729 kernel pass |
| 016 | 128–159 | NF729 kernel pass |
| 020 | 160–191 | NF729 kernel pass |
| 024 | 192–223 | NF729 kernel pass |
| 028 | 224–241 | NF729 kernel pass |

The final quad includes the **two-position `Fin 2` terminal block**,
coordinates 240 and 241. The original 31 blocks are collectively exhaustive
and nonoverlapping.

The accepted source-specific result is *stronger* than a source-free
`P : Fin 242 → Prop` gluing implication. Both true original propositions
were supplied and accepted by the full Lean kernel.

## NF733 permanent custody

Run `scripts/nf733_accept_original_index_one_custody.py verify` after
restoring the **immutable NF732 source artifact** to
`nf733-accepted-original-source/` and the **immutable NF732 kernel artifact**
to `nf733-accepted-original-kernel/`.

It independently checks:
- Source file identity and original NF702/NF703 proposition text.
- Exact eight original numerical quad declarations, their 31 packed
  block ancestry and all 242 original positions for both HD and A.
- Original generated source and source-manifest SHA-256 identity.
- Exact two accepted theorem names in the final Lean axiom log.
- All eight accepted compiled numerical proof-object fingerprints reported
  in the kernel-verified original assembly.
- Internal accepted audit, manifest, numerical receipt, and theorem source
  fingerprints.
- Explicit **negative** scope flags for unresolved obligations.

The output machine ledger is `nf733-original-index-one-custody.json`.
A passing NF733 custody audit is a *secondary reproducibility check* of
the already-accepted NF732 theorem, not a separate or broader Lean proof.

## Boundary: what this does *not* establish

**Original physical matrix index one is closed. Full original numerical
enclosure custody is not closed.**

Neither accepted theorem establishes:

- Original HD/A product identities for every other matrix index.
- The complete original global vector and physical-payment gate bank.
- Every corrected physical Gram or coercivity transfer required downstream.
- Original all-input Weil positivity, the Riemann Hypothesis, or a complete
  independent RH proof.

Remaining numerical closure must be tracked separately, with exact source
and kernel acceptance, rather than inferred from the complete index-one result.

## Next frontiers

1. Persist the newly accepted index-one source, compiled-object, and axiom
   custody across the active research-PR chain.
2. Audit which other original physical matrix-index rows are already fully
   certified versus partially covered (including index zero), before
   choosing the next exact entry bank.
3. Continue numerical vector and full-payment rows separately; do not conflate
   those obligations with HD/A index-one matrix products.
4. Maintain exact distinctions between `LEAN PASS`, source-authenticated
   candidate, external arithmetic verification and open global Weil claims.
