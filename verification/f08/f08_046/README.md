# F08-046 — Original normalized Schwartz difference and square bounds

**Native source-only candidate until original frozen IV023 Lean 4.34.0 build and separate independent whole-ZIP source/axiom custody.**

For actual complex Schwartz `g:𝓢(ℝ,ℂ)`, and every real `1/2≤λ≤3/2`, source F08-030's actual a.e. representative is `Complex.ofReal(Real.sqrt(abs λ)) • g(λ ξ)`. The two proposed new declarations prove a uniform bound on its difference from `g ξ` and on the **squared** norm of that difference, by the genuine source seminorm `M=SchwartzMap.seminorm ℝ 0 0 g` and factor `1+Real.sqrt(3/2)`.

F08-046 stages the exact F08-042 original compiler-certified source bound and the proposed F08-045 common-support theorem. No new source domain, interpolated spectrum or substitute normalizations are permitted. The original F08-042 and F08-045 declarations remain subject to their own acceptance gates.

In conjunction with the F08-045 common interval `[-2R,2R]`, this gives an eventual bounded-support real-valued dominating function:
`((1+sqrt(3/2))*M)^2 * (Icc (-2R) (2R)).indicator 1 ξ`.
However **constructing that real indicator and proving it integrable**, filtered source `volume` dominated convergence, and exact original Lp norm conversion from source F08-030 a.e. equality are **not yet** formally proved. The accepted F08-038 dense-to-all conditional transfer would apply only after those premises are satisfied.

Frequency compact support remains distinct from physical compact support of an inverse Fourier transform and the fixed-radius logarithmic Weil form core. Original signed smooth Weil mixed form, F42 positivity and RH remain open. Research ledger #932; master ledger #898.
