# F08-005 — genuine source log-Fourier mollifier multiplier convergence

**Candidate only until actual Lean compile + strict axioms + independent custody.** This addresses the F08 original supported logarithmic domain rather than numerical F41 certificates. Source obligation #932.

Frozen mathematical research source: IV023 `614ba879f7389fdb620c474adaee273b00eac71c`, `NeutralCanonicalFormDomain.lean` Git SHA `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`; exact source weight `w(ξ)=log(e+|ξ|)`, genuine physical complex `L²` Fourier coordinate.

Three Lean candidates: for `m:ℝ→ℂ` with pointwise `‖m ξ‖≤1`, bound
`w ξ · ‖(m ξ−1)F ξ‖² ≤ 4(w ξ·‖F ξ‖²)`;
deduce integrability of the weighted Fourier error for a strongly measurable complex multiplier; and prove by dominated convergence that if a sequence `mₙ` of these multipliers converges pointwise to `1`, then
`∫ w ξ·‖(mₙ ξ−1)F ξ‖²dξ → 0`.

These are not merely restatements of F08-003's integrability of `mF`; the new error converges to zero under an explicit source-dependent integrable majorant. They are the needed *spectral convergence* theorem for a compact mollifier **after** a separate source-matched Fourier-convolution identity has been proven. They do not prove an arbitrary Fourier multiplier preserves physical support; the support-gap construction, mollifier transform, dilation strong continuity, original Schwartz↔native equality and global positivity remain open.

Single narrowly source-scoped Lean 4.34/Mathlib pinned compiler run and **three named ordinary-axiom** checks; independent real ZIP/source/axiom verification required after a successful compiler receipt.
