# RPB108 LF69 — spectral L2 passage with explicit domain condition

Adds `NeutralLogMetricSpectralL2.lean`, registered in targeted CI and the root library.

The new theorem upgrades Fourier transforms of actual full-line cutoff actions from pointwise convergence to convergence in the spectral L2 seminorm, under explicit membership of `Fourier(v)*logarithmicFourierWeight` in L2. A second theorem specializes to actual cap-bounded zero extensions.

The proof derives measurability of every cutoff Fourier transform from continuity of the Fourier transform of the proved integrable action. LF68's logarithmic majorant and the weighted-product membership give uniform integrability; LF67 supplies pointwise convergence; Mathlib's finite-p Lp convergence theorem supplies the limit. No desired convergence premise or new global definition.

The full weighted-product membership is an operator-domain condition. It is deliberately retained as a hypothesis and is not derived from cap regularity or form energy by this theorem. The conclusion concerns spectral functions/seminorms, not yet Fourier L2 representatives or the physical-source identity.

Validation at submission: LF65 commit 89a9c738970d06f1a362824681ff9c78d155fcaa passed complete-root run 38181762113. LF66 run 38183520443 was running targeted checks; LF68 run 38183965819 was queued. LF65 remains the latest confirmed full-root checkpoint. LF69 awaits cumulative remote Lean CI; no local Lean executable is available.

Remaining: prove weighted-product membership for the intended trials, transport actual Fourier representatives through Plancherel/inversion, and identify the compressed/full physical source with exterior action retained. No aperture positivity, F4 closure or RH claim.
