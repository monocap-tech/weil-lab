# RPB108 LF87 — fractional reciprocal-tail integrability

Proves integrability on ξ > 1 of (ξ^σ/ξ)^2 whenever σ < 1/2. The proof rewrites the quotient as ξ^(σ−1) and its square as ξ^(2σ−2), then applies the pinned Mathlib improper-integral criterion for an exponent below −1. The quarter-frequency specialization gives the concrete tail estimate needed by the LF86 route.

This is an actual integrable tail, with no integrability premise. It does not yet derive a Fourier decay bound or establish the shifted (e+|ξ|) fractional product on the full line. The shift comparison, reflected negative tail, bounded central interval and trial-specific boundary contributions remain to be assembled. No new global definitions.

Validation: LF84 commit 42c6a56d50d9b40e757b8214dec07ddd162aad10 remains the latest confirmed full-root code checkpoint. LF86 run 38201182309 had no job assigned at the initial check. Local structural checks and unfinished-declaration rejection pass for LF87; cumulative remote Lean validation is pending. No local Lean executable is available.

Next: assemble the shifted full-line fractional L2 criterion from a reciprocal decay bound, then derive that bound for intended zero extensions including endpoint jumps. No aperture positivity, F4 closure or RH claim.
