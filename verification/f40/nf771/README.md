# F40 / NF771 — original index-zero 128–135 source admission (draft)

**Source-only. NO LEAN PASS, NO new original HD/A gate acceptance.**

Accepted historical frontier is **740/968** after NF770, with original index-one HD/A 0–241 and index-zero HD/A 0–127. NF771 proposes exactly 8 more original index-zero positions per family (16 prospective HD/A gate instances), and 35 direct named axiom queries (32 column declarations and 3 shared).

This branch now contains the three **nonpromoting Python preflights**, a strict local post-compiler audit candidate, a narrowly path-filtered source-only PR workflow, and a separate **explicitly gated one-shot Lean workflow**. No compile marker file is committed; no heavy job has been dispatched. The PR's hosted source-only jobs perform source syntax/strict YAML checks, actual SHA-256 NF737 archive restoration and complete 242-column source authentication (run 45043518350), and live NF770 run/job/artifact metadata checks. The independently reconciled old NF770 archive remains historical #761 evidence. The separate runner can execute only on main with an exact source pin and deliberate manual confirmation or an exact one-shot marker/commit-message pair.

**True original-source admission** requires an isolated immutable research checkout at `a431f903254000bb5ad8edbc276ccc8599da98f5`, plus the genuine NF737 complete 242-column source archive. Overlay the two `nf771_original_indexzero_*.py` drivers into its `scripts/` directory and run the `nf771_original_indexzero_128_135_source_preflight.py` candidate. That script calls the original NF737 full-bank source verifier and constructs the exact 35-name axiom query text; its success is still **source preparation only**. All 242 original generated columns are artifact-restored, not added to main.

**Before any NF771 gate PROMOTION**, separately verify the exact immutable NF737 original SHA/source bank, actual NF681.Common → NF703Cache.Frontier → NF681.Col128–135 → NF704Frontier.Common import DAG, accepted NF728/NF729 source and `.olean` cache, authentic NF770 740 predecessor artifact, eight direct unique new Col128–135 `.olean` objects and compiler exit-zero receipts, all 35 strict `#print axioms` results with no `sorryAx`, and an independently checked ZIP/source hash custody receipt in #761. No new acceptance may be inferred from this PR alone.

**Prospective result only:** 740 + 16 = 756/968; 212 would remain. F41 complete 242×242 physical matrix, F42 literal signed Weil form, unrestricted positivity and RH remain open. See master ledger #898.

## New kernel candidate lane (not an acceptance)

The staged `.github/workflows/f40-nf771-single-lane.yml` is intentionally not a PR compiler. It permits only exact original-source `a431f903254000bb5ad8edbc276ccc8599da98f5` and exact NF771 driver-overlay SHA; it fails closed when other Actions runs are active. An authorized run restores original NF737 242-column artifact **only after original ZIP byte SHA-256 validation**, verifies old NF728 source and accepted NF729 Lean object cache, orders NF681.Common before NF703Cache.Frontier, compiles eight genuine original Col128–Col135 `.olean` files, and prints 35 exact named Lean axiom reports. `nf771_original_indexzero_128_135_kernel_audit.py` requires those source-bound objects, timing receipts, 35 standard-only names, true predecessor 740 data and import-order hashes. Even a fully green kernel job remains an **unreconciled local audit** until its newly produced archive bytes and metadata are independently checked and inserted into #761.

CI release requires the full source-only hosted YAML, predecessor and PR authorization checks. An isolated main-branch marker is **not** part of this PR and shall not be added before deliberate release.
