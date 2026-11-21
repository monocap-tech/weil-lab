# Weil-Lab — CP012
## Actual upstream BatchSpec loses indexed numeric row provenance: exact negative control and minimal kernel attachment contract

**Independent CP### project stage**, stacked on CP011 PR #825 → CP010 #822 → CP009 #819 → CP008 #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. No changes to independent Phase IV IV### original signed Weil Lean/source support extension, Phase III NF### numerical enclosure compilation, or PI### arithmetic/trace projections.

**Scope and status:** CP012 finds and formally isolates a **real logical information-loss boundary** in the previously proposed numerical-roster/Lean handoff. It is not a new positive zeta-zero interval certificate, full-Weil form, or RH. The original upstream certificate's finite-height Turing count/zero existence remain genuine external source theorems. CP011's newly drafted source uniqueness lemma is still **not** an accepted new local Lean kernel theorem; the CP011 workflow was queued at kickoff. CP008/CP010 refined-root candidate existence proofs, the CP011 first original RS source-row read and the corresponding direct Lean kernel receipts are still pending. CP012's exact rational countermodel was independently checked locally; the GH workflow reproducing its original source SHA audit remains a new candidate until it actually completes.

## 1. Precise finding in the exact external original Lean interface

Fetched and compared **the actual original source**, pinned to `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3`:

| Original source file | Actual immutable Git blob | Actual public object |
|---|---|---|
| `Zeta/Zeros/Certificates/Basic.lean` | `128e19e4bb056332b0fd71a8c107f4075cd8cd07` | `BatchSpec` exposes **only** interval count, first-left, last-right |
| `Zeta/Zeros/Certificates/Fold.lean` | `2596e253a8c8f94c47ce880500973775f2611d77` | `BatchSpec.append` preserves only count addition and outer two endpoints |
| `Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean` | `12848f56d0b62df858dcb89b708a858f4f7b28fb` | Actual first 200 original RS intervals `BatchSpec 200 149500 1000 474603 1000`, no first interval's right endpoint |

The publicly exported original type is **literally**:

```lean
abbrev BatchSpec (n an ad bn bd : ℕ) : Prop :=
  ∃ C : CertifiedZeroIntervals, C.intervals.length = n ∧
    C.intervals.head?.map (·.fst) =
      some (Enclosure.sfrac false an ad) ∧
    C.intervals.getLast?.map (·.snd) =
      some (Enclosure.sfrac false bn bd)
```

Under Lean's module system, the heavy per-row `build_batch_rs` source proof is **private**, and the public theorem's statement does not expose indexed intermediate original numerical interval endpoints. `BatchSpec.bundle` chooses some certified witness of that public existential; the public projection cannot identify every row's original decimal endpoints simply from source hash/README/list length. This is **not an accusation that the underlying original proof is wrong**. It is an interface/dictionary limitation of what the *public theorem* entails.

### What CP011 actually proves, if its Lean candidate passes

From the original Turing-count equality `N(g)=1748002` and the full original certified separated-interval list, the **mathematical zero set** inside `0<Im(z)<g` is exhausted, and each abstract source-certified interval in the witness bundle has exactly one zero. That is an intrinsic zero-ID fact.

