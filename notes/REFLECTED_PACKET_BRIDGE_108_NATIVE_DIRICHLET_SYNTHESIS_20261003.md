# RPB-108 — actual native Dirichlet synthesis (2026-10-03)

Parent: `387ab390612a3209663f6c0b19f99b91f492e52f`.
Cursor: WD-T38 actual source/quadratic/null attachment; F-4 pending.
Threshold bookkeeping is closed.

## Definitions before use

`NeutralNativeShellCoefficients count` is the actual Mathlib `lp 2`
space of complex coefficients indexed by the retained multiplicity shell
type `ZetaShellIndex count`. It is not an independently assumed Hilbert
coefficient space.

`neutralNativeGreenSynthesis` is the L2 sum of coefficient multiples of
the full endpoint-corrected compact native Green columns.
`neutralNativeGradientSynthesis` is the L2 sum of the same coefficient
multiples of their compact derivative columns. The latter name describes
its defining columns; the weak derivative identity for the two sums is
not asserted in this chunk.

## Proved actual witnesses

The parent's actual square-summability of both column families combines
with the coefficient space's norm-square summability. The elementary
product bound by the sum of the two squares proves absolute L2 convergence
of each series. Both synthesized vectors therefore have actual HasSum
witnesses for every supplied native coefficient vector, under the existing
positive-window, shell-data, and shell-count hypotheses.

Applying the actual continuous linear functional `innerSL` to each
HasSum proves the same-vector mixed pairing law

    inner f (synthesis u) = sum_g u_g * inner f column_g

for every physical L2 vector f. The convention is first-antilinear,
second-linear. These are actual vector sums and actual continuous pairings;
no source representation equality is imported as a premise.

## Retained and unresolved

This constructs native physical Green/derivative series; bounded operator
packaging, their weak derivative relation, and supported logarithmic form
attachment are not certified here. Nor is native background completion
constructed. Its retained written coefficient/background dictionary still
requires realization in the formal source model.

The current WD-T38 physical carrier is independently parameterized and is
not identified with one of these sums or with the retained background
completion vector. Its actual logarithmic energy and source quadratic/null
identity remain unattached. Current-mode same-domain mixed/normalized
attachment and enlarged-window central cancellation remain open.

The retained shell records remain explicit inputs, with no new actual-zeta
instance claimed. The smooth compact columns' L2 convergence is not a
proof of current-mode membership
`MemLp (neutralWeilSpectralProduct carrier a) 2`. That spectral witness
remains unproved from WD-T38 and is not assumed.

Once actual central cancellation is available,
`neutralExteriorIntegralGrowthResidual_realizes_of_central` consumes the
existing locally integrable residual and boundary-removal route. Exterior,
digamma, boundary, and threshold work remain closed; F-4 is pending.

## Validation

Validation commit: `889e85d9d12c8109672dec156e13762754d54aff`.
GitHub Actions run `37139836509`, job `111251788314`:
root build passed (9034 jobs). All six public theorem audits use only
`propext, Classical.choice, Quot.sound`, with no `sorryAx`.
The unfinished/project-axiom declaration gate passed.
Research workflow and historical notes are preserved.
