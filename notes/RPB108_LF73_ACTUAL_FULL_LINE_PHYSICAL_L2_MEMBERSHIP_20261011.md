# RPB108 LF73 — actual full-line physical L2 membership

Extends `NeutralLogMetricTimeActionBounds.lean` with actual finite-action physical L2 membership, a cap-bounded zero-extension specialization, and integrability of pairings with every physical L2 test vector.

The squared norm is bounded by the LF72 uniform physical bound times the LF65 integrable norm. This proves integrability of the squared norm, hence MemLp 2. The argument retains the exterior component and requires no spectral weighted-product premise. Pairing integrability follows from the actual physical toLp representative and its almost-everywhere identity.

No new global definitions, desired membership assumptions, or spectral source premises. For the cap specialization, only measurability and finite-cap boundedness are required; no global integrability assumption is imposed on the original trial.

Validation at submission: LF66 commit 0ee0510b0980a6ba24b574bb5a8bc7d0a2b701da remains the latest confirmed full-root success. LF71 run 38184849291 was running targeted checks; LF72 run 38185105927 was queued. LF73 awaits cumulative remote Lean CI; no local Lean executable is available.

Next: prove equality of the Fourier L2 representative of the actual physical finite action with the constructed spectral representative, and consume it in inverse-Fourier convergence. Full weighted-product membership for intended trials and compressed/full-source identification remain open. No aperture positivity, F4 closure or RH claim.
