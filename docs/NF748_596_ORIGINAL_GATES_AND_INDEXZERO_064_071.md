# Weil-Lab — NF748
## Recover 596 certified original numerical HD/A gates and launch exact original index-zero 64–71

**Canonical Phase III numerical certification:** NF748. This is not Phase IV IV014 or analytical support-expansion research.

**Previous Phase III stack:** NF745 PR #775 → NF746 PR #776 → NF747 PR #777 → NF748 (this branch). The original NF742 PR #768 and NF743 PR #770 source/numerical runs were checked independently.

**New original numerical 64–71 status:** SOURCE CANDIDATES COMMITTED; REAL ORIGINAL LEAN NUMERICAL CI AND STRICT 35-THEOREM AXIOM CHECK NOT YET ACCEPTED. Do not count 64–71 from source/preflight/cache provenance.

### 1. Newly authenticated original kernel results

The old accepted original global matrix gate count before pilots was **532 distinct true source-bound HD/A instances**:
- 24 original index-zero HD row 0 gates and 24 index-zero A column 0 gates, indices 0–23, independently accepted through NF708/NF713/NF715;
- 242 genuine original index-one HD gates and 242 original index-one A gates, universally accepted via the NF733 permanent genuine kernel custody audit.

The following **four nonoverlapping eight-index numerical pilots** now each have successful ORIGINAL Lean kernel jobs, successful source-specific 35-theorem strict-axiom audit steps, and actual immutable artifact ID and SHA-256 receipts:

| Stage | Actual index-zero | Successful Actions run | Actual numerical job | Kernel artifact | SHA256 |
|---|---|---:|---:|---:|---|
| NF737 | 32–39 | 44791346863 | 136514439734 | 14672703515 | bd3771cf2b939e76bc4dea956f4547c3efb4330f77a318db46cf71b78004e89a |
| NF739 | 40–47 | 44795709843 | 136528518645 | 14673191666 | 95da4ce94c83bc021b7361fdf261699a74f45a65a507a505a28567dbc3087258 |
| NF742 | 48–55 | 44800994258 | 136579243726 | 14678836252 | 907ac7e634209604dfc5d4b6fa9c4706791664155a7c9d60e13e14701360ace2 |
| NF743 | 56–63 | 44836454830 | 136633947443 | 14680553841 | b0c0c1acc85701b0ba437fa99dece7309a7d00500307cae05bf3a3bfea9d169d |

The independent NF745 true live ledger run 44818061251/job 136571445603, artifact 14676318703 SHA256 5524933c91f0786732d6ab0272385a693188518bf9dba3a37006a115675eee5a, established 564 verified original gate instances before the NF742 and NF743 numerical acceptances.

The corrected acceptance count is therefore

    532 + 4 × (8 genuine HD + 8 genuine A) = 596.

The accepted original index-zero positions for BOTH HD and A are

    {0,…,23} ∪ {32,…,63}.

NF734 24–31 is **not certified by this stage**. The remaining index-zero positions currently excluded are exactly

    {24,…,31} ∪ {64,…,241},

or **186 coordinates per HD/A side = 372 gate instances**. Thus 596 of the 968 index-zero-plus-index-one original frontier gate instances have actual numerical kernel proof receipts. This is not a 242×242 matrix or full numerical enclosure; all other row/column obligations remain.

### 2. NF748's NEW real numerical pilot, not a source-only assertion

Launch exact frozen ORIGINAL NF702/NF703 global HD row-zero and A column-zero gates for all i∈64..71:

    nf703OriginalCache.HDGate nf702OriginalInputs 0 (i : Fin 242) = true
    nf703OriginalCache.AGate  nf702OriginalInputs (i : Fin 242) 0 = true.

These are **16 new physical matrix gate instances**, four original named declarations per original Fin-242 column (DGate, DProjection, HD, A), and three audited original shared declarations: 35 actual Lean axiom targets.

The source is taken exclusively from the original authenticated NF737 242-column 227 MB frozen generated Lean source artifact. The new audit script verifies ALL original source manifests/previous source anchors, matches each original Col064–Col071 SHA and exact HD/A goal syntax, and refuses fabricated source modules or ordinary examples. No original physical coefficient, cache, matrix entry, support, frequency, or divisor source definition is changed.

A successful new batch would raise the count from 596 to **612**, and would certify 64..71 without implying that the older independent NF734 24..31 passes. The index-zero universal theorem is still separate.

### 3. Reusing accepted genuine Lean objects without weakening proof custody

