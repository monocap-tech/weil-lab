# RPB108 LF71 — inverse-Fourier vector and pairing limit

Extends `NeutralLogMetricSpectralL2.lean` with inverse-Fourier transport of the LF70 actual spectral representative limit and physical inner-product convergence against every fixed L2 test vector.

Mathlib's continuous inverse Fourier transform on L2 transports the vector limit. Continuity of the complex inner product then transports physical pairings, with source in the first argument. Both consume the existing representative convergence; no new definitions or desired convergence premises.

The full weighted-product L2 domain condition remains explicit. The inverse-transformed vectors are not yet equated with the actual time-action functions or the cap-supported endpoint candidate. Those require a separate representative/Plancherel attachment, retaining exterior action.

Validation at submission: LF65 commit 89a9c738970d06f1a362824681ff9c78d155fcaa is the latest confirmed full-root success. LF66 run 38183520443 passed targeted checks and remained in the root build. LF70 run 38184486427 was queued. LF71 awaits cumulative remote Lean CI; no local Lean executable is available.

Remaining: actual-action identification, proof of the intended trials' full weighted-product domain membership, and compressed/full-source attachment. No aperture positivity, F4 closure or RH claim.
