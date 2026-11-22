# CP-C1(B/C/D) — single local original-source compiler lane

The original IV009 Lean 4.34 proof has passed compiler and strict standard-axiom audit in [run 44850887402](https://github.com/monocap-tech/weil-lab/actions/runs/44850887402). First CP-C1(B) genuine run [45060782018](https://github.com/monocap-tech/weil-lab/actions/runs/45060782018) FAILED with two source errors; their repairs are committed but not yet compiler verified. CP-C1(C) and CP-C1(D) remain source candidates.

Run the following **in the genuine full Weil-Lab repository checkout on the CP branch, with elan/Lake installed**:

```bash
bash scripts/cpc1b_c1c_c1d_local_kernel_lane.sh
```

This script does **not** open a PR, dispatch GitHub Actions, or touch the NF/IV source lines. It first enforces the source theorem inventories and pinned original IV008/IV009 Git blobs. It initializes Lake, builds B, then C, then D, runs direct `lake env lean` for each eight/five/seven axiom-print inventory, verifies every axiom is one of `propext`, `Classical.choice`, `Quot.sound`, requires a genuine nonempty `.olean` for each and emits SHA-256-bound receipts. A failed build stops immediately, so no downstream proof can borrow an invalid `sorryAx` declaration.

**Current status:** RUNNER AND RECEIPT VERIFIER SOURCE ONLY. This script has not been run in a valid complete Lean 4.34 checkout here; do not interpret preparation as Lean acceptance. The independent target's nine real probe readings, exact CP001 frozen flat bumps, and complete external spectral zero roster are not certified by this lane.
