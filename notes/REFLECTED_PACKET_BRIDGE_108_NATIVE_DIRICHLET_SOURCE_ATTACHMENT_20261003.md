# RPB-108 — actual native Dirichlet source attachment (2026-10-03)

Parent: `bead3b17bafd5a8cf14144a4ac262f08ffe898a9`.
Cursor: WD-T38 actual source/null witness attachment; F-4 pending.
Threshold bookkeeping is closed.

## Concrete source certified

`NeutralLogDirichletSourceAttachment.lean` uses the existing actual
`dirichletProblemOneColumn a z`, including both Dirichlet endpoint corrections.
It constructs its compact-window physical L2 column from continuity and compact
integration, and proves its exact first-antilinear integral pairing. Applying
the actual physical inclusion adjoint constructs its form Riesz representative
in the already complete supported logarithmic Hilbert carrier.

For the existing nonresonance condition `problemOneGreenDenom z ≠ 0`, the
existing differential Green equation proves that the compact differential
source is exactly `neutralExponentialColumn a z`. Thus its physical L2
membership is established directly, and the existing actual raw source form
representative pairs against every vector in the logarithmic carrier as

```math
\langle r_z,f\rangle_{\log}
=\int_{-a}^{a}\overline{L_a g_{a,z}(x)}\,f_{\mathrm{phys}}(x)\,dx
=F_{f_{\mathrm{phys}}}(\bar z).
```

Here `g_{a,z}` is the full actual Green column. This is an actual differential
source identity on the same domain, with no assumed representation equality.
It does not replace the full Green column by its scalar resolvent factor.
No positivity, zero-counting, selected packet, or Weil spectral-domain
hypothesis is added.

## Precise remaining witness gaps

This constructs individual native Green/source columns, not the bounded native
Green operator or its square root, and not an integration-by-parts theorem.
The column's physical L2 membership is distinct from membership of
`neutralWeilSpectralProduct carrier a` in L2. The latter is neither derived
from WD-T38 nor assumed here.

The current WD-T38 abstract `P,C,k,Q,density,extend` fields still lack an actual
zeta/native model identification with this concrete form. In particular this
does not prove that the current density is the Fourier energy density of the
physical carrier, that its scalar pole term is the actual complex cross-pole
form, or that its null vector gives the actual same-domain quadratic null.
The already proved diagonal/polarization and normalized bridges remain
available once that identification is supplied.

The retained written native background construction, strict positivity,
completion argument, and coefficient dictionary remain retained/written rather
than newly Lean-certified actual WD-T38 witnesses. The actual physical Garding
estimate was certified at the parent; strict background coercivity is not
inferred from it.

Enlarged central cancellation on all compact Schwartz tests in `(-a,a)`
remains open. The already certified inner-collar route produces a locally
integrable actual residual and consumes boundary removal immediately once
that central witness is attached, without requiring spectral L2. No exterior,
digamma, boundary, or threshold work is reopened. F-4 logarithmic Gaussian
coercivity, WD-T40, and RH remain open.

## Validation

Validation: `5ea502a1b601420846ad908a5d7834c3c5f8dac7`, [run 37133188266](https://github.com/monocap-tech/weil-lab/actions/runs/37133188266), job `111232254587`. Whole-root `lake build WeilDefect` passed (9,029 jobs). All six public theorem axiom audits reported only `[propext, Classical.choice, Quot.sound]`; unfinished/project-axiom gate passed. Research workflow and historical notes remain unchanged.
