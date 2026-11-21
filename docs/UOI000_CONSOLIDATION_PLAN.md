# Weil-Lab — Unified Operative Investigation (UOI)

**Date:** 2026-11-21  
**Status:** Governance consolidation **proposal with executable, read-only planning prototype**. No new mathematics, Lean certificate, RH claim, Actions workflow, research PR or heavy job is authorized by this document.

## Decision

One **operative investigation** owns the RH-facing obligation graph. The existing `NF`, `IV`, `CF`, `GA`, `CP`, `PI`, and `RD` names become *execution and verification functions* rather than independent competing research priorities. They keep their source branches, immutable proof records, mathematical independence, and distinct evidence standards.

The single operative cursor is **UOI-INTAKE**, not the largest checkpoint number or the most recent research message. We retain both original-Weil and independent-arithmetic **alternative routes** to RH. They are not assumed equivalent, and the first route is not a prerequisite for the second. Explicit cross-projection evidence is optional unless a proposed route actually consumes it.

## Read-only repository inspection (November 21)

- `main` presents the completed Horizon-1 public package, with **3** workflow definitions, not the active post-Horizon source stack. Its README says RH-facing work remains open.
- Representative original numerical branch `research/nf768-original-indexzero-104-111-controlled-kernel` has **608** workflows and the repository-level `GOVERNANCE.md`; representative IV025 branch has **612**. Branch content and workflow triggers vary by lineage. Do **not** bulk-merge them into `main` or assume one trigger fix applies to all PR heads.
- Active research governance **already exists**: `research/obligations.json` schema v1 on the NF768 research branch, `docs/OBLIGATION_FIRST_PROGRESSION.md`, `docs/ACTIVE_FRONTIER.md`, `scripts/verify_obligation_manifest.py`, and `.github/workflows/obligation-governance.yml`. Its active mathematical cursor remains `W-ODD-NEG`. The old validator allows only `SI/SM/RC/LF/INTEGRATION` methods and expects exactly one active check set; it is **not** a complete NF/IV/CF/GA/CP/PI/RD controller. **Preserve it; overlay rather than overwrite.**
- The representative `critical-path-audit.yml` has path-scoped PR triggering but includes substantial research-specific replays. The NF750/NF753 numerical workflows use source-scoped pull-request triggers plus manual dispatch; their source and strict named axiom audits must not be weakened.
- The original Phase IV manifest preflight failure was traced to requiring generated `lake-manifest.json` before the `lake update` that generates it. The separate Actions incident involved high historical pull-request fan-out. Queue count reaching zero does **not** prove containment of either issue on every research branch.
- At read-only inspection, API `status=queued` returned 0 and latest visible CP034 workflow run succeeded. These volatile snapshots are not durable certificates or a complete Actions history.
- Canonical NF registry #761 reported **708/968** independently reconciled original HD/A gate instances. The count is *not* full physical matrix certification or global Weil positivity.
- The recent CP PR chain is stacked on previous research branches (e.g., CP034 base CP033), not on `main`; some older IV and NF PRs are likewise stacked. A governance-only change must not silently retarget or merge those branches.

## Source-of-truth hierarchy

1. **Exact source and immutable evidence:** Git commit/tree SHA, Lean declaration statement, original test/form and domain, emitted certificate hashes, independent named axiom audit, source-specific receipts. These determine *what is proved*.
2. **Historical canonical custodians:** issue #761 (NF and IV historical registry), #814 (IV operational), #826 (cross-projection IV/PI), #792 (PI), #841 (GA), #857–#860 (RD), #193 (global composition), and #834 (CI incident). Existing research branch receipts are preserved.
3. **UOI coordination overlay:** lists the missing theorem-shaped obligations, dependencies, responsible functions, acceptance conditions and the **next authorized planning action**. It must never silently upgrade a historical analytic or source-only report to Lean/kernel acceptance.
4. **Legacy local manifest:** `research/obligations.json` and its `W-ODD-NEG` cursor remain valid inside the post-Horizon original odd-operator program. UOI does not rename, delete or overwrite them. A subsequent reviewed compatibility migration may add pointers in both directions.

