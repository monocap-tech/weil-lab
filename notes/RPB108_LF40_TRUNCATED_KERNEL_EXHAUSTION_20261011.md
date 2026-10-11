# RPB108 — LF40: truncated kernel exhaustion

## Submitted coverage

Add NeutralLogMetricTruncatedLimit with two convergence theorems. For any natural-number-indexed increasing family of finite closed time intervals whose union is exactly Ioi 0, the actual truncated jump density tends to the actual full jump density at every positive spatial radius. A second theorem handles every nonzero signed spatial displacement by absolute-distance symmetry.

The proof uses the already established convergence of the defining full time integral and Mathlib's tendsto_setIntegral_of_monotone, then multiplication by two. It does not assume the desired convergence and does not use a totalized divergent integral. Interval monotonicity and exact coverage remain explicit caller obligations. No new definitions are introduced. The root and targeted CI chain import the new module.

## Primary source

Mathlib/MeasureTheory/Integral/Bochner/Set.lean at pinned revision 5ed2965256430c3649e86755f9576b54eca72435: tendsto_setIntegral_of_monotone requires measurable sets, monotonicity, and integrability on their union, and returns convergence to the integral on that union.

## Validation boundary

At preparation, LF39 commit d3e225fc27dd5e176f99b3744f820d8710930345, run 38148324601 job 114496270980, was still in the targeted build. No outcome is inferred. LF37 and LF38 compiled TrialJump; LF28 remains the latest successful full-root checkpoint. LF40 and downstream cumulative coverage await CI; no local Lean executable is available.

## Remaining obligations

Construct and verify a concrete exhausting interval sequence. Establish pointwise convergence of cancelled trial jumps including the diagonal, then pass the spatial integral to the limit using the integrable LF34/LF29 majorant. Physical weak attachment, L2 convergence, and spectral source identification remain open. No new aperture positivity, F4 closure, or RH claim.
