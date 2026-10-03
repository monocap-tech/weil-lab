# RPB-108 — actual native Dirichlet coordinate summability (2026-10-03)

Parent: `7e1cd8537a3c16d3c217e66df1ed502441fb50be`.
Cursor: WD-T38 actual source/quadratic/null attachment; F-4 pending.
Threshold bookkeeping is closed.

## Proved witnesses

`NeutralNativeDirichletSummability.lean` consumes the retained WD-T28
positive Dirichlet-energy summability and the concrete native L2 coordinates
from the parent chunk. For every supplied actual shell ordinate, the
previously certified nonresonance theorem permits the exact identification

    DirichletEnergy(gamma)
      = norm(gradientL2_gamma)^2 + (1/4) norm(greenL2_gamma)^2.

Consequently the sum of these concrete coordinate energies is summable.
Nonnegativity separately bounds the derivative norm squared by the retained
energy and the Green norm squared by four times that energy. Both actual
families are therefore square summable. Every column is the full
endpoint-corrected Green column, not its raw exponential approximation.

The hypotheses are the existing positive window, `ActualProblemOneShellData`,
and `ZetaZeroShellCountData`. The result introduces no assumed source
representation, no new regularity premise, and no unspecified column norm.

## Scope of attachment

This is an actual coordinate witness for the retained native shell model.
It provides square summability required for native analysis/synthesis and
completion, but does not itself construct those operators or the background
completion. The shell-data and shell-count records remain explicit inputs;
this chunk does not manufacture an actual-zeta instance of those records.

The current WD-T38 physical carrier remains independently parameterized.
Its equality with the retained native form-completion vector, logarithmic
energy, and actual source quadratic/null law remain open. The current-mode
diagonal-to-mixed and normalized comparison attachments cannot be claimed
until those source witnesses are attached.

No enlarged-window central cancellation is proved here. Once available,
`neutralExteriorIntegralGrowthResidual_realizes_of_central` supplies the
locally integrable actual residual, boundary removal, and whole compact
weak realization. No exterior, digamma, boundary, or threshold reopening
is needed.

Actual current-mode membership
`MemLp (neutralWeilSpectralProduct carrier a) 2` is not derived from WD-T38
and is not assumed. Square summability of these actual smooth native column
families does not imply spectral membership of the unidentified current
physical mode. F-4 logarithmic Gaussian coercivity remains pending.

## Validation

Validation commit: `004a7acfc8937d1988a58a1575d428e95ba17451`.
GitHub Actions run `37138864918`, job `111248947986`:
root build passed (9033 jobs). All four public theorem audits use only
`propext, Classical.choice, Quot.sound`, with no `sorryAx`.
The unfinished/project-axiom declaration gate passed.
Research workflow and historical notes are preserved.
