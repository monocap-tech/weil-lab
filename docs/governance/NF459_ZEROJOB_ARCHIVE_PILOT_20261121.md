# NF459 GitHub Actions zero-job archive pilot

Date: 2026-11-21. Evidence class: maintenance experiment; NOT Lean certification.

## Why this workflow

- Original source: `.github/workflows/nf459-native-original-christoffel.yml`
- Original Git blob SHA-1: `99a5f899fcc257f6d78e0f990abf591735ac1d83`
- Its only declared event on the checked-out maintenance source is `workflow_dispatch`.
- GitHub nonetheless recorded a completed failed `push` event for this workflow (run [44946137989](https://github.com/monocap-tech/weil-lab/actions/runs/44946137989)) with ZERO jobs. The workflow is not on default `main`.
- The exact 825-character source is preserved at `docs/governance/archived-workflows/nf459-native-original-christoffel.yml.txt`.

## Controlled change

Archive the workflow outside `.github/workflows` in an isolated branch. No jobs, scripts, Lean declarations, numerical certificates, receipts or data are altered. It can be restored by copying these exact text bytes back to the original path.

## Falsifiable check

After the source disappears from `.github/workflows`, compare subsequent branch pushes with existing zero-job runs. If failures persist against this path, the cause is not simply a currently present GitHub Actions YAML file. A failure record on the deletion push itself may reflect workflow-registration lag and is not conclusive.

**Operational limits:** The archived file no longer participates in Actions and is not manually dispatchable until restored. This is a probe, not proof that GitHub server-side validation or registry state was the original cause. No automatic broad retirement is authorized based solely on this pilot.
