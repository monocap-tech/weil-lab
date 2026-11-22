# Formalization F40 — NF770 source-only 120–127 preparation

**Status: NOT RUN / NOT KERNEL ACCEPTED.** This is a nonpromoting, source-only preparation handoff for F40 after independently reconciled NF769 (724/968).

Frozen original-source parent: `a431f903254000bb5ad8edbc276ccc8599da98f5`, with exactly NF769's accepted source lineage, complete NF737 242-column bank, NF702/NF703 cache and NF681 import order. Target `NF704Frontier.Col120–Col127`: eight original columns, sixteen HD/A index-zero gate instances; 32 column declaration axiom queries plus three shared = **35 direct named axioms**.

Files:
- `nf770_original_prior_724_custody.py` calls immutable NF769 predecessor verification and checks the actual NF769 GitHub run/artifact identity; no new gate claimed.
- `nf770_original_indexzero_import_order_guard.py` validates the actual source import DAG and compiled prerequisite objects.
- `nf770_original_indexzero_120_127_cached_kernel.py` prepares strict source binding and 35-axiom queries; only its **audit** stage may write a success record, contingent upon genuine compiled columns and accepted-cache and prior receipts.

To execute, overlay these scripts into `scripts/` of an isolated checkout of immutable original source `a431f903254000bb5ad8edbc276ccc8599da98f5`. Use a **single source-pinned, manually authorized** Lean/Mathlib v4.34 lane, `lake update` before any manifest validation, restore original NF737 source and NF728/NF729 accepted caches, compile actual NF681 prerequisites and each of Col120–Col127, run all 35 `#print axioms`, and archive actual Lean logs/objects/source receipts. Independently validate the artifact bytes and GitHub job status before any promotion.

Never amend the historical NF769 certificate or mark 740/968 accepted from this draft. F41 complete physical 242×242 source enclosure and F42 literal signed Weil domain attachment remain independent **open** obligations.

Operational: a **draft** single-lane workflow is staged at `.github/workflows/f40-nf770-single-lane.yml`. It includes a PR/manual source-only audit, a manually confirmed 120–127 Lean execution, and a one-shot **main-branch push marker** that also requires one exact commit message and immutable marker contents. The heavy job is pinned to accepted NF769 source, fail-closed against other active Actions runs, and uses the IV018/UOI030 shared concurrency group. It is **not registered on main, not dispatched, and not compiler-tested**. Source-only hosted preflight run 44995444574 passed against the earlier draft SHA, verifying Python syntax and live historical 724-gate custody; subsequent draft improvements remain subject to new preflight. No source push to historical 600-workflow branches and no new numerical acceptance. F40 remains the formalization priority; coordinate single-heavy-run authorization with current IV/UOI activity. See [#898](https://github.com/monocap-tech/weil-lab/issues/898) and [#761](https://github.com/monocap-tech/weil-lab/issues/761).
