# RPB108 LF80 — Schwartz trial domain membership

Derives first-frequency-moment L2 membership for Schwartz spectral functions by multiplying in Schwartz space. LF79 then gives full logarithmic multiplier-domain membership. The Fourier transform preserves Schwartz space, supplying the weighted Fourier domain for every physical Schwartz trial with no weighted-domain premise. For cap-supported Schwartz trials, the actual trial zero extension equals the original function, so the same domain theorem applies directly to the zero extension used by the endpoint-source identity.

This establishes a concrete smooth trial class. Arbitrary cap-Lipschitz trials with boundary jumps remain outside this proof; their weaker decay route remains open. No new global definitions or exterior-action suppression.

Repairs the single spectral error reported by LF79 run 38188007961: use simp only [pow_two] across both scalar types after rewriting the ENNReal norm. LF79's run built the physical bounds module successfully but stopped before the attachment module.

Validation: local structural checks and unfinished-declaration rejection pass. LF80 awaits cumulative remote Lean validation. LF66 commit 0ee0510b0980a6ba24b574bb5a8bc7d0a2b701da remains the latest confirmed full-root success. No local Lean executable is available.

Next: consume the derived Schwartz domain witness in endpoint compression and resolve cumulative CI; then extend to boundary-jump trial classes. No aperture positivity, F4 closure or RH claim.
