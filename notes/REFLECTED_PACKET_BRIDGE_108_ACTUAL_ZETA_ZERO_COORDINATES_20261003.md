# RPB-108 — actual zeta zero coordinates and reflection (2026-10-03)

Parent: `964bc39dfe8573ce67ecb0cabd14a31eaa7ca454`.
Cursor: actual divisor/source transport for WD-T38 witness attachment.
Threshold bookkeeping is closed; F-4 pending.

## Definitions before use

`NeutralActualZetaZeroPoint` is the subtype of the actual mathlib
`riemannZeta` zero set satisfying 0 < Re rho < 1. It records genuine
open-strip zero points, not arbitrary ordinates admitted by shell bounds.
It is not yet a multiplicity-weighted divisor or shell enumeration.

`neutralActualZetaOrdinate rho = -I * (rho - 1/2)` uses the Bombieri
convention rho=1/2+I gamma. Its real part is Im rho; its imaginary part
is 1/2-Re rho.

## Proved actual witnesses

The source reconstruction is exact, and the actual zeta value at the
reconstructed argument is zero. Open-strip membership gives the strict
ordinate strip |Im gamma| < 1/2 without RH.

The pinned mathlib functional equation proves rho -> 1-rho carries
these actual points to actual points. The map is involutive, and its
ordinate action is gamma -> -gamma. This is functional-equation
reflection, not conjugate-ordinate pairing. The latter requires the
separate zeta conjugation transport and remains next.

Every such actual ordinate has nonzero `problemOneGreenDenom`:
its real part is (Re gamma)^2+1/4-(Im gamma)^2 > 0. No shell-height
lower bound, frequency gap, operator-domain membership, or spectral L2
premise is needed. This supplies the actual Green-denominator witness,
including points not covered by the shell model's height >= 1 condition.

No extra zero equation or source equality is postulated as a new
representation field. The coordinate carrier is defined directly using
the existing actual function; the reflection proof consumes its certified
functional equation.

## Precise scope and next transport

This repairs actual-zero point custody at the first arithmetic boundary.
The shell record and its historical definitions are unchanged. The grid
audit remains valid; no current arbitrary shell record is automatically
converted into this actual zero carrier.

Next arithmetic pieces are actual conjugate-ordinate transport,
multiplicity-weighted divisor enumeration/quotient and its count custody,
then the actual same-domain explicit-formula/source transport or direct
retained background-form identification. The current P,C,k and physical
Rk/Gh map must be transported to that actual model; an independently
constructed native Green sum may not be substituted for the current mode.

Existing source diagonal/polarization and normalized comparison bridges
remain ready, but the current WD-T38 quadratic/null attachment and enlarged
central cancellation are not proved by point custody alone.

Once actual enlarged central cancellation is available, immediately
consume `neutralExteriorIntegralGrowthResidual_realizes_of_central`
for actual locally integrable residual, boundary removal and whole compact
weak realization. Do not reopen exterior, digamma, boundary or threshold
work.

## Witness status

Proved in this chunk: actual zero point/source equation, strict ordinate
strip, actual functional-equation reflection and involution, and
nonzero actual Green denominator.

Retained/written: native/background completion, its actual physical map,
strict background positivity and completion-based endpoint mixed nullity.
Current source/model/vector identification remains open.

Current `MemLp (neutralWeilSpectralProduct carrier a) 2` remains unproved
from WD-T38 and unassumed. The earlier native-family derivative/logarithmic
domain proofs remain proved for their stated supplied inputs; they are
not upgraded to a current-carrier spectral witness. F-4 remains pending.

## Validation

Validation commit: `c388dc65530c558a5037107ec310ee1cb5ed4dae`.
GitHub Actions run `37147912095`, job `111275554391`: full root build
passed (9,041 jobs). All seven public declaration axiom audits passed with
only `propext`, `Classical.choice`, and `Quot.sound`; no project axiom or
unfinished-proof declaration was introduced.
