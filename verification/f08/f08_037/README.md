# F08-037 — compactly supported Schwartz functions dense in original complex L²

**UNCOMPILED until native frozen original IV023 Lean 4.34.0 produces SUCCESS and exactly one standard-only axiom report.**

The proposed theorem proves that the image of the set `{g : 𝓢(ℝ,ℂ) | HasCompactSupport (g : ℝ → ℂ)}` under Mathlib's genuine continuous `SchwartzMap.toLpCLM ℝ ℂ 2 volume` is dense in the actual original `RealComplexL2`. It is not a generic abstract replacement. The exact **frozen Mathlib v4.34.0** contains `MeasureTheory.Lp.dense_hasCompactSupport_contDiff` (genuinely smooth compactly supported representatives dense in native `Lp`) and `HasCompactSupport.toSchwartzMap` (each such representative is a Schwartz function). Directly converting those dense source representatives proves the same original `toLpCLM` image density goal. The later `SchwartzMap.dense_hasCompactSupport` module is not available in the frozen environment.

This gives the **dense compact-core part** of F08's next strong-L²-continuity proof. On each compactly supported Schwartz (g), pointwise continuity of `√λ g(λξ)` plus a common bounded support interval for λ near 1 gives an (L²)-integrable dominating function. The actual original normalized dilation's a.e. representative and native `LinearIsometry` from independently accepted F08-030/033 and still-pending F08-035 can then combine with this density to prove strong (L²) convergence.

**Crucial separation:** compact support here is **frequency-side Schwartz support**, not compact physical support of inverse Fourier functions; this result does not itself prove original fixed physical radius `C_c^∞((-a,a))` density in `neutralCanonicalLogFormDomain a`, weighted Fourier continuity, complete literal original signed Weil source pairing identity, F42 positivity or RH. No strong continuity statement is asserted in this file.

Frozen original research IV023 `614ba879f7389fdb620c474adaee273b00eac71c`, canonical source blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`, native `leanprover/lean4:v4.34.0`. Parent #932 and ledger #898.

First original Lean run [45536526411](https://github.com/monocap-tech/weil-lab/actions/runs/45536526411) failed at the unavailable `Mathlib.Analysis.Distribution.SchwartzSpace.CompactSupport` import; the current source uses only actual original v4.34.0 declarations, retaining the same theorem statement and no extra axioms. Reverification is required.
