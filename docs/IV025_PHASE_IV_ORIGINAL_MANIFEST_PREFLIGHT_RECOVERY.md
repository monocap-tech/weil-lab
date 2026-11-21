# Weil-Lab — IV025: Real original Lean certification recovery, not another support-extension claim

**Canonical Phase IV stage:** IV025. Recovery branch `research/iv025-original-manifest-preflight-recovery`, stacked on IV024 PR #811. **Deliberately no new pull request was opened at this stage:** the previous IV024 pull request already triggered at least 62 repository workflows, many unrelated NF### gates, while the repository reports thousands of queued jobs. Generating another pull_request fan-out would add to the operational backlog without proving a single original Lean theorem. This branch is committed and suitable for subsequent controlled backport to original stage branches when CI capacity returns.

**No Phase III NF### content changed. No new signed Weil positivity theorem or RH claim.**

## 1. Actual GitHub Actions queue diagnosis

Observed at IV025 inspection via GitHub REST API, separately from mathematical proof status:

| Repository-wide GitHub Actions filter | Total |
|---|---:|
| queued | 2369 |
| in_progress | 263 |
| pending | 32 |

The existing repaired IV009 run [44850887402](https://github.com/monocap-tech/weil-lab/actions/runs/44850887402) is still QUEUED (run_attempt=1). IV018 [44850967574](https://github.com/monocap-tech/weil-lab/actions/runs/44850967574) remains PENDING. IV019 [44851439481](https://github.com/monocap-tech/weil-lab/actions/runs/44851439481), IV020 [44851946887](https://github.com/monocap-tech/weil-lab/actions/runs/44851946887), IV021 [44852596209](https://github.com/monocap-tech/weil-lab/actions/runs/44852596209), IV022 [44853338807](https://github.com/monocap-tech/weil-lab/actions/runs/44853338807), IV023 [44854690456](https://github.com/monocap-tech/weil-lab/actions/runs/44854690456) and IV024 [44855627588](https://github.com/monocap-tech/weil-lab/actions/runs/44855627588) also remain QUEUED.

Other repository jobs are IN PROGRESS and completed results exist, so Actions is not categorically disabled. Queue size alone does not establish whether the specific root cause is runner concurrency, billing policy, rate limiting, workflow approval, scheduling pressure or another external issue. We do not control those settings through this repository source and cannot claim a fix to them.

A direct [IV024 PR #811](https://github.com/monocap-tech/weil-lab/pull/811) head-commit workflow inventory returned **62 distinct pull-request-triggered workflows in its first page**, including numerous unrelated original NF### jobs. This strongly motivates *not* opening another automatic PR during backlog triage. It is evidence of significant PR workflow fan-out, not a proof of one specific queue root cause.

## 2. NEW concrete deterministic original CI blocker: missing generated Lake manifest at SOURCE preflight

The actual GitHub source root in this branch contains:

    lean-toolchain                = leanprover/lean4:v4.34.0
    lakefile.toml                 = mathlib git rev v4.34.0
    lake-manifest.json           = NOT TRACKED / ABSENT AT CHECKOUT

The original audit scripts IV017–IV023 listed `Path("lake-manifest.json")` in their source dependency list, then ran:

    for p in DEPS:
        assert p.is_file()

**before** the workflow's install stage executed `lake update`, which generates `lake-manifest.json` at project root. This is a deterministic preflight ordering error, quite separate from the queued Actions problem and from the truth of any theorem.

On an ordinary fresh checkout, these seven audits would fail prior to invoking the actual Lean compiler, regardless of whether the downstream mathematical source is valid. This failure is NOT a disproven source theorem or RH issue.

### IV025 committed exact remedy

In ALL SEVEN stage-specific original source auditors:

- IV017: `scripts/iv017_original_narrow_diagonal_coercivity_audit.py`
- IV018: `scripts/iv018_original_three_cell_coercivity_audit.py`
- IV019: `scripts/iv019_original_width_capacity_kernel_audit.py`
- IV020: `scripts/iv020_original_wider_three_cell_kernel_audit.py`
- IV021: `scripts/iv021_original_three_cell_smooth_partition_audit.py`
- IV022: `scripts/iv022_original_four_cell_prime_capacity_audit.py`
- IV023: `scripts/iv023_original_four_cell_prime_transfer_audit.py`

the **source-only preflight** allows ONLY the specifically identified generated `lake-manifest.json` to be absent, but continues to require every other original source dependency and every theorem/axiom inventory check.

The **KERNEL verify** method now separately asserts that the Lake-generated manifest EXISTS after `lake update` and the real Lean source compilation. The manifest remains in the SHA-fingerprinted source/toolchain dependency list; no verified dependency is dropped. Each stage additionally includes the actually TRACKED `lakefile.toml` in its dependencies, binding both the pinned Mathlib `rev=v4.34.0` declaration and the real generated manifest at final verification.

This is *not* a bypass of a kernel axiom audit: source preflight can succeed without an ungenerated file, whereas genuine kernel acceptance still requires that generated file, both original compiled `.olean` artifacts (or the stage's actual objects), all original source names and only standard axiom receipts.

**IV009 is unchanged** by the seven-source manifest fix; its dedicated auditor did not make the bad manifest preflight assumption, and the original IV009 mathematical raw-transform summability repair still awaits actual compiler confirmation.

### Regression contract

New `scripts/iv025_manifest_order_source_regression.py` statically parses each of the SEVEN actual audited Python files into an AST and checks:

1. Source dependency inventory still includes BOTH the tracked `lakefile.toml` and `lean-toolchain`, plus generated `lake-manifest.json`.
2. Preflight skips **only** the generated manifest, and still asserts the existence of all OTHER original physical mathematical dependencies.
3. Kernel verification explicitly asserts manifest existence and fingerprints the full dependency list, and still requires original `.olean` and strict `sorryAx` checks.
4. Negative controls intentionally remove the kernel manifest requirement, the preflight-only exception, and the pinned Lake configuration. Each mutation must be rejected; pass means the regression actually fails closed.
5. Output clearly states NONKERNEL, no original Weil theorem acceptance.

This is a source/CI-ordering regression, NOT a mathematical theorem proof or a claim that the Lean code compiles. A read-only post-edit GitHub review independently confirmed all seven source files contain the intended separate guards and pinned config fingerprint bindings.

## 3. Earliest real original Lean source recovery without PR fan-out

Committed a focused opt-in script:

    bash scripts/iv025_recover_first_original_lean.sh

This script is NOT a new automatic GitHub PR workflow, and has NOT executed on a genuine Lean toolchain in IV025. It is a reproducible command sequence for an authorized checkout/runner with the real `lake` binary installed.

The actual sequence is:
1. Verify `lean-toolchain` and `lakefile.toml` exist; stop on missing actual `lake` or Python, explicitly reporting BLOCKED.
2. Run the exact already committed original IV009 source-only preflight and record pinned toolchain SHA-256.
3. Run `lake update` from the tracked Mathlib v4.34.0 configuration, require genuine generated `lake-manifest.json`, fingerprint its SHA-256, retrieve pinned Mathlib cache.
4. Run the full REAL `lake build WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization` with failure-propagating shell pipeline and preserved compiler log.
5. Run the authentic direct `lake env lean WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean` source to obtain original `#print axioms` receipts.
6. Run `python3 scripts/iv009_original_schwartz_polarization_audit.py verify`, which requires the ACTUAL compiled .olean and all eight new + four original standard-only axiom receipts.

The bash script fails closed under `set -euo pipefail`. It NEVER prints a PASS absent the real kernel compiler, successful original standard-only axiom audit and source-bound compiled object. It does not claim to repair downstream IV017–IV023 mathematical source errors before their diagnostics appear.

Because there are already >2,000 queued runs, IV025 **does not automatically start another CI fan-out**. Backporting the seven audited files to individual stage PR branches must be coordinated with available runner capacity; on the IV025 stacked branch, all seven ordering patches are already present. The old stage PRs still require those patches before their own fresh preflight executions can succeed.

## 4. Mathematical research boundary

The IV023 FOUR-CELL source theorem candidates remain pending:
- actual smooth original physical complex Schwartz partition f=f_old+f_plus+f_minus;
- full original ±log Λ-active prime transfer P_original(f,f)=P_original(f_old,f_old) including surviving NF600 n=9;
- historical 2/5 old n9 cost transfer using true physical mass monotonicity;
- signed Gamma + BOTH original poles with physical support measure 17/2000 and prospective restricted 1/16 coercivity.

IV024's separately constructed exact prime-power graph has only two surviving old-old n9 edges and no new-support edges, but arithmetic graph consistency does not prove the full original signed quadratic form or its Lean realization. Its log2 collision negative control and width-capacity negative control show the geometric and analytic gates are genuinely distinct.

This remains a restricted support-extension investigation. The separate cross-projection question requires an independently defined arithmetic/spectral target, exact map of common domains, full signed pairing including Γ and both poles, and independent mass/normalization hypotheses. None is proved by correcting Lake's manifest ordering.

## 5. IV026 decision gate

IV025 is **branch-committed, not a new pull request**, in order to avoid an additional ~62 unrelated workflow fan-outs during heavy queue load. This is an operational safeguard, not a reduction in mathematical standards.

The immediate subsequent work is to obtain an ACTUAL complete IV009 kernel receipt or a concrete compiler error from the existing queued job/controlled local runner, then fix the exact source obligation and backport the seven auditor-order corrections into the relevant stacked source PRs as capacity allows.

Until the genuinely compiled original `.olean` objects and strict standard-axiom receipts exist, **no IV017–IV023 candidate becomes certified.** Phase III NF### numerical source certification remains independent and untouched.

**No global Weil positivity, RH, or independent spectral equivalence.**
