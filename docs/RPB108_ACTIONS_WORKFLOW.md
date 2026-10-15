# RPB108 GitHub Actions checkpoint workflow

The RPB108 Route Consolidation validators already have an exact `--replay`
mode. `.github/workflows/rpb108-certificates.yml` runs that mode on a
GitHub-hosted runner, reducing dependence on an interactive model session for
the arithmetic workload.

## Workflow contract

- **Push/PR on the RC research branch:** a fast custody job, then exact
  reverse replay of the **latest numbered RC validator** in the checked-out
  commit. The latest script, matching note and matching certificate must each
  be unique. Replay checks its committed JSON and every inherited blob pin.
- **Manual `workflow_dispatch`:** choose `latest` or an RC number and
  `replay` (default) or `custody`. GitHub exposes manual dispatch only once
  this workflow also exists on the repository's default branch; until then,
  use its branch-push and pull-request triggers.
- **Outputs:** job logs, step summary, and JSON report artifacts.
  Nothing is committed back by the workflow.
- **Limits:** full replay is time-limited to 300 minutes. Same-ref newer
  pushes cancel superseded runs. No secrets and no write permission are used.
  The Lean build remains separately handled by `lean.yml`.

## Local equivalence

From the repository root, after checking out the desired RC commit:

```bash
python scripts/rpb108_actions_verify.py --checkpoint latest --mode custody
python scripts/rpb108_actions_verify.py --checkpoint latest --mode replay
# A specific checkpoint:
python scripts/rpb108_actions_verify.py --checkpoint 280 --mode replay
```

The second invocation performs the same command the underlying checkpoint
note documents:

```bash
python scripts/validate_rpb108_rc280_combined_jump_tail.py \
  --output certificates/rpb108_rc280_combined_jump_tail.json --replay
```

It reuses historically pinned source certificates when the validator does;
this is **not** an independent regeneration of every ancestor, a Lean proof,
a peer-reviewed verification, or a Stage I/RH closure claim. Preserve the
checkpoint note's exact mathematical scope and failure conditions.

## Operational handoff

1. Continue authoring RC notes, certificates and validators on
   `research/rpb108-route-consolidation`.
2. Review the latest automatic replay result before declaring a checkpoint
   independently reproduced in CI. A repository commit by itself does not
   establish that its Actions job has passed.
3. For expensive old checkpoints, run manual targeted replay rather than
   bundling the entire historical chain into every push.
4. On failure, inspect the job log and downloaded report. Do not regenerate
   or overwrite a pinned historical certificate to silence a mismatch.
5. Keep mathematical proof design and source custody in reviewable PRs;
   use Actions only for deterministic arithmetic, lint/custody, and replay.
