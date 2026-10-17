# LF95 — endpoint-retaining phase norm bound

Adds `neutralLogMetricFourierPhase_interval_norm_le` for an ordered finite interval, a nonzero frequency, differentiable trial and interval-integrable derivative. The finite phase integral is bounded by the sum of both endpoint norms and the derivative L1 mass, divided by 2π|ξ|. The proof consumes LF92 integration by parts, proves unit phase norm and the exact phase coefficient norm, and applies the integral triangle inequality. Endpoint vanishing is not assumed.

This remains a differentiable-trial interface; it does not yet derive the general Lipschitz/BV class or identify the phase integral with the actual cap-zero-extension Fourier transform. That attachment is the next step toward consuming LF91's logarithmic-domain criterion.

Validation: local structural and unfinished-declaration scans pass. No local Lean executable is available. LF93 CI was still running targeted checks; LF94 run 38204423595 had no job assigned at preparation. LF84 commit 42c6a56d50d9b40e757b8214dec07ddd162aad10 (run 38196728241) remains the latest confirmed full-root checkpoint. Cumulative Lean CI must validate LF86–LF95. No aperture positivity, F4 closure or RH is claimed.
