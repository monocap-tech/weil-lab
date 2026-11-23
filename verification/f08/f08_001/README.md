# F08-001 — source-specific log-weight dilation inequality

Mathematical lead: F08 source/domain bridge, IV/CF supported core. [Analytic density result and original source bindings — Issue #932](https://github.com/monocap-tech/weil-lab/issues/932).

Two new Lean **proof candidates**, not yet kernel-certified, bound the exact original function `logarithmicFourierWeight ξ = log(e+|ξ|)` under inward dilation for `1/2 ≤ λ ≤ 1`. This is only the first scalar step toward a dense compact-Schwartz core in the actual `NeutralLogHilbertCarrier a`; it does not prove strong continuity of the dilation action, mollifier convergence, source↔native form identity, arbitrary-support positivity, or RH.

The single PR path-scoped workflow checks the genuine mathematical file at fixed IV023 revision `614ba879f7389fdb620c474adaee273b00eac71c`, Git blob `ae932d4f3f7e4d6d06dbd778a5708927172238dc`, then initializes the pinned Lean v4.34.0 Lake environment and attempts two genuine declarations, followed by two exact ordinary-only `#print axioms` checks. A failed source/preflight or compiler stage is not a mathematical counterexample.

No existing original mathematical file, numeric witness, source-domain definition, Lean axiom, or certificate is modified.
