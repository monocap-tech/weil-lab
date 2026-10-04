# RPB108 actual native logarithmic bounds — 2026-10-04

Definitions precede load-bearing use in ActualZetaNativeLogBounds.lean.

| Term | Exact meaning |
| --- | --- |
| Canonical logarithmic weight | The existing weight log(exp(1) + |ξ|), bounded below by 1. |
| Vertical digamma error | For positive real part and |Im z| ≥ 1, the certified Stirling theorem bounds |Re ψ(z) − log ‖z‖| by 4. |
| Actual archimedean logarithmic envelope | A nonnegative global constant bounds the absolute difference between the actual archimedean symbol at 2πξ and the canonical weight. |
| Prime symbol bound | The finite sum of absolute actual prime coefficients over the unchanged right-limit prime-power set; equality-threshold primes remain included. |
| Actual native logarithmic envelope | For each window a, a nonnegative constant C bounds |m_a(ξ) − log(exp(1) + |ξ|)| for every real ξ. |
| Shifted coercivity | The actual inequality weight ≤ m_a + C ≤ (1 + 2C) weight. The lower coefficient is exactly 1. |

The envelope is derived from actual special-function estimates and the finite prime sum. It is not an assumed symbol bound or a new representation interface. It does not establish all-derivative temperate growth, unshifted background positivity, a contractive WD-T10 factorization, source-form density, retained graph membership, or the retained same-vector P/C/k source/null identity.
