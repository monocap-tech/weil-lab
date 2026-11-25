# RPB108 LF82 — real-power spectral norm repair

Repairs the remaining spectral convergence error from LF81 run 38194180347. The eLpNorm integral formula uses an ENNReal real exponent, not a natural-number power. After converting the complex extended norm to ofReal of its norm, apply ENNReal.ofReal_rpow_of_nonneg in the forward direction with explicit complex difference and real exponent 2, then Real.rpow_two. This directly identifies the integrand with ofReal of the squared real norm.

No theorem statements, hypotheses, definitions or mathematical scope change. The repair is grounded in the pinned Mathlib Pow/NNReal.lean declaration. LF81's attempted multiplicative conversion did not match the real-power expression.

Validation: LF81 built NeutralLogMetricTimeActionBounds successfully and failed only in NeutralLogMetricSpectralL2; the attachment module remained blocked. Local structural and unfinished-declaration checks pass. LF82 awaits cumulative remote Lean validation. LF66 commit 0ee0510b0980a6ba24b574bb5a8bc7d0a2b701da remains the latest confirmed full-root success. No local Lean executable is available.

Next: resolve cumulative spectral/attachment/root validation before extending to cap-Lipschitz trials with endpoint jumps. No aperture positivity, F4 closure or RH claim.
