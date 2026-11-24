# F08-027 — first native L² frequency scaling bridge

**Compiler candidate, narrow source status until genuine Lean and separate custody.**

The exact frozen original IV023 `RealComplexL2` carrier is used. Unlike an unjustified same-volume composition, this defines the genuine pushforward-frequency measure `Measure.map (fun ξ => λ * ξ) volume`, proves scaling is measure-preserving *to that measure*, proves its real one-dimensional Haar Jacobian for `λ ≠ 0`, then constructs Mathlib's actual `Lp.compMeasurePreservingₗᵢ` as a complex linear isometry between **two distinct native** `Lp ℂ 2` spaces. It also supplies the exact a.e.-representative identity under ordinary volume.

Four strict named axiom queries: `f08_027_scale_measurePreserving`, `f08_027_scaledFrequencyMeasure_jacobian`, `f08_027_nativeFrequencyPullback_norm`, and `f08_027_nativeFrequencyPullback_ae`.

**Not proved yet:** the same-original-volume `U_λ k(ξ)=sqrt(λ)k(λξ)` isometry, its strong continuity at 1, physical Fourier scaling with original `-2π` convention, weighted `K(D_λf)=m_λ U_λ(Kf)`, strict physical support, dense interior smooth form core, exact original signed Weil source↔native mixed pairing, F42, or RH.

The missing bridge between these two measure spaces and same Lebesgue volume will require accounting for `Measure.map (λ ·) volume = |λ|^{-1} • volume`, with the correct rescaling of `L²` norm. Do not silently apply `Lp.compMeasurePreservingₗᵢ` with original Lebesgue volume as both measures.

Frozen source `614ba879f7389fdb620c474adaee273b00eac71c`, original `NeutralCanonicalFormDomain.lean` blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`, Lean v4.34.0. Parent [Issue #932](https://github.com/monocap-tech/weil-lab/issues/932), master ledger #898.
