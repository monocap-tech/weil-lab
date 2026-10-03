# RPB-108 — concrete native Dirichlet L2 coordinates (2026-10-03)

Parent: `e22564aa10df22ff1dcb508bd319a0737182f49a`.
Cursor: WD-T38 actual source/quadratic/null attachment; F-4 pending.
Threshold bookkeeping is closed.

## Proved concrete witnesses

`NeutralNativeDirichletCoordinates.lean` constructs the actual compact
derivative column of the full endpoint-corrected native Green column.
Global C2 regularity already certified in `DirichletEnergy.lean` gives its
physical L2 membership, without an operator-domain premise for the WD-T38 mode.

Both the derivative and Green columns have actual mixed L2 pairings equal
to the corresponding integrals on the same closed window. The existing
mixed Green identity is thereby attached to concrete physical coordinates:

    integral conj(e_z) g_w
      = inner gradientL2_z gradientL2_w
        + (1/4) inner greenL2_z greenL2_w.

For a positive window and the retained nonzero source Green denominator,
the existing native diagonal energy is exactly

    problemOneColumnEnergySq a z
      = norm(gradientL2_z)^2 + (1/4) norm(greenL2_z)^2.

This realizes the native column energy in actual L2 coordinates. It adds
no assumed representation equality, no arbitrary source operator, and no
new spectral hypothesis. The mixed identity uses the already certified
source differential equation and endpoint cancellation.

## Retained and open witnesses

The native coefficient/background-completion dictionary remains a retained
written construction. The current WD-T38 physical mode has not yet been
identified with that native form-completion vector. Its actual supported
logarithmic energy and source quadratic/null identity remain unattached.
Consequently same-domain current-mode mixed nullity, normalized comparison
attachment, and enlarged-window central cancellation remain open.

Actual membership
`MemLp (neutralWeilSpectralProduct carrier a) 2` is not derived from WD-T38
and is not assumed here. L2 membership of these smooth compact native
columns is a different, explicitly constructed witness; it cannot be
substituted for current-mode spectral membership.

The certified locally integrable residual route already suffices once
actual central cancellation is attached:
`neutralExteriorIntegralGrowthResidual_realizes_of_central` constructs
the regular residual and consumes boundary removal. Exterior, digamma,
boundary, and threshold work is not reopened. F-4 is still pending.

## Validation

Validation commit: `152663d9888a1db83a8379213f4f62140886dc33`.
GitHub Actions run `37137395365`, job `111244596498`:
root build passed (9032 jobs); all five public theorem audits use only
`propext, Classical.choice, Quot.sound`; no `sorryAx`.
The unfinished/project-axiom declaration gate passed.
Research workflow and historical notes are preserved.