## Mathematical routes and nontrivial composition

**Original signed Weil route:** exact form/domain + source-attached Gamma/prime/pole assembly + boundary/neutral-mode control + arbitrary-support extension + full original-form positivity + independently checked applicable Weil criterion → RH. **Each arrow is a separate obligation.** Fixed support, selected Gram positivity, or 968 indexed gates do not independently close this route.

**Independent arithmetic route:** precise terminal implication (e.g. source-pinned prime-window or weighted-energy statement) + **independent proof** of its arithmetic premise → RH. RD001–RD003 provide source audits, analytical reductions, and a PNT-envelope negative control, not an independent proof of the missing arithmetic premise.

**Cross-projection interfaces:** PI/CP seek exact common-domain maps with source normalization, antilinearity, both poles, Gamma and signed prime phase. They are **not** mandatory for either route unless a particular proposed theorem consumes such a map. IV030's phase witnesses are falsifiers of graph-plus-mass-only reconstruction.

## Proposed planner state machine

Obligation record contains: ID, lead, contributors, kind, exact statement, exact acceptance predicate, source links, supporting evidence with classification, `depends_on` (AND), standing, proof receipt, and intended run class. The root terminal criterion contains **OR across complete alternative routes**, not a merged AND across all fronts.

- `open`: not discharged; can be **ready for review** if all mandatory prerequisites have accepted receipts.
- `conditional`: implication/lemma proven only under named unpaid hypotheses; not satisfied as a prerequisite.
- `blocked`: precise missing source/translation/CI prerequisite identified.
- `accepted`: exact theorem and scope separately reviewed with immutable source SHA, artifact SHA256, independent audit and scope validation. A green workflow on a proxy never suffices.
- `retired`: a failed/irrelevant method, with history retained. Never represent a retired attempt as a theorem refutation unless the claim was actually disproved.

Transitions require explicit provenance and reviewer/operator decision. The planner does not mutate the manifest or dispatch jobs; it only prints `READY/REVIEW ONLY` and `BLOCKED`. An accepted node's receipt must contain the original operator/domain/scope, trusted Lean/audit standing or independently assessed mathematical proof, and the exact applicable dependency transfer.

## Execution workflow after consolidation

```text
Source recovery (Git SHA, issue, exact theorem)
   -> reconcile obligations / source-domain guards
   -> cheap DAG and non-promotion validation
   -> choose highest-impact READY obligation by reviewed priority
   -> assign one lead function and explicit supporting functions
   -> local analytic / exact-rational work (no Actions)
   -> request source-specific CI only if needed
   -> CI safety gate + operator-reviewed one-job lease
   -> source-pinned manual workflow_dispatch on effective lineage
   -> strict Lean compiler + named axiom/source/artifact audits
   -> independent evidence reconciliation
   -> update UOI and historical registries, with no automatic promotion
   -> reassess critical path and release next READY obligation
```

At the beginning **only UOI-INTAKE and CI-FANOUT are review-ready**. Every other action is subordinated to the consolidation hold. The read-only prototype already detects cycles, duplicate IDs, unknown dependencies, false closed status and missing closure receipts (eight local tests passed). It is not an independent check of theorem content or live source SHAs.

### CI architecture: two stages, never mass conversion

**Stage A — ready immediately, no GitHub Actions changes:** create a governance-only coordination branch and issue. Maintain `research/unified/obligations.json` and a stdlib-only `scripts/uoi_validate.py` planner, plus tests. Use issue edits or source commits to record progress after review. No `.github/workflows` additions, no new PR, no heavy dispatch.

