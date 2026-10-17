# LF96 — actual zero-extension Fourier decay

Adds an exact dictionary from the Fourier transform of the actual cap indicator representative to the finite-interval phase integral. It uses Mathlib's negative-exponent 2π convention, preserves multiplication order explicitly, and removes the closed/open endpoint difference through null singleton measure. The dictionary requires only B ≥ 0; no integrability premise is needed for this identity of totalized integrals.

The actual zero-extension reciprocal Fourier norm bound then consumes LF95. It retains both endpoint norms and the interval derivative L1 mass, requires nonzero frequency, and has explicit differentiability and interval-integrable derivative hypotheses. The next step is to consume this derived decay in LF91's full logarithmic-domain criterion and then endpoint compression. General Lipschitz/BV coverage remains open.

Validation: structural and unfinished-declaration scans pass locally; Lean is unavailable locally. LF93 targeted CI was still running and LF95 CI had no job assigned at preparation. LF84 (42c6a56d50d9b40e757b8214dec07ddd162aad10, run 38196728241) remains the latest confirmed full-root checkpoint. Cumulative CI is required for LF86 onward. No aperture positivity, F4 closure or RH is claimed.
