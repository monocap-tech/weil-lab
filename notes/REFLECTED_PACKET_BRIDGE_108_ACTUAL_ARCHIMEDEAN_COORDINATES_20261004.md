# RPB108 actual archimedean coordinates — 2026-10-04

Parent certified research: 810ee2eaf39637d8071720cf3429d88a12eb2c26.

The new module proves six identities on the already constructed actual-divisor Green carriers. Ordinary Fourier transform of the same C² compact inverse correlation agrees almost everywhere with its concrete mixed spectrum; its Fourier integral is L¹. The raw real-frequency coordinate is exactly -2πξ. The external gamma bracket is even, agrees pointwise with compactWindowArchimedeanSymbol, and consequently evaluates at -2πξ to the native symbol at +2πξ. Evenness uses the certified external digamma conjugation theorem, with quarter-line noninteger membership proved arithmetically.

The initial candidate failed only because simplification did not descend to the pointwise Fourier rewrite under an almost-everywhere function equality. The corrected proof introduces the pointwise AE witness, rewrites the raw transform, and uses that witness.

This chunk supplies the spectral and special-function coordinate dictionaries. It does not yet prove weighted digamma integrability or transform the archimedean integral. Fourier L¹ integrability alone does not establish weighted integrability.

Next cursor: derive absolute integrability of the digamma-weighted same Green correlation spectrum using the certified external digamma strip growth bound and existing zeroth/first/second spectral moments. Apply the exact real change of variables r = -2πξ; the raw-spectrum almost-everywhere identity and gammaBracket(-2πξ) = compactWindowArchimedeanSymbol(2πξ) are now proved. Finish the actual archimedean form = native spectral pairing, combine the certified prime and pole dictionaries, then recover retained WD-T38 coefficients/source data and prove the same-vector source/null identity. Retained spectral operator-domain membership is not assumed; background completion, central cancellation and F-4 remain open.

Residue preserved: exact constructed Green source/divisor identities, prime right-limit spectral identity, canonical-image pole dictionary, full external explicit-formula closure. Retained WD-T38 same-vector source/null attachment, central cancellation, background completion, and F-4 remain open. No RH claim, no retained operator-domain membership assumption, no new project axioms.

Certificate: candidate e9668aafc0756663c76cec81c474b73c2b66a823; [run 37179769918](https://github.com/monocap-tech/weil-lab/actions/runs/37179769918), job 111369824421. Lean 4.34.0; isolated 9149/full 9182 build jobs. All six public exports audit to exactly [propext, Classical.choice, Quot.sound]; unfinished declaration gate passed. Exact source/root promoted from this candidate.
