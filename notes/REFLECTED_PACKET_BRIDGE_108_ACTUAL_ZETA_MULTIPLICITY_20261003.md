# RPB-108 — actual zeta multiplicity and divisor coordinates (2026-10-03)

Parent: `e7a6ae95e1b686442b3341401890f67f2298c27c`.
Cursor: actual divisor/source transport for WD-T38 witness attachment.

## Proved witnesses

For every actual open-strip zeta-zero point, zeta is analytic at the
point. The point differs from its pole at 1. Analytic order is finite:
the complement of {1} in the complex plane is connected, zeta is
analytic there, and its actual nonzero value at 2 excludes infinite
order everywhere on that domain. No retained packet field supplies
this finiteness.

`neutralActualZetaMultiplicity` is the natural analytic order. Its
coercion equals the actual extended analytic order and it is strictly
positive at every actual zero point. There is an actual analytic germ
g, nonzero at the point, with zeta(z) = (z-rho)^m g(z) locally.

`NeutralActualZetaDivisorCoordinate` is the dependent sum of actual
zero points with `Fin m`. Each fiber has exactly m elements and is
nonempty. Each repeated coordinate reconstructs an actual zeta zero
via the Bombieri ordinate convention. No zero simplicity, RH, chosen
enumeration, shell-count estimate, or existence of a zero is asserted.

## Remaining attachment

The actual point pair from the previous head is certified, but its
multiplicity transport is not yet proved by this module. Next is
actual multiplicity symmetry, then the lawful multiplicity-weighted
pair/divisor analysis and the same-domain explicit-formula transport.
The new repeated-coordinate type is not identified with the retained
WD-T38 coefficient system merely by naming it a divisor.

Current WD-T38 physical carrier identification, actual source
quadratic/null attachment, same-domain polarization/normalized
attachment, and enlarged central cancellation remain open. The
background completion model and its endpoint mixed nullity remain
retained/written, not an instantiated current Lean witness.

As soon as actual enlarged central cancellation is proved, consume
`neutralExteriorIntegralGrowthResidual_realizes_of_central` immediately:
it supplies actual local regularity, boundary removal and whole
compact weak realization. Do not reopen those certified steps.

Current `MemLp (neutralWeilSpectralProduct carrier a) 2` is unproved
from WD-T38 and unassumed. Finite analytic multiplicity says nothing
about the current carrier's spectral operator domain. The stronger
regularity of an arbitrary native Green synthesis is not transferred
to that carrier. Threshold work remains closed; F-4 remains pending.

## Validation

Validated exact candidate `e59d618084d0c5d12ded0c1deea0649d82efdb98` in
[run 37150215782](https://github.com/monocap-tech/weil-lab/actions/runs/37150215782),
job `111282340105`: full `lake build WeilDefect` succeeded
(9,043 jobs). Nine public declaration audits report only
`[propext, Classical.choice, Quot.sound]`. The unfinished/project-axiom
gate passed. The initial candidate failed on an unqualified namespace;
the corrected exact candidate above is the one certified and promoted.
The research workflow is preserved from the parent.
