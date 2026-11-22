# UOI052 — source recovery intake and governance handoff

**Date:** 2026-11-21 (America/Los_Angeles). **Classification:** analytical/source custody, not Lean or RH proof. **Scope:** append-only evidence on the existing UOI operative obligation graph.

## Recovered source

The former conversation-only UOI035–UOI048 research notes, their retrievable finite checkers/receipts, and adjacent CF017/018/020 source plus CF017–021 exploratory validators have been restored to the independent source-custody [draft PR #899](https://github.com/monocap-tech/weil-lab/pull/899). UOI049/050 were already in that draft. It contains **57 added paths**, no altered historical Lean/artifact source and no workflow file changes. The [machine-readable recovery index](https://github.com/monocap-tech/weil-lab/blob/research/uoi049-uoi050-prime-core-tail-custody-20261121/research/unified/receipts/UOI052_cross_thread_recovery_index.json) records all first 56 paths and explicit evidence limits.

Independent exact GitHub read-back confirmed the seven known original SHA-256s documented in [Formalization #898](https://github.com/monocap-tech/weil-lab/issues/898): UOI044 checker/finite matrix, UOI045 Gamma note/receipt, UOI046 note/checker/receipt. The terminal newline restored from the original file serialization was necessary to reproduce those historical digests.

**Unresolved artifact collision:** two distinct UOI045 research outputs exist (Gamma localization and later cubic Fourier flatness). The later `check_uoi045.py` is recovered, but the earlier *Gamma* checker with historical SHA-256 `0e8ff00b98d1d015daaa58ca6c2e6b487f4f7395f255607ff6e41c9eb0bdb014` is not in the retrievable Library. The Gamma report and original receipt are recovered and hashed. Never assign the cubic script the Gamma checker's identity.

## Controller modifications in this review branch

Exactly four **existing** nodes receive one additional source-linked, **non-accepting** evidence item: `UOI-INTAKE`, `CF-BOUNDARY`, `W-SOURCE-DOMAIN`, `W-EXTENSION`. Their new `sources` point to exact recovered files or PR #899. Node IDs, prerequisites, standing, accepted certificates, source pins, terminal OR routes, historical manifest, and zero automated dispatch authority are retained. There are still **13** nodes. This is a custody and obligation-graph handoff, not a proof transition.

## Distinguish historical controller policy from current owner order

Issue [#834](https://github.com/monocap-tech/weil-lab/issues/834) and governance [#861](https://github.com/monocap-tech/weil-lab/issues/861) explicitly expired the old *blanket* research/CI ban on 2026-11-21. Controlled research PRs and strictly bounded, source-pinned actual Lean verification are authorized with lineage-specific fan-out and generated Lake manifest checks.

However, the **older UOI planning-only validator** in `scripts/uoi_validate.py` still deliberately asserts that `authority.execution_policy == "consolidation_hold"`. That field cannot safely be changed alone without also revising the validator and its fail-closed tests. Therefore this recovery **does not change** the machine's `execution_policy` or automatic-dispatch bits. Treat this controller as a historical planning/read-only guard, **not** the controlling repository-wide permission policy. A separate reviewed controller-policy migration is needed if that program is to authorize bounded CI execution.

## Mathematical scope and next checks

The recovered UOI047/048 sources are authentic *analytic manuscripts*, not accepted positive-tail/completed-space Lean theorems. The full original signed form and domain, all complex prime phases, both poles, exact collar geometry, gamma coercivity, infinite-tail Schur/core interaction, source-to-native F01/F08 bridge, and arbitrary-support positivity remain separate proof gates. No new `.olean`, named axiom receipt, or numerical HD/A gate acceptance is claimed. Independently reconciled original numerical frontier remains 708/968. Formalization's F40→F41→F42 queue retains priority.

**Integration condition:** Review/merge the source-custody PR and this small governance PR independently. Add only source references/evidence classes; never transfer a proposed theorem into `accepted` without independent mathematical and kernel evidence.
