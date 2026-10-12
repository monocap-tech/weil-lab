# RPB108 LF86 — fractional-frequency domain criterion

Adds a weaker sufficient logarithmic-domain criterion. For any σ > 0, almost-everywhere strong measurability of G together with L2 membership of (e+|ξ|)^σ G implies L2 membership of G log(e+|ξ|). The proof uses the pinned Mathlib inequality Real.log_le_rpow_div and the real majorant (1/σ) times the norm of the fractional product. A quarter-frequency specialization supplies a concrete interface.

No first-frequency-moment hypothesis is used. This opens a route for boundary-jump trials: a 1/|ξ| Fourier tail is compatible with a quarter-frequency L2 moment, whereas the full first moment may fail. The integrable tail and the actual Fourier decay are not yet derived by this checkpoint; fractional membership remains an explicit sufficient premise. No new global definitions or source-attachment assumptions.

Validation: LF84 commit 42c6a56d50d9b40e757b8214dec07ddd162aad10 passed cumulative targeted compilation, complete root build and unfinished-declaration rejection in run 38196728241, job 114643485286. LF85 records that success. Local structural checks and unfinished-declaration rejection pass for LF86; cumulative remote Lean validation is pending. LF84 remains the latest externally confirmed full-root code checkpoint. No local Lean executable is available.

Next: prove the quarter-frequency L2 tail majorant and derive the required Fourier decay for cap-Lipschitz or bounded-variation zero extensions, including endpoint boundary terms. No aperture positivity, F4 closure or RH claim.
