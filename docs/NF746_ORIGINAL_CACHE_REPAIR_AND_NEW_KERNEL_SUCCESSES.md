# NF746 — New genuine original numerical Lean successes and NF743 cache recovery

Canonical Phase III NF iteration, stacked on [NF745 PR #775](https://github.com/monocap-tech/weil-lab/pull/775). Phase IV is separately tracked under IV###. Do not count source generation, synthetic tests, or a cached object by itself as numerical kernel acceptance.

## 1. Two actual independent numerical successes recovered

Both the NF737 and NF739 genuine original numerical jobs are completed **SUCCESS**, including successful strict 35-name original theorem/axiom verification, and both have unexpired source-specific numerical audit artifacts.

| Genuine original index-zero numerical gate | Run | Successful numerical job | Numerical audit artifact | Artifact ZIP SHA256 |
| --- | ---: | ---: | ---: | --- |
| NF737 original HD(0,32..39), A(32..39,0) | 44791346863 | 136514439734 | 14672703515 | bd3771cf2b939e76bc4dea956f4547c3efb4330f77a318db46cf71b78004e89a |
| NF739 original HD(0,40..47), A(40..47,0) | 44795709843 | 136528518645 | 14673191666 | 95da4ce94c83bc021b7361fdf261699a74f45a65a507a505a28567dbc3087258 |

Original accepted baseline: 242 HD + 242 A original index-one universal gates = 484; original index-zero positions 0..23 = 24 HD + 24 A = 48. The newly successful NF737 and NF739 jobs add 8 HD + 8 A = 16 apiece. Consequently the independently supported cumulative count is **484 + 48 + 16 + 16 = 564 distinct genuine original HD/A gate instances**, with actual accepted index-zero positions 0..23 and 32..47. NF734 24..31 remains excluded pending its own independent proof receipt. Source-only NF737/NF739 successes were not mistakenly counted as new numerical proof; these are the separate genuine original numerical jobs.

## 2. Actual NF743 failure and mathematical distinction

NF743 [run 44813177950](https://github.com/monocap-tech/weil-lab/actions/runs/44813177950), job 136554678956, completed **FAILURE** in the historical cache comparison step, after successful source preflight and Lean/Mathlib installation. Actual exception:

    AssertionError: ('Missing required genuine original source family', ('NF702Inputs', 'NF703Cache', 'NF681'))

This reports that at least one of those three families is absent from the historical archive. It does NOT establish which family is missing or whether any overlapping source file bytes differ. NF728's original index-one proof used NF700 packed local blocks; NF737's separate original index-zero construction authenticates the NF681 local bank. There is no mathematical reason to demand that a historical archive contain every later local source family merely to reuse earlier accepted NF702/NF703 cache modules.

The NF743 error was before numerical gate 56..63 Lean compilation. It proves neither failure nor acceptance of any original gate equation.

## 3. Source-identity repair, preserving the trusted boundary

The NF743 source verifier now checks **exactly the two source families underlying the reused NF729 accepted cache**, NF702Inputs and NF703Cache. It requires both complete same-name source sets and exact SHA256 of every cache source byte, the two original Data source anchors and Frontier source, the immutable NF728 accepted ZIP SHA, and exact accepted NF729 numerical kernel-object ZIP SHA. Missing cache families, new/missing cache files, or a single changed cache byte fail closed.

The actual newer NF737 NF681 source is treated separately: the prior NF737 full 242-module source verification still runs first; the repair explicitly requires all 242 local original Col000..Col241 source files. If NF728 does contain overlapping NF681 files, each must also have exactly identical bytes. The verifier does not assert NF681 complete historical equality or infer NF681 Lean acceptance from the earlier cached center proof.

The NF743 gate audit now requires explicit receipt scope fields. The generated certificate flags cache-only comparison versus the independently authenticated NF737 local source; it cannot silently upgrade a cache match to an original 56..63 theorem.

## 4. New tests and execution handoff

NF746 adds eight synthetic fail-closed source-scope tests: NF681 absent from historical archive, rootless uploaded-folder layout, cache byte mismatch, extra contemporary cache file, missing required archival cache source, missing one of 242 contemporary NF681 local sources, mismatched optional NF681 overlap, and identical optional overlap. All eight are purely Python synthetic tests. They do not prove a real historical archive identity or a Lean proposition.

New short workflow: .github/workflows/nf746-original-cache-source-scope-selftest.yml. Modifying the original NF743 source verifier and gate auditor also makes the existing full genuine NF743 numerical Lean workflow eligible to run on this PR. Acceptance of NF743 56..63 remains **PENDING** until that job independently succeeds and its final strict 35-name audit artifact exists. If actual required cache source bytes differ, the revised check must fail; no bypass is permitted.

NF745's live acceptance ledger is separately queued. Its historical baseline of 532 should gain 32 actual gates only if its own live API snapshot authenticates both just-observed successful jobs, strict steps and digests.

## 5. Open work

NF734 indexzero 24..31; NF742 48..55; NF743 56..63; remaining 64..241; other global matrix rows and columns; original vector and full-payment systems; full original physical numerical enclosure; all-support mixed signed Weil positivity; global Weil positivity; RH.

**No global Weil positivity or RH theorem is claimed.**
