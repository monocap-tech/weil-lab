# Weil-Lab — NF755
## Phase III original numerical compiler recovery: verified pull-request fan-out and bounded trigger repair

### 1. Actual compiler custody — no unsupported Lean acceptance

On NF755 recovery, the genuine original signed Weil numerical HD row-zero/A column-zero index-zero pilot jobs were unchanged: **all six remained QUEUED, with no job steps or numerical audit artifacts**:

| Stage | Frozen original HD/A index-zero positions | Authentic GitHub Actions run | Exact job |
|---|---|---|---|
| NF748 | 64–71 | [44846764448](https://github.com/monocap-tech/weil-lab/actions/runs/44846764448) | 136668270768 |
| NF749 (historical NF734 gap) | 24–31 | [44847296036](https://github.com/monocap-tech/weil-lab/actions/runs/44847296036) | 136670051321 |
| NF750 | 72–79 | [44851970198](https://github.com/monocap-tech/weil-lab/actions/runs/44851970198) | 136685181507 |
| NF751 | 80–87 | [44852365683](https://github.com/monocap-tech/weil-lab/actions/runs/44852365683) | 136686459933 |
| NF752 | 88–95 | [44852653466](https://github.com/monocap-tech/weil-lab/actions/runs/44852653466) | 136687397543 |
| NF753 | 96–103 | [44853095710](https://github.com/monocap-tech/weil-lab/actions/runs/44853095710) | 136688825709 |

The authenticated previous original HD/A two-frontier count remains **596 / 968**, not 692. In particular original index-zero 24–31 is not accepted. Retain original NF737, NF739, NF742 and NF743 success artifacts and the historical source-equal NF728/NF729/NF743 accepted center-cache objects unchanged.

### 2. A verified, non-hypothetical CI scheduling defect

The NF754 diagnostic PR #806 changed **only two files** (`scripts/nf754_original_numerical_ci_backpressure.py` and `docs/NF754_ORIGINAL_NUMERICAL_CI_BACKPRESSURE_RECOVERY.md`) relative to its parent. Yet GitHub Actions reported **62 pull_request workflow runs** for its head branch, including unrelated expensive legacy NF481, NF501, NF474 and NF485 tests.

Concrete evidence:
- [NF481 numerical source workflow 44854750709](https://github.com/monocap-tech/weil-lab/actions/runs/44854750709) was queued on NF754's unrelated diagnostic PR, despite being a 65-minute + 25-minute two-job native test with unchanged original J8 inputs.
- [NF501 original 242D workflow 44854750787](https://github.com/monocap-tech/weil-lab/actions/runs/44854750787) was queued on that diagnostic PR, despite its expensive 65-minute + 20-minute pipeline and its pre-existing *scoped push* event.
- [NF474 independent Fraction audit 44854750911](https://github.com/monocap-tech/weil-lab/actions/runs/44854750911), and [NF485 exact rational log-moment 44854750775](https://github.com/monocap-tech/weil-lab/actions/runs/44854750775) likewise queued.

All four workflow YAML files genuinely had **bare `pull_request:` without `paths:`**. The NF501 workflow's `push` was already path-scoped, but its **pull_request** event had been accidentally left unrestricted. Thus unrelated pull requests really can enqueue large, historically completed source tests.

A separate repository-wide GitHub Actions snapshot found **2,316 queued** and **257 in_progress** runs. This establishes a contributory pull-request fan-out problem, **not** that this is the sole cause of queued runner delays, that GitHub is necessarily globally impaired, or that any of the original Lean mathematical proofs has failed. The separate recent `push` zero-job failure cases still require their own workflow event/branch validation; do not conflate them with queued `pull_request` numerical jobs.

### 3. Actual NF755 trigger-scope repairs

Only the following four *legacy GitHub Actions workflow definitions* are changed. **No Lean source, original numerical generated bank, frozen original `NF702/NF703` inputs, prior accepted `.olean` objects, job steps, runtime timeouts, artifact identities, push triggers, or manual-dispatch triggers change.** The complete before/after source was compared independently and confirmed **solely the insertion of `pull_request.paths`**.

| Historical workflow | New automatically triggering PR changes |
|---|---|
| `nf474-original-j7-fast-source-independent-fraction-audit.yml` | Its own workflow YAML; `verify_nf474_original_J7_right_panel_and_partial_union_exact.py` |
| `nf485-j8-principal-image-log-moment-algebra.yml` | Its own workflow YAML; `verify_nf485_J8_principal_image_log_moment_algebra_exact.py` |
| `nf481-original-j8-20jet-source-unconditional-energy.yml` | Its own workflow YAML; its original NF471, NF481 source and NF481 independent exact energy audit scripts |
| `nf501-original-J242-correlated-log-projection.yml` | Its own workflow YAML; the original NF501 numerical projector script and independent exact Fraction auditor |

This retains automatic testing of the four direct source obligations and **manual `workflow_dispatch`** for transitive dependency changes or intentional historical reruns. NF501's original branch-filtered path-scoped **push** trigger is preserved exactly. This scoped pilot does not claim to repair the other legacy workflows still matching arbitrary PRs.

### 4. Offline fan-out detector and regressions

**New** `scripts/nf755_ci_pr_workflow_fanout_audit.py` supports:

```bash
python scripts/nf755_ci_pr_workflow_fanout_audit.py selftest
python scripts/nf755_ci_pr_workflow_fanout_audit.py audit
```

`selftest` performs seven synthetic controls for unscoped/scoped PR recognition, exact path parsing, absent PR event recognition, no NF754 diagnostic-file matches across the four repaired workflows, and continued triggering on all four legitimate workflow/input paths.

`audit` walks `.github/workflows/*.{yml,yaml}`, classifies simple PR event blocks as unrestricted/scoped/paths-ignore, validates the exact four introduced scopes, checks manual dispatch and preserved NF501 push, and writes `nf755-original-CI-pull-request-fanout-audit.json`. The detector deliberately marks complex YAML triggers separately; it is a **conservative static inspection**, not a complete GitHub Actions parser, not a mathematically certified theorem and not an automatic CI workflow.

No additional heavy numerical kernel or automatic CI status observer is created by NF755. No existing queued run is cancelled by this change. Pending old queued events are **not retroactively removed** by changing workflow definitions.

### 5. Mathematical and operational exit conditions

There are six disjoint original eight-coordinate HD/A batches awaiting genuine numerical Lean execution and the complete **35-target strict `#print axioms`** audits. After independently audited source-bound kernel/axiom/immutable-artifact acceptance for exactly `k` of these six, the original designated frontier count is `596 + 16*k`. The conditional maximum 692 requires all six to pass, and even then original index-zero 104–241 remains unaccepted (276 further gate instances).

**Actual count is 596/968.** Complete original 242×242 matrix enclosure, full original vector/payment enclosure, arbitrary-support mixed Weil positivity, global Weil positivity and RH remain **OPEN**.

**Next NF756:** Reassess the six existing queued numerical jobs, check for any actual compiler log/audited artifact, inspect the offline workflow inventory and prioritize further narrowly justified path scoping of the largest remaining unscoped legacy PR workflows. Do not flood GitHub Actions with additional original numerical pilot workflows before recovering prior actual jobs. Continue independent Phase IV support-extension and cross-projection work under its IV iteration numbers; no equivalence is assumed.
