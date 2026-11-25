# RPB108 LF77 — cap-supported spectral/endpoint agreement

Adds weak agreement of the actual full-line spectral source and endpoint candidate against every physical L2 test vanishing almost everywhere outside the cap. The proof compares two independently constructed limits: full-line physical-vector pairing convergence from LF76, and cap-supported Poisson-action integral pairing convergence. Their finite pairings coincide because the test vanishes outside the cap and the trial zero extension equals the trial inside it. Uniqueness of limits identifies the pairings.

The full weighted-product L2 membership hypothesis remains explicit. This is supported-test agreement, not equality of the endpoint zero extension with the full-line source. Exterior action is retained. No new global definitions or desired attachment hypotheses.

Repairs the remaining time integrability normalization reported by LF75 run 38186194385: first change function subtraction to the pointwise lambda before distributing multiplication. LF76's spectral normalization and command-placement repairs remain awaiting CI.

Validation: structural checks and unfinished-declaration rejection run locally; cumulative remote Lean validation pending. LF76 run 38186612205 was resolving dependencies. LF66 commit 0ee0510b0980a6ba24b574bb5a8bc7d0a2b701da remains the latest confirmed full-root success; there is no local Lean executable.

Next: upgrade supported-test agreement to explicit cap-compressed vector equality and derive intended-trial weighted-product domain membership. No aperture positivity, F4 closure or RH claim.
