# RPB-108 — integral-growth Gaussian support-gap bridge

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `238f9afcfe9ae41176e95f58b33d0f6670b58301`.

## Growth interface repaired additively

The finite-prime pass established actual local regularity and integral growth,
while exposing that compact L2 support does not supply the current full
residual's pointwise exponential field. `NeutralIntegralGrowthResidual`
now retains a locally integrable q, strict radius a>c, nonnegative rate κ,
genuine integrability of |q(x)| exp(-κ|x|), and a.e. central cancellation.
It is an additive interface; previous carriers and historical proofs remain
unchanged. It does not itself supply the actual archimedean representative.

## Actual Gaussian estimate

The radius-only exterior envelope is proved for the actual filtered carrier
without requiring any residual package. Gaussian completion bounds

\[
 |G_R(x)|e^{\kappa|x|}
 \le \|C_k\|\sqrt R\,\|h\|_{L^1}
 e^{\kappa c}e^{-R(a-c)^2/16}
\]

outside (-a,a), whenever R≥0 and 8κ≤R(a-c).

`integralGrowth_pairing_bound` proves genuine Hermitian product integrability
and bounds its integral by this exterior weighted test bound times the
weighted L1 mass of q. The actual Gaussian specialization consequently gives

\[
 \left|\int \overline{G_R(x)}q(x)\,dx\right|
 \le \|C_k\|\sqrt R\,\|h\|_{L^1}
 e^{\kappa c}e^{-R(a-c)^2/16}
 \int |q(x)|e^{-\kappa|x|}\,dx.
\]

The proof keeps central cancellation a.e. and uses no pointwise bound on q.
The fixed weighted mass replaces the former pointwise growth constant and
remaining Gaussian tail-mass integration. The collar decay is still explicit;
absorption of the sqrt(R) prefactor is not claimed in this pass.

## Concrete shell and weak-identity extension

`primeShellIntegralGrowthResidual` constructs an actual instance for the
already represented physical shell, using rate zero and its certified L1
mass and central vanishing. It is the prime correction component, not the
whole Weil residual.

`integralGrowth_weakIdentity_of_integrableSchwartz` extends a specified
all-compact-test weak identity by the previously certified Schwartz cutoffs.
Its proof is independent of the old pointwise-growth package. Both test
pairings must genuinely converge; the exact source weak identity remains an
input. This theorem alone does not attach the full Gaussian multiplier/pole
identity.

## Remaining residue

The integral-growth route to the physical Gaussian support-gap estimate is
constructed. Next: construct the actual archimedean function and weighted
mass, attach the full compact weak identity and central cancellation, and
supply pole pairing for the weighted route. Actual source-domain/quadratic/
normalized-estimate attachment remains open. These inputs still precede
logarithmic coercivity and final WD-T40 assembly.

Threshold bookkeeping stays closed. Coercivity has not started; canonical
Weil and WD-T40 standing are unchanged.

## Certification

Certification: exact module passed 8,958 jobs on Lean 4.34.0 and mathlib
`5ed2965256430c3649e86755f9576b54eca72435`. Validation head
`8250f691fbfcf7fbc58be23c21d4a279820d89df`, run `36930149011`,
job `110597667759`, source blob `a6c45e4a13c704a522164d0a420435bdc7858636`.
All six audited endpoints use only `propext`, `Classical.choice`, and
`Quot.sound`; the unfinished/project-axiom declaration gate passed.

Validation-only workflow/cache changes are excluded from research promotion.
The original research workflow blob remains
`f194e9564577d3b79831b7abfb91b5933f3af98f`. Prior checkpoint notes remain
immutable. The promoted source is identical to the certified module blob.
