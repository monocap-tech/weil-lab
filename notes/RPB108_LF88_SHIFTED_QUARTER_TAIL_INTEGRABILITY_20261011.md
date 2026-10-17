# RPB108 LF88 — shifted quarter-tail integrability

Proves integrability on ξ > 1 of ((e+ξ)^(1/4)/ξ)^2. For ξ > 1, e+ξ ≤ (e+1)ξ, hence the shifted fractional reciprocal tail is bounded by (e+1)^(1/4) times the unshifted tail. Its square is dominated by the constant-scaled integrable square proved in LF87.

This addresses the positive-tail shift in LF86's actual (e+|ξ|) fractional-domain criterion. Negative-tail reflection, central-interval control and the trial-specific Fourier decay remain to be assembled. No new global definitions or domain-membership assumptions.

Validation: LF86 run 38201182309 and LF87 run 38201621734 had no jobs assigned at this checkpoint. Local structural checks and unfinished-declaration rejection pass for LF88; cumulative remote Lean validation is pending. LF84 commit 42c6a56d50d9b40e757b8214dec07ddd162aad10 remains the latest confirmed full-root code checkpoint. No local Lean executable is available.

Next: combine positive and negative tails with central control to prove shifted fractional L2 membership from a reciprocal Fourier decay bound, then derive that bound including endpoint terms. No aperture positivity, F4 closure or RH claim.
