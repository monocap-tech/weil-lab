# RPB108 LF79 — frequency-moment domain criterion

Adds a sufficient full logarithmic multiplier-domain criterion: if a spectral function G and ξG belong to L2, then G log(e+|ξ|) belongs to L2. The proof uses log(e+|ξ|) ≤ e+|ξ| and the L2 majorant e‖G‖+‖ξG‖, with measurable weighted multiplication. A specialization supplies the domain proof to the cap-compression identity from Fourier L2 membership and first-frequency-moment L2 membership.

This replaces the desired logarithmic-product premise with an independent, stronger frequency-moment regularity criterion. It does not derive that criterion for all bounded cap-Lipschitz trials, and does not identify form-energy membership with operator-domain membership. Boundary jumps of zero extensions remain relevant. No new global definitions; exterior action retained.

Validation: local structural checks and unfinished-declaration rejection pass. LF77 run 38187183332 was running targeted Lean checks; LF78 run 38187687373 was pending. LF79 awaits cumulative remote Lean validation. LF66 commit 0ee0510b0980a6ba24b574bb5a8bc7d0a2b701da remains the latest confirmed full-root success. No local Lean executable is available.

Next: resolve cumulative CI and prove the frequency-moment criterion for an appropriate smooth or zero-boundary trial class, or use a weaker decay criterion for trials with boundary jumps. No aperture positivity, F4 closure or RH claim.
