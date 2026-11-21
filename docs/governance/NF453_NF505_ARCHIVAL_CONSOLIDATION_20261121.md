# NF453–NF505 workflow archival consolidation — 2026-11-21

**Scope: custodial GitHub Actions cleanup, not mathematical certification.**

Source baseline: `research/iv026-single-lane-iv009-kernel-recovery` at `37fc895c88f9b52a35d6d867c3d0ecc4d9661a5f`.

- The 64 historical unrestricted NF453–NF505 PR triggers were already retired in the first stage (see the two Git-blob ledgers).
- This second stage archives **62** manual-only workflow definitions as unchanged Git blobs under `docs/governance/archived-workflows/` with `.yml.txt` suffixes and removes their old `.github/workflows/*.yml` entries.
- NF459 was moved in a separate one-file pilot (commit `2d36d04c7d98962c82f3058e70f8d84b90ed6751`), followed by the remaining 61 here.
- Two historical NF workflows, NF501 and NF504, retain source-limited `push` triggers; they remain installed and are not archived.
- The active `.github/workflows` directory is expected to decrease from **613 to 551 files**. All original workflow contents are recoverable by original and archived Git blob identities. No Lean source, numerical input, source audit implementation, historical artifacts, or accepted proofs are altered by workflow moves.

**Important behavior change:** archived workflows are no longer executable or manually dispatchable without being restored to `.github/workflows` (and, where applicable, registered on the default branch). These files are historical custody only.

**Evidence and limits:** after the NF459 pilot push, nine zero-job failure records remained while NF459 was absent. This is consistent with reducing workflow-registration noise. It does not identify the server-side validation root cause. A failed record with zero jobs is not a Lean failure and should not be counted as runner execution.

**Validation:** `scripts/workflow_retirement_inventory.py --check` now accepts either an active matching Git blob or an archived matching Git blob for each of the 64 custody records. The script is a static inventory/identity check, not a full GitHub Actions YAML parser or compiler test.

**Promotion gate:** before applying to IV026, compare the exact Git tree, require 62 path moves (unchanged Git blobs), one auditor update, and one governance note, confirm no math source edits, recheck zero queued/in-progress runner jobs and branch head. No heavy workflow dispatch.
