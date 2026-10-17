# LF94 — reciprocal-decay elaboration repairs

LF92 CI (run 38203177667, job 114661246475) exposed additional errors beyond LF93's fractional-tail repairs. This checkpoint repairs central shifted-power monotonicity with an explicitly ordered real inequality, unfolds positive/negative tail membership before arithmetic automation, and normalizes the real-to-complex continuous linear map in the Fourier-phase derivative.

The exact integration-by-parts identity still retains both endpoint terms. No new mathematical theorem or boundary assumption is added here. The next mathematical step remains its endpoint-retaining reciprocal norm estimate and attachment to the cap trial Fourier integral.

Validation: local structural and unfinished-declaration scans pass. Lean is unavailable locally; cumulative CI is required. LF84 (42c6a56d50d9b40e757b8214dec07ddd162aad10; run 38196728241) remains the latest successful full-root validation. LF93 CI was still running when this checkpoint was prepared. No aperture positivity, F4 closure, or RH result is asserted.
