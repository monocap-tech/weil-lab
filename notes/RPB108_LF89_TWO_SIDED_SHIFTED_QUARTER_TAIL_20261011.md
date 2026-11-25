# RPB108 LF89 — two-sided shifted quarter tail

Combines positive and negative shifted quarter-frequency reciprocal tails in the actual absolute-frequency form ((e+|ξ|)^(1/4)/|ξ|)^2. The proof lifts positive-tail integrability to an indicator on the whole line, reflects it using integrable.comp_neg, recovers negative-tail integrability, normalizes absolute values on each tail and combines the restrictions over ξ < −1 or ξ > 1.

The resulting two-sided tail has derived square-integrability. Central-interval control and trial-specific reciprocal Fourier decay remain open. No new global definitions, desired domain-membership premise or suppression of exterior action.

Validation: LF88 run 38202113227 had no job assigned at this checkpoint. Local structural checks and unfinished-declaration rejection pass for LF89; cumulative remote Lean validation is pending. LF84 commit 42c6a56d50d9b40e757b8214dec07ddd162aad10 remains the latest confirmed full-root code checkpoint. No local Lean executable is available.

Next: assemble central control with the two-sided tail to prove the full shifted fractional L2 criterion from reciprocal decay, then derive that decay including endpoint contributions. No aperture positivity, F4 closure or RH claim.
