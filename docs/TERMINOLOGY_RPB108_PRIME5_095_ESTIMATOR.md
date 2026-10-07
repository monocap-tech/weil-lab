# RPB108: complete Gram and scalar-estimator decision at 19/20

The retained space is the span of the first 84 physical orthonormal Legendre
vectors on (-19/20,19/20). Q84 denotes its actual native restriction, not a
surrogate Gram and not the full native form on the infinite-dimensional domain.
The actual residual source map B is projected orthogonally away from these
same 84 vectors. R denotes B*B in retained coefficient coordinates.

The complete nine-panel surrogate residual Gram Rtilde retains every smooth,
endpoint-log and mixed contraction. The source map error eta and a certified
surrogate map norm upper M give the exact error allowance
delta=eta(2M+eta), so ||R-Rtilde||<=delta. A finite native restriction and
partial panel accumulation cannot replace this complete bound.

A scalar physical complement lower bound c>0 gives the sufficient corrected
retained estimator Q84-(Rtilde+delta I)/c. Positive corrected pivots can be
converted to a whole-domain bound only after the full source, complement,
normalization and exact conversion checks.

Conversely, a rational retained vector v with

    upper(Q84[v])-lower(Rtilde[v])/c+delta||v||^2/c < 0

certifies failure of this scalar estimator even after allowing the favorable
source-error correction. The necessary scalar complement value along that
direction is at least

    (lower(Rtilde[v])-delta||v||^2)/upper(Q84[v]).

This is not a negative witness for the actual full native form. In particular,
the same v can have strictly positive native finite energy. A lower bound c
is not the actual complement operator: failure of its scalar substitution
does not show failure of positivity at the aperture. It calls for a stronger
lawful estimate, finer coupling/complement information, or a revised retained
space, with fresh certificates and definitions before their first use.

Decimal arithmetic may locate a candidate but is not proof evidence. The
candidate must be stored rationally and verified by outward rational bounds
and a separate exact signed-endpoint audit. Historical aperture data are not
substituted. Whole-domain, global/F4 and Lean standing change only when their
respective certificates have actually closed.

## Proposed next test: positive weighted Schur bound

A proposed auxiliary weight w is a positive bounded measurable function on
the window, bounded away from zero. For the actual self-adjoint combined
prime translation operator T, an independently checked pointwise inequality
Tw<=b w gives ||T||<=b by the weighted positive-kernel Schur test. This does
not require T to be positive semidefinite, nor w to be a native form-domain
vector. A finite piecewise-constant w would require exact support and
translated-cell refinement, outward amplitude bounds, and checks on every
open refined cell; finitely many boundary points are null sets.

No such weight or improved b is certified by the current Gram decision. This
is the next proposed test for sharpening the prime loss while keeping the
completed 84-vector Gram. Any new complement must be separately certified
and its corrected sign rerun. If this route is insufficient, revising the
retained space requires fresh finite/source/Gram custody.
