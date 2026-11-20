# NF745 — Fail-closed original physical numerical kernel acceptance ledger

**Canonical Phase III iteration:** NF745 · **Source predecessor:** [NF744 PR #772](https://github.com/monocap-tech/weil-lab/pull/772) · **Repository registry:** [Issue #761](https://github.com/monocap-tech/weil-lab/issues/761). The separate Phase IV sequence now reaches IV010; those independent analytical theorems are not certificates for the original 242×242 physical numerical matrix.

## 1. Recovery: accepted originals and actual queued numerical jobs

The following original source-specific objects are already **genuinely accepted** in Lean, with immutable GitHub proof/artifact custody:

| Original source / kernel milestone | Run | Accepted job | Accepted artifact |
| --- | ---: | ---: | ---: |
| NF708 original HD row-zero and A column-zero positions 0–7 | 44640227758 | 135969102426 | 14589570565 |
| NF713 original positions 8–15 | 44649041852 | 135998999534 | 14594190839 |
| NF715 third original global matrix positions 16–23 | 44669131044 | 136065595864 | 14599683589 |
| NF733 permanent custody of **both full original index-one universals**, 242 HD and 242 A | 44782027897 | 136446941618 | 14652498322 |
| NF737 complete genuine original 242-coordinate **source preflight only** | 44791346863 | 136479519760 | 14660147684 |
| NF739 independent genuine original 242-coordinate **source preflight only** | 44795709843 | 136494577562 | 14663320765 |

All six immutable source and proof receipts have pinned SHA-256 artifact archive digests in the new NF745 verifier.

The baseline is consequently **532 genuine original global matrix gate instances**: 24 original HD row-zero and 24 A column-zero entries, plus 242+242 original index-one universal statements. This is a **gate-instance tally**, not a full matrix or a new computational proof.

At NF745 preparation, the specific follow-on numerical jobs NF737 32–39, NF739 40–47, NF742 48–55 and NF743 56–63 were not concluded; original NF744 full-index-zero source and pure-range jobs were also queued. NF742's source job was queued. NF734 genuine 24–31 remains a separate certification obligation **not authenticated by NF745's pilot ledger**.

A source preflight marked PASS does **not** make any new original HD/A numerical gate true. A pure Fin242 range covering theorem does **not** make any new numerical gate true. Neither does a separate Phase IV Mathlib-only positivity theorem.

## 2. Concrete problem NF745 addresses

Multiple independent research threads generate genuine original gate source candidates from the same immutable NF702/NF703/NF681 original physical data. Their GitHub Jobs may run much later than source preflight, and previous status reports can inadvertently conflate:

- historical accepted original numerical kernels;
- accepted source-generation and immutable source identity;
- queued, in-progress, failed or still unscheduled original numerical jobs;
- successful pure range logic without any actual original numerical proof;
- fully successful original numerical jobs with the exact printed Lean axiom audit.

The new lightweight `scripts/nf745_live_original_kernel_acceptance_ledger.py` is a **fail-closed acceptance reconciler**. It does not claim a new mathematical theorem and does not replace any Lean kernel.

## 3. The live original numerical acceptance contract

A new index-zero eight-coordinate batch is counted as **16 additional original global HD/A gate instances** only when **all** of the following hold:

1. Every historical immutable accepted original source/axiom artifact ID and its exact published SHA-256 digest still agrees with a genuinely successful upstream GitHub job.
2. The **specific genuine numerical gate job** (not its source-only predecessor or a similarly named pure/analytical job) has `status=completed` and `conclusion=success`.
3. Its GitHub step list includes a successfully completed **strict actual original theorem axiom/source-bound verification step**. A passing job without that step is not accepted.
4. Its run contains the correct nonexpired **genuine original numerical kernel artifact** with a well-formed SHA-256 digest. An expired artifact, an unrelated archive, or a source-only archive is not acceptance.
5. The batch's declared literal coordinate positions are disjoint from the prior accepted positions and from other newly counted batches.

This is a **second-order custody check of GitHub's accepted Lean jobs**: the individual job's strict verifier must already have checked all 35 actual original source-specific `DGate`, `DProjection`, `HD`, `A` and shared projection theorem axioms. The NF745 reconciler itself does not replay or recompile those proof objects; it binds the actual completed source-specific kernel job and artifact identity. A future deeper custody pass can download and inspect individual numerical audit JSON receipts when those jobs finish.

If any required historical original source provenance is missing or disagrees, the ledger **fails** rather than silently reducing or increasing the baseline. The compiler cannot substitute a new synthetic matrix or rounded witness.

## 4. Precisely tracked numerical frontiers

| Original physical matrix index-zero family | Source-status provenance | Numerical kernel acceptance rule |
| --- | --- | --- |
| 0–23 (24 per HD/A) | NF708/NF713/NF715 original global | **Previously accepted** |
| 24–31 | NF734 original numerical stage | **Excluded** until separately authenticated; not silently counted |
| 32–39 | NF737 original `Col032`–`Col039` | Successful run 44791346863 genuine kernel job + strict axiom step + matching artifact |
| 40–47 | NF739 original `Col040`–`Col047` | Successful run 44795709843 genuine kernel job + strict axiom step + matching artifact |
| 48–55 | NF742 original `Col048`–`Col055` | Successful run 44800994258 genuine kernel job + strict axiom step + matching artifact |
| 56–63 | NF743 source-equal original cache reuse and actual `Col056`–`Col063` | Successful run 44813177950 genuine kernel job + strict axiom step + matching artifact |
| 64–241 | NF737/NF744 authentic complete source and 31-shard handoff | **Source-only** until genuine source-specific numerical kernels exist and pass |

The reconciler does not infer status for **NF734 24–31**, nor does it count any index-zero coordinate `64–241` from NF744's proposed complete source. This is a deliberately conservative covered subset of the overall proof ledger.

The resulting accepted count is **exactly**

[
532 + 16\times\#\{\text{verified successful new original eight-coordinate numerical pilots}\},
]

with each pilot's coordinate interval authenticated and mutually disjoint. Since this implementation tracks four such new pilots, it can report at most **596** gate instances from this particular verified source chain; it **must not** claim complete index-zero closure.

## 5. Independent six-case fail-closed test

The new driver includes an in-memory synthetic test suite, run **before** live GitHub reads. It verifies:

1. Four queued numerical jobs produce the true unchanged 532-gate baseline.
2. A job marked successful **without a successful strict Lean theorem axiom step** contributes no gate.
3. A successful strict step **without the expected genuine numerical kernel artifact** contributes no gate.
4. An **expired** otherwise correctly named artifact contributes no gate.
5. Exactly one genuinely successful strictly audited original eight-coordinate batch contributes **16** gates, resulting in **548**.
6. A failed numerical job never contributes numerical gates even if an earlier successful audit step and artifact are present.

These are control-plane acceptance tests, not new Lean proofs. Their status must be reported separately from actual live GitHub proof results.

## 6. CI and deliverables

The new inexpensive [NF745 workflow](../.github/workflows/nf745-original-kernel-acceptance-ledger.yml) performs three stages on an ordinary GitHub runner, **without downloading 227MB original source banks, a 320MB accepted compiled-object archive, or installing Lean**:

- Run all six fail-closed synthetic control tests.
- Retrieve actual immutable GitHub Actions `run`, `jobs`, `steps`, and `artifacts` data for exact historical and current run IDs, retaining a source-bound JSON snapshot of the observed data.
- Reconcile accepted original kernel status, strictly reject false promotions, and publish `nf745-original-numerical-kernel-acceptance-ledger.json` with actual accepted positions, current awaiting-run states, counted genuine gate instances and explicit global nonclosure.

Three separately archived machine-readable outputs are expected: the self-test JSON, exact actual GitHub status snapshot JSON, and the final accepted numerical gate-state ledger JSON. An accepted run has to succeed before these are treated as independently verified.

**NF745's output does not itself close any unproved original numerical gate.**

## 7. Separate unresolved mathematics

Even completed original **index-zero row/column** universals would leave other original 242×242 matrix indices, original vector/full-payment systems, full numerical enclosure, corrected physical form transport and global arbitrary-support Weil positivity as separate obligations. Phase IV's new explicit mixed Weil and Schur conditions likewise do not substitute for actual arithmetic off-diagonal positivity.

**Full numerical enclosure: OPEN. Global Weil positivity: OPEN. RH: NOT PROVED.**

**Operational next step:** prioritize running the existing genuine original numerical kernel jobs, especially NF743's source-equal accepted original cache optimization. Do **not** allocate additional expensive redundant eight-coordinate jobs merely because the previous ones have not started.
