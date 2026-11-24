# F08-029 — source-native L² pushforward representation and exact measure-scaling norm

**Uncompiled candidate until original pinned Lean 4.34.0 and distinct archive custody PASS.**

Stacked on F08-027 [PR #1006](https://github.com/monocap-tech/weil-lab/pull/1006), not yet accepted. This module uses the *actual original* `RealComplexL2`, F08-027's pushforward measure and Jacobian, and Mathlib `MemLp.smul_measure`, `MemLp.toLp`, `Lp.norm_toLp`, `eLpNorm_smul_measure_of_ne_zero`. Four new named theorem targets:
1. Original complex L² vector is MemLp under the genuine scaled measure;
2. Its Lp equivalence-class construction has the literal a.e. representative;
3. Exact extended L² norm Jacobian identity;
4. The corresponding native Lp norm identity.

No claim that unchanged `k` has the *same* numerical L² norm under different measures. The eventual same-volume unitary requires inserting a compensating sqrt scale before F08-027's native L² pullback, and then proving strong continuity.

Frozen original IV023 source `614ba879f7389fdb620c474adaee273b00eac71c`; actual source `Morphology/NeutralCanonicalFormDomain.lean` blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`; immediate F08-027 predecessor source blob `eecfe2a849fa79aa13810ede85e9ba625eba7777`. The candidate must compile in frozen original root with real Lean objects and four standard-only named axiom reports; independent archive auditor remains required.

The following are NOT proved: fully same-volume unitary `Uλ`, its strong L² continuity, physical `-2π` Fourier scaling, support transfer, weighted log form core, source-sign exact Weil pairing, F42, RH.
