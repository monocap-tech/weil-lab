# UOI002 — Read-only obligation planner integration

**Date:** 2026-11-21. **Authority:** [UOI000 issue #861](https://github.com/monocap-tech/weil-lab/issues/861); [UOI001 issue #862](https://github.com/monocap-tech/weil-lab/issues/862).

**Evidence class:** governance implementation, **not** mathematical proof, Lean compilation, original certificate promotion, or CI deployment.

## Installed on isolated governance branch

- `research/unified/obligations.json`: source-linked, 13-node additive RH-facing coordination graph. Two *alternative* complete terminal routes: original signed Weil form or independently proven arithmetic criterion. Those routes are OR alternatives; requirements within either route are AND.
- `scripts/uoi_validate.py`: Python stdlib-only, deterministic **read-only** DAG/receipt/scope validator and prioritization reporter. No network calls, file writes, process execution, GitHub API, or workflow dispatch.
- `scripts/test_uoi.py`: fail-closed regression suite: unknown dependencies, cycles, duplicate obligations, forged receipts, unauthorized dispatch/promotion, preservation of the original odd-operator cursor, route separation and heavy-job review-only behavior.

This integration **does not** change the historical research-tree `research/obligations.json`, its original `W-ODD-NEG` cursor, `docs/OBLIGATION_FIRST_PROGRESSION.md`, or any accepted SHA-bound numerical/Lean source.

## Operator commands (read only)

```sh
python scripts/uoi_validate.py research/unified/obligations.json --plan
python scripts/uoi_validate.py research/unified/obligations.json --plan --json
python -m unittest discover -s scripts -p 'test_uoi.py' -v
```

The `--plan` output is **a list of candidates for review, not an executable schedule**. The JSON always declares both `dispatch_authorized=false` and `mathematical_promotion_authorized=false`, regardless of whether a heavy node appears ready. The terminal flag remains false; an accepted proof requires independent external scrutiny and a separately authorized change in the research-governance procedure.

## Intake state (partial evidence review, not closure)

`UOI-INTAKE` and `CI-FANOUT` are review-ready. The other 11 nodes remain blocked on unpaid mandatory dependencies. **UOI-INTAKE has not been closed.** The seven-function source inventory in UOI001 shows:
- **NF:** 708/968 source-specific HD/A gate instances; not a physical full-matrix, original-form, or RH theorem.
- **IV:** IV009 direct original finite Schwartz polarization Lean + strict standard axiom run 44850887402 completed success; historical #761 table needs append-only reconciliation, not retroactive erasure.
- **CF:** canonical source/branch not independently recovered; no closure assignment.
- **GA:** GA032 is a source-level Lean candidate, not compiled kernel acceptance.
- **CP:** CP034 4/4 original source-split/unit-cell declarations passed genuine Lean and standard-axiom audit, not the complete independent spectral/zero argument.
- **PI:** PI034 exact arithmetic replay; no independent full-form spectral correspondence, no Lean promotion.
- **RD:** arithmetic terminal implications and finite-energy source expressions are analytical/conditional; no independently established RH-strength prime estimate, no new Lean acceptance.

## Deployment safety and exclusions

**No** new GitHub Actions YAML, PR, integration merge, branch retarget, scheduled workflow, issue-comment execution hook, runner lease, or heavy research job is introduced by UOI002. Do not interpret push to this governance branch as the old active research lineage; `main` and the stacked NF/IV/CP branches have different workflow inventories.

Before any CI integration is authorized:
1. Complete source/status custody for all seven functions and reconcile remaining scope discrepancies.
2. Audit the **effective** source PR base and head, workflow path and branch filters, required-checks, and Lake manifest preparation order. A zero queue is not proof of safe fan-out.
3. Specify a cheap non-skippable validation check *separately* from source-specific, manually dispatched heavy Lean workflows. No untrusted issue text may become a shell command.
4. Obtain an explicit one-job lease and exact source SHA; reconcile compiler, named axiom, job and artifact digests before any scope-typed acceptance.
5. Retain all historical proof-custody files and original `W-ODD-NEG` obligation ownership until a reviewed compatibility migration.

**Immediate next gate:** UOI003, reconcile the missing CF source custody and effective CI-FANOUT safety; only then arbitrate the first review-ready mathematical obligation. The planner itself never grants execution authority.
