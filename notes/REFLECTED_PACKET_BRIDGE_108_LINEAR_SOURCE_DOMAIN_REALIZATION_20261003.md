# RPB-108 — actual linear source-domain realization (2026-10-03)

Parent: `f079d9aec01743905d3897bfb0283f6da05be14c`.
Cursor: WD-T38 actual source/quadratic/null witness attachment; F-4 pending.
Threshold bookkeeping is closed.

## Actual component proved

`NeutralLogSourceDomainRealization.lean` strengthens the already certified
canonical-domain correspondence to a complex-linear equivalence from the
complete logarithmic Hilbert carrier to the full supported finite-logarithmic-
energy submodule of physical L2. Its inverse is the actual Fourier weighting
construction, not an assumed source representation.

Every existing lawful `NeutralSourceFormDomainAttachment D` now has an actual
injective complex-linear lift into that complete carrier. The physical vector
is preserved exactly, and the lifted squared norm is precisely the actual
logarithmic Fourier energy of the original vector. In particular the
distinguished `carrier.l2Mode` in D remains that same physical mode.

The canonical-domain subtype and D retain their ordinary physical L2 norms.
The new equivalence/lift is a LinearEquiv/LinearMap, not an asserted bounded
inverse or equivalence of these norms. Completeness belongs to the logarithmic
Hilbert carrier. No operator-domain L2 regularity is inferred.

Under the existing retained temperateness and normalized lower/upper shifted
symbol estimates, the actual concrete multiplier-plus-pole operator has:
- exactly the existing `sourceDomainWeilFormFromShiftedComparison D` as its
  mixed pairing on the lifted domain;
- exactly the existing real `sourceDomainQuadratic D` as its diagonal.

These equalities are proved using the actual integral and cross-pole formulas.
No new representation equality, positivity, null identity, spectral membership,
or density identification is assumed. Both slots remain on the same lawful
source domain. Because the lift is linear, the existing source-domain
polarization theorem uses the same sums and complex scalings after lifting;
no enlargement of the physical domain occurs.

## What this does not attach

The actual physical-to-form realization is certified. The present generic
WD-T38 instance still needs its own actual finite-logarithmic-energy custody
and identification of its imported quadratic/null with this concrete source
quadratic. The existing independent density/scalar pole fields do not supply
that identification. This theorem neither constructs D for that current
instance nor declares its imported null to be the actual Weil null.

The retained native background/Green square-root model and strict completion
construction remain retained/written. The individual actual Dirichlet source
columns and their differential source were certified at the parent, but do
not by themselves identify current `P,C,k,Q,density,extend`.

Enlarged central cancellation on every compact Schwartz test supported in
`(-a,a)` is still open. The already certified inner-collar theorem supplies
the locally integrable actual residual, boundary removal, and whole compact
weak realization as soon as that central witness is obtained. No exterior,
digamma, boundary, or threshold work is reopened.

Spectral L2 membership of `neutralWeilSpectralProduct carrier a` has not been
derived from WD-T38 and is not assumed. Logarithmic energy is not upgraded to
that stronger domain. F-4 logarithmic Gaussian coercivity, WD-T40, and RH remain
open.

## Validation

Validation: `a9f7686f1512fb4841650a20782529757c364643`, [run 37134529034](https://github.com/monocap-tech/weil-lab/actions/runs/37134529034), job `111236237732`. Whole-root `lake build WeilDefect` passed (9,030 jobs). All seven public declaration axiom audits reported only `[propext, Classical.choice, Quot.sound]`; unfinished/project-axiom gate passed. Research workflow and historical notes remain unchanged.
