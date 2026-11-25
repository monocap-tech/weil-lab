# RPB108 LF74 — infinite-measure spectral L2 proof repair

Repairs the spectral L2 passage in `NeutralLogMetricSpectralL2.lean` after LF71 run 38184849291, job 114605162732, reported an unavailable `IsFiniteMeasure volume` instance and three declaration-elaboration heartbeat timeouts.

The previous Vitali theorem required finite measure and therefore did not apply to full-line spectral volume. LF74 replaces it with dominated convergence of the real squared errors, bounded by `4*norm(G)^2`, where G is the full weighted product. Integrability follows from the retained MemLp 2 domain condition. The proof converts the squared-error lintegral to eLpNorm 2 by its defining formula and continuity of the ENNReal square-root power. No finite-volume instance is introduced and no theorem statement or domain condition changes.

The three declarations involving dependent toLp representatives receive bounded theorem-local maxHeartbeats budgets of 1,000,000 instead of the default 200,000. This changes elaboration resources, not proof premises or trust.

Validation: LF71's cumulative build failed on the finite-measure requirement and three timeouts. LF66 commit 0ee0510b0980a6ba24b574bb5a8bc7d0a2b701da remains the latest confirmed full-root success. LF73 run 38185387990 has started dependency resolution. LF74 requires cumulative remote CI; no local Lean executable is available.

Physical/spectral representative agreement, full weighted-product membership for intended trials, and compressed/full-source identification remain open. No new definitions, aperture positivity, F4 closure or RH claim.
