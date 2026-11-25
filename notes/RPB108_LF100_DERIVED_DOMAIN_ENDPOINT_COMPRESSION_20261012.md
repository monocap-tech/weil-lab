# LF100 — endpoint compression with a derived domain

Adds `neutralLogMetricEndpointSource_compression_eq_of_derivative`. For a measurable bounded cap trial with the existing cap Lipschitz modulus, classical derivative witnesses and an interval-integrable derivative, the cap compression of the whole-line logarithmic spectral source equals the constructed physical endpoint L2 candidate. The spectral-domain witness is derived by LF99, not assumed. Nonzero endpoint values are allowed.

This consumes the existing supported-test compression theorem. It does not identify the full-line source with its cap compression or discard exterior action. It does not derive operator-domain membership from form energy. The derivative hypotheses remain stronger than general cap Lipschitz/BV regularity; deriving a broader class and concrete trial specializations remains further work.

Validation: local structural and unfinished-declaration scans pass; Lean is unavailable locally. LF98 run 38209431745, job 114680063078, was running targeted checks; LF99 run 38209534513 had no assigned job. LF84 (42c6a56d50d9b40e757b8214dec07ddd162aad10; run 38196728241) remains the latest successful full-root checkpoint. LF100 requires cumulative CI. No aperture positivity, F4 closure or RH is claimed.
