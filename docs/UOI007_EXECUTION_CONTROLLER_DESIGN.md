# Weil-Lab — UOI007: minimal source-pinned controller, inspection-only candidate

**Date:** 2026-11-21. **Parent:** UOI006, issue #867. **Classification:** governance design and locally tested **non-executable** controller prototype. **NOT** a GitHub Actions workflow deployment, source-workflow repair, remote SHA attestation, protected-branch approval, proof certification, or authorization to resume heavy CI.

## Decision: one default-branch controller, NOT 600 historical workflows

GitHub documents that `workflow_dispatch` requires its workflow definition to exist on the default branch; its UI/API availability on historical research-only branches cannot be inferred from the mere presence of `workflow_dispatch:` in their YAML. The current `main` at `a117b3cf39d52643a2f33826fcbf8725cb5f86cf` has exactly three workflow files; none is a general NF/IV UOI controller. (The existing `rpb108-manual.yml` dispatches a moving, RPB-specific research branch and is not a safe general execution entrypoint.)

**Chosen design:** a single small, manually triggered *read-only source inspection* workflow **eventually installed on main after independent review**. It accepts a `source_key` *choice* (NF768 or IV025), never an arbitrary Git ref or shell command. A vetted code-side pin table and a separately committed catalog bind each key to the exact historical commit recorded by UOI006. The operator's request cannot grant its own approval. Later heavy execution would be a separately designed, authorized workflow, not a hidden mode of this controller.

**Relevant GitHub Docs:**
- Workflow dispatch default branch: <https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_dispatch>.
- Skipped path-filtered required checks may remain pending: <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onpull_requestpull_request_targetbranchesbranches-ignore>.

## Locally tested implementation (governance branch only)

| Staged path | Purpose |
| --- | --- |
| `scripts/uoi007_preflight.py` | Stdlib read-only validation and fixed code-side allowlist; imports existing `uoi_validate.py`, requires consolidation hold and open `CI-FANOUT`; returns no execution permission under any successful input. |
| `scripts/test_uoi007_preflight.py` | **30/30 local unit tests PASS**, including bad source keys and injection text, divergent frozen SHA, catalog tampering, false approval, wrong event/ref/repo, a lifted hold, and fail-closed missing inputs. |
| `research/unified/controller/UOI007_frozen_sources.json` | Source-identity agreement with UOI006 for NF768 `b477d9a8eb6c33781a8eee7c1208de93c705f307` and IV025 `f89952aebfbb1e9775a9fb0dbbe71995ae636b04`. No executable job/command field. |
| `research/unified/controller/UOI007_manual_preflight.workflow.yml.txt` | **Text draft only**—*not* in `.github/workflows`. Its only trigger is `workflow_dispatch`, with `contents:read`, `main`-ref job guard, immutable controller revision checkout via `${{ github.sha }}`, explicit SHA check, 5-minute timeout, static single concurrency group and no research source execution. |

Read-only local operator commands (exact candidate source key):

```sh
python scripts/uoi007_preflight.py \
  --manifest research/unified/obligations.json \
  --catalog research/unified/controller/UOI007_frozen_sources.json \
  --source-key NF768
python -m unittest discover -s scripts -p 'test_uoi007_preflight.py' -v
```

Successful inspection produces an immutable snapshot *identifier*, not a proof of a live remote commit lookup. Results deliberately carry:

```json
{
  "snapshot_matches_frozen_UOI006_record": true,
  "fresh_remote_commit_attestation": false,
  "required_checks_authenticated": false,
  "external_operator_approval_authenticated": false,
  "source_workflows_fully_audited": false,
  "heavy_runner_lease_issued": false,
  "dispatch_authorized": false,
  "execution_permitted": false
}
```

**Security distinction:** Matching a SHA to a code- and catalog-pinned record proves *internal consistency only*, not commit ancestry, current remote content, source safety, or independent approval. The `main` branch will require an authenticated repository rules/required-check contract and an appropriate review policy before installing any controller. Its versioned dependencies (`actions/checkout`, `setup-python`) should be pinned to reviewed immutable action SHAs in the deployment review. This prototype does not execute user-supplied commands, `git checkout` research source, call the GitHub API, create artifacts, alter status, or launch subprocesses.

## Exact safety requirements before making it live

1. **Main deployment review.** Confirm default-branch workflow placement, job/event semantics, actor permissions and protections, and approved immutable action versions. Never deploy 608/612 historical workflow files to `main` to solve dispatch.
2. **Authoritative required checks.** Obtain an operator-admin read of real branch protection and stacked PR required checks. The current integration's branch-protection API returns 403; an empty ruleset list is not a sufficient assurance.
3. **Remote commit/source attestation.** In a later enhanced controller, verify the selected immutable commit actually exists in the correct repository, conforms to an independently approved ticket/attestation, and is reviewed before any checkout/execution. **Do not execute source code based solely on catalog equality.**
4. **Runner lease and capacity.** Establish a cross-workflow one-job lease (not just the single workflow's concurrency group), no queued protected numerical jobs, and hard timeout/permissions/no-secret boundaries. An inspection-only job is not a heavy-lease mechanism.
5. **End-to-end source lineage.** Finish all 608/612 workflow trigger and required-check compatibility audits and IV source's `lake update`/manifest-before-preflight requirement; NF450–NF505 still contains 45 vs 64 bare PR workflows on respective frozen heads.
6. **Evidence reconciliation.** Receipt must bind source commit, code version, job/run ID, proof/check status, strict named Lean axiom checks and immutable artifact SHA; never infer full original Weil/RH from a numerical gate or conditional analytic reduction.

Until these prerequisites are paid, UOI `CI-FANOUT` is **OPEN** and `execution_policy=consolidation_hold`, and *no* GitHub Actions execution—including a dry-run preflight—is deployed by UOI007.

## Next cursor

**UOI008:** independent controller release-gate review and source-complete NF/IV workflow audit. The immediate attainable outcome is a *reviewed path to a low-cost manual inspection on main*, not a heavy proof job. Any actual `main` deployment must be a separate explicitly approved change after branch/rules audit. Preserve `W-ODD-NEG`, NF accepted 708/968, and all source identities.
