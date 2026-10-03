# RPB-108 — actual mixed native Green identity and reciprocity (2026-10-03)

Parent: `ea23d3bffdf941f661cf52a4290866ebe2fcedef`.
Cursor: WD-T38 actual source/quadratic/null attachment; F-4 pending.
Threshold bookkeeping is closed.

## Existing diagonal recovered

`DirichletEnergy.lean` already certifies global C2 regularity, diagonal
integration by parts, positive real Dirichlet energy, the equality
`problemOneColumnEnergySq = problemOneDirichletEnergy` in a positive window
with nonzero Green denominator, and positive-energy summability under the
explicit shell-count/ordinate-data inputs. The deferred comment in the older
`DirichletResolvent.lean` was not evidence that this theorem remained open.
No duplicate definition or diagonal proof is promoted.

## New actual mixed source witness

`DirichletGreenMixed.lean` imports that existing energy module and proves,
for the full endpoint-corrected actual Green columns,

    integral conj(e_z) g_w
      = integral conj(g_z') g_w' + (1/4) integral conj(g_z) g_w.

Every integral is on the same oriented window `-a..a`. Here e_z is the
retained native exponential source and g_z is the full actual Dirichlet
Green column. The law uses `a ≠ 0` and the existing nonresonance condition
`problemOneGreenDenom z ≠ 0`. It requires no nonresonance for w, whose role
uses smoothness and its exact Dirichlet endpoint values. Convergence and
integration by parts use the existing genuine C2 column regularity.

For both nonresonant ordinates, the actual source/Green pairing obeys

    integral conj(e_z) g_w = conj(integral conj(e_w) g_z).

Thus native mixed source reciprocity is certified for distinct columns,
without assuming a Green operator, self-adjointness field, or representation
equality. On the diagonal the new mixed expression agrees exactly with the
existing `problemOneDirichletEnergy`; there is only one energy definition.
The full endpoint corrections are retained throughout.

Pinned mathlib integration-by-parts and conjugate interval-integration APIs
were checked directly at `5ed2965256430c3649e86755f9576b54eca72435`.

## Remaining actual-instance gap

Column reciprocity is not the bounded native Green operator/square root,
native Hilbert completion, infinite actual-zeta synthesis, strict background
positivity, or a current WD-T38 model instance. The existing native positive-
energy summability still has explicit shell-count and ordinate-data inputs;
this pass does not instantiate them for all actual zeta zeros.

The actual linear source-domain lift, logarithmic norm, and exact existing
source quadratic/mixed realization were certified at the parent. Present
generic WD-T38 fields still need identification with the actual model and an
actual physical logarithmic-energy/null witness. Their named density is not
automatically the Fourier norm-square density of their physical carrier.
The already certified zero-density reindex audit records this independence.

Native background completion and the endpoint-null argument remain retained/
written. Enlarged central cancellation for every compact Schwartz test
supported in `(-a,a)` remains open.

Actual Weil spectral L2 membership is unproved from WD-T38 and unassumed.
Native column Dirichlet energy is not that current-mode membership. Once
actual enlarged central cancellation is attached, the existing inner-collar
theorem supplies the locally integrable defect, boundary removal, and whole
compact weak realization without spectral L2.

No existing exterior/digamma/residual-boundary or threshold work is reopened.
F-4 logarithmic Gaussian coercivity, WD-T40, and RH remain open.

## Validation

Validation: `41b1606db89ae51d8ce819b28985002988d64346`, [run 37136385069](https://github.com/monocap-tech/weil-lab/actions/runs/37136385069), job `111241663248`. Whole-root `lake build WeilDefect` passed (9,031 jobs). All three public theorem axiom audits reported only `[propext, Classical.choice, Quot.sound]`; unfinished/project-axiom gate passed. Research workflow and historical notes remain unchanged.
