# RPB108 LF70 — actual spectral L2 representatives

Extends `NeutralLogMetricSpectralL2.lean` with finite spectral L2 membership and convergence of actual `toLp` representatives of the finite-action Fourier transforms.

Membership follows from Fourier continuity of the integrable physical action and domination by the norm of the full weighted product. The representative convergence consumes LF69 seminorm convergence through Mathlib's exact Lp convergence equivalence. No desired convergence premise or new global definition.

The full weighted-product membership remains an explicit domain condition. This does not derive it from cap regularity or form energy. The theorem supplies actual spectral vectors, but does not yet equate their inverse Fourier transforms with the actual full-line time actions or attach the physical endpoint candidate.

Validation at submission: LF65 commit 89a9c738970d06f1a362824681ff9c78d155fcaa passed full-root run 38181762113. LF66 run 38183520443 passed targeted transport and was still building the complete root. LF69 run 38184106073 was queued. LF65 remains the latest confirmed full-root checkpoint. LF70 awaits cumulative remote Lean CI; no local Lean executable is available.

Next: inverse-Fourier/Plancherel transport of these representatives, with actual-action identification and the weighted-product domain obligation retained. No aperture positivity, F4 closure or RH claim.
