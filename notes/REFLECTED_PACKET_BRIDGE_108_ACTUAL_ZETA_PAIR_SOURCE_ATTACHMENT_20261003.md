# RPB-108 — actual zeta conjugate-ordinate source attachment (2026-10-03)

Parent: `7a15744a62a87a111f3e653b9aa5fd8234f8ea31`.
Cursor: actual divisor/source transport for WD-T38 witness attachment.
Threshold bookkeeping is closed; F-4 pending.

## Definitions before use

`neutralActualZetaZeroConjugate` maps the actual open-strip zero point
rho to conj rho. It consumes the pinned mathlib theorem
`riemannZeta_conj`, whose proof uses real Dirichlet coefficients and
analytic continuation; no new conjugation hypothesis is supplied.

`neutralActualZetaZeroPair` is the already certified functional-equation
reflection of that conjugate point, hence rho -> 1-conj rho.
This is the actual partner giving conjugate Bombieri ordinates.

## Proved actual witnesses

Zeta conjugation preserves the actual zero point carrier and is
involutive. It commutes with rho -> 1-rho. In the convention
rho=1/2+I gamma, conjugation alone acts as gamma -> -conj gamma,
whereas the combined point pair acts as gamma -> conj gamma.
The combined pair is involutive.

The existing concrete source-column bridges are immediately consumed on
these actual point partners:
- the positive pair source is unchanged;
- the negative pair source changes sign;
- the selected negative rank-one operator is unchanged.

Thus this part of the retained linear-analysis convention is now attached
to actual zeta-zero points, rather than to independently supplied packet
symmetries. The fixed negative-coordinate sign is not discarded.

## Scope and next actual transport

Point reflection does not certify multiplicity equality or the
sqrt(multiplicity) quotient normalization. These require actual analytic
orders and their symmetry transport, followed by divisor/count custody.
No exhaustive shell enumeration or sharp zero-count theorem is fabricated.

The current P,C,k and physical Rk/Gh or background-completion vector remain
unidentified with that actual divisor/core model. Next: actual
multiplicity/divisor transport and same-domain explicit-formula or
retained background/physical-map transport. Then attach the current source
quadratic/null law and consume the existing same-domain polarization and
normalized comparison bridges.

Endpoint nullity remains distinct from enlarged frozen-action central
cancellation. Once that actual central witness is available, immediately
consume `neutralExteriorIntegralGrowthResidual_realizes_of_central`.
It supplies actual local regularity, boundary removal and whole compact
weak realization without assuming full spectral L2. Exterior, digamma,
boundary and threshold work stay closed.

## Witness status

Proved: actual zeta conjugation, commuting functional-equation reflection,
actual conjugate-ordinate pairing and involution, and actual point-pair
positive/negative source and selected-operator attachment.

Retained/written: native/background completion, strict background
positivity and completion-based endpoint mixed nullity. Current actual
source/model/vector identification and enlarged cancellation remain open.

Current `MemLp (neutralWeilSpectralProduct carrier a) 2` is still
unproved from WD-T38 and unassumed. No earlier native-family derivative
or logarithmic energy theorem is transferred to the current carrier by
this point-pair result. F-4 remains pending.

## Validation

Validation commit: `156df50e172673982a445d01f0a20cf5258f5781`.
GitHub Actions run `37148403859`, job `111276998075`: full root build
passed (9,042 jobs). All nine public declaration axiom audits passed with
only `propext`, `Classical.choice`, and `Quot.sound`; no project axiom or
unfinished-proof declaration was introduced.
