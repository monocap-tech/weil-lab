# RPB108 LF67 — actual cutoff pointwise spectral limit

Adds `NeutralLogMetricTimeActionLimit.lean`, registered in targeted CI and the root library.

The module proves integrability of the damped finite coefficient term, cancels the two finite Laplace coefficient integrals, and derives pointwise convergence of Fourier transforms of the actual full-line cutoff actions to the trial transform times the existing logarithmicFourierWeight. The concrete cutoffs are [1/(n+1), n+1], and all frequencies including zero are covered. A specialization applies to cap-bounded measurable trials through their actual zero extensions.

This uses LF66's actual finite-action Fourier identity and LF60's proved coefficient limit; neither is assumed as a premise. Integral subtraction has explicit integrability witnesses. No new global definitions or spectral convergence assumptions.

Validation at submission: LF63 commit a1310edf16d67bcfb23169db82b03c1a4cf13fa3 passed full-root run 38181384412. LF65 run 38181762113 passed targeted checks and remained in the full-root build. LF66 run 38183520443 was queued. LF63 remains the latest confirmed full-root checkpoint. LF67 awaits cumulative remote Lean CI; no local Lean executable is available.

The new result is pointwise spectral convergence of actual full-line actions. It does not establish convergence in spectral L2, spectral operator-domain membership, or identify the cap-supported endpoint source with the full spectral source. These remain separate obligations, with exterior action retained. No aperture positivity, F4 closure or RH claim.