**What it does not prove:** for the `k=52` (zero #53, zero-based indexing) original certified bundle, `(Z.intervals.get k).fst` and `.snd` equal the two decimals in the published first RS text-file row. This is NOT a consequence of its abstract `BatchSpec` count/endpoints alone. A successful CP011 source-level uniqueness theorem would not magically supply such a row-binding receipt.

## 2. Exact Fraction countermodel: even known COMPLETE simple zeros don't identify the certificate's intermediate endpoints

Take the same *complete* simple underlying roster `{1/2, 3/2, 5/2}`, all counted with multiplicity one, with the same three sorted, disjoint, open containing intervals. Compare two legal presentations:

| Slot index | Model A | Model B | Exact zero contained |
|---|---|---|---|
| 0 | `(0,1)` | `(0,9/10)` | `1/2` |
| 1 | `(1,2)` | `(13/10,17/10)` | `3/2` |
| 2 | `(2,3)` | `(2,3)` | `5/2` |

Both models satisfy:
- exact count 3 and complete identical list of all three roots;
- ordered non-overlapping interval interiors; each contains exactly one root;
- `BatchSpec`'s visible projections `length=3`, `head.fst=0`, `last.snd=3`.

Yet slot 0's **right endpoint** and slot 1's **both endpoints** differ. Therefore those indexed endpoint equalities are *logically underdetermined* even after assuming the strongest finite-height zero-count and simplicity facts. This is a counterexample to a proposed **proof-interface inference**, **NOT** an example of false mathematics or a counterexample to zeta zeros being simple.

Source-backed executable `scripts/cp012_batchspec_indexed_row_no_go.py --self-test` uses exact `fractions.Fraction`, checks all model obligations and negative controls, and prints `CP012 EXACT FRACTION BATCHSPEC INDEXED-ROW NONIDENTIFIABILITY: PASS`. It does not pretend the model itself represents zeta zeros.

## 3. Exact minimal missing mathematical contract: source-index **CONTAINMENT**, not necessarily equality

A stronger source row certificate would assert:

```lean
structure ExactSourceRowAt
    (Z : CertifiedZeroCount) (k : Fin Z.intervals.length)
    (a b : ℝ) : Prop where
  left_eq : (Z.intervals.get k).fst = a
  right_eq : (Z.intervals.get k).snd = b
```

However, **the full equality is not needed to prove the zero identity**. The exact sufficient interface is weaker:

```lean
structure IndexedSlotContains
    (Z : CertifiedZeroCount) (k : Fin Z.intervals.length)
    (a b : ℝ) : Prop where
  left_le : (Z.intervals.get k).fst ≤ a
  right_le : b ≤ (Z.intervals.get k).snd
```

Given a genuine new refined zero `s` with `Im(s)∈(a,b)`, one obtains:

```
 original_slot_k.left <= a < Im(s) < b <= original_slot_k.right
```

and invokes CP011's (source-level candidate) `refined_root_identifies_original_slot` to conclude that `s` is the original canonical zero in slot `k`. No separate local zero-uniqueness axiom and no exact numerical equality of old slot boundaries are required.

**The real missing source theorem for zero #53** is of the form:

```
 IndexedSlotContains certifiedZeroCount (Fin.mk 52 (proved 52<n))
   150.05352 150.05353
```

(or a *different rigorous rank theorem* identifying the genuine refined zero as the 53rd positive-height zero). **Neither** currently follows from the published first-RS `BatchSpec 200 149500 1000 474603 1000` statement. The original full first-RS store SHA and actual first-row source content remain relevant provenance and numerical evidence, but not this kernel theorem by themselves.

This is a precise correction to any reading of CP011 that said “source SHA + original slot uniqueness = numerical source row identification.” That implication is **INVALID** without indexed containment (or a certified ordinal ranking argument).

## 4. New actual Lean source modules and fail-closed verification

New `cp011_zeta_v435/CP012RowReceipt.lean` imports CP011's local isolated source candidate and provides:

1. `ExactSourceRowAt.implies_containment`: stronger index-equality receipt implies the minimal containment contract.
2. `refined_root_equals_canonical_at_index`: conditional original-zero-identity transport from exact certified refined roots **assuming explicitly** `IndexedSlotContains`.
3. `refined_root_of_exact_source_row`: the stronger equality version of the same transport.

This is a **no-sorry Lean 4.35 SOURCE CANDIDATE** and says, by design, nothing about actually proving `IndexedSlotContains` for any source row. Even a real Lean compilation would certify only a conditional implication. The new `scripts/cp012_row_bridge_lean_axiom_audit.py` requires actual CP011 and CP012 compiled `.olean` files and three standard-only `#print axioms` receipts before calling this a **conditional Lean bridge**; it explicitly records `full_zero_53_row_attached: false`.

New cheap source CI `.github/workflows/cp012-original-batchspec-interface-audit.yml`:
- runs the exact Fraction false-inference countermodel;
- fetches three ACTUAL ORIGINAL upstream files pinned at exact commit and checks each Git blob SHA;
- checks the exact original `BatchSpec` theorem type and first RS batch and its appending source shape;
- reports `PINNED_SOURCE_BATCHSPEC_ROW_OPACITY_CONFIRMED_NOT_LEAN` only.

New **manual-only** `.github/workflows/cp012-original-source-row-bridge-v435-manual-kernel.yml` compiles CP011 then CP012 against original Zeta v4.35.0, checks source pin, true .olean and axiom receipts, but **still never claims zero #53's numeric source row attached**. No IV###/NF### compiler preemption.

## 5. Repair strategy: make the mathematical dictionary actually source-faithful

To close the remaining bridge, choose one:

**A. Publish a stronger original-source row receipt.** Extend the original generated Lean 4.35 source certificate *at a deliberately selected slot or batch prefix* with a new public theorem exposing the kth **concrete certified interval's containment** of a specified rational bracket. That theorem must be proved from a bundle representation whose slot meaning remains stable across `BatchSpec.append` and abstract existential witnesses. Merely recompiling a separate `build_batch_rs 0 1` certificate will not imply equality with the original global bundle's `Classical.choose` witness.

**B. Prove ordinal ranking directly.** Instead of opening the original abstract `Z` slot's endpoints, derive from independently kernel-certified zero counts/upper bounds at strategic cut heights that the refined zero is the 53rd positive-height zero. It is not enough to know merely `N(g)=1,748,002` and the lower 52 Euler source-row count: this alone does not exclude an additional zero between 149.5 and the new candidate. A proper local count upper bound or equivalent separation argument is needed.

**C. Rebuild a source-indexed witnessed complete roster.** Replace the index-opacity-prone existential bundle API for the interface with a certificate-bearing data type that exposes specific indexed interval equations/proofs (possibly selectively for target rows) and proves it has count/exhaustiveness. This has engineering/Lean cost but makes the transport semantics explicit.

**Falsifier:** if the actual pinned original RS row #1 does NOT contain the proposed `[150.05352,150.05353]`, the CP010 source-row attachment claim is wrong regardless of sign-screen values, even though it could still contain the actual zero numerically; then adapt the source-index evidence or use a separate count/rank proof. The CP011 first-row CI remains queued at kickoff.

## 6. Invariant / provenance classification

- **Intrinsic:** actual zeta zeros, their ordinates and multiplicities; under a complete count certificate, their strictly ordered finite-height zero sequence and the fact that no other zeros occur below g. A genuine new rigorous enclosure preserves the zero's identity if properly linked.
- **Certificate-relative:** the rational interval endpoints, width, dyadic halfwidth sums, batch and source-file segmentation, `BatchSpec` existential witnesses, and source SHA. These are not uniquely determined by intrinsic zeros or the original count theorem.
- **Frozen support-dependent:** CP005–CP010 normalized matrix error allowance `1/500`, compact-bump Fourier derivative constants, exact normalized dyadic budgets and the root-53 exception allowance. They are sufficiency certificates, not a theorem of original signed Weil positivity.

**Next CP013:** run/inspect the actual source/API preflight; test a kernel-meaningful *index-53* source witness export or a finite-height rank count. Only after obtaining a **real** `IndexedSlotContains` or rank theorem and a **real** Euler/RS narrow sign proof can CP011's uniqueness argument identify a new source-indexed zero with the original fully count-certified roster. The complete pole-prime-Gamma zero-side equality and quadrature remain separate falsifiable tasks. No RH/global Weil positivity claim.

Primary source: https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Certificates/Basic.lean ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Certificates/Fold.lean ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean .
