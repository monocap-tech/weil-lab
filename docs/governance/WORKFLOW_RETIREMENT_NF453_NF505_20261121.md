# Weil-Lab historical workflow retirement — NF453–NF505

Date: 2026-11-21. This is **maintenance-only source custody**, not new Lean or numerical certification.

## Decision

Retire the unrestricted ordinary `pull_request` triggers on 64 historical NF453–NF505 workflows, while retaining the workflow definitions, verification commands, manual `workflow_dispatch` entries, underlying source files, and all preexisting certificates and Actions run records. The Git history and the companion custody manifests record old/new Git blob identities.

- **24** workflows (NF453–NF474 cohort) changed in the first batch.
- **40** workflows (NF475–NF505 cohort) changed in the second batch.
- **613** workflow files before and after; no workflow file was deleted.
- Every affected workflow diff removes exactly **one** unrestricted `pull_request:` event line. No job body was changed.
- NF501 and NF504 also retain their preexisting narrow `push` triggers to specific historical branches. NF502/NF503, which had only branch-scoped pushes, were left unchanged.
- The already staged IV018/IV023 Lake initialization-order corrections are inherited from `maintenance/iv026-lake-bootstrap-and-trigger-custody-20261121`.

## Auditable evidence

1. `docs/governance/NF453_NF474_MANUAL_ONLY_RETIREMENT_20261121.json` — 24 original/retained Git blob pairs.
2. `docs/governance/NF475_NF505_PR_TRIGGER_RETIREMENT_20261121.json` — 40 original/retained Git blob pairs.
3. `python scripts/workflow_retirement_inventory.py --check` — read-only static trigger inventory and fail-closed SHA-1 Git blob/dispatch guard over the 64 recorded workflows.

The audit is a **static YAML-pattern check**. It is not a general GitHub Actions syntax validator, a Lean build, a proof, or a new acceptance receipt. It does not verify historical run artifacts are still downloadable.

## Deliberately not yet done

**No pull request, merge, heavy CI dispatch, certificate promotion, or removal of historical proof artifacts is authorized by this branch.** A source-only maintenance branch does not affect workflows on other existing research branches until changes are propagated.

Before proposing a PR or updating any active research branch:

1. Enumerate all remaining unrestricted triggers on the intended *actual merge base and candidate head*, including workflows outside NF453–NF505.
2. Resolve required status-check protection and ruleset dependencies. Branch-protection read returned GitHub integration **403**; absence of readable protection data is **not** proof that nothing depends on these checks.
3. Independently validate GitHub Actions YAML and compare event fan-out; use an isolated bounded PR only once safe.
4. Where historical on-demand replay is needed, ensure the workflow is deployed to the default branch (GitHub's `workflow_dispatch` availability requirement). A `workflow_dispatch` key on a non-default research branch is not by itself a guarantee of UI/manual dispatch.
5. Preserve accepted source/artifact provenance, then reopen controlled IV018/IV023 Lean compilation and strict axiom receipts.

The accepted Phase III numerical frontier **692/968** is unchanged, as are original signed Weil mathematics and the unresolved support-independent positivity goal.
