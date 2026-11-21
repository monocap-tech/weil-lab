# Weil-Lab — UOI005: four source-bound PR workflow repair previews

**Date:** 2026-11-21  **Status:** Staged, provenance-verified PREVIEW. **NO RESEARCH BRANCH PATCH APPLIED; no pull request, Actions dispatch, branch retarget or theorem advancement.**

## Integration choice and safety reason

Candidate numerical integration source: `research/nf768-original-indexzero-104-111-controlled-kernel`, fixed commit `b477d9a8eb6c33781a8eee7c1208de93c705f307`. This is a **candidate** research source for evaluating the repairs, not a declared universal integration base. Its accepted original HD/A scope is 708/968 gate instances, which must not be overwritten or recast as a complete signed Weil form. The separate IV branch has divergent source/workflow history and requires its own real base/head audit. The patch generator **does not** touch the source tree and does not create a research PR.

**Why stage instead of commit directly to NF768:** Original source branch SHA is a frozen proof-custody anchor. The inherited ~608-workflow tree contains other bare `on: pull_request:` files. Moreover push-trigger reachability, stacked-PR required checks and original IV Lake bootstrap have not been reconciled. Directly pushing a four-workflow edit would not justify lifting the CI incident hold and could itself trigger unrelated jobs.

## Four exact source-dependent repair candidates

All source-workflow blobs and source dependencies were inspected against the original NF768 recursive Git tree (8,783 entries, complete `truncated=false`) and relevant Python script bodies. **28 path references** (four workflows and 24 direct source/data paths) were checked for existence and SHA identity. The selected workflow definitions are still bare ordinary pull-request events with manual dispatch retained.

| Workflow | Frozen source Git blob | Proposed path filters |
| --- | --- | ---: |
| NF459 native 244D Christoffel | `3ef43267450c93ae65c5603d63167c57cd902a7f` | 12 (workflow + source script + 10 data inputs) |
| NF460 bulk seam H1 | `8b8c399211523dc1d2711ed7689e617bd9837f26` | 9 (workflow + source script + 7 data inputs) |
| NF465 derivative resolution stop | `775939c38730184d1fe4f735700b6f98e01fa437` | 2 (workflow + source script) |
| NF471 joint arch mean | `f93fbb51a56a073bb329e2e6079ca8edf781e532` | 5 (workflow + source script + 3 data inputs) |

**Scope caveat:** This is a checked *declared direct-input inventory*, not a transitive-import theorem. The NF471 code also uses a pinned external checkout. For changes to the pinned external source, Python environment, transitive script/data dependencies, or job executor semantics, manual workflow dispatch remains the intentional recovery channel. NF458 and NF464 were deliberately **not** included: NF458 dynamically delegates to NF459/NF461, while NF464 imports NF463, which itself imports NF462/NF453 and their own data dependencies. They require a separately audited transitive closure.

## Installed governance-only artifacts

- `research/unified/repairs/UOI005_nf768_four_source_scopes.json`: exact original research commit, frozen workflow Git blobs and each direct source blob SHA. Preserves `approved_for_push=false`, `approved_for_pr=false`, `dispatch_authorized=false`.
- `scripts/uoi_source_scope_patch.py`: Python stdlib-only **dry-run** patch builder. Checks every expected source/workflow Git blob before acting; demands exact `on: pull_request:` + `workflow_dispatch:` shape; inserts **only** literal `pull_request.paths`; verifies the original jobs body byte-for-byte; no network or shell; never changes input sources. Optional preview is written to a **separate directory**, never to source or a parent. Refuses already scoped, drifted, unknown, or partially missing sources.
- `scripts/test_uoi_source_scope_patch.py`: **23/23 locally executed fail-closed unit tests**, including SHA drift, missing source, manifest tampering, path traversal, duplicate input, parent/nested output alias, unchanged jobs, preserved manual dispatch, and proof of no automatic approval.
- `research/unified/repairs/UOI005_nf768_four_source_scopes.patch`: standalone proposed textual Git patch generated against exact retrieved original NF768 YAML, containing only the four approved workflow-event stanzas; **not applied on research branch**.

### Reproduce with a complete exact checkout

```sh
python -m unittest discover -s scripts -p 'test_uoi_source_scope_patch.py' -v
python scripts/uoi_source_scope_patch.py \
  --source-root /absolute/path/to/checked-out-NF768 \
  --plan research/unified/repairs/UOI005_nf768_four_source_scopes.json
python scripts/uoi_source_scope_patch.py \
  --source-root /absolute/path/to/checked-out-NF768 \
  --plan research/unified/repairs/UOI005_nf768_four_source_scopes.json \
  --preview-dir /absolute/path/to/SEPARATE-preview
```

This is **not** a CI dispatcher. No source checkout was cloned in the offline execution environment; the direct four-original-source YAML transformation is separately checked byte-for-byte in the GitHub source inspection used to construct the patch. The Python test receipt is a synthetic-fixture regression suite, not a full source-branch repair execution certificate.

## Result and operational NO-GO

UOI005 **discharges a four-workflow patch proposal**, not the repository's `CI-FANOUT` obligation. **Do not open a PR, dispatch heavy work or rewrite NF768.** Before integrating any repair:

1. Audit all real pull-request and push-event workflow triggers in a complete intended integration head and stacked base, including path semantics, opt-in labeled workflows, required checks and runner budget. Existing UOI004 source-bound two-tree scanner is an additional conservative negative gate.
2. Determine whether repair should be applied to a fresh isolated child integration branch rather than any certified source SHA; independently check branch-creation/push fan-out first.
3. Verify no source/axiom/numerical artifacts or historical `research/obligations.json` / `W-ODD-NEG` obligations are touched. Keep IV025 generated Lake manifest strict source preflight correctly ordered after `lake update` on the actual IV branch.
4. Obtain operator authorization for one SHA-pinned, manually leased pilot **only** after branch-base required check, effective workflows, and queue conditions are independently paid.

**Next: UOI006** completes the remaining unrestricted-workflow inventory and proposes bounded repairs across the selected integration lineage. For now the unified mathematical programs remain a single UOI-controlled dependency graph with two distinct (OR) RH-facing routes. RH and support-independent original Weil positivity remain open.
