# RPB108 LF75 — actual physical/spectral representative attachment

Adds `NeutralLogMetricFourierAttachment.lean`, registered in targeted CI and the root library, and repairs two physical-bound normalization errors reported by LF73 run 38185387990.

The generic attachment reuses the existing repo theorem `neutralIntegrableL2_fourier_ae` from `ActualZetaCorrelationFourierAgreement.lean`. It proves equality between the L2 Fourier transform of an integrable physical toLp representative and the toLp representative of its ordinary Fourier integral. Inversion gives equality of the inverse-transformed spectral vector with the actual physical vector. A specialization attaches the constructed finite-action spectral representative to the actual full-line finite-action L2 representative, retaining the exterior action.

The spectral weighted-product premise remains explicit in the specialized interface supplying finite spectral membership. No desired Fourier/source identity is assumed; no new global definitions.

Repairs: add Pi.sub_apply when normalizing function subtraction in time integrability, and reduce the function-product application before the squared-norm bound. No physical hypotheses or theorem statements change.

Validation: LF73 failed on those two physical-bound errors plus the already-known finite-measure spectral error/timeouts addressed in LF74. LF74 run 38185651815 was still running targeted checks. LF66 commit 0ee0510b0980a6ba24b574bb5a8bc7d0a2b701da remains the latest confirmed full-root success. LF75 awaits cumulative remote Lean CI; no local Lean executable is available.

Next: consume the actual-action attachment in physical L2 convergence and pairing limits, then establish compressed endpoint-source agreement. Full weighted-product domain membership for intended trials remains open. No aperture positivity, F4 closure or RH claim.
