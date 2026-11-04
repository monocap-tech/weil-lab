# NF454 — Verified active frontier supplement (2026-11-03)

**NF454 status: ACCEPTED algebraic gate reduction, not an NF404 proof.**

Original six full signed cell intervals, NF410 principal power, NF453 last-two-cell principal energies, and the exact NF404 centered cap are source-pinned in `scripts/local_replay/verify_nf454_gate.py`. The verifier's strict rational tests passed on [Actions run #41753094792](https://github.com/monocap-tech/weil-lab/actions/runs/41753094792), job #126322680439, evidence artifact #13286072934.

The unchanged physical odd response satisfies `Efull=A+2E78`, with `A=Ep+sum(D1..D6)-2(Ep7+Ep8)` and original nonnegative positive-side `E78=integral_(J7 union J8)(p+z)^2`. Exact original outward intervals prove `5.7e-22<A<5.8e-22` and the source-exact NF404 threshold `2.59e-22<(C-A)/2<2.62e-22`. Therefore **E78 <= 2.59e-22 guarantees this original NF404 sufficient cap**; **E78 >= 2.62e-22 rejects only this sufficient cap**, not Weil positivity or RH. Between them, the outcome is unresolved.

**Current open:** E78 itself is not certified; whole J7/D7, J8/D8, original NF404 centered scalar, exterior J242, W-ODD-NEG, even/whole form, operator domain and RH remain OPEN. This supplants no historical source. The older NF453 pending header was already superseded by its accepted source-CI supplement.

**Next NF455:** construct one full source-correlated, endpoint-aware, original J7+J8 physical square-energy bound. [NF454 note](../notes/provisional/NF454_ORIGINAL_TWO_CELL_SQUARE_ENERGY_GATE_20261103.md) and [custody](../notes/data/provisional/NF454_original_two_cell_square_gate_custody.json). Draft stacked PR #481; no main merge.
