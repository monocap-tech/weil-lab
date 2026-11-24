# F08-025 — exact source logarithmic dilation correction factor (first compiler slice)

**Draft, nonpromoting until genuine Lean and independent custody.**

This slice defines the exact real scalar correction
`m_λ(ξ) = sqrt(logarithmicFourierWeight ξ / logarithmicFourierWeight (λξ))`
in the original IV023 logarithmic Hilbert carrier. Its five Lean targets prove nonnegativity, exact value one at λ=1, squared uniform bound `m_λ(ξ)^2 ≤ 1 + log 2` for `1/2 ≤ λ ≤ 1`, continuity at λ=1, and pointwise convergence to one.

It **reuses** the independently accepted F08-001 original scalar inequality and pinned original `logarithmicFourierWeight_continuous`. This is the measurable/pointwise ingredient for the decomposition `K(D_λf) = m_λ U_λ(Kf)`, not a proof of that equality.

**Important limitations:** Native `RealComplexL2` physical/frequency dilation, its exact `-2π` Fourier scaling, support transportation, isometry and strong continuity of `U_λ`, the weighted Hilbert element identity, fixed-support smooth core, all-complex signed Weil identity, F42/unrestricted positivity/RH are NOT proved by this slice. Do not promote F08-025 as completed based on five scalar theorems.

**Source pin:** original IV023 research commit `614ba879f7389fdb620c474adaee273b00eac71c`; original `Arithmetic/LogarithmicForm.lean` blob `ae932d4f3f7e4d6d06dbd778a5708927172238dc`, original `Morphology/NeutralCanonicalFormDomain.lean` blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`, accepted F08-001 additive blob `5dce3a647223afbf75ef09f72d90c8afb331ee81`. Lean v4.34.0; require direct `.olean`, five exact named standard-only axiom reports and separate original producer source/ZIP custody before acceptance.

Parent [Issue #932](https://github.com/monocap-tech/weil-lab/issues/932#issuecomment-7117926487), master ledger #898.
