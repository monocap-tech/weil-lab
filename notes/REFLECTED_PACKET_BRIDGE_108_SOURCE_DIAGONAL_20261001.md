# RPB-108 — real source diagonal and retained shifted comparison

Date: 2026-10-01 (America/Los_Angeles).
Recovered live research head: `71dddf5382d0b876b96599406a4a923950ed654e`.

## Concrete advance

The prior mixed form required an explicit absolute-symbol upper bound and
expressed source identification as equality with the candidate form's
diagonal. This continuation derives that bound from the retained shifted
comparison and evaluates the candidate's diagonal as the explicit real
source quadratic expression.

For the exact normalized symbol `m = rightLimitCompactWeilSymbolMathlib a`,
the diagonal is

\[
Q_a(f)=\int m(\xi)|\mathcal F f(\xi)|^2\,d\xi
 +2\operatorname{Re}(\overline{M_{-1/2}(f)}M_{1/2}(f)).
\]

There is no additional Fourier normalization factor. The real part and
conjugation in the pole term are essential for complex carriers. The
unconjugated complex product from the real source formula cannot be copied
unchanged into this Hermitian extension.

## Derived symbol bound

From `0 ≤ m + shift ≤ upperC * logarithmicFourierWeight` and the certified
`1 ≤ logarithmicFourierWeight`, the new algebraic estimate is

\[
|m(\xi)|\le (|\mathrm{upperC}|+|\mathrm{shift}|)
 \mathrm{logarithmicFourierWeight}(\xi).
\]

The retained nonnegative lower comparison implies the required shifted
nonnegativity. `rightLimitWeil_absoluteSymbolBound` performs this transfer
for the exact normalized symbol. `sourceDomainWeilFormFromShiftedComparison`
constructs the mixed form using the derived bound internally. It adds no
absolute-symbol analytic hypothesis to the retained two-sided estimates.
The actual normalized EXT5 estimates still need their source attachment;
this is not a new proof of digamma asymptotics.

## Diagonal, carrier, and source comparison

`sourceDomain_signedEnergy_integrable` proves genuine convergence of the
signed real multiplier energy. `sourceDomainMultiplierPairing_diagonal`
identifies the complex integral diagonal with that real energy.
`sourcePoleCrossTerms_diagonal` supplies the real pole algebra, and
`sourceDomainWeilForm_diagonal` identifies the full concrete diagonal.

`sourceDomainQuadratic_carrier` uses retained carrier membership and compact
support to identify the actual carrier's pole term with the real part of
the certified global Hermitian integral against `neutralWeilSourcePole`.
Thus the coefficient expression is tied to the previously named physical
pole function.

The comparison theorems consume equality of a specified source form's
diagonal with `Q_a` on this same retained domain, then use certified complex
polarization to obtain mixed equality. They do not enlarge the test domain.

## Remaining source residue

The historical source-domain witness, its explicit same-domain quadratic
identity, and the exact normalized shifted estimates remain retained source
inputs to attach. An instance of those inputs is not created by the new
comparison theorem.

The actual function representing the multiplier core, its local
integrability, exponential growth, and central cancellation of `r + p_h`
remain open. A real-valued finite quadratic energy does not prove core
regularity. Threshold bookkeeping stays closed; logarithmic Gaussian
coercivity has not started. WD-T40 and canonical Weil standing are unchanged.

## Certification

Certification: exact module passed 8,956 jobs on Lean 4.34.0 and mathlib
`5ed2965256430c3649e86755f9576b54eca72435`. Validation head
`3e285dea9d9ca673fd7f568003d10763b5e7f398`, run `36907744139`,
job `110522433582`, source blob `e1949dd4a3996e2e9445c3117aaa3459d3da36b9`.
All ten audited endpoints use only `propext`, `Classical.choice`, and
`Quot.sound`; the unfinished/project-axiom declaration gate passed.

Validation-only workflow/cache changes are excluded from research promotion.
The original research workflow blob remains
`f194e9564577d3b79831b7abfb91b5933f3af98f`. Prior checkpoint notes remain
immutable. The promoted source is identical to the certified module blob.
