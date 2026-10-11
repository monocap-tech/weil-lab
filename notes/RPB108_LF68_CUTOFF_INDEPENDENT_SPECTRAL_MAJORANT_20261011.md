# RPB108 LF68 — cutoff-independent spectral majorant

Extends `NeutralLogMetricTimeActionLimit.lean` with three bounds:

- The real finite cancelled coefficient lies between one and the canonical logarithmicFourierWeight.
- The actual complex finite cancelled coefficient has norm at most that weight.
- The Fourier transform of every actual finite full-line action is bounded by `norm(Fourier(v)(ξ))*logarithmicFourierWeight(ξ)`.

Nonnegativity on positive time, integrability of the full cancelled Laplace integrand, and integral monotonicity under set restriction bound the real coefficient. The complex coefficient is its exact real cast. The final estimate consumes the derived actual-action Fourier identity and finite cancellation equality. No new global definitions or desired bound assumptions.

Validation at submission: LF65 commit 89a9c738970d06f1a362824681ff9c78d155fcaa passed run 38181762113, including targeted transport, complete root library and unfinished-declaration rejection. LF66 run 38183520443 was checking; LF67 run 38183731460 was queued. LF65 is the latest confirmed full-root checkpoint. LF68 awaits cumulative remote Lean CI; no local Lean executable is available.

This supplies a common majorant for spectral L2 passage when the full weighted product is in L2. It does not infer that domain membership from cap regularity or form energy. Spectral L2/domain and compressed/full-source identification remain open. No aperture positivity, F4 closure or RH claim.
