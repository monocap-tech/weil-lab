# RPB108 LF72 — physical bounds for finite-action attachment

Adds `NeutralLogMetricTimeActionBounds.lean`, registered in targeted CI and the root library.

The two new theorems prove that positive-time Poisson convolution preserves a measurable trial's uniform bound, and that the actual full-line finite cancelled action is uniformly bounded by `M + integral(abs(weight))*2*M`. Unit shifted Poisson mass proves the convolution bound. Time integrability of the cancelled action is proved before estimating its norm integral; the pointwise difference is bounded by 2*M.

These physical bounds require no spectral weighted-product domain premise. Together with the previously proved whole-line integrability, they prepare direct L2 membership of the finite physical actions for representative/Plancherel attachment. No global definitions or desired attachment assumptions are introduced.

Validation at submission: LF66 commit 0ee0510b0980a6ba24b574bb5a8bc7d0a2b701da passed run 38183520443, including targeted transport, complete root library and unfinished-declaration rejection. LF71 run 38184849291 was resolving dependencies. LF66 is the latest confirmed full-root checkpoint. LF72 awaits cumulative remote Lean CI; no local Lean executable is available.

The actual-action L2 membership and its representative identification remain to be proved. Full weighted-product domain membership for intended trials and compressed/full-source identification remain open. No aperture positivity, F4 closure or RH claim.
