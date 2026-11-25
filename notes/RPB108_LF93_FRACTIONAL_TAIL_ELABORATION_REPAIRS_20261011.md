# RPB108 LF93 — fractional-tail elaboration repairs

Repairs LF89 run 38202260080, job 114658077661, diagnostics and applies the same explicit real-power annotation to the later LF90 fractional-product occurrences.

Repairs: compute fractional powers in ℝ before casting to ℂ; reduce the power-tail congruence goal to pointwise expressions before rewriting; provide measurable squared-quotient witness explicitly before AEStronglyMeasurable conversion; expose the positive-tail membership as 1 < ξ for the shift inequality; unfold indicator conditionals in the reflection proof. No mathematical hypotheses or desired source identities are added. Real-domain annotations clarify the intended theorem statements rather than introducing complex powers.

Validation: LF89 failed on these diagnostics. LF92 run 38203177667 was running targeted checks and LF91 had no job assigned. Local structural checks and unfinished-declaration rejection pass for LF93; cumulative remote Lean validation is pending. LF84 commit 42c6a56d50d9b40e757b8214dec07ddd162aad10 remains the latest confirmed full-root code checkpoint. No local Lean executable is available.

Next: resolve cumulative fractional-tail and domain validation, then derive the reciprocal phase-integral norm bound and attach it to actual zero-extension Fourier integrals. No aperture positivity, F4 closure or RH claim.