**Stage B — only after audited workflow lineage:** install **one small governance validator** as the required, non-skippable status check on the actual integration base (if branch rules support it). A later manual-only orchestrator can accept a registered obligation ID, pinned commit SHA and an allowlisted workflow identity; it must run the cheap validator first, check required checks and no active heavy lease, and refuse undeclared arbitrary commands. Never permit a generated issue body to execute shell commands. Heavy subject-specific Lean jobs remain in their respective original branches with source-scoped triggers. No automatic `issues`/`issue_comment`-to-heavy-workflow trigger. Do not turn all historical 600+ research YAML files into one giant workflow.

Operational release conditions for heavy jobs:

1. Re-open the **exact** head/base revision and verify bounded PR workflow fan-out (including all legacy NF workloads), no unexpected validation errors, and required checks satisfiable.
2. Verify current queue/running jobs, branch SHA, and source-bound manifest/setup ordering; do not assume the prior zero queue persists.
3. Verify immutable accepted evidence and all strict 35-declaration (or source-specific) axiom audits remain in place, with no new `sorry`/axioms or weakened original test.
4. Obtain one explicit operator-reviewed heavy lease (`max_concurrent_heavy_jobs=1`); run only the named source workflow at pinned SHA, no simultaneous unrelated submissions. Keep the lease until archive reconciliation or formally recorded failure.
5. Record actual run/job/artifact IDs and hashes before moving a node to `accepted`. A successful workflow does not close a mathematical claim outside its scope.

## First reconciliation batch (one week of work, not a promised time estimate)

**Gate 0 — this intake:** freeze new mathematical branches and heavy jobs; retain existing certified artifacts. Registry issue owns the active UOI cursor.

**Gate 1 — provenance inventory:** obtain one signed evidence handoff from each function: original theorem wording, domain, support, source SHA, which numerical/Lean jobs truly passed, what remains conditional, and an explicit `next_action`/falsifier. Recover CI status separately. The scope of CF's GitHub custodian remains to be identified; do not invent one.

**Gate 2 — graph arbitration:** identify the two or three most critical *currently open* mathematical arrows, rule out redundant investigative forks, and decide which supporting functions are required. Preserve a separate numerical certification lane; do not put NF gate counts above global composition automatically.

**Gate 3 — controlled pilot:** pick **one** genuinely ready obligation with a small, inexpensive, source-specific validation. Run the existing source workflow manually only if the repaired effective branch passes the CI gate, or otherwise continue read-only. Evaluate whether its result updates the shared obligation graph correctly.

**Gate 4 — operating cadence:** every subsequent `continue`/`UOI` recovers the graph, chooses the highest-impact ready obligation, delegates to relevant functions, reconciles evidence, and re-plans. `NF`/`IV`/etc. can still request a scoped function. Autonomous future execution is **not** enabled by the planning prototype; separate approved Actions/automation is needed for recurring work.

## Rollback and stop rules

- If lineage shows new unrestricted PR fan-out: **no heavy dispatch**; CI function repairs the effective base first.
- If graph dependencies are inconsistent: fail closed; do not select an obligation.
- If any purported accepted theorem lacks exact source, independent audit or applicable domain: downgrade its *coordination* standing to open pending review, without modifying its historical certificate.
- If a mathematical bound is established only on a proxy/fixed support: retain it as scoped evidence, not full theorem closure.
- If alternate RH routes cannot be composed: explicitly keep them separate. No claim of RH, global Weil positivity, or spectral equivalence.

## Initial run and test

```bash
python scripts/uoi_validate.py research/unified/obligations.json --plan
python -m unittest discover -s scripts -p 'test_uoi.py' -v
```

The accompanying **local planning prototype** is not yet committed or installed as a GitHub workflow. It is **planning-only**: it cannot use network tokens, dispatch Actions, merge branches or accept a proof. The commands above show the proposed repository paths after reviewed staging; in the local package run `python validate_uoi.py obligations.json --plan` and `python -m unittest -v test_uoi.py`. Review the exact active research lineage before any PR or CI installation.