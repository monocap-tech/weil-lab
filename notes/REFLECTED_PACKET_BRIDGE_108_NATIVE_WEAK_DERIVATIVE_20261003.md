# RPB-108 — actual native weak derivative attachment (2026-10-03)

Parent: `6a4d9dad1c4587af595294b891ddf692bf67fba8`.
Cursor: WD-T38 actual source/quadratic/null attachment; F-4 pending.
Threshold bookkeeping is closed.

## Proved concrete witnesses

`NeutralNativeWeakDerivative.lean` proves the actual L2 pairing formulas
for Schwartz tests against the compact full Green and derivative columns.
The Schwartz derivative is the actual `SchwartzMap.derivCLM`; both the
test and its derivative use their actual `toLp 2 volume` realizations.

For every positive window, every source ordinate, and every Schwartz test,
integration by parts and the existing Dirichlet endpoint values give

    inner (derivative test) greenL2 = - inner test gradientL2.

There is no support restriction on the test, and no Green denominator
hypothesis is needed for this first-derivative relation. The Green column
already has global C2 regularity, and its two endpoint values vanish.
This is the global weak derivative law for its physical zero extension.

The parent's convergent native syntheses and their pairing laws transport
that identity term by term:

    inner (derivative test) (GreenSynthesis v)
      = - inner test (GradientSynthesis v).

Thus the synthesized compact derivative vector is attached as the global
weak derivative of the synthesized Green vector. Both vectors were
constructed in physical L2 before this identity was proved. The retained
positive window, shell-data, and shell-count inputs certify series
convergence. The coefficient vector is genuinely in `lp 2`.

## Scope and outstanding attachment

This proves a native L2 weak-derivative witness, not a Weil spectral
operator-domain witness. Support of the synthesized vector, its Fourier
derivative identity, and its supported logarithmic-form-domain attachment
are not certified by this chunk. Native background completion is still
a retained written construction.

The current WD-T38 mode has not been identified with this native Green
synthesis or with the background form-completion vector. Its actual source
quadratic/null law remains unattached; same-domain mixed/normalized
attachment and enlarged-window frozen-action central cancellation remain
open. A global first-derivative identity for the native vector does not
establish that cancellation.

Current-mode membership
`MemLp (neutralWeilSpectralProduct carrier a) 2` is not derived from WD-T38
and is not assumed. This stronger route is not used to obtain the native
derivative attachment.

Once actual central cancellation is available, consume
`neutralExteriorIntegralGrowthResidual_realizes_of_central` immediately:
the certified locally integrable residual and boundary-removal route already
supply whole compact weak realization. Exterior, digamma, boundary, and
threshold work remain closed. F-4 remains pending.

## Validation

Validation commit: `60cebfa46ce526f92f1912a298f9beadde1b7020`.
GitHub Actions run `37140249307`, job `111253012042`:
root build passed (9035 jobs). All four public theorem audits use only
`propext, Classical.choice, Quot.sound`, with no `sorryAx`.
The unfinished/project-axiom declaration gate passed.
Research workflow and historical notes are preserved.
