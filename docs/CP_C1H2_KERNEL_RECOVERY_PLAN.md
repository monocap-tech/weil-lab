# Weil-Lab — CP-C1(H2) original frozen correlation integrals

**2026-11-22. Custody:** local source candidate and strict verifier; **not yet a Lean compiler result**.

## Newly verified upstream kernel state

At source commit `cd174c693a5153b55167cf8ecfa0a06444291524`, the original Lean 4.34 CI job 45084686441 genuinely compiled the frozen CP-C1(F/G) source and strict standard axiom reports; its upstream CP-C1(B–E) compiler receipt also passed. CP-C1(B–E) independently passed in run 45083293301. The source anchors still distinguish the complete zeta divisor from an independently constructed spectral target.

Current original pointwise CP-C1(H1) test: run 45090246035 at SHA `3880bab7290fb4e644fff439246f9f7e6893df3f`. Its preflight and pinned Lean installation passed, but at report generation the rebuild/Lean compiler step was still **in progress**, and no H1 axiom receipt was available.

## H2 new source

The file `CP_C1H2_OriginalFrozenCorrelationIntegrals.lean` separates the remaining **12** named genuine-source theorem candidates from the earlier uncompiled 14-theorem H draft and **imports** H1's two pointwise theorems instead of duplicating them. Source-only inventory passed; there are 16 axiom print requests (four existing dependencies + twelve new names).

The expected mathematical chain, each item requiring direct Lean elaboration, is:

1. Original NF600 collar-support for the phase family `L + v • R`, using the exact CP001 functions at outer half-width `1/2000`.
2. Both authentic ±log(9) physical correlation integrals: + shift retains `v`, negative shift retains `conj v`.
3. Real-valued original flat bump inputs, Lebesgue translation invariance of the overlap, and conversion from complex integral to the exact physical real scalar `neutralCPC1HOverlapReal`.
4. Actual two-point response of `neutralNF600Prime`, reduced by the original `neutralNF600Prime_single` theorem to the genuine von Mangoldt `n=9` term, with no H1 pointwise or G physical correlation hypotheses remaining.

This is solely the **prime sector**; the full Weil form includes poles and Gamma. Independent nine-reading external spectral certification, the interval enclosure **inside Lean**, universal Weil positivity, and RH remain open.

## Gate discipline

- `cpc1h2_original_integral_kernel_gate.py` binds unchanged H1 / F/G / E upstream Git blobs, requires exactly the names and axiom prints expected, runs seven negative transcript controls, and checks H1's actual `.olean` and SHA-256 bound genuine kernel receipt before accepting H2.
- `cpc1h2_original_integral_local_kernel_lane.sh` sets up a one-leaf B→G→H1→H2 native build and all strict axiom audits under pinned Lean v4.34.0.
- `cpc1h2-original-integrals-one-shot-kernel.yml` is ready for an isolated workflow launch **only after** H1's genuine compiler outcome has been inspected and any H1 source repairs have been reconciled with the H1 upstream pin.

**Do not submit H2 or claim the mathematical premises are kernel-discharged until H1 genuinely passes and H2 itself is compiled and axiom-audited.**
