# UOI004 — CI lineage and manual-execution control

**Date:** 2026-11-21. **Status:** READ-ONLY SOURCE GATE INSTALLED; **CI-FANOUT REMAINS OPEN**. This is operational research governance, not Lean or arithmetic certification, no PR, workflow YAML, heavy dispatch, or cross-branch merge.

## Direct source finding: current NF and IV lineages are not contained

Reopened actual GitHub `pull_request` files in NF753 PR #797 (base `research/nf752-original-indexzero-088-095-live-compiler-recovery`, head `research/nf753-original-indexzero-096-103-kernel-five-run-custody`) and IV023 PR #805 (base `research/iv022-original-four-cell-capacity-prime-separation`, head `research/iv023-original-four-cell-schwartz-partition-and-prime-transfer`). The NF753 and IV023 research directories contain respectively **607** and **611** workflow files; modern NF768 and IV025 contain **608** and **612**. These totals are not counts of automatically triggered workflows.

**Direct risk witnesses** (actual Git blobs, all with bare `on:\n  pull_request:` and no `paths` or `types` guard):
- NF753 HEAD `nf457-original-log-peel.yml` (`25bb13e47e87150d54e13240ddd41a3a793fbb3c`), `nf463-original-j7-spatial-necessity.yml` (`f96a10937fc703850209d1502b13b696a08d320e`).
- NF753 and IV023 BASE (identical historical blobs): `nf453-original-j7-j8-principal-signed.yml` (`e44bf3843d1fc8509b399812dd5de216cf92680b`); `nf454-original-square-energy.yml` (`ba37ff2cfc825f81b1ee0b8aa9a4d535780254f0`); `nf456-original-two-ray-residual-budget.yml` (`249eef499a0b208faea7f211937e4a45b813c413`); `nf471-original-j7-complete-mean-receipt.yml` (`a1c33ea0910a5378c0ea21bfc422994153101477`).
- IV023 HEAD remaining unrestricted: `nf458-original-endpoint-leverage-gate.yml` (`fa932e125909f312d8660bcaea821ed53367a7b5`), `nf459-native-original-christoffel.yml` (`fe9991d3e4af8f84c1ed2409c9fcedbeadf667ac`), `nf460-original-bulk-seam-h1.yml` (`8b8c399211523dc1d2711ed7689e617bd9837f26`), `nf464-original-j7-macroscopic-necessity.yml` (`5743a4c3a2042262ecab68b3b4de3df0b40947a4`), `nf465-j7-derivative-resolution-stop.yml` (`775939c38730184d1fe4f735700b6f98e01fa437`), `nf471-original-j7-joint-arch-macroscopic-mean.yml` (`f93fbb51a56a073bb329e2e6079ca8edf781e532`). At least `nf458` (NF768) and `nf459` + NF471 joint (IV025) remain at the same bare-PR blob identities.

These explicit counterexamples are **sufficient to keep the CI-FANOUT gate blocked** even though many workflow filters have already been repaired. They do **not** establish the exact current total of unsafe workflows or the number of jobs any particular PR will launch. Some historical PRs have demonstrably generated 60+ jobs; event semantics, default branch and stacked-base behavior must be inspected before asserting a future count.

## Installed read-only two-tree fan-out gate

- `scripts/uoi_ci_fanout_gate.py`: stdlib, no network, shell, API call or file mutation. Takes two *complete local* source checkouts and an independently obtained list of PR changed files. Scans every `.github/workflows/*.yml|*.yaml` in both trees. Reports scoped matches, unrestricted pull-request events, YAML configurations it cannot safely classify, and label-only events excluded from ordinary synchronize.
- `scripts/test_uoi_ci_fanout_gate.py`: **16/16 offline tests PASS** on byte-identical committed source files. Includes bare-PR rejection, source path match, labeled-only event separation, unknown YAML fail-closed behavior, base/head divergence and retained `dispatch_authorized=false` even when locally clean.
- **Limitation:** intentionally conservative subset of actual GitHub YAML, branch glob and path filter semantics. Any unknown is unsafe for dispatch. A passing static report **never** proves full GitHub event behavior or required-check satisfiability.

Usage from a locally checked-out governance copy with separate fully checked-out NF or IV `base/` and `head/` trees and an operator-verified exact PR file list:

```sh
python scripts/uoi_ci_fanout_gate.py \
  --base /abs/path/base --head /abs/path/head \
  --base-branch research/exact-stacked-base \
  --changed-files-json /abs/path/verified-pr-files.json \
  --event synchronize --min-workflows 600
python -m unittest discover -s scripts -p test_uoi_ci_fanout_gate.py -v
```

An output flag `static_negative_controls_cleared` is only an input to independent operator review. **The tool always emits `dispatch_authorized=false`, `required_checks_verified=false` and `mathematical_promotion_authorized=false`.** No issue text or command string from untrusted GitHub comments is executed.

## Required checks and manifest ordering: not yet discharged

GitHub repository rulesets response was empty, but branch protection endpoint for this connection is inaccessible (previous 403) and **no per-stacked-base required-check contract has been authenticated**. Thus the required-check gate is still UNVERIFIED, not interpreted as an empty set.

The IV025 repair exists on its particular descendant branch. The repaired Lake environment generation/preflight order must be verified for each future selected source HEAD; it must not be assumed inherited by IV018–IV023 older PRs. Original `lake-manifest.json` is generated and must be tested after Lake bootstrap as specified by the IV025 source-recovery issue #814.

## Explicit go/no-go

**NO-GO for new heavy NF/IV PRs** until the repaired source-scoped workflow definitions are present in the *actual chosen head/base lineage*, a complete two-tree audit has zero bare unrestricted ordinary PR triggers and zero unknown/unsafe configs (or documented and independently tested exclusions), and the required-check and Lake bootstrap gates are externally verified.

Continue read-only/local mathematical work and source conservation. `UOI-INTAKE` still needs final source/acceptance sign-offs, `CI-FANOUT` is **OPEN**, global Weil positivity/RH remain OPEN. NF canonical Phase III acceptance remains **708/968** gate instances, not a full original matrix.

**Next proposed UOI005:** narrow, peer-reviewed repair of the remaining source-unscoped historical triggers on the selected research integration lineage, preserving `workflow_dispatch` and exact original jobs; then run this tool on complete exact base/head checkouts before a single manually leased pilot.
