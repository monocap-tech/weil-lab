# F08-035 — genuine native L² complex-linear isometry and approximation bound

**Uncompiled native source candidate.** This gate advances from F08-033's genuine original-source norm preservation to a `RealComplexL2 →ₗᵢ[ℂ] RealComplexL2` object, with proof of linearity on a.e. equivalence classes (NOT raw pointwise substitution).

A separate lemma transfers a.e. equality under original Lebesgue measure through the correct nonzero `λξ` pushforward measure. The additivity and complex homogeneity proofs then use the certified F08-030 actual normalized source operator `Uλk(ξ)=√|λ| k(λξ)`, F08-033 norm preservation, and exact measure transfer.

The final estimate is the standard dense-approximation reduction
`‖Uλ k - k‖ ≤ 2 ‖k - g‖ + ‖Uλ g - g‖`.
**It does not yet prove** `‖Uλ g-g‖→0` on the Schwartz dense class, the full strong `L²` continuity result, original paper-convention Fourier scaling, the weighted logarithmic supported core, arbitrary compact-smooth signed Weil identity, global positivity or RH. Strict original frozen IV023 Lean kernel compile + four exact named standard-only axiom reports and separate original ZIP custody are required before acceptance.

Predecessors original-source Git blobs: F08-027 `eecfe2a849fa79aa13810ede85e9ba625eba7777`; F08-029 `4da65f9b9df7cae6ea30a4a7f25d3e6c1606c294`; F08-030 `5c260b69f464f5793e095f9b5448c90f7984617f`; F08-033 `8b4055c065ab7987a01bf55143908d8cd77f0f23`. Canonical original source blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`, frozen commit `614ba879f7389fdb620c474adaee273b00eac71c`, Lean 4.34.0. Parent #932, ledger #898.