The successful NF743 recovery demonstrated that the immutable historical NF728 original source archive and NF729 original numerical quad-000 cache object archive can be reused ONLY after exact accepted-source SHA, source-family membership, compiler/Mathlib/toolchain compatibility, and accepted original object provenance checks. The historical cache reuse driver `scripts/nf743_reuse_accepted_original_nf703_cache.py` remains deliberately unchanged.

NF747's real compiler recovery proved the import order:

    NF681.Common.olean
       before NF703Cache.Frontier.olean
       before NF681.Col064..071.olean
       before NF704Frontier.Common.olean
       before real global NF704Frontier.Col064..071.

The new independent NF748 source-DAG verifier checks the original generated import clauses and exact prior compiled dependencies, rejecting a missing or reordered required original Lean object. Reusing a byte-identical compiled accepted cache does **not** certify a new global matrix gate; the new columns themselves must compile and pass strict standard-axiom audits.

### 4. True live rollforward and fail-closed regression

New script: `scripts/nf748_original_596_kernel_rollforward.py`.

In GitHub Actions this script queries the ACTUAL historical NF745, NF737, NF739, NF742 and NF743 jobs and immutable artifacts via GitHub API. It requires:
- the exact historical successful job ID/name;
- for all four numerical pilots, successful strictly named original 35-theorem axiom audit steps;
- the exact unexpired numerical kernel artifact ID/name and pinned complete SHA256 digest;
- a nonoverlapping original index set;
- a final count of precisely 596 and no acceptance of NF734 24–31 or the NEW 64–71.

Seven synthetic negative tests reject queued or failed numerical jobs, missing strict axiom audits, expired/missing artifacts and incorrect artifact hashes. Synthetic tests **do not** constitute a Lean proof or GitHub live-data attestation.

Live rollforward receipt:
`nf748-original-596-accepted-gate-rollforward.json`

The actual new 64–71 kernel audit requires that specific LIVE receipt and binds its SHA to the accepted old 596 prior original gates. This prevents the new stage from silently counting either source-only or queued claims.

### 5. The new kernel workflow and its strict acceptance rule

Workflow:
`.github/workflows/nf748-original-indexzero-064-071-cached-kernel.yml`

New scripts:
- `scripts/nf748_original_596_kernel_rollforward.py`
- `scripts/nf748_original_indexzero_import_order_guard.py`
- `scripts/nf748_original_indexzero_064_071_cached_kernel.py`.

The workflow:

1. Authenticates accepted 596 original numerical gate instances against LIVE GitHub Actions job-step/artifact-digest state.
2. Restores and SHA-authenticates the complete exact original NF737 242-column generated source bank.
3. Generates the actual new 64–71 source/audit ledger but explicitly marks it as source-only.
4. Verifies immutable historical NF728/NF729 cache source and accepted Lean object identity, with the original NF743 fail-closed cached-object driver.
5. Installs the pinned genuine Lean/Mathlib environment and verifies the 64–71 original import DAG.
6. Compiles missing original prerequisites, then **directly kernel-compiles all eight genuine frozen NF704Frontier Col064–Col071 Lean modules**.
7. Replays `#print axioms` for 35 actual original theorem declarations, accepts only standard `propext`, `Classical.choice`, `Quot.sound`, rejects `sorryAx`, requires the complete actual source and accepted-cache hash custody, and publishes the numerical Lean kernel artifact.

**A source preflight, an accepted cache, the previous 596-gate ledger or a successful workflow setup step cannot promote the 16 new gates.** Only the complete final numerical gate + axiom audit can.

### 6. Remaining Phase III numerical and analytical obligations

- **NF734 indexzero 24–31** remains a historical eight-coordinate gap until its own numerical gate kernel proof receipt succeeds.
- **NF748 indexzero 64–71** new genuine original gate batch pending.
- **Indexzero 72–241** future genuine numerical certificate batches still pending.
- **NF744 31-shard source/logical Fin242 cover** passed, but a theorem requiring all genuine index-zero numeric gates cannot be promoted until every actual shard has accepted Lean numerical proof custody.
- Original matrix entries beyond the already certified global index-one/selected index-zero gates, complete vector/payment enclosure, global Weil positivity and RH remain OPEN.

**Next NF749:** recover the real NF748 64–71 compiler result, identify any source-cache import or math elaboration failure, and continue exact original kernel gate shard acceptance without claiming source-only gates.

### Source provenance

All numerical claims above are tied to the specific successful immutable original GitHub Actions runs and SHA-256 artifact IDs checked by the new live script. The separate Phase IV branch IV013 PR #779 has its own unrelated original signed Weil support problem and must not be used to promote numerical Phase III gates.
